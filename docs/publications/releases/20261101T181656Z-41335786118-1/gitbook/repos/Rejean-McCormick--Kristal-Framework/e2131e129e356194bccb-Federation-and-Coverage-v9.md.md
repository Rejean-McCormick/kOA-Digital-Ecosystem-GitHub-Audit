<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Federation-and-Coverage-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 4ea484f11b552c00c2f064c18b7ee6b6ecdbd376b414e3c795dd2f8f2c4926d9 -->

# Federation and Coverage

V9 federation composes independently governed logical states without requiring content duplication.

## Shard versus segment

A **shard** is a semantic/governance/lifecycle boundary.

A **segment** is a physical storage boundary.

```text
SHARD != SEGMENT
```

A small course Kristal can be an independent shard stored in one file. A huge Pokémon shard can be one semantic unit represented by hundreds of segments.

## Pinned child references

A parent may pin child states:

```text
University State
  ├─ child A @ commitment X
  ├─ child B @ commitment Y
  └─ child C @ commitment Z
```

The parent does not need to copy the child canon.

```text
REFERENCE != OWNERSHIP TRANSFER
```

## Federated update

If child `C1` becomes `C2`, an already-published parent does not silently change. A new parent snapshot must explicitly adopt the new child commitment.

## Coverage

A local Exchange/Runtime may carry only part of a state. Coverage metadata distinguishes local availability from logical absence.

```text
NOT PRESENT LOCALLY != LOGICALLY ABSENT
PARTIAL AVAILABILITY != NEGATION
```

The v8 query layer remains responsible for communicating `complete`, `partial`, `unknown`, continuation and omission semantics to query consumers.
