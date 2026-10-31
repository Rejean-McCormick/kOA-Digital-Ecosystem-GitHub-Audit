<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Integration-Orgo-Konnaxion | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: 7ae280dce4e1dd7b93e06a53d48445546d2045bc0973d0b1c81e48aae05dad39 -->

# Integration — Orgo ↔ Konnaxion

The target direct protocol between Konnaxion and Orgo is the **Interaction Kernel (IK)**.

## Konnaxion → Orgo

A finalized Konnaxion DecisionRecord may be handed to Orgo through:

`governance.decision.execute/1.0.0`

The DecisionRecord remains Konnaxion-owned. Publication does not by itself imply execution; the Profile and governance authority context express execution intent.

## Orgo → Konnaxion

Operational impact/accountability publication maps to:

`accountability.impact.publish/1.0.0`

Orgo uses its IntegrationOperation/outbox reliability mechanisms. Konnaxion remains owner of Konnaxion persistence and authorizes its own state transition.

## Implementation status

Historical Orgo→Konnaxion bridge evidence exists, but current Konnaxion canonical documentation does not claim the full external adapter set as active/conformant. The direct finalized DecisionRecord→Orgo path remains migration/conformance work.

See [Interaction Kernel](Integration-Interaction-Kernel) and [Status](Status).
