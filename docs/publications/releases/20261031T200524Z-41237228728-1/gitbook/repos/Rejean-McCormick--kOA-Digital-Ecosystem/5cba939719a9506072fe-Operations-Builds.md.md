<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Operations-Builds | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: b591223b6093d8b0526af874156e34ca8436e3fb28a49ad664e2b9ba44c70bea -->

# Build operations

Build operations use **Build Record v2** and Kristal v5 semantics.

## Knowledge build sequence

A Profile may use:

```text
native/source input
  -> Structured Epistemic State
  -> Working Exchange
  -> validation/review
  -> authority recognition
  -> Reference Exchange
  -> Runtime Pack
```

Claim-IR/Resolved Claim-IR may appear when an extractor/resolver Profile requires them.

## Gates

Do not use the historical universal rule “validation failure means compile must not run”. Instead record separate status and enforce the gate appropriate to the requested transition:

- compile eligibility;
- reference eligibility;
- publication eligibility;
- distribution eligibility;
- activation eligibility.

A production kOA policy can require validated/recognized Reference material before release or activation while still retaining a Working Exchange for diagnosis/review.

## Build evidence

Record exact dependency pins, input refs/digests, deterministic tool/profile versions, Working/Reference output refs, Validation Reports, Authority Recognition refs, Runtime Pack refs and reason codes.
