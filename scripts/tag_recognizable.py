"""Tag each case recognizable: true/false from the contamination probe results.

A case is recognizable if any probe seed's guess names the real company: the guess matches
real_identity or an alias, ignoring case, punctuation and suffixes like "Inc".
Synthetic cases are recognizable: false unless the probe names something real with confidence 60 or more
(that would mean the synthetic case accidentally copies a real one, which is worth knowing).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_manifest import norm_name  # noqa: E402


def main() -> int:
    cases_path = ROOT / "data" / "cases.json"
    data = json.loads(cases_path.read_text(encoding="utf-8"))
    rows = []
    for c in data["cases"]:
        key = json.loads((ROOT / "data" / "answer_keys" / f"{c['id']}.json").read_text(encoding="utf-8"))
        names = {norm_name(n) for n in [key.get("real_identity"), *(key.get("aliases") or [])] if n}
        names.discard(None)
        probes = sorted((ROOT / "data" / "probes").glob(f"{c['id']}.seed*.json"))
        probes = [p for p in probes if not p.name.endswith(".meta.json")]
        if not probes:
            continue
        hit, guesses = False, []
        for p in probes:
            g = json.loads(p.read_text(encoding="utf-8"))
            guess, conf = str(g.get("guess", "")), int(g.get("confidence") or 0)
            guesses.append(f"{guess} ({conf})")
            ng = norm_name(guess) or ""
            if names and any(n and (n in ng or ng in n) and len(ng) >= 3 for n in names):
                hit = True
            if not names and ng and ng != "fictional" and conf >= 60:
                hit = True
        c["recognizable"] = hit
        c["probe_guesses"] = guesses
        rows.append((c["id"], c["track"], hit, "; ".join(guesses), key.get("real_identity")))
    cases_path.write_text(json.dumps(data, indent=1), encoding="utf-8")
    for r in rows:
        print(f"{r[0]:<5} {r[1]}  recognizable={str(r[2]):<5}  guess: {r[3]:<40}  actual: {r[4]}")
    n = sum(1 for r in rows if r[2])
    print(f"\n{n}/{len(rows)} recognizable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
