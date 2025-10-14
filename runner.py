# runner.py
# Python 3.10+
# ------------------------------------------------------------
# General Python grader (reference-guided), zero per-problem code change:
# - Infers input schema from reference (int/float/str)
# - Generates random test cases (--cases)
# - Instruments both ref & student to capture:
#     * all input() prompts (every call)
#     * all values before they are printed (labeled or unlabeled)
# - Learns output spec from ref (with fallback on first real run)
# - Compares PROMPT, STDOUT (optionally stripping prompts), and PROCESS (pre-print values)
# ------------------------------------------------------------

from __future__ import annotations
import sys, ast, json, subprocess, textwrap, difflib, time, tempfile, argparse, random, re
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any

# ===================== CLI =====================
def build_cli():
    p = argparse.ArgumentParser(description="General Python grader (reference-guided).")
    p.add_argument("--ref", required=True, help="path to reference solution .py")
    p.add_argument("--student", required=True, help="path to student solution .py")
    p.add_argument("--cases", type=int, default=3, help="number of random test cases")
    p.add_argument("--strict-prompt", action="store_true", help="require prompt to match exactly (default: loose)")
    p.add_argument("--strict-stdout", action="store_true", help="require stdout to match exactly (default: loose)")
    p.add_argument("--ignore-prompts-in-stdout", action="store_true",
                   help="strip all input() prompts from each program's stdout before comparing")
    p.add_argument("--float-tol", type=float, default=1e-9, help="tolerance for float comparisons")
    p.add_argument("--seed", type=int, default=42, help="random seed for reproducibility")
    return p.parse_args()

# ===================== Runtime helpers =====================
def run(path: Path, stdin_text: str, timeout: float = 2.0) -> tuple[int,str,str]:
    p = subprocess.Popen([sys.executable, str(path)],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True)
    try:
        out, err = p.communicate(stdin_text, timeout=timeout)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        p.kill()
        return -9, "", f"TIMEOUT>{timeout:.1f}s"

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

def normalize_spaces(s: str) -> str:
    return re.sub(r"[ \t]+", " ", s.strip())

# ===================== Input schema inference =====================
class InputSpec:
    def __init__(self, typ: str):  # "str" | "int" | "float"
        self.typ = typ

    def gen(self) -> str:
        if self.typ == "int":
            return str(random.randint(-10, 10))
        if self.typ == "float":
            val = random.uniform(-10, 10)
            return f"{val:.6f}".rstrip("0").rstrip(".")
        # str: สุ่มค่าทั่วไปที่มักเจอ
        choices = [
            "Alice", "Bob", "Charlie", "Delta",
            "alice@example.com", "bob@x.y", "user123@test.io"
        ]
        return random.choice(choices)

    def __repr__(self): return f"InputSpec({self.typ})"

def infer_input_schema_from_ref(ref_src: str) -> List[InputSpec]:
    tree = ast.parse(ref_src)
    specs: List[InputSpec] = []

    def is_input_call(n: ast.AST) -> bool:
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Name) and n.func.id == "input":
                return True
            if isinstance(n.func, ast.Name) and n.args:
                return any(is_input_call(a) for a in n.args)
        return False

    for node in tree.body:
        if isinstance(node, ast.Assign):
            val = node.value
            if isinstance(val, ast.Call) and isinstance(val.func, ast.Name) and val.func.id == "input":
                specs.append(InputSpec("str"))
            elif isinstance(val, ast.Call) and isinstance(val.func, ast.Name) and val.args:
                fname = val.func.id
                if any(is_input_call(a) for a in val.args):
                    if fname == "int":   specs.append(InputSpec("int"))
                    elif fname == "float": specs.append(InputSpec("float"))
                    elif fname == "str":   specs.append(InputSpec("str"))
                    else: specs.append(InputSpec("str"))
    return specs if specs else [InputSpec("str")]

def build_random_cases(specs: List[InputSpec], n: int) -> List[str]:
    cases = []
    for _ in range(n):
        vals = [sp.gen() for sp in specs]
        cases.append("\n".join(vals) + "\n")
    return cases

