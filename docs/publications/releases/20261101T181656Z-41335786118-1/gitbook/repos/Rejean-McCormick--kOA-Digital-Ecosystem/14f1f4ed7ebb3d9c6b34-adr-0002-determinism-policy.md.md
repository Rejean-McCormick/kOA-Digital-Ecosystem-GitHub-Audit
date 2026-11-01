<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/90-reference/adr/adr-0002-determinism-policy.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 0454af1e7defe05a2023185b805e2394d4f09f9cbd5057fe7d77f178776cc4c4 -->

# ADR-0002: Determinism Policy

- **Status:** Accepted, amended by ADR-0008
- **Decision:** retain deterministic artifact production and reproducible evidence; remove the historical universal validation-before-compile gate.

## Context

Determinism is required for content addressing, signatures, reproducible builds, reliable compatibility checks and idempotent cross-system operations. Kristal v6 separates deterministic content identity/projection from validation and authority recognition.

## Decision

kOA requires deterministic behavior where a contract defines canonicalization, hashing, serialization, ordering, identity derivation or idempotency fingerprints.

For Kristal:

1. exact Kristal version/tag/commit and canonicalization profile are pinned;
2. a deterministic compile may create a Working Exchange;
3. validation/review and authority recognition are recorded independently;
4. stricter production policies may gate Reference status, publication, distribution or activation;
5. Build Record v2 records these statuses independently.

## Consequences

The earlier formulation “compile must not run unless validation PASS” is superseded by ADR-0008. Historical records remain interpretable, but new implementations and docs use stage-specific eligibility gates.
