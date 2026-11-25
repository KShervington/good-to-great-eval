# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict

**Good, not yet great. Runway has won the easy half of Brightwater, but not the half where the risk lives.**

- **Hedgehog Concept:** Runway makes changing production at Brightwater safe, fast and reversible in minutes, starting with the services that move money.
- **Weakest flywheel link:** there is no rollback under 5 minutes, so Payments won't migrate, so the riskiest services stay on legacy pipelines.
- **Top three stop-doing:** (1) owning Atlas in Q4; (2) new starters and template features ahead of rollback; (3) one-off pipeline tweaks on request.
- **Most urgent brutal fact:** 5 of 6 Sev-1/2 incidents were on legacy pipelines, and both Sev-1s were in Payments. The one fix Payments asked for has slipped three quarters running.
- **Numbers that would change this:** deploys per pipeline, the count of money-moving services and how many are already on Runway, and Runway's current rollback time.

Greatness potential: 55/100

---

## 1. The great version in one paragraph

In its great version, Runway is how every Brightwater service changes production, and that includes card-auth-gateway, payouts-scheduler and ledger-recon. Any bad deploy can be undone in under five minutes. The card-network change-approval step is built into the pipeline as an auditable gate, so it is no longer a reason to stay on legacy. Change-caused Sev-1 incidents become rare and short. The legacy pipelines are retired, so nobody depends on one person to debug their plugins. Leadership funds the team because it carries most of the company's production-change risk, not because it ships visible new products. Being "great" for this team means **indispensable output**: if Runway disappeared, Brightwater would lose its ability to ship to money-moving systems safely.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):** *Runway makes changing production at Brightwater safe, fast and reversible in minutes, starting with the services that move money.*

| Circle | Candidates considered | Kept | Ruled out |
|---|---|---|---|
| **Best in the world at** (narrow world: Brightwater) | Golden-path templates; safe, auditable, fast-reversible deploys for regulated services; developer portal; maintaining legacy pipelines | **Safe, reversible, auditable change for money-moving services.** Templates are already won (34 of 35 new services chose Runway). | **Developer portal.** No evidence the team is uniquely placed, and off-the-shelf options exist `[ASSUMPTION: not researched this session]`. **Legacy plugin maintenance** and **bespoke one-off pipelines** also ruled out. |
| **Resource engine** (budget and headcount leverage) | Service count on Runway; deploys per quarter; survey score; risk carried | **Leadership trust and mandate earned by owning the risky changes.** Headcount follows that. | Unweighted service count. It can rise without touching the risk. |
| **Passion** | Greenfield launches; developer experience; reliability craft | **Developer experience where "fast" includes "fast to undo."** Two members already pushed for rollback. | Greenfield work as a goal in itself. This is the Atlas pull. |

**Denominator:** *production-change risk retired per tier-1 (money-moving) service on Runway.* Track it as tier-1 services on Runway together with change-caused Sev-1/2 per quarter.

**Why this one:**
- It explains past wins. New services pick Runway because it is the fastest and safest path, and commit-to-production time fell from 58 to 41 minutes.
- It rules things out: Atlas, more language starters, and one-off tweaks.
- It is uncomfortable. It means telling a VP no to two headcount, and doing compliance plumbing instead of greenfield work.

**Confirmation tests (by the end of Q2 Year 1):**
- Rollback under 5 minutes ships.
- The Payments platform lead accepts the approval gate design.
- card-auth-gateway deploys on Runway.
- Change-caused Sev-1/2 incidents fall per quarter.

If Payments still doesn't move after both of its conditions are met, the hedgehog is wrong. Revisit Gate 5.

## 3. The flywheel

```
 ┌─► 1. Fast, reversible, auditable deploys
 │      (rollback < 5 min + built-in approval gate)
 │                     │
 │                     ▼
 │   2. Money-moving (tier-1) services migrate  ◄── WEAKEST LINK (blocked)
 │                     │
 │                     ▼
 │   3. Fewer, shorter change-caused Sev-1/2s
 │      [denominator: risk retired per tier-1 service]
 │                     │
 │                     ▼
 │   4. Trust from engineers + leadership
 │      (mandate to sunset legacy, funding)
 │                     │
 │                     ▼
 │   5. Legacy retired → fewer interrupts,
 │      key-person load lifted
 │                     │
 └──── 6. Capacity reinvested in guardrails ◄┘
```

New services defaulting to Runway feed step 2 from the side. That source is already running well.

**Current push (next one or two turns):**
1. Ship rollback under 5 minutes on Runway.
2. Co-design the change-approval gate with the Payments platform lead and compliance, then migrate **card-auth-gateway** as the lighthouse. It had two bad deploys this quarter, with rollbacks of 47 and 22 minutes.

