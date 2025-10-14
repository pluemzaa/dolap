# train_hf_multilabel.py — robust + class weight + per-label threshold + extra metrics & CM
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TRANSFORMERS_NO_FLAX"] = "1"
# os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"  # ลด warning บน Windows (ไม่บังคับ)

import json, random
from pathlib import Path
from typing import List, Dict

import numpy as np
import torch
import torch.nn.functional as F
import pandas as pd
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    f1_score,
    classification_report,
    accuracy_score,
    hamming_loss,
    multilabel_confusion_matrix,
)

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
)

import matplotlib
matplotlib.use("Agg")  # เผื่อไม่มี display
import matplotlib.pyplot as plt

# ====== CONFIG ======
CSV_PATH = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\data_labeled\dataset.csv")
MODEL_NAME = "huggingface/CodeBERTa-small-v1"  # "microsoft/codebert-base"  # "microsoft/unixcoder-base"
OUT_DIR   = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\model_CodeBERTa-small-v1_20e_8b_m512")

LABELS  = ["inputError", "processError", "outputError"]
MAX_LEN = 512
BATCH   = 8
EPOCHS  = 20
LR      = 5e-5

TEST_SIZE = 0.15
VAL_SIZE  = 0.15
SEED      = 123
# =====================

random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)

class CodeDataset(Dataset):
    def __init__(self, df: pd.DataFrame, tokenizer, max_len: int):
        self.df = df.reset_index(drop=True)
        self.tok = tokenizer
        self.max_len = max_len
    def __len__(self): 
        return len(self.df)
    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        code = Path(row["path"]).read_text(encoding="utf-8", errors="ignore")
        # ทำ truncation ที่นี่ (เวอร์ชันเก่าของ tok.pad ไม่รับพารามิเตอร์นี้)
        enc = self.tok(code, truncation=True, max_length=self.max_len)
        enc["labels"] = [float(row[l]) for l in LABELS]  # ให้ collator เป็นคน stack
        return enc

def compute_metrics(eval_pred):
    logits, labels = (eval_pred if isinstance(eval_pred, tuple)
                      else (eval_pred.predictions, eval_pred.label_ids))
    probs = torch.sigmoid(torch.tensor(logits)).numpy()
    y_pred = (probs >= 0.5).astype(int)
    y_true = np.asarray(labels)
    return {
        "micro_f1": f1_score(y_true, y_pred, average="micro", zero_division=0),
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
    }

def make_training_args():
    base = dict(
        output_dir=str(OUT_DIR / "runs"),
        learning_rate=LR,
        per_device_train_batch_size=BATCH,
        per_device_eval_batch_size=BATCH,
        num_train_epochs=EPOCHS,
        logging_steps=50,
        report_to=[],
        seed=SEED,
    )
    try:
        return TrainingArguments(
            **base,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            metric_for_best_model="macro_f1",
            greater_is_better=True,
        )
    except TypeError:
        return TrainingArguments(**base)

