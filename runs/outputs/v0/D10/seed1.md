# Good to Great: Delivery Platform team (Brightwater Financial)

## Verdict

**The team is good and has a clear path to great. Getting there means declining to own Atlas on the terms offered, and shipping the fast-rollback work it has postponed for three quarters.**

- **Hedgehog Concept (working hypothesis):** *Make Runway the one road at Brightwater where any change, including changes to regulated, money-moving services, ships fast and can be undone in under five minutes.*
- **Weakest flywheel link:** the first push has never happened. Sub-5-minute rollback has slipped three quarters running. The next link, "rollback ships, then Payments migrates", rests on a spoken condition from Payments, not a written commitment.
- **Top 3 stop-doing:**
  1. Don't take ownership of Atlas now. Counter-offer the two headcount toward rollback and the change-approval gate.
  2. Stop doing one-off pipeline tweaks on request.
  3. Drop "80% of services on Runway" as the headline goal. It counts a toy service the same as `card-auth-gateway`.
- **Most urgent brutal fact:** **5 of 6** Sev-1/Sev-2 incidents this quarter happened on legacy pipelines. So did **both** Sev-1s, and **4 of 6** were in Payments. `card-auth-gateway` took **47 and 22 minutes** to roll back. The company's biggest deploy risk sits outside Runway, and the team has been told exactly what would bring it in.
- **Missing numbers that would change this answer:**
  - the list of Tier-1 (money-moving) services, and how many are still on legacy
  - how the 4,212 deploys split between Runway and legacy, which gives per-deploy incident rates
  - Runway's current rollback time
  - a real estimate for the rollback epic
  - whether the VP's headcount can be redirected away from Atlas
  - how many of Q3's +25 Runway services were migrations rather than new services

Greatness potential: 40/100

> **Evidence note:** This run used autonomous mode and only the Q3 retro dossier. There was no access to memory, past runs or web research, so there is no earlier scorecard baseline and no outside market check. Every inference is marked `[ASSUMPTION]`.

---

## 1. The great version in one paragraph

In its great version, Delivery Platform is the team Brightwater cannot do without. Every service that authorizes, moves or reconciles customer money ships on Runway. Each has a drilled rollback under five minutes and a compliance approval step built into the pipeline, so audit evidence comes with every deploy. Deploy-caused Sev-1s are rare and short. Payments, the hardest customer, moved because Runway met its stated conditions, not because of a mandate. The team's capacity grows because legacy pipelines shrink, interrupts dry up and leadership funds it for measurable risk reduction rather than visible launches. It is known for making the safe way the easy way, not for building the most tools. Developer portals, language starters and legacy maintenance are things it supports or hands off. They are not what it is.

## 2. The Hedgehog Concept

**Sentence:** *Make Runway the one road at Brightwater where any change, including changes to regulated, money-moving services, ships fast and can be undone in under five minutes.*

