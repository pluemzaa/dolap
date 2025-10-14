# find_and_copy_by_input_prompts.py
from __future__ import annotations
import ast
import re
import csv
import shutil
from pathlib import Path
from typing import List, Dict, Set

# ========== CONFIG ==========
# โฟลเดอร์ต้นทาง (ที่มีไฟล์ .py จำนวนมาก)
SRC_DIR = Path(r"D:\GitHub\dolap\files_dolab\vfiles")
# โฟลเดอร์ปลายทาง (จะคัดลอกไฟล์ที่พบเงื่อนไขมารวมไว้)
OUT_DIR = Path(r"D:\GitHub\dolap\files_dolab\out_vfile_gpa")
# คีย์เวิร์ดที่ต้องการตรวจใน "ข้อความของ input()"
KEYWORDS: Set[str] = {"name", "email", "gpa"}
# True = ต้องพบครบทุกคำในไฟล์เดียวกัน / False = เจอคำใดคำหนึ่งก็ถือว่าผ่าน
REQUIRE_ALL = True
# ===================================

INPUT_CALL_REGEX = re.compile(
    r"""input\s*\(\s*(['"])(?P<prompt>.*?)(\1)\s*\)""",
    re.IGNORECASE | re.DOTALL,
)

def extract_prompts_ast(py_code: str) -> List[str]:
    """
    พยายามพาร์ส AST เพื่อหา call ที่ชื่อ 'input' และอาร์กิวเมนต์แรกเป็นสตริงคงที่
    คืนลิสต์ข้อความพรอมป์ทั้งหมดที่พบ
    """
    prompts: List[str] = []
    try:
        tree = ast.parse(py_code)
    except SyntaxError:
        return prompts  # ถ้าพาร์สไม่ได้ ค่อยไป regex ภายหลัง

    class Visitor(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call):
            # ฟังก์ชันชื่อ 'input' ไหม (รองรับทั้ง Name และ Attribute เผื่อมีเครสแปลก)
            func_name = ""
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr

            if func_name == "input" and node.args:
                first_arg = node.args[0]
                if isinstance(first_arg, ast.Constant) and isinstance(first_arg.value, str):
                    prompts.append(first_arg.value)
                # กรณี f-string
                elif isinstance(first_arg, ast.JoinedStr):
                    # ดึงส่วนสตริงที่ต่อรวมกันมาเพื่อเช็คคีย์เวิร์ดแบบคร่าวๆ
                    flat = "".join(
                        (s.value if isinstance(s, ast.Constant) and isinstance(s.value, str) else "")
                        for s in first_arg.values
                    )
                    if flat:
                        prompts.append(flat)
            self.generic_visit(node)

    Visitor().visit(tree)
    return prompts

def extract_prompts_regex(py_code: str) -> List[str]:
    """
    ถ้า AST ไม่ได้ผล ใช้ regex หา input("...") แบบเบื้องต้น
    คืนลิสต์ข้อความพรอมป์ที่พบ
    """
    prompts = []
    for m in INPUT_CALL_REGEX.finditer(py_code):
        prompts.append(m.group("prompt"))
    return prompts

def find_keywords_in_prompts(prompts: List[str], keywords: Set[str]) -> Set[str]:
    found: Set[str] = set()
    for p in prompts:
        lower = p.casefold()
        for kw in keywords:
            if kw.casefold() in lower:
                found.add(kw)
    return found

def main():
    if not SRC_DIR.exists():
        raise SystemExit(f"[ERROR] SRC_DIR not found: {SRC_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    matches: List[Dict[str, str]] = []

    py_files = list(SRC_DIR.rglob("*.py"))
    for f in py_files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            # ถ้าอ่านไม่ได้ ข้ามไฟล์
            continue

        prompts = extract_prompts_ast(text)
        if not prompts:
            # fallback เป็น regex
            prompts = extract_prompts_regex(text)

        if not prompts:
            continue

        found = find_keywords_in_prompts(prompts, KEYWORDS)

        ok = (found.issuperset(KEYWORDS)) if REQUIRE_ALL else (len(found) > 0)
        if not ok:
            continue

        # คัดลอกไฟล์ไป OUT_DIR โดยคงโครงสร้างโฟลเดอร์สัมพัทธ์
        rel = f.relative_to(SRC_DIR)
        dest_path = OUT_DIR / rel
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest_path)

        matches.append({
            "file": str(f),
            "relative": str(rel),
            "matched_keywords": ",".join(sorted(found)),
            "prompts_preview": " | ".join(p.strip().replace("\n", " ")[:200] for p in prompts),
        })

    # เขียนรายงาน CSV
    report_path = OUT_DIR / "match_report.csv"
    with report_path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=["file", "relative", "matched_keywords", "prompts_preview"])
        writer.writeheader()
        writer.writerows(matches)

    print(f"[DONE] scanned: {len(py_files)} files")
    print(f"[HIT ] matched: {len(matches)} files")
    print(f"[OUT ] copied to: {OUT_DIR}")
    print(f"[REPORT] {report_path}")

if __name__ == "__main__":
    main()
