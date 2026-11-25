# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict

**Hedgehog:** *"We make every production change at Brightwater safe to ship and fast to undo, starting with the services that move money."*

**Weakest flywheel link:** shipping rollback in under 5 minutes plus Payments' change-approval step. It has slipped three quarters running, and it gates the riskiest services' move to Runway.

**Top 3 stop-doing:**
1. Owning Atlas now. Ask the VP to put the 2 headcount on rollback instead.
2. New template or language features until rollback ships.
3. "80% of services" as the headline OKR.

**Most urgent brutal fact:** 5 of 6 Sev-1/2 incidents this quarter, including both Sev-1s, came through legacy pipelines. Four of them were in Payments, which won't move to Runway until rollback ships.

**Missing numbers that would change the answer:** deploys and incident rate split by pipeline; Runway's current rollback time; how many services Payments owns; whether Payments' commitment holds up in writing.

**Confidence:** moderate. It rests on one quarter of incident data and Payments' stated conditions.

Greatness potential: 58/100

---

## 1. The great version in one paragraph

At its great version, Runway is how Brightwater changes production, and above all how it changes the systems that move customers' money. A bad deploy to card-auth-gateway rolls back in under five minutes, often automatically. Payments' card-network compliance sign-off is built into the pipeline as an audited approval step, so nobody has to work around it. Every Sev-1/2 is tagged by pipeline and cause, so the safety case is measured rather than asserted. Legacy pipelines are being retired, and the knowledge of how they work no longer lives in one person's head. The team earns its headcount by reducing the cost and frequency of change-caused incidents, not by launching visible new products. If Runway disappeared, the hole would show up in Brightwater's incident reviews and its compliance audits, not only in developer convenience.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):** *We make every production change at Brightwater safe to ship and fast to undo, starting with the services that move money.*

