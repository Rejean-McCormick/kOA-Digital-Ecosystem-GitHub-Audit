<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/State-Snapshots-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: e3431501ea955f4a3e99aef2e72e2d3aa8248ae1e048c8a0fa0f81ad64ae5a15 -->

# State Snapshots

A v9 **State Snapshot** is an immutable logical composition.

```text
STATE SNAPSHOT IS IMMUTABLE
```

A logical mutation creates a new snapshot; an existing published snapshot is never edited in place.

## Members and references

A snapshot can contain:

```text
owned logical members
+
pinned external references
```

Owned membership does not require all members to share the same payload shape.

Pinned references allow federation without copying child canon.

## No mutable membership

Selectors such as:

```text
HEAD
main
current
latest
```

may be used during discovery/build, but a published snapshot must resolve them to exact immutable commitments.

## Parent lineage

Parent references record history/lineage. In the baseline v9 content-commitment profile, operational lineage is separate from logical content identity.

Two independently produced snapshots may therefore have the same logical content commitment while retaining different histories.

## Membership removal is not erasure

If artifact `A` is present in snapshot `S1` and absent in `S2`, v9 does not imply that `A` never existed, was physically deleted, or was epistemically retracted. Those are separate domain/lifecycle operations.

See [[Build-Publish-Activate-v9]] and [[Federation-and-Coverage-v9]].
