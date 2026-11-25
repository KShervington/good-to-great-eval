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

## 2026-11-23: Track E and Phase 1 completed
- Added Track E (already-great controls) at the user's request: new judge dimension D9 (restraint); the stop-doing check is waived for these cases; D2 is reinterpreted as the restraint decision.
- Built the full roster with 8 parallel research agents: 58 cases (A 28, B 9, C 2, D 12, E 7), all validated by `scripts/build_manifest.py`.
- Track C: 32 candidates screened, 1 pair passed (Stryker vs U.S. Surgical).
- Corrected Kimberly-Clark's transition year to 1972 in the A01 key (Collins's appendix).
- Splits: 42 dev / 16 held-out, clustered by company. Held-out runs are blocked in the harness without `--final-eval`.
- Contamination probes: 44/44 real cases recognized; 14/14 synthetic cases called fictional.

## 2026-11-24: Baseline round r0 in progress
- First real limit at 01:07: a shared session limit hit both Opus and Fable at once (the message: "You've hit your session limit · resets 1:50am (America/New_York)"). Usage up to that point: Opus 176 calls / $38.81 and Fable 120 calls / $32.42, about $71 API-equivalent in one window. Auto-resume at 01:52. 17 jobs remaining (3 paused_limit, 14 pending).
- Next step after the round finishes: `python scripts/calibration.py make`, then the user scores 6 sheets.

## 2026-11-24: Baseline round r0 complete
- 252/252 jobs done (126 skill runs + 126 judge calls on 42 dev cases × 3 seeds), 0 failures, $76.63 API-equivalent.
- One limit pause: a shared Opus+Fable session limit at 01:07, with the reset parsed as 01:50. The PC slept from 01:20 to 08:37, so the run resumed at 08:37. That's 7.5 h of wall-clock pause, 6.75 h of it caused by sleep. Fix: the harness now asks Windows to stay awake while work remains (SetThreadExecutionState, released on exit; `--allow-sleep` turns it off). `status` now reports wall-clock pause time (overlapping Opus/Fable pauses count once).
- **v0 baseline (dev):**
  - Composite: mean 87.7, SD 5.4.
  - Noise: mean within-case SD across seeds 2.8.
  - AUROC (greatness potential, Tracks A/C/D): 0.86.
  - Greatness potential by group: great 40.6, comparison 18.8, unsustained 22.3, fallen 25.8, already-great 67.2, drifting 56.0.
  - Track E restraint (D9): 3.5 for already-great, 3.7 for drifting.
- **Deterministic checks:**

  | Check | Pass rate |
  |---|---|
  | Sections | 123/126 |
  | Gate counts | 119/125 |
  | Stop-doing ≥5 | 110/111 |
  | Hedgehog one sentence | 108/126 |
  | `[ASSUMPTION]` tagging | 36/126 |
  | No long quote | 126/126 |
  | Greatness potential present | 126/126 |

- **Gate failures:** D12 (one-off artifact) fails Gate 0 in 3/3 seeds. D05 (not yet good) never fails Gate 1: it gets CONDITIONAL in 3/3 seeds.
- **Contamination:** no hindsight leaks; 1 output (B01 s2) named the real company.
- **Scorer fixes:**
  - The long-quote check paired quotes from different quotations, giving 23 false positives. It now flags only 15+-word quotations attributed to Collins or his books. Limitation: unattributed Collins quotes can't be detected without the books' text.
  - D9 (restraint) is now scored on Track E only, in the scorer and the prompts. The Track B keys carry `already_great`, so the judge had been scoring D9 there.
- **Calibration:** 6 sheets built in `calibration/` (A03, A25, B05, C01, D03, E06) for the user to score blind.

## 2026-11-24: Policy changes and round 1 proposal
- Human calibration dropped (user decision). Replaced by the automated judge check, `scripts/judge_validity.py` (31 judge calls).
- The skill may change its fundamental principles where the evidence shows an obvious improvement (user decision).
- The `[ASSUMPTION]` check is now reported only. Derived or approximate figures count as honestly marked.
- Composite after these scoring fixes: v0 dev mean 90.7. Track B judgments must be re-run, because they were judged while D2 and D9 treated B as "already great".

### Round 1: failure clusters (v0, dev)
1. **Already-great blindness:** D9 is 3 or below in 7 of 15 Track E outputs. The skill never says "already great", rates these companies 55–70, gives 3–4 CONDITIONAL gates, and writes 7–9 stop-doing items.
2. **Gate 1 never fails:** D05 (not yet good) gets CONDITIONAL in 3/3 seeds. CONDITIONAL is used as a hedge.
3. **Verdict too long:** D8 = 4 in 69 of 126 outputs. The judge's reasons: greatness-potential rationale, gate tallies and run notes in the verdict.
4. (Queued for round 2) **Boilerplate decline register:** D5 = 3 in 9 outputs. It walks all 5 stages instead of naming the subject's own mechanism.
5. (Queued) **Hedgehog over one sentence:** 18 of 126 outputs.

### Round 1: candidate v1 (3 edits; +8.4% words over v0; overfitting scan clean)
- **E1, a three-state Gate 1 with stewardship mode.** Hypothesis: giving the skill an explicit "already great" outcome (confirm the existing hedgehog, list only real temptations, no minimum stop-doing count, Gate 10 at the center) lifts D9 and E-track D1/D2 without hurting other tracks. The principle line gets an "already great" exception, and Gate 6's five-item minimum is waived in this mode.
- **E2, firm FAIL for not-yet-good.** Hypothesis: concrete signs of "not yet good" (dependence on the steward's network, unproven retention, hand-operated core) plus "don't soften to CONDITIONAL" make Gate 1 fail D05, raising D6, while good subjects still pass.
- **E3, verdict under about 150 words, with rationale, tallies and notes moved out.** Hypothesis: raises D8 with no loss elsewhere.
