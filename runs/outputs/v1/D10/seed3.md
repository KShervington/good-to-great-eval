# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict

**Good, not yet great.** Runway already wins the easy services. The services that move money are still not on it.

- **Hedgehog Concept:** *Make changing production at Brightwater fast and reversible, and measure ourselves by the money-moving services that trust Runway with it.*
- **Weakest flywheel link:** rollback under five minutes plus Payments' change-approval step. It has never been built, so Payments won't migrate.
- **Stop doing:** (1) taking ownership of Atlas now; (2) the "80% of services" OKR; (3) new templates or starters before rollback ships.
- **Most urgent brutal fact:** 5 of 6 Sev-1/2 incidents were on legacy pipelines. Both Sev-1s were Payments deploys. The card-auth-gateway service took 47 and 22 minutes to roll back.
- **Missing numbers that would change this answer:** a tier-1 service list, current Runway rollback time, migrations vs. retirements in Q3, and whether the VP's two headcount can be redirected.

Greatness potential: 55/100

---

## 1. The great version in one paragraph

Runway is the boring, trusted way every Brightwater service reaches production. That includes card authorization, payouts and loan disbursement. Any deploy can be undone in under five minutes. Payments' compliance sign-off is a step inside the pipeline with an exportable audit trail, not a reason to stay off it. Deploy-caused Sev-1s are rare and short. The team is judged by customer-impact minutes it has eliminated, not by service count. The legacy pipelines are retired, and Bartek's plugin knowledge is no longer a single point of failure. New services default to Runway with no effort, as they nearly do today. The team earns headcount because it removes the company's largest source of production risk, not because it takes on visible greenfield projects.

## 2. The Hedgehog Concept *(working hypothesis)*

**Sentence:** *Make changing production at Brightwater fast and reversible, and measure ourselves by the money-moving services that trust Runway with it.*

| Circle | Candidates considered | Narrowed to | Not best at |
|---|---|---|---|
| **Best in the world at** (world = Brightwater) | Service templates; CI speed; progressive rollout; developer portal; safe change for regulated services | **Safe, reversible change to production, including the compliance-gated kind.** No vendor or other team knows Brightwater's deploy paths, incidents and Payments' audit step the way this team can. | Developer portals, catalogs and docs search, where off-the-shelf tools exist `[ASSUMPTION]`. A growing library of language starters. One-off pipeline customization. |
| **Economic / resource engine** (headcount, budget, VP trust) | Services on Runway; deploys per engineer; satisfaction; incident minutes avoided | **Denominator: deploy-caused customer-impact minutes on tier-1 services, per quarter.** All 6 Q3 Sev-1/2s were change-caused (config push, deploy, flag, migration, dependency upgrade), so this is the risk the company will pay to remove. | Raw service count. You can reach 80% without moving a single Payments service. |
| **Deep passion** | Greenfield, visible work; developer happiness; craft and safe execution | **Shipping without fear.** Evidence: zero-incident secret-manager migration, template v3 two weeks early, on-call pages down 29%. `[ASSUMPTION]` The team's visible energy goes to new, greenfield work (v3, Kotlin, Atlas), so passion for rollback and compliance is unconfirmed. Two people asking about the rollback epic is a good sign. | — |

**Tests**
- **Explains past wins?** Yes. Commit-to-production fell from 58 to 41 minutes, pages fell, new services adopt almost universally, and the secret migration had no incidents.
- **Explains the failure?** Yes. Payments stays off because Runway isn't yet reversible or compliance-aware enough.
- **Rules things out?** Yes: Atlas ownership, more starters and one-off tweaks.
- **Uncomfortable?** Yes. It means turning down greenfield work and two headcount the team is excited about.

**What would confirm it within about two quarters:**
1. Rollback under five minutes ships, and Payments starts migrating card-auth-gateway.
2. Deploy-caused impact minutes on tier-1 services fall measurably.
3. The team's engagement holds through a quarter of unglamorous work.

## 3. The flywheel

