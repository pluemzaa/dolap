#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Clustering Pipeline — CodeT5 (T5EncoderModel) + K-Means
- อ่านไฟล์ .py ทั้งโฟลเดอร์ (recursive)
- ทำความสะอาดด้วย AST (ลบคอมเมนต์/ดอคสตริง + รีเนมตัวแปร/ฟังก์ชัน)
- ฝังความหมายด้วย CodeT5 (encoder-only) หรือ TF-IDF fallback (+ตัวเลือก SVD ลดมิติ)
- จัดกลุ่มด้วย K-Means (auto-k หรือกำหนดเอง)
- บันทึกผล: clusters.csv, clusters_pca.png, clusters_summary.txt, exemplars/, logs.txt
"""

import argparse
import ast
import glob
import json
import os
import re
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# ------------------------- Logging -------------------------

class Logger:
    def __init__(self, out_path: Path):
        self.out_path = out_path
        self.buf: List[str] = []

    def log(self, msg: str):
        line = str(msg).strip()
        print(line)
        self.buf.append(line + "\n")

    def save(self):
        try:
            self.out_path.write_text("".join(self.buf), encoding="utf-8")
        except Exception:
            pass

# ------------------------- File IO -------------------------

def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "latin-1", "cp1252"):
        try:
            return path.read_text(encoding=enc, errors="ignore")
        except Exception:
            continue
    return ""

def list_files(src: Path, pattern: str, max_files: Optional[int]) -> List[Path]:
    files = sorted([Path(p) for p in glob.glob(str(src / "**" / pattern), recursive=True)])
    if max_files is not None and len(files) > max_files:
        files = files[:max_files]
    return files

# ------------------------- Code Normalization -------------------------

def _unparse(tree: ast.AST) -> str:
    try:
        return ast.unparse(tree)  # Py3.9+
    except Exception:
        try:
            import astor  # type: ignore
            return astor.to_source(tree)
        except Exception:
            return ""

def strip_comments_and_docstrings(source: str) -> str:
    """ลบคอมเมนต์ + ดอคสตริงด้วย AST (มี regex สำรอง)"""
    try:
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
                if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], "value", None), ast.Str):
                    node.body[0].value.s = ""  # type: ignore
        new_src = _unparse(parsed)
        new_src = re.sub(r"[ \t]*#.*", "", new_src)
        return new_src
    except Exception:
        s = re.sub(r"'''[\s\S]*?'''", "", source)
        s = re.sub(r'"""[\s\S]*?"""', "", s)
        s = re.sub(r"[ \t]*#.*", "", s)
        return s

def simple_ast_normalize_identifiers(source: str) -> str:
    """แทนชื่อ var/func/class ด้วย x1/f1/C1 ลดผลจากการรีเนม"""
    try:
        tree = ast.parse(source)
    except Exception:
        return source

    class Renamer(ast.NodeTransformer):
        def __init__(self):
            super().__init__()
            self.map: Dict[str, str] = {}
            self.vi = self.fi = self.ci = 0

        def _map(self, name: str, kind: str) -> str:
            if name not in self.map:
                if kind == "v":
                    self.vi += 1; self.map[name] = f"x{self.vi}"
                elif kind == "f":
                    self.fi += 1; self.map[name] = f"f{self.fi}"
                elif kind == "c":
                    self.ci += 1; self.map[name] = f"C{self.ci}"
                else:
                    self.vi += 1; self.map[name] = f"x{self.vi}"
            return self.map[name]

        def visit_FunctionDef(self, node: ast.FunctionDef):
            node.name = self._map(node.name, "f"); return self.generic_visit(node)
        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
            node.name = self._map(node.name, "f"); return self.generic_visit(node)
        def visit_ClassDef(self, node: ast.ClassDef):
            node.name = self._map(node.name, "c"); return self.generic_visit(node)
        def visit_Name(self, node: ast.Name):
            node.id = self._map(node.id, "v"); return node
        def visit_arg(self, node: ast.arg):
            node.arg = self._map(node.arg, "v"); return node

    try:
        norm_tree = Renamer().visit(tree)  # type: ignore
        ast.fix_missing_locations(norm_tree)
        out = _unparse(norm_tree)
        return out if out.strip() else source
    except Exception:
        return source

def normalize_code(source: str,
                   strip_docs_comments: bool = True,
                   ast_rename_identifiers: bool = True,
                   squeeze_whitespace: bool = True) -> str:
    s = source
    if strip_docs_comments:
        s = strip_comments_and_docstrings(s)
    if ast_rename_identifiers:
        s = simple_ast_normalize_identifiers(s)
    if squeeze_whitespace:
        s = re.sub(r"[ \t]+", " ", s)
        s = re.sub(r"\n{2,}", "\n", s)
        s = s.strip()
    return s

# ------------------------- Embeddings -------------------------

def try_import_transformers_enc():
    """
    โหลดเฉพาะ AutoTokenizer + T5EncoderModel เพื่อหลีกเลี่ยง torchvision/image_utils
    """
    import torch
    from transformers import AutoTokenizer, T5EncoderModel
    return torch, AutoTokenizer, T5EncoderModel

def embed_codet5_encoder(texts: List[str], model_name: str, batch_size: int, device: str, logger: Logger) -> np.ndarray:
    """
    ใช้ T5EncoderModel เป็น encoder-only (ไม่ต้อง decoder_input_ids)
    """
    torch, AutoTokenizer, T5EncoderModel = try_import_transformers_enc()
    tok = AutoTokenizer.from_pretrained(model_name, use_fast=True, truncation_side="left")
    enc = T5EncoderModel.from_pretrained(model_name)
    enc = enc.to(device)
    enc.eval()
    logger.log(f"[Embedding] CodeT5 encoder: {model_name} on {device}")

    vecs = []
    with torch.no_grad():
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            toks = tok(batch, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
            out = enc(**toks)  # last_hidden_state: [B, L, H]
            hidden = out.last_hidden_state
            attn = toks.attention_mask.unsqueeze(-1).float()
            summed = (hidden * attn).sum(dim=1)
            counts = attn.sum(dim=1).clamp(min=1.0)
            pooled = summed / counts  # [B, H]
            vecs.append(pooled.detach().cpu().numpy())
    X = np.vstack(vecs)
    logger.log(f"[Embedding] shape={X.shape}")
    return X

def embed_tfidf_char_ngrams(texts: List[str], logger: Logger) -> np.ndarray:
    """
    TF-IDF char 3–5 grams (ทนต่อการเปลี่ยนชื่อ/รูปแบบ)
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer(analyzer="char", ngram_range=(3, 5), min_df=2, max_features=150_000)
    X = vec.fit_transform(texts).astype(np.float32)
    logger.log(f"[Embedding] TF-IDF (char3–5) sparse_shape={X.shape}")
    return X.toarray()  # KMeans ต้องใช้ dense

