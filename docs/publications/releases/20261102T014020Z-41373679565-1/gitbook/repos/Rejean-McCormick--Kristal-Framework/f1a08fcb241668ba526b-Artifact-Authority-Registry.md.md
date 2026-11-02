<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Artifact-Authority-Registry | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 2e41b75d9ccc84f5e6fcb78d08e61b226e6e62ac621a85c1723128dc5a6defeb -->

# Authority Registry / Recognition Material

> **Legacy compatibility surface:** this page describes the historical v5-era Authority Registry contract. Kristal v9 does not promote this historical schema to its semantic core. For the inherited v9 semantic-state architecture see [[Artifacts]], [[Exchange-and-Runtime-v9]], [[State-Snapshots-v9]] and [[Federation-and-Coverage-v9]]; for the v10 hosted network see [[Architecture-v10]].

Kristal v6 treats authority as plural and scoped.

An authority record may describe:

- authority channel identity;
- trust roots / keys;
- recognition policies;
- validation policies;
- revocation references;
- applicability rules.

## Authority is external to storage

A Kristal record does not become authoritative because it is labeled `authoritative_constraint`. The authority must come from the actual law, institution, standards body, manufacturer, organization or other recognized source.

## Typical questions

A consumer should be able to determine:

- which authority recognized this assertion or artifact;
- for which applicability envelope;
- under which policy;
- whether recognition is still effective;
- whether another authority disagrees.

## Integrity vs authority

A valid signature proves that a key signed content. It does not prove that the signer has authority for every possible domain or jurisdiction.

See [[Trust-Authority-and-Signatures]].
