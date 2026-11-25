## Verdict: Delivery Platform (Runway) is good, not yet great, and one decision away from drifting

**Hedgehog Concept:** Runway makes changing any Brightwater service, especially the ones that move money, fast, compliant and reversible in under five minutes.

**Weakest flywheel link:** fast rollback plus Payments' change-approval step. It has slipped three quarters running, and it is the stated price of Payments migrating.

**Top three stop-doing items:**
1. Atlas as scoped. Counter-offer the headcount to rollback.
2. Chasing "80% of services".
3. New templates and one-off tweaks until rollback ships.

**Most urgent brutal fact:** Payments services on legacy pipelines caused both Sev-1s and 4 of 6 Sev-1/2s. card-auth-gateway took 47 and 22 minutes to roll back.

**Missing numbers that would change this:**
- How many of the 119 legacy services are money-moving.
- Runway's current rollback time.
- Whether the VP's headcount is tied to Atlas specifically.

**Confidence:** moderate. It rests on one quarter's retro, with no outside research.

`Greatness potential: 40/100`

---

## 1. The great version in one paragraph

In its great version, Delivery Platform is the team Brightwater cannot imagine operating without. The reason is not that Runway hosts the most services. It is that the services which move customers' money change safely through Runway.

- A bad deploy to card-auth-gateway is rolled back automatically in under five minutes.
- Payments' card-network sign-off is a first-class, auditable step in the pipeline, not a reason to stay on a hand-maintained legacy plugin that only Bartek can debug.
- The team's headline metric is change-induced incidents per 1,000 deploys across the whole company, legacy pipelines included. Adoption becomes a consequence of that metric, not the goal.
- Leadership funds the team because incident minutes in money-moving systems keep falling.
- The team keeps the discipline to turn down attractive greenfield work, including a well-funded developer portal, until the safety path is complete.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):** *We make changing any Brightwater service, especially the ones that move money, fast, compliant and reversible in under five minutes.*

| Circle | Candidates considered | Chosen |
|---|---|---|
| **Best in the world at** (world = Brightwater) | Paved-road CI/CD; service templates; developer portal; progressive delivery for regulated payment services | **Safe, compliant, instantly reversible change for regulated money-moving services.** No one else inside Brightwater can do it, and no product org will build it for itself. **Not best at:** developer portals and catalogs (generic, and buyable or adoptable `[ASSUMPTION]`), wide language-template coverage, bespoke per-team pipeline tweaks. |
| **Drives the resource engine** (budget and headcount leverage) | Services on Runway; deploys per engineer; lead time; incidents avoided | **Leadership trust and headcount earned by visibly reducing change-induced incidents in money-moving systems.** The two Sev-1s are what executives remember; 64% adoption is not. |
| **Passionate about** | Shipping early and greenfield work (template v3, Kotlin, Atlas excitement); developer experience; reliability (two dissenters raised rollback) | **Making shipping fast and boring for every engineer** `[ASSUMPTION]`. This is the weakest circle. The team's demonstrated passion is new, visible launches. Rollback and the approval gate need to be framed as the hard, novel engineering problem they actually are. |

**Denominator:** **change-induced Sev-1/2 incidents per 1,000 deploys, company-wide (all pipelines).**
- Current value: 6 ÷ 4,212 ≈ **1.4**. All six Q3 Sev-1/2s were triggered by a change: config push, deploy, flag, migration or dependency upgrade.
- Secondary measure: time to restore after a bad change.

**Tests:**
- *Explains past wins?* Yes. The secret-manager migration had zero incidents, lead time fell from 58 to 41 minutes, pages fell from 52 to 37, and Runway services had 1 Sev-1/2 against 5 on legacy.
- *Rules things out?* Yes: Atlas as scoped, more templates before rollback, one-off tweaks, and the 80% headline.
- *Uncomfortable?* Yes. It turns down two headcount and the project most of the team wants. It also holds the team accountable for incidents on pipelines it does not own.

**Evidence that would confirm it:**
- Payments signs a written migration commitment tied to the rollback and approval criteria.
- card-auth-gateway deploys through Runway.
- The denominator falls for two consecutive quarters.
- The VP's next headcount offer cites incident reduction.

## 3. The flywheel