# ===================== Instrumentation (print tapping & prompt capture) =====================
class PrintTapper(ast.NodeTransformer):
    """
    ก่อนทุก print(...): เก็บค่าอาร์กิวเมนต์ทั้งหมดเป็น "value"
    - รองรับ f-string, list/tuple/dict, ฯลฯ
    นอกจากนี้ มีการ monkeypatch input() เพื่อบันทึก prompt ทุกครั้ง
    """
    def __init__(self):
        pass

    @staticmethod
    def _const_str(n: ast.AST) -> Optional[str]:
        return n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else None

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Call):
            call = node.value
            is_print = isinstance(call.func, ast.Name) and call.func.id == "print"
            if is_print:
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
import atexit, json, sys, builtins as __builtins
__CAPTURE = []
__PROMPTS = []

def __norm(v):
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
        return {"__type":"dict","items":[[k,__norm(v[k])] for k in v.keys()]}
    return {"__type":type(v).__name__,"repr":repr(v)}

def __record(kind, payload):
    __CAPTURE.append({"kind":"value","value":__norm(payload["value"])})

# --- monkeypatch input() เพื่อบันทึก prompt ทุกครั้ง ---
__orig_input = __builtins.input
def __patched_input(__prompt=None):
    p = "" if __prompt is None else str(__prompt)
    print(p, end="")
    try:
        __PROMPTS.append(p)
    except Exception:
        pass
    return sys.stdin.readline().rstrip("\n")
__builtins.input = __patched_input

def __dump():
    try:
        print("<<<CAPTURE>>>"+json.dumps(__CAPTURE, ensure_ascii=False), file=sys.stderr)
        print("<<<PROMPTS>>>"+json.dumps(__PROMPTS, ensure_ascii=False), file=sys.stderr)
    except Exception:
        print("<<<CAPTURE>>>[]", file=sys.stderr)
        print("<<<PROMPTS>>>[]", file=sys.stderr)