**Doom-loop check:** this is not yet a doom loop, but three early signs are present.
- **Visible demand keeps beating the blocker.** Template v3 and the Kotlin starter were both prioritized over rollback.
- **A new direction is on offer.** Atlas would be a big new program that jump-starts headcount, not momentum.
- **The draft OKR chases an unweighted number.** "80% of services" means 265 of 331, or +53. That can be reached mostly through new services and legacy retirements without moving one Payments service.

## 4. The bus

| Person / commitment | Call | Why |
|---|---|---|
| Ines (EM) | **Keep** | Strong Level 5 humility signals (details below). |
| Mei | **Keep, move seat → rollback + Payments migration** | She ran the template v3 launch. Put the best executor on the biggest opportunity, not on the next template. |
| Sana | **Keep, give the rollback epic protected capacity** | The carry-overs look like a capacity and priority failure, not a person failure `[ASSUMPTION]`. Pair Sana with Mei, and put nothing above the epic. |
| Bartek | **Keep, change seat: legacy knowledge → migration runbook** | He is a single point of failure on the legacy plugins. Pair him with a second engineer, and turn what he knows into migration tooling instead of ad hoc rescues. |
| Ravi | **Keep** | Park the Kotlin gRPC example until rollback ships, unless it takes under a day. |
| Tomasz (on leave) | **Keep** | Unknown seat `[ASSUMPTION]`. Consider him for the approval-gate work when he returns. |
| TPM | **Keep, move seat → Payments and compliance liaison** | The approval gate is mostly a cross-org design and audit-evidence problem. |
| Payments platform lead | **On the bus as the key partner** | They have stated their entry conditions. Treat them as co-owner of the gate design. |
| Intern build-cache dashboard | **Keep as-is, don't grow** | It serves commit-to-production speed but is not a roadmap item. |
| One-off pipeline tweak requests | **Off** | Replace with weekly office hours and a self-service extension point. |
| Atlas as a team-owned product | **Off (for now)** | Outside the hedgehog. See §5. |
| **Missing seat:** compliance-fluent engineer or partner | **Fill** | Someone who knows the card-network audit evidence requirements. It could be borrowed from Payments. |
| **Missing seat:** second legacy-plugin debugger | **Fill internally** | Removes the Bartek dependency. |

**Leadership read (Ines).**
- **Strengths:**
  - She looks out the window when things go well: she asked to be replaced on the hero slide by the template v3 crew.
  - She leads with questions, as with the Atlas decision going to the team.
  - Her kudos credit others.
- **Gap:** resolve. The epic that unlocks the highest-risk services has slipped three quarters under her watch, and the Atlas decision is heading toward consensus among people excited by greenfield work.
- **One behavior change:** name rollback and the approval gate as Q4's only top priority, and protect it in writing. Any item carried over twice goes to her and the VP, not back into the backlog.

## 5. Stop-doing list

1. **Don't own Atlas in Q4.** The pain is real (58% say finding owners and docs is hard), but it isn't this team's hedgehog.
   - Tell the VP so, and make a counter-offer: Runway will publish owner and docs metadata from every template, so a catalog can be built or bought cheaply later.
   - Ask whether the two headcount can go toward the Payments migration instead. If it is Atlas or nothing, decline anyway.
2. **No new language starters or template features until rollback ships.** Small bug fixes are fine.
3. **No one-off pipeline tweaks on request.** Route them to office hours. Recurring asks become features only if they serve the hedgehog.
4. **No ad hoc legacy plugin rescues by one person.** Time-box them, pair on them, and turn each one into a migration step.
5. **Stop measuring success by unweighted service count.** Replace the 80% OKR with tier-1 coverage and change-caused incident metrics.
6. **Stop muting alerts as a fix.** A mute needs a ticket and an expiry date. Fix the build-cluster disk alerts properly.
7. **Stop carrying epics over silently.** A third carry-over is not allowed without escalation.

**Non-negotiable disciplines:**
- Every Runway deploy is reversible.
- Hold a rollback drill monthly on a tier-1 service.
- Every Sev-1/2 is tagged with its pipeline and time-to-rollback.
- Rollback is the top item in every planning meeting until it is done.

**Freedom within the framework:** engineers choose the design and implementation freely. The fixed parts are the priority order (rollback → approval gate → tier-1 migrations → everything else) and the definition of done (proven on a real Payments service).

**Bureaucracy check:**
- The Payments manual sign-off is a real compliance need, not bureaucracy. Encode it in the pipeline; don't fight it.
- The flood of tweak requests points to missing self-service, not missing process.

