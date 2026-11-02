<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/upgrades/orgo.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: b9748f6e754c38512bad462a30e68abbff86bfd9ac5ff8ccb57b7ee29e54eaae -->

# Orgo upgrade

Reuse existing infrastructure rather than duplicating it:

- `IntegrationOperation` → IK semantic operation projection;
- `OutboxMessage/OutboxWorker` → IK-Reliable delivery implementation;
- inbound `governance.decision.execute` → idempotent Signal → published WorkflowVersion → Case/Tasks;
- `ArtifactLink` projection only, not artifact ownership;
- `OrgoExport v1` as a source-owned snapshot/export boundary;
- Kristal adapter routes through DaaT;
- reuse/upgrade existing kOA BuildRecord/ReleaseRecord contracts.

Orgo remains authoritative for its mutable operational state. IK/DaaT/Kristal integration MUST NOT require direct mutation of Orgo's database by another participant or a distributed commit spanning Orgo and Kristal. Cross-boundary effects use the existing durable outbox, idempotency and reconciliation model.

Reference mapping: [`adapters/orgo-typescript/`](../../adapters/orgo-typescript/).

See [ADR-IK-05](../adrs/ADR-IK-05-operational-state-artifact-boundary.md).