atexit.register(__dump)
"""

def instrument_source(src: str) -> str:
    tree = ast.parse(src)
    tree = PrintTapper().visit(tree)
    ast.fix_missing_locations(tree)
    pre = ast.parse(INJECT_PREAMBLE)
    pre.body.extend(tree.body)
    return ast.unparse(pre) if hasattr(ast, "unparse") else compile(pre, "<ast>", "exec")

def write_temp_instrumented(src_path: Path) -> Path:
    inst = instrument_source(src_path.read_text(encoding="utf-8"))
    tmp = Path(tempfile.gettempdir()) / f"__inst_{src_path.stem}_{int(time.time()*1000)}.py"
    tmp.write_text(inst if isinstance(inst, str) else "", encoding="utf-8")
    return tmp

# ===================== CAPTURE & PROMPT helpers =====================
def parse_capture(stderr_text: str) -> List[Dict[str,Any]]:
    last = ""
    for line in stderr_text.splitlines():
        if line.startswith("<<<CAPTURE>>>"):
            last = line[len("<<<CAPTURE>>>"):]
    try:
        return json.loads(last) if last else []
    except Exception:
        return []

def parse_prompts(stderr_text: str) -> list[str]:
    last = ""
    for line in stderr_text.splitlines():
        if line.startswith("<<<PROMPTS>>>"):
            last = line[len("<<<PROMPTS>>>"):]
    try:
        return json.loads(last) if last else []
    except Exception:
        return []

def strip_stdout_prompts(stdout_text: str, prompts: list[str]) -> str:
    """
    ลบ prompt ทุกครั้งที่เกิดขึ้นตามลำดับ รวมทั้งกรณีติดกัน/มีช่องว่างตามหลัง
    แล้ว trim ช่องว่างหัว-ท้ายอีกชั้น เพื่อให้เทียบผลลัพธ์ “จริง” ได้สะอาด
    """
    s = stdout_text
    for p in prompts:
        if not p:
            continue
        # ลบแบบ strict ที่หัวก่อน
        if s.startswith(p):
            s = s[len(p):]
        # ลบซ้ำให้หมดกรณี prompt เดียวกันข้างใน (concatenated)
        s = s.replace(p, "")
        # ลบช่องว่างที่อาจติดท้าย prompt (เช่น p ตามด้วย ' ' หรือ '\t')
        while s and s[0] in " \t":
            s = s[1:]
    return s.strip()

# ===================== Output spec learning (from ref) =====================
def group_unlabeled(caps: List[Dict[str,Any]]) -> List[Dict[str,Any]]:
    return [e["value"] for e in caps if e.get("kind")=="value"]

def norm_equals(n1: Dict[str,Any], n2: Dict[str,Any], float_tol: float) -> bool:
    t1, t2 = n1.get("__type"), n2.get("__type")
    if t1 != t2: return False
    if t1 == "float":
        return abs(float(n1["value"]) - float(n2["value"])) <= float_tol
    if t1 in ("int","str"):
        return n1["value"] == n2["value"]
    if t1 in ("tuple","list"):
        a1, a2 = n1["items"], n2["items"]
        if len(a1) != len(a2): return False
        return all(norm_equals(x,y,float_tol) for x,y in zip(a1,a2))
    if t1 == "dict":
        d1 = {k:v for k,v in n1["items"]}
        d2 = {k:v for k,v in n2["items"]}
        if set(d1.keys()) != set(d2.keys()): return False
        return all(norm_equals(d1[k], d2[k], float_tol) for k in d2.keys())
    return n1 == n2

def describe_norm(n: Dict[str,Any]) -> str:
    t = n.get("__type")
    if t in ("int","float","str"):
        return t
    if t in ("list","tuple"):
        inner = ", ".join(describe_norm(x) for x in n["items"])
        return f"{t}[{inner}]"
    if t == "dict":
        keys = [k for k,_ in n["items"]]
        return f"dict{{{', '.join(keys)}}}"
    return t or "unknown"

def learn_output_spec_from_ref(cap: List[Dict[str,Any]]) -> Dict[str,Any]:
    spec: Dict[str,Any] = {"unlabeled":[]}
    for v in group_unlabeled(cap):
        spec["unlabeled"].append(describe_norm(v))
    return spec

# ===================== Checking logic =====================
def compare_prompts(ref_prompt: str, stu_prompt: str, strict: bool) -> bool:
    if strict:
        return ref_prompt == stu_prompt
    return normalize_spaces(ref_prompt) == normalize_spaces(stu_prompt)

def compare_stdout(ref_out: str, stu_out: str, strict: bool) -> bool:
    if strict:
        return ref_out == stu_out
    a = "\n".join(normalize_spaces(l) for l in ref_out.splitlines())
    b = "\n".join(normalize_spaces(l) for l in stu_out.splitlines())
    return a == b

def compare_captures_against_spec(ref_cap, stu_cap, spec, float_tol: float) -> Tuple[bool,List[str]]:
    msgs = []
    ok = True
    ref_un = group_unlabeled(ref_cap)
    stu_un = group_unlabeled(stu_cap)
    if len(ref_un) != len(stu_un):
        ok = False; msgs.append(f"[unlabeled] count mismatch (ref={len(ref_un)} vs stu={len(stu_un)})")
    m = min(len(ref_un), len(stu_un))
    for i in range(m):
        if not norm_equals(ref_un[i], stu_un[i], float_tol):
            ok = False; msgs.append(f"[unlabeled] value mismatch at index {i} (expected {describe_norm(ref_un[i])})")
    return ok, msgs

# ===================== Main =====================
def main():
    args = build_cli()
    random.seed(args.seed)

    ref_path = Path(args.ref)
    stu_path = Path(args.student)
    if not ref_path.exists() or not stu_path.exists():
        print(f"[ERROR] missing {ref_path} or {stu_path}")
        sys.exit(1)

    ref_src = ref_path.read_text(encoding="utf-8")

    # 1) infer input schema & build test cases
    specs = infer_input_schema_from_ref(ref_src)
    tests = build_random_cases(specs, args.cases)

    # 2) PROMPT (first sniff) — quick sanity check only
    print("# ====== PROMPT check ======")
    ref_prompt = sniff_prompt(ref_path)
    stu_prompt = sniff_prompt(stu_path)
    ok_prompt = compare_prompts(ref_prompt, stu_prompt, args.strict_prompt)
    print(f"- ref prompt:\n{ref_prompt!r}")
    print(f"- stu prompt:\n{stu_prompt!r}")
    print(f"=> PROMPT_MATCH: {ok_prompt}")

    # 3) instrument both sides
    ref_inst = write_temp_instrumented(ref_path)
    stu_inst = write_temp_instrumented(stu_path)

    # 4) learn spec (with fallback)
    print("\n# ====== LEARNED OUTPUT SPEC (from reference) ======")
    learn_rc, learn_out, learn_err = run(ref_inst, tests[0], timeout=2.0)
    ref_cap0 = parse_capture(learn_err)
    learned_spec = learn_output_spec_from_ref(ref_cap0)

    def show_spec(spec):
        if spec["unlabeled"]:
            print("- unlabeled (by order):")
            for i, s in enumerate(spec["unlabeled"]):
                print(f"  [{i}] -> {s}")
        else:
            print("(empty for now; will derive from first test case run)")

    show_spec(learned_spec)

    print("\n# ====== RUN TESTS ======")
    out_ok = 0
    pre_ok = 0

    for idx, sin in enumerate(tests, 1):
        rc_r, out_r, err_r = run(ref_inst, sin, timeout=2.0)
        rc_s, out_s, err_s = run(stu_inst, sin, timeout=2.0)

        # fallback: learn spec from first real run if empty
        if not learned_spec["unlabeled"]:
            ref_cap_try = parse_capture(err_r)
            learned_spec = learn_output_spec_from_ref(ref_cap_try)

        # parse captures & prompts
        ref_cap = parse_capture(err_r)
        stu_cap = parse_capture(err_s)
        ref_prompts = parse_prompts(err_r)
        stu_prompts = parse_prompts(err_s)

        # strip prompts from stdout (if requested)
        out_r_cmp = out_r
        out_s_cmp = out_s
        if args.ignore_prompts_in_stdout:
            out_r_cmp = strip_stdout_prompts(out_r_cmp, ref_prompts)
            out_s_cmp = strip_stdout_prompts(out_s_cmp, stu_prompts)

        # ✅ เทียบเฉพาะสตริงหลัง strip (ไม่ผูกกับ return code เพื่อเลี่ยง false negative)
        out_equal = compare_stdout(out_r_cmp, out_s_cmp, args.strict_stdout)
        if out_equal:
            out_ok += 1

        pre_equal, pre_msgs = compare_captures_against_spec(ref_cap, stu_cap, learned_spec, args.float_tol)
        if pre_equal:
            pre_ok += 1

        print(f"- [case {idx}] stdout_equal={out_equal} preprint_equal={pre_equal}")
        if not out_equal:
            print("  stdout diff:")
            # ถ้า diff ว่าง ให้โชว์ repr เพื่อดีบั๊ก
            d = udiff(out_r_cmp, out_s_cmp)
            if not d.strip():
                print("    (no visible diff; debug)")
                print(f"    ref: {out_r_cmp!r}")
                print(f"    stu: {out_s_cmp!r}")
            else:
                print(textwrap.indent(d, "    "))
        if not pre_equal:
            print("  pre-print issues:")
            for m in pre_msgs:
                print("    " + m)

    # 6) SUMMARY
    print("\n# ====== SUMMARY ======")
    print(f"PROMPT(1): {1.0 if ok_prompt else 0.0:.1f}")
    print(f"STDOUT({len(tests)}): {out_ok:.1f} / {len(tests)} (strict={args.strict_stdout}, strip_prompts={args.ignore_prompts_in_stdout})")
    print(f"PROCESS-PREPRINT({len(tests)}): {pre_ok:.1f} / {len(tests)} (float_tol={args.float_tol})")
    total = (1.0 if ok_prompt else 0.0) + out_ok + pre_ok
    denom = 1 + len(tests) + len(tests)
    print(f"=> TOTAL: {total:.1f} / {denom}")

    if not ok_prompt:
        print("\n[HINT] Prompt ต่าง — ถ้าต้องการผ่อนปรนใช้โหมดไม่ strict หรือปรับข้อความให้ตรงกัน")
    if out_ok < len(tests):
        print("[HINT] STDOUT ต่าง — ใช้ --ignore-prompts-in-stdout เพื่อตัดข้อความ prompt ออกก่อนเทียบ หรือดู diff เพื่อแยกเรื่องรูปแบบ vs ค่า")
    if pre_ok < len(tests):
        print("[HINT] ค่าก่อนพิมพ์ต่าง — นักศึกษาอาจคำนวณสูตร/ชนิดไม่ตรงกับเฉลย")

if __name__ == "__main__":
    main()


def evaluate(ref_path: str, stu_path: str, *, cases: int = 3,
             strict_prompt: bool = False, strict_stdout: bool = False,
             ignore_prompts_in_stdout: bool = True, float_tol: float = 1e-9, seed: int = 42) -> dict:
    import random
    random.seed(seed)

    ref_path = Path(ref_path)
    stu_path = Path(stu_path)
    ref_src = ref_path.read_text(encoding="utf-8")

    # 1) infer input schema & testcases
    specs = infer_input_schema_from_ref(ref_src)
    tests = build_random_cases(specs, cases)

    # 2) prompt sniff (quick)
    ref_prompt = sniff_prompt(ref_path)
    stu_prompt = sniff_prompt(stu_path)
    ok_prompt = compare_prompts(ref_prompt, stu_prompt, strict_prompt)

    # 3) instrument
    ref_inst = write_temp_instrumented(ref_path)
    stu_inst = write_temp_instrumented(stu_path)

    # 4) learn spec (fallback ready)
    learn_rc, learn_out, learn_err = run(ref_inst, tests[0], timeout=2.0)
    ref_cap0 = parse_capture(learn_err)
    learned_spec = learn_output_spec_from_ref(ref_cap0)

    results = {
        "config": {
            "cases": cases, "strict_prompt": strict_prompt,
            "strict_stdout": strict_stdout, "ignore_prompts_in_stdout": ignore_prompts_in_stdout,
            "float_tol": float_tol, "seed": seed
        },
        "prompt": {"ref": ref_prompt, "stu": stu_prompt, "match": ok_prompt},
        "spec": learned_spec,
        "cases": []
    }

    out_ok = 0
    pre_ok = 0

    for idx, sin in enumerate(tests, 1):
        rc_r, out_r, err_r = run(ref_inst, sin, timeout=2.0)
        rc_s, out_s, err_s = run(stu_inst, sin, timeout=2.0)

        if not learned_spec["unlabeled"]:
            ref_cap_try = parse_capture(err_r)
            learned_spec = learn_output_spec_from_ref(ref_cap_try)

        ref_cap = parse_capture(err_r)
        stu_cap = parse_capture(err_s)
        ref_prompts = parse_prompts(err_r)
        stu_prompts = parse_prompts(err_s)

        out_r_cmp = out_r
        out_s_cmp = out_s
        if ignore_prompts_in_stdout:
            out_r_cmp = strip_stdout_prompts(out_r_cmp, ref_prompts)
            out_s_cmp = strip_stdout_prompts(out_s_cmp, stu_prompts)

        out_equal = compare_stdout(out_r_cmp, out_s_cmp, strict_stdout)
        if out_equal: out_ok += 1

        pre_equal, pre_msgs = compare_captures_against_spec(ref_cap, stu_cap, learned_spec, float_tol)
        if pre_equal: pre_ok += 1

        results["cases"].append({
            "index": idx,
            "stdin": sin,
            "stdout": {"ref": out_r_cmp, "stu": out_s_cmp, "equal": out_equal},
            "preprint": {"equal": pre_equal, "issues": pre_msgs},
            "rc": {"ref": rc_r, "stu": rc_s}
        })

    results["summary"] = {
        "prompt": 1.0 if ok_prompt else 0.0,
        "stdout_pass": out_ok,
        "preprint_pass": pre_ok,
        "denom": 1 + cases + cases,
        "total": (1.0 if ok_prompt else 0.0) + out_ok + pre_ok
    }
    return results
# ---- END ADD ----