| Circle | Candidates considered | Kept | Ruled out (can't be best at) |
|---|---|---|---|
| **Best in the world at** (world = Brightwater) | Paved road for new services; safe, audited change for regulated money flows; developer portal; language starters | **Safe, reversible, auditable change to production.** It is already the default for new services (34 of 35), and only this team can build it. | Developer portal or discovery (no evidence of edge; anyone could build it); maintaining per-org legacy pipelines; one-off customizations |
| **Resource engine** (budget and headcount leverage) | Services on Runway; deploys per engineer; incidents avoided | **Trust and funding earned by reducing the cost of change-caused incidents in money-moving systems** | Headcount earned through visibility (Atlas). It works once, then has to be fed again. |
| **Passion** | Greenfield launches; craft; being "the standard" | **Shipping things engineers actually use, and being the real standard.** This is supported by the pride in template v3, the zero-incident secret migration, and the two people who defended rollback. | Not, honestly, compliance plumbing for its own sake. See the tension below. |

**Denominator:** *share of Tier-1 (money-moving) production deploys that go through Runway*, checked against *change-caused Sev-1/2 incidents per 1,000 deploys*. `[ASSUMPTION]` Both are currently unmeasurable, because legacy pipelines are not instrumented.

**Tests:**
- **Does it explain past wins?** Yes. New-service adoption, lead time cut from 58 to 41 minutes, and the zero-incident secret migration.
- **Does it rule things out?** Yes. Atlas, one-off tweaks, more language starters, and acting as the support desk for legacy plugins.
- **Is it uncomfortable to commit to?** Yes. It means turning down two headcount and an idea most of the team is excited about.

**Passion tension, stated plainly:** most of the team's energy goes to greenfield work. The plan therefore runs rollback and Payments onboarding as a real launch, with a launch lead, a named pilot, and a public ship date, instead of treating it as maintenance. `[ASSUMPTION]` Framed that way, it will draw the same energy as template v3.

**Evidence that would confirm the hedgehog:**
- Payments names a pilot service and the conditions in writing.
- One or two more quarters of incident data, with deploy counts by pipeline, still show legacy changes causing a disproportionate share of Sev-1/2s per deploy.

## 3. The flywheel

```
   ┌─► 1. Ship safety features critical services require
   │      (<5-min rollback, approval-as-code, migration guardrails)
   │                      │
   │                      ▼
   │   2. Tier-1 / Payments services migrate to Runway
   │                      │
   │                      ▼
   │   3. More production change flows through one
   │      instrumented pipeline  ← DENOMINATOR rises
   │                      │
   │                      ▼
   │   4. Fewer and shorter change-caused Sev-1/2s, measured by pipeline
   │                      │
   │                      ▼
   │   5. Credible safety case → exec trust, headcount,
   │      and a mandate to retire legacy pipelines
   │                      │
   │                      ▼
   └── 6. Capacity freed from legacy support and interrupts
```

**Current push (next one or two turns):**
- **Link 1:** ship rollback for one pilot service, and co-design the change-approval step with Payments.
- **Link 4, in parallel:** instrument legacy deploy events, so that the "before" picture exists before migration starts.

**Weakest link:** link 1. The team has never pushed it. It has been "re-estimated" three times. Link 2 is unverified until Payments commits.

**Doom-loop check: medium risk.** Signs present:
- Direction keeps moving to the newest visible project (template v3, then Kotlin, now Atlas).
- Re-estimating has replaced doing.
- Atlas is a large program offered to create visibility and momentum.

Signs absent: no reactive reorganization, and no lurching between strategies.

## 4. The bus

| Person / commitment | Call | Note |
|---|---|---|
| **Ines (EM)** | Keep | Strong humility (asked to be taken off the hero slide; credits the crew). Needs to show more resolve. See leadership read in the appendix. |
| **Mei** | Move seat → launch lead for rollback and the Payments pilot | Proven: template v3 shipped two weeks early. Put the best people on the biggest opportunity. |
| **Sana** | Keep, with the epic finally staffed | Has owned an epic that was repeatedly starved of capacity. Give her a squad, not another re-estimate. `[ASSUMPTION]` The slip came from prioritization, not from her. |
| **Bartek** | Move seat → Payments migration engineer and legacy-knowledge transfer | The only person who can debug legacy plugins. That makes him a single point of failure, and also exactly the expertise migration needs. Move him from firefighting to retiring the legacy pipelines. Fix the disk alerts properly; don't mute them. |
| **Ravi** | Keep; pause the gRPC example | Move to the rollback squad or the approval step `[ASSUMPTION]`. The gRPC example could be contributed by a user team instead. |
| **TPM** | Keep → owns instrumentation and the incident-tagging mechanism | |
| **Tomasz** | Keep | On leave. Seat to be decided on return. |
| One-off pipeline tweak requests | **Off the bus** (as an ad-hoc commitment) | Replace with a weekly front-door triage and a supported extension point. |
| Unofficial legacy-plugin support for Payments | **Off the bus** (time-boxed, then converted into migration work) | |
| Intern's build-cache dashboard | Keep, *with a named owner* | "Keep it" without an owner is a new commitment quietly taking up capacity. |
| **Missing: Payments liaison** with compliance and change-approval knowledge | Missing seat | Embedded part-time from Payments `[ASSUMPTION]`. |
| **Missing: an Atlas owner, if Atlas happens later** | Missing seat (outside this team) | Atlas needs its own lead, not this team's spare cycles. |

## 5. Stop-doing list

1. **Taking on ownership of Atlas now.** Counter-offer: put the two headcount on rollback and the approval step, and provide Runway's service and owner metadata as a data feed for whoever builds a catalog later. If the headcount comes only with Atlas, decline it this cycle. A portal can be built by others; Brightwater's deploy-safety layer can only be built by this team. Note also that template discovery is not Runway's bottleneck: 34 of 35 new services already chose it.
2. **Starting new template or language-starter features** (including the Kotlin gRPC example) until rollback is in production for a pilot service.
3. **"80% of services on Runway" as the headline OKR.** It would need about 53 more services in one quarter, more than twice last quarter's net gain of 25, and it could be met without moving a single Payments service.
4. **Accepting one-off pipeline tweaks as interrupts.** Route them through a weekly front door. Fold the recurring ones into an extension point, and make Payments' approval step its first client. `[ASSUMPTION]` Many of these tweaks follow the same pattern.
5. **Carrying rollback as "re-estimate."** It either ships, or the team holds a blameless autopsy on why not.
6. **Muting alerts as a fix.** Muted alerts are silenced red flags.
7. **"Not our services, not our budget"** as the reason not to measure legacy pipelines. Collecting deploy events is cheap, and it is the evidence that funds the flywheel.

**Non-negotiable disciplines:**
- Rollback-first work-in-progress rule: no new feature epic starts while rollback is open.
- Every Sev-1/2 on any pipeline is tagged with pipeline, cause, and time to recover, and with whether Runway would have prevented or shortened it.
- Any new commitment names the commitment it replaces.

**Framework boundaries:** inside the hedgehog, engineers choose the design and implementation. Anything outside it needs an explicit stop-doing trade agreed at planning. Payments' manual sign-off is compliance, not bureaucracy: Runway encodes it and does not route around it.

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Change-caused Sev-1/2s are concentrated in legacy pipelines and in Payments | 5 of 6 incidents legacy, both Sev-1s; 4 of 6 Payments; card-auth-gateway hit twice | Critical | Ines |
| 2 | The blocker named by the highest-risk customer has slipped three quarters running behind visible work | Retro "didn't go well"; action item carried over for the third time | Critical | Ines + Sana |
| 3 | Adoption growth comes from new services defaulting to Runway; migration of existing services has stalled | Runway net +25 against 34 new services started on it, so existing services netted −9 (retirements and migrations combined; split not given) | High | TPM |
| 4 | Rollback time on legacy is measured in tens of minutes on the card authorization path | 47 min and 22 min to roll back card-auth-gateway | High | Payments + team |
| 5 | Fast rollback is necessary but not sufficient | Schema migration, dependency upgrade and config push incidents can't simply be rolled back. Runway also had its own feature-flag misfire. | Medium | Team |
| 6 | The team can't prove its own safety case | Legacy pipelines uninstrumented; deploys not split by pipeline | High | TPM |
| 7 | Satisfaction is measured only among people who already use Runway | 4.1/5 "among Runway users"; non-users' view unknown | Medium | TPM |
| 8 | Single point of failure on legacy knowledge, and alerts silenced | Bartek "the only person"; two alerts muted | Medium | Bartek |
| 9 | Headcount is currently offered for visibility, not for risk reduction | Atlas offer | Medium | Ines |

**Truth climate:**
- **Good:** candid retro, dissent voiced, and the EM deliberately invites debate.
- **Weak:** no autopsy of the three slips, alerts muted, and measurement dismissed in the parking lot.

**Charisma check:** the risk here is not that Ines's force of personality is suppressing bad news. It is that majority enthusiasm for Atlas drowns out the two people who raised rollback.

**Faith statement:** Runway already wins wherever it is the default. Once it is the safest way to touch money-moving systems, it becomes the standard for all of them.

## 7. Core ideology and BHAG

**Core values:**
- Production safety before feature novelty.
- Earn adoption by being better, not by mandate.
- Measure what we claim.
- Credit the crew, own the misses.

**Core purpose:** let every Brightwater engineer change production without fear.

**BHAG** (team-scale; 3-year horizon, shortened from Collins's 10–30 years because this is a team): *By Year 3, no money-moving change at Brightwater ships outside Runway, and no change-caused Sev-1 takes more than five minutes to undo.*

**Clock-building mechanisms:**
- A rollback SLO enforced in Runway.
- Approval-as-code with an audit trail.
- Incident tagging by pipeline.
- Runbooks for the legacy plugins.
- A rotating front-door duty.
- A rollback drill before each Tier-1 migration.

## 8. Scorecard

| Output | Current (end of Q3, Year 0) | 12-month target | BHAG trajectory (Year 3) |
|---|---|---|---|
| p90 time to roll back a bad Tier-1 deploy | Unknown for Runway; legacy observed at 47 and 22 min | < 5 min on Runway pilot services `[ASSUMPTION: Payments' stated bar]` | < 5 min, automated, on every Tier-1 service |
| Payments / Tier-1 services on Runway | Not reported; Payments implied near 0 `[ASSUMPTION]` | Payments card path, including card-auth-gateway, on Runway `[ASSUMPTION]` | 100% of money-moving services |
| Change-caused Sev-1/2 per quarter (per 1,000 deploys once instrumented) | 6 (5 legacy, 1 Runway); rate unknown | ≤ 3 per quarter, none > 5 min to recover `[ASSUMPTION]` | Rate trending down every year |
| *Secondary:* services on Runway; median commit-to-production time | 64% (212/331); 41 min | Track only, not headline | — |

## 9. Next 90 days (Q4)

1. **Before the offsite, take the counter-proposal to the VP.** Show the incident table, decline Atlas ownership for now, and ask for the two headcount to go to rollback and the approval step. Offer Runway's owner metadata to any future catalog. *Owner: Ines.*
2. **Make rollback the Q4 #1 objective, as a launch.** A dedicated squad, a work-in-progress freeze on new features, and a public ship date for one pilot service. *Owners: Sana (epic), Mei (launch lead).*
3. **Co-design the change-approval step with Payments.** Get the Payments platform lead to name a lower-risk pilot service and confirm the migration conditions in writing. Build the step as a general extension point. *Owners: TPM + Bartek.*
4. **Instrument and tag.** Collect deploy events from legacy pipelines, tag every Sev-1/2 by pipeline and cause, fix the disk alerts, and write the legacy-plugin runbooks. *Owners: TPM (instrumentation and tagging); Bartek (alerts and runbooks).*
5. **Rewrite the Q4 OKRs** around rollback time, the Payments pilot, and incident rate. Set up the weekly front door for tweak requests. *Owners: Ines + TPM.*

## 10. Re-check

Offer: a scheduled re-check about 90 days out, at the end of Q4 of Year 0. It would re-score this scorecard with real numbers (rollback p90, Payments services on Runway, incidents by pipeline) and re-run Gates 1, 5 and 8. This session can't create scheduled tasks, so confirm if you want one set up.

## 11. Risk register

| Risk | Source | Early warning | Trigger / threshold → action |
|---|---|---|---|
| **Undisciplined pursuit of more** (Atlas, new starters) | Gate 10, stage 2 | Any new epic starts while rollback is open | Rollback not live on a pilot service by the end of Q1, Year 1 → freeze all new feature work and hold a blameless autopsy |
| **Denial of risk: vanity adoption metric** | Gate 10, stage 3 | Service % rises while the Payments count on Runway stays flat | A quarter with zero Payments migrations → OKR review leads with Tier-1 coverage |
| **Grasping: rushed Payments migration** | Gate 10, stage 4 | Migration scheduled without a rollback drill | Any Runway-caused Sev-1 on a Tier-1 service → pause migrations and run an autopsy before resuming |
| **Hubris: mistaking default adoption for trust** | Gate 10, stage 1 | "34 of 35" cited as proof of success | Payments or other critical-path teams still decline Runway → treat as the real verdict |
| **Bus factor on legacy knowledge** | Gate 3 / 10 | Legacy questions still routed only to Bartek | No runbook by end of Q4 → pair-rotation becomes mandatory |
| **CONDITIONAL (Gate 2): leadership resolve** | Gate 2 | Atlas decided by enthusiasm vote; rollback slips a fourth time | PASS when Ines states and owns a rollback-first call and rollback ships |
| **CONDITIONAL (Gate 5): hedgehog unconfirmed** | Gate 5 | Payments adds new conditions after rollback ships | PASS when Payments names a pilot in writing and instrumented data confirms legacy carries a disproportionate share of incident risk |
| **Capitulation** (stage 5) | Gate 10 | Team drifts toward being an internal tools shop for whatever is fashionable | Annual check: does the hedgehog still decide the roadmap? |

## 12. Gate log

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing internal platform team with a steward, a multi-year horizon, and metrics |
| 1 Baseline | PASS | Good, not yet great: strong default adoption, but the highest-risk services sit outside Runway |
| 2 Level 5 | CONDITIONAL | Humility clearly present; resolve not yet shown on rollback |
| 3 First Who | PASS | No misaligned key seat; move Mei and Bartek to the biggest opportunity; Payments liaison missing |
| 4 Brutal facts | PASS | Incidents concentrate in legacy Payments; consistent with the Gate 1 baseline |
| 5 Hedgehog | CONDITIONAL | Safe, reversible change for money-moving services; needs Payments' commitment and incident data |
| 6 Discipline | PASS | Seven stop-doing items, led by Atlas |
| 7 Technology | PASS | Auto-rollback and approval-as-code accelerate the hedgehog; the portal does not |
| 8 Flywheel | PASS | Loop closes; weakest link is shipping rollback |
| 9 Built to Last | PASS | 3-year team BHAG (shortened); mechanisms listed |
| 10 Mighty Fall | PASS | Top risks: Atlas-style "more" and a vanity adoption metric |

Tally from the table: 9 PASS, 2 CONDITIONAL, 0 FAIL.

**Evidence note:** this session had no memory, past chats, or web search, so there was no prior run to use as a baseline and no outside research. The evidence-question batch was skipped (autonomous mode). The dossier is the only evidence.

---

### Appendix: gate artifacts not covered above

**Subject card (Gate 0)**
- **Name:** Delivery Platform team / Runway.
- **Type:** team or org unit.
- **Steward:** Ines (EM).
- **Horizon:** multi-year.
- **Stage:** three years old, majority adoption.

**Baseline sheet (Gate 1)**
- **Evidence of good:**
  - 64% of services on Runway (up from 57% last quarter).
  - 34 of 35 new services started on Runway.
  - Median commit-to-production time 41 min (down from 58).
  - Satisfaction 4.1/5 among Runway users.
  - On-call pages down from 52 to 37.
- **Great means indispensable output**, judged on the three tests:
  - **Superior performance:** safe, fast change.
  - **Distinctive impact:** if Runway vanished, money-moving systems would become riskier. Today the hole would mostly be felt by newer, less critical services.
  - **Endurance:** survives beyond Bartek and Ines.
- **State:** good, not yet great.

**Leadership read (Gate 2)**
- **Strengths:** looks out the window (credits the crew, asked to come off the hero slide); invites debate; runs a candid retro.
- **Gaps:** rollback slipped three times with no visible look in the mirror; the Atlas call has been handed to a team where most people are excited; "not our budget" was accepted without challenge.
- **One behavior change:** at the planning meeting, Ines states her own rollback-first recommendation with the incident table, invites the team to attack it, then decides and personally owns the outcome.

**Tech triage (Gate 7)**

| Technology | Class | Note |
|---|---|---|
| Automated rollback on health signals | Accelerates | Pioneer candidate |
| Approval-as-code with audit trail for card-network compliance | Accelerates | Pioneer candidate |
| Progressive rollout and feature flags | Accelerates | Add guardrails after the notifications misfire |
| Legacy deploy-event instrumentation | Accelerates | Cheap; builds the safety case |
| Expand/contract schema-migration guardrails | Accelerates | Later push |
| Templates v3, Kotlin starter | Parity | Maintain only |
| Build-cache dashboard | Neutral | Keep, with an owner |
| Developer portal (Atlas) | Irrelevant to the hedgehog now | Hype flag: adoption prompted by a single peer-company visit |