| Circle | Candidates considered | Kept | Ruled out (cannot be best at) |
|---|---|---|---|
| **Best in the world at** (the world is Brightwater) | Paved-road deploys; templates and scaffolding; safe progressive rollout and rollback for regulated services; developer portal; legacy pipeline support | **Safe, fast, reversible deploys for every service, including compliance-bound ones.** No other group at Brightwater can do this, and outside tools don't know Brightwater's audit rules. | A developer portal (a commodity category with off-the-shelf options). Maintaining legacy pipelines (they belong to other teams). Starter templates for every language (nice to have, not distinctive). |
| **Resource engine** (budget and headcount leverage) | Services on Runway; deploy count; developer satisfaction; Sev-1/2 incidents avoided; Tier-1 services on Runway | **Per Tier-1 service on Runway with drilled sub-5-minute rollback.** Leadership funds platform teams for reducing business risk, and each Tier-1 migration removes the most expensive kind of incident. | A raw service count, which rewards migrating easy services. Satisfaction, which only covers people already on Runway. |
| **Passion** | Polished greenfield products; visibility; craft (template v3 shipped early); making other engineers' lives easier; reliability | **Building products other engineers love, and shipping them well.** Rollback plus the compliance gate is itself greenfield, high-visibility product work, so it should be framed that way. | — `[ASSUMPTION: this reframe is untested. Most of the team's visible energy right now is for Atlas.]` |

**Denominator:** Tier-1 services on Runway with drilled sub-5-minute rollback. `[ASSUMPTION: Tier-1 means services that authorize, move or reconcile customer money, or are in card-network compliance scope. Examples: card-auth-gateway, payouts-scheduler, ledger-recon, loan-disbursement.]`

**Tests:**
- *Does it explain past wins?* Yes. 34 of 35 new services chose Runway because it is the easiest path. Median commit-to-production dropped from 58 to 41 minutes. Satisfaction is 4.1 out of 5.
- *Does it explain the gaps?* Yes. The holdouts are exactly the services where deploy safety matters most, and their owners have named the safety features they are waiting for.
- *Does it rule things out?* Yes: Atlas, more starter templates, ad-hoc tweaks and broad legacy instrumentation.
- *Is it uncomfortable?* Yes. It means turning down visible work and two headcount, and disappointing a team that is excited about Atlas.

**What would confirm it within 2–3 quarters:**
1. Payments signs a written migration list with dates, tied to the two criteria.
2. The first Tier-1 Payments service cuts over and passes a rollback drill.
3. Deploy-caused Sev-1/2 incidents on migrated services fall.
4. The team staffs rollback willingly rather than reluctantly.

## 3. The flywheel

```
 ┌─► 1. Ship sub-5-min rollback + compliance approval gate in Runway
 │          │
 │          ▼
 │   2. Tier-1 (Payments, then Lending) services migrate, with a rollback drill at cutover
 │          │
 │          ▼
 │   3. Fewer, shorter deploy incidents on money-moving services
 │          │
 │          ▼
 │   4. Proof → trust: Payments, VP and other orgs see measured risk reduction
 │          │                      → funding and voluntary adoption
 │          ▼
 │   5. Legacy shrinks → fewer interrupts, no legacy-plugin heroics → freed capacity
 │          │
 └──────────┘  6. Capacity reinvested in the next safety capability
                  (automated canary-triggered rollback, policy-as-code approvals)
