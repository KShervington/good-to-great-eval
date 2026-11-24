# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict (one screen)

**Hedgehog Concept (working hypothesis):** *Runway is how Brightwater safely changes the systems that move money: every deploy can be rolled back in minutes and is audit-ready by default.*

**Decision due before the Q4 offsite: say no to Atlas for now and make a counter-offer.** Ask for the two headcount to go to safe change for money-moving services. Offer Atlas a data spine (owner, tier and pipeline for every service) and nothing more. If the VP's offer is all-or-nothing, decline it. This is a judgment call, and it is explained in Section 5.

**Weakest link in the flywheel:** step 1, *make every change reversible and audit-ready*. It has never turned. The fast-rollback epic has slipped three quarters in a row, and it is the explicit precondition Payments set before it will migrate.

**Top three stop-doing items:**
1. Stop using the rollback epic as the buffer that template and starter work borrows from.
2. Stop Atlas as a portal owned by this team: docs search, scorecards and UI.
3. Stop the headline OKR "80% of services on Runway." It treats a notifications service and card-auth-gateway as equal.

**Most urgent brutal fact:** Both Sev-1s this quarter, and four of the six Sev-1/Sev-2s, hit Payments services on legacy pipelines. Card-auth-gateway went down twice and took 47 and 22 minutes to roll back. Payments has said what it needs in order to move. The team has deferred that work three times in favor of easier wins.

**Missing numbers that would change the answer:**
- Runway coverage by service tier: how many money-moving services exist, and how many are on Runway.
- How many existing services actually migrated this quarter. The dossier's numbers allow anywhere from 0 to 21.
- Deploys and change-failure rate broken down by pipeline.
- Current rollback time on Runway, and the re-estimate of the rollback epic.
- What Payments' change-approval step actually requires.
- Whether the VP will accept the counter-offer.

Greatness potential: 45/100

*Run notes:* Autonomous mode. Memory, past-chat search and web research weren't available, so the evidence step and Gate 4's market research were skipped and the dossier is the only evidence. Every inference is marked `[ASSUMPTION]`. "Today" is the end of Q3, Year 0.

---

## 1. The great version in one paragraph

A year or two out, the Delivery Platform team is the reason Brightwater can change its card, payout and lending systems quickly without its customers ever noticing a bad deploy. Card-auth-gateway and the other money-moving services ship through Runway. Any change can be rolled back in under five minutes. The card-network compliance sign-off happens inside the pipeline, and the audit evidence is generated automatically. Change-induced Sev-1s have become rare, and when one does happen it is short. The team measures itself by risk removed from the services Brightwater can least afford to break, not by the share of services on Runway. Its headcount grows because that evidence is hard to argue with. It is narrow on purpose. It owns the paved road and its safety features. It does not own every team's custom pipeline, every language starter, or the developer portal.

## 2. The Hedgehog Concept

**Sentence:** *Runway is how Brightwater safely changes the systems that move money: every deploy can be rolled back in minutes and is audit-ready by default.*

| Circle | Candidates considered | What survives |
|---|---|---|
| **Best in the world** (the "world" here is Brightwater) | (a) Service templates and starters. (b) A developer portal. (c) Fast CI. (d) Safe, reversible, compliant change for regulated services. | **(d).** No vendor or other internal team knows Brightwater's legacy plugins, its card-network audit step and its rollout tooling the way this team does. The team **cannot** be best at portals or docs search, which are commodity problems with off-the-shelf options `[ASSUMPTION]`. It also cannot be best at handling one-off pipeline requests or at a starter for every language. |
| **Resource engine** (budget and headcount leverage) | (a) Visible new products. (b) Adoption counts. (c) Production risk retired. | **(c).** A payments and lending company loses money and regulator goodwill to card-auth outages. Risk removed is the most defensible case for headcount, even though today's offer rewards visibility instead (see Brutal facts). |
| **Passion** | (a) Greenfield and visible work, which is Atlas. (b) Shipping things engineers love (template v3 shipped early, 4.1/5 satisfaction). (c) Reliability craft. | **(b) and (c) together, which is the weak circle.** The team's current excitement points at Atlas. Two people worried about the rollback epic. The hypothesis is that moving card-auth-gateway is *more* visible than a portal, if it is framed and staffed as a flagship launch. |

**Denominator:** *per critical (money-moving) service.* The team's leverage grows with the number of critical services that deploy through Runway, with rollback under five minutes and approval built in. The companion engine metric is **change-induced Sev-1/Sev-2 minutes per critical service per quarter**.

