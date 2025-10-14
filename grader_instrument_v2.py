# grader_instrument_v2.py  (Python 3.10+)
from __future__ import annotations
import sys, ast, json, subprocess, textwrap, difflib, time, tempfile
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any
from collections import Counter

# ======= CONFIG =======
REF_PATH = Path(r"D:\GitHub\dolap\solution_ref.py")
STU_PATH = Path(r"D:\GitHub\dolap\solution_student.py")
# งานแบบ “พิมพ์โครงสร้าง” (ไม่มี label) คาดหวังให้มีสามชนิดนี้
EXPECTED_UNLABELED_TYPES = ["list", "tuple", "dict"]
# ถ้ามี label ก็ยังใช้ได้ (กำหนดชื่อ label ตรงนี้)
EXPECTED_LABELS: List[str] = []

TESTS = [
    {"name": "t1", "stdin": "Alice\nalice@example.com\n3.75\n"},
    {"name": "t2", "stdin": "Bob\nbob@x.y\n4.00\n"},
]
TIMEOUT = 2.0
FLOAT_TOL = 1e-9

ERROR_CLASSES = ("InputError", "ProcessError", "OutputError", "ProcessError and OutputError")

# ======= RUNTIME HELPERS =======
def run(path: Path, stdin_text: str, timeout: float) -> tuple[int,str,str]:
    p = subprocess.Popen([sys.executable, str(path)],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True)
    try:
        out, err = p.communicate(stdin_text, timeout=timeout)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        p.kill()
        return -9, "", f"TIMEOUT>{timeout}s"

def sniff_prompt(path: Path, sniff_seconds=0.2) -> str:
    p = subprocess.Popen([sys.executable, str(path)],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True)
    time.sleep(sniff_seconds)
    try:
        p.kill()
    except Exception:
        pass
    try:
        out, _ = p.communicate(timeout=0.1)
    except Exception:
        out = ""
    return out

def udiff(a: str, b: str) -> str:
    return "".join(difflib.unified_diff(
        a.splitlines(keepends=True),
        b.splitlines(keepends=True),
        fromfile="expected", tofile="got"
    ))

# ======= AST INSTRUMENTER =======
class PrintTapper(ast.NodeTransformer):
    """
    แทรก __record(kind, payload) ก่อน print(...)
    - ถ้าเจอ label: print("LAB:", expr)/f"LAB: {expr}" -> kind="label", payload={"label":LAB,"value":expr}
    - ถ้าไม่มี label: บันทึกค่าของอาร์กิวเมนต์แต่ละตัวที่พิมพ์ -> kind="value", payload={"value":expr}
    """
    def __init__(self, known_labels: List[str]):
        self.known_labels = set(known_labels)

    @staticmethod
    def _const_str(n: ast.AST) -> Optional[str]:
        return n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else None

    def _extract_label_expr(self, call: ast.Call) -> Optional[Tuple[str, ast.AST]]:
        # A: f-string
        if call.args:
            a0 = call.args[0]
            if isinstance(a0, ast.JoinedStr):
                leading = ""
                expr_node = None
                for v in a0.values:
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        leading += v.value
                    elif isinstance(v, ast.FormattedValue) and expr_node is None:
                        expr_node = v.value
                        break
                lab = leading.strip()
                if lab and (not self.known_labels or lab in self.known_labels):
                    if expr_node is not None:
                        return lab, expr_node
            # B: print("LAB:", expr)
            s0 = self._const_str(a0)
            if s0 is not None:
                lab = s0.strip()
                if lab and (not self.known_labels or lab in self.known_labels):
                    if len(call.args) >= 2:
                        return lab, call.args[1]
            # C: "LAB: " + str(x)
            if isinstance(a0, ast.BinOp) and isinstance(a0.op, ast.Add):
                left = a0.left; right = a0.right
                sleft = self._const_str(left)
                if sleft:
                    lab = sleft.strip()
                    if lab and (not self.known_labels or lab in self.known_labels):
                        if isinstance(right, ast.Call) and right.args:
                            return lab, right.args[0]
                        if isinstance(right, ast.Name):
                            return lab, right
        return None

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Call):
            call = node.value
            is_print = isinstance(call.func, ast.Name) and call.func.id == "print"
            if is_print:
                info = self._extract_label_expr(call)
                if info:
                    lab, expr = info
                    rec = ast.Expr(value=ast.Call(func=ast.Name(id="__record", ctx=ast.Load()),
                                                  args=[ast.Constant("label"),
                                                        ast.Dict(keys=[ast.Constant("label"), ast.Constant("value")],
                                                                 values=[ast.Constant(lab), expr])],
                                                  keywords=[]))
                    ast.copy_location(rec, node)
                    return [rec, node]
                else:
                    recs = []
                    for arg in call.args:
                        recs.append(ast.Expr(value=ast.Call(func=ast.Name(id="__record", ctx=ast.Load()),
                                                            args=[ast.Constant("value"),
                                                                  ast.Dict(keys=[ast.Constant("value")],
                                                                           values=[arg])],
                                                            keywords=[])))
                    if recs:
                        for r in recs: ast.copy_location(r, node)
                        return recs + [node]
        return self.generic_visit(node)

