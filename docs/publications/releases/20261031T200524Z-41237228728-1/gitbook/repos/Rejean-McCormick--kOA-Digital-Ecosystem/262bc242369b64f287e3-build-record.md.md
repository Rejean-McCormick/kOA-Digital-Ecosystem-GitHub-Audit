<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/30-artifacts/build-record.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 821d0d81e97d8e666200abae3f8cb152f97acf6fc7fc3037d6845a188a478ff2 -->

# Build Record v2

A Build Record records **what happened during a reproducible build/compile workflow** without collapsing independent lifecycle axes. It is kOA-owned operational evidence; owner artifacts remain authoritative.

## Principle

The record distinguishes:

```text
compile_status
validation_status
recognition_status
publication_status
activation_status
```

A successful compile does not imply validation/recognition. Publication and activation are separate transitions.

## Required evidence

A Build Record should identify:

- inputs/source snapshots/evidence used;
- toolchain and exact applicable Kristal contract/release baseline;
- Interaction Kernel Profile/correlation identity when applicable;
- executed stages and outcomes;
- produced Working/Reference artifacts;
- validation and authority-recognition references;
- Runtime Packs and source-artifact status;
- publication/activation requests/outcomes;
- stable reason codes for blocked/failed transitions.

## Kristal mapping

Recommended opaque references include Referent Registry entries, Kristal State, Working Exchange, Validation Report, Authority Recognition, Reference Exchange, Runtime Pack Manifest and Reader Policy. The Build Record does not duplicate their internal fields.

Schema: `schemas/build-record.schema.json`.