**Tests of the hypothesis:**
- *Does it explain past wins?* Yes. Runway took 34 of 35 new services and cut pages from 52 to 37 because it was the easiest safe path. It also explains the main loss: Payments is holding out because the safety features are missing.
- *Does it rule things out?* Yes. It rules out Atlas, the Kotlin gRPC example, one-off tweaks, and the service-count OKR.
- *Is it uncomfortable to commit to?* Yes. It means turning down two headcount and the team's preferred project.

**Evidence that would confirm it (working hypothesis, recheck at 90 days):**
1. Payments gives a written definition of "done" for both of its conditions, and does not add new ones.
2. A pilot Payments service migrates within two quarters of rollback shipping.
3. Change-induced incident minutes fall on migrated critical services.
4. The VP funds reliability work on the strength of that evidence.
5. The rollback and approval work is staffed by volunteers, not draftees.

## 3. The flywheel

```
 ┌──► 1. Make every change reversible & audit-ready
 │       (rollback < 5 min; change-approval as a Runway step)   ◄── WEAKEST LINK
 │                         │
 │                         ▼
 │    2. Money-moving services move onto Runway
 │       (Payments pilot → card-auth-gateway → Lending)         ◄── denominator
 │                         │
 │                         ▼
 │    3. Fewer, shorter change-induced Sev-1/2s,
 │       measured per critical service, by pipeline
 │                         │
 │                         ▼
 │    4. Evidence earns trust, headcount and budget              ◄── unproven link
 │       (resource engine)
 │                         │
 │                         ▼
 │    5. Paved road gets safer and more self-service
 │       → fewer interrupts → more capacity for step 1
 └─────────────────────────┘
```

**Current push (the next two turns):**
1. Ship rollback under five minutes on Runway and drill it on a real service. Get Payments' change-approval requirement in writing and build it as a pipeline step.
2. Migrate one lower-risk Payments service as a pilot before card-auth-gateway. Measure its rollback time and incidents against its old legacy baseline.

**Doom-loop check:** There are early signs, though not a full doom loop yet.
- The same priority has slipped three quarters running behind newer, shinier work. That is inconsistency.
- Atlas is a new direction being offered with a deadline attached. Saying yes would be jump-starting momentum with a big program.
- The 80% OKR is a target the team could hit while avoiding the hard work, through new services and retirements alone.
- Counter-sign: the team is consistent about keeping the paved road good. Deploy time fell from 58 to 41 minutes, and the secret-manager migration finished with zero incidents.

## 4. The bus

Per the guardrails, "off" applies to commitments and roles for this endeavor. It is not a judgment of anyone's worth. No person on the team shows misalignment in the dossier.

| Who / what | Call | Seat and why |
|---|---|---|
| Ines (EM) | **Keep, and sharpen the seat** | She owns the priority call. See the leadership read: humility is evident, resolve is not yet shown. |
| TPM | **Keep, move seat** | From OKR drafting to running the Payments migration program, including the service-tiering baseline. |
| Mei | **Keep, move to the biggest opportunity** | She ran the template v3 launch two weeks early. Make her launch lead for rollback and the Payments pilot `[ASSUMPTION: she wants it]`. |
| Sana | **Keep** | She owns the rollback epic. The carry-overs came from deprioritization, not from anything she did. Give the epic protected capacity. |
| Bartek | **Keep, move seat** | He moves from being the sole firefighter on legacy plugins to being the guide for the Payments migration, because he knows their pipelines. He also pairs with someone to remove the single point of failure. |
| Ravi | **Keep, move seat** | Hand the Kotlin gRPC example to the teams that use the starter. Move him onto the change-approval step or rollback. |
| Tomasz (on leave) | **Keep** | Seat to be assigned on return. |
| Five unnamed engineers | **Keep** | Seats unknown `[ASSUMPTION]`. Bias toward the work in step 1. |
| Intern dashboard | **Keep as is** | Useful. Run it, but add no new features. |
| Atlas portal | **Off (for now)** | Outside the Hedgehog Concept. |
| Ad-hoc one-off pipeline tweaks | **Off** | Replace with a front door (see Stop-doing). |
| "80% of services" OKR | **Off** | It measures the wrong thing. |
| **Missing:** a Payments co-owner | **Missing** | A named engineer from Payments who co-owns the migration. Without this seat, Payments' commitment stays verbal. |
| **Missing:** a compliance partner | **Missing** | The person who can define what the card-network audit actually requires as evidence. |
| **Missing:** a second legacy-plugin expert | **Missing** | Reduces the Bartek risk. |
| **Missing:** a reliability engineer | **Missing** | For automated rollback. This is where the negotiated two headcount should go. |

