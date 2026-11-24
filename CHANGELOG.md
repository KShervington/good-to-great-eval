# CHANGELOG

Every phase and every improvement round is logged here: what ran, scores, the edits proposed (each with its hypothesis), the accept/reject decision and the reason, and limit pauses.

**If a session restarts, read this file, then `python -m harness status` and the ledger, before doing anything else.**

## 2026-11-23: Phase 0/1 dry run
- Confirmed model access: `claude-opus-5-5` (skill) and `claude-fable-5-2` (judge).
- Snapshotted the baseline skill to `skill_versions/v0/SKILL.md` (unchanged copy of `skills/good-to-great-anything/SKILL.md`).
- Built dry-run dossiers A01 (great), A02 (comparison) and D01 (synthetic startup), with answer keys.
- Built the harness (ledger, limit detection, pause/resume, lock, toasts, Task Scheduler script) and passed the fake-limit tests.
- Real dry run: 3 probes + 3 skill runs + 3 judge calls (1 seed). Results are in PLAN.md.
- Dry run: 9/9 jobs done, 0 failures, 0 limit pauses, $1.86 API-equivalent. Composite v0: A01 92.0, A02 90.0, D01 88.3. AUROC 0.75 (n=3, not meaningful yet).
- Fixed deterministic-check parsing (bold pseudo-headings, hedgehog sentence extraction, time-horizon numbers, a stray backspace in a regex).
- Tests: `tests/test_resume.py` PASS (45/45 jobs; killed mid-round; 0 lost; 0 duplicated; Fable continued during an Opus pause). `tests/test_limits.py` PASS.
