# predict.py — multi-label grading (single file or folder) with per-label thresholds
import os, json
from pathlib import Path
from typing import List, Dict, Optional
import torch
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ============== CONFIG (แก้ได้ตามต้องการ) ==============
# โฟลเดอร์โมเดลที่เซฟจากสคริปต์เทรน (มี best_model/, labels.json, best_thresholds.json)
MODEL_ROOT = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\model_codebert_20e_8b_m512")

# โหมดทำนาย: เลือกอย่างใดอย่างหนึ่ง
INPUT_FILE: Optional[Path] = None #Path(r"D:\GitHub\dolap\files_dolab\files\some_student.py")  # ไฟล์เดียว
INPUT_DIR:  Optional[Path] = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\test_data")  # หรือกำหนดเป็นโฟลเดอร์ที่จะสแกน *.py

# ตั้งค่าทั่วไป
MAX_LEN = 512
FILENAME_GLOB = "*.py"   # ใช้เมื่อ INPUT_DIR ไม่ใช่ None
THRESH_FALLBACK = 0.5    # ถ้าไม่มี best_thresholds.json จะใช้ค่านี้ทุกป้าย
OUT_CSV = MODEL_ROOT / "predictions.csv"  # สำหรับโหมดโฟลเดอร์
# =========================================================

def load_model_and_meta(model_root: Path):
    model_dir = model_root / "best_model"
    labels = json.loads((model_dir / "labels.json").read_text(encoding="utf-8"))
    tok = AutoTokenizer.from_pretrained(str(model_dir))
    model = AutoModelForSequenceClassification.from_pretrained(str(model_dir))
    # thresholds
    th_path = model_root / "best_thresholds.json"
    if th_path.exists():
        best_th = json.loads(th_path.read_text(encoding="utf-8"))
        thr = np.array([best_th.get(lb, THRESH_FALLBACK) for lb in labels], dtype=float)
    else:
        thr = np.array([THRESH_FALLBACK] * len(labels), dtype=float)
    return model, tok, labels, thr

@torch.no_grad()
def predict_one(py_path: Path, model, tok, labels: List[str], thr: np.ndarray, max_len: int = 512):
    code = py_path.read_text(encoding="utf-8", errors="ignore")
    enc = tok(code, truncation=True, max_length=max_len, return_tensors="pt")
    logits = model(**enc).logits.squeeze(0)  # [num_labels]
    probs = torch.sigmoid(logits).numpy()
    yhat = (probs >= thr).astype(int)
    active = [lb for lb, v in zip(labels, yhat) if v == 1]
    if not active:
        active = ["ok"]  # ไม่มีป้ายไหนติด → ok
    return probs, yhat, active

def main():
    if INPUT_FILE is None and INPUT_DIR is None:
        raise SystemExit("กรุณากำหนด INPUT_FILE หรือ INPUT_DIR อย่างใดอย่างหนึ่งในส่วน CONFIG")

    model, tok, labels, thr = load_model_and_meta(MODEL_ROOT)
    print("Loaded labels:", labels)
    print("Using thresholds:", {lb: float(t) for lb, t in zip(labels, thr)})

    if INPUT_FILE:
        probs, yhat, active = predict_one(INPUT_FILE, model, tok, labels, thr, MAX_LEN)
        print("\n=== RESULT (single file) ===")
        print("File       :", str(INPUT_FILE))
        print("Probabilities:", {lb: float(p) for lb, p in zip(labels, probs)})
        print("Predicted  :", active)
        return

    # Folder mode
    paths = sorted(INPUT_DIR.rglob(FILENAME_GLOB)) if "**" in FILENAME_GLOB else sorted(INPUT_DIR.glob(FILENAME_GLOB))
    rows = []
    for p in paths:
        if not p.is_file() or p.suffix.lower() != ".py":
            continue
        probs, yhat, active = predict_one(p, model, tok, labels, thr, MAX_LEN)
        row = {
            "path": str(p),
            "pred_labels": ";".join(active),
        }
        for lb, pr, yh in zip(labels, probs, yhat):
            row[f"prob_{lb}"] = float(pr)
            row[f"pred_{lb}"] = int(yh)
        rows.append(row)

    if not rows:
        print("ไม่พบไฟล์ .py ตามแพทเทิร์นในโฟลเดอร์ที่กำหนด")
        return

    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
    print(f"\nSaved predictions to: {OUT_CSV}")
    # แสดงตัวอย่าง 5 แถว
    print(df.head(5).to_string(index=False))

if __name__ == "__main__":
    main()
