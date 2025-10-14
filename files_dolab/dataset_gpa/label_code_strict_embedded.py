# label_code_strict_embedded_multilabel.py
# ใช้ได้ทันที: กำหนดพาธและโหมดไว้บนหัวไฟล์ ไม่ต้องใส่ --src/--out
# Multi-label: ถ้าผิดหลายอย่าง คัดลอกไฟล์ไปทุกโฟลเดอร์ที่ตรงกับความผิดนั้น
# เงื่อนไขเข้ม:
#   INPUT  : ต้องมี input() 3 ครั้ง และ prompt ตรงตามลำดับ 100%
#   PROCESS: ต้อง cast name=str(name), email=str(email), GPA=float(GPA)
#            และสร้าง data_list=[name,email,GPA], data_tuple=(...), data_dict={"name":...}
#   OUTPUT : ผ่านได้ 2 สไตล์
#            A) print("name", name) ; print("email", email) ; print("GPA", GPA)  (ตามลำดับ)
#            B) print(data_list) ; print(data_tuple) ; print(data_dict)         (อนุญาตเลือกใช้)

from __future__ import annotations
import ast
import shutil
from pathlib import Path

# ===================== CONFIG (แก้ตรงนี้) =====================
SRC_DIR  = r"D:\GitHub\dolap\files_dolab\dataset_gpa\data_unlabeled"          # โฟลเดอร์ .py ที่ยังไม่ติดฉลาก
OUT_DIR  = r"D:\GitHub\dolap\files_dolab\dataset_gpa\data_labeled" # โฟลเดอร์ผลลัพธ์
PATTERN  = "**/*.py"                                      # ค้นหาแบบรีเคอร์ซีฟ
ACTION   = "copy"  # None=พรีวิวอย่างเดียว, "copy"=คัดลอก, "move"=ย้าย(สร้างหลายสำเนาแล้วลบต้นฉบับ)
ALLOW_LEGACY_STRUCT_OUTPUT = True  # True = ยอมรับสไตล์ B (print(data_list/tuple/dict))
# =============================================================

REF_INPUT_PROMPTS = [
    "Enter your name: ",
    "Enter your email: ",
    "Enter your GPA: ",
]

LABELS = ["ok", "inputError", "processError", "outputError"]