```
 ┌─► 1. Ship <5-min automated rollback + auditable change-approval gate
 │            │
 │            ▼
 │   2. Money-moving (Payments, Lending) services migrate to Runway
 │            │
 │            ▼
 │   3. Change-induced Sev-1/2 per 1,000 deploys falls; restores take minutes
 │            │
 │            ▼
 │   4. Leadership and product orgs trust Runway → legacy pipelines retired,
 │      Bartek's legacy load and one-off interrupts shrink
 │            │
 │            ▼
 │   5. Freed capacity + headcount earned on incident data
 │            │
 └────────────┘ reinvested in safety features and extension points
```

**Current push (the next two turns):**
1. Get rollback to under 5 minutes at p95 and build the approval gate *with* the Payments platform lead.
2. Use card-auth-gateway, which had two Sev-1/2s and slow rollbacks, as the first migration and the proof case.

**Doom-loop check:**
- *Early warning signs present.* Three quarters in a row, newer and more visible work (template v3, the Kotlin starter) beat rollback. A new big program, Atlas, is now on offer as the momentum story. The draft OKR of "80% of services" can be hit without touching the hard residue.
- *Not yet a doom loop.* Direction has been consistent, and the team is still delivering.
- *Verdict:* the loop closes. The one unproven causal link, step 4 to 5 (whether headcount actually follows incident reduction), is logged under Gate 5.

## 4. The bus

| Person / commitment | Call | Note |
|---|---|---|
| Ines (EM) | **Keep** | Strong Level 5 signals; see the Gate 2 read. |
| Mei | **Move seat → rollback / Payments path** `[ASSUMPTION]` | She delivered template v3 two weeks early. Put the best person on the biggest opportunity, not on the next template. |
| Sana | **Keep, and reinforce** | She owns rollback but has been re-estimating it alone for three quarters. The seat is under-staffed; this is not a judgment of her. Pair with Mei. |
| Bartek | **Move seat → Payments migration design + legacy knowledge transfer** | He is the only person who can debug legacy plugins. That knowledge of Payments' world is an asset for migration and a single point of failure if he stays the only holder. |
| Ravi | **Keep** | Defer the Kotlin gRPC example unless it costs under about 2 days `[ASSUMPTION]`. |
| TPM | **Keep, re-seat on the Payments partnership** | Owns the written migration agreement and the approval-gate requirements. |
| Tomasz, others (5 engineers unnamed) | **Keep** `[ASSUMPTION]` | No evidence either way. |
| Intern build-cache dashboard | **Keep as-is** | Useful and neutral. Don't expand it. |
| Atlas commitment | **Off (for now)** | Outside the Hedgehog Concept. See stop-doing item 1. |
| One-off pipeline tweak requests | **Off** | Replace with extension points and a weekly intake slot. |
| **Missing:** Payments design partner | **Missing seat** | A named Payments compliance or change-approval owner who co-designs the gate and signs off on it. |
| **Missing:** second legacy-plugin debugger | **Missing seat** | Fill by pairing with Bartek, not by hiring. |

## 5. Stop-doing list

1. **Stop: Atlas as scoped.** Tell the VP the team won't build and own Atlas until rollback and the approval gate meet Payments' criteria.
   - Counter-offer: put the two headcount on the Payments path, and Runway publishes service ownership metadata as a feed that whoever builds a catalog can use.
   - The 58% "finding owners or docs is hard" pain is real. It just isn't this team's best-in-world work.
2. **Stop chasing "80% of services".** Reaching 265 of 331 means converting about 53 more services. The cheapest 53 are almost certainly not the ones causing Sev-1s.
3. **Stop starting new templates and template versions** while rollback is in flight.
4. **Stop doing one-off pipeline tweaks.** Offer documented extension points plus a fixed weekly intake slot.
5. **Stop re-estimating rollback.** Staff it, protect its capacity, and demo it weekly.
6. **Stop treating legacy pipelines as unmeasurable** ("not our services, not our budget"). The team doesn't need to own them, but it does need to see them: deploy events, change-incident tags and time to restore.
7. **Stop muting alerts without a ticket and an expiry date.**
8. **Stop single-threading legacy-plugin knowledge** through Bartek.

**Non-negotiable disciplines:**
- Rollback and approval-gate work gets protected capacity of at least 40% of the team `[ASSUMPTION]` until the exit criteria are met.
- Every Sev-1/2 is tagged by pipeline and time to restore, and gets a blameless review.
- Any work that is neither rollback nor the approval gate must state which flywheel step it pushes.
- An action item carried over twice escalates automatically to the EM and VP.

