<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0001-single-canonical-architecture.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 39d8d4fb8fe2e08c286b59d22bef718f721c515bb18c24e8ba4f2c6c2c18e1e7 -->

# ADR-0001 — Single canonical architecture

Status: **accepted**

## Context

The previous SA contains useful ideas and validated behavior but also architecture that must not constrain the new design.

## Decision

The repository has one canonical runtime contract and no alternate compatibility layer.

## Consequences

A single canonical architecture keeps implementation and conformance unambiguous.