def read_code(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def parse_safe(code: str):
    try:
        return ast.parse(code)
    except SyntaxError:
        return None

def is_name(node, name: str) -> bool:
    return isinstance(node, ast.Name) and node.id == name

def is_call_name(node, fname: str) -> bool:
    return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == fname

def lit_str(node):
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None

# ---------- INPUT ----------
def check_inputs(tree: ast.AST) -> bool:
    prompts = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "input":
            if node.args:
                s = lit_str(node.args[0])
                prompts.append(s if s is not None else "__NON_LITERAL__")
            else:
                prompts.append("")
    return prompts == REF_INPUT_PROMPTS

# ---------- PROCESS ----------
def check_process(tree: ast.AST):
    cast_ok = {"name": False, "email": False, "GPA": False}
    list_var = None
    tuple_var = None
    dict_var = None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and node.targets and isinstance(node.targets[0], ast.Name):
            tname = node.targets[0].id
            v = node.value

            if tname == "name" and is_call_name(v, "str") and len(v.args) == 1 and is_name(v.args[0], "name"):
                cast_ok["name"] = True
            if tname == "email" and is_call_name(v, "str") and len(v.args) == 1 and is_name(v.args[0], "email"):
                cast_ok["email"] = True
            if tname == "GPA" and is_call_name(v, "float") and len(v.args) == 1 and is_name(v.args[0], "GPA"):
                cast_ok["GPA"] = True

            if isinstance(v, ast.List):
                elts = v.elts
                if len(elts) == 3 and all(isinstance(e, ast.Name) for e in elts):
                    if elts[0].id == "name" and elts[1].id == "email" and elts[2].id == "GPA":
                        list_var = tname

            if isinstance(v, ast.Tuple):
                elts = v.elts
                if len(elts) == 3 and all(isinstance(e, ast.Name) for e in elts):
                    if elts[0].id == "name" and elts[1].id == "email" and elts[2].id == "GPA":
                        tuple_var = tname

            if isinstance(v, ast.Dict):
                keys = v.keys
                vals = v.values
                if len(keys) == 3 and len(vals) == 3:
                    kv = {}
                    ok = True
                    for k, val in zip(keys, vals):
                        ks = lit_str(k)
                        if ks is None or not isinstance(val, ast.Name):
                            ok = False
                            break
                        kv[ks] = val.id
                    if ok and set(kv.keys()) == {"name", "email", "GPA"} and \
                       kv["name"] == "name" and kv["email"] == "email" and kv["GPA"] == "GPA":
                        dict_var = tname

    process_ok = all(cast_ok.values()) and (list_var is not None) and (tuple_var is not None) and (dict_var is not None)
    return process_ok, {"list_var": list_var, "tuple_var": tuple_var, "dict_var": dict_var}

# ---------- OUTPUT ----------
def check_outputs(tree: ast.AST, names: dict) -> bool:
    prints = [n for n in ast.walk(tree)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "print"]

    # Style A: print("name", name); print("email", email); print("GPA", GPA)
    def is_labeled_prints_ok():
        if len(prints) < 3:
            return False
        first_three = prints[:3]
        labels = ["name", "email", "GPA"]
        vars_ = ["name", "email", "GPA"]
        for call, lab, var in zip(first_three, labels, vars_):
            if len(call.args) < 2:
                return False
            s = lit_str(call.args[0])
            if s != lab:
                return False
            if not (isinstance(call.args[1], ast.Name) and call.args[1].id == var):
                return False
        return True

    # Style B: print(data_list); print(data_tuple); print(data_dict)
    def is_legacy_struct_prints_ok():
        if not ALLOW_LEGACY_STRUCT_OUTPUT:
            return False
        if not names["list_var"] or not names["tuple_var"] or not names["dict_var"]:
            return False
        if len(prints) < 3:
            return False
        expected = [names["list_var"], names["tuple_var"], names["dict_var"]]
        first_three = prints[:3]
        for call, exp in zip(first_three, expected):
            if not call.args:
                return False
            if not isinstance(call.args[0], ast.Name) or call.args[0].id != exp:
                return False
        return True

    return is_labeled_prints_ok() or is_legacy_struct_prints_ok()

# ---------- MULTI-LABEL ----------
def decide_labels(py_path: Path):
    code = read_code(py_path)
    tree = parse_safe(code)
    if tree is None:
        return ["processError"]

    inp_ok = check_inputs(tree)
    proc_ok, name_map = check_process(tree)
    out_ok = check_outputs(tree, name_map)

    if inp_ok and proc_ok and out_ok:
        return ["ok"]

    labels = []
    if not inp_ok:
        labels.append("inputError")
    if not proc_ok:
        labels.append("processError")
    if not out_ok:
        labels.append("outputError")
        
    return labels or ["processError"]

# ---------- RUN ----------
def ensure_dirs(out_root: Path):
    out_root.mkdir(parents=True, exist_ok=True)
    for lb in LABELS:
        (out_root / lb).mkdir(parents=True, exist_ok=True)

def main():
    src = Path(SRC_DIR)
    out = Path(OUT_DIR)
    if not src.exists():
        raise SystemExit(f"ไม่พบโฟลเดอร์ต้นทาง: {src}")

    ensure_dirs(out)
    files = sorted(src.glob(PATTERN))
    if not files:
        print("ไม่พบไฟล์ตามแพทเทิร์น")
        return

    summary = {k: 0 for k in LABELS}
    for f in files:
        if not f.is_file() or f.suffix.lower() != ".py":
            continue

        lbs = decide_labels(f)
        for lb in lbs:
            summary[lb] += 1

        print(f"{f.relative_to(src)!s:60s} → {', '.join(lbs)}")

        if ACTION == "copy":
            for lb in lbs:
                shutil.copy2(f, out / lb / f.name)
        elif ACTION == "move":
            # สร้างหลายสำเนาแล้วลบต้นฉบับ
            first = True
            for lb in lbs:
                if first:
                    shutil.copy2(f, out / lb / f.name)
                    first = False
                else:
                    shutil.copy2(f, out / lb / f.name)
            try:
                f.unlink()
            except Exception:
                pass
        else:
            # preview only
            pass

    print("\n=== SUMMARY (multi-label counts) ===")
    for k in LABELS:
        print(f"{k:24s}: {summary[k]}")
    print(f"\nOUT_DIR: {out}")

if __name__ == "__main__":
    main()
