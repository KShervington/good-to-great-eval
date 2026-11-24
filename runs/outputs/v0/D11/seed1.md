# Good to Great: Heart Failure Transitions Program (HFTP), St. Aldric Regional Medical Center

## One-screen verdict

**Hedgehog Concept (working hypothesis):** *HFTP finds and fixes the specific reasons each heart-failure patient in our region keeps coming back, through medications, home conditions and follow-up, and stays with them until they are stable rather than until day 30.*

**Most urgent brutal fact:** at 90 days, enrolled and non-enrolled patients are readmitted at almost the same rate: **32.7% vs 33.9%**. Between day 31 and day 90, after "graduation," enrolled patients are readmitted *more* often than non-enrolled patients (+16.8 points vs +12.1). The program's headline 30-day gap may be mostly a selection effect, a delay in readmissions, or both. This number appears only in an accreditation checklist. It is not in the memo.

**Weakest flywheel link:** the step from *"we fixed the cause"* to *"verified readmissions avoided."* The program has no fair comparison group, no mortality data and no cost per readmission. Until those exist, its value case rests on stories and a confounded comparison.

**Top three stop-doing items:**
1. **Don't take on leadership of Hospital at Home now.** Offer a referral and advisory role instead.
2. **Stop graduating every patient at day 30.** End follow-up based on stability and risk, not on the penalty window.
3. **Stop presenting enrolled vs not-enrolled as the program's effect.**

**Missing numbers that would change this answer:**
- A risk-adjusted 30- and 90-day comparison with nursing-facility discharges taken out of the comparator.
- Mortality by group.
- Reason codes for the day 31–90 readmissions.
- Finance's cost per readmission and bed occupancy.
- Whether readmissions to *other* hospitals are captured.

Greatness potential: 32/100

> *Run notes: autonomous mode. This session had no memory, past-chat search or web research, so there was no prior run to baseline against, and market and regulatory facts were not checked. Every inference is marked `[ASSUMPTION]`. All arithmetic uses only the dossier's figures.*

---

## 1. The great version in one paragraph

Three years from now, HFTP is the team St. Aldric's finance office cites by name. It cites the team because a risk-adjusted analysis shows HFTP prevents readmissions that would otherwise have happened, and keeps preventing them at 90 days, not because of a letter to the CEO. The team doesn't run one uniform six-touch protocol. Each patient is assigned a risk tier at the bedside. Low-risk patients get a light touch. High-risk patients get a pharmacist medication review within days, including on Fridays and weekends, a community health worker who goes looking for the people who can't be reached by phone, and follow-up that ends when the patient is stable, not when the penalty clock stops. Every readmission of an enrolled patient gets a blameless review, and every review sharpens the protocol. The team is the same size or modestly larger. It is narrower in scope, deeper in effect, and it can run without its founding manager.

## 2. The Hedgehog Concept

| Circle | Candidates considered | Kept | Ruled out (and why) |
|---|---|---|---|
| **Best in world at** (narrow world: heart-failure patients leaving St. Aldric) | (a) The 30-day post-discharge bridge; (b) finding and fixing the root causes of readmission (medications, home, follow-up gaps); (c) home-based acute care; (d) long-term heart-failure management | **(b)**. The Mr. D. case (duplicate diuretics from two specialists), 82% seven-day follow-up and the community health workers' reach into homes all point to the same thing: root-cause detection across fragmented care. | (a) The 90-day data suggests the bridge alone doesn't last. (c) Hospital at Home is acute inpatient care: physician oversight, round-the-clock escalation and vendor monitoring. That is a different discipline from transitions nursing. (d) Long-term management belongs to the cardiology clinic `[ASSUMPTION: one exists]`. |
| **Resource engine** (team inside a hospital: budget and headcount leverage) | Penalty dollars avoided; readmissions avoided at 30 days per dollar; hospital days avoided per dollar; **verified 90-day readmissions avoided per FTE** | **Verified 90-day readmissions avoided per FTE.** 88% of the budget is salaries ($1.291M of $1.46M), so FTE is the real constraint. | Penalty dollars: the federal readmissions penalty covers several conditions across the whole hospital and uses lagged performance periods `[ASSUMPTION: general knowledge, not checked in this session]`, so HFTP can't claim the drop from 1.12% to 0.71%. A 30-day metric rewards pushing readmissions past day 30. |
| **Deep passion** | Patients "making it home and staying home"; home visits; the Hospital at Home opportunity | **"Make it home and stay home."** This is in the founding mission and in every story. | Passion for home-based care *in general* pulls the team toward Hospital at Home. That passion is real, but it is a pull away from the hedgehog, not part of it. |

