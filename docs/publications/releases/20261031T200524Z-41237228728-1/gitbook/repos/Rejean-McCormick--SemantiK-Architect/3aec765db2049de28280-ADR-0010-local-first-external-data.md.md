<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0010-local-first-external-data.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 929ad1041fe5ce3309b5f1ce7a81b83b8ad692a7da53082dda152b93dfe08405 -->

# ADR-0010 — Local-first external data and Wikimedia interoperability

Status: **accepted**

## Context

The ecosystem uses Wikidata concepts but must not require live Wikimedia services.

## Decision

Support local mirrors and namespace-qualified references; Wikimedia-specific protocols remain adapters.

## Consequences

Offline operation and interoperability coexist without unnecessary rewriting.