# ------------------------- Clustering utils -------------------------

def auto_choose_k(X: np.ndarray, k_min: int, k_max: int, seed: int, logger: Logger) -> Tuple[int, float]:
    best_k, best_score = None, -1.0
    logger.log(f"[Auto-K] search {k_min}..{k_max}")
    for k in range(k_min, k_max + 1):
        try:
            km = KMeans(n_clusters=k, n_init="auto", random_state=seed)
            labels = km.fit_predict(X)
            if len(set(labels)) == 1:
                continue
            sil = silhouette_score(X, labels, metric="euclidean")
            logger.log(f"[Auto-K] k={k} silhouette={sil:.4f}")
            if sil > best_score:
                best_k, best_score = k, sil
        except Exception as e:
            logger.log(f"[Auto-K] k={k} failed: {e}")
    if best_k is None:
        logger.log("[Auto-K] fallback k=2")
        return 2, -1.0
    return best_k, best_score

def per_cluster_exemplars(X: np.ndarray, labels: np.ndarray, files: List[Path], topn: int = 5) -> Dict[int, List[Tuple[str, float]]]:
    km = KMeans(n_clusters=len(set(labels)), n_init="auto", random_state=0).fit(X)
    centroids = km.cluster_centers_
    out: Dict[int, List[Tuple[str, float]]] = {}
    for c in sorted(set(labels)):
        idx = np.where(labels == c)[0]
        if idx.size == 0:
            out[c] = []; continue
        Xc = X[idx]
        dists = np.linalg.norm(Xc - centroids[c], axis=1)
        order = np.argsort(dists)[:topn]
        out[c] = [(str(files[idx[i]]), float(dists[order[i]])) for i in range(len(order))]
    return out

# ------------------------- Main Pipeline -------------------------

@dataclass
class Config:
    src: Path
    pattern: str = "*.py"
    max_files: Optional[int] = None
    min_lines: int = 1
    strip_docs_comments: bool = True
    ast_rename_identifiers: bool = True
    squeeze_whitespace: bool = True
    embed_model: str = "Salesforce/codet5-base"
    device: str = "cpu"            # "cpu" หรือ "cuda"
    batch_size: int = 8
    use_auto_k: bool = False
    k: Optional[int] = None
    k_min: int = 2
    k_max: int = 10
    seed: int = 42
    save_embeddings: Optional[Path] = None
    out_dir: Path = Path(".")
    exemplar_topn: int = 5
    svd_components: int = 0        # >0 จะใช้ TruncatedSVD กับ TF-IDF (เช่น 256)