**Denominator:** verified readmissions avoided at 90 days, per FTE, against a fair comparison group.

**Where things stand now (naive, unadjusted, using only dossier arithmetic):**

| Window | Readmissions avoided (estimate) | Per FTE | Cost per avoided readmission |
|---|---|---|---|
| 30 days | (21.8% − 15.9%) × 1,146 ≈ 68 | ≈ 5.8 | ≈ $21,600 |
| 90 days | (33.9% − 32.7%) × 1,146 ≈ 14 | ≈ 1.2 | ≈ $106,000 |

Both figures are almost certainly wrong, because the comparison is confounded. That is exactly the point: nobody knows the true number yet.

**Confirmation tests.** This is a working hypothesis. It is confirmed if:
1. A risk-adjusted 90-day comparison shows a meaningful gap.
2. Day 31–90 readmission reviews show causes the team could have caught (medications, weight gain, missed visits).
3. Program components with root-cause work (the pharmacist call, the community health worker visit) correlate with fewer 90-day readmissions more than the purely navigational touches do.

It is disconfirmed if the adjusted effect is about zero even after redesign. Then HFTP should be honest that it is a *good* process program and size itself to the process value it delivers.

## 3. The flywheel

```
  ┌──────────────────────────────────────────────┐
  │ 1. Reach every HIGH-RISK HF discharge         │
  │    (incl. weekends, phone-unreachable)        │
  └───────────────┬──────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────┐
  │ 2. Find & fix the root cause                  │
  │    meds (pharmacist) · home (CHW) ·           │
  │    follow-up (navigator) · social (LCSW)      │
  └───────────────┬──────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────┐
  │ 3. Stay until stable (risk-tiered, ≤90 days)  │
  └───────────────┬──────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────┐
  │ 4. VERIFIED 90-day readmissions avoided / FTE │  ◄── WEAKEST LINK
  └───────────────┬──────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────┐
  │ 5. Credible value case (finance $, beds)      │
  │    + readmission reviews → better protocol    │
  └───────────────┬──────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────┐
  │ 6. Protected capacity aimed at highest-yield  │
  │    causes (pharmacist, CHW)                   │──► back to 1
  └──────────────────────────────────────────────┘
```

**Current push:**
- **Turn 1:** measure fairly, at 90 days, with mortality included. This repairs link 4.
- **Turn 2:** review why enrolled patients come back between day 31 and day 90. This redesigns link 3.

Everything else waits for these two turns.

**Doom-loop check:**

| Signal | Present? |
|---|---|
| Big program to jump-start momentum | **Yes, risk.** Hospital at Home adds 6 FTE to an 11.6 FTE team (+52%), brings a vendor platform, rests on one external study, and comes with an enthusiastic board. |
| Chasing a metric without understanding it | **Mild.** The weekend shift chases the enrollment rate without knowing who the unreached patients are. |
| Reaction without understanding | **Mild.** "Show our value" is listed third, behind growth. |
| Repeated new directions | **Not yet.** Four years of a consistent protocol is a real asset. |

## 4. The bus

| Person / commitment | Call | Reason |
|---|---|---|
| Colette Marsh, manager | **Keep, with a choice to make** | She is a strong operator: low turnover, staff growth, growing enrollment. She has to choose between running HFTP and becoming the Hospital at Home director. She can't do both well. Either choice is legitimate. Going after both is the risk. |
| Five nurse navigators | **Keep, and change how they work** | Move them from one uniform protocol to risk-tiered caseloads. Give them judgment over how intensive each patient's follow-up is, within each tier. |
| Pharmacists (1.6 FTE) | **Keep, and point them at the biggest opportunity** | They are the root-cause mechanism behind the best outcome on record (Mr. D.) and the scarcest resource. Close the Friday gap first. |
| The pharmacist who pulled the 90-day data | **Keep, and give a new seat: outcome truth-teller** | This person surfaced the program's most important fact. Make that a formal role: co-owner of the quarterly outcome report. |
| Community health workers (2) | **Keep, and move seats** | Point them at the patients who can't be reached by phone and are currently missed, not only at the scheduled day-14 visit. |
| Social worker Ana (newly licensed) | **Move seat** | Give her the high-risk psychosocial caseload and the complex patients in days 31–90. |
| Second social worker | Keep | `[ASSUMPTION: aligned; no information in the dossier]` |
| **Hospital at Home** (as an HFTP commitment) | **Off this bus** | It belongs on a different bus: a team led by a physician with acute-care escalation. HFTP can be its referral and post-discharge partner. |
| **Day-30 graduation** (as a fixed rule) | **Off** | It is designed around the penalty window, not around patient stability. |
| **Enrollment rate** (as the headline goal) | **Off** | Replace it with coverage of *high-risk* discharges. |
| **Missing:** quality or finance analyst (part-time is fine) | **Add first** | Needed for risk adjustment, mortality, out-of-hospital readmissions and cost per readmission. |
| **Missing:** cardiology physician champion | Add | `[ASSUMPTION: none is named]` Needed for medication changes across prescribers and for credibility with the CMO. |
| **Missing:** Friday and weekend pharmacist coverage | Add, through reallocation | Fund it partly by taking touches away from low-risk patients. |
| **Missing:** deputy or lead navigator | Add | No successor is named. If Colette moves to Hospital at Home, the program has no leader. |

