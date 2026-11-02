<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/KristalDiag-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: b0313884bb27c78a97fbf2ed055131aef38c10c860b6314f17eb0a60e422589b -->

# KristalDiag v9

KristalDiag is the **independent examiner** for Kristal v9.

```text
Kristal Framework = normative contracts + reference implementation
KristalDiag        = independent qualification
```

## Why independent?

A single reference implementation can accidentally agree with its own ambiguity. V9 therefore benefits from a second implementation that reproduces the same golden commitments from the specification rather than sharing code.

KristalDiag v9 implements the baseline commitment rules in Python and does not import or execute the Framework JavaScript commitment implementation.

## V9 profiles

```text
V9-State-Reader
V9-Builder
V9-Materializer
V9-Publisher
V9-Full
```

## V9 levels

KristalDiag adds:

```text
K15  machine contracts
K16  independent logical commitments
K17  State Snapshot semantics
K18  derivations/reproducibility
K19  materialization binding
K20  Exchange binding
K21  Build / Publish / Activate
K22  polymorphic workload corpus
K23  negative/invariance corpus
K24  inherited compatibility substrate
```

K14 remains the final fail-closed gate.

## What it protects

- hash-profile ambiguity;
- accidental inclusion/exclusion drift;
- stale declared commitments;
- mutable references in immutable snapshots;
- runtime/canon confusion;
- broken inherited compatibility;
- implementations that work only for one knowledge shape.

## Authority boundary

A KristalDiag PASS is qualification evidence, not semantic truth or deployment authority.
