# Tallypaw: Good to Great

## Verdict

**Good, not yet great. The biggest risk is filed under "housekeeping."**

- **Hedgehog Concept (working):** Tallypaw is the inventory system independent vet clinics trust to order every drug and supply, from any distributor. It grows by raising profit per inventory-active clinic.
- **Weakest flywheel link:** winning new clinics. 38% of ARR comes through VetSource, and most of the rest depends on Maya's demos.
- **Stop:** the dental pilot, the corporate-chain push, and adding roadmap items.
- **Most urgent fact:** VetSource carries about $912K of ARR. Its agreement renews in 5 months, it is building its own inventory tool, and it has ignored two renewal emails.
- **Numbers that would change this:**
  - who holds the contracts with VetSource-referred clinics;
  - S&M spend and churn by channel;
  - whether inventory's churn advantage holds outside VetSource accounts.
- **Confidence:** moderate. This rests only on founder-supplied numbers, with no outside research.

Greatness potential: 24/100

---

## 1. The great version in one paragraph

Great Tallypaw is the inventory system for independent vet clinics. Independents across its markets run their pharmacy and supply ordering on it, whichever distributor they buy from. It works for the clinic, not for the seller. Most clinics come through referrals and channels Tallypaw controls, not through one distributor's goodwill. Every clinic is inventory-active within weeks of signing. Churn sits at the inventory-clinic rate, not the reminder-only rate. Demos are run by a team trained in Maya's method. Support is staffed by people who have worked behind a clinic counter. Each added clinic sharpens the reorder suggestions and price benchmarks for the others. Reminders still exist, but as a cheap retention utility, not a battleground. The company stays out of dental and out of chains. It has decided that "venture-scale" will come from going deeper with independents, and it will not prove that by leaving them.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):** *Tallypaw is the inventory system independent vet clinics trust to order every drug and supply, from any distributor, and it grows by raising profit per inventory-active clinic.*

| Circle | Candidates considered | Chosen |
|---|---|---|
| **Best in the world at** | Practice software for small vet clinics; appointment reminders; inventory for vet clinics; **distributor-neutral drug and supply ordering for 1–4 vet independents**; clinic software in general (vet plus dental) | **Distributor-neutral drug and supply inventory for independent vet clinics.** Inventory is the module customers mention most, 71% of clinics attach it, and those clinics churn at about half the rate. |
| **Not best at** | Reminders (a commodity that depends on an SMS vendor), enterprise chains (0 of 2 pilots converted), human dental (no domain edge, different buyer), full practice management | Everything in this column is ruled out. |
| **Economic engine denominator** | ARR per clinic; logos; gross profit per clinic-year; **profit per inventory-active clinic** | **Profit per inventory-active clinic.** This captures both of what drives value here: inventory halves churn, and inventory is where pricing power lives. "Active" means the clinic orders through Tallypaw, which is different from merely having the module attached. |
| **Passion** | Serving the people they used to be; product craft; growth | **Helping independent clinics run well enough to stay independent.** Evidence: founders from inside clinics, CS staff who are former vet techs praised by name, and a CTO who built the inventory engine. |

**Why "distributor-neutral":** VetSource is building inventory tools inside its own portal. That tool will serve the distributor. Tallypaw's open position is to serve the clinic across all its suppliers. `[ASSUMPTION]` Independent clinics buy from more than one distributor. If they don't, neutrality is worth much less.

**Confirmation tests:**
1. Re-run the CTO's churn analysis split by channel. Does inventory still halve churn among *direct* (non-VetSource) clinics? VetSource bundles the inventory module, so channel may explain part of the effect.
2. Survey or pull order data: what share of clinics buy from two or more distributors?
3. Does converting reminder-only clinics to inventory measurably cut their churn within two quarters?
4. Does it rule things out? Yes: dental, chains, and a reminder feature race. Is it uncomfortable? Yes: it kills Maya's dental idea and the Head of Sales's plan, and it creates tension with VetSource.

## 3. The flywheel

```
 ┌─► 1. Clinic-native know-how (ex-practice manager CEO, vet-tech CS)
 │        │
 │        ▼
 │   2. Inventory engine that cuts stockouts, waste and drug spend
 │        │
 │        ▼
 │   3. Clinics go inventory-active and stay (~half the churn)
 │        │
 │        ▼
 │   4. More cross-clinic ordering data → sharper reorders + price benchmarks
 │        │
 │        ▼
 │   5. Practice managers refer peers → growth through channels Tallypaw controls
 │        │
 │        ▼
 │   6. Higher profit per inventory-active clinic
 │        │
 └────────┘  reinvested in the engine and in clinic-background people
```