def run(cfg: Config) -> None:
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    logger = Logger(cfg.out_dir / "logs.txt")
    logger.log("[Start] Code Clustering Pipeline")

    # 1) Load files
    files = list_files(cfg.src, cfg.pattern, cfg.max_files)
    logger.log(f"[Files] found {len(files)} candidate(s)")

    # 2) Normalize
    texts_norm, kept_files = [], []
    for p in files:
        s = read_text(p)
        if not s.strip():
            continue
        if s.count("\n") + 1 < cfg.min_lines:
            continue
        kept_files.append(p)
        texts_norm.append(normalize_code(
            s,
            strip_docs_comments=cfg.strip_docs_comments,
            ast_rename_identifiers=cfg.ast_rename_identifiers,
            squeeze_whitespace=cfg.squeeze_whitespace,
        ))

    if not kept_files:
        logger.log("[ERROR] no non-empty files after filtering")
        logger.save(); sys.exit(1)

    logger.log(f"[Preprocess] kept {len(kept_files)} file(s)")

    # 3) Embedding
    emb_backend = None
    try:
        X = embed_codet5_encoder(texts_norm, cfg.embed_model, cfg.batch_size, cfg.device, logger)
        emb_backend = f"CodeT5Enc:{cfg.embed_model}"
    except Exception as e:
        logger.log(f"[WARN] CodeT5 encoder failed: {e}")
        logger.log("[Fallback] TF-IDF (char 3–5)")
        X = embed_tfidf_char_ngrams(texts_norm, logger)
        if cfg.svd_components and cfg.svd_components > 0:
            try:
                logger.log(f"[SVD] Reducing TF-IDF to {cfg.svd_components} dims")
                X = TruncatedSVD(n_components=cfg.svd_components, random_state=cfg.seed).fit_transform(X)
            except Exception as e2:
                logger.log(f"[SVD] failed: {e2}")
        emb_backend = f"TFIDF(char3-5){f'+SVD{cfg.svd_components}' if cfg.svd_components else ''}"

    # 4) Scale
    scaler = StandardScaler(with_mean=True, with_std=True)
    Xs = scaler.fit_transform(X)

    # 5) k selection
    if cfg.use_auto_k and cfg.k is None:
        k, sil_auto = auto_choose_k(Xs, cfg.k_min, cfg.k_max, cfg.seed, logger)
        logger.log(f"[K] auto selected k={k} silhouette={sil_auto:.4f}")
    else:
        k = cfg.k if cfg.k is not None else 5
        logger.log(f"[K] fixed k={k}")

    # 6) KMeans
    km = KMeans(n_clusters=k, n_init="auto", random_state=cfg.seed)
    labels = km.fit_predict(Xs)

    # 7) Metrics
    sil = -1.0
    if len(set(labels)) > 1:
        try:
            sil = silhouette_score(Xs, labels, metric="euclidean")
        except Exception as e:
            logger.log(f"[Silhouette] failed: {e}")

    centroids = km.cluster_centers_
    dists = np.linalg.norm(Xs - centroids[labels], axis=1)

    # 8) Save embeddings
    if cfg.save_embeddings is not None:
        try:
            np.save(cfg.save_embeddings, X)
            logger.log(f"[Save] embeddings -> {cfg.save_embeddings}")
        except Exception as e:
            logger.log(f"[Save] embeddings failed: {e}")

    # 9) PCA plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        XY = PCA(n_components=2, random_state=cfg.seed).fit_transform(Xs)
        plt.figure(figsize=(9, 7))
        plt.scatter(XY[:, 0], XY[:, 1], s=18, c=labels)
        plt.title(f"Code Clusters (k={k}) | {emb_backend} | silhouette={sil:.3f}")
        plt.xlabel("PCA-1"); plt.ylabel("PCA-2")
        handles = [plt.Line2D([0],[0], marker='o', linestyle='', label=f"C{lb}") for lb in sorted(set(labels))]
        plt.legend(handles=handles, title="Clusters", bbox_to_anchor=(1.02,1), loc="upper left", borderaxespad=0.0)
        plt.tight_layout()
        out_png = cfg.out_dir / "clusters_pca.png"
        plt.savefig(out_png, dpi=160)
        logger.log(f"[Save] PCA plot -> {out_png}")
    except Exception as e:
        logger.log(f"[PCA] failed: {e}")

    # 10) CSV
    df = pd.DataFrame({
        "file": [str(p) for p in kept_files],
        "cluster": labels,
        "centroid_distance": dists
    })
    counts = df["cluster"].value_counts().to_dict()
    df["cluster_size"] = df["cluster"].map(counts)
    df["embedding"] = emb_backend
    df["silhouette_overall"] = sil
    out_csv = cfg.out_dir / "clusters.csv"
    df.to_csv(out_csv, index=False, encoding="utf-8")
    logger.log(f"[Save] clusters -> {out_csv}")

    # 11) Exemplars
    exemplar_dir = cfg.out_dir / "exemplars"
    exemplar_dir.mkdir(parents=True, exist_ok=True)
    ex = per_cluster_exemplars(Xs, labels, kept_files, topn=cfg.exemplar_topn)
    for c, items in ex.items():
        lines = [f"# Cluster {c} | top {cfg.exemplar_topn} closest to centroid"]
        for fpath, dist in items:
            lines.append(f"{dist:10.6f}  {fpath}")
        (exemplar_dir / f"cluster_{c:02d}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 12) Summary
    summary = {
        "n_files": int(len(kept_files)),
        "embedding": emb_backend,
        "k": int(k),
        "silhouette_overall": float(sil),
        "clusters": {int(c): int(cnt) for c, cnt in sorted(counts.items())},
        "config": {
            "strip_docs_comments": cfg.strip_docs_comments,
            "ast_rename_identifiers": cfg.ast_rename_identifiers,
            "squeeze_whitespace": cfg.squeeze_whitespace,
            "pattern": cfg.pattern,
            "min_lines": cfg.min_lines,
            "svd_components": cfg.svd_components
        }
    }
    out_txt = cfg.out_dir / "clusters_summary.txt"
    out_txt.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.log(f"[Save] summary -> {out_txt}")

    logger.log("[Done]")
    logger.save()

# ------------------------- CLI -------------------------

def parse_args() -> Config:
    ap = argparse.ArgumentParser(description="Cluster Python files using CodeT5 (T5EncoderModel) with K-Means (TF-IDF fallback).")
    ap.add_argument("--src", type=str, required=True, help="root folder containing .py (recursive)")
    ap.add_argument("--pattern", type=str, default="*.py", help="glob pattern")
    ap.add_argument("--max-files", type=int, default=None, help="limit number of files")
    ap.add_argument("--min-lines", type=int, default=1, help="skip files with < min_lines")

    ap.add_argument("--strip-docs-comments", action="store_true")
    ap.add_argument("--no-strip-docs-comments", dest="strip_docs_comments", action="store_false")
    ap.set_defaults(strip_docs_comments=True)

    ap.add_argument("--ast-rename-identifiers", action="store_true")
    ap.add_argument("--no-ast-rename-identifiers", dest="ast_rename_identifiers", action="store_false")
    ap.set_defaults(ast_rename_identifiers=True)

    ap.add_argument("--squeeze-whitespace", action="store_true")
    ap.add_argument("--no-squeeze-whitespace", dest="squeeze_whitespace", action="store_false")
    ap.set_defaults(squeeze_whitespace=True)

    ap.add_argument("--model", type=str, default="Salesforce/codet5-base", help="HuggingFace model name")
    ap.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--batch-size", type=int, default=8)

    ap.add_argument("--k", type=int, default=None, help="number of clusters (ignored if --auto-k)")
    ap.add_argument("--auto-k", action="store_true", help="search k by silhouette")
    ap.add_argument("--k-min", type=int, default=2)
    ap.add_argument("--k-max", type=int, default=10)
    ap.add_argument("--seed", type=int, default=42)

    ap.add_argument("--save-embeddings", type=str, default=None, help="path *.npy to save embeddings")
    ap.add_argument("--out-dir", type=str, default=".", help="output directory")
    ap.add_argument("--exemplar-topn", type=int, default=5)
    ap.add_argument("--svd", type=int, default=0, help="TF-IDF SVD components (0=off, e.g., 256)")

    args = ap.parse_args()

    return Config(
        src=Path(args.src).expanduser().resolve(),
        pattern=args.pattern,
        max_files=args.max_files,
        min_lines=args.min_lines,
        strip_docs_comments=args.strip_docs_comments,
        ast_rename_identifiers=args.ast_rename_identifiers,
        squeeze_whitespace=args.squeeze_whitespace,
        embed_model=args.model,
        device=args.device,
        batch_size=args.batch_size,
        use_auto_k=bool(args.auto_k),
        k=args.k,
        k_min=args.k_min,
        k_max=args.k_max,
        seed=args.seed,
        save_embeddings=(Path(args.save_embeddings).expanduser().resolve() if args.save_embeddings else None),
        out_dir=Path(args.out_dir).expanduser().resolve(),
        exemplar_topn=args.exemplar_topn,
        svd_components=int(args.svd)
    )

if __name__ == "__main__":
    cfg = parse_args()
    run(cfg)
