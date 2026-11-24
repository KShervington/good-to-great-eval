# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict

**Hedgehog Concept (working hypothesis):** *Runway is how Brightwater safely changes the systems that move customers' money. Every deploy carries its compliance sign-off and can be rolled back in under five minutes.*

**Weakest flywheel link:** the first one. Runway has neither sub-five-minute rollback nor a change-approval step, and those are the two conditions Payments set for moving its services. The rollback epic has now slipped three quarters running. Until it ships, the flywheel doesn't turn.

**Stop doing (top 3):**
1. **Atlas as offered.** Decline the portal for now. Counter-offer the VP: take the two headcount and point them at rollback and approval.
2. **New starters and template extras** (for example, the Kotlin gRPC example) until rollback ships.
3. **The "80% of services on Runway" OKR.** It counts a hello-world service the same as card-auth-gateway.

**Most urgent brutal fact:** 5 of the 6 Sev-1/2 incidents this quarter, including both Sev-1s, happened on legacy pipelines. Four of the six were Payments services. card-auth-gateway went down twice from bad deploys and took 47 and 22 minutes to roll back. The risk sits in the services Runway doesn't serve, and Payments has said exactly what would bring them over.

**Missing numbers that would change this answer:**
- How many services Payments (and Lending) still run on legacy.
- Runway's current rollback time.
- Whether sub-five-minute rollback is feasible within one quarter.
- What the card-network audit actually requires the approval step to record.
- How many existing services migrated this quarter versus were retired.
- Hours lost to interrupts and to legacy-plugin support.

Greatness potential: 55/100

---

*How this run was done:* autonomous mode. This session had no memory, past chats or web search, so there was no prior baseline, no market research and no evidence questions. Everything below comes from the Q3 retro dossier. Every inference is marked `[ASSUMPTION]`.

---

## 1. The great version in one paragraph

A year from now, the great Delivery Platform team is the reason a bad deploy at Brightwater is a five-minute non-event instead of a 47-minute card-authorization outage. Runway is the paved road for every service, and it is the *only* road for money-moving services, because it is the one path that rolls back in under five minutes and records the compliance sign-off the card-network audit needs. Payments moved because Runway delivered what Payments asked for, not because of a mandate. Lending followed. Legacy pipelines are being retired, Bartek's knowledge is written down, and interrupts arrive as requests in a queue instead of pings. The team is judged by deploy-caused incidents and recovery time, not by a service count. Leadership funds it for that reason.

## 2. The Hedgehog Concept

| Circle | Candidates considered | Selected | What it rules out |
|---|---|---|---|
| **Best in the world at** (the world here is Brightwater) | (a) the golden path for new services; (b) safe, auditable change for money-moving services; (c) an internal developer portal | **(b).** (a) is already largely won: 34 of 35 new services started on Runway. (c) is greenfield work in which the team has no edge, and portals are a build-or-buy category `[ASSUMPTION]`. Nobody else at Brightwater is positioned for (b): Payments maintains its own legacy pipelines, and Runway already does progressive rollout. | The portal, language-starter breadth, maintaining legacy pipelines as a service |
| **Resource engine** (budget and headcount leverage) | services on Runway; deploys per quarter; developer satisfaction; incidents avoided | **Leadership funds the team for reducing customer-facing risk.** The VP's offer shows headcount is available; the question is what it is earned for. | Count-chasing low-risk services to hit a percentage |
| **Passionate about** | greenfield, visible work (Atlas); great developer experience (template v3 shipped early, 4.1/5); not getting paged (pages fell from 52 to 37) | **"Shipping without fear":** developer experience aimed at the riskiest deploys. `[ASSUMPTION]` The team will choose this over Atlas. Two members already raised the rollback concern. | Work chosen mainly because it is new |

**Denominator:** *money-moving services on a sub-five-minute-rollback path.* Today that number is effectively zero `[ASSUMPTION: the incident table shows no Payments service on Runway, and Payments says it will not move until rollback is under five minutes]`.

**Tests**

- **Explains past wins?** Partly. Runway won new services on convenience. It has not yet won the critical ones, which is why the hedgehog has to narrow toward them.
- **Rules things out?** Yes: Atlas, new starters, ad-hoc tweaks and the 80% count.
- **Uncomfortable?** Yes. It means saying no to the VP's offer as framed, and no to the work the team is most excited about.

