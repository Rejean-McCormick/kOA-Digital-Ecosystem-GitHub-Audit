<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Build-Publish-Activate-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 3b0dae201ce74442a2ac776ec10ba2cea0ad163885e7115d3a7ae7699f3deee6 -->

# Build / Publish / Activate

V9 separates three lifecycle operations:

```text
BUILD != PUBLISH != ACTIVATE
```

## BUILD

Produces candidate Logical Artifacts and materializations from declared Derivations.

BUILD does not change the active state.

## PUBLISH

Validates candidates and creates an immutable State Snapshot.

Recommended order:

```text
1. write physical blobs
2. verify blob digests
3. write materialization manifests
4. reconstruct/verify logical commitments
5. construct immutable State Snapshot
6. validate snapshot
7. publish snapshot
```

## ACTIVATE

Moves a mutable channel pointer such as `production` or `HEAD` to a published immutable snapshot.

```text
production → S42
```

may atomically become:

```text
production → S43
```

S42 remains unchanged.

## Crash consistency

A failure before activation must leave the previous active state usable. Unreferenced candidate blobs may later be garbage-collected.

## Concurrent publication

A publisher may use compare-and-swap semantics against the expected previous commitment. A pointer conflict is not automatically a semantic conflict.

```text
STORAGE CONFLICT != SEMANTIC CONFLICT
```

## Rollback

Rollback selects a retained prior immutable snapshot. It does not rewrite history to pretend the newer snapshot never existed.
