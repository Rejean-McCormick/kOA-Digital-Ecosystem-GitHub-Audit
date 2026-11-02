<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0008-composed-immutable-runtime-set.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 357900edce2a60754fa1507df0913a6947d323dffbb51d78462d9dfe8841d033 -->

# ADR-0008 — Composed immutable RuntimeSet

Status: **accepted**

## Context

One copied monolithic pack per language would duplicate large shared artifacts and complicate 300-language scaling.

## Decision

A RuntimeSet pins hashes of grammar, lexical, locale, capability and conformance artifacts.

## Consequences

Resources can be shared while requests remain reproducible and immutable.
