"""Deterministic checks on skill outputs, plus aggregation of judge scores.

  python score.py check runs/outputs/v0/A01/seed1.md --dossier data/dossiers/A01.md
  python score.py table --version v0 [--cases dev]       # per-case scores (deterministic + judge)

Deterministic checks (each pass/fail):
  sections       every required section is present
  gate_counts    the gate-log summary counts match the gate-log table
  stop_doing_5   at least 5 stop-doing items
  hedgehog_1s    the Hedgehog Concept is one sentence
  assumptions    figures not in the dossier are tagged [ASSUMPTION]
  no_long_quote  no quotation of 15+ words (Collins or otherwise) that isn't from the dossier
  gp_present     the "Greatness potential: NN/100" line is present
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent

REQUIRED_SECTIONS = {
    "verdict": r"verdict|one[- ]screen|at a glance|summary",
    "great_version": r"great version",
    "hedgehog": r"hedgehog",
    "flywheel": r"flywheel",
    "bus": r"\bbus\b|people|who",
    "stop_doing": r"stop[- ]doing",
    "brutal_facts": r"brutal facts?",
    "ideology_bhag": r"bhag|core ideology|core values|purpose",
    "scorecard": r"scorecard",
    "next_90": r"90 days|ninety days|next 90",
    "recheck": r"re-?check",
    "risk_register": r"risk register",
    "gate_log": r"gate log",
}
VERDICTS = ("PASS", "CONDITIONAL", "FAIL")


def headings(md: str) -> list[tuple[int, str, int]]:
    """(level, text, line index) for markdown headings and bold-only lines used as headings."""
    out = []
    for i, line in enumerate(md.splitlines()):
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            out.append((len(m.group(1)), m.group(2).strip(), i))
        elif re.match(r"^\*\*[^*]{3,80}\*\*:?\s*$", line.strip()):
            out.append((7, line.strip().strip("*:"), i))
    return out


def section(md: str, pattern: str) -> str:
    """Text of the first heading matching pattern, up to the next heading of the same or higher level."""
    lines = md.splitlines()
    hs = headings(md)
    order = sorted(range(len(hs)), key=lambda k: (hs[k][0] == 7, k))  # real headings first
    for k in order:
        lvl, text, i = hs[k]
        if re.search(pattern, text, re.I):
            end = len(lines)
            for lvl2, _, j in hs[k + 1:]:
                if lvl2 <= lvl:
                    end = j
                    break
            return "\n".join(lines[i + 1:end])
    return ""


def check_sections(md: str) -> tuple[bool, list[str]]:
    texts = [t for _, t, _ in headings(md)]
    missing = [k for k, pat in REQUIRED_SECTIONS.items() if not any(re.search(pat, t, re.I) for t in texts)]
    # the verdict usually opens the reply without its own heading
    if "verdict" in missing and re.search(r"verdict", "\n".join(md.splitlines()[:15]), re.I):
        missing.remove("verdict")
    return not missing, missing


def gate_table_verdicts(md: str) -> dict[int, str]:
    sec = section(md, r"gate log") or md
    out = {}
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip(" *`") for c in line.strip().strip("|").split("|")]
        g = next((re.search(r"(?:gate\s*)?(\d{1,2})\b", c, re.I) for c in cells[:2] if re.search(r"\d", c)), None)
        v = next((c.upper() for c in cells for vv in VERDICTS if c.upper().startswith(vv)), None)
        if g and v:
            verdict = next(vv for vv in VERDICTS if v.startswith(vv))
            out.setdefault(int(g.group(1)), verdict)
    return out


def check_gate_counts(md: str) -> tuple[bool | None, str]:
    table = gate_table_verdicts(md)
    if not table:
        return False, "no gate-log table found"
    actual = {v: sum(1 for x in table.values() if x == v) for v in VERDICTS}
    sec = section(md, r"gate log") or md
    claimed = {}
    for v in VERDICTS:
        m = re.search(rf"(\d+)\s*(?:x\s*)?`?{v}`?S?\b", sec.replace("**", ""), re.I) or \
            re.search(rf"`?{v}`?S?\s*[:=]?\s*(\d+)\b", sec.replace("**", ""), re.I)
        if m:
            claimed[v] = int(m.group(1))
    if not claimed:
        return None, f"no summary counts to compare (table: {actual})"
    bad = {v: (claimed[v], actual[v]) for v in claimed if claimed[v] != actual[v]}
    return not bad, (f"mismatch claimed/actual {bad}" if bad else f"ok {actual}")


def check_stop_doing(md: str) -> tuple[bool, int]:
    sec = section(md, r"stop[- ]doing")
    items = [l for l in sec.splitlines() if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+\S", l)]
    rows = [l for l in sec.splitlines() if l.strip().startswith("|") and not re.match(r"^\|\s*:?-", l.strip())]
    n = max(len(items), max(0, len(rows) - 1))
    return n >= 5, n


def hedgehog_sentence(md: str) -> str:
    sec = section(md, r"hedgehog") or ""
    for pat in (r"^\s*>\s*\**(.+?)\**\s*$",
                r"\*\*(?:the )?(?:hedgehog(?: concept)?(?: sentence)?|sentence|concept)(?: \([^)]*\))?:?\*\*:?\s*(.+)",
                r"^\s*\*\*(.+?)\*\*\s*$"):
        m = re.search(pat, sec, re.I | re.M)
        if m and len(m.group(1).split()) >= 6:
            return m.group(1).strip().strip('*"“” ')
    m = re.search(r"hedgehog(?: concept)?(?: \([^)]*\))?\**\s*[:\-–]\s*\**[\"“*]?(.+?)[\"”*]?\**\s*$", md, re.I | re.M)
    return m.group(1).strip() if m else ""


def check_hedgehog_one_sentence(md: str) -> tuple[bool, str]:
    s = hedgehog_sentence(md)
    if not s:
        return False, "hedgehog sentence not found"
    s_clean = re.sub(r"\[ASSUMPTION\]|e\.g\.|i\.e\.|vs\.|etc\.|\b[A-Z]\.", "", s)
    n = len([x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", s_clean.strip()) if x.strip()])
    return n == 1, s[:200]


_NUM = re.compile(r"(?<![\w.])(\$?\d[\d,]*(?:\.\d+)?\s*(?:%|x|×|[kKmMbB](?:n)?\b|bps)?)")
_STRUCTURAL = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "15", "30", "90", "100"}


def _norm(n: str) -> str:
    return re.sub(r"[\s,$]", "", n).lower().replace("×", "x")


def check_assumptions(md: str, dossier: str) -> tuple[bool, list[str]]:
    """Numbers that aren't in the dossier must sit on a line (or table row) tagged [ASSUMPTION]."""
    gp = greatness_potential(md)
    dnums = {_norm(m) for m in _NUM.findall(dossier)}
    dnums |= {re.sub(r"[^\d.]", "", x) for x in dnums}
    flagged = []
    for line in md.splitlines():
        if re.search(r"\[ASSUMPTION|assum|estimate|target|bhag", line, re.I):
            continue
        if re.match(r"^\s*#", line) or re.search(r"greatness potential", line, re.I):
            continue
        for raw in _NUM.findall(line):
            n = _norm(raw)
            digits = re.sub(r"[^\d.]", "", n)
            if not digits or digits in _STRUCTURAL and not re.search(r"[%$xkmb]", n):
                continue
            if re.fullmatch(r"(19|20)\d\d", digits):  # years
                continue
            if re.search(rf"{re.escape(raw.strip())}\s*(?:[-–]\s*\d+\s*)?\+?\s*(?:months?|years?|yrs?|days?|weeks?|quarters?|steps?|gates?|items?|facts?)\b", line, re.I):
                continue  # horizons and counts of the analysis's own parts, not metrics
            if re.search(rf"(?:day|week|month|year|gate|stage|step|item|#)\s*{re.escape(digits)}\b", line, re.I):
                continue  # "by day 60", "Stage 3", "#4"
            if gp is not None and digits == str(gp):
                continue
            if re.search(rf"gate\s*{re.escape(digits)}\b", line, re.I):
                continue
            if n in dnums or digits in dnums:
                continue
            flagged.append(f"{raw.strip()}  <- {line.strip()[:100]}")
    return not flagged, flagged


