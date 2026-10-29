# SEC-25 — Cryptographic Use Is Auditable

## Core principle

A key can remain secret while still being abused by an authorized but compromised signer. Monitoring only key extraction misses fraudulent signing and anomalous verification patterns.

## Security invariant

High-value signing/decryption operations MUST emit security evidence: caller/workload identity, key ID, operation purpose, artifact digest or bounded reference, time, result and relevant policy context.

## Senior architecture

Instrument KMS/HSM usage and correlate it with release/build/approval records. Alert on unusual signer identity, volume, environment, time or artifact class. Keep sensitive plaintext out of crypto audit; record cryptographic identifiers and hashes instead.

## Application to the supplied ecosystem

For release metadata and Runtime Pack signing, a release record should reconcile one-to-one with expected signing events. For Audit Broker or identity keys, unexplained signing should be incident-worthy even if the signature is cryptographically valid.

## Failure modes / anti-patterns

- “Signature verifies, therefore release is legitimate.”
- No logs from HSM/KMS.
- Signer can sign arbitrary bytes outside approved pipeline.
- Crypto audit stored only on same host as signer.
- Alerting only on failed verification, not anomalous successful signing.

## Evidence that proves the control

Security team can map every production signature to an approved workflow. Unapproved KMS signing event triggers alert. Signer role cannot delete its own key-usage audit. Verification failures include deterministic key/policy reason codes.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- Sigstore / Cosign keyless signing: https://docs.sigstore.dev/cosign/signing/overview/
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
