<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Architecture-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: a6291eba909f9e51f033e12dbcf52eacd3ca2e292b51760930ae20fcfdc751ea -->

# v9 Architecture

## Layer model

```text
                 ┌────────────────────────┐
                 │   LOGICAL STATE        │
                 │ immutable snapshot     │
                 │ logical artifacts      │
                 │ pinned references      │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │   DERIVATION GRAPH     │
                 │ declared inputs        │
                 │ transforms / policies  │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ MATERIALIZATION LAYER  │
                 │ manifests / segments   │
                 │ dictionaries / codecs  │
                 └───────────┬────────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              ┌──────────┐      ┌──────────┐
              │ EXCHANGE │      │ RUNTIME  │
              │ portable │      │ optimized│
              └──────────┘      └──────────┘
```

## Logical state

The logical state defines **what logical content participates in a snapshot**. It is not defined by segment boundaries, compression or storage URI.

## Derivation graph

Derivation records explain how artifacts were computed from declared inputs. Build provenance does not become epistemic authority.

## Materialization layer

A logical artifact may have one or several physical representations:

```text
inline JSON
native blob
segmented JSONL
columnar representation
encrypted envelope
runtime database
```

The selected profile is explicit.

## Exchange

Exchange packages state descriptors, materialization manifests and blobs for portable distribution. Two different Exchange packages may represent the same logical state.

## Runtime

Runtime packs, indexes and caches optimize access. They must identify their source logical commitments and remain rebuildable when the profile claims reconstructability.

## Anti-corruption boundary

A storage engine cannot redefine domain semantics. An ordered AST remains ordered. A graph can remain cyclic. A local dictionary integer never becomes semantic identity.

See [[Logical-Artifacts]], [[Materialization-v9]] and [[Exchange-and-Runtime-v9]].
