<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Operations | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 74acdc6e0aa2e7a31f2f935200b4616d8140aa53a654dacc3c58b195fd20861e -->

# Operations

Operating Kristal v9 means protecting logical meaning, compatibility, immutable publication and query completeness as carefully as byte integrity.

## Monitor

- blob-digest failures;
- Logical Commitment mismatches;
- stale Runtime Packs/indexes against source State commitment;
- unsupported contract/profile versions;
- semantic identity resolution failures;
- mutable/unpinned references in publication candidates;
- derivation inputs that are not pinned;
- missing provenance/evidence;
- applicability/value-state drift;
- lexical missing/conflict rates;
- query partial/truncated rates and causes;
- unavailable shards/segments;
- activation compare-and-swap conflicts;
- rollback/revocation policy violations;
- accidental promotion of read/model output to authority.

## Operational invariants

```text
STATE SNAPSHOT != HEAD
BUILD != PUBLISH != ACTIVATE
READ MODEL != CANONICAL STATE
PARTIAL RESULT != NEGATIVE RESULT
STORE WRITE != PUBLISH AUTHORITY != ACTIVATE AUTHORITY
```

## Release shape

Prefer:

```text
candidate blobs
→ verified materializations
→ immutable State Snapshot
→ publication
→ atomic activation
```

The active pointer moves last.

See [[Build-Publish-Activate-v9]], [[Operations-Release-Strategy]] and [[Operations-Observability-and-Troubleshooting]].
