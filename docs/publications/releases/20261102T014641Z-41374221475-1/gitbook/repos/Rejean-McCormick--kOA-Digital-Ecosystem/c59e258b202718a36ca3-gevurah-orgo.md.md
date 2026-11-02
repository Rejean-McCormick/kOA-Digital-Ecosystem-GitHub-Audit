<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/20-nodes/gevurah-orgo.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 10e8231f609f6cdf1ac0a9a1148e3c786ecff2b648a7ce7f95d3604e965b280d -->

# Gevurah — Orgo workflow and operational boundary

Orgo owns governed work represented as Signals, WorkflowVersions, Cases, Tasks and IntegrationOperations. It is **not** the universal control plane for Konnaxion decisions, Kristal epistemic states or kOA-Linux host activation.

## Responsibilities

- persist/normalize accepted Signals;
- evaluate published WorkflowVersions deterministically;
- create/update Orgo-owned Cases and Tasks;
- route internal actions through Orgo domain services;
- represent durable external effects as IntegrationOperations;
- deliver external effects through durable outbox/worker infrastructure;
- preserve correlation/idempotency and reconcile terminal receipts;
- record operational evidence and audit for Orgo-owned state.

## Konnaxion boundary

A finalized Konnaxion DecisionRecord can request governed work through the Interaction Kernel `governance.decision.execute` Profile. Orgo validates/adopts the request and mutates only Orgo state.

Operational impact can be published back using `accountability.impact.publish`.

## Kristal boundary

Orgo can request Kristal work through an IK Profile routed to Da’at. Orgo does not reinterpret validation, valuation, authority recognition or Reader Policy.

## Invariants

```text
Case status         ≠ Konnaxion decision status
Task status         ≠ Kristal assertion status
IntegrationOperation status ≠ Task status
accepted            ≠ succeeded
```
