<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/adr/ADR-0002-articulation-not-content-selection.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: d28f9f8a7e7087bafb7c7041be96465ba1d7f82e8a9ec1657bd3d27ded139294 -->

# ADR-0002 — SA owns articulation, not content selection

Status: **accepted**

## Context

Upstream systems decide what information is to be communicated.

## Decision

SA must discharge every submitted communication obligation and may reorganize but not silently remove it.

## Consequences

Faithfulness becomes a hard invariant; summarization-by-deletion requires a different upstream obligation set.
