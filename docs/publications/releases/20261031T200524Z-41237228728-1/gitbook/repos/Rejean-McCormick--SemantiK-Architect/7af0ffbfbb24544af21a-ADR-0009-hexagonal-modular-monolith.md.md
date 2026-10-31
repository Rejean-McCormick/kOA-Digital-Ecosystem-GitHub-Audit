<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0009-hexagonal-modular-monolith.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 5712729c296d2c62d559208892773646c0e798f42026336fe5eb150b0fd4fe95 -->

# ADR-0009 — Hexagonal modular monolith

Status: **accepted**

## Context

SA needs strong boundaries but not distributed-system complexity.

## Decision

Use ports/adapters plus strict modules in one default package/process.

## Consequences

Easy testing/maintenance; distributed deployment remains possible later behind ports.
