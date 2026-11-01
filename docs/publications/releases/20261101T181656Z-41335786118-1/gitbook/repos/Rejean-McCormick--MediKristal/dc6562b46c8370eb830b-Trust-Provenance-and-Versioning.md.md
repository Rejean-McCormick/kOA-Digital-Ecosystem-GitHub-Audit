<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Trust-Provenance-and-Versioning | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: 1eee1055476cbb540f929dbc99c6d41a82a616e15ccdc22a2afa5fe870b9c1b1 -->

# Trust, Provenance, and Versioning

MediKristal treats provenance and versioning as part of medical knowledge itself.

## No recommendation without a traceable chain

A target rule is:

> **No clinical recommendation without an attributable evidence chain and an applicable policy or protocol.**

```text
output
 ↓
protocol rule
 ↓
medical assertion(s)
 ↓
source(s)
 ↓
source version / jurisdiction / date
```

## Version everything that can change

Potentially versioned objects include:

- terminology releases;
- imported source snapshots;
- source-to-source mappings;
- MediKristal assertions;
- guidelines;
- institutional protocols;
- Smart Vote lenses;
- eligibility/competence snapshots;
- language realizations;
- Runtime Packs;
- publication representations sent to UCKK.

## Jurisdiction matters

A recommendation can differ because of:

- approved products;
- formularies;
- test availability;
- public-health rules;
- institutional resources;
- professional regulation;
- local protocols.

Jurisdiction therefore belongs inside the knowledge model.

## Revocation and supersession

Outdated content should normally be **superseded or revoked**, not silently deleted.

This preserves historical auditability.

## Runtime reproducibility

A Runtime Pack should make it possible to identify exactly which knowledge state was in use.

```text
release identity
source versions
promoted assertions
protocol versions
jurisdiction
language artifacts
integrity metadata
```

See:

- [Portable Knowledge with Kristal](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Portable-Knowledge-with-Kristal)
- [Release and Artifact Lifecycle](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Release-and-Artifact-Lifecycle)
