<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/Components-Orgo.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: b295f3b105b32ca1dfc8fb3ffcc92e833d2a85fcde1ab77db1b5a533cd5ab629 -->

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

## Kristal v6 gating

Orgo must not impose the old universal `validation PASS -> compile` rule. Kristal v6 separates:

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
