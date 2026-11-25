# Good to Great: Delivery Platform team (Runway), Brightwater Financial

## Verdict

**Good, not yet great. Decline Atlas as offered and ship rollback.**

- **Hedgehog Concept:** Runway is how Brightwater changes money-moving production safely. Every deploy can be approved, rolled out progressively and undone in under five minutes.
- **Weakest flywheel link:** fast rollback plus a compliance approval step. It has slipped three quarters in a row, and it is the stated price of moving Payments onto Runway.
- **Top three stop-doing items:** (1) taking Atlas as offered; (2) steering by raw service count ("80%"); (3) one-off pipeline tweaks handled as interrupts.
- **Most urgent brutal fact:** both Sev-1s and 4 of 6 Sev-1/2s were Payments services on legacy pipelines. card-auth-gateway had two of them, taking 47 and 22 minutes to roll back.
- **Numbers that would change this:** the count of tier-1 money-moving services and which pipeline each uses; Runway's current rollback time; Q3 migrations versus retirements; the cost of Atlas.
- **Confidence:** moderate. It rests on one quarter of incidents and one retro, with no service-tiering data.

Greatness potential: 55/100

---

## 1. The great version in one paragraph

In the great version, nobody at Brightwater debates whether a change to a service that moves money is safe to ship, because it goes through Runway. Runway records the card-network compliance sign-off as a first-class, auditable step. It rolls the change out progressively and can undo it in under five minutes, and the team proves that with regular drills. Payments and Lending moved their critical services because Runway met their conditions, not because they were told to. Deploy-caused Sev-1s on money-moving services become rare, and the team measures that across every pipeline, including the legacy ones it doesn't own. The team is small and narrow. It turns down attractive greenfield work, and it earns headcount by reducing risk the company can see, not by taking on visible new products. Its output is indispensable: if it disappeared, the company would lose its main way of making production changes safe.

## 2. The Hedgehog Concept (working hypothesis)

**Sentence:** *We make changing production at Brightwater boringly safe, starting with the services that move money.*

| Circle | Candidates considered | Chosen | Not best at (rule out) |
|---|---|---|---|
| Best in the world at (world = Brightwater) | Service templates; CI speed; developer experience broadly; safe, compliant deploys of money-moving services | **Safe, compliant, reversible change for money-moving services.** The team already runs progressive rollout and has cut median lead time from 58 to 41 min. | Developer portals and catalogs, docs search, language starter kits beyond the core, bespoke per-team pipeline customization, long-term ownership of other orgs' legacy pipelines |
| Resource engine (headcount, budget, trust) | Services on Runway; deploys per quarter; developer satisfaction; incidents avoided | **Mandate and headcount earned per tier-1 service on Runway.** In a payments and lending company, trust comes from removing deploy risk on critical paths, not from coverage of low-risk services. `[ASSUMPTION]` | Headcount "bought" by taking on adjacent products (Atlas) |
| Deeply passionate about | Greenfield launches; developer experience; reliability and safety | **Developer experience and craft, aimed at reliability.** `[ASSUMPTION]` The retro shows the most energy for launches and greenfield work. Only two people pushed for rollback. | |

**Denominator:** tier-1 (money-moving) services on Runway. Track it together with the worst-case rollback time on those services.

**Confirmation tests (6–12 months):**
1. Rollback in under five minutes and the approval step ship, and Payments migrates card-auth-gateway as the first, "lighthouse" service.
2. Deploy-caused Sev-1/2s on money-moving services fall, measured across all pipelines.
3. The VP grants further headcount or mandate on the strength of that result, with no adjacent product attached.
4. The team, not just its manager, commits to this focus over Atlas in the Q4 vote. This tests the passion circle, which is the weakest.

**It explains past wins:** 34 of 35 new services chose Runway, and satisfaction is 4.1/5. The team wins wherever the safe, paved road also fits the need. **It rules things out:** Atlas, more starter kits, and the 80% count OKR. **It is uncomfortable:** it means telling an enthusiastic team and a VP holding two headcount "not this."

## 3. The flywheel

```
   ┌─► 1. Ship <5-min rollback + auditable approval step in Runway
   │                    │
   │                    ▼
   │   2. A tier-1 Payments service migrates (lighthouse: card-auth-gateway)
   │                    │
   │                    ▼
   │   3. Fewer, shorter deploy-caused Sev-1/2s on money-moving services
   │      (measured across ALL pipelines)
   │                    │
   │                    ▼
   │   4. Visible proof → trust from Payments/Lending + VP → mandate, headcount
   │                    │
   │                    ▼
   │   5. Capacity to migrate the next tier-1 services; legacy plugins retire;
   │      interrupts and the knowledge held only by Bartek shrink
   └────────────────────┘
```