**Confirmation tests (this is a hypothesis):**
1. A spike shows sub-five-minute rollback on a real Runway service.
2. Payments names, in writing, which services it will move once both conditions are met.
3. The team chooses this at the planning offsite without being ordered to.
4. The first migrated Payments service has a bad deploy and recovers in under five minutes.

## 3. The flywheel

```
 ┌─► 1. Runway: rollback < 5 min + built-in compliance approval
 │            │
 │            ▼
 │   2. Money-moving services migrate (Payments first, then Lending)
 │      [denominator: money-moving services on a <5-min rollback path]
 │            │
 │            ▼
 │   3. Fewer, shorter deploy-caused Sev-1/2s (minutes, not 47)
 │            │
 │            ▼
 │   4. Visible proof in the incident tracker → trust from Payments,
 │      engineers and leadership
 │            │
 │            ▼
 │   5. Mandate and protected capacity: headcount aimed at the hedgehog,
 │      legacy sunset, less Bartek/legacy firefighting, fewer interrupts
 │            │
 │            ▼
 └── 6. Reinvest in deeper safety (auto-rollback on health signals,
        approval evidence captured automatically)
```

**Current push (next two turns):**
- **Turn 1:** ship sub-five-minute rollback and a minimal approval step. Pilot both on card-auth-gateway, the service that hurt twice.
- **Turn 2:** migrate the four Payments services from this quarter's incident table, and report their recovery times at the Q1 review.

**Doom-loop check:**

| Sign | Present? |
|---|---|
| New direction after new direction | **Yes, a risk.** Template v3, then Kotlin, then the gRPC example, and now Atlas. Each one pushed rollback back. |
| A big program to jump-start momentum | **Atlas fits the pattern.** It is visible, greenfield and comes with headcount, but it would not have prevented any of the six incidents. |
| Reaction without understanding | Interrupt-driven one-off tweaks. Alerts muted instead of fixed. |
| Inconsistency | The rollback epic has been carried over three times. |

## 4. The bus

| Person / commitment | Call | Reason |
|---|---|---|
| **Ines (EM)** | Keep, steward | Strong humility. Needs to own the rollback-versus-Atlas call (see the Appendix, Gate 2). |
| **Sana** | Keep, give protected seat | Technical owner of rollback, with real protected capacity. The three slips were priority decisions, not hers. |
| **Mei** | **Move seat** → delivery lead for rollback + approval `[ASSUMPTION]` | She shipped template v3 two weeks early. Put the best people on the biggest opportunity. |
| **Bartek** | **Move seat** → Payments migration engineer | His legacy knowledge becomes migration knowledge. He documents it and pairs with someone, so it stops living in one head. |
| **Ravi** | Keep, re-seat `[ASSUMPTION]` | Pause the gRPC example. Move to approval-step or migration tooling. |
| **TPM** | Keep, new seat | Owns the Payments migration agreement and the new scorecard. |
| **Tomasz and the other engineers** | Keep `[ASSUMPTION: no data]` | Run Runway core and parity work, including the disk-alert fix. |
| **Atlas (commitment)** | **Off the bus for now** | Outside the hedgehog. Revisit once the first Payments service is on Runway, or the VP finds it another owner. |
| **One-off pipeline tweaks via interrupt** | **Off** | Replace with a request queue, weekly triage and documented extension points. |
| **Open-ended legacy-plugin support for Payments** | **Off over time** | Timebox it now and sunset it as services migrate. |
| **"80% of services" OKR** | **Off** | Replace with the scorecard below. |
| *Missing:* Payments design partner | **Add** | A named Payments engineer with allocated time, working inside the team's sprint. |
| *Missing:* compliance/audit counterpart | **Add** | Defines what the approval step must record. |
| *Missing:* backup for legacy knowledge | **Add** | Bartek is the only person who can debug the legacy plugins. |
| *VP headcount (2)* | Accept only for the hedgehog seat | When in doubt, don't hire. Two people hired for Atlas would be the right people in the wrong seats. |

## 5. Stop-doing list

