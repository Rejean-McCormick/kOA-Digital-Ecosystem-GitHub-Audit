# SEC-24 — Envelope Encryption and Key Scope

## Core principle

“Encrypted at rest” is too coarse. High-value multi-tenant data needs keys scoped so a storage-layer compromise or one tenant's key does not expose unrelated security domains.

## Security invariant

Data encryption keys SHOULD be scoped by data class/tenant/security domain where the threat model warrants it, wrapped by centrally governed key-encryption keys. Key access is separately authorized and audited.

## Senior architecture

Use envelope encryption: per-object/batch/tenant DEKs, KMS/HSM KEKs, explicit encryption context binding tenant/object/type, and rotation by rewrapping where possible. Keep backup key-access paths distinct and tested.

## Application to the supplied ecosystem

Apply strongest scoping to identity bindings, grants, approval evidence, forensic exports and sensitive Kristal/knowledge artifacts when confidentiality demands it. Encryption context should prevent ciphertext copied across tenant/object domains from decrypting successfully.

## Failure modes / anti-patterns

- One application master key in config.
- Encryption context omitted.
- Backup keys accessible to same runtime role.
- Database admin automatically gets KMS decrypt.
- Rotating KEK requires decrypt/re-encrypt every object online.

## Evidence that proves the control

Tests copy ciphertext across tenant/object context and fail decryption. KMS audit shows purpose-scoped decrypts. Backup restore exercise proves key availability without granting broad production runtime access.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
