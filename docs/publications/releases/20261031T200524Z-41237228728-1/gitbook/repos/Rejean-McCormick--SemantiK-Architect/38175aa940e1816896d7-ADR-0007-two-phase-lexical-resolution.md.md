<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0007-two-phase-lexical-resolution.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 4289a39d0f5c831c20311383a416618f40baa9a806171fe75a0a0d4067a7a48f -->

# ADR-0007 — Two-phase lexical knowledge and binding

Status: **accepted**

## Context

Construction choice may depend on lexical properties, while morphology belongs to GF.

## Decision

Resolve lexical planning facts before LanguagePlan; bind exact runtime lexical entries after operation selection.

## Consequences

Planning has required information without duplicating morphology.
