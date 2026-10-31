<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/ADR/0002-declarative-query-plans.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: b3abf10d690c82c7cd425716f13832dc30e1f397ee83f69f47dcc3cf09bc344e -->

# ADR 0002 — Declarative Semantic Query Plans

## Status

Accepted.

## Decision

LLMs submit semantic operations against advertised capabilities. They do not submit implementation commands.

## Rationale

This decouples the agent from heterogeneous Kristal CLIs, permits adapters to evolve, enables strict schema validation, and sharply reduces command-injection risk.

## Consequences

Adapter authors must invest in capability design and mapping. Native query tools remain implementation details.
