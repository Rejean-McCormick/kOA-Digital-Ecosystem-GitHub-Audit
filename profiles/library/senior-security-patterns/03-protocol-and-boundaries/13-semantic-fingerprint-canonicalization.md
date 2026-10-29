# SEC-13 — Canonical Semantic Fingerprints

## Core principle

Distributed systems need to know whether two requests are the “same” semantically, not merely byte-identical. Security controls based on naive JSON hashing are bypassed by serialization differences, field ordering or non-semantic metadata.

## Security invariant

Idempotency, approval and integrity checks MUST hash a documented canonical semantic projection, with explicit versioning of both canonicalization and included fields. Security-relevant fields cannot be silently excluded.

## Senior architecture

Define a profile like `semantic-fingerprint/jcs+sha256/vN`: select semantic fields, canonicalize deterministically (e.g., RFC 8785 JCS), hash, and version the profile. Keep trace IDs/timestamps out only if they are intentionally non-semantic. Any change to projection rules is a protocol version change.

## Application to the supplied ecosystem

IK already implements a JCS-based request fingerprint over selected semantic fields and detects same-key/different-fingerprint conflicts. Reuse this discipline for Konfid approval proposals, privileged commands, Release Sets and Runtime Pack activation receipts instead of inventing ad hoc hashes.

## Failure modes / anti-patterns

- Hashing raw JSON bytes.
- Approval digest omits target, tenant or scope.
- Canonicalization changes without version bump.
- Treating SHA-256 as authenticity without a trusted binding/signature.
- Including volatile fields so every retry becomes a new semantic request.

## Evidence that proves the control

Cross-language test vectors produce identical fingerprints. Mutation tests show every security-relevant field changes the digest. Version negotiation rejects unknown fingerprint profiles. Approval/execution compare the same canonical projection implementation.


## Reference anchors

- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