## 6. Brutal facts and the faith statement

*Note: web research for market or peer facts wasn't available in this session. Everything below comes from the dossier.*

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The fix that unlocks Payments has slipped three quarters running. | Retro: rollback epic carried over a third time, deprioritized behind v3 and Kotlin. | **Critical** | Ines |
| 2 | The services that most need Runway aren't on it. | 5 of 6 Sev-1/2 on legacy pipelines. 4 of 6 and both Sev-1s in Payments. card-auth-gateway rollbacks took 47 and 22 min. | **Critical** | Ines + Payments lead |
| 3 | All six incidents were caused by changes (config, deploy, migration, flag, dependency), which is squarely the platform's domain. | Incident table. | High | Team |
| 4 | Adoption growth comes mostly from new services, not migrations. | Runway gained a net 25 while 34 new services started on it. The total rose by only 5 despite 35 new services, so about 30 were retired. Migrations and retirements of legacy services can't be separated. | High | TPM |
| 5 | The draft 80% OKR can be met without reducing the main risk. | 265 of 331 needed. Nothing ties it to tier-1 services. | High | Ines + TPM |
| 6 | "Runway is safer" is suggestive, not proven. | 1 incident on Runway versus 5 on legacy, but there are no deploy counts per pipeline, and Runway also had a flag misfire. | Medium | TPM |
| 7 | Legacy pipelines are blind spots. | Not instrumented, and the parking lot says "not our budget." | Medium | TPM |
| 8 | Key-person risk. | Bartek is the only person who can debug the legacy plugins. | Medium | Ines |
| 9 | The satisfaction score covers users only. | 4.1/5 is "among Runway users," so non-adopters weren't measured. | Low | TPM |
| 10 | Red-flag mechanisms are being switched off. | Disk alerts muted. Rollback carried over with no escalation. | Medium | Bartek / Ines |

**Truth climate:** good inside the team. The retro is candid and dissent about Atlas was voiced. Two weaknesses:
- **Missing red flag.** Nothing forces a stalled critical item into the open.
- **Charisma check.** The pressure doesn't come from Ines. It comes from above: the VP is offering headcount and wants an answer before the offsite.

**Faith statement:** Runway already wins wherever it's adopted, and Payments has told us exactly what it would take to get on board. We prevail by building that, before anything else.

## 7. Core ideology and the BHAG

- **Core values:**
  - Reversible by default.
  - Customers' money is never the experiment.
  - Boring is a feature.
  - A paved road, not a mandate.
  - Write it down so it doesn't live in one head.
- **Core purpose:** let every Brightwater engineer change production quickly without putting customers at risk.
- **BHAG (one line; a team's horizon is shorter than a company's):** *No Brightwater customer is ever harmed by a deploy that couldn't be undone in minutes.*
- **Clock-building mechanisms:**
  - Monthly rollback drills.
  - A pipeline and time-to-rollback field on every incident.
  - Two owners for every critical component.
  - An escalation rule for any item carried over twice.
  - A migration runbook instead of hero debugging.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| Change-caused Sev-1/2 per quarter | 6 (5 legacy; 2 Sev-1) | ≤ 2, with 0 Sev-1 `[ASSUMPTION: target]` | Change-caused Sev-1 is a rare, short event |
| Time to roll back a tier-1 service (p90) | 22–47 min observed (legacy). Runway's figure is unknown; the epic implies > 5 min. | < 5 min on Runway for all tier-1 services | < 2 min, triggered automatically |
| Tier-1 (money-moving) services on Runway | **Unknown.** Likely few Payments services `[ASSUMPTION]`. | card-auth-gateway, payouts-scheduler, ledger-recon and loan-disbursement migrated, and ≥ 75% of tier-1 overall `[ASSUMPTION: target]` | 100%, with legacy pipelines retired |

Secondary health checks:
- Overall adoption (64%) and median commit-to-production (41 min) stay as guardrails, not goals.
- Survey satisfaction should also cover non-users.

## 9. Next 90 days

| # | Action | Owner |
|---|---|---|
| 1 | Before the offsite, answer the VP: decline Atlas ownership for now. Offer Runway owner and docs metadata. Ask to redirect the headcount to the Payments migration. | Ines |
| 2 | Replace the "80% of services" OKR with: rollback < 5 min p90 on Runway; approval gate signed off by Payments; card-auth-gateway on Runway; change-caused Sev-1/2 ≤ 3 in Q4. | Ines + TPM |
| 3 | Ship the rollback epic with protected capacity, nothing above it, and weekly demos. | Sana (lead) + Mei |
| 4 | Co-design the change-approval gate with the Payments platform lead and compliance, including the audit evidence trail. | TPM + one engineer (Tomasz on return, `[ASSUMPTION]`) |
| 5 | Pair on the legacy plugins, write the Payments migration runbook, and properly fix and unmute the disk alerts. Add pipeline and time-to-rollback fields to the incident tracker, and pull deploy counts per pipeline. | Bartek + one engineer; TPM for the tracker |