INJECT_PREAMBLE = r"""
import atexit, json, sys
__CAPTURE = []
def __norm(v):
    # ทำให้ JSON-serializable พร้อมติด tag ชนิด
    if isinstance(v, float):
        return {"__type":"float","value":v}
    if isinstance(v, int):
        return {"__type":"int","value":v}
    if isinstance(v, str):
        return {"__type":"str","value":v}
    if isinstance(v, tuple):
        return {"__type":"tuple","items":[__norm(x) for x in v]}
    if isinstance(v, list):
        return {"__type":"list","items":[__norm(x) for x in v]}
    if isinstance(v, dict):
        # คงลำดับ keys ตามที่ถูกสร้าง
        return {"__type":"dict","items":[[k,__norm(v[k])] for k in v.keys()]}
    # fallback
    return {"__type":type(v).__name__,"repr":repr(v)}

def __record(kind, payload):
    # payload: {"label":..., "value":...} หรือ {"value":...}
    if kind == "label":
        __CAPTURE.append({"kind":"label","label":payload["label"],"value":__norm(payload["value"])})
    else:
        __CAPTURE.append({"kind":"value","value":__norm(payload["value"])})

def __dump():
    try:
        print("<<<CAPTURE>>>"+json.dumps(__CAPTURE, ensure_ascii=False), file=sys.stderr)
    except Exception:
        print("<<<CAPTURE>>>[]", file=sys.stderr)
atexit.register(__dump)
"""

def instrument_source(src: str, known_labels: List[str]) -> str:
    tree = ast.parse(src)
    tree = PrintTapper(known_labels).visit(tree)
    ast.fix_missing_locations(tree)
    pre = ast.parse(INJECT_PREAMBLE)
    pre.body.extend(tree.body)
    if not hasattr(ast, "unparse"):
        raise RuntimeError("Python 3.10+ required (ast.unparse missing)")
    return ast.unparse(pre)

def write_temp_instrumented(src_path: Path, known_labels: List[str]) -> Path:
    inst = instrument_source(src_path.read_text(encoding="utf-8"), known_labels)
    tmp = Path(tempfile.gettempdir()) / f"__inst_{src_path.stem}_{int(time.time()*1000)}.py"
    tmp.write_text(inst, encoding="utf-8")
    return tmp

# ======= CAPTURE PARSER / COMPARATORS =======
def parse_capture(stderr_text: str) -> List[Dict[str,Any]]:
    last = ""
    for line in stderr_text.splitlines():
        if line.startswith("<<<CAPTURE>>>"):
            last = line[len("<<<CAPTURE>>>"):]
    try:
        return json.loads(last) if last else []
    except Exception:
        return []

def float_equal(a: float, b: float) -> bool:
    return abs(a - b) <= FLOAT_TOL

def norm_equals(n1: Dict[str,Any], n2: Dict[str,Any]) -> bool:
    t1, t2 = n1.get("__type"), n2.get("__type")
    if t1 != t2: return False
    if t1 in ("float","int","str"):
        if t1 == "float": return float_equal(n1["value"], n2["value"])
        return n1["value"] == n2["value"]
    if t1 in ("tuple", "list"):
        a1, a2 = n1["items"], n2["items"]
        if len(a1) != len(a2): return False
        return all(norm_equals(x,y) for x,y in zip(a1,a2))
    if t1 == "dict":
        d1 = {k:v for k,v in n1["items"]}
        d2 = {k:v for k,v in n2["items"]}
        if set(d1.keys()) != set(d2.keys()): return False
        return all(norm_equals(d1[k], d2[k]) for k in d1.keys())
    return n1 == n2

