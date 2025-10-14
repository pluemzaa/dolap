from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
from collections import Counter, defaultdict

# ===== CONFIG =====
GRADER = Path(r"D:\GitHub\dolap\grader_instrument_v2.py")   # path ไปยังไฟล์ grader ที่แพตช์แล้ว
REF    = Path(r"D:\GitHub\dolap\files_dolab\solution_ref.py")

# โครงสร้างชุดทดสอบ (รองรับ 2 แบบ)
# A) แบบง่าย: มีเพียง correct/ และ incorrect/
DATASET_DIR = Path(r"D:\GitHub\dolap\files_dolab\data_files_c_168_in_168")

# B) ถ้าคุณแยกกลุ่มย่อย error ได้ ให้สร้างโฟลเดอร์แบบนี้ภายใต้ incorrect/:
#    incorrect/InputError/
#    incorrect/ProcessError/
#    incorrect/OutputError/
#    incorrect/ProcessError_and_OutputError/
# สคริปต์จะตรวจอัตโนมัติว่ามีโฟลเดอร์ย่อยแบบ B หรือไม่

# ===== Helpers =====
CLASSES = ["OK","InputError","ProcessError","OutputError","ProcessError and OutputError"]

def run_grader(student: Path) -> dict:
    """เรียก grader ให้คืน JSON (stdout)"""
    p = subprocess.run([sys.executable, str(GRADER), "--ref", str(REF), "--student", str(student), "--json-stdout"],
                       capture_output=True, text=True)
    if p.returncode != 0:
        # ถ้า grader พัง ให้ตีเป็น InputError (หรือจะตั้งเป็น Unknown ก็ได้)
        return {"error":"grader_failed", "stdout":p.stdout, "stderr":p.stderr, "overall":"InputError"}
    try:
        return json.loads(p.stdout.strip())
    except Exception:
        return {"error":"bad_json", "raw":p.stdout, "overall":"InputError"}

def find_files() -> list[tuple[Path,str]]:
    """
    คืนลิสต์ (path, label_true). รองรับสองกรณี:
    - A) correct/*.py => label_true="OK"
       incorrect/*.py => label_true="NotOK"
    - B) ถ้ามี subfolders ใน incorrect/ จะอ่านชื่อโฟลเดอร์เป็นคลาสจริง
    """
    correct_dir   = DATASET_DIR / "correct"
    incorrect_dir = DATASET_DIR / "incorrect"

    items: list[tuple[Path,str]] = []
    # correct
    if correct_dir.exists():
        for p in correct_dir.glob("*.py"):
            items.append((p, "OK"))

    # incorrect
    if incorrect_dir.exists():
        # ตรวจว่ามี sub-class ไหม
        subdirs = [d for d in incorrect_dir.iterdir() if d.is_dir()]
        if subdirs:
            name_map = {
                "InputError": "InputError",
                "ProcessError": "ProcessError",
                "OutputError": "OutputError",
                "ProcessError_and_OutputError": "ProcessError and OutputError",
                "ProcessError and OutputError": "ProcessError and OutputError",
            }
            for d in subdirs:
                label = name_map.get(d.name, None)
                if label is None:
                    # โฟลเดอร์อื่นๆที่ไม่รู้จัก ข้ามหรือ map เป็น "NotOK"
                    label = "NotOK"
                for p in d.glob("*.py"):
                    items.append((p, label))
        else:
            # ไม่มี subclass => ทั้งหมดเป็น NotOK
            for p in incorrect_dir.glob("*.py"):
                items.append((p, "NotOK"))
    return items

def binarize(pred: str) -> str:
    return "OK" if pred == "OK" else "NotOK"

def main():
    items = find_files()
    if not items:
        print("[ERROR] no files found in dataset")
        return

    # รัน grader ทุกรายการ
    rows = []
    for path, y_true in items:
        rep = run_grader(path)
        y_pred = rep.get("classification",{}).get("overall") or rep.get("overall") or rep.get("pred_class") or "InputError"
        rows.append({
            "file": str(path),
            "y_true": y_true,
            "y_pred": y_pred,
        })

    # =========================
    # 1) ถ้า dataset เป็นแบบ A (มีแค่ OK vs NotOK)
    # =========================
    if any(r["y_true"] == "NotOK" for r in rows):
        # Binary metrics
        tp = sum(1 for r in rows if r["y_true"]=="OK"    and binarize(r["y_pred"])=="OK")
        tn = sum(1 for r in rows if r["y_true"]=="NotOK" and binarize(r["y_pred"])=="NotOK")
        fp = sum(1 for r in rows if r["y_true"]=="NotOK" and binarize(r["y_pred"])=="OK")
        fn = sum(1 for r in rows if r["y_true"]=="OK"    and binarize(r["y_pred"])=="NotOK")

        total = len(rows)
        acc   = (tp+tn)/total if total else 0.0
        prec_ok  = tp/(tp+fp) if (tp+fp) else 0.0
        rec_ok   = tp/(tp+fn) if (tp+fn) else 0.0

        print("\n=== Binary (OK vs NotOK) ===")
        print(f"Total: {total}")
        print(f"Accuracy: {acc:.3f}")
        print(f"Precision(OK): {prec_ok:.3f}")
        print(f"Recall(OK):    {rec_ok:.3f}")
        print("Confusion matrix [rows=true, cols=pred]:")
        #   True\Pred   OK   NotOK
        print(f"OK        {tp:4d} {fn:6d}")
        print(f"NotOK     {fp:4d} {tn:6d}")

    # =========================
    # 2) ถ้า dataset เป็นแบบ B (มี subclass 4 error)
    # =========================
    has_multiclass = any(r["y_true"] in CLASSES for r in rows)
    if has_multiclass:
        # กรองเฉพาะที่ y_true เป็นหนึ่งใน CLASSES
        mc = [r for r in rows if r["y_true"] in CLASSES]
        # confusion
        idx = {c:i for i,c in enumerate(CLASSES)}
        mat = [[0]*len(CLASSES) for _ in CLASSES]
        for r in mc:
            i = idx[r["y_true"]]
            j = idx[r["y_pred"]] if r["y_pred"] in idx else idx["InputError"]
            mat[i][j] += 1

        total_mc = sum(sum(row) for row in mat)
        acc_mc = sum(mat[i][i] for i in range(len(CLASSES))) / total_mc if total_mc else 0.0

        print("\n=== Multiclass (OK + 4 error classes) ===")
        print(f"Total: {total_mc}")
        print(f"Accuracy: {acc_mc:.3f}")
        print("Labels (index):", {i:c for c,i in idx.items()})
        print("Confusion matrix [rows=true, cols=pred]:")
        for i, row in enumerate(mat):
            print(f"{CLASSES[i]:28s} " + " ".join(f"{n:4d}" for n in row))

    # บันทึกผลรายไฟล์ (CSV)
    out_csv = DATASET_DIR / "eval_results.csv"
    with out_csv.open("w", encoding="utf-8") as f:
        f.write("file,y_true,y_pred\n")
        for r in rows:
            f.write(f"{r['file']},{r['y_true']},{r['y_pred']}\n")
    print(f"\n[Saved] {out_csv}")

if __name__ == "__main__":
    main()
