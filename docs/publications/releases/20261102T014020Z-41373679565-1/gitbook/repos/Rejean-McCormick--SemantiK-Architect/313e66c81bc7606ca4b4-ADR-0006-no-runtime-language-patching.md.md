<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0006-no-runtime-language-patching.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: dd85fa0cea47969418c40ccbc507bae7342ed9d839e86bd3f32f7177d52e2c49 -->

# ADR-0006 — No runtime language patching or hidden fallback

Status: **accepted**

## Context

Fallback renderers hide underdeveloped grammar and produce false success.

## Decision

Only released language/profile artifacts may serve production. Grammar gaps are fixed in the GF language repository and revalidated.

## Consequences

Failures are explicit; no family-engine/safe-mode duplicate grammar.
