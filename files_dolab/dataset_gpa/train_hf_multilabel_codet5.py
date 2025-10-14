# train_hf_multilabel_codet5.py — Stable on old transformers
# T5EncoderModel + custom head + SequenceClassifierOutput
# - ปิด checkpoint-saving ระหว่างเทรน (กัน safetensors + tied weights)
# - ครบ: class weight, threshold per-label, metrics, confusion matrices, save artifacts
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TRANSFORMERS_NO_FLAX"] = "1"

import json, random
from pathlib import Path
from typing import List, Dict, Union, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    f1_score, classification_report, accuracy_score, hamming_loss, multilabel_confusion_matrix
)

from transformers import (
    AutoTokenizer,
    T5EncoderModel,
    AutoConfig,
    Trainer,
    TrainingArguments,
)
from transformers.modeling_outputs import SequenceClassifierOutput

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ====== CONFIG ======
CSV_PATH = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\data_labeled\dataset.csv")
MODEL_NAME = "Salesforce/codet5-base"
OUT_DIR   = Path(r"D:\GitHub\dolap\files_dolab\dataset_gpa\model_codet5_test")

LABELS  = ["inputError", "processError", "outputError"]
MAX_LEN = 128
BATCH   = 2
EPOCHS  = 1
LR      = 5e-5

TEST_SIZE = 0.15
VAL_SIZE  = 0.15
SEED      = 123
# =====================

random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)

ArrayLike = Union[np.ndarray, torch.Tensor, List, Tuple]

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
        enc = self.tok(code, truncation=True, max_length=self.max_len)
        enc["labels"] = [float(row[l]) for l in LABELS]
        return enc

# ----- Custom Model: T5Encoder + masked mean pooling + linear head -----
class T5EncoderForMultiLabel(nn.Module):
    def __init__(self, model_name: str, num_labels: int):
        super().__init__()
        self.config = AutoConfig.from_pretrained(model_name)
        self.encoder = T5EncoderModel.from_pretrained(model_name)
        hidden = self.config.d_model
        self.classifier = nn.Linear(hidden, num_labels)
        nn.init.xavier_uniform_(self.classifier.weight)
        nn.init.zeros_(self.classifier.bias)

    def forward(self, input_ids=None, attention_mask=None, **kwargs):
        enc_out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden = enc_out.last_hidden_state  # [B, S, H]
        if attention_mask is None:
            mask = torch.ones(last_hidden.size()[:-1], device=last_hidden.device)
        else:
            mask = attention_mask
        mask = mask.unsqueeze(-1)                # [B, S, 1]
        summed = (last_hidden * mask).sum(dim=1) # [B, H]
        denom = mask.sum(dim=1).clamp(min=1e-6)  # [B, 1]
        pooled = summed / denom                  # [B, H]
        logits = self.classifier(pooled)         # [B, L]
        # ✅ คืนแบบมาตรฐาน HF เพื่อกันการ squeeze เป็น 1D ใน eval/predict
        return SequenceClassifierOutput(logits=logits)

def compute_metrics(eval_pred):
    logits, labels = (eval_pred if isinstance(eval_pred, tuple)
                      else (eval_pred.predictions, eval_pred.label_ids))
    # logits อาจเป็น list/tuple ของก้อน → รวมเป็น [N, L]
    if isinstance(logits, (list, tuple)):
        logits = np.concatenate([np.array(x) for x in logits], axis=0)
    logits = np.array(logits)
    if logits.ndim == 1:
        logits = logits.reshape(-1, len(LABELS))
    probs = 1.0 / (1.0 + np.exp(-logits))  # sigmoid
    y_pred = (probs >= 0.5).astype(int)
    y_true = np.asarray(labels)
    return {
        "micro_f1": f1_score(y_true, y_pred, average="micro", zero_division=0),
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
    }

def make_training_args():
    # ใช้พารามิเตอร์พื้นฐานเท่านั้น + ปิดเซฟเช็คพอยต์ระหว่างเทรน (save_steps ใหญ่)
    return TrainingArguments(
        output_dir=str(OUT_DIR / "runs"),
        learning_rate=LR,
        per_device_train_batch_size=BATCH,
        per_device_eval_batch_size=BATCH,
        num_train_epochs=EPOCHS,
        logging_steps=50,
        report_to=[],   # ไม่ส่งไป wandb/none
        seed=SEED,
        save_steps=10**12,   # ดันให้ไกลมากจนไม่เซฟระหว่างเทรน
        # save_total_limit=0, # คอมเมนต์ไว้เผื่อเวอร์ชันไม่รองรับ
    )