def main():
    # ---------- 1) Load & split ----------
    df = pd.read_csv(CSV_PATH)
    ids = df["id"].unique().tolist()
    train_ids, test_ids = train_test_split(ids, test_size=TEST_SIZE, random_state=SEED)
    train_ids, val_ids  = train_test_split(train_ids, test_size=VAL_SIZE/(1-TEST_SIZE), random_state=SEED)
    tr_df, va_df, te_df = (df[df["id"].isin(s)].copy() for s in (train_ids, val_ids, test_ids))
    print(f"Train: {len(tr_df)}  Val: {len(va_df)}  Test: {len(te_df)}")

    # ---------- 2) Tokenizer & Model ----------
    tok = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=len(LABELS))
    try:
        model.config.problem_type = "multi_label_classification"
    except Exception:
        pass

    # ---------- 3) Datasets ----------
    train_ds, val_ds, test_ds = (CodeDataset(d, tok, MAX_LEN) for d in (tr_df, va_df, te_df))

    # ---------- 4) Custom collator ----------
    def collate_fn(batch: List[Dict]):
        labels = [item.pop("labels") for item in batch]
        padded = tok.pad(batch, padding=True, return_tensors="pt")  # เวอร์ชันเก่า: ห้ามส่ง truncation/max_length
        padded["labels"] = torch.tensor(labels, dtype=torch.float)
        return padded

    # ---------- 5) Class weights (pos_weight) ----------
    # pos_weight = (neg/pos) ต่อป้าย จาก TRAIN SET
    pos_counts = tr_df[LABELS].sum(axis=0).values.astype(float) + 1e-6
    neg_counts = len(tr_df) - pos_counts + 1e-6
    pos_weight_vec = torch.tensor(neg_counts / pos_counts, dtype=torch.float)
    print("pos_weight:", {lb: float(w) for lb, w in zip(LABELS, pos_weight_vec)})

    # ---------- 6) Weighted Trainer ----------
    class WeightedBCETrainer(Trainer):
        # รองรับ signature ใหม่: มี num_items_in_batch/kwargs
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            labels = inputs.pop("labels")
            outputs = model(**inputs)
            logits = outputs.logits
            # ให้แน่ใจว่า labels เป็น float tensor [B, num_labels]
            if not torch.is_tensor(labels):
                labels = torch.tensor(labels, dtype=torch.float, device=logits.device)
            else:
                labels = labels.to(dtype=torch.float, device=logits.device)
            loss = F.binary_cross_entropy_with_logits(
                logits, labels, pos_weight=pos_weight_vec.to(logits.device)
            )
            return (loss, outputs) if return_outputs else loss

    args = make_training_args()
    trainer = WeightedBCETrainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=collate_fn,
        compute_metrics=compute_metrics,
    )

    # ---------- 7) Train & Eval ----------
    trainer.train()
    try:
        print("\n=== Val metrics ===", trainer.evaluate())
    except Exception:
        pass

    # ---------- 8) Threshold tuning on VAL (per-label) ----------
    val_preds  = trainer.predict(val_ds)
    val_probs  = torch.sigmoid(torch.tensor(val_preds.predictions)).numpy()
    val_true   = va_df[LABELS].values

    best_th = {}
    for j, lb in enumerate(LABELS):
        y = val_true[:, j]; p = val_probs[:, j]
        best_f1, best_t = -1.0, 0.5
        for t in np.linspace(0.1, 0.9, 81):
            yhat = (p >= t).astype(int)
            f1 = f1_score(y, yhat, zero_division=0)
            if f1 > best_f1:
                best_f1, best_t = f1, t
        best_th[lb] = float(best_t)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "best_thresholds.json").write_text(json.dumps(best_th, indent=2), encoding="utf-8")
    print("Best thresholds (from VAL):", best_th)

    # ---------- 9) Test & Extra Metrics ----------
    test_preds = trainer.predict(test_ds)
    test_probs = torch.sigmoid(torch.tensor(test_preds.predictions)).numpy()
    y_true     = te_df[LABELS].values

    # ใช้ threshold ต่อป้าย
    y_pred = np.zeros_like(test_probs, dtype=int)
    for j, lb in enumerate(LABELS):
        th = best_th.get(lb, 0.5)
        y_pred[:, j] = (test_probs[:, j] >= th).astype(int)

    micro_f1 = f1_score(y_true, y_pred, average="micro", zero_division=0)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    subset_acc  = accuracy_score(y_true, y_pred)         # exact match
    hamming_acc = 1.0 - hamming_loss(y_true, y_pred)     # ต่อป้าย

    # Per-label accuracy
    per_label_acc = {}
    for j, lb in enumerate(LABELS):
        tn = np.sum((y_true[:, j] == 0) & (y_pred[:, j] == 0))
        tp = np.sum((y_true[:, j] == 1) & (y_pred[:, j] == 1))
        fn = np.sum((y_true[:, j] == 1) & (y_pred[:, j] == 0))
        fp = np.sum((y_true[:, j] == 0) & (y_pred[:, j] == 1))
        per_label_acc[lb] = (tp + tn) / (tp + tn + fp + fn + 1e-12)

    print("\n=== Test metrics (with tuned thresholds) ===")
    print("micro_f1               :", micro_f1)
    print("macro_f1               :", macro_f1)
    print("subset_accuracy        :", subset_acc)
    print("hamming_accuracy       :", hamming_acc)
    print("\nPer-label accuracy:")
    for lb in LABELS:
        print(f" - {lb:12s}: {per_label_acc[lb]:.4f}")

    report_txt = classification_report(y_true, y_pred, target_names=LABELS, zero_division=0)
    print("\nPer-label report:\n", report_txt)
    (OUT_DIR / "test_classification_report.txt").write_text(report_txt, encoding="utf-8")

    # ---------- 10) Confusion matrices (multi-label: one per label) ----------
    cms = multilabel_confusion_matrix(y_true, y_pred, labels=[0, 1, 2])
    for idx, lb in enumerate(LABELS):
        cm = cms[idx]  # [[TN, FP],[FN, TP]]
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.imshow(cm)
        ax.set_title(f"Confusion Matrix — {lb}")
        ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
        ax.set_xticklabels(["Pred 0", "Pred 1"])
        ax.set_yticklabels(["True 0", "True 1"])
        for (i, j), val in np.ndenumerate(cm):
            ax.text(j, i, int(val), ha="center", va="center")
        ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
        fig.tight_layout()
        fig.savefig(OUT_DIR / f"confusion_matrix_{lb}.png", dpi=150)
        plt.close(fig)

    # ---------- 11) Save model & artifacts ----------
    save_dir = OUT_DIR / "best_model"
    save_dir.mkdir(parents=True, exist_ok=True)
    try:
        trainer.save_model(str(save_dir))
    except Exception:
        model.save_pretrained(str(save_dir))
    tok.save_pretrained(str(save_dir))
    (save_dir / "labels.json").write_text(json.dumps(LABELS, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nSaved model to: {save_dir}")
    print(f"Saved classification report to: {OUT_DIR / 'test_classification_report.txt'}")
    print(f"Saved thresholds to: {OUT_DIR / 'best_thresholds.json'}")
    for lb in LABELS:
        print(f"Saved confusion matrix: {OUT_DIR / f'confusion_matrix_{lb}.png'}")

if __name__ == "__main__":
    main()
