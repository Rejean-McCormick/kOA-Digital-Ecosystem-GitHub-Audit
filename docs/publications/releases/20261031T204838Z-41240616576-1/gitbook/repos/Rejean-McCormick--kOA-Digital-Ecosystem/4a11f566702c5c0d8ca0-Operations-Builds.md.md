<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Operations-Builds.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 77a8a77ff88b79aa08e811af05240f08c7d625fa8e1c861cb9de5f824fe772ee -->

# Build operations

Build operations use **Build Record v2** and Kristal v6 semantics.

## Knowledge build sequence

A Profile may use:

```text
native/source input
  -> Kristal State
  -> Working Exchange
  -> validation/review
  -> authority recognition
  -> Reference Exchange
  -> Runtime Pack
```

Claim-IR/Resolved Claim-IR may appear when an extractor/resolver Profile requires them.

## Gates

Compilation, validation, recognition, publication and activation use separate stage-specific gates. Instead record separate status and enforce the gate appropriate to the requested transition:

- compile eligibility;
- reference eligibility;
- publication eligibility;
- distribution eligibility;
- activation eligibility.

A production kOA policy can require validated/recognized Reference material before release or activation while still retaining a Working Exchange for diagnosis/review.

## Build evidence

Record exact dependency pins, input refs/digests, deterministic tool/profile versions, Working/Reference output refs, Validation Reports, Authority Recognition refs, Runtime Pack refs and reason codes.
