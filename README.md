# good-to-great-eval

An evaluation suite and improvement loop for the **[good-to-great-anything](https://github.com/KShervington/good-to-great-anything)** Claude skill. That repo has the skill itself. This one shows how it was tested and how the final version was chosen.

**Start with [REPORT.md](REPORT.md):** the results, the changes made and why, and the limits. [CHANGELOG.md](CHANGELOG.md) is the step-by-step log of every phase and decision. [PLAN.md](PLAN.md) is the original design.

## In short

- **58 cases** in five tracks. The cases are split 42 dev / 16 held-out, clustered by company.
  - **A:** Collins's great companies and their direct comparisons, dated before the transition.
  - **B:** great companies that later fell, dated at their peak.
  - **C:** a *Great by Choice* pair.
  - **D:** synthetic subjects with planted traps (startups, solo products, careers, nonprofits, teams, a civic initiative).
  - **E:** already-great companies, where the right answer is mostly "leave it alone".
- **Two models.** The skill runs on Claude Opus 5.5. A separate judge, Claude Fable 5.2, grades each output against a hidden answer key, so nothing is graded by the model that produced it.
  - The judge scores hedgehog match, stop-doing, brutal facts, decline risk, honesty, verdict quality and restraint.
  - Deterministic checks cover structure, the gate log and whether Gates 0/1 fail when they should.
  - The composite is 0–100.
- **The improvement loop.**
  - At most 3 edits per round, each with a hypothesis.
  - A round is accepted only if the clustered-bootstrap 95% CI of the paired gain excludes 0, no dimension drops more than 0.3, and the skill grows no more than 20%.
  - It stops after two rounds in a row each gaining less than 2 points.
- **Outcome.**
  - Round 1 was accepted (+1.87). Round 2 was rejected (+0.74, CI includes 0), which ended the loop.
  - The final skill is round 2's version with its one failed edit removed.
  - On the held-out set it scored 93.95 vs the original's 92.02 (+1.9, CI [−0.9, 4.0]).

## Layout

| Path | What it is |
|---|---|
| `skill_versions/v0`–`v3` | Every version of the skill tested. v0 is the original and v3 is the final. |
| `skills/good-to-great-anything/` | Snapshot of the original skill as it was installed at the start (= v0). The current skill lives in the other repo. |
| `deliverable/` | The final `SKILL.md` and its diff against the original. |
| `data/` | Case manifest (`cases.json`), dossiers, answer keys, sources and contamination probes. |
| `prompts/` | Judge rubric, pairwise prompt, probe prompt, skill preamble. |
| `harness/` | Resumable job runner: SQLite ledger, usage-limit pause/resume, concurrency, notifications. |
| `score.py`, `analyze.py` | Deterministic checks, composite score, bootstrap decisions. |
| `scripts/` | Manifest builder, judge validity check, re-judge, final evaluation and charts. |
| `runs/` | Every output, judgment, pairwise comparison and decision file. |
| `report/` | Charts used in REPORT.md. |
| `tests/` | Pause/resume and limit-handling tests. |
| `calibration/` | Human calibration sheets, superseded by the automated judge check. |

## Reproducing

Requires Python 3.11+ and the Claude Code CLI with access to both models.

```
python -m harness status
python -m harness enqueue --round r1 --version v1 --compare-to v0 --cases dev --seeds 3 --stages run,judge,pairwise
python -m harness run --concurrency 2
python analyze.py decide --round r1 --candidate v1 --baseline v0
python scripts/final_eval.py --final v3
```

The harness is safe to stop and restart. It picks up from the ledger and sleeps through usage limits. Held-out cases only run with `--final-eval`. A full dev round is 378 model calls, about $114 API-equivalent.

## Caveats

This suite measures agreement with Collins's own analysis of each case, not real-world outcomes. Collins's method is retrospective, and some of his great companies later fell. The skill model also recognized every real company despite the anonymization. See "Known limits" in [REPORT.md](REPORT.md).