```

**Denominator in the loop:** step 2 (Tier-1 services on Runway with drilled rollback).

**Current push (Q4):** Turns 1 and 2. Ship rollback on Runway and drill it on a pilot service. In parallel, get Payments' change-approval requirement written down precisely with their compliance owner, and agree a first service to migrate. `[ASSUMPTION: a lower-risk Payments service first, then card-auth-gateway.]`

**Doom-loop check:**

| Doom-loop sign | Present? | Evidence |
|---|---|---|
| New direction after new direction | **Yes, mild** | Template v3, then the Kotlin starter, now Atlas. Each was worthwhile, and each displaced rollback. |
| A big program to jump-start momentum | **At risk** | Atlas comes with two headcount and a deadline. It is the textbook shape of this sign. |
| Reaction without understanding | **Yes, mild** | The 80% goal was set without tiering services and without checking whether the pace allows it. |
| Inconsistency | Partial | Rollback has been "next" three quarters running. |

The loop closes, but the team is one decision away from a doom-loop turn.

## 4. The bus

| Person or commitment | Call | Reasoning |
|---|---|---|
| **Ines (EM)** | **Keep**, and own the decision | Strong humility signals. Resolve gap: see Gate 2. |
| **Mei** | **Move seat → co-lead rollback and the compliance gate** | She shipped template v3 two weeks early. Put the best people on the biggest opportunity. |
| **Sana** | **Keep, co-lead rollback with Mei** | The three carry-overs came from prioritization, not from her. Give her staff and protection, not just another re-estimate. |
| **Bartek** | **Move seat → Payments migration engineer and legacy-knowledge transfer** | He is the only person who understands the legacy plugins, which is exactly the knowledge migration needs. Use it to retire the legacy pipelines, not to keep them alive. Fix or delete the muted alerts first. |
| **Ravi** | **Keep → finish the gRPC example only if it takes under a week, then join rollback** | Freeze further starter work. |
| **TPM** | **Move seat → Payments migration program and compliance liaison** | The Payments contract (requirements, dates, sign-offs) is now the critical path. |
| **Tomasz and other engineers** | Keep, assign to the current push | `[ASSUMPTION: no information on individual fit]` |
| **Intern's build-cache dashboard** | Keep the tool, give it no roadmap | Useful. It must not become a product line. |
| **Atlas ownership** | **Off the bus (for now)** | Outside the Hedgehog Concept. See stop-doing #1. |
| **Free legacy-plugin debugging for Payments** | **Off the bus as a habit** | Time-box it, and only for services with a scheduled migration. |
| **One-off pipeline tweaks** | **Off the bus** | Replace with an intake rule. |
| **Missing: named Payments engineering and compliance counterpart** | **Missing seat** | Someone on their side who owns the migration and can sign off the approval design. |
| **Missing: second legacy-plugin expert** | **Missing seat** | Bus factor of one. Pair someone with Bartek. |
| **Missing: executive sponsor for the Tier-1 metric** | **Missing seat** | Ideally the VP, so the Atlas "no" turns into a "yes" to something she cares about more. |

## 5. Stop-doing list

1. **Don't take ownership of Atlas this year.** Counter-offer: put the two headcount on rollback and the compliance gate; revisit Atlas once the first Tier-1 Payments services are on Runway; and Runway exposes its service metadata (owners, templates, deploy health) for whoever builds a catalog.
   - *Fallback, if the VP insists:* hire both people into a separate Atlas cell, move no existing engineers onto it, and make rollback the first line of every status update. This is worse, because it splits management attention, but it is survivable.
2. **Stop one-off pipeline tweaks.** Take requests through a fortnightly intake. If the same request arrives three times, it becomes a template feature. Otherwise the answer is no, with a pointer to an extension point.
3. **Drop "80% of services" as the headline goal.** It needs about +53 services in Q4 (80% of 331 is about 265, against 212 today), compared with +25 in Q3. It also rewards migrating the easiest services. Keep overall coverage as a guardrail metric.
4. **Freeze new language starters and template feature work** until rollback ships.
5. **Stop free legacy-plugin rescues.** Only do them for services with a committed migration date, and document every fix.
6. **Stop muting alerts without a ticket.** Fix them or delete them. Muted alarms are ignored information made official.
7. **Don't instrument legacy pipelines broadly.** On the parking-lot question, the answer is no. The exception is a cheap baseline of time-to-restore for Tier-1 legacy services, pulled from the incident tracker, so that migration gains can be measured.

## 6. Brutal facts and faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Most deploy risk sits outside Runway, in Payments. | 5 of 6 Sev-1/2 incidents were on legacy, including both Sev-1s; 4 of 6 were in Payments; `card-auth-gateway` failed twice. | **High** | Ines + TPM |
| 2 | The team repeatedly picks visible work over the thing that unlocks adoption. Atlas would be the fourth time. | Rollback epic carried over 3 quarters, behind template v3 and the Kotlin starter. | **High** | Ines |
| 3 | Payments has stated its entry price, and the team has built neither part of it. | Payments wants rollback under 5 minutes and its change-approval step supported. | **High** | Mei + Sana |
| 4 | The Q4 goal can't be reached and points at the wrong thing. | It needs +53 services against +25 last quarter. 35 services were created but the total grew by only 5, so about 30 were retired. How many of the +25 were real migrations is unknown. | Med-High | Ines + TPM |
| 5 | Legacy-pipeline knowledge has a bus factor of one, and alarms are muted. | Bartek is "the only person who can still debug" the plugins. Two alerts are muted. | Medium | Bartek |
| 6 | The team can't yet prove Runway is safer per deploy. | Legacy is not instrumented. The deploy split is unknown. Six incidents is a small sample. Satisfaction is measured only among Runway users. | Medium | TPM |
| 7 | Runway has failures of its own. | Sev-2 on `notifications` from a feature-flag misfire. Payments will cite it. | Medium | Ravi `[ASSUMPTION]` |
| 8 | The Atlas problem is real, so a "no" needs an answer attached. | 58% of engineers say finding owners and docs is hard. The VP is waiting on a deadline. | Medium | Ines |
| 9 | The interrupt load means the paved road has gaps, or the team says yes too often. | "Too many interrupts" for one-off tweaks. | Low-Med | Bartek / Ravi |

**Truth climate:**
- *Good signs:* the retro names its failures; two people raised the rollback risk out loud; Ines asked for a team decision rather than dictating one.
- *Weak signs:* no blameless autopsy after three carry-overs; muted alerts; the "not our services, not our budget" stance toward the incidents that matter most.
- *Charisma check:* Ines isn't suppressing bad news. The pressure comes from the VP's offer and deadline and from team excitement, not from a dominant personality.

**Faith statement:** *Runway already wins nearly every new service and Payments has told us exactly what it takes to win theirs. When we build that, the hardest services in the company come to us.*

## 7. Core ideology and BHAG

**Core values:**
1. Make the safe way the easy way.
2. Undo is a feature.
3. Earn adoption; don't mandate it.
4. Credit the crew. (Ines swapping herself off the hero slide is the model.)
5. Fix the alarm; don't mute it.

**Core purpose:** *So Brightwater's engineers can change money-moving software quickly without putting customers' money at risk.*

**BHAG (one line, because this is a team inside a larger company):** *No Brightwater customer is ever harmed by a deploy that couldn't be undone in five minutes.*

**Clock-building mechanisms:**
- Rollback drills before every Tier-1 cutover, then quarterly.
- A Tier-weighted scorecard reviewed every quarter.
- A carry-over rule: any item carried twice triggers a blameless autopsy and an explicit keep or kill decision.
- Intake rules for tweak requests.
- Documented, paired legacy-plugin knowledge.
- Compliance approval implemented as an auditable deploy gate rather than a person.

## 8. Scorecard

| Output | Current (end Q3 Y0) | 12-month target `[ASSUMPTION: proposed]` | BHAG trajectory |
|---|---|---|---|
| **Tier-1 services on Runway with drilled sub-5-min rollback** | Unknown. Effectively **0 with drilled rollback**, since rollback hasn't shipped. | ≥50% of Tier-1, including `card-auth-gateway` and `payouts-scheduler` | 100% of Tier-1 |
| **Deploy-caused Sev-1/2 incidents per quarter** | **6** (5 legacy, 1 Runway); 2 Sev-1 | ≤2 per quarter; 0 deploy-caused Sev-1 | Approaching 0; none customer-harming |
| **p90 time to roll back a bad Tier-1 deploy** | Observed **22–47 min** on `card-auth-gateway` (legacy); Runway unknown | <5 min on every migrated Tier-1 service | <5 min everywhere, automated |

Guardrails, which must not get worse:
- overall coverage (64%)
- median commit-to-production time (41 min)
- Runway satisfaction (4.1/5)
- team pages per quarter (37)

## 9. Next 90 days

| # | Action | Owner | Flywheel turn |
|---|---|---|---|
| 1 | Before the offsite, decide and own the Atlas call. Present the VP with the counter-offer (headcount to rollback and the compliance gate, a dated Atlas revisit, a Runway metadata export). Explain it to the team as a choice of greenfield, not a ban on it. | **Ines** | Protects turn 1 |
| 2 | Ship sub-5-minute rollback on Runway and drill it on a pilot service. Staff it as the team's number-one priority, with no carry-over allowed. | **Mei + Sana** | Turn 1 |
| 3 | Get Payments' conditions in writing: the exact change-approval requirements, signed off by their compliance owner; the migration list with dates; the first pilot service. Design the approval step as an auditable deploy gate. | **TPM** (with Payments platform lead) | Turns 1 → 2 |
| 4 | Replace the 80% goal with the Tier-1 scorecard. Build the Tier-1 inventory and the legacy time-to-restore baseline from the incident tracker. | **Ines + TPM** | Measures turns 2–3 |
| 5 | Pair someone with Bartek on legacy plugins and write the runbook. Fix the disk alerts. Start the tweak-intake rule. | **Bartek** (pair: Ravi) | Turn 5 |

## 10. Re-check

I can set up a scheduled re-check about 90 days out, around the end of Q4 Y0. It would re-score the table above with real numbers and re-run Gates 1, 5 and 8. In particular it would check whether rollback shipped, whether Payments signed, and whether the Atlas decision held. This session has no tools, so it isn't scheduled yet. Ask for it and I'll set it up.

## 11. Risk register

| Source | Risk / open condition | Evidence that clears it | Early warning |
|---|---|---|---|
| Gate 2 (CONDITIONAL) | Leader humility is clear. Resolve is unproven, since rollback slipped 3 times under the current leadership. | Ines makes and owns the Atlas call. Rollback ships in Q4 with a named owner. | The decision is pushed to a team vote "for consensus" after the deadline. |
| Gate 5 (CONDITIONAL) | The passion circle is unconfirmed, and the Payments commitment is only spoken. | Engineers volunteer for the rollback work. Payments signs the migration list. | Payments adds new conditions once rollback ships. |
| Gate 6 (CONDITIONAL) | The stop-doing list hasn't been adopted. | The Q4 plan shows Atlas declined or ring-fenced, and starters frozen. | New scope enters the plan while rollback is "in progress." |
| Shared root (Gates 2, 5, 6) | **(a)** A habit of picking visible greenfield work over the unlock. **(b)** An unverified Payments commitment. | Actions 1 and 3. | — |
| Fact | Bus factor of one on legacy plugins. | Pair trained, runbook written. | Bartek is pulled into a Payments incident while away from work. |
| Decline 1: Hubris | "200 services, 34 of 35 new ones" breeds the belief that adoption will look after itself. | — | The team celebrates count metrics while the Tier-1 number stays flat. |
| Decline 2: Undisciplined more | Atlas, more starters, more templates. | — | Scope is accepted while rollback is still open. |
| Decline 3: Denial | "Not our services, not our budget"; muted alarms. | — | Legacy incidents explained away in retros. |
| Decline 4: Grasping | A mandated big-bang migration or a reorg after Payments says no. Atlas used to regain visibility. | — | A new tool or reorg is proposed as the fix. |
| Decline 5: Capitulation | Payments builds its own platform. Runway ends up serving only low-risk services, and the team is folded into a generic DevEx group. | — | Payments starts staffing its own pipeline team. |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing team with a steward, people, a multi-year horizon and metrics. |
| 1 Baseline | PASS | Clearly good: 64% coverage, 34/35 new services, 41-min median, 4.1/5. |
| 2 Level 5 | CONDITIONAL | Humility strong; resolve unproven after three rollback slips. |
| 3 First Who | PASS | No misaligned key seat. Move best people to rollback. Three missing seats. |
| 4 Brutal Facts | PASS | Nine facts; none contradicts the baseline. Legacy and Payments risk dominate. |
| 5 Hedgehog | CONDITIONAL | Safe, fast, reversible deploys for every service. Passion and Payments unconfirmed. |
| 6 Discipline | CONDITIONAL | Seven stop-doing items; not yet adopted. |
| 7 Tech | PASS | Rollback and the approval gate accelerate the Hedgehog; Atlas and broad legacy instrumentation don't. |
| 8 Flywheel | PASS | Six-step loop closes; doom-loop signs logged. |
| 9 Built to Last | PASS | Five values, a purpose, a one-line BHAG, mechanisms. |
| 10 Mighty Fall | PASS | Five decline paths, each with a warning sign. |

**Count:** 8 PASS, 3 CONDITIONAL, 0 FAIL. That is under half CONDITIONAL. All three trace back to the two shared roots listed in the risk register.

---

### Appendix: gate artifacts not covered above

**Subject card (Gate 0):**
- *Subject:* Delivery Platform team (Runway).
- *Type:* team / org unit.
- *Steward:* Ines (EM); the VP of Engineering controls headcount.
- *Horizon:* multi-year; the team is in year 3.
- *Stage:* past early adoption, now facing the hard tail.
- *Great means:* indispensable output.

**Baseline (Gate 1):**
- *Good:* coverage went from 57% to 64%; 97% of new services chose Runway; median commit-to-production fell from 58 to 41 min; satisfaction 4.1/5 among Runway users; pages fell from 52 to 37; secret-manager migration with zero incidents.
- *Great tests:*
  - **Superior:** the safest and fastest way to ship any Brightwater service.
  - **Distinctive:** if Runway vanished, regulated deploys would fall back to fragmented, slow-to-roll-back pipelines.
  - **Enduring:** it works without heroes like Bartek or Mei, through mechanisms.
- *Scorecard outputs:* see section 8.

**Leadership read (Gate 2):**
- *Strengths:* window and mirror (asked for crew credit instead of the hero slide); invites dissent.
- *Gap:* resolve. Three slips, and a high-stakes call deferred to a group that is excited about the alternative.
- *Behavior change:* make the Atlas and rollback call personally, explain it, and own it if it turns out wrong.
- *Succession:* Mei is a credible lead for the next major initiative. `[ASSUMPTION]`

**Tech triage (Gate 7):**

| Tool / tech | Classification |
|---|---|
| Fast rollback; compliance approval gate; progressive rollout; templates | **Accelerates** |
| Feature flags | **Accelerates, with guardrails** (caused a Sev-2) |
| Kotlin starter; build-cache dashboard; secret manager; build-cluster alerting | **Parity** |
| Atlas portal; broad legacy instrumentation | **Irrelevant to the Hedgehog now** |
| Hype check | Atlas adoption is partly visibility-driven. |
| Pioneer opportunities | Canary-analysis-triggered automatic rollback for payment services; policy-as-code compliance approvals that produce audit evidence on every deploy. |

*All conclusions are disciplined hypotheses drawn from one quarter's retro, not guarantees. Collins's method was retrospective, and several of his "great" companies later declined.*