## 5. Stop-doing list

1. **Stop treating the rollback epic as the buffer.** No new template or starter features until rollback under five minutes is in production.
2. **Stop Atlas as a portal owned by this team.** No docs search, scorecards or UI.
   - *Keep:* the ownership, tier and pipeline metadata on every service. Runway needs it for the scorecard, and Atlas can use it later.
   - *Tell the VP:* the 58% "can't find owner or docs" problem is real. It deserves an owner, and it may be a buy-or-adopt decision `[ASSUMPTION]`.
   - *Offer:* revisit Atlas once rollback ships and the Payments pilot is live.
3. **Stop making "% of services on Runway" the headline OKR.** It can rise with zero migrations, and the dossier's numbers cannot rule that out.
4. **Stop taking unplanned one-off pipeline tweaks.**
   - Create one rotating "front door" engineer per sprint.
   - Publish extension points so teams can make the change themselves.
   - Anything else goes into the backlog.
5. **Stop building new language starters and template examples in-house.** The Kotlin gRPC example goes to the teams that consume it, with a review only from this team.
6. **Stop muting alerts without a fix ticket and a date.** The build-cluster disk alerts are a small case of a big habit.
7. **Stop saying "not our services, not our budget" about legacy measurement.** Instrument lightly: pull deploy and rollback times from the incident tracker and deploy events, not a full integration.

**Non-negotiable disciplines:**
- Every Runway release keeps rollback under five minutes.
- Every Sev-1/Sev-2 is reviewed with a pipeline column and a rollback-time column.
- Rollback drills run monthly on critical services.
- Every new commitment is checked against the Hedgehog sentence before it is accepted.

**Framework boundaries:** The team is free to choose *how* to build rollback and approval, and individuals choose which part of step 1 they take. The team is not free to start work outside the Hedgehog Concept without the EM's explicit trade-off decision.

**Bureaucracy check:** No rules in the dossier look like they exist to compensate for the wrong people. The problem is the opposite: too little structure around interrupts and alerts.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The riskiest services are off Runway and are where the outages happen. | 4 of 6 Sev-1/2s are Payments on legacy, including both Sev-1s. Card-auth-gateway hit twice, 47 and 22 min to roll back. 5 of 6 overall are legacy. | Critical | Ines |
| 2 | The precondition Payments set for migrating has slipped three quarters running. | Rollback epic carried over a third time, behind template v3 and the Kotlin starter. | Critical | Ines + Sana |
| 3 | The coverage number may hide zero migrations. | Q2 187/326 → Q3 212/331, with 34 new services on Runway. Runway's net gain of +25 means at least 9 Runway services left the count. Legacy fell by 21 through retirements and migrations combined. Migrations could be anywhere from 0 to 21. | High | TPM |
| 4 | The team can't prove its value where it matters. | Legacy pipelines aren't instrumented. Deploys aren't split by pipeline. Rollback time on Runway is not reported. | High | TPM |
| 5 | The incident comparison is confounded. | Legacy services have roughly 9× more Sev-1/2s per service (5/119 against 1/212). But the legacy set holds the inherently riskiest systems, so this is not proof that Runway is safer. | Medium | Ines |
| 6 | Runway is not immune. | The notifications Sev-2 came from a feature-flag misfire. Payments will scrutinize it. | Medium | Sana |
| 7 | The resource engine currently rewards visibility, not risk reduction. | The headcount is offered for Atlas, not for rollback. | High | Ines |
| 8 | Payments' commitment is verbal and could move. | "Repeated" in the architecture review. The change-approval requirement is undefined. | High | TPM + Payments lead |
| 9 | There is a single point of failure on legacy. | Bartek is the only person who can debug legacy plugins. | Medium | Bartek + Ines |
| 10 | Interrupts and noise erode capacity. | "Too many interrupts." Two alerts muted. | Medium | Ines / Bartek |

**Truth climate:** Mostly healthy. Ines leads with questions and invites debate, and the retro names uncomfortable things.
- The gap is red-flag mechanisms: alerts get muted, legacy is unmeasured, and the incident review apparently doesn't trend results by pipeline.
- **Charisma check:** Ines is not suppressing bad news. The quieter risk is the team's enthusiasm drowning out the two people who flagged the rollback concern.

**Faith statement:** *Runway won the easy 64% by being the better road. It will win the hard 36% the same way, by becoming the safest way to change money-moving systems.*

## 7. Core ideology and the BHAG