**Weakest link: step 5.** About 38% of ARR flows through a partner that is turning into a competitor. Most of the rest depends on the CEO personally running demos. No one can currently say what a clinic costs to win by channel.

**Current push (the next two turns):**
1. **Secure distribution.** Either renew with VetSource on terms that don't hollow out the inventory module, or build the replacement path now (direct relationships with those clinics, a second distributor integration).
2. **Make every clinic inventory-active.** About 90 clinics (29%) are reminder-only. By rough math, they churn at about 14% a year, against about 7% for inventory clinics `[ASSUMPTION: derived; see Appendix B]`. Converting them is the cheapest growth available.

**Doom-loop check: warning signs are present.**
- New direction after new direction: an upmarket push to chains, then a second-market push into dental, both within about 8 months.
- A big program to jump-start momentum: two engineers for six months on a new vertical, justified by a non-binding LOI.
- Inconsistency: the board asked for fewer roadmap items, and the answer was deferred until after the new program.
- The trap ahead is *reaction without understanding*. If VetSource walks, the temptation will be to answer with a rushed "AI inventory" feature race or to grab dental revenue as a replacement. Both would be Stage 4 grasping (see section 11).

## 4. The bus

| Person / commitment | Call | Seat and reasoning |
|---|---|---|
| **Maya (CEO)** | Keep, adjust seat | Put the best person on the biggest opportunity. Right now that is the VetSource renewal and distribution strategy, not running most demos. She should codify her demo and hand off at least half of demos within 90 days. |
| **Jonah (CTO)** | Keep | He owns the inventory moat and the distributor-neutral build. His habit of owning mistakes first in post-mortems should become a company mechanism (see section 6). |
| **Head of Sales** | Move seat; review at day 90 | His enterprise-chain thesis fails the Hedgehog Concept and the evidence (0 of 2 pilots converted). New seat: build a repeatable *independent-clinic* direct engine, take demos off Maya, and produce channel-level CAC. If he can't commit to the independents market, it is a humane off-the-bus conversation. This is about the wrong role for this strategy, not about his worth. |
| **Customer success (2 former vet techs)** | Keep, protect | Customers praise them by name, so they are part of the moat. At 155 clinics each, they are stretched. |
| **Two engineers assigned to dental** | Move seat | Back to inventory: distributor integrations and activating reminder-only clinics. |
| **Dental LOI / pilot** | Off | A commitment, not a person. Decline or defer politely. Note that the buyer is a 14-office group, the same chain-like buyer that failed twice in vet. |
| **Corporate-chain pilots** | Off | End them cleanly. |
| **VetSource agreement** | Undecided: renegotiate | Stay on the bus only on terms that don't let VetSource absorb the inventory value. |
| **Missing: third CS hire (clinic background)** | Hire | Needed for inventory activation at scale. |
| **Missing: finance / RevOps owner** | Hire or assign | Nobody can produce S&M or churn by channel today. That gap is itself a finding. |
| **Missing: partnerships / channel lead** | Hire or assign (could report to Maya) | Second-distributor relationships, and VetSource whatever the outcome. |

## 5. Stop-doing list

1. **Stop the dental pilot.** Return both engineers to inventory now. Revisit only if the Hedgehog Concept's confirmation tests come back and the board sets kill criteria.
2. **Stop pursuing corporate chains.** End the remaining pilot conversations and remove chain features (multi-site rollups, SSO-for-enterprise) from the roadmap.
3. **Stop adding roadmap items.** Deliver the short roadmap the board asked for within 30 days. Every item must raise profit per inventory-active clinic.
4. **Stop treating VetSource as housekeeping.** It becomes the first agenda item at every board and leadership meeting until it is resolved.
5. **Stop selling reminder-only as an end state.** Every new clinic gets an inventory onboarding path with a date.
6. **Stop building reminder features beyond parity.** Renegotiate or switch the SMS vendor, and consider passing SMS costs through.
7. **Stop funding channels you can't measure.** No new trade-show or marketing commitments until spend and wins are attributed by channel.
8. **Stop routing most demos through Maya.**

