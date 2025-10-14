# orchestrator_llm.py
import os, json, requests
from pathlib import Path
import importlib.util
import argparse

# ---- load runner.evaluate from runner.py ----
RUNNER_PATH = Path(__file__).parent / "runner.py"
spec = importlib.util.spec_from_file_location("grader_runner", RUNNER_PATH)
runner = importlib.util.module_from_spec(spec)  # type: ignore
spec.loader.exec_module(runner)                 # type: ignore

# ---- LLM provider auto-detect: OpenAI -> Ollama -> fallback ----
OPENAI_KEY   = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OLLAMA_HOST  = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral:7b")

def use_openai() -> bool:
    return bool(OPENAI_KEY)

def use_ollama() -> bool:
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
        return r.status_code == 200
    except Exception:
        return False

def llm_feedback(prompt: str) -> str:
    # 1) OpenAI
    if use_openai():
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_KEY)
            res = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role":"system","content":"You are a precise code grading assistant. Be concise, actionable, and cite concrete mismatches."},
                    {"role":"user","content": prompt}
                ],
                temperature=0.2,
            )
            return res.choices[0].message.content.strip()
        except Exception as e:
            return f"(LLM error/OpenAI: {e})"

    # 2) Ollama (local, free)
    if use_ollama():
        try:
            resp = requests.post(
                f"{OLLAMA_HOST}/api/chat",
                json={
                    "model": OLLAMA_MODEL,
                    "messages": [
                        {"role":"system","content":"You are a precise code grading assistant. Be concise, actionable, and cite concrete mismatches. Reply in Thai."},
                        {"role":"user","content": prompt}
                    ],
                    "options": {"temperature": 0.2},
                    "stream": False   # <<<< ปิดสตรีมให้ส่ง JSON เดียว
                },
                timeout=180
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("message", {}).get("content", "").strip() or "(LLM/Ollama returned empty content)"
        except Exception as e:
            return f"(LLM error/Ollama: {e})"

    # 3) fallback: rule-based short line
    return "(no-LLM) " + prompt.splitlines()[0][:140]

def build_llm_prompt(task_name: str, results: dict) -> str:
    cfg = results["config"]; sm = results["summary"]
    lines = [
        f"Task: {task_name}",
        "Scoring: PROMPT, STDOUT (after stripping input prompts), PROCESS-PREPRINT.",
        f"Config: strict_prompt={cfg['strict_prompt']} strict_stdout={cfg['strict_stdout']} strip_prompts={cfg['ignore_prompts_in_stdout']} tol={cfg['float_tol']}",
        f"Summary: prompt={sm['prompt']} stdout_pass={sm['stdout_pass']}/{cfg['cases']} preprint_pass={sm['preprint_pass']}/{cfg['cases']}",
    ]
    bad = [c for c in results["cases"] if (not c["stdout"]["equal"] or not c["preprint"]["equal"])]
    for c in bad[:6]:
        lines += [f"\nCase {c['index']}:"]
        if not c["stdout"]["equal"]:
            lines += [
                "- STDOUT mismatch (after stripping prompts)",
                f"  ref={repr(c['stdout']['ref'])}",
                f"  stu={repr(c['stdout']['stu'])}",
            ]
        if not c["preprint"]["equal"]:
            lines += ["- PRE-PRINT issues:"]
            for m in c["preprint"]["issues"]:
                lines += [f"  * {m}"]
    lines += ["\nเขียนฟีดแบ็กภาษาไทยแบบสั้น กระชับ เป็นข้อ ๆ และชี้ว่าควรแก้ตรงไหน."]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description="LLM Orchestrator for grader")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--student", required=True)
    ap.add_argument("--cases", type=int, default=4)
    ap.add_argument("--strict-prompt", action="store_true")
    ap.add_argument("--strict-stdout", action="store_true")
    ap.add_argument("--ignore-prompts-in-stdout", action="store_true", default=True)
    ap.add_argument("--float-tol", type=float, default=1e-9)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--json-out", default="")
    args = ap.parse_args()

    results = runner.evaluate(
        ref_path=args.ref,
        stu_path=args.student,
        cases=args.cases,
        strict_prompt=args.strict_prompt,
        strict_stdout=args.strict_stdout,
        ignore_prompts_in_stdout=args.ignore_prompts_in_stdout,
        float_tol=args.float_tol,
        seed=args.seed,
    )

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    task_name = Path(args.ref).stem
    prompt = build_llm_prompt(task_name, results)
    feedback = llm_feedback(prompt)

    sm = results["summary"]
    print("# ====== SCORE ======")
    print(f"TOTAL: {sm['total']} / {sm['denom']}")
    print(f"PROMPT={sm['prompt']}  STDOUT_PASS={sm['stdout_pass']}/{results['config']['cases']}  PREPRINT_PASS={sm['preprint_pass']}/{results['config']['cases']}")
    print("\n# ====== FEEDBACK (LLM) ======")
    print(feedback)

if __name__ == "__main__":
    main()