```
 ┌─► 1. Reversible, compliance-aware Runway
 │      (rollback <5 min + change-approval step with audit trail)
 │                    │
 │                    ▼
 │   2. Tier-1 / Payments services migrate
 │      (card-auth-gateway as lighthouse)
 │                    │
 │                    ▼
 │   3. Deploy-caused customer-impact minutes fall   ◄── denominator
 │      (measured from the incident tracker)
 │                    │
 │                    ▼
 │   4. Proof → credibility → VP mandate + headcount earned
 │                    │
 │                    ▼
 │   5. Legacy pipelines retire; interrupts and
 │      legacy-plugin support shrink (Bartek freed)
 │                    │
 └────────────────────┘  (capacity reinvested in step 1)

 Side loop already spinning: new services default to Runway (34 of 35 in Q3)
```

**Current push:** step 1 → step 2. Ship rollback under five minutes on Runway, co-design the change-approval step with the Payments platform lead and compliance, and plan card-auth-gateway as the first migration.

**Weakest link:** step 1. It has been pushed zero times in three quarters.

**Doom-loop check (moderate risk):**
- **New direction every quarter:** template v3, then the Kotlin starter, now Atlas. Each one is visible and new, and each pushed out the one thing the holdout customer asked for.
- **A big program to jump-start momentum:** Atlas plus two headcount fits this pattern.
- **Reacting without understanding:** one-off pipeline tweaks consume capacity.

The loop closes, so the gate passes. But the team has been pushing a side loop, not the main one.

## 4. The bus

| Person / commitment | Move | Why |
|---|---|---|
| Ines (EM) | **Keep** | Humble, invites dissent, credits the crew. Needs to supply more resolve (see Gate 2). |
| TPM | **Keep; new seat:** owner of the Payments migration program and the change-approval requirements | Cross-org compliance work needs a program owner. |
| Mei | **Move seat → lead rollback + change-approval** | Proven launcher (v3). Put the best people on the biggest opportunity. |
| Sana | **Keep; pair with Mei on rollback** | The epic's slips trace to prioritization, not to her `[ASSUMPTION]`. Give her staffing, not another re-estimate. |
| Bartek | **Move seat → legacy-to-Runway translation for Payments** | He is the only legacy-plugin debugger, a hidden single point of failure. His knowledge is exactly what migration needs. Write it down as runbooks. |
| Ravi | **Keep** | Finish the gRPC example only if it is small `[ASSUMPTION]`, then join the rollback or migration work. |
| Tomasz (on leave), other engineers | **Keep** `[ASSUMPTION]` | No evidence of misalignment. Assign to the main loop when he returns. |
| Intern / build-cache dashboard | **Keep** | Cheap, useful, and supports speed. |
| *Commitment:* ad-hoc one-off pipeline tweaks | **Off** | Replace with a weekly intake or office hours and self-serve extension points. |
| *Commitment:* informal legacy-plugin support for Payments | **Off as a favor, on as migration work** | Turns firefighting into progress on the flywheel. |
| *Commitment:* owning Atlas | **Don't board (now)** | Outside the Hedgehog Concept. See stop-doing. |
| **Missing:** Payments migration partner | **Fill** | A named Payments engineer co-owning card-auth-gateway's move. |
| **Missing:** compliance/audit stakeholder | **Fill** | Must sign off that Runway's approval step satisfies the card-network audit. |
| **Missing:** VP as sponsor of the Payments path | **Fill** | Redirect her energy and the two headcount toward the main loop. |

## 5. Stop-doing list

1. **Don't take ownership of Atlas this year.** Tell the VP, with the incident table: "Both Sev-1s this quarter were Payments legacy deploys; give us the two headcount to make those reversible." Offer Runway's service-ownership metadata as an API for whoever builds a portal (`[ASSUMPTION]` that Runway records ownership). Revisit Atlas once rollback ships and the first Payments tier-1 service is live on Runway. The 58% "finding the owner or docs is hard" finding is real, but it isn't this team's Hedgehog Concept. The onboarding claim (six weeks to three) rests on one peer-company anecdote.
2. **Stop the "80% of services" OKR.** It needs 53 more services (265 of 331). It is reachable without touching Payments, and it rewards exactly the work that has crowded out rollback.
3. **No new template versions or language starters until rollback ships**, apart from security fixes.
4. **Stop fielding one-off pipeline tweaks by DM.** Use an intake queue, office hours and extension points.
5. **Stop carrying epics.** Anything carried over twice is either staffed this quarter or killed in writing.
6. **Stop muting alerts without a ticket, owner and expiry date.** This applies to the build-cluster disk alerts and everything after them.
7. **Stop celebrating raw service count.** Report tier-1 coverage and impact minutes first.
8. **Stop saying "not our services, not our budget"** about legacy risk. Legacy incidents are the clearest evidence of Runway's value.