## 6. Brutal facts and the faith statement

*No web research was possible in this session. Market and competitor facts below come only from the dossier. Facts marked `[ASSUMPTION]` are general knowledge that has not been verified.*

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The largest channel is becoming a competitor, and it has gone quiet five months before renewal | 38% of ARR (~$912K) is VetSource-referred. VetSource announced "native inventory intelligence." Two renewal emails are unanswered. | **Critical** | Maya |
| 2 | Nobody knows whether Tallypaw owns those 38% of customer relationships | The contract structure isn't stated. Losing about $711K a year of gross profit (~$59K/month) would shorten 20 months of runway by an unknown amount `[derived]`. | **Critical** | Maya + counsel |
| 3 | The inventory "moat" may be partly channel-driven | VetSource bundles the inventory module, and the churn analysis isn't split by channel. | High | Jonah |
| 4 | Leadership attention is going to new markets while the core is threatened | Dental at two engineers for 6 months. The chain push. The roadmap cut was deferred. | High | Maya + board |
| 5 | Sales depends on the founder | Maya runs most demos. | High | Head of Sales |
| 6 | Acquisition efficiency is unknown and probably mediocre | $1.1M of S&M bought about $0.84M of new ARR: about $1.31 per $1, and about $10K per clinic, a ~1.7-year payback `[derived]`. Spend isn't broken out by channel. | Medium | Finance/RevOps (missing seat) |
| 7 | Expansion is thin | NRR is 104%, so growth comes almost entirely from new logos. | Medium | Jonah + CS |
| 8 | Reminders are a commodity with rising cost | The SMS vendor raised prices 30%. Reminder-only clinics churn about twice as fast. | Medium | Eng lead |
| 9 | The core market may be shrinking | `[ASSUMPTION]` Corporate consolidation of vet clinics is reducing the independent base. This needs verification with market data. | Medium | Maya |
| 10 | "We need a second market to be venture-scale" hasn't been tested against the first market | 310 clinics is likely a small share of independents `[ASSUMPTION]`. No penetration or TAM figures were given. | Medium | Maya + board |

**Truth climate:** this is mixed. Jonah's blameless post-mortems are a real asset. Two red flags stand against it. The most severe risk in the company appeared under "housekeeping" in board notes. And the board's request for focus was deferred by the CEO. Maya is fast and decisive, which is the classic profile where bad news gets outrun rather than suppressed. **Red-flag mechanism:** open every board and leadership meeting with a standing "top three risks" list. Jonah owns it, and anyone can add to it.

**Faith statement:** *No distributor or chain vendor will ever understand how a small clinic actually orders drugs as well as people who did it themselves, and clinics that run inventory on Tallypaw stay twice as long to prove it.*

## 7. Core ideology and the BHAG

**Core purpose:** Keep independent veterinary clinics strong enough to stay independent.

**Core values:**
1. **Behind the counter first.** Build for how a small clinic actually works.
2. **The clinic's side of the counter.** We work for the clinic, not the seller.
3. **Tell the truth early.** Mistakes and bad news surface first, the way Jonah's post-mortems already do.
4. **Earn the next reorder.** Value is proven every month, not at signing.

**BHAG (about 14 years):** *By 2040, half of all independent vet clinics in our markets run their pharmacy and supply ordering on Tallypaw, and independents beat the chains on inventory cost.* `[ASSUMPTION: home market and clinic counts not given]`

**Clock-building mechanisms:**
- a documented demo playbook that others run;
- CS hiring from clinic roles;
- inventory-first onboarding with a dated activation target;
- monthly channel-level CAC and churn;
- a roadmap gate: every item states its effect on profit per inventory-active clinic;
- the standing risks list.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Inventory-active clinics** (ordering monthly, not just attached) | ~220 attached (71%). Active usage unknown. | 85% of clinics active `[ASSUMPTION target]` | Half of independents in our markets |
| **Profit per inventory-active clinic** (gross profit per clinic-year) | ~$6.0K blended proxy ($7.7K ACV × 78% GM) `[derived]`. Inventory-only figure unknown. | +10%, through neutral-ordering value and SMS cost control `[ASSUMPTION target]` | Rises every year as data and benchmarks compound |
| **Share of ARR through channels Tallypaw controls** | ~62% (non-VetSource) | ≥70%, through growth rather than loss `[ASSUMPTION target]` | No single partner above 20% |

