**Verdict: good, not yet great. Decline Atlas as offered and ship fast rollback.**

- **Hedgehog Concept:** Runway makes changing Brightwater's money-moving services boringly safe. Any bad deploy is reversed in under five minutes, and compliance sign-off is built in.
- **Weakest flywheel link:** the first one. Sub-five-minute rollback doesn't exist yet, and it has slipped three quarters running.
- **Stop doing:**
  1. Building and owning Atlas.
  2. Starting new templates or starters before rollback ships.
  3. Measuring success as "% of services on Runway."
- **Most urgent brutal fact:** 5 of 6 Sev-1/Sev-2 incidents hit legacy pipelines, including both Sev-1s. Four of the six were in Payments, which has stated exactly what it needs before it will move.
- **Missing numbers that would change this:**
  - How many of the 119 legacy services are Payments or money-moving.
  - How many existing services actually migrated this quarter, as opposed to new ones starting on Runway.
  - Runway's current rollback time.
  - Whether the VP's two headcount can be used for something other than Atlas.

Greatness potential: 42/100

---

*Method note: this session had no access to memory, past chats or web search, so there was no prior baseline and no outside market research. The evidence questions were skipped (autonomous mode). Everything below rests on the Q3 retro dossier, and inferences are marked `[ASSUMPTION]`.*

## 1. The great version in one paragraph

A year from now, the Delivery Platform team is the reason Brightwater's riskiest software changes are dull. Every money-moving service, including card-auth-gateway, ledger-recon, payouts-scheduler and loan-disbursement, deploys through Runway. A bad deploy is detected and reversed in under five minutes, often automatically. The card-network change-approval step is a recorded, auditable stage in the pipeline, so nobody routes around it. Deploy-caused Sev-1s are rare, short and boring.

The team measures itself by risk covered, not by services counted. It says no to adjacent shiny work, including good ideas like a developer portal, because it knows exactly what it is for. Its value no longer depends on Ines, Bartek or any one person.

## 2. The Hedgehog Concept

**Sentence (working hypothesis):**
> *We make changing Brightwater's money-moving software boringly safe: any deploy, including the riskiest, reversible in under five minutes, with compliance built in.*

| Circle | Candidates considered | Kept | Ruled out (and why) |
|---|---|---|---|
| **Best in the world at** (the "world" is Brightwater) | Service templates; CI speed; progressive rollout and rollback; developer portal; legacy pipeline support | **Safe change for critical services:** progressive rollout, fast rollback, compliance-aware gates. The team already owns the rollout machinery and the paved road that 34 of 35 new services chose. | **Developer portal:** buyable or adoptable off the shelf `[ASSUMPTION]`, and not a distinctive strength. **Templates:** now table stakes, already won. **Raw CI speed:** nobody holding out is asking for it. |
| **Resource engine** (headcount and budget leverage) | Services on Runway; deploys; commit-to-prod minutes; Sev-1s avoided | **Leadership funds the team for avoiding customer-money incidents.** That is where Sev-1 cost, regulatory exposure and VP attention sit. | Service count: it rewards easy greenfield wins and ignores where the damage is. |
| **Passion** | Greenfield building; developer experience; making Runway excellent; reliability craft | **Making Runway the thing engineers trust.** Two team members already pushed for rollback over Atlas. | Greenfield for its own sake. Most of the team's excitement about Atlas is about novelty, not mission. |

**Denominator:** *money-moving (Tier-1) services covered by Runway with sub-five-minute rollback.* The team's leverage is measured per critical service made safe, not per service onboarded.

**Confirmation tests** (the evidence that would turn this hypothesis into a PASS):
- Payments migrates card-auth-gateway within one quarter of rollback plus the approval gate shipping. If Payments moves the goalposts, the "best at" circle is weaker than assumed.
- Deploy-caused Sev-1/Sev-2 incidents and rollback minutes fall measurably on migrated services.
- The team keeps the rollback epic as its top priority through Q4 without losing morale. This tests the passion circle.

