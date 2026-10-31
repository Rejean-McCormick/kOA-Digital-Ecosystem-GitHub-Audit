<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0005-versioned-sa-gf-bridge.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: a3c0adf71908fd8616927f6da8ddebe6c3458b6119606c40fea18d175a67f390 -->

# ADR-0005 — Versioned SA↔GF bridge contract

Status: **accepted**

## Context

Direct coupling to arbitrary GF/RGL AST details would create unstable per-language integration.

## Decision

SA targets a thin versioned operation catalog/bridge grammar; only the GF adapter uses PGF.

## Consequences

GF remains grammar authority; SA gains stable multi-language integration and conformance.
