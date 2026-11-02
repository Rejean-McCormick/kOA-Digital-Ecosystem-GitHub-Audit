<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/10-system/determinism.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: f246115a5d2677a71a648cc6bab81ede2423ab84adfd36af86b165242418768d -->

# Determinism

Determinism is required where kOA produces reproducible artifacts, signatures/digests, idempotent requests or release evidence. It does **not** imply a universal validation-before-compilation gate.

## Kristal v6

For the pinned Kristal version, canonicalization is `kristal.v6:jcs-rfc8785` version `1`.

A deterministic compile can produce a **Working Exchange**. Validation/review and authority recognition are independent, scoped decisions. Reference publication, release or activation may be gated by stricter kOA Profiles.

## Requirements

- pin exact schema/tool/Profile versions used for reproducible outputs;
- canonicalize and hash exactly as required by the owning contract;
- preserve input identities and provenance;
- keep compile, validation, recognition, publication and activation state distinct;
- never infer epistemic status from a successful digest/signature;
- use deterministic idempotency fingerprints for cross-system commands where defined by IK;
- same idempotency key + different fingerprint must be treated as conflict, not replay.

## Reproducibility

A build/release record should contain enough immutable references to reproduce or explain the result: exact Kristal pin, schema-set/canonicalization identity, source refs/digests, Profile/policy refs, output refs and reason codes.