**Core values:**
1. Every change is reversible.
2. Evidence beats adoption counts.
3. One paved road, not a thousand custom paths.
4. Credit the crew. This one comes from Ines asking that the template v3 names replace hers on the all-hands slide.

**Core purpose:** Let Brightwater change the systems people's money depends on quickly and without fear.

**BHAG** (kept to one line, because an internal team's horizon depends on the org; about 5 years `[ASSUMPTION]`): *Every system at Brightwater that moves money deploys through Runway, and no customer ever notices a bad deploy.*

**Mechanisms that keep this working without the current people:**
- Service tier and owner metadata on every service.
- The incident review template, with pipeline and rollback-time fields.
- Monthly rollback drills.
- Change approval implemented as policy-as-code with an automatic audit trail.
- The front-door rotation.
- Documented legacy-plugin runbooks, which reduce the dependence on Bartek.

## 8. Scorecard

| Output | Current (end of Q3, Year 0) | 12-month target | BHAG trajectory |
|---|---|---|---|
| Critical (money-moving) services on Runway | **Unknown.** 0 of the 4 Payments/Lending services named in incidents are on Runway. | Card-auth-gateway plus ≥75% of critical services `[ASSUMPTION]` | 100%, legacy pipelines retired |
| Change-induced Sev-1/2 per quarter (by pipeline) | **6** (5 legacy, 1 Runway; 2 Sev-1, both Payments legacy) | ≤2, with zero legacy-caused Sev-1 `[ASSUMPTION]` | Sev-1 from deploys rare; customer impact under 5 min |
| Rollback time, p95, critical services | **Unmeasured** on Runway. Legacy incidents took 47 and 22 min. | <5 min, drilled monthly | <1 min, automatic on health regression |

Secondary metrics, tracked but not headline: overall coverage (64%), Runway median commit-to-production time (41 min), satisfaction (4.1/5), team pages (37).

## 9. Next 90 days

| # | Action | Owner | Flywheel step |
|---|---|---|---|
| 1 | Before the offsite, answer the VP with the counter-offer. Proposal: the two headcount go to rollback, change approval and the Payments migration. Atlas gets the metadata spine now and a revisit after rollback ships. Make the call after hearing the team, but make it. | Ines | 4 → 1 |
| 2 | Ship rollback under five minutes on Runway as Q4 priority #1 with protected capacity, and drill it on a production service. | Sana (epic), Mei (launch lead) `[ASSUMPTION]` | 1 |
| 3 | Get Payments' two conditions written as acceptance criteria. Name a Payments co-owner and a compliance contact. Pick a lower-risk pilot service. Design the change-approval step. | TPM + Bartek (with Ravi on the approval step) | 1 → 2 |
| 4 | Build the baseline: tag all 331 services with owner, tier and pipeline. Compute critical coverage and Q3 migrations. Pull legacy rollback times from the incident tracker. Rewrite the Q4 OKR around the scorecard. | TPM | 3 |
| 5 | Start the front-door rotation, fix the disk alerts properly, and begin pairing on the legacy plugins. | Ines + Bartek | 5 |

## 10. Re-check

Would you like me to set up a scheduled task for about 90 days out, timed to the Q4 retro? It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8. Without that check, the run never learns whether rollback-first was the right call.

## 11. Risk register

| Source | Risk | Condition / early warning sign | Evidence that clears it |
|---|---|---|---|
| Gate 2 (COND) | Humility is present, resolve is unproven. | The rollback epic slips a fourth time, or the Atlas decision is left to drift by consensus. | Ines publicly commits rollback as Q4 #1 and it ships. |
| Gate 3 (COND) | Missing seats: Payments co-owner, compliance partner, second legacy expert. | Payments keeps commenting from outside. | A named Payments engineer and compliance contact are on the migration. |
| Gate 4 (COND) | Weak red-flag mechanisms. | Alerts muted without tickets; incidents reviewed without a pipeline field. | Alert fix shipped; incident template updated; legacy rollback times reported. |
| Gate 5 (COND) | The passion circle and the denominator data are unconfirmed. | The team staffs Atlas-like work with enthusiasm and rollback reluctantly. | Volunteers staff rollback and approval; tiered coverage numbers exist. |
| Gate 8 (COND) | Step 1 has never turned, and the 3 → 4 link is unproven. | The VP funds visible work regardless of incident data. | Rollback in production; reliability headcount funded on the evidence. |
| Decline 1: hubris | "34 of 35 new services chose us," so the holdouts must be stubborn. | Retro language blaming Payments; critical coverage flat while total coverage grows. | Critical coverage is the headline metric. |
| Decline 2: undisciplined more | Atlas, more starters, scorecards. | New product lines appear in the OKRs. | The stop-doing list is reviewed each quarter. |
| Decline 3: denial | Legacy treated as "not ours"; Runway's flag misfire played down. | Incidents without a pipeline column. | Scorecard reported by pipeline. |
| Decline 4: grasping for salvation | After a big Payments outage: a forced-migration mandate, a big-bang rewrite, or buying a vendor platform. | Proposals of the form "all services by date X." | Steady pilot-first migrations with measured results. |
| Decline 5: capitulation | Runway becomes a template factory for low-risk services. Payments builds its own platform, or the team is reorganized into Atlas. | Payments hires its own platform engineers. | Card-auth-gateway on Runway within 12 months. |

**Shared root of the conditionals:** Five of eleven gates are CONDITIONAL. That is not more than half, but all five trace back to two root problems:
1. The team hasn't committed its scarce capacity to the hard, risky work (rollback and Payments).
2. It lacks risk-weighted measurement, so it can't show that the hard work matters.

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | An ongoing team with a steward (Ines), people to rearrange, a multi-year horizon and metrics. |
| 1 Baseline | PASS | Clearly good: 64% coverage, 34/35 new services, 58 → 41 min, 4.1/5, pages 52 → 37. |
| 2 Level 5 | CONDITIONAL | Strong humility, resolve not yet shown on rollback. |
| 3 First Who | CONDITIONAL | Right people; missing a Payments co-owner and compliance seat; Bartek is a single point of failure. |
| 4 Brutal Facts | CONDITIONAL | Facts are surfaced honestly; red-flag mechanisms are weak. No contradiction with Gate 1. |
| 5 Hedgehog | CONDITIONAL | The intersection is real; passion and denominator data are unconfirmed. |
| 6 Discipline | PASS | Seven-item stop-doing list and framework set. |
| 7 Tech | PASS | Triage below. |
| 8 Flywheel | CONDITIONAL | The loop closes; step 1 has never turned; link 3 → 4 is unproven. |
| 9 Built to Last | PASS | Values, purpose, one-line BHAG, mechanisms. |
| 10 Mighty Fall | PASS | Decline register in Section 11. |

**Count from the table:** 11 gates. PASS: 6 (Gates 0, 1, 6, 7, 9, 10). CONDITIONAL: 5 (Gates 2, 3, 4, 5, 8). FAIL: 0.

---

### Appendix: other gate artifacts

**Gate 0, subject card**

| Field | Value |
|---|---|
| Name | Delivery Platform team / Runway |
| Type | Team / org unit |
| Steward | Ines (EM), with the VP of Engineering above her |
| Horizon | Multi-year; the team is 3 years old |
| Stage | Good, and at a fork (Atlas versus rollback) |

**Gate 1, definition of great**
- **Superior performance:** the safest and fastest path to production for critical services.
- **Distinctive impact:** if Runway vanished, Brightwater's money-moving changes would go back to slow, unrecoverable legacy deploys.
- **Endurance:** it works without Bartek, without Ines, and without a lucky quarter.

**Gate 2, leadership read**
- **Strengths:** Ines points the window outward, asking to be removed from the hero slide. She invites dissent.
- **Gap:** her resolve on the cause. The rollback epic slipped three times on her watch, and the Atlas decision is deferred to consensus under VP time pressure.
- **One behavior change:** lead with questions, then decide and protect the decision in public.

**Gate 7, tech triage**

| Technology | Class | Note |
|---|---|---|
| Progressive rollout | Accelerates | Core of the Hedgehog Concept. |
| Fast and automatic rollback on health regression | Accelerates; **pioneer** | Step 1 of the flywheel. |
| Change approval as policy-as-code with an auto-generated audit trail | Accelerates; **pioneer** | Turns a Payments objection into a feature. |
| Feature flags | Accelerates | Needs guardrails; caused the notifications Sev-2. |
| Lightweight legacy deploy and rollback telemetry | Accelerates | Needed for the scorecard. |
| Service owner, tier and pipeline metadata | Accelerates | Also the spine for Atlas later. |
| Templates v3, Kotlin starter, secret manager, build-cache dashboard | Parity | Maintain, don't expand. |
| Developer portal UI, docs search, scorecards | Irrelevant for now | Drop for this team. |

**Hype flag:** Atlas's appeal is partly that it is greenfield and visible. Its evidence (58% in the survey, plus one peer company's onboarding result) is real but does not bear on this team's Hedgehog Concept.