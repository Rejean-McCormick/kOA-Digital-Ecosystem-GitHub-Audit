<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/reliability.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 80636a179179f34205c0394526ac964db107dc6cffad68b7d6de7641b67caf6a -->

# Reliability

Reference semantics: **at-least-once delivery + idempotent processing + reconciliation**.

`idempotency_key` identifies the logical effect. `request_fingerprint` identifies the semantic request content.

```text
same key + same fingerprint      => replay, no new effect
same key + different fingerprint => IK_IDEMPOTENCY_CONFLICT
```

Fingerprint profile: `ik.request-fingerprint/jcs-rfc8785+sha256/v1`.

Semantic projection includes class/profile/source/target/subject/operation/authority/data_schema/data/governance/artifact_refs/evidence and excludes id/time/correlation/causation/trace/response/delivery metadata.

## Commit and emission boundary

IK does not require a distributed transaction across participants. The authoritative participant commits its own domain state locally, then durably emits the corresponding cross-boundary interaction. An Event MUST describe a fact already committed by its publisher.

Where available, use a transactional outbox or equivalent durable emission boundary so the local state transition and intent to publish are committed together. Remote acceptance/completion is reconciled asynchronously through idempotency, Receipts, Events and redrive.

Orgo reuses its existing `IntegrationOperation`, `OutboxMessage` and worker. Konnaxion adds or reuses an equivalent durable emission boundary.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md).