**Framework:**
- *Boundary:* all work reduces change risk or change time on Runway.
- *Freedom:* engineers choose the technical approach, the sequencing and the tools inside that boundary.
- *Bureaucracy check:* Payments' manual sign-off is **not** compensating for wrong people. It is a real card-network compliance requirement, so build it in as a first-class, auditable gate rather than trying to engineer it away.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The riskiest services are exactly the ones not on Runway, and the team has deprioritized the stated price of moving them three times. | Both Sev-1s and 4 of 6 Sev-1/2s were Payments services on legacy pipelines. Rollbacks took 47 and 22 minutes. Payments' conditions (rollback under 5 minutes plus the approval step) were repeated in the architecture review. The rollback epic has been carried over for a third time. | **Critical** | Ines |
| 2 | Adoption growth is mostly greenfield, not migration. | 34 of 35 new services started on Runway, and net Runway growth was +25. The 119 services left on legacy are the hard residue. | High | Ines + TPM |
| 3 | The team cannot see the risk it exists to reduce. | Legacy pipelines aren't instrumented. The 41-minute lead time covers Runway only. Runway's own rollback time is not reported. | High | Bartek + 1 |
| 4 | Legacy incidents run at about 9× the Runway rate per service, but criticality confounds the comparison. | 5 per 119 services (≈4.2 per 100) against 1 per 212 (≈0.5 per 100). The legacy set includes the money-moving services. | Medium (use carefully) | TPM |
| 5 | The satisfaction score is self-selected. | 4.1/5 is reported only among Runway users. Non-users' view is unknown. | Medium | TPM |
| 6 | There is a key-person dependency. | Bartek is the only legacy-plugin debugger and is also quietly muting alerts. | Medium | Ines |
| 7 | Interrupts are draining capacity. | "Too many" one-off tweak requests (not counted). | Medium | Ines |
| 8 | Atlas would be the fourth item in a row to beat rollback, and it comes with a deadline and headcount attached. | The same pattern as template v3 and the Kotlin starter. Most of the team is excited. | High | Ines |

**Truth climate:**
- Good. The retro is candid, Ines leads with questions, and two people dissented openly.
- Weak spots are the red-flag mechanisms: muted alerts, uninstrumented pipelines, and carry-overs that never escalate.
- *Charisma check:* there is no sign that the leader suppresses bad news. The real risk is enthusiasm drowning out the two dissenters.

**Faith statement:** *The services that matter most are already asking to move, and they have told us the exact price, so we will prevail by paying it.*

## 7. Core ideology and the BHAG

**Core values:**
- Safe by default.
- Boring deploys are the goal.
- Measure what matters, even where it isn't ours.
- Credit the crew, own the slip.

**Core purpose:** let every Brightwater engineer change production with confidence, so customers' money moves reliably.

**BHAG** (kept to one line, because this is a team inside an org): *No Brightwater customer is affected for more than five minutes by a bad change* `[ASSUMPTION: ~5-year horizon]`.

