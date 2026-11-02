<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/ADR/0004-no-arbitrary-shell.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: 5fcfeb66eada6c7264f0079c4a040493dea83aa3117552bcc7fed5b18e804d81 -->

# ADR 0004 — No Arbitrary Shell in Agent-facing Contracts

## Status

Accepted.

## Decision

No Kompiler v1 protocol message can carry an arbitrary shell command or executable path.

## Rationale

The LLM is an untrusted planner. Execution details belong to trusted local adapters. This is both safer and more portable.

## Consequences

Subprocess adapters use fixed executable/script mappings and argument vectors. New native commands require adapter changes, not arbitrary query-plan strings.
