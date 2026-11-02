<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Components.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 575a4ed6a0c6d50f5fa19d4fa71a68fb7e8e8fd1877955d779e81a3c91f84016 -->

# Components and systems

| System / boundary | Owns | Does not own |
|---|---|---|
| **Konnaxion** | civic/public state, DecisionRecord, readings, product state | Orgo work state, Kristal State, Runtime Pack active state |
| **Orgo** | Signal, Workflow, Case, Task, IntegrationOperation, outbox/reconciliation | Konnaxion civic outcomes, Kristal recognition, host privilege |
| **EncyKlopedia** | source discovery/acquisition, provider resolution, immutable evidence and corpus-harvest handoff | epistemic validation/recognition, Moodle projections |
| **Da’at** | mapping/ACL at the Kristal integration boundary | source state, Kristal core semantics/authority |
| **Kristal** | Referent Registry semantics, Kristal State, valuations/coordinates/applicability, validation/recognition, Reader Policy, record-role/actionability semantics, derived knowledge-runtime semantics | source acquisition, platform Release Set, Moodle materialization |
| **UCKK / Univers-Cité** | scoped consumer projections, Moodle/campus state, derived glossary/media presentation, local Assembly decisions | Kristal assertions/referent authority, Konnaxion civic state, host privilege |
| **kOA-Linux** | platform profiles, trust/policy/resources, artifact admission, release channels, lifecycle contracts | subsystem business semantics |
| **`kristal_runtime`** | Runtime Pack verification/compatibility state, active Runtime Pack record, activation/rollback receipts, runtime health | governance policy, resource scheduling, host privilege, workflow state |
| **kOA Node Agent** | narrow node-local privileged lifecycle/activation/recovery operations | release authority, epistemic authority, business authority |
| **Koali Spaces** | optional presentation composition, routing, shell, Space activation and admitted surfaces | product business authority, Kristal authority, host privilege |
| **Interaction Kernel** | envelope/Profile/reliability semantics where adopted | participant state; universal transport authority |
| **SemantiK Architect** | language planning/realization, SA↔GF contract, RuntimeSet/capability/conformance semantics | civic/workflow/epistemic authority |
| **SemantiK Runtime Orchestrator** | RuntimeSet release sequencing, promotion/rollback and activation ordering | grammar, SA semantics, diagnostic truth |
| **SenTient** | candidate extraction/resolution/reconciliation | reference recognition or activation authority |

## No global control plane

No system automatically controls every ecosystem transition. Acquisition, workflow, epistemic state, consumer projection, release coordination, Runtime Pack active state, privileged host operations and presentation state remain separate ownership domains.

## kOA-Linux composition

kOA-Linux is the operational composition root for selected profiles. Independent applications remain removable and independently authoritative. Hosting a subsystem does not transfer its domain authority to kOA-Linux.

## Additional mapped applications (not core authority owners)

| **Skope** | Local Wikidata selection/scope recipe and noncanonical working export | Kristal epistemic authority, EncyKlopedia source-custody authority, platform admission |
| **Ékole** | Pedagogical authoring, catalogue, learner/teacher/operations local surfaces and derived projections | Kristal v9/v10 qualification, global source acquisition, live Moodle authority without an explicit bridge |

For evidence, local port overlap and candidate handoffs see [Skope & Ékole](Components-Skope-and-Ekole.md).
