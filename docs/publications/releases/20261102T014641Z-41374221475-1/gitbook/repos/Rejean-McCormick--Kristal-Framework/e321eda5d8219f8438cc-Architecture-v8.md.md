<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Architecture-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 0086e14f1594b63a81952d43c9e409de62c59f0df49c40721e98db036871e96e -->

# v8 Architecture

> **v9 note:** This page documents the preserved v8 language/query architecture. V9 adds representation-independent logical state below/around these read capabilities. See [[Architecture-v9]].


## Layer model

```text
                 canonical / authoritative
┌─────────────────────────────────────────────────────┐
│ v6 portable state + v7 semantic registries / Mesh  │
└─────────────────────────────────────────────────────┘
               │                         │
               │                         │
       lexical companions          derived read models
               │                         │
        Language Resolver          KQP Query Engine
               │                         │
               └──────────┬──────────────┘
                          │
                   Context Compiler
                          │
                 human / AI projections
```

v8 uses a CQRS-like separation: canonical state is optimized for integrity and semantic fidelity; derived read models are optimized for lookup, query and presentation. This does **not** require asynchronous infrastructure or a particular database.

## Anti-corruption boundaries

Adapters isolate v6, v7 and external KOS formats from v8 query internals. External identifiers remain mappings; legacy fields are not silently reinterpreted to simplify implementation.

## Federation and sharding

Large semantic or lexical universes may be sharded by subject, jurisdiction, organization or operational locality. Sharding is an operational partition: **semantic identity remains stable across shards**.

## Derived material

Unless an inherited contract says otherwise, these are read-side material:

- query/search/vector indexes;
- lexical-resolution caches;
- semantic slices;
- AI context bundles;
- compact symbol tables;
- query plans;
- rendered human views.

Derived material must remain traceable to source state/snapshot.

## Graceful degradation

- missing lexicon → preserve semantic ID;
- unavailable index → slower exact query or explicit unsupported operation;
- unavailable shard → partial result with missing-shard disclosure;
- exhausted budget → truncated result with continuation/omission metadata;
- unavailable tokenizer → bytes/items remain authoritative and token estimate is omitted or marked heuristic.

No degradation path may fabricate semantic content.