**Does it explain past wins?** Partly. Runway won the easy middle on speed and convenience. **Does it rule things out?** Yes: Atlas, new starters and free pipeline tweaks. **Is it uncomfortable?** Yes. It means telling the VP "not this" with headcount on the table.

## 3. The flywheel

```
   ┌──────────────────────────────────────────────────────────┐
   │                                                          ▼
 (1) Ship <5-min rollback      (2) Money-moving services migrate
     + built-in approval gate  ───►  to Runway (Payments first)
   ▲                                          │
   │                                          ▼
 (5) Freed capacity + earned        (3) Fewer, shorter deploy-caused
     headcount reinvested in   ◄──      Sev-1/2s  [DENOMINATOR:
     safety (auto-rollback,             Tier-1 services with safe rollback]
     policy-as-code)                          │
   ▲                                          ▼
   └──────── (4) Legacy pipelines retire: fewer interrupts,
                 Bartek freed, leadership trust rises
```

**Weakest link:** component 1. It doesn't exist yet. The arrow from 1 to 2 also carries goalpost risk, because it depends on Payments honoring its stated conditions.

**Current push (next one or two turns):**
1. Staff and ship rollback in under five minutes, covering both deploy reverts and feature-flag reverts, since Runway's own Sev-2 was a flag misfire.
2. Co-design the change-approval gate with Payments and compliance. Pilot both on card-auth-gateway.

**Doom-loop check (warning signs already present):**
- A new direction each quarter (template v3, then Kotlin starter, now Atlas) instead of repeated pushes on one loop.
- A big new program (Atlas plus headcount) offered as the source of momentum.
- A Q4 target ("80% of services") that rewards motion, not progress on the loop.

None of these is fatal yet. All three point the same way.

## 4. The bus

| Person / commitment | Move | Why |
|---|---|---|
| **Ines (EM)** | Keep | Strong "window" behavior: she asked to come off the hero slide and credited the crew. Needs to add resolve (see the leadership read in Gate 2). |
| **Mei** | **Move seat → lead the rollback and approval-gate launch** `[ASSUMPTION: among the strongest executors]` | Ran template v3 to an early ship. Put the best launcher on the biggest opportunity. |
| **Sana** | Keep → co-own rollback with real staffing | Re-estimating an unstaffed epic three times is a priority failure, not a people failure. |
| **Bartek** | **Move seat → Payments migration** + pair a second engineer on legacy plugins | Only person who can debug legacy plugins. That knowledge is exactly what migration needs, and it is also the team's biggest single-person risk. |
| **TPM** | Keep → owns the Payments migration contract and the compliance relationship | Cross-org commitments need a dedicated owner. |
| **Ravi** | Keep | Kotlin gRPC example deferred; see the stop-doing list. |
| **Tomasz, the remaining engineers** | Keep | No evidence of misalignment. |
| **Intern's build-cache dashboard** | Keep, don't expand | Cheap and useful, but neutral to the Hedgehog Concept. |
| **Atlas (build and own)** | **Off the bus** | A real problem, but not this team's to own; see the stop-doing list. |
| **Ad-hoc one-off pipeline tweaks** | **Off the bus** as a free interrupt service | They eat the capacity the flywheel needs. |
| **Missing seat: Payments champion** | Add (seconded engineer from Payments) | Migrations of critical services need an insider. |
| **Missing seat: compliance partner** | Add (named contact, part-time) | Defines what an auditable approval gate and an emergency revert must look like. |
| **Missing seat: interrupt shield** | Add (rotating weekly) | Protects the rollback crew. |

"Off the bus" here means wrong role for this team, not a judgment of the idea or the people behind it.

## 5. Stop-doing list

