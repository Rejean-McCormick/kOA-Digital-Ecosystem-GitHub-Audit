<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0003-typed-semantic-graph-and-obligations.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 8d47a55d409cbc27398ce090d3742fe2d28326294d545d4977d3188c7e0a4dec -->

# ADR-0003 — Canonical semantic graph plus explicit obligations

Status: **accepted**

## Context

Key/value SemanticItem models leak domains and blur support metadata with must-say content.

## Decision

Use a typed structural SemanticGraph with extensible predicate/role vocabulary plus a separate CommunicationObligation set and supporting context.

## Consequences

Core remains domain-neutral and scalable while retaining explicit coverage.
