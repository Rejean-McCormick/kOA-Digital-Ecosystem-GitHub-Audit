<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/90-reference/adr/adr-0008-kristal-v5-epistemic-lifecycle.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 02fd2682c6903ea7a94bb077397fe648767d259b011d2f2a804a25d663300bcb -->

# ADR-0008: Kristal v5 epistemic lifecycle and stage-specific gates

- **Status:** Superseded for the active baseline by ADR-0013; retained as the v5 historical decision
- **Date:** 2026-09-16
- **Supersedes:** ADR-0001 Truth Boundary
- **Scope:** kOA interpretation of Kristal v5 lifecycle; does not redefine Kristal schemas

## Context

The former kOA model treated Kristal as a single truth boundary and required validation success before compilation. Kristal v5 explicitly separates compilation, validation, certainty, authority recognition, reference status, publication and activation.

## Decision

1. Structured Epistemic State is the primary structured Kristal input.
2. Claim-IR/Resolved Claim-IR are optional profile/intermediate artifacts.
3. A Working Exchange may be compiled before final validation or recognition when policy permits.
4. Validation failure/rejection does not universally erase or prohibit Working artifacts.
5. Reference Exchange status requires the applicable recognition path.
6. Runtime Packs preserve source artifact status and Reader Policy references.
7. kOA Build Records keep compile, validation, recognition, publication and activation statuses separate.
8. kOA may define stricter **stage-specific** gates for reference publication/distribution/activation, but must label them as kOA/deployment policy rather than Kristal core semantics.

## Consequences

The terms “canonical truth”, “truth plane”, “truth boundary” and universal “no compile on fail” were removed from normative kOA documentation for the v5 era. For the active v6 baseline, use ADR-0013 and the Kristal v6 integration pages.
