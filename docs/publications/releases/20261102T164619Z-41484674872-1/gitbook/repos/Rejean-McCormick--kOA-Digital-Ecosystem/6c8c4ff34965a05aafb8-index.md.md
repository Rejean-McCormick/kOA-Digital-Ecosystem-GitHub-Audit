<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/interaction-kernel/index.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 176dc3810678ad1467eba8fba0e5f52de003581aa558b271d21042670afc23e4 -->

# Interaction Kernel integration

**Protocol authority:** Interaction Kernel owner contracts

Interaction Kernel (IK) is a distributed cross-system protocol/Profile layer. It is not a central server, participant database or Kristal artifact store.

## Core protocol

Business classes: `command`, `query`, `event`. Protocol records include receipts/query results; boundary objects include ArtifactRef and ExportManifest.

ArtifactRef never transfers ownership, authority or validation status. ExportManifest identifies immutable boundary material; it is not permission to mutate the source database.

## Reliability

Reference semantics are at-least-once delivery + idempotent processing + reconciliation.

```text
same key + same semantic fingerprint       => idempotent replay
same key + divergent semantic fingerprint  => conflict / fail closed
```

## Current adopted/frozen profiles

Qualified Konnaxion↔Orgo:

- `governance.decision.execute/1.0.0`
- `accountability.impact.publish/1.0.0`

Current knowledge-contract baseline:

- `kristal.build.request/2.0.0`
- `kristal.artifact.ready/2.0.0`

Other profiles exist only where their owning boundaries explicitly adopt them.

## Architecture rules

- Konnaxion↔Orgo is direct by default; Kristal is not an automatic hop.
- Da’at is the mapping/ACL boundary for IK-facing Kristal work.
- participant owners commit mutable state locally; IK does not require distributed cross-owner DB transactions.
- source-owned exports remain source-owned.
- Profile/schema versions used for conformance are explicit and immutable within their published version.

- `kristal.revision.request/2.0.0` is the aligned v6 revision boundary.