Nursing-facility discharges are a deliberate **non-seat**. Don't expand into them. They are outside the hedgehog.

## 5. Stop-doing list

1. **Stop pursuing leadership of Hospital at Home and the combined department in Year 1.** Offer the CMO a referral pathway and an advisory seat, and revisit after the fair-comparison results are in.
2. **Stop graduating every patient at day 30.** End follow-up based on stability criteria, out to 90 days for the high-risk tier.
3. **Stop giving all patients the same six-touch protocol.** Low-risk patients get the 48-hour call, the 7-day visit and a pharmacist check. Everything else goes to the high-risk tier.
4. **Stop reporting enrolled vs not-enrolled as the program's effect.** The comparator includes nursing-facility discharges, people who declined and people who couldn't be reached.
5. **Stop using enrollment rate as the headline goal.** Hold the weekend enrollment shift until the team knows *who* the remaining 33% are. If they are mostly nursing-facility discharges, 75% may be structurally out of reach `[ASSUMPTION: the 67% denominator, 1,146 of 1,702, appears to include nursing-facility discharges]`.
6. **Stop letting stories carry the value case.** Keep Mr. D.'s story as an illustration, never as evidence.
7. **Stop citing the drop in the federal readmissions penalty as HFTP's return.** It is hospital-wide, covers several conditions and is lagged.

**Non-negotiable disciplines:**
- Every patient is assigned a risk tier at the bedside.
- Every high-risk patient has a pharmacist medication review by day 7, Fridays included.
- Every 90-day readmission of an enrolled patient gets a blameless reason-code review.
- A quarterly outcome report covers 30- and 90-day readmissions, mortality and a fair comparator, and **the 90-day number goes on page one**.

**Freedom within a framework:**
- **The framework:** risk tiers, the non-negotiables and the 90-day denominator.
- **The freedom:** navigators decide how intense follow-up is, what channel to use and when a patient is stable, within each tier.

**Bureaucracy check:** the uniform protocol stands in for judgment that these experienced staff already have. Remove it.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | No meaningful difference in 90-day readmissions | 32.7% vs 33.9% (Attachment A) | **Critical** | Colette + pharmacist |
| 2 | Enrolled patients come back more often after "graduation" | Day 31–90 increase: +16.8 points enrolled vs +12.1 points not enrolled (derived from Attachment A minus Section 2) | **Critical** | Colette |
| 3 | The headline comparison is confounded | The non-enrolled group includes nursing-facility discharges, people who declined and people unreachable by phone | High | Analyst (missing seat) |
| 4 | No mortality data | If non-enrolled patients die more often, their readmission rates look lower than they really are. The readmission results can't be read without it. | High | Analyst |
| 5 | No return-on-investment figure, though the VP asked last quarter | Finance hasn't assigned a cost per readmission. Naive cost per avoided readmission is about $21.6K at 30 days and about $106K at 90 days. | High | Colette + finance |
| 6 | Hospital at Home would grow the team 52% before the core effect is proven, and would take its leader | Memo §4.2. One external study. A different clinical model. Reimbursement status not verified `[ASSUMPTION]`. | High | Colette + VP of Nursing |
| 7 | The scarcest resource is the best mechanism | 1.6 pharmacist FTE for 1,146 patients, thin on Fridays | Medium | Colette |
| 8 | The patients who aren't reached are probably the highest risk | 33% not enrolled, including people unreachable by phone | Medium | Community health workers |
| 9 | Unknown whether readmissions to other hospitals are counted | Readmission counts are all-cause, but the source isn't stated | Medium | Analyst |
| 10 | Satisfaction isn't outcome | Survey n = 391 of 1,146 (34% response) | Low | — |
| 11 | No mechanism for raising red flags | The program's most important number sat in an accreditation checklist | Medium | Colette |