## 6. Brutal facts and the faith statement

*Web and market research isn't available in this session, so this register is built from the dossier alone.*

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The riskiest deploys aren't on Runway. | 5 of 6 Sev-1/2 on legacy; both Sev-1s in Payments; card-auth-gateway twice, with 47 and 22 min rollbacks. Per service: legacy 5/119 (4.2%) vs. Runway 1/212 (0.5%). Small sample, and confounded by Payments' risk profile. | Critical | Ines |
| 2 | The holdout customer stated its terms and the team hasn't met them for three quarters. | Rollback epic carried three times. The change-approval step isn't on any backlog or action list. | Critical | Ines / Mei |
| 3 | Adoption growth is mostly new services, not migrations. | Net Runway +25 vs. 34 new Runway services. 30 services left the inventory. The data allows anywhere from 0 to 21 migrations, so it can't prove any happened. | High | TPM |
| 4 | The draft OKR measures the wrong thing. | 80% by count is reachable without a single tier-1 move. | High | Ines + TPM |
| 5 | The team can't show Runway beats legacy. | Legacy isn't instrumented, and satisfaction (4.1) was measured only among Runway users. The incident tracker already holds impact data, so no pipeline instrumentation is needed to start. | Medium | TPM |
| 6 | A single point of failure is hidden in a kudos line. | Bartek is the only person who can debug the legacy plugins. | Medium | Bartek / Ines |
| 7 | Warning signals are being silenced. | Disk alerts were muted rather than fixed. | Low (as a symptom: medium) | Bartek |
| 8 | The team's enthusiasm reliably beats its own top priority. | v3 and Kotlin beat rollback. Atlas is next in line and "most of the team is excited." | High | Ines |

**Truth climate:** mostly healthy. The retro is candid, two people dissented on Atlas, and Ines invites debate.

- **Gaps:** muting alerts, and dismissing legacy measurement in the parking lot.
- **Charisma check:** low risk. Ines suppresses her own spotlight, not bad news. The real risk is consensus drifting toward the exciting work.
- **Red-flag mechanism to add:** every Sev-1/2 change-caused incident, on any pipeline, gets a blameless review with one required line: *"Would Runway as it exists today have prevented or shortened this? If not, what's missing?"*

**Faith statement:** Runway already wins nearly every service it's allowed to compete for. Once it can undo a bad deploy faster than Payments can page someone, the services that move money will come too.

## 7. Core ideology and the BHAG

**Core values**
1. Every change is reversible.
2. Serve the hardest customer first.
3. Measure what hurts, even when it isn't ours.
4. Credit the crew, own the misses.

**Core purpose:** let every Brightwater engineer change production without fear, so customers' money never pays for a bad deploy.

**BHAG (kept to one line because this is a team inside an organization):** *No Brightwater customer loses access to their money because of a deploy.*

**Mechanisms that work without the current people:**
- A weekly rollback drill.
- The carried-epic rule.
- The "would Runway have helped?" line in every incident review.
- Tier-1 coverage and impact minutes on the team dashboard.
- Legacy-plugin runbooks.
- Pipeline intake in place of DMs.
- An alert-muting policy.

## 8. Scorecard