Also track logo churn split by inventory vs reminder-only *and* by channel.

## 9. Next 90 days

| # | Action | Owner | Flywheel step |
|---|---|---|---|
| 1 | **VetSource.** Within two weeks, escalate beyond email to an executive-level meeting. In parallel, have counsel read the agreement: who holds clinic contracts, data rights, non-compete terms, notice and transition terms. Build Plan B: direct relationships with referred clinics (if permitted) and a second distributor integration. Set a hard decision date four months before expiry. | Maya (+ counsel) | 5 |
| 2 | **Focus.** Pause the dental pilot, end the chain pilots, and send the board a short roadmap within 30 days. | Maya | All (stops the doom loop) |
| 3 | **Prove the moat.** Re-run the churn analysis by channel. Measure multi-distributor buying. Ship one non-VetSource distributor integration using the two returned engineers. | Jonah | 2, 4 |
| 4 | **Activate the 90 reminder-only clinics.** Run inventory onboarding campaigns and start hiring a third clinic-background CS person. | CS lead | 3 |
| 5 | **Build the direct engine.** Codify Maya's demo, move at least 50% of demos off her, and report S&M and wins by channel monthly. The day-90 seat review depends on this. Separately, renegotiate or replace the SMS vendor. | Head of Sales; Eng lead (SMS) | 5, 6 |

## 10. Re-check

Offer: set a scheduled re-check for about **23 February 2027**, 90 days out. It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8. That date lands about two months before the VetSource expiry and just before the March lease renewal. This session has no scheduling tool, so the task has not been created.

## 11. Risk register

| Source | Risk | Condition / early warning | Trigger for action |
|---|---|---|---|
| Gate 1 (CONDITIONAL) | The quality of 38% of ARR is unknown | Contract ownership and channel economics are unverified | **PASS when:** counsel confirms who holds the contracts, and S&M and churn by channel are reported |
| Gate 2 (CONDITIONAL) | Founder focus and founder dependence | Dental deferred the roadmap cut. Maya runs most demos. | **PASS when:** the short roadmap is delivered before any dental work, and at least 50% of demos are run by others |
| Gate 3 (CONDITIONAL) | Head of Sales strategy is misaligned with the Hedgehog Concept | Still pushing chains | **PASS when:** he owns the independent-clinic engine with channel CAC by day 90; otherwise, a seat change |
| Gate 5 (CONDITIONAL) | The Hedgehog Concept rests on possibly confounded churn data | Inventory churn not split by channel. Multi-distributor buying unverified. | **PASS when:** direct-channel inventory clinics still churn about half as much, and most clinics use two or more distributors |
| Gate 10 (CONDITIONAL) | Stage 2–3 markers present today | Dental and chains alongside the VetSource silence | **PASS when:** dental is paused, and the VetSource renewal is signed or Plan B is executed |
| Decline: Stage 3 | Denial of the VetSource risk | No executive meeting by mid-December. VetSource-referred new bookings falling. VetSource portal ships inventory features. | No substantive renewal talks by **4 months before expiry**, or referred bookings down >30% vs the trailing 3-month average → execute Plan B fully |
| Decline: Stage 2 | Undisciplined pursuit of more (dental, chains, "venture-scale") | Engineering time on non-independent-vet work; roadmap item count rising | Any engineer allocated outside the Hedgehog Concept without board-set kill criteria |
| Decline: Stage 4 | Grasping for salvation if VetSource leaves | Dental or chain deals pitched as "replacement revenue" | Any new-market proposal made within 6 months of a VetSource loss → board review against the Hedgehog Concept first |
| Decline: Stage 1 | Hubris: "vets love us because we were one of them" | NPS 61 from 138 of 310 clinics may flatter. Silent clinics may be at risk. | NPS falls below 50, or response rate drops |
| Decline: Stage 5 | Runway runs out | 20 months at current burn. Burn not given. | Runway below 12 months without a funded plan |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing B2B startup with clear stewards, a multi-year horizon and metrics |
| 1 Baseline | CONDITIONAL | Good, not yet great: $2.4M ARR (+60%), 104% NRR, 78% GM, NPS 61. Ownership of the 38% via VetSource is unverified. |
| 2 Level 5 | CONDITIONAL | Maya shows strong resolve and domain credibility, but speed outruns discipline and sales depends on her. Jonah shows mirror behavior. |
| 3 First Who | CONDITIONAL | Head of Sales is in the wrong seat. Dental and chain commitments come off. CS, finance and channel seats are missing. |
| 4 Brutal Facts | PASS | VetSource is the critical fact. It threatens durability but doesn't contradict "good." |
| 5 Hedgehog | CONDITIONAL | Distributor-neutral inventory for independents. The churn evidence may be channel-confounded. |
| 6 Discipline | PASS | Eight concrete stop-doing items; adoption is tracked under Gate 2 |
| 7 Technology | PASS | Inventory and integrations accelerate. Reminders are parity. Dental and enterprise builds drop. |
| 8 Flywheel | PASS | The loop closes. Weakest link is acquisition. Doom-loop signs are flagged. |
| 9 Built to Last | PASS | Purpose, values, BHAG and mechanisms drafted (BHAG kept to one line) |
| 10 Mighty Fall | CONDITIONAL | Stage 2 and Stage 3 markers are present now |

