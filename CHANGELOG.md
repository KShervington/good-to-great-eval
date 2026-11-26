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

## 2026-11-24: Judge check (user approved the judge check, the Track B re-judge and round 1)
- `scripts/judge_validity.py`: 31 Fable calls, plus 2 re-runs. **The judge passed every test; no rubric change.**
  - Retest (12 untouched outputs judged again): 71 dimension scores, 89% identical, 100% within 1 point.
  - Swap (another case's output graded against this key): 4/4, D1 = 1, D2 = 2, D3 = 1 every time.
  - Fabricated untagged metrics: 4/4, D7 fell to 2 each time (from 4–5).
  - Verdict removed: 4/4, D8 fell to 2.
  - Track E told to exit its core: 3/3, D9 fell to 1–2.
  - Stop-doing removed: first pass 2/4. Both misses were a bug in the damage step, not the judge: a bold label (`**Top three stop-doing items:**`) was taken for a bullet, so the verdict's numbered "Stop…" items survived, and the judge rightly credited them. Fixed the label regex and re-ran those 2 (old judgments archived under `runs/judgments_archive/no_stop-transform-bug/`).
- Track B baseline: 18 judge jobs reset and re-run under the Track-E-only D9 rule (`scripts/rejudge.py`; old judgments archived under `runs/judgments_archive/b-not-already-great/`). Because the rubric didn't change, the other 108 baseline judgments stand.
- Round 1 queued: 126 v1 runs, 126 v1 judge calls, 126 v1-vs-v0 pairwise calls.

## 2026-11-25: Round 1 result: v1 ACCEPTED
- 378 jobs (126 v1 runs, 126 judge calls, 126 v1-vs-v0 pairwise), 0 failures, $114 API-equivalent (runs $37.36, judge $31.06, pairwise $45.56).
- One limit pause: Fable at 00:48 (reset parsed as 01:30), auto-resumed at 01:32. Wall-clock paused so far: 8.2 h total across the project.
- **Scorer fixes before the decision (they apply to v0 and v1 alike):**
  - A run that FAILs Gate 0 or Gate 1 is told to stop there. `sections`, `stop_doing_5` and `hedgehog_1s` are now waived for such runs, since the later sections are rightly absent. Whether the FAIL was right is still scored by D6. Before this fix, D12 (v0 and v1) and D05 (v1) lost points for stopping correctly.
  - In stewardship mode a "temptations to refuse" heading now counts as the stop-doing section.
  - These fixes raised the round-1 diff from +1.47 [0.47, 2.35] to +1.87 [0.98, 2.79]. Both pass.
- **Decision (`runs/decisions/r1.json`): ACCEPT.** Composite v1 92.88 vs v0 91.01. Diff +1.87, 95% CI [0.98, 2.79] (clustered bootstrap, 26 clusters). No dimension dropped more than 0.3. Growth +8.4%. Overfitting scan clean.
  - **Stopping rule:** +1.87 is below 2% of max (2.0 points). This round counts as the first "small gain" round. If round 2 also gains under 2.0, or its CI includes 0, the loop stops.
- **Per dimension (v0 → v1):** D8 verdict 4.48 → 4.96. D9 restraint (Track E) 3.53 → 4.33. D5 4.67 → 4.58. D7 4.19 → 4.17. D1, D2 and D3 flat.
- **Per track (composite v0 → v1):** A 90.4 → 90.9, B 94.3 → 94.9, C 84.1 → 87.6, D 91.6 → 93.7, E synthetic 90.2 → 95.8, E real 89.6 → 93.7.
  - AUROC 0.863 → 0.851 (within noise).
  - Track E mean greatness potential 65.0 → 69.9.
- **Hypotheses:**
  - E1 confirmed: 14/15 Track E outputs say "already great", and D9 rose 0.8.
  - E2 confirmed: D05 FAILs Gate 1 in 3/3 (v0 0/3).
  - E3 confirmed: D8 = 5 in 122/126 (v0 61/126).
- **Side effects found:**
  - **Honesty in the verdict (pairwise D7: v0 won 58, v1 won 19, 49 ties).** The judge's reasons: v1's shorter verdict dropped confidence statements, missing-data lists and assumption tags. 41/58 reasons mention flagging or marking, 26 mention uncertainty. The absolute D7 barely moved (−0.02), but the A/B comparison sees it clearly. The cause is E3's "leave out … caveats".
  - **Gate 1 false positive on a once-good company in crisis.** A24 (unsustained, key expects no gate fail) FAILs Gate 1 in 3/3 under v1 (2/3 under v0). The new "not yet good" wording catches a turnaround as if it were a startup that never worked.
  - **Decline register still generic.** D5 = 3 in 12 outputs (v0 9). A-track D5 fell 4.37 → 4.24.
  - B05/B08 (fallen companies at their peak) now open "already great, with early signs of decline". That is correct for those dossiers, and Track B composite rose.

### Round 2: candidate v2 (3 edits; +13.5% words over v0; overfitting scan clean)
- **E4, turnaround vs not-yet-good.** "Not yet good" is for a core that has never worked on its own. A once-good subject in crisis (mounting losses, lost share, funding squeeze) is run as a turnaround, with brutal facts and survival actions first. Hypothesis: fixes the A24 false FAIL (D6), and D05 still FAILs.
- **E5, honesty kept in the short verdict.** Add one line on how confident the verdict is and what it rests on. Keep `[ASSUMPTION]` tags on verdict figures. Caveats are no longer on the "leave out" list. Hypothesis: wins back pairwise D7 and raises absolute D7, with D8 unchanged.
- **E6, specific decline mechanisms first.** Gate 10 leads with the one or two mechanisms most likely to bring this subject down, from its own evidence, each with a warning sign and a trigger threshold. Then the remaining stages briefly. Hypothesis: D5 = 3 outputs fall, D5 mean rises.

## 2026-11-25: Round 2 result: v2 REJECTED, loop stops (user approved round 2)
- 378 jobs (126 v2 runs, 126 judge calls, 126 v2-vs-v1 pairwise; v1 runs and judgments reused from round 1), 0 failures, no limit pauses. About $114 API-equivalent; the project total is now $311.
- **Decision (`runs/decisions/r2.json`): REJECT.** Composite v2 93.63 vs v1 92.88. Diff +0.74, 95% CI [-0.23, 1.92] includes 0. The other checks pass: no dimension dropped more than 0.3, growth +13.5%, overfitting scan clean.
- **Per dimension (v1 -> v2):** D1 4.56 -> 4.64. D2 4.79 -> 4.75. D3 4.97 -> 4.92. D5 4.58 -> 4.63. D7 4.17 -> 4.27. D8 4.96 -> 4.98. D9 4.33 -> 4.33.
- **Per track (composite v1 -> v2):** A 91.1 -> 92.4, B 94.9 -> 95.1, C 87.6 -> 88.9, D 95.5 -> 95.7, E already great 94.4 -> 94.7, E already great but drifting 97.1 -> 96.2. These are recomputed with the round-1 scorer fixes; D and E are grouped differently from the round-1 entry.
- Pairwise overall: v2 won 64, v1 won 61, 1 tie.
- **Hypotheses:**
  - E4 confirmed: A24 now passes Gate 1 (PASS 1, CONDITIONAL 2; under v1 it was FAIL 3/3). D05 still FAILs. D6 is now correct in 126/126 (v1 123/126). A24 is the biggest gainer at +17.3.
  - E5 confirmed: pairwise D7 v2 won 69, v1 won 22, 35 ties. This reverses round 1's loss. Absolute D7 rose 0.10, and D8 held at 4.98.
  - E6 not confirmed: D5 = 3 or lower in 11 outputs (v1 12). Pairwise D5: v1 won 35, v2 won 29.
- Biggest losers: A17 -5.6, A23 -4.4, D06 -3.3, B08 -3.2. Spread across tracks, consistent with seed noise.
- **Stopping rule triggered.** Round 1 gained +1.87, under 2.0. Round 2's CI includes 0. That is two rounds in a row. The dev loop ends with **v1 as the final candidate**.
  - Note for the report: E4 and E5 each fixed what they targeted, but the overall gain didn't clear noise on 26 clusters, so neither goes in under the rules.
- Next: Phase 4, the held-out evaluation of v0 vs v1. It is 16 cases × 3 seeds, 240 calls (about $70: 96 runs, 96 judge calls, 48 pairwise), and needs the user's OK.

## 2026-11-25: Final candidate v3 = v2 with E6 reverted (user decision, made before any held-out results)
- The user asked whether v2, though rejected, should be kept. Points from the round-2 data:
  - P(v2 > v1) is 0.93 by clustered bootstrap.
  - E4's A24 fix is a deterministic gate check: 0/3 correct -> 3/3.
  - E5's honesty gain is pairwise D7 69 vs 22 (sign test p < 1e-6).
  - E6 missed its target: pairwise D5 favored v1 35 vs 29. It also accounts for v2's largest losses: A17 D5 4 -> 2 and 5 -> 2, A23 D5 5 -> 4 and 4 -> 3. The judge noted that v2 missed the decline mechanism the key expects. Leading with "the one or two most likely mechanisms" narrows the register and drops the expected one.
- **User decision: drop E6 and send the result to the held-out evaluation without another dev round.** Removing E6 puts Gate 10 back to v1's wording, which round 1 tested. E4 and E5 keep the wording round 2 tested. The held-out run is the test of the combination.
- This departs from the pre-set accept rule (v2's CI included 0). It is recorded here so the report states it plainly.
- `skill_versions/v3/SKILL.md`: 2,766 words, +11.6% over v0 (v1 +8.4%, v2 +13.5%). Overfitting scan clean.
- Phase 4 queued: v3 vs v0 on 16 held-out cases × 3 seeds (96 runs, 96 judge calls, 48 pairwise; about $70). Approved by the user.

## 2026-11-25: Phase 4: held-out evaluation and report
- 240 jobs (96 runs, 96 judge calls, 48 pairwise), 0 failures, no limit pauses, $72.63. The project total is $384.09 API-equivalent across 1,337 jobs.
- **v3 vs v0 on held-out (16 cases × 3 seeds, 10 clusters):** 93.95 vs 92.02. Diff +1.94, 95% CI [-0.86, 3.96]. P(v3 > v0) = 0.92. 5 clusters better, 4 worse.
- Dimensions: D8 4.52 -> 5.00 (A/B 24 vs 5). D9 3.0 -> 3.5. D7 +0.06. D1, D2, D3 and D5 flat (within ±0.03).
  - A/B overall: v0 25, v3 23.
  - D6 48/48 for both. AUROC 0.94 -> 0.95.
- Tracks: A +2.3, B +1.2, D -1.7 (3 synthetic cases: D07, D08), E +7.2.
  - E01 is run in stewardship mode in 3/3 (v0 0/3).
  - E05 is still "good, close to great" in 3/3.
- `scripts/final_eval.py` writes `runs/decisions/final.json` and the charts in `report/`. It was tested on dev data before any held-out file was read.
- Wrote `REPORT.md`. The deliverable is `deliverable/SKILL.md` (= v3) plus `deliverable/SKILL.diff` against the installed skill, which was not modified.

## 2026-11-25: Release
- The final skill (v3) was installed at the user's request over the claude.ai-synced copy in `~/.claude/skills/synced/.../good-to-great-anything/SKILL.md`. A later sync from claude.ai may overwrite it until the new version is uploaded there too.
- The skill now lives in its own public-ready repo, `good-to-great-anything` (plugin manifests, MIT license, a README and a worked example on fictional case D04 Linewright). This repo is now documentation of the evaluation: added README.md, removed `.claude-plugin/plugin.json` so the repo isn't taken for the plugin, and marked `calibration/` as superseded.
