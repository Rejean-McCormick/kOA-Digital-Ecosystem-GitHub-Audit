<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Components-Orgo | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: 815ef542f31dcb27badd44595f58ce7fa58d3ae025a98804793fa54f70ac6939 -->

# Orgo

Orgo is the **operational/workflow system** of the kOA ecosystem. It owns work represented inside Orgo: Signals, WorkflowVersions, Cases, Tasks, IntegrationOperations and its outbox/retry state.

It is not a global ecosystem control plane. Konnaxion retains civic/governance state, Kristal retains epistemic artifacts and policies, and kOA-Linux retains local host activation when deployed.

## Responsibilities

- accept governed work inputs through explicit integration contracts;
- authorize and execute Orgo-owned workflows;
- persist Cases, Tasks and IntegrationOperations;
- make external effects reliable through outbox/idempotency/reconciliation;
- expose operational status without taking ownership of source-system domain state.

## Interaction Kernel

The target ecosystem protocol is Interaction Kernel (IK).

- `governance.decision.execute/1.0.0`: Konnaxion DecisionRecord/authority context -> Orgo governed-work input;
- `accountability.impact.publish/1.0.0`: Orgo execution impact -> Konnaxion accountability/read model;
- Kristal-related work uses IK Profiles toward Da'at; Da'at translates at the Kristal boundary.

The current Orgo documentation defines a generic Orgo-owned integration bridge. That bridge is compatible with the architecture, but its existence does **not** by itself prove that a native Konnaxion or Kristal adapter is implemented or conformant.

## Kristal v5 gating

Orgo must not impose the old universal `validation PASS -> compile` rule. Kristal v5 separates:

1. compilation;
2. validation/review;
3. authority recognition;
4. publication/distribution;
5. activation.

A Working Exchange can exist before final validation or recognition where the active policy permits. A kOA production Profile may impose stricter gates on **reference publication, release or activation**; those are policy gates, not a universal Kristal compile rule.

## Reliability

Cross-system delivery is at-least-once with idempotent processing and reconciliation. `accepted` is not equivalent to `succeeded`. Same idempotency key with different request content is a protocol conflict.

## Ownership boundary

Orgo may request external actions, but the receiving system owns its own state transition. No integration grants Orgo direct writes into another system's database or authoritative state.