1. **Atlas as a greenfield portal.** The 58% "hard to find owner/docs" figure is real pain, but the evidence offered is one peer-company anecdote, and it is not this team's hedgehog. The team itself asked whether it would delay rollback again, and it would.
2. **New language starters and template extras** (Kotlin gRPC example and similar) until rollback ships to Payments.
3. **Chasing "80% of services."** Hitting 80% in Q4 needs about 265 of 331 services, which is +53. Last quarter's net gain was +25, and almost all of it came from new services. The only quick way to hit the number is to migrate low-risk services, which does nothing for the risk.
4. **Interrupt-driven one-off pipeline tweaks.** Use a queue and self-serve extension points instead.
5. **Muting alerts without a fix and an owner.** The two muted disk alerts get a ticket and a deadline.
6. **"Re-estimate" as an action item for the hedgehog epic.** Replace it with a ship date and an explicit scope cut.
7. **Treating legacy-pipeline risk as "not our services, not our budget."** That is where 5 of 6 Sev-1/2s happened.
8. **Expanding the intern build-cache dashboard.** Keep it running as is, and don't grow it.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Deploy risk lives on legacy pipelines, mostly in Payments | 5 of 6 Sev-1/2 on legacy, including both Sev-1s; 4 of 6 were Payments | Critical | Ines |
| 2 | The one feature that unlocks Payments has slipped three quarters running | Rollback epic carried over a third time, behind template v3 and Kotlin | Critical | Ines + Sana |
| 3 | card-auth-gateway is the single most dangerous service, and it isn't on Runway | Two bad deploys; 47- and 22-minute rollbacks; customers likely couldn't pay `[ASSUMPTION]` | Critical | TPM + Payments lead |
| 4 | The headline metric misleads | Runway grew by 25 while 34 new services started on it, so existing services were retired or moved off faster than legacy ones migrated on. Net migration of existing services was between 0 and 21 and can't be pinned down. The 80% target is out of reach without count-chasing. | High | Ines + TPM |
| 5 | Accepting Atlas will almost certainly delay rollback a fourth time | The team raised this itself, and the VP wants an answer before the offsite | High | Ines |
| 6 | The approval step may be harder than rollback | Payments' manual card-network sign-off; requirements unknown `[ASSUMPTION]` | High | TPM + compliance counterpart |
| 7 | Key-person risk on legacy | Bartek is the only person who can debug the legacy plugins | High | Ines + Bartek |
| 8 | Red flags are being silenced | Two disk alerts muted; legacy instrumentation dismissed in the parking lot | Medium | Bartek / TPM |
| 9 | Satisfaction is measured only among people who already chose Runway | 4.1/5 "among Runway users"; non-users' view unknown | Medium | TPM |
| 10 | Interrupt load is eating capacity | "Too many" one-off tweak requests, not quantified | Medium | EM |

**Truth climate:**
- Mostly healthy. The retro names its own failures, and Ines invites debate instead of dictating.
- Charisma check: no sign that Ines suppresses bad news. She actively deflects credit.
- Gap: the red-flag mechanisms (alerts, legacy visibility) are being switched off rather than strengthened.

**Faith statement:** Runway already wins nearly every new service, cut commit-to-production from 58 to 41 minutes, and cut pages from 52 to 37. The team that did that can build the one thing its hardest customer has asked for in plain words.

## 7. Core ideology and the BHAG

- **Core purpose:** let Brightwater engineers change the systems that move people's money without fear.
- **Core values:**
  1. Every change is reversible.
  2. Earn adoption, don't mandate it.
  3. Pave the road; don't police it.
  4. Fix the signal; never mute it.
- **BHAG** (kept to one line, because this is a team inside a larger company): *By the end of Year 3, no Brightwater customer is locked out of their money by a deploy. Every money-moving service ships on Runway and rolls back in under five minutes.*

## 8. Scorecard

| Output | Current (Q3 Y0) | 12-month target | BHAG trajectory |
|---|---|---|---|
| Change-caused Sev-1/2 per quarter `[ASSUMPTION: all 6 were change-caused: config push, deploys, flag, migration, upgrade]` | 6 (2 Sev-1) | ≤ 2, zero Sev-1 `[ASSUMPTION]` | Zero change-caused Sev-1 |
| Rollback time, p90, on money-moving services | Legacy observed 22–47 min; Runway **unknown** | < 5 min for every migrated Payments service | < 5 min everywhere, mostly automatic |
| Money-moving services on Runway (the denominator) | ~0 `[ASSUMPTION]` | card-auth-gateway plus the other three Payments incident services, at least 4 `[ASSUMPTION]` | All of Payments and Lending |

Service-count percentage (64%) and median commit-to-production time (41 min) remain health metrics, not goals.

## 9. Next 90 days