def check_no_long_quote(md: str, dossier: str) -> tuple[bool, list[str]]:
    quotes = re.findall(r"[\"“]([^\"”\n]{20,})[\"”]", md)
    long_q = [q for q in quotes if len(q.split()) >= 15 and q.strip()[:40] not in dossier]
    return not long_q, long_q


def greatness_potential(md: str) -> int | None:
    m = re.search(r"greatness potential\**\s*[:=]\s*\**\s*(\d{1,3})\s*/\s*100", md, re.I)
    return int(m.group(1)) if m else None


def check_all(md: str, dossier: str, waive: tuple | set = ()) -> dict:
    s_ok, s_missing = check_sections(md)
    g_ok, g_msg = check_gate_counts(md)
    sd_ok, sd_n = check_stop_doing(md)
    h_ok, h_s = check_hedgehog_one_sentence(md)
    a_ok, a_list = check_assumptions(md, dossier)
    q_ok, q_list = check_no_long_quote(md, dossier)
    gp = greatness_potential(md)
    checks = {
        "sections": s_ok, "gate_counts": g_ok, "stop_doing_5": sd_ok, "hedgehog_1s": h_ok,
        "assumptions": a_ok, "no_long_quote": q_ok, "gp_present": gp is not None,
    }
    for w in waive:  # e.g. Track E (already great) waives stop_doing_5: restraint is the right answer there
        checks[w] = None
    scored = [v for v in checks.values() if v is not None]
    return {
        "checks": checks,
        "pass_rate": sum(1 for v in scored if v) / len(scored),
        "details": {"missing_sections": s_missing, "gate_counts": g_msg, "stop_doing_items": sd_n,
                    "hedgehog": h_s, "untagged_figures": a_list[:20], "long_quotes": q_list,
                    "gate_verdicts": gate_table_verdicts(md)},
        "greatness_potential": gp,
    }