1. **Stop: building and owning Atlas.** The 58% survey finding is real, but 34 of 35 new services already start on Runway, so discoverability is not Runway's bottleneck. The evidence for a halved onboarding time is one peer company's anecdote. Suggest that another team own a portal, or adopt an existing one `[ASSUMPTION]`.
2. **Stop: new templates, starters and template versions until rollback ships.** That includes the Kotlin gRPC example.
3. **Stop: measuring success by "% of services."** Keep it as a health metric only. Replace the Q4 OKR with a risk-weighted target.
4. **Stop: re-estimating the rollback epic.** Staff it as the number-one priority.
5. **Stop: free, unscheduled one-off pipeline tweaks.** Route them through weekly intake or self-serve configuration.
6. **Stop: muting alerts as a fix.** Every mute gets a ticket and an expiry date.
7. **Stop: treating Bartek's legacy debugging as an informal favor.** Make it a documented, rotated, time-boxed service with a sunset date tied to legacy retirement.
8. **Stop: "not our services, not our budget" for legacy measurement.** Emit at least deploy and rollback events for Tier-1 legacy services.

**Non-negotiable disciplines:**
- The top Hedgehog item is protected every quarter and cannot be displaced by visible greenfield work.
- Every deploy-caused Sev-1/Sev-2, on any pipeline, gets a blameless review with a Runway follow-up.
- Rollback drills (game days) run on Tier-1 services monthly.

**Framework boundaries:**
- *Fixed:* the denominator and rollback-first priority.
- *Free:* engineers choose how they build within that, including design, tooling and pairing.
- *Bureaucracy check:* the Payments manual sign-off is compliance, not bureaucracy. Build it in rather than fighting it.

## 6. Brutal facts and faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | Runway isn't where the damage is | 5 of 6 Sev-1/2 on legacy; both Sev-1s in Payments; card-auth-gateway failed twice with 47- and 22-minute rollbacks | **Critical** | Ines |
| 2 | The team keeps choosing visible work over critical work | Rollback slipped three quarters behind template v3 and Kotlin; Atlas is the next candidate | **Critical** | Ines |
| 3 | The biggest holdout's price is known and unpaid | Payments has stated its conditions repeatedly: rollback under five minutes plus an approval step | High | TPM |
| 4 | Growth may be almost all greenfield | Net +25 Runway with 34 new on Runway means about 30 services were retired; actual legacy migrations can't be confirmed and may be near zero | High | TPM |
| 5 | 80% in one quarter is likely unreachable without legacy migrations | Needs +53 net (265 of 331) against a +25/quarter pace | Medium | Ines + TPM |
| 6 | The team can't see the 36% where the incidents happen | Legacy pipelines aren't instrumented | High | Bartek |
| 7 | Single point of failure | Only Bartek can debug legacy plugins | High | Ines |
| 8 | Red flags are being silenced | Two disk alerts muted; satisfaction surveyed only among Runway users | Medium | Bartek |
| 9 | Runway isn't immune | Runway's own Sev-2 was a feature-flag misfire. Payments will notice. | Medium | Sana |
| 10 | Fast rollback and manual approval may conflict | Needs a compliance rule that reverting to a previously approved version requires no new sign-off `[ASSUMPTION]` | High | TPM + compliance |

**Truth climate:** good. The retro is candid, dissent on Atlas was voiced, and Ines invited debate. Gaps: muted alerts, user-only surveys, and the "not our budget" framing in the parking lot. **Charisma check:** not an issue, since Ines is low-ego. The risk is consensus drifting toward excitement, not suppression.

**Faith statement:** Brightwater has already chosen Runway for nearly every new service. Once Runway makes the riskiest change safe, the last holdouts will have no reason left to stay away.

## 7. Core ideology and BHAG

**Core values:**
1. Customers' money is never the price of shipping.
2. A paved road, not a mandate: the team earns adoption.
3. Measure what actually matters, even when it's not ours.
4. Credit the crew; own the misses.

**Core purpose:** let every Brightwater engineer change software without putting customers' money at risk.

**BHAG (one line; team horizon, so kept short):** *No Brightwater customer ever loses money or access because of a deploy.*

**Clock-building mechanisms:**
- Rollback drills.
- Tier-1 coverage dashboard.
- Rotated legacy knowledge.
- Policy-as-code approval gates.
- Architecture decision records.
- A written migration contract with each product org.

