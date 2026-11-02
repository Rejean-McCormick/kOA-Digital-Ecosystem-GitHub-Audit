<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/ADR/0003-kristal-v6-semantics.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: 1aaaebf1c4c37a4bf830d0a8e568925bfa85595686e6b4d5502e8df398ee06cb -->

# ADR 0003 — Kristal v6 Semantics Are First-class

## Status

Accepted.

## Decision

The common normalized model preserves v6 valuations, record roles, actionability, coordinates/applicability, provenance, validation, authority recognition, and state identity where present. v5 is supported through explicit legacy fields/mapping profiles.

## Rationale

Flattening these dimensions into generic `confidence` or `fact` fields would destroy information and can create false authority.

## Consequences

The Context Pack schema is richer than a conventional RAG result list. Cross-version mappings must be explicit and versioned.
