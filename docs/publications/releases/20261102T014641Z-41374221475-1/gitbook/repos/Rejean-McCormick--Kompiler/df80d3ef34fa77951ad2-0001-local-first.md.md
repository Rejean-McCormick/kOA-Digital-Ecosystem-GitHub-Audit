<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/ADR/0001-local-first.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: 72a260dd8a6f9c898faeb25cff9f646d4a1036a7632592d278902a3522b3474f -->

# ADR 0001 — Local-first Runtime

## Status

Accepted.

## Decision

The reference Kompiler runtime executes locally and does not require GitHub, cloud storage, or a hosted service.

## Rationale

- Kristals can be large and already exist locally.
- Clipboard/file transport is sufficient for the core LLM workflow.
- Local execution improves privacy and removes network latency/dependencies.
- Future direct integrations can use the same protocol over a different transport.

## Consequences

Remote/federated adapters remain possible but are optional and must declare network behavior.