| # | Action | Owner | Pushes link |
|---|---|---|---|
| 1 | Before the offsite, answer the VP: **"Yes to two heads, aimed at rollback + approval, with an end-of-quarter demo on card-auth-gateway. Atlas will be revisited once the first Payments service is live, or handed to another owner."** Frame it around the VP's own goal, fewer outages, and show the six-incident table. | Ines | 1, 5 |
| 2 | Demo sub-five-minute rollback on one real Runway service by week 4. Freeze new starters and template extras until then. | Sana (tech), Mei (delivery) | 1 |
| 3 | Get a written migration agreement with the Payments platform lead: named services, the definition of "rollback < 5 min," and approval-step requirements from compliance. card-auth-gateway is the pilot. | TPM + Ines | 1 → 2 |
| 4 | Write a debugging runbook for the legacy plugins and pair on it. Unmute the two disk alerts with a real fix. Join the Payments migration. | Bartek | 5 |
| 5 | Replace the 80% OKR with this scorecard. Pull legacy deploy and rollback timings from the incident tracker (no new pipeline instrumentation). Add a "pipeline" column to every Sev-1/2 review. Stand up the tweak-request queue. | TPM | 3, 4 |

## 10. Re-check

I can set up a scheduled task about 90 days out, at the end of Q4 Year 0. It would re-score this scorecard with real numbers and re-run Gates 1, 5 and 8. This session had no scheduling tool, so it hasn't been created yet.

## 11. Risk register

| Source | Risk | Condition / warning sign | Evidence that clears it |
|---|---|---|---|
| Gate 2 (COND) | Steward's resolve on the hardest work is unproven | Atlas decided by team excitement; rollback carried over a fourth time | Ines makes and owns the Atlas call, and rollback ships with capacity she defended |
| Gate 5 (COND) | Hedgehog unconfirmed: feasibility unknown, passion untested | No rollback spike; team votes for Atlas | Sub-five-minute demo, plus the team commits at the offsite |
| Gate 6 (COND) | Discipline track record is poor | Any stop-doing item restarts; the epic is carried over again | Two quarters with no carry-over and no restarts |
| Gate 8 (COND) | Payments' commitment is only verbal | "Once…" never turns into named services | Written agreement, and card-auth-gateway on Runway |
| Fact 6 | The approval step may be the real blocker | Compliance requirements still undefined by week 6 | Requirements in writing; minimal step piloted |
| Fact 7 | Bartek key-person risk | Bartek is still the only person who can debug the legacy plugins | Runbook done; second person resolves a legacy issue alone |
| Political | VP relationship strained by the counter-offer | Headcount withdrawn; Atlas imposed | VP accepts the reframed offer |
| Decline 1: Hubris | Celebrating count milestones ("200!") while Sev-1s happen on legacy | Retro leads with service counts, not incidents | Incidents-by-pipeline is the first slide |
| Decline 2: Undisciplined more | Atlas, more starters, more dashboards | Hedgehog epic loses capacity to new work | Protected capacity holds |
| Decline 3: Denial of risk | "Not our services"; muted alerts | Alerts muted without tickets; legacy incidents treated as someone else's | Pipeline column in every review |
| Decline 4: Grasping for salvation | If Payments stalls: push a mandate, reorg, or jump to a portal to stay relevant | Proposals for a mandate or a big new product | Payments migrates on merit |
| Decline 5: Capitulation | Payments builds its own rollback; Runway becomes "the pipeline for low-risk services" | Payments staffs its own pipeline project | Payments services on Runway |

**Shared root cause:** all four CONDITIONALs trace back to one pattern. The team's capacity follows what is exciting and countable, not its hardest customer's stated condition. Fixing the prioritization mechanism (actions 1, 2 and 5) addresses all four.

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing team, clear steward, multi-year horizon, metrics exist |
| 1 Baseline | PASS | Clearly good (64% adoption, 34/35 new services, 41 min, pages down); not yet great on the riskiest services |
| 2 Level 5 | CONDITIONAL | Humility evident; resolve on the hardest work unproven |
| 3 First Who | PASS | Right people; seats need moving; Payments partner and compliance seats missing |
| 4 Brutal Facts | PASS | Facts are on the table; red-flag mechanisms need repair |
| 5 Hedgehog | CONDITIONAL | Real intersection; feasibility and passion untested |
| 6 Discipline | CONDITIONAL | Stop-doing list is clear; three-quarter slip record |
| 7 Technology | PASS | Rollback and the approval step are pioneer candidates; Atlas is hype-adjacent |
| 8 Flywheel | CONDITIONAL | Loop closes; first link unbuilt; Payments' commitment verbal |
| 9 Built to Last | PASS | Ideology and mechanisms drafted |
| 10 Mighty Fall | PASS | Decline risks mapped with warning signs |

