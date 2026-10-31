<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/upgrades/konnaxion.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: f242ac2e59542c73501ff6bc7bb6984aedfc3851dc1306f1155e0506e1f3c134 -->

# Konnaxion upgrade

Preserve the existing `orgo_bridge_*` J30 implementation and `OrgoImpactPublication`. Wrap it with the IK Profile `accountability.impact.publish` first.

Add:

- IK inbound/outbound adapter boundary;
- immutable `DecisionRecord` contract/read-model;
- durable emission port tied to DecisionRecord finalization;
- `KonnaxionExport v1` as a source-owned snapshot/export boundary;
- ArtifactRef support;
- RuntimePackActivationPort delegation (kOA-Linux owns host activation when present).

Konnaxion remains authoritative for its mutable governance/civic operational state. IK and Kristal artifacts may project or reference that state, but do not replace the Konnaxion system of record. Konnaxion↔Orgo remains direct unless a Profile explicitly requires a Kristal artifact.

The reference compatibility adapter is in [`adapters/konnaxion-python/`](../../adapters/konnaxion-python/).

See [ADR-IK-05](../adrs/ADR-IK-05-operational-state-artifact-boundary.md).