| Output | Current (end Q3, Y0) | 12-month target | BHAG trajectory |
|---|---|---|---|
| Tier-1 (money-moving) services on Runway | Unknown; no tier-1 list exists. At least 4 money-moving services are known to be on legacy (card-auth-gateway, ledger-recon, payouts-scheduler, loan-disbursement). | ≥ 50% of tier-1, including card-auth-gateway `[ASSUMPTION]` | 100% of tier-1 |
| Runway rollback time (p90) | Unmeasured; assumed > 5 min `[ASSUMPTION]` | < 5 min in production for all Runway services | < 1 min, automatic on health signals |
| Change-caused Sev-1/2 and customer-impact minutes | 6 Sev-1/2 (5 legacy, 2 Sev-1). Known rollback time: 69 min across the two card-auth incidents. Full impact minutes not yet computed. | Halve change-caused Sev-1/2 per quarter `[ASSUMPTION]` | Zero Sev-1s from a deploy that couldn't be undone in 5 min |

Health metric, not a target: overall adoption (64%, up from 57% in Q2).

## 9. Next 90 days (Q4)

1. **Answer the VP on Atlas before the offsite.** Decline ownership for now, propose redirecting the two headcount to rollback and the Payments path, and offer the ownership-metadata API. *Owner: Ines.*
2. **Make rollback under five minutes the top priority, fully staffed.** Mei leads, Sana co-owns, and nothing new starts before it reaches a production pilot. *Owner: Mei.*
3. **Write the change-approval requirements with Payments and compliance within 30 days**, then build the approval step as an auditable pipeline stage. *Owner: TPM + Payments platform lead.*
4. **Rewrite the Q4 OKRs around the scorecard.** Build the tier-1 list with org leads and baseline impact minutes from the incident tracker. *Owner: Ines + TPM.*
5. **Prepare card-auth-gateway as the lighthouse migration**: plugin-by-plugin translation plus runbooks. *Owner: Bartek + Payments migration partner.*

## 10. Re-check

I can't set up a scheduled task from this session. I recommend a re-check around the end of Q1, Y1, about 90 days out. It should re-score the three scorecard rows with real numbers, re-run Gate 1 (is tier-1 coverage moving?), Gate 5 (did the team stay engaged, and did Payments commit?) and Gate 8 (did step 1 actually turn?). If you'd like, I can set that up in a session that has scheduling tools.

## 11. Risk register

| Source | Risk | Condition / early warning | Evidence that clears it |
|---|---|---|---|
| Gate 2 (CONDITIONAL) | Leader's resolve. The rollback epic slipped three times under the current plan. | Atlas decided by an enthusiasm vote, without the incident data. | Rollback reaches a production pilot in Q4 with no further slip. |
| Gate 5 (CONDITIONAL) | Passion circle unconfirmed; denominator unmeasured. | Engagement or attrition drops in a maintenance-heavy quarter; no tier-1 list by mid-Q4. | Team commits at the offsite; tier-1 list and impact-minute baseline exist. |
| Gate 6 (CONDITIONAL) | Discipline untested on the Atlas decision. | Atlas accepted "in parallel," or the capacity floor for rollback isn't set. | Atlas declined or deferred in writing; rollback staffed first. |
| Gate 10, stage 1: hubris | "200+ services, 34 of 35 new" breeds belief that the hard core will follow on its own. | Count celebrated while Payments migrations stay at zero. | — |
| Gate 10, stage 2: more | Atlas and more starters. | New scope accepted while any epic is carried over. | — |
| Gate 10, stage 3: denial | "Not our services" thinking; muted alerts. | Incident reviews of legacy Sev-1s that never mention Runway. | — |
| Gate 10, stage 4: salvation | A Runway v4 rewrite, a portal bought for visibility, or a top-down migration mandate without rollback. | A proposal for a VP mandate before rollback ships. | — |
| Gate 10, stage 5: irrelevance | Payments builds its own deploy platform, and Runway becomes the tool for non-critical services. | Payments staffs its own rollback or CD project. | — |
| External | VP ties the headcount to Atlas only. | The redirect request is refused. | Even then, decline Atlas ownership. Fewer people on the right loop beats more people on the wrong one. |

**Root cause shared by the three CONDITIONALs:** priority discipline. The hard, unglamorous Payments work keeps losing to visible new work.

## 12. Gate log

Evidence basis: the dossier only. Memory, past runs and web research weren't available, so no prior baseline exists.