**Clock-building mechanisms** (so this works without the current people):
- Automatic pipeline tagging of incidents.
- A rollback-time SLO dashboard.
- The protected-capacity rule.
- An intake rotation for requests.
- Legacy-plugin runbooks.
- Automatic escalation of carry-overs.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| Change-induced Sev-1/2 per 1,000 deploys (all pipelines) | **≈1.4** (6 / 4,212, Q3) | ≤ 0.7 `[ASSUMPTION]` | Approaching zero customer-impact minutes |
| Runway rollback time, p95 | **Unknown.** Legacy examples were 47 and 22 minutes. | **< 5 minutes** (Payments' own bar) | < 5 minutes, automatic |
| Money-moving (Tier-1) services on Runway | **Unknown.** card-auth-gateway, payouts-scheduler, ledger-recon and loan-disbursement are all legacy. | card-auth-gateway and payouts-scheduler migrated; ≥ 50% of Tier-1 services `[ASSUMPTION]` | 100% of Tier-1 services |

Supporting measure, not a target: median commit-to-production time on Runway (41 minutes).

## 9. Next 90 days (Q4)

1. **Answer the VP before the offsite.** Decline Atlas as scoped and counter-offer the two headcount for the rollback and approval path, plus a Runway ownership-metadata feed. Bring the incident table as evidence. **Owner: Ines.**
2. **Rewrite the Q4 OKR** from "80% of services" to:
   - rollback under 5 minutes at p95 in production;
   - the approval gate live;
   - card-auth-gateway migration-ready, with a signed Payments commitment.

   **Owner: Ines + TPM.**
3. **Staff rollback, don't re-estimate it.** Mei leads with Sana `[ASSUMPTION]`, protected capacity, and a weekly demo. **Owner: Mei / Sana.**
4. **Co-design the change-approval gate with the Payments platform lead** and get the migration commitment in writing. **Owner: TPM + Bartek.**
5. **Make the risk visible:**
   - tag every Sev-1/2 by pipeline and time to restore;
   - pull deploy events read-only from legacy pipelines;
   - pair on legacy-plugin runbooks;
   - fix the disk alerts properly.

   **Owner: Bartek + one engineer.**

## 10. Re-check

I can't create a scheduled task in this session. Would you like one set up for about 90 days out (the end of Q4 Year 0)? It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8.

## 11. Risk register

| Source | Risk | Early warning / condition | Trigger → action |
|---|---|---|---|
| Gate 3 (CONDITIONAL) | Bartek is the only person who can debug legacy plugins. | Payments escalations still route only to him. | PASS when a second engineer resolves a legacy-plugin issue unaided. |
| Gate 5 (CONDITIONAL) | The passion circle and the engine link are unproven: will the team choose rollback over Atlas, and will leadership reward incident reduction? | The team picks Atlas, or the VP withdraws headcount without Atlas. | PASS when the team commits in planning, Payments signs the migration criteria, and headcount or budget is tied to incident data. |
| Decline stage 2: undisciplined pursuit of more (**top risk**) | Atlas plus headcount pulls the team off rollback for a fourth quarter. | The rollback epic carries over again. | If p95 rollback isn't under 5 minutes in staging by the end of Q4, freeze all non-Hedgehog work. |
| Decline stage 3: denial of risk (**top risk**) | The adoption percentage rises while the incident rate doesn't move. | Runway share goes up but change-incidents per 1,000 deploys stays flat. | Two flat quarters → treat the adoption metric as misleading and re-run Gate 5. |
| Stage 1: hubris | "Crossed 200!", 34 of 35 new services, a 4.1 score among users. | Retros celebrate counts rather than incidents. | Lead every retro with the incident table. |
| Stage 4: grasping for salvation | Atlas or a big re-platform gets used to restore the story if rollback struggles. | A new initiative is proposed mid-epic. | It requires a written flywheel-step justification. |
| Stage 5: capitulation | Payments builds its own pipeline and the team becomes a template shop. | Payments starts investing in its own legacy tooling. | Escalate to the VP immediately. |

## 12. Gate log

*Evidence note:* memory, past chats and web research were not available in this session, so no earlier run was found and no external facts were checked. Everything rests on the dossier, and inferences are tagged `[ASSUMPTION]`.

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing team, a steward (Ines, with the VP as sponsor), a multi-year horizon, and real metrics. Current stage: mid-adoption (64%). |
| 1 Baseline | PASS | **Good, not yet great.** 64% adoption, lead time 58→41 minutes, pages 52→37, a 4.1 score among users. Great means indispensable output for money-moving services. |
| 2 Level 5 | PASS | Strong humility (asked to come off the hero slide, credits the crew, leads with questions). Gap in resolve: three rollback slips, and Atlas left to an enthusiasm vote. **Behavior change:** own the slips as a prioritization call and defend rollback to the VP personally. |
| 3 First Who | CONDITIONAL | No misaligned people. Bartek is a key-person risk, and the Payments design-partner seat is missing. |
| 4 Brutal Facts | PASS | Nothing contradicts Gate 1. The facts sharpen what great means. |
| 5 Hedgehog | CONDITIONAL | Safe, compliant, reversible change for money-moving services. The passion and engine links are unproven. |
| 6 Discipline | PASS | Eight stop-doing items. The approval gate is a real requirement, not bureaucracy. |
| 7 Technology | PASS | Accelerates: automated rollback, the auditable approval gate, legacy deploy telemetry. Parity: the Kotlin template, the secret manager. Neutral: the build-cache dashboard. Drop for now: Atlas (visibility-driven, not hedgehog-driven). Pioneer candidates: an approval gate built as code with audit evidence; SLO-triggered auto-rollback on payment-success metrics. |
| 8 Flywheel | PASS | The loop closes. Weakest link: rollback plus the approval gate. |
| 9 Built to Last | PASS | Values, purpose, a one-line BHAG, and six mechanisms. |
| 10 Mighty Fall | PASS | Top risks: undisciplined pursuit of more (Atlas) and denial of risk (unmeasured legacy). |

Tally from the table: 11 gates, 9 PASS, 2 CONDITIONAL, 0 FAIL.