def main():
    # ---------- 1) Load & split ----------
    df = pd.read_csv(CSV_PATH)
    ids = df["id"].unique().tolist()
    train_ids, test_ids = train_test_split(ids, test_size=TEST_SIZE, random_state=SEED)
    train_ids, val_ids  = train_test_split(train_ids, test_size=VAL_SIZE/(1-TEST_SIZE), random_state=SEED)
    tr_df, va_df, te_df = (df[df["id"].isin(s)].copy() for s in (train_ids, val_ids, test_ids))
    print(f"Train: {len(tr_df)}  Val: {len(va_df)}  Test: {len(te_df)}")

    # ---------- 2) Tokenizer ----------
    tok = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token

    # ---------- 3) Model ----------
    model = T5EncoderForMultiLabel(MODEL_NAME, num_labels=len(LABELS))

    # ---------- 4) Datasets ----------
    train_ds, val_ds, test_ds = (CodeDataset(d, tok, MAX_LEN) for d in (tr_df, va_df, te_df))

    # ---------- 5) Collator ----------
    def collate_fn(batch: List[Dict]):
        labels = [item.pop("labels") for item in batch]
        padded = tok.pad(batch, padding=True, return_tensors="pt")
        padded["labels"] = torch.tensor(labels, dtype=torch.float)
        return padded

    # ---------- 6) Class weights ----------
    pos_counts = tr_df[LABELS].sum(axis=0).values.astype(float) + 1e-6
    neg_counts = len(tr_df) - pos_counts + 1e-6
    pos_weight_vec = torch.tensor(neg_counts / pos_counts, dtype=torch.float)
    print("pos_weight:", {lb: float(w) for lb, w in zip(LABELS, pos_weight_vec)})

    # ---------- 7) Trainer (no-save during training) ----------
    class WeightedBCETrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            labels = inputs.pop("labels")
            outputs = model(**inputs)             # SequenceClassifierOutput
            logits = outputs.logits               # [B, L]
            if not torch.is_tensor(labels):
                labels = torch.tensor(labels, dtype=torch.float, device=logits.device)
            else:
                labels = labels.to(dtype=torch.float, device=logits.device)
            loss = F.binary_cross_entropy_with_logits(
                logits, labels, pos_weight=pos_weight_vec.to(logits.device)
            )
            return (loss, outputs) if return_outputs else loss

        # ----- สำคัญ: กัน Trainer เซฟ checkpoint ระหว่างเทรน -----
        def _save_checkpoint(self, model, trial, metrics=None):
            return
        def _save(self, output_dir: str, state_dict=None):
            return

    args = make_training_args()
    trainer = WeightedBCETrainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=collate_fn,
        compute_metrics=compute_metrics,
    )

    # ---------- 8) Train ----------
    trainer.train()

    # ---------- 9) Threshold tuning on VAL ----------
    val_preds  = trainer.predict(val_ds)
    logits = val_preds.predictions
    if isinstance(logits, (list, tuple)):
        logits = np.concatenate([np.array(x) for x in logits], axis=0)
    logits = np.array(logits)
    if logits.ndim == 1:
        logits = logits.reshape(-1, len(LABELS))
    val_probs = 1.0 / (1.0 + np.exp(-logits))
    val_true  = va_df[LABELS].values

    best_th = {}
    for j, lb in enumerate(LABELS):
        y = val_true[:, j]; p = val_probs[:, j]
        best_f1, best_t = -1.0, 0.5
        for t in np.linspace(0.1, 0.9, 81):
            f1 = f1_score(y, (p >= t).astype(int), zero_division=0)
            if f1 > best_f1:
                best_f1, best_t = f1, t
        best_th[lb] = float(best_t)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "best_thresholds.json").write_text(json.dumps(best_th, indent=2), encoding="utf-8")
    print("Best thresholds (from VAL):", best_th)

    # ---------- 10) Test + Metrics ----------
    test_preds = trainer.predict(test_ds)
    logits = test_preds.predictions
    if isinstance(logits, (list, tuple)):
        logits = np.concatenate([np.array(x) for x in logits], axis=0)
    logits = np.array(logits)
    if logits.ndim == 1:
        logits = logits.reshape(-1, len(LABELS))
    test_probs = 1.0 / (1.0 + np.exp(-logits))
    y_true     = te_df[LABELS].values

    y_pred = np.zeros_like(test_probs, dtype=int)
    for j, lb in enumerate(LABELS):
        th = best_th.get(lb, 0.5)
        y_pred[:, j] = (test_probs[:, j] >= th).astype(int)

    micro_f1 = f1_score(y_true, y_pred, average="micro", zero_division=0)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    subset_acc  = accuracy_score(y_true, y_pred)
    hamming_acc = 1.0 - hamming_loss(y_true, y_pred)

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

    # ---------- 11) Confusion matrices ----------
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

    # ---------- 12) Save model & artifacts ----------
    save_dir = OUT_DIR / "best_model"
    save_dir.mkdir(parents=True, exist_ok=True)
    # เซฟเฉพาะ "หัว custom" + meta + tokenizer + labels
    torch.save(model.state_dict(), save_dir / "pytorch_model_custom_head.bin")
    meta = {"model_name": MODEL_NAME, "d_model": int(model.config.d_model), "labels": LABELS}
    (save_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    tok.save_pretrained(str(save_dir))
    (save_dir / "labels.json").write_text(json.dumps(LABELS, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nSaved custom head to: {save_dir / 'pytorch_model_custom_head.bin'}")
    print(f"Saved classification report to: {OUT_DIR / 'test_classification_report.txt'}")
    print(f"Saved thresholds to: {OUT_DIR / 'best_thresholds.json'}")
    for lb in LABELS:
        print(f"Saved confusion matrix: {OUT_DIR / f'confusion_matrix_{lb}.png'}")

if __name__ == "__main__":
    main()