## 8. Scorecard

| Output | Current (end of Q3) | 12-month target | BHAG trajectory |
|---|---|---|---|
| **Money-moving (Tier-1) services deploying via Runway** | Unknown `[missing]`. At least 4 critical services are legacy (card-auth-gateway, ledger-recon, payouts-scheduler, loan-disbursement). | All Payments Tier-1 services, including card-auth-gateway `[ASSUMPTION]` | 100% of Tier-1 |
| **Bad-deploy rollback time, p95, Tier-1** | Legacy: 22 and 47 min (2 data points). Runway: unmeasured. | **< 5 min** | < 1 min, automatic |
| **Deploy-caused Sev-1/Sev-2 per quarter** | 6 (5 legacy, 1 Runway) | ≤ 2, none with rollback > 5 min `[ASSUMPTION]` | Near zero customer-impact minutes |
| *Health metric (not a goal):* services on Runway | 212 of 331 (64%) | Tracked, not targeted | — |

## 9. Next 90 days

| # | Action | Owner |
|---|---|---|
| 1 | **Answer the VP before the offsite.** Decline building and owning Atlas. Counter-propose spending the two headcount on rollback plus the approval gate, framed as cutting the Sev-1 pattern on card-auth-gateway. Offer one cheap, in-Hedgehog piece: a required owner field in Runway service manifests. Propose revisiting Atlas once the Tier-1 target is hit. Be ready to proceed even if the headcount is withdrawn. | Ines |
| 2 | **Rewrite the Q4 OKR** from "80% of services" to: "Rollback < 5 min shipped on Runway, and card-auth-gateway live on Runway with the approval gate." | Ines + TPM |
| 3 | **Staff rollback as priority #1**, covering deploys and feature flags. Freeze new template work and set up the rotating interrupt shield. | Mei (lead) + Sana `[ASSUMPTION]` |
| 4 | **Pin the goalposts.** Co-design the approval gate with the Payments platform lead and compliance, including the emergency-revert rule. Get written acceptance criteria and a migration date. | TPM + Bartek |
| 5 | **Make the risk visible.** Emit deploy and rollback events for Tier-1 legacy services, fix the muted disk alerts properly, and pair a second engineer on legacy plugins. | Bartek + one engineer |

## 10. Re-check

Offered once: set up a re-check at the end of Q4 (Year 0), about 90 days out. It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8, with special attention to whether Payments moved once its conditions were met. This session can't schedule tasks, so the reminder has to be set elsewhere.

## 11. Risk register

| Source | Risk | Early warning | Evidence for PASS / mitigation |
|---|---|---|---|
| Gate 2 CONDITIONAL | Ines's humility is clear, but her resolve to protect the critical priority is unproven | Atlas is decided by enthusiasm vote; rollback slips a fourth time | Rollback ships in Q4 under explicit priority protection by Ines |
| Gate 5 CONDITIONAL | The passion circle is uncertain and the Payments goalposts are untested | Morale dips during rollback work; Payments adds new conditions | Team commits at the offsite; card-auth-gateway migrates within a quarter of shipping |
| Gate 6 CONDITIONAL | The stop-doing list is proposed but not adopted | Kotlin or Atlas work reappears in sprints | List adopted in Q4 planning; sprint work outside the Hedgehog Concept < 20% `[ASSUMPTION]` |
| Gate 3 | Bartek bus factor | Payments escalations still route only to him | Second engineer handles a legacy issue alone |
| Gate 4 | Rollback and manual approval conflict | Compliance rejects approval-exempt reverts | Written compliance ruling early in Q4 |
| External | VP withdraws headcount or insists on Atlas | Offsite framing shifts to "portal first" | The case framed in Sev-1 cost; a fallback plan with current staff |
| **Decline 1: Hubris** | "34 of 35 new services chose us" breeds dismissal of holdouts | Payments described as "resistant" | Treat holdouts' conditions as requirements |
| **Decline 2: More** | Atlas, new starters, scope sprawl funded by headcount | Roadmap items outside the Hedgehog Concept grow | Stop-doing list reviewed quarterly |
| **Decline 3: Denial** | Uninstrumented legacy, muted alerts, user-only surveys, "not our budget" | Incidents attributed to "their pipeline" | Company-wide deploy incident reviews |
| **Decline 4: Salvation** | After a Sev-1, a forced migration mandate or a Runway v4 rewrite | Proposals for big-bang deadlines | Stay on the flywheel and push one Tier-1 service at a time |
| **Decline 5: Irrelevance** | Payments builds its own platform; Runway becomes a starter kit for non-critical services | Payments starts its own rollback project | Win card-auth-gateway within 2 quarters |