**Tally (counted from the table):** 6 PASS, 5 CONDITIONAL, 0 FAIL. That is under half, but the five CONDITIONALs share two root problems: **dependence on VetSource without data on it**, and **focus discipline at the top**. Fix those two and most conditions clear.

**Evidence note:** there was no memory, past-chat or web search access, so the run uses the dossier alone. Market size, consolidation and competitor facts are unverified, and no prior scorecard baseline exists.

---

### Appendix A: Gate artifacts

**Subject card:**

| Field | Value |
|---|---|
| Name | Tallypaw |
| Type | Business (B2B SaaS) |
| Steward | Maya (CEO) with Jonah (CTO), overseen by the board |
| Horizon | Years. Runway is about 20 months. |
| Stage | Post-Series A, 23 staff, 5 years old |

**Leadership read (Gate 2):**
- **Strengths:** Maya has insider credibility, decisiveness and resolve for the cause, and is a proven seller. Jonah owns mistakes before anyone else, which is the Level 5 mirror in action.
- **Gaps:** Maya defers focus requests, and the company can't sell without her. There is no evidence about whether her ambition is aimed at herself or the company. Her drive reads as being for the company, but "venture-scale" pressure is steering it toward breadth.
- **One behavior change:** before starting any new initiative, Maya names in writing the roadmap item it replaces, and shows the board.

**Tech triage (Gate 7):**

| Technology | Call |
|---|---|
| Inventory engine / reorder suggestions | **Accelerates** |
| Multi-distributor catalog and ordering integrations | **Accelerates. Pioneer opportunity.** |
| Anonymized cross-clinic price and usage benchmarks | **Accelerates. Pioneer opportunity** (check data rights under the VetSource contract). |
| Controlled-substance logging | Possible accelerator `[ASSUMPTION: relevance and current coverage unknown]` |
| Reminder module / SMS vendor | Parity. Minimize cost. |
| Generic "AI" features not tied to inventory | Hype risk. Flag any feature built mainly to match VetSource's announcement. |
| Dental build; enterprise chain features | Irrelevant. Drop. |

### Appendix B: Derived figures (all from dossier numbers, all approximate)

| Figure | Calculation | Result |
|---|---|---|
| VetSource ARR | 38% × $2.4M | ≈ **$912K** |
| VetSource gross profit | $912K × 78% | ≈ $711K/yr, ≈ $59K/month |
| Retained base | $1.5M × 104% | $1.56M |
| New-logo ARR | $2.4M − $1.56M | ≈ **$0.84M** |
| Implied gross new clinics | $0.84M ÷ $7.7K, assuming new clinics sign at average ACV | ≈ 109 |
| Implied churned clinics | 109 − 90 net adds | ≈ 19, about 9% logo churn |
| Segment churn | Solving 0.71·(x/2) + 0.29·x = 9% | Reminder-only ≈ 14%, inventory ≈ 7% |
| CAC | $1.1M ÷ 109 | ≈ $10K per clinic |
| Gross profit per clinic-year | $7.7K × 78% | ≈ $6.0K |
| Blended payback | $10K ÷ $6.0K | ≈ 1.7 years |
| Reminder-only clinics | 29% × 310 | ≈ 90 |
| Clinics per CS person | 310 ÷ 2 | 155 |