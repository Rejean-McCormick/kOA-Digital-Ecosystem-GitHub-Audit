<!-- Frozen source: https://github.com/Rejean-McCormick/Daat/blob/24d288b040d345405c508eb650d40a6c8856cf2a/docs/decisions/ADR-0003-IK-PROFILE-GOVERNANCE.md | commit: 24d288b040d345405c508eb650d40a6c8856cf2a | SHA-256: b191b7fe7b66c6cca6c7d23916ea62675bddc8ad7b666af45b7fb4669c57526f -->

# ADR-0003 — Preserve owner contracts; version generic external profiles

**Status:** Proposed for review · **Date:** 2026-10-12

## Decision proposed

Keep IK `kristal.build.request/2.0.0` and `kristal.artifact.ready/2.0.0` as the existing **portable Kristal v6** interaction surface. Do not widen their semantics. New external capabilities (e.g. non-Kristal `inventory.read`) require separately named, owner-approved IK profiles with explicit security, authority, output and receipt obligations.

## Compatibility note

The IK snapshot's v7 pin is draft.3.1; Kristal Framework reports draft.3.2. Those must be reconciled through explicit contract owner tests and pin releases, not silent downgrades/upgrades. Portable v6 remains unchanged.

## Dependency

Approval by Interaction Kernel and any receiving domain owner before implementation of live generic external IK exchange.