**Truth climate:** reporting is driven by stories (the CEO letter, the scales, Mr. D.). That isn't suppression, and the 90-day data was attached openly. But nothing in the system forces a bad number onto page one, and that is what needs fixing.

**Charisma check:** the risk isn't Colette's personality. It is the hospital's success narrative: best in its peer group two years running, plus an enthusiastic board.

**Faith statement:** *Heart-failure readmissions have causes that can be found and fixed, such as the wrong pills, an unweighed patient or a missed visit, and a team that already reaches 82% of its patients within a week can learn to fix those causes for good.*

## 7. Core ideology and the BHAG

**Core values:**
1. The patient stays home, not just past day 30.
2. Truth before story.
3. Fix the cause, not the symptom.
4. Everyone owns the outcome.

**Core purpose:** to help people with heart failure live at home, well, for longer.

**BHAG (10-year):** *No heart-failure patient in our region is readmitted for a cause we could have found and fixed.* This is measured through readmission reason codes.

**Clock-building mechanisms:**
- A quarterly fair-comparison outcome report.
- Blameless 90-day readmission reviews.
- A written, risk-tiered protocol playbook.
- A named deputy.
- An outcome truth-teller role that doesn't depend on the manager.

## 8. Scorecard

| Output | Current value | 12-month target | BHAG trajectory |
|---|---|---|---|
| 90-day all-cause readmission, enrolled vs fair comparator (risk-adjusted, mortality reported alongside) | 32.7% vs 33.9% (unadjusted; about a 1.2-point gap) | Adjusted baseline set by month 3. Gap of ≥3 points by month 12. `[ASSUMPTION: target set at about half the unadjusted 30-day gap]` | Gap widens each year. Preventable-cause readmissions trend toward zero. |
| Verified 90-day readmissions avoided per FTE | About 1.2 (naive, unadjusted) | ≥3 per FTE, verified `[ASSUMPTION]` | Rising per FTE, without adding headcount faster than results |
| High-risk coverage: % of high-risk discharges with pharmacist medication review by day 7 (weekends and Fridays included) | Unknown (not measured) | ≥90% `[ASSUMPTION]` | ≥95% and sustained |

## 9. Next 90 days

| # | Action | Owner | Flywheel step |
|---|---|---|---|
| 1 | **Run a fair comparison** of Year 0 outcomes. Risk-adjust, report nursing-facility discharges separately, and include mortality, days alive and out of hospital, and readmissions to other hospitals. Deliver by day 45. | Colette + quality analyst (request the seat from the VP) + the pharmacist | 4 |
| 2 | **Review the day 31–90 readmissions** of enrolled Year 0 patients (all of them, or about 50) using reason codes such as medications, fluid and weight, missed visit, social or unrelated. | Lead pharmacist + navigators + Ana | 2, 3 |
| 3 | **Answer the CMO.** Decline to lead Hospital at Home in Year 1. Offer a referral and post-discharge partnership. Put the 90-day number in front of the VP *before* the decision. | Colette with the VP of Nursing | Protects the whole loop |
| 4 | **Pilot risk tiers:** a lighter touch for low-risk patients, follow-up to day 60–90 for high-risk patients, and Friday pharmacist coverage funded by the capacity this frees up. | Colette + lead navigator (deputy candidate) | 1, 3, 6 |
| 5 | **Build the value case with finance** using verified numbers only: cost per readmission plus the value of freed beds `[ASSUMPTION: it is unknown whether the hospital runs at capacity]`. Have it ready for the budget cycle. | Colette + finance | 5 |

## 10. Re-check

Offer: schedule a review about 90 days out (around late February of Year 1). It would re-score the three scorecard measures with the fair-comparison and readmission-review results, and re-run Gates 1, 5 and 8. In particular, it would decide whether the Hedgehog Concept survives and whether to revisit Hospital at Home. This session has no tools, so the review can't be scheduled from here.

## 11. Risk register

