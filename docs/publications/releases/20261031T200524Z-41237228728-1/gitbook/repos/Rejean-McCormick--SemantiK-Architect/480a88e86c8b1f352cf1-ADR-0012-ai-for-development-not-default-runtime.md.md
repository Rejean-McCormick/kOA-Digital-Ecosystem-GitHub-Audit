<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0012-ai-for-development-not-default-runtime.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: de0895e4c0c2e29fe20f2eeaa1a09735f924997643fd3a4497733f9c6e3da853 -->

# ADR-0012 — AI assists development; deterministic path remains default runtime

Status: **accepted**

## Context

AI accelerates GF language/lexicon/test development but probabilistic runtime behavior weakens reproducibility.

## Decision

LLMs are permitted for development tooling; any future probabilistic runtime is explicit experimental capability and never silent default.

## Consequences

Rapid language scaling without sacrificing deterministic production semantics.