def kind_of(n: Dict[str,Any]) -> str:
    return n.get("__type","unknown")

def group_unlabeled_by_main_type(caps: List[Dict[str,Any]]) -> Dict[str,List[Dict[str,Any]]]:
    groups: Dict[str,List[Dict[str,Any]]] = {}
    for e in caps:
        if e.get("kind") == "value":
            t = kind_of(e["value"])
            groups.setdefault(t, []).append(e["value"])
    return groups

def first_label_map(caps: List[Dict[str,Any]]) -> Dict[str,Dict[str,Any]]:
    m: Dict[str,Dict[str,Any]] = {}
    for e in caps:
        if e.get("kind") == "label":
            lab = e["label"]
            if lab not in m:
                m[lab] = e["value"]
    return m

def compare_unlabeled_structs(ref_caps, stu_caps) -> Tuple[bool, List[str]]:
    msgs = []
    ok = True
    ref_groups = group_unlabeled_by_main_type(ref_caps)
    stu_groups = group_unlabeled_by_main_type(stu_caps)

    for t in EXPECTED_UNLABELED_TYPES:
        rvs = ref_groups.get(t, [])
        svs = stu_groups.get(t, [])
        if not rvs or not svs:
            ok = False
            msgs.append(f"[{t}] missing in {'student' if rvs else 'reference'}")
            continue
        if not norm_equals(rvs[0], svs[0]):
            ok = False
            msgs.append(f"[{t}] value mismatch")
    return ok, msgs

def compare_labeled_values(ref_caps, stu_caps, labels: List[str]) -> Tuple[bool, List[str]]:
    msgs = []
    ok = True
    rm = first_label_map(ref_caps)
    sm = first_label_map(stu_caps)
    for lab in labels:
        if lab in rm and lab in sm:
            if not norm_equals(rm[lab], sm[lab]):
                ok = False
                msgs.append(f"[{lab}] value mismatch")
        else:
            ok = False
            msgs.append(f"[{lab}] missing in {'student' if lab in rm else 'reference'}")
    return ok, msgs

def process_checks_for_this_task(ref_caps, stu_caps) -> Tuple[bool,List[str]]:
    """
    เช็คเชิงตรรกะสำหรับโจทย์ name/email/GPA:
    - list/tuple: ต้องมี 3 ช่อง [str, str, float]
    - dict: keys ต้องเป็น {"name","email","GPA"} และค่าตามชนิด [str,str,float]
    """
    ok = True; msgs = []
    groups = group_unlabeled_by_main_type(stu_caps)

    # list
    if "list" in groups and groups["list"]:
        lst = groups["list"][0]["items"]
        if len(lst) != 3 or lst[0]["__type"]!="str" or lst[1]["__type"]!="str" or lst[2]["__type"] not in ("float","int"):
            ok = False; msgs.append("[process] list must be [str, str, float]")
    else:
        ok = False; msgs.append("[process] missing printed list")

    # tuple
    if "tuple" in groups and groups["tuple"]:
        tpl = groups["tuple"][0]["items"]
        if len(tpl) != 3 or tpl[0]["__type"]!="str" or tpl[1]["__type"]!="str" or tpl[2]["__type"] not in ("float","int"):
            ok = False; msgs.append("[process] tuple must be (str, str, float)")
    else:
        ok = False; msgs.append("[process] missing printed tuple")

    # dict
    if "dict" in groups and groups["dict"]:
        d = {k:v for k,v in groups["dict"][0]["items"]}
        expected_keys = {"name","email","GPA"}
        if set(d.keys()) != expected_keys:
            ok = False; msgs.append("[process] dict keys must be {name,email,GPA}")
        else:
            if d["name"]["__type"]!="str" or d["email"]["__type"]!="str" or d["GPA"]["__type"] not in ("float","int"):
                ok = False; msgs.append("[process] dict values must be {'name':str,'email':str,'GPA':float}")
    else:
        ok = False; msgs.append("[process] missing printed dict")

    return ok, msgs