| Source | Risk | Condition / early warning sign | Evidence that resolves it |
|---|---|---|---|
| Gate 1 (CONDITIONAL) | The "good" baseline rests on process measures and a confounded outcome | — | A risk-adjusted 30-day effect shown against a fair comparator |
| Gate 2 (CONDITIONAL) | The leader's personal advancement is tied to scope expansion, and there is no successor | — | Colette chooses one role. A deputy is named. The 90-day number leads her next report. |
| Gate 4 (CONDITIONAL) | Brutal facts are listed but not yet in front of decision-makers | — | The VP and CMO see the 90-day and adjusted numbers before the Hospital at Home decision |
| Gate 5 (CONDITIONAL) | "Best at root-cause fixing" is unproven, and the engine isn't priced | — | Confirmation tests 1–3 pass. Finance assigns a cost per readmission. |
| Gate 8 (CONDITIONAL) | Flywheel link 4 (verified effect) isn't evidenced | — | Two consecutive quarterly reports show an adjusted 90-day gap |
| Decline 1: Hubris | "Best in peer group" plus the CEO letter breeds certainty | Reports cite enrolled vs not-enrolled without adjustment | — |
| Decline 2: Undisciplined pursuit of more | Hospital at Home, the combined department, +6 FTE | The leader spends more than 20% of her time on Hospital at Home planning, or vendor contracts are signed before results are in | — |
| Decline 3: Denial of risk | The 90-day data is dismissed as "outside our window" | The 90-day number is missing from leadership reports | — |
| Decline 4: Grasping for salvation | After a budget challenge, the team buys a new platform or takes on a new program to justify itself | A technology purchase is proposed without a pilot and a comparator | — |
| Decline 5: Capitulation | The program is cut, or quietly absorbed into Hospital at Home | Navigator caseloads rise while visits per patient fall, or the HFTP name disappears from the budget | — |

**Shared root problem:** 5 of 11 gates are CONDITIONAL, which is under half. All five trace back to the same root: **the program has never measured its own causal effect.** The single action of a fair, 90-day comparison with mortality included would resolve or reframe all of them.

**Tech triage (Gate 7 artifact):**

| Tool | Class | Note |
|---|---|---|
| Phone and software ($44K) | Parity | Keep |
| Hospital at Home vendor monitoring platform | Irrelevant to the hedgehog | Only reconsider as a *pilot* of connected scales for the high-risk tier, judged on 90-day results |
| EHR plus regional data for risk tiering and capturing readmissions to other hospitals | **Accelerator, with pioneer potential** | |
| Pharmacy fill and prescriber data to detect duplicate prescriptions across specialists (the Mr. D. pattern) | **Accelerator, with pioneer potential** | |
| Bathroom scales | Accelerator | Fund them from the budget for the high-risk tier rather than relying on donations |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing hospital team, a clear steward, 11.6 FTE, a multi-year horizon, measurable outcomes |
| 1 Baseline | CONDITIONAL | Good on process (82% seven-day follow-up, growing enrollment, low turnover). The outcome effect is unproven, and the 90-day data was folded into the baseline here to avoid a Gate 4 contradiction. |
| 2 Level 5 | CONDITIONAL | Strong operator. Scope ambition is tied to a promotion, and no successor is named. |
| 3 First Who | PASS | No misaligned key seat. Missing seats: analyst, physician champion, Friday pharmacist, deputy. |
| 4 Brutal Facts | CONDITIONAL | 90-day parity and confounding are surfaced but not yet in front of decision-makers |
| 5 Hedgehog | CONDITIONAL | Root-cause fixing until stable. Denominator: verified 90-day readmissions avoided per FTE. Unconfirmed. |
| 6 Discipline | PASS | Seven stop-doing items, four non-negotiables, risk-tier framework |
| 7 Technology | PASS | Data and medication-duplication detection accelerate the hedgehog. The Hospital at Home platform is irrelevant. |
| 8 Flywheel | CONDITIONAL | The loop closes logically. Link 4 (verified effect) has no evidence yet. |
| 9 Built to Last | PASS | Values, purpose, a 10-year BHAG and clock-building mechanisms defined |
| 10 Mighty Fall | PASS | Stress test done. Stage 2 (Hospital at Home) is the live risk. |

**Count:** 6 PASS (0, 3, 6, 7, 9, 10), 5 CONDITIONAL (1, 2, 4, 5, 8), 0 FAIL.

*These are disciplined hypotheses drawn from a single memo, not guarantees. Collins's method looks backward at companies, and some of the companies he called great later declined.*