## 10. Re-check

Would you like a scheduled task at the end of Q4 Year 0, about 90 days from now? It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8. The key test is whether Payments moved once rollback and the approval gate existed.

## 11. Risk register

| Source | Risk | Early warning | Mitigation |
|---|---|---|---|
| Gate 2 (CONDITIONAL) | Resolve gap: the critical blocker keeps losing to visible work. | Rollback isn't demoable by mid-Q4. | **Turns PASS when** rollback < 5 min ships in Q4. |
| Gate 3 (CONDITIONAL) | Bartek is a single point of failure, and the compliance-fluent seat is missing. | Payments escalations still route only to Bartek. | **Turns PASS when** a second engineer has handled a legacy plugin issue solo and a compliance partner is named. |
| Gate 5 (CONDITIONAL) | The hedgehog is unconfirmed: the passion circle is uncertain (the team leans toward greenfield) and the tier-1 count is unknown. | The team votes for Atlas, or tier-1 coverage can't be measured. | **Turns PASS when** the team commits at planning and the tier-1 list and its coverage are produced. |
| Political | The VP insists on Atlas or no headcount. | Headcount is framed as Atlas-only. | Decline. Offer the metadata, and revisit after Payments migrates. |
| Decline 1: Hubris | 34 of 35 new services and 4.1/5 read as "we've won." | The OKR celebrates service count. The survey covers users only. | Tier-1 metrics; survey non-users too. |
| Decline 2: Undisciplined more | Atlas, more starters, dashboards growing into products. | Rollback carried over a fourth time. Headcount accepted with strings. | Stop-doing list; escalation rule. |
| Decline 3: Denial of risk | Legacy treated as "not our budget." Alerts muted. The Runway flag misfire shrugged off. | Incidents without a pipeline tag. Mutes without tickets. | Minimal instrumentation; mute expiry dates. |
| Decline 4: Grasping for salvation | After a major Payments outage, leadership forces a mass migration or a rewrite. | An exec mandate or reorg "to fix deploys." | Earn the migration with the lighthouse service first. |
| Decline 5: Capitulation | Payments builds its own platform, and Runway becomes the "low-risk services" tool. | Payments hires platform engineers or extends its legacy pipelines. | Deliver both Payments conditions within two quarters. |

Three of 11 gates are CONDITIONAL. They share one root cause: **priority discipline**. Capacity keeps flowing to visible, enjoyable work instead of the blocker that controls the risk.

## 12. Gate log

| Gate | Verdict | Note |
|---|---|---|
| 0 Fit | PASS | Team / org unit. Steward: Ines (EM). 12 people. 3-year history, multi-year horizon. Measurable. |
| 1 Baseline | PASS | Good, not yet great: 64% adoption, 34 of 35 new services on Runway, 41-min median, 4.1/5. Fails "distinctive impact" where it matters most. |
| 2 Level 5 | CONDITIONAL | Humility clear; resolve gap on rollback. |
| 3 First Who | CONDITIONAL | Key-person risk; compliance seat missing. |
| 4 Brutal facts | PASS | Consistent with Gate 1. No web research was available this session. |
| 5 Hedgehog | CONDITIONAL | Working hypothesis; the passion circle and tier-1 count are unconfirmed. |
| 6 Discipline | PASS | Stop-doing list of 7. Atlas declined. |
| 7 Technology (light) | PASS | **Accelerates:** rollback, approval gate, progressive rollout, templates, flags with guardrails. **Parity:** secret manager, build-cache dashboard. **Irrelevant now:** Atlas portal. **Pioneer:** SLO-triggered auto-rollback; compliance-as-code audit evidence. |
| 8 Flywheel | PASS | The loop closes. The weakest link (rollback → Payments migration) is unbuilt. |
| 9 Built to Last (light) | PASS | One-line BHAG used. |
| 10 Mighty Fall | PASS | Five decline risks logged. |

Tally from the table: 8 PASS, 3 CONDITIONAL, 0 FAIL.

*Method notes: autonomous mode. Memory and past chats weren't available, so no prior run was used as a baseline. The evidence batch was skipped, and inferences are marked `[ASSUMPTION]`. These are disciplined hypotheses to test, not guarantees. Collins's method was retrospective.*