| Gate | Verdict | One line |
|---|---|---|
| 0 Fit | PASS | Ongoing internal platform team with a steward (Ines), a three-year history, and measurable outcomes. |
| 1 Baseline | PASS | Good, not yet great: 64% adoption, 34 of 35 new services, 41-min median, 4.1/5. Fails the distinctive-impact test on the critical services. |
| 2 Level 5 | CONDITIONAL | Humility is clear; resolve is unproven. |
| 3 First Who | PASS | No misaligned key seats. Move Mei and Bartek to the main loop; fill the Payments and compliance seats. |
| 4 Brutal Facts | PASS | Critical facts are about legacy incidents and an unmet customer condition. They refine Gate 1 rather than contradict it. |
| 5 Hedgehog | CONDITIONAL | Fast, reversible change, measured on money-moving services. Passion circle and denominator still to confirm. |
| 6 Discipline | CONDITIONAL | Stop-doing list is clear; the Atlas decision is the test. |
| 7 Technology | PASS | Rollback and approval-as-code accelerate the Hedgehog Concept; the portal is out of scope for now. |
| 8 Flywheel | PASS | The loop closes. Weakest link is step 1. |
| 9 Built to Last | PASS | Values, purpose, a one-line BHAG and mechanisms are defined. |
| 10 Mighty Fall | PASS | Stages 2 and 3 are the live risks. |

Tally from the table: 8 PASS, 3 CONDITIONAL, 0 FAIL.

---

## Appendix: gate artifacts not shown above

**Gate 0, subject card**

| Field | Value |
|---|---|
| Name | Delivery Platform team (Runway) |
| Type | Team / org unit |
| Steward | Ines (EM), with the TPM. VP of Engineering is the sponsor. |
| Horizon | Multi-year (three years old; legacy retirement spans years) |
| Stage | Mature adoption among new services; stalled on critical services |

**Gate 1, baseline sheet**
- **Evidence of good:**
  - Runway share rose from 187/326 (57%) to 212/331 (64%).
  - 34 of 35 new services started on Runway.
  - Median commit-to-production fell from 58 to 41 min.
  - On-call pages fell from 52 to 37.
  - 4.1/5 satisfaction (118 respondents, Runway users only).
  - Secret migration finished with zero incidents.
- **Tests of great:**
  - Superior performance: partial, since Runway is faster but legacy isn't measured.
  - Distinctive impact: not yet, since the riskiest services don't use it.
  - Endurance: partial. The team culture is sound, but there is a hidden single point of failure (Bartek).

**Gate 2, leadership read**
- **Strengths:** Ines gave the credit away (the hero slide), invites dissent, and runs a candid retro.
- **Gaps:** she let the stated customer condition slip three quarters, is putting a strategy call to an open vote, and drafted a count-based OKR.
- **One behavior change:** bring the incident table to the Atlas discussion, lead with the question "which of our Q3 incidents would Atlas have prevented?", then make the call and own it.

**Gate 6, framework**
- **Framework:** Q4 capacity goes first to rollback, the approval step and the card-auth-gateway preparation. A floor of about 60% of engineering time is suggested `[ASSUMPTION]`.
- **Freedom:** the team chooses design, sequencing and tooling within that floor.
- **Non-negotiables:** weekly rollback drill, blameless review of every change-caused Sev-1/2, the carried-epic rule, and no alert muted without an expiry date.
- **Bureaucracy check:** Payments' manual sign-off is a genuine compliance requirement, not a workaround for having the wrong people. Runway should encode it, not argue against it.

**Gate 7, tech triage**

| Technology | Class |
|---|---|
| Progressive rollout | Accelerates (the foundation for fast rollback) |
| Automated health-based rollback | Accelerates, **pioneer candidate** |
| Change-approval as code with audit export | Accelerates, **pioneer candidate** (a lasting advantage for regulated services) |
| Feature flags | Accelerates, but needs guardrails (cause of the Q3 notifications incident) |
| Build-cache dashboard, secret manager, disk-alert fix | Parity / keep up |
| Kotlin starter and further starters | Neutral; freeze new scope |
| Atlas developer portal | Outside the Hedgehog Concept for now. Adoption is hype- and visibility-driven (a single peer-company visit). |
| Full legacy-pipeline instrumentation | Not needed; use incident-tracker data instead |