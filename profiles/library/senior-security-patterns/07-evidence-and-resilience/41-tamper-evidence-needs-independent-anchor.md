# SEC-41 — Tamper Evidence Needs an Independent Anchor

## Core principle

Hash chaining makes modification detectable only if an attacker cannot rewrite the entire chain and its head. A chain stored solely beside the data it protects is useful but not an independent proof.

## Security invariant

Tamper-evident local journals SHOULD periodically anchor chain heads or immutable batches into an independently governed system. Verification must detect deletion, reordering, mutation and forked history.

## Senior architecture

Use canonical event serialization, per-tenant/domain sequencing where appropriate, hash chaining/Merkle batching, and export chain head/records to an authoritative broker/WORM/transparency mechanism. Define restore behavior so old DB snapshots cannot silently fork history.

## Application to the supplied ecosystem

Konfid's per-tenant local chain + authoritative Audit Broker is a strong design. Formalize broker-side sequence/head reconciliation and restoration rules so a restored database cannot resume writing an alternate valid-looking local chain without detection.

## Failure modes / anti-patterns

- Hash chain head stored only in same table.
- Backups restore an older head and system resumes.
- Multi-writer audit sequence races silently.
- Canonicalization differs across DB timezone representations.
- Broker accepts out-of-order records without explicit gap handling.

## Evidence that proves the control

Restore/fork tests trigger head mismatch. Broker tracks expected sequence/head. Independent anchor survives local DB deletion. Chain verifier uses pinned canonicalization/version and can produce deterministic first-failure evidence.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