# ---------------------------------------------------------------- aggregation

JUDGE_DIMS = ["D1", "D2", "D3", "D5", "D7", "D8", "D9"]  # D9 (restraint) applies to already-great cases only


def gate_fail_correct(md: str, key: dict) -> bool | None:
    """D6: Gate 0/1 should FAIL exactly when the answer key expects it."""
    exp = key.get("expected_gate_fail")
    v = gate_table_verdicts(md)
    failed_01 = v.get(0) == "FAIL" or v.get(1) == "FAIL"
    if exp is None:
        return not failed_01
    return v.get(int(exp)) == "FAIL"


def case_record(root: Path, version: str, case: dict, seed: int) -> dict | None:
    out = root / "runs" / "outputs" / version / case["id"] / f"seed{seed}.md"
    if not out.exists():
        return None
    md = out.read_text(encoding="utf-8")
    dossier = (root / case["dossier"]).read_text(encoding="utf-8")
    key = json.loads((root / "data" / "answer_keys" / f"{case['id']}.json").read_text(encoding="utf-8"))
    det = check_all(md, dossier, waive=tuple(key.get("waive_checks", ())))
    rec = {"case": case["id"], "track": case["track"], "group": case["group"], "seed": seed,
           "recognizable": case.get("recognizable"), "det_pass_rate": det["pass_rate"],
           "checks": det["checks"], "gp": det["greatness_potential"], "D6": gate_fail_correct(md, key),
           "label": key.get("greatness_label"), "already_great": bool(key.get("already_great"))}
    jpath = root / "runs" / "judgments" / version / case["id"] / f"seed{seed}.json"
    if jpath.exists():
        j = json.loads(jpath.read_text(encoding="utf-8"))
        for d in JUDGE_DIMS:
            rec[d] = (j.get(d) or {}).get("score")
        rec["hindsight_leak"] = j.get("hindsight_leak")
    return rec


def composite(rec: dict) -> float | None:
    """0-100. 80% judge dims (mean of available 1-5 scores, rescaled) + 20% deterministic pass rate.
    D6 (gate fail correctness) is folded into the deterministic part as one more check."""
    js = [rec.get(d) for d in JUDGE_DIMS if isinstance(rec.get(d), (int, float))]
    if not js:
        return None
    jmean = (sum(js) / len(js) - 1) / 4
    det = rec["det_pass_rate"]
    if rec.get("D6") is not None:
        det = (det * 7 + (1.0 if rec["D6"] else 0.0)) / 8
    return round(100 * (0.8 * jmean + 0.2 * det), 2)


def auroc(scores_labels: list[tuple[float, int]]) -> float | None:
    pos = [s for s, l in scores_labels if l == 1]
    neg = [s for s, l in scores_labels if l == 0]
    if not pos or not neg:
        return None
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("output")
    c.add_argument("--dossier", required=True)
    t = sub.add_parser("table")
    t.add_argument("--version", default="v0")
    t.add_argument("--cases", default="all")
    t.add_argument("--seeds", type=int, default=3)
    t.add_argument("--root", default=str(PROJECT))
    a = ap.parse_args(argv)
    if a.cmd == "check":
        res = check_all(Path(a.output).read_text(encoding="utf-8"), Path(a.dossier).read_text(encoding="utf-8"))
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    root = Path(a.root)
    cases = json.loads((root / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]
    if a.cases in ("dev", "heldout"):
        cases = [x for x in cases if x.get("split") == a.cases]
    elif a.cases == "dryrun":
        cases = [x for x in cases if x.get("dry_run")]
    recs = []
    for case in cases:
        for s in range(1, a.seeds + 1):
            r = case_record(root, a.version, case, s)
            if r:
                r["composite"] = composite(r)
                recs.append(r)
    cols = ["case", "seed", "group", "composite", "det_pass_rate", "gp"] + JUDGE_DIMS + ["D6"]
    print("\t".join(cols))
    for r in recs:
        print("\t".join("" if r.get(k) is None else (f"{r[k]:.2f}" if isinstance(r[k], float) else str(r[k]))
                        for k in cols))
    sl = [(r["gp"], r["label"]) for r in recs if r["gp"] is not None and r["label"] in (0, 1)]
    print(f"\nAUROC (greatness potential vs label): {auroc(sl)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
