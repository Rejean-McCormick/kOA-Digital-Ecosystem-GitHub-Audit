<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0011-deterministic-fail-closed-runtime.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 21231b13bb6a76c86aa59b45990650a1fc8ce9162446790b0269d9c6af8c77a4 -->

# ADR-0011 — Deterministic fail-closed production runtime

Status: **accepted**

## Context

Wrong meaning/language is more damaging than explicit failure.

## Decision

Canonical runtime is deterministic and fails closed on semantic/language/runtime correctness errors; graceful degradation is auxiliary-only.

## Consequences

Reproducible, auditable behavior; fewer hidden surprises.