# ======= CLASSIFIER (4 classes + OK) =======
def classify_test_case(ok_input: bool, r: Dict[str, Any]) -> str:
    if not ok_input:
        return "InputError"
    pe = not r["process_ok"]
    oe = not r["stdout_equal"]  # ถ้าอยากนับ preprint เข้มขึ้น:  oe = (not r["stdout_equal"]) or (not r["preprint_equal"])
    if pe and oe:
        return "ProcessError and OutputError"
    if pe:
        return "ProcessError"
    if oe:
        return "OutputError"
    return "OK"

def classify_overall(ok_input: bool, results: List[Dict[str, Any]]) -> str:
    if not ok_input:
        return "InputError"
    any_proc_err = any(not r["process_ok"] for r in results)
    any_out_err  = any(not r["stdout_equal"] for r in results)
    if any_proc_err and any_out_err:
        return "ProcessError and OutputError"
    if any_proc_err:
        return "ProcessError"
    if any_out_err:
        return "OutputError"
    return "OK"

def _pct(n, d): return (float(n) / float(d) * 100.0) if d else 0.0

# ======= CORE RUN (returns JSON report) =======
def run_grade_once(ref_path: Path, stu_path: Path, verbose: bool=True) -> Dict[str, Any]:
    if not ref_path.exists() or not stu_path.exists():
        msg = f"[ERROR] missing {ref_path} or {stu_path}"
        if verbose: print(msg); 
        return {"error": "missing_path", "message": msg}

    # INPUT check
    if verbose: print("# ====== INPUT check (prompt must match 100%) ======")
    ref_prompt = sniff_prompt(ref_path)
    stu_prompt = sniff_prompt(stu_path)
    ok_input = (ref_prompt == stu_prompt)
    if verbose:
        print(f"- ref prompt:\n{ref_prompt!r}")
        print(f"- stu prompt:\n{stu_prompt!r}")
        print(f"=> INPUT_MATCH: {ok_input}")

    # เตรียมไฟล์ instrumented
    ref_inst = write_temp_instrumented(ref_path, EXPECTED_LABELS)
    stu_inst = write_temp_instrumented(stu_path, EXPECTED_LABELS)

    if verbose: print("\n# ====== OUTPUT + PRE-PRINT ======")
    out_ok_count = 0
    pre_ok_count = 0
    proc_ok_count = 0
    results: List[Dict[str, Any]] = []

    for tc in TESTS:
        name = tc["name"]; sin = tc["stdin"]
        rc_r, out_r, err_r = run(ref_inst, sin, TIMEOUT)
        rc_s, out_s, err_s = run(stu_inst, sin, TIMEOUT)

        out_equal = (rc_r == 0 and rc_s == 0 and out_r == out_s)
        if out_equal: out_ok_count += 1

        cap_r = parse_capture(err_r)
        cap_s = parse_capture(err_s)

        if EXPECTED_LABELS:
            pre_equal, pre_msgs = compare_labeled_values(cap_r, cap_s, EXPECTED_LABELS)
        else:
            pre_equal, pre_msgs = compare_unlabeled_structs(cap_r, cap_s)
        if pre_equal: pre_ok_count += 1

        proc_ok, proc_msgs = process_checks_for_this_task(cap_r, cap_s)
        if proc_ok: proc_ok_count += 1

        row = {
            "name": name,
            "stdout_equal": out_equal,
            "preprint_equal": pre_equal,
            "process_ok": proc_ok,
            "stdout_diff": (udiff(out_r, out_s) if not out_equal else ""),
            "pre_msgs": pre_msgs if not pre_equal else [],
            "proc_msgs": proc_msgs if not proc_ok else [],
        }
        row["pred_class"] = classify_test_case(ok_input, row)
        results.append(row)

        if verbose:
            print(f"- [{name}] stdout_equal={out_equal}   preprint_equal={pre_equal}   process_ok={proc_ok}   class={row['pred_class']}")
            if not out_equal:
                print("  stdout diff:")
                print(textwrap.indent(row["stdout_diff"], "    "))
            if not pre_equal:
                print("  pre-print diffs:")
                for m in pre_msgs: print("    " + m)
            if not proc_ok:
                print("  process issues:")
                for m in proc_msgs: print("    " + m)

    # Metrics
    total_tests = len(TESTS)
    strict_ok_count = sum(1 for r in results if r["stdout_equal"] and r["preprint_equal"] and r["process_ok"])
    acc_out   = out_ok_count / total_tests if total_tests else 0.0
    acc_pre   = pre_ok_count / total_tests if total_tests else 0.0
    acc_proc  = proc_ok_count / total_tests if total_tests else 0.0
    acc_strict = strict_ok_count / total_tests if total_tests else 0.0

    overall_class = classify_overall(ok_input, results)
    class_counts = Counter(r["pred_class"] for r in results)

    if verbose:
        print("\n# ====== SUMMARY ======")
        print(f"INPUT(1): {1.0 if ok_input else 0.0:.1f}")
        print(f"OUTPUT({total_tests}): {out_ok_count:.1f} / {total_tests}  (acc={_pct(out_ok_count,total_tests):.1f}%)")
        print(f"PRE-PRINT({total_tests}): {pre_ok_count:.1f} / {total_tests}  (acc={_pct(pre_ok_count,total_tests):.1f}%)")
        print(f"PROCESS-SCHEMA({total_tests}): {proc_ok_count:.1f} / {total_tests}  (acc={_pct(proc_ok_count,total_tests):.1f}%)")
        print(f"STRICT({total_tests}): {strict_ok_count:.1f} / {total_tests}  (acc={_pct(strict_ok_count,total_tests):.1f}%)")
        print(f"\n# ====== CLASSIFICATION ======")
        print(f"Overall predicted class: {overall_class}")
        print("Per-test class counts:", dict(class_counts))

        total_legacy = (1.0 if ok_input else 0.0) + out_ok_count + pre_ok_count + proc_ok_count
        print(f"\n=> TOTAL (legacy): {total_legacy:.1f} / {1 + 3*total_tests}")

        if not ok_input:
            print("\n[HINT] Prompt ไม่ตรง 100% — สังเกตเว้นวรรคหลังโคลอน")
        if out_ok_count < total_tests:
            print("[HINT] stdout ไม่ตรง — ดู diff เพื่อแยกเรื่องรูปแบบ/ค่าคำนวณ")
        if pre_ok_count < total_tests:
            print("[HINT] ค่าก่อนพิมพ์ไม่ตรง — ตรวจสูตรและชนิดข้อมูลก่อนการจัดรูปแบบ")
        if proc_ok_count < total_tests:
            print("[HINT] โครงสร้าง/ชนิดข้อมูลไม่ตรงสเปค — ตรวจ list/tuple/dict และชนิดของ GPA")

    report = {
        "config": {
            "tests": total_tests,
            "timeout": TIMEOUT,
            "float_tolerance": FLOAT_TOL,
            "mode": ("labeled" if EXPECTED_LABELS else "unlabeled"),
            "expected_labels": EXPECTED_LABELS,
            "ref_path": str(ref_path),
            "student_path": str(stu_path),
        },
        "metrics": {
            "input_pass": bool(ok_input),
            "acc_output": acc_out,
            "acc_preprint": acc_pre,
            "acc_process": acc_proc,
            "acc_strict": acc_strict,
        },
        "classification": {
            "overall": overall_class,
            "per_test_counts": dict(class_counts),
        },
        "tests": results,
    }
    # เขียนไฟล์สรุป JSON ชั่วคราวเสมอ (ช่วยดีบัก)
    report_path = Path(tempfile.gettempdir()) / "grader_report.json"
    try:
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        if verbose:
            print(f"\n[REPORT] saved JSON -> {report_path}")
    except Exception:
        pass
    return report

# ======= CLI =======
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", type=Path, default=REF_PATH, help="reference solution path")
    ap.add_argument("--student", type=Path, default=STU_PATH, help="student solution path")
    ap.add_argument("--json-out", type=Path, default=None, help="write JSON report to this path")
    ap.add_argument("--json-stdout", action="store_true", help="print only JSON report to stdout")
    ap.add_argument("--quiet", action="store_true", help="suppress verbose text report")
    args = ap.parse_args()

    # override globals ให้สอดคล้อง args
    REF_PATH = args.ref
    STU_PATH = args.student

    report = run_grade_once(REF_PATH, STU_PATH, verbose=not args.quiet)

    # เขียน/พิมพ์ JSON
    if args.json_out:
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.json_stdout:
        print(json.dumps(report, ensure_ascii=False))