- **Weakest link:** step 1 has not turned in three quarters. Step 3 is half-blind, because legacy pipelines aren't instrumented, though the incident tracker already tags pipelines.
- **Current push:** (a) rollback under five minutes on Runway, drill-tested; (b) an approval step co-designed with the Payments platform lead against the card-network audit requirement; (c) card-auth-gateway as the lighthouse migration.
- **Doom-loop check:** there are early signs but no full doom loop yet.
  - The direction shifts each quarter (template v3, then the Kotlin starter, now Atlas) while the stated blocker waits.
  - A large, visible program with headcount attached is being weighed as the source of momentum.
  - The draft OKR measures activity (count) rather than the outcome (risk).

## 4. The bus

| Person / commitment | Call | Why |
|---|---|---|
| Ines (EM) | **Keep** | Humble, runs a candid retro. Needs to lead harder on the Atlas decision (see the leadership read). |
| TPM | **Keep, refocus** | Owns the Payments migration agreement and rewrites the OKRs around tier-1 measures. |
| Mei | **Move seat → lead rollback + approval** | Shipped template v3 two weeks early. Put the best launcher on the biggest opportunity. `[ASSUMPTION]` she wants it. |
| Sana | **Keep, pair with Mei** | Has carried the rollback re-estimate three times. Pair her with Mei and give her protected time rather than another carry-over. |
| Bartek | **Keep; move seat partly → migration guide** | Only person who can debug legacy plugins. That knowledge is exactly what a Payments migration needs, but it is also a single point of failure. Pair him with someone and document what he knows. |
| Ravi | **Keep** | The gRPC example for the Kotlin starter waits until rollback ships, or is kept minimal. |
| Tomasz, other engineers | **Keep** `[ASSUMPTION]` | No contrary evidence. |
| Intern build-cache dashboard | **Keep** | Cheap and useful. Fold it into tooling that sits at parity. |
| Atlas (as an owned product) | **Off** | Outside the Hedgehog Concept. The aim is to place it elsewhere; this is not a verdict on its value. |
| One-off pipeline tweaks via interrupt | **Off** | They eat capacity. Route them through a weekly intake. |
| **Missing:** Payments design partner | **Add** | Someone who owns the compliance audit requirement and signs off acceptance criteria. |
| **Missing:** second legacy-plugin owner | **Add** | Removes the dependency on Bartek during the migration. |
| **Missing:** VP as sponsor of the outcome | **Add** | Turns headcount from "build Atlas" into "remove Payments deploy risk." |

**Leadership read (Ines):**
- **Strengths:** she points the window at others and the mirror at herself; she asked to be taken off the hero slide and credited the crew. She invites debate, and two dissenting views were voiced openly.
- **Gaps:** fierce resolve is unproven. The epic the biggest holdout customer asked for slipped three times under her, and the Atlas decision was handed to the team without framing the facts. Consensus without the brutal facts tends to choose what is exciting.
- **One behavior change:** at the planning offsite, open with the incident table and her own recommendation, then let the team challenge it. Lead with questions, but don't arrive with none.

## 5. Stop-doing list

1. **Don't take ownership of Atlas as offered.** Counter-offer: Runway publishes the service-ownership metadata it already holds as a feed that whoever builds a portal can use. Atlas can be revisited after the lighthouse migration lands.
2. **Stop using raw service count as the headline OKR.** Replace "80% of services" with tier-1 coverage plus rollback time. At the current pace of about +25 a quarter, 80% (265 services) is out of reach anyway, and it could be met or missed without touching the risk.
3. **Stop taking one-off pipeline tweaks as interrupts.** Run a weekly intake with a rotating owner. Each request becomes either a supported extension point or a clear no.
4. **Stop starting new starter kits and language templates** until rollback and the approval step ship.
5. **Stop carrying over epics.** Anything carried twice is either staffed with protected capacity or explicitly killed, and the decision is recorded.
6. **Stop muting alerts without a fix date.** A muted alert needs a ticket and an owner. The build-cluster disk alerts are this quarter's case.
7. **Stop treating legacy outcomes as "not our budget."** Owning those pipelines isn't required. Measuring their deploy outcomes is.

