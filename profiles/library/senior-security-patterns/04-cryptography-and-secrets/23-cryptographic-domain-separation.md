# SEC-23 — Cryptographic Domain Separation and Agility

## Core principle

Crypto failures often come from using the right primitive in the wrong domain: same key, same hash preimage, or same signature semantics across unrelated purposes. Domain separation prevents cross-protocol substitution and makes algorithm migration tractable.

## Security invariant

Signed or hashed objects MUST bind protocol/version, object type, authority domain and semantic purpose. Verifiers reject unsupported algorithms and algorithm/key-purpose mismatches. Cryptographic policy is versioned independently from application data.

## Senior architecture

Prefix/structure canonical payloads with explicit context. Use separate keys or derivation contexts for artifact signing, receipts, audit chain and tokens. Maintain an algorithm allowlist, deprecation process and inventory of where each algorithm is used.

## Application to the supplied ecosystem

IK's versioned fingerprint profile is a good pattern. Apply similar domain/version labels to approval digests, audit chain hashing, Runtime Pack signatures and release metadata so no valid signature can be reinterpreted as a different artifact class.

## Failure modes / anti-patterns

- Signing raw hash without object type/domain.
- Accepting algorithm declared by attacker without policy allowlist.
- One generic “signature” verifier for every artifact.
- Hard-coding algorithm with no migration path.
- Confusing digest integrity with signature authenticity.

## Evidence that proves the control

Cross-protocol substitution tests fail. Crypto inventory maps algorithms/keys to artifact classes. A policy update can reject deprecated algorithms without code surgery. Test vectors pin canonical bytes and domain context.


## Reference anchors

- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
