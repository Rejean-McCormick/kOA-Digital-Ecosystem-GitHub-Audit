<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/core-protocol.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 8ca58e33c7534c96b8f855c33e1bb50a0569f8844208c68f99b5218c0418a9c6 -->

# Core protocol

Business classes are only `command`, `query`, and `event`.

- **Command**: asks a receiver to evaluate and possibly mutate receiver-owned state.
- **Query**: asks for a projection/read.
- **Event**: announces a fact already committed by the publisher.

Protocol records are `Receipt` and `QueryResult`. `accepted` does not mean `succeeded`.

Boundary value objects are `ArtifactRef` and `ExportManifest`. There is no separate `ArtifactOutcome`; artifact results are expressed by Receipt + Event + ArtifactRef.

## State ownership rule

IK never makes the transport envelope the system of record for business state. Commands may cause receivers to mutate receiver-owned state; Events are emitted only after the publisher's claimed fact has been committed locally.

Cross-owner effects are not one distributed transaction. They are coordinated through durable emission, idempotent admission, Receipts/Events and reconciliation.

`ExportManifest` and `ArtifactRef` expose immutable/versioned boundary artifacts without granting write access to the owner's database.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md).