**Non-negotiable disciplines:** a rollback drill on a schedule (weekly once the feature ships `[ASSUMPTION]`); a blameless review of every deploy-caused Sev-1/2 on any pipeline, asking "would Runway have prevented or shortened this?"; one top priority per quarter.

**Framework and freedom:** the team doesn't negotiate on the Hedgehog Concept, the Q4 top priority, or the scorecard. Engineers have autonomy over how rollback and approval are designed, and over the 20% of time not committed to them `[ASSUMPTION split]`.

**Bureaucracy check:** Payments' manual sign-off is a compliance requirement (the card-network audit), not a rule that compensates for the wrong people. Build it into Runway rather than fight it.

**Tech triage (Gate 7):**

| Technology | Class | Note |
|---|---|---|
| Automated progressive rollout + fast rollback | **Accelerates** | The core of the flywheel |
| Auditable approval step ("approval as code" with evidence for audit) | **Accelerates; pioneer candidate** | Few internal platforms do compliant approvals well `[ASSUMPTION]` |
| Deploy-outcome instrumentation across all pipelines | **Accelerates** | Start lightweight, from deploy events and incident tracker tags |
| Feature flags | Accelerates, with care | Incident #3 was a flag misfire. Add guardrails. |
| Template v3, Kotlin starter, secret manager, build cache | Parity | Maintain, don't expand |
| Developer portal (Atlas) | Irrelevant to the Hedgehog | Flag: adoption driven by visibility and headcount, not by the team's core |

## 6. Brutal facts and the faith statement

| # | Fact | Evidence | Severity | Owner |
|---|---|---|---|---|
| 1 | The riskiest services aren't on Runway | 5 of 6 Sev-1/2s on legacy; both Sev-1s in Payments; card-auth-gateway twice (47 and 22 min to roll back) | Critical | Ines + Payments lead |
| 2 | The one feature the biggest holdout asked for keeps losing to visible work | Rollback epic slipped three quarters; Atlas would be a fourth deferral | Critical | Ines |
| 3 | Coverage gains may be entirely new services | Runway +25 net against 34 new; legacy −20. ~30 services retired across both pipelines, so the data can't show a single migration happened. `[inference]` | High | TPM |
| 4 | The team can't see the outcome it exists to improve | Legacy pipelines not instrumented; parked as "not our budget" | High | TPM / Bartek |
| 5 | Knowledge of legacy pipelines has a bus factor of one | Bartek is the only legacy plugin debugger | High | Ines |
| 6 | Red flags are being silenced | Two disk alerts muted, no fix yet | Medium | Bartek |
| 7 | Runway isn't risk-free either | Sev-2 from a feature-flag misfire on notifications | Medium | Mei |
| 8 | The case for Atlas is thin | One survey item (58%) plus one anecdote from a peer company; no cost estimate | Medium | VP / Ines |

**Truth climate:** good on candor, since the retro names the slip and dissent is voiced. The blind spot is structural: outcomes on legacy pipelines are out of sight by design. **Charisma check:** nobody's personality is suppressing bad news. The risk runs the other way: the team's collective enthusiasm for greenfield work is setting the priorities.

**Faith statement:** Runway already won 34 of 35 new services and cut lead time by 29%, and Payments has said in writing exactly what would bring it over. This team can earn that.

## 7. Core ideology and the BHAG

- **Core values:** safe by default; boring is a feature; earn adoption, don't mandate it; own outcomes, not tickets; blameless and evidence-first.
- **Core purpose:** let Brightwater change the software that moves people's money without fear.
- **BHAG** (kept to one line, because this is a team with a short planning horizon): *Every service that moves money at Brightwater ships through Runway, and no customer ever waits on a rollback.*
- **Clock-building mechanisms:** scheduled rollback drills; a cross-pipeline review of deploy incidents; OKRs tied to tier-1 measures; a rotation and written runbook for legacy plugins; a weekly intake for requests; a written charter with the Payments design partner.

## 8. Scorecard

| Output | Current | 12-month target | BHAG trajectory |
|---|---|---|---|
| Tier-1 money-moving services on Runway | **Unknown.** Payments appears to be mostly off Runway `[ASSUMPTION]` | card-auth-gateway plus ≥50% of Payments tier-1 services `[ASSUMPTION]` | 100% |
| Worst-case rollback time, deploy-caused Sev-1/2 | 47 min (legacy); Runway unknown | <5 min on Runway, drill-verified | <5 min everywhere |
| Deploy-caused Sev-1/2s per quarter, all pipelines | 6 (5 legacy) | ≤2 `[ASSUMPTION]` | Rare, and none on money paths |
| *Context only:* overall coverage | 64% (212/331) | Track, don't target | — |