**Shared root cause:** all three CONDITIONALs, and decline risks 2 and 3, trace to one pattern. The team picks visible greenfield work over the hard critical path.

## 12. Gate log

| Gate | Verdict | Note |
|---|---|---|
| 0 Fit | PASS | Team / org unit; steward Ines; ongoing for 3 years with a multi-year horizon; measurable |
| 1 Baseline | PASS | **Good, not yet great.** 34/35 new services choose Runway; 41-min median deploy; 4.1/5 satisfaction; pages down 29% |
| 2 Level 5 Leadership | CONDITIONAL | Strong humility; resolve unproven (see the risk register) |
| 3 First Who | PASS | Right people; seats moved; three seats missing |
| 4 Brutal Facts | PASS | Facts limit "great" but don't contradict "good" |
| 5 Hedgehog | CONDITIONAL | Intersection exists; passion and Payments goalposts untested |
| 6 Discipline | CONDITIONAL | Stop-doing list not yet adopted |
| 7 Technology | PASS | See the tech triage below |
| 8 Flywheel | PASS | Loop closes; first component unbuilt; mild doom-loop signs |
| 9 Built to Last | PASS | BHAG kept to one line (team horizon) |
| 10 Mighty Fall | PASS | Five decline paths named |

**Tally (counted from the table):** 11 gates, 8 PASS, 3 CONDITIONAL, 0 FAIL.

---

### Appendix: gate artifacts not shown above

**Subject card (Gate 0):**
- **Name:** Delivery Platform team (Runway), Brightwater Financial.
- **Type:** team / org unit.
- **Steward:** Ines (EM).
- **Size:** 10 engineers, 1 EM, 1 TPM.
- **Horizon:** multi-year.
- **Stage:** year 3, at majority adoption.

**Baseline sheet (Gate 1):**
- **Good:** 64% coverage (up from 57%); 34 of 35 new services on Runway; median commit-to-prod 58 → 41 min; 4.1/5 satisfaction among Runway users; on-call pages 52 → 37; secret-manager migration with zero incidents.
- **Tests of great:**
  - *Superior performance:* not yet, because the incident risk sits outside Runway.
  - *Distinctive impact:* yes for 212 services.
  - *Endurance:* weak, given the Bartek dependency and unmeasured legacy.

**Leadership read (Gate 2):**
- **Strengths:** credits others publicly and invites debate.
- **Gap:** the rollback slip has been carried for three quarters without a visible "mirror" moment. The Atlas decision is being delegated to consensus under a deadline.
- **One behavior change:** Ines states the priority call herself ("rollback first, and here's why"), owns the past slips aloud, and then lets the team design the how.

**Tech triage (Gate 7):**

| Technology | Class |
|---|---|
| Progressive rollout with automated rollback (SLO-triggered revert) | **Accelerates.** Pioneer candidate. |
| Policy-as-code approval gates with audit export | **Accelerates.** Pioneer candidate: compliance-native deploys. |
| Feature flags | Accelerates, but needs revert guardrails |
| Deploy and rollback event instrumentation for legacy | Accelerates (data) |
| Service templates, Kotlin starter | Parity: maintain, don't expand |
| Build-cache dashboard, secret manager | Parity |
| Developer portal (Atlas) | Irrelevant to this team's Hedgehog Concept. **Hype flag:** justified by one peer anecdote. |