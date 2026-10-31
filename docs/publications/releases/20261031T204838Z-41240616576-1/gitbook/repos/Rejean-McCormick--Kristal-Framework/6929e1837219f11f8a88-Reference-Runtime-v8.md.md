<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Reference-Runtime-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 055af56566cf1b8298247752dcacd3e2ce536519b5dfbef617b56782e73e54d8 -->

# Reference Runtime v8

> **v9 note:** This page describes the v8 reference surface. The inherited reference runtime also implements v9 state/commitment/lifecycle behavior; see [[Reference-Runtime-v9]] and [[Reference-Runtime-v10]].


The repository includes a **non-normative JavaScript reference runtime** targeting Kristal v8.0.0. The specification, schemas and TCK remain authoritative for conformance.

## Implemented profiles / behavior

The current reference runtime demonstrates local behavior for:

- **V8-Reader** — v6, v7 and v8 artifact detection/adaptation without rewriting inherited artifacts;
- **V8-Language** — BCP 47 parsing, deterministic lexicon-stack precedence, explicit missing/conflict handling;
- **V8-Query** — exact identity lookup, neighborhood, semantic traversal, evidence closure, semantic slices and unknown-root inspection;
- **V8-AI-Context** — deterministic semantic-atom selection, byte budgets, optional token estimates and `symbol_table_v1` compact payloads;
- **V8-Integrity** — inherited byte fingerprints plus a documented reference semantic-fingerprint profile;
- rebuildable query indexes for identity, incoming/outgoing edges, predicate use, assertions and evidence.

## Current federation boundary

The reference runtime **does not claim remote `V8-Federation` transport conformance**. It can query multiple local source artifacts, but remote shard coordination/availability is intentionally not simulated and its advertised capability reports federation as unavailable.

## Key commands

```text
inspect-artifact
v8-capabilities
semantic-fingerprint
resolve-lexicon
query-v8
build-query-index
compile-ai-context
```

The runtime validates, adapts, indexes, queries and projects. It does not define factual truth, legal authority, organizational policy or execution permission.