## 9. Next 90 days

1. **Ines, before the offsite:** present the incident table and a recommendation. Decline owning Atlas. Ask the VP to put the two headcount on rollback, the approval step and the Payments migration, and offer an ownership-metadata feed for whoever builds a portal. If the headcount comes only with Atlas, decline both and say why.
2. **Mei + Sana (Bartek advising):** re-estimate rollback within one week, with no carry-over allowed. Ship rollback under five minutes on Runway with the majority of team capacity `[ASSUMPTION ≥50%]`, and stand up drills.
3. **TPM + Payments platform lead:** a written migration agreement covering the audit requirements for the approval step, card-auth-gateway as lighthouse, and acceptance criteria that won't move.
4. **TPM + Bartek:** instrument deploy outcomes for all pipelines (start from deploy events and incident tags); rewrite the Q4 OKRs around the scorecard; begin documenting legacy plugins in pairs.
5. **Bartek:** fix the build-cluster disk alerts and unmute them. **Rotating owner:** start the weekly intake for pipeline requests.

## 10. Re-check

I can set up a scheduled task about 90 days out, at the end of Q4 of Year 0. It would re-score the scorecard with real numbers and re-run Gates 1, 5 and 8. It would test in particular whether rollback shipped and whether card-auth-gateway moved.

## 11. Risk register

| Source | Risk | Early warning | Trigger for action |
|---|---|---|---|
| Gate 2 (CONDITIONAL) | Resolve gap: priorities set by consensus drift toward greenfield work | Rollback capacity is negotiated away in Q4 planning | Rollback below the majority of team capacity, or carried over a 4th time → Ines escalates to the VP |
| Gate 5 (CONDITIONAL) | Passion circle unconfirmed; Payments' commitment is verbal | Team vote favors Atlas; Payments adds new conditions | No signed Payments agreement by mid-Q4 → revisit the Hedgehog Concept |
| Gate 8 (CONDITIONAL) | Flywheel link 1 unproven | No drill-verified rollback by the end of Q4 | → loop back to Gate 5 |
| Decline stage 2 (primary) | Undisciplined pursuit of more: Atlas, starter kits | New initiatives appear in the plan before rollback ships | Any new owned product before the lighthouse migration → stop and review |
| Decline stage 3 (primary) | Denial of risk: legacy outcomes out of sight, alerts muted, single bus factor | Another Payments Sev-1 on legacy; Bartek unavailable during an incident | Any Sev-1 with rollback over 10 min `[ASSUMPTION]` → joint review with Payments within one week |
| Decline stage 1 | Hubris: "crossed 200" celebrated while risk sits elsewhere | Retro wins are counts, not outcomes | Headline metric reverts to coverage |
| Decline stage 4 | Grasping: after a major incident, a mandated migration or a platform rewrite | Calls for "force everyone onto Runway" | Any mandate before Runway meets Payments' conditions |
| Decline stage 5 | Capitulation: Payments builds its own platform | Payments staffs pipeline work of its own | Any Payments platform headcount request |

## 12. Gate log

*Evidence note:* no memory, past-chat or web search was available in this session, so there is no prior baseline and no external research. The run uses the dossier alone.

| Gate | Verdict | Note |
|---|---|---|
| 0 Fit | PASS | Ongoing team; steward is Ines (EM) under the VP; multi-year horizon; measurable outcomes |
| 1 Baseline | PASS | Good, not yet great: strong on new services, absent from the riskiest services |
| 2 Level 5 Leadership | CONDITIONAL | Humility strong, resolve unproven; condition: rollback gets protected Q4 capacity |
| 3 First Who | PASS | Right people; seats need reallocation; Bartek bus factor logged under Gate 10 |
| 4 Brutal Facts | PASS | Facts sharpen Gate 1 and don't contradict it |
| 5 Hedgehog | CONDITIONAL | Passion circle and Payments' commitment unconfirmed |
| 6 Discipline | PASS | Seven specific stop-doing items |
| 7 Technology | PASS | Rollback and the approval step accelerate; Atlas irrelevant |
| 8 Flywheel | CONDITIONAL | Loop closes; first link unproven for three quarters |
| 9 Built to Last | PASS | BHAG kept to one line |
| 10 Mighty Fall | PASS | Stages 2 and 3 lead the register |

Of 11 gates, 8 are PASS, 3 are CONDITIONAL and none FAIL. All three CONDITIONALs share one root cause: the rollback and approval work keeps losing to more visible projects.