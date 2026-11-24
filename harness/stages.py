"""What each stage sends to the model and where its output goes.

The skill-runner (stage `run`) reads only the dossier and the skill version. Answer keys are
read only by `judge` and `pairwise`, and the judge never sees which skill version produced
an analysis.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
from pathlib import Path

from .config import STAGE_EFFORT, STAGE_TIMEOUT_S, Paths


def load_cases(p: Paths) -> dict[str, dict]:
    data = json.loads((p.data / "cases.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in data["cases"]}


def skill_text(p: Paths, version: str) -> str:
    return (p.versions / version / "SKILL.md").read_text(encoding="utf-8")


def skill_hash(p: Paths, version: str) -> str:
    return hashlib.sha256(skill_text(p, version).encode("utf-8")).hexdigest()[:12]


def dossier_text(p: Paths, case: dict) -> str:
    path = Path(case["dossier"])
    if not path.is_absolute():
        path = p.data.parent / path
    return path.read_text(encoding="utf-8")


def answer_key_for_judge(p: Paths, case_id: str) -> str:
    key = json.loads((p.data / "answer_keys" / f"{case_id}.json").read_text(encoding="utf-8"))
    # The judge grades substance; real names would only bias it.
    for k in ("real_identity", "aliases", "notes"):
        key.pop(k, None)
    return json.dumps(key, indent=2, ensure_ascii=False)


# ------------------------------------------------------------------ output paths

def run_output(p: Paths, version: str, case_id: str, seed: int) -> Path:
    return p.runs / "outputs" / version / case_id / f"seed{seed}.md"


def judge_output(p: Paths, version: str, case_id: str, seed: int) -> Path:
    return p.runs / "judgments" / version / case_id / f"seed{seed}.json"


def pairwise_output(p: Paths, a: str, b: str, case_id: str, seed: int) -> Path:
    return p.runs / "pairwise" / f"{a}__vs__{b}" / case_id / f"seed{seed}.json"


def probe_output(p: Paths, case_id: str, seed: int) -> Path:
    return p.data / "probes" / f"{case_id}.seed{seed}.json"


def output_path(p: Paths, job) -> Path:
    s = job["stage"]
    if s == "run":
        return run_output(p, job["version"], job["case_id"], job["seed"])
    if s == "judge":
        return judge_output(p, job["version"], job["case_id"], job["seed"])
    if s == "pairwise":
        return pairwise_output(p, job["version"], job["other_version"], job["case_id"], job["seed"])
    if s == "probe":
        return probe_output(p, job["case_id"], job["seed"])
    raise ValueError(s)


# ------------------------------------------------------------------ prompts

def build_call(p: Paths, job, cases: dict) -> dict:
    """Return the call spec for a job: system prompt text, user text, effort, timeout."""
    stage = job["stage"]
    case = cases[job["case_id"]]
    dossier = dossier_text(p, case)
    if stage == "run":
        system = (p.prompts / "skill_preamble.md").read_text(encoding="utf-8") + "\n" + skill_text(p, job["version"])
        user = f"Run good-to-great-anything on this subject. Just run it.\n\n<dossier>\n{dossier}\n</dossier>"
    elif stage == "judge":
        system = (p.prompts / "judge_rubric.md").read_text(encoding="utf-8")
        analysis = run_output(p, job["version"], job["case_id"], job["seed"]).read_text(encoding="utf-8")
        user = (f"JUDGE_INPUT\n\n<dossier>\n{dossier}\n</dossier>\n\n<answer_key>\n{answer_key_for_judge(p, case['id'])}"
                f"\n</answer_key>\n\n<analysis>\n{analysis}\n</analysis>")
    elif stage == "pairwise":
        system = (p.prompts / "pairwise.md").read_text(encoding="utf-8")
        a = run_output(p, job["version"], job["case_id"], job["seed"]).read_text(encoding="utf-8")
        b = run_output(p, job["other_version"], job["case_id"], job["seed"]).read_text(encoding="utf-8")
        flip = pairwise_flip(job)
        first, second = (b, a) if flip else (a, b)
        user = (f"PAIRWISE_INPUT\n\n<dossier>\n{dossier}\n</dossier>\n\n<answer_key>\n"
                f"{answer_key_for_judge(p, case['id'])}\n</answer_key>\n\n<analysis_1>\n{first}\n</analysis_1>\n\n"
                f"<analysis_2>\n{second}\n</analysis_2>")
    elif stage == "probe":
        system = (p.prompts / "probe.md").read_text(encoding="utf-8")
        user = dossier
    else:
        raise ValueError(stage)
    return {"system": system, "user": user, "effort": STAGE_EFFORT[stage], "timeout": STAGE_TIMEOUT_S[stage]}


def pairwise_flip(job) -> bool:
    """Deterministic random order for A/B, so a re-run of the same job shows the same order."""
    h = hashlib.sha256(job["id"].encode()).digest()
    return h[0] % 2 == 1


def parse_json_reply(text: str) -> dict:
    t = text.strip()
    if "```" in t:
        parts = t.split("```")
        for part in parts[1::2]:
            part = part[4:] if part.startswith("json") else part
            try:
                return json.loads(part.strip())
            except json.JSONDecodeError:
                continue
    start, end = t.find("{"), t.rfind("}")
    if start >= 0 and end > start:
        return json.loads(t[start:end + 1])
    raise ValueError("no JSON object in reply")


def validate_and_render(job, text: str, meta: dict) -> tuple[str, str | None]:
    """Turn the model's text into the file we save. Returns (content, error)."""
    stage = job["stage"]
    if stage == "run":
        return text, None
    if meta.get("fake"):
        return json.dumps({"fake": True, "text": text, "meta": meta}, indent=2), None
    try:
        obj = parse_json_reply(text)
    except (ValueError, json.JSONDecodeError) as e:
        return "", f"unparseable {stage} reply: {e}"
    if stage == "pairwise":
        obj["_order_flipped"] = pairwise_flip(job)
        obj["_analysis_1_is"] = job["other_version"] if obj["_order_flipped"] else job["version"]
    obj["_meta"] = meta
    return json.dumps(obj, indent=2, ensure_ascii=False), None


# ------------------------------------------------------------------ atomic write

def atomic_write(path: Path, content: str, tmp_dir: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir.mkdir(parents=True, exist_ok=True)
    tmp = tmp_dir / f"{path.name}.{os.getpid()}.{random.randrange(1 << 30)}.tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def write_output(p: Paths, job, content: str, meta: dict) -> Path:
    """Write output, then its .meta.json last. Recovery treats a job as finished only if both exist."""
    out = output_path(p, job)
    atomic_write(out, content, p.tmp)
    atomic_write(out.with_suffix(out.suffix + ".meta.json"), json.dumps(meta, indent=2), p.tmp)
    return out


def recover_output(p: Paths, job) -> dict | None:
    out = output_path(p, job)
    meta = out.with_suffix(out.suffix + ".meta.json")
    if out.exists() and meta.exists():
        try:
            m = json.loads(meta.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None
        if m.get("job_id") == job["id"]:
            return m
    return None