Tally from the table: 7 PASS, 4 CONDITIONAL, 0 FAIL. Fewer than half are CONDITIONAL, and the four share the single root cause named in the risk register.

---

## Appendix: gate artifacts not shown above

**Gate 0, subject card**

| Field | Value |
|---|---|
| Name | Delivery Platform team (Runway) |
| Type | Team / org unit |
| Steward | Ines (EM). The VP of Engineering controls headcount. |
| Team | 10 engineers + EM + TPM |
| Age | 3 years |
| Horizon | Multi-year |
| Stage | Good and scaling; adoption plateau on critical services |

**Gate 1, baseline sheet**
- **Evidence of good:**
  - 212 of 331 services on Runway (64%, up from 57%).
  - 34 of 35 new services started on Runway.
  - Median commit-to-production 41 min, down from 58.
  - Satisfaction 4.1/5 among Runway users.
  - Pages down from 52 to 37.
  - Template v3 early; secret migration with zero incidents.
- **Definition of great:**
  1. **Superior performance:** the fastest *and* safest way to change any service, including the riskiest.
  2. **Distinctive impact:** if Runway vanished, money-moving services would lose their fast recovery and their audit trail. That is not true today, because they don't depend on it.
  3. **Endurance:** works without Bartek, Ines or any hero.
- **Scorecard outputs:** see section 8.

**Gate 2, leadership read (Ines)**
- **Strengths:** window-and-mirror humility. She asked to be taken off the hero slide in favor of the template v3 crew. She invites debate.
- **Gaps:** nothing shows her taking personal ownership of the three-quarter slip. Leaving the Atlas decision to a team vote, under a VP deadline, risks letting enthusiasm decide the hedgehog.
- **Succession:** no evidence either way `[ASSUMPTION]`.
- **One behavior change:** at the offsite, open with "rollback slipped three times on my watch." Then lead with questions, such as "Which of our six incidents would Atlas have prevented?", and make the call herself if the team splits.

**Gate 6, framework**
- **Framework:**
  - Every service ships via the Runway golden path.
  - Rollback and approval are non-negotiable for money-moving services.
  - The hedgehog epic gets protected capacity: at least half the team until the Payments pilot is live `[ASSUMPTION]`.
- **Freedom:** product teams choose templates and extend through documented extension points. Engineers choose how to build inside the epic.
- **Non-negotiable disciplines:**
  - Every Runway service's rollback is tested regularly.
  - No alert is muted without a fix ticket and an owner.
  - The hedgehog epic is never carried over without an explicit scope cut made by Ines.
  - Incidents are reviewed by pipeline every quarter.
- **Bureaucracy check:** Payments' manual sign-off is a compliance requirement, not a crutch, so build it in rather than fight it. Inside the team, the "re-estimate" ritual stands in for a decision. Retire it.

**Gate 7, tech triage**

| Technology | Class |
|---|---|
| Progressive rollout | Accelerates |
| Fast rollback | **Accelerates; pioneer candidate.** Auto-rollback on health signals. |
| Approval step with automatically captured audit evidence | **Accelerates; pioneer candidate** `[ASSUMPTION about audit needs]` |
| Feature flags | Accelerates. Note the Growth flag misfire: flag rollback needs the same rigor. |
| Template v3, Kotlin starter, secret manager | Parity: maintain |
| Build-cache dashboard | Neutral: keep, don't grow |
| Disk-alert fix | Parity: do it |
| Legacy-pipeline instrumentation | Partial. Measure via the incident tracker only. |
| Legacy plugins | Drop over time |
| Atlas portal | Irrelevant to the hedgehog now. Adoption would be visibility-driven. |

**Gate 9, clock-building mechanisms**
- The rollback SLO acts as a release gate for money-moving services.
- Protected-capacity rule for the hedgehog epic.
- Pipeline column in every Sev-1/2 review.
- Legacy runbooks, so knowledge isn't held by one person.
- Quarterly scorecard re-score.