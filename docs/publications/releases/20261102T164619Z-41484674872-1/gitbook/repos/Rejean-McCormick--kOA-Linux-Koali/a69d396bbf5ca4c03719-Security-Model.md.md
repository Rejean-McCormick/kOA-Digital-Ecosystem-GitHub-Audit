<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Security-Model | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 2231978d7db5011cd26100ab6f2b939985d88797ad0ee863a4f7a78ee7ab0dc2 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Security Model

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

## Security posture

kOA uses explicit trust, least privilege, compartmentalized authority, signed artifacts, narrow privileged interfaces, bounded integrations, and recoverable failure states.

## Major security boundaries

- identity and trust roots;
- profile-scoped privilege and service identities;
- network and storage isolation;
- encrypted data and key handling;
- AI and external-integration boundaries;
- privacy, disclosure, consent, and cultural rights;
- selective audit and evidence access;
- cross-domain publication;
- offline import and software supply chain;
- break-glass authority with receipts and review.

## Privileged operations

The kOA Node Agent exposes closed high-level operations rather than arbitrary shell, package, file, container, service-manager, device, or private-key interfaces. The active node performs final local validation before a sensitive mutation.

## Disclosure and audit

Audit is selective. Evidence access follows policy, purpose, identity, disclosure class, and recourse rules. Auditability does not imply unrestricted transparency.

## Sources

- [`docs/07-security/00-threat-model.md`](../blob/main/docs/07-security/00-threat-model.md)
- [`docs/07-security/01-security-baseline.md`](../blob/main/docs/07-security/01-security-baseline.md)
- [`docs/07-security/02-security-domains.md`](../blob/main/docs/07-security/02-security-domains.md)
- [`docs/07-security/03-identity-trust-and-signatures.md`](../blob/main/docs/07-security/03-identity-trust-and-signatures.md)
- [`docs/07-security/05-privilege-boundaries.md`](../blob/main/docs/07-security/05-privilege-boundaries.md)
- [`docs/07-security/06-privileged-broker.md`](../blob/main/docs/07-security/06-privileged-broker.md)
- [`docs/07-security/08-network-boundaries.md`](../blob/main/docs/07-security/08-network-boundaries.md)
- [`docs/07-security/09-storage-boundaries.md`](../blob/main/docs/07-security/09-storage-boundaries.md)
- [`docs/07-security/13-privacy-and-disclosure.md`](../blob/main/docs/07-security/13-privacy-and-disclosure.md)
- [`docs/07-security/14-cultural-rights-and-consent.md`](../blob/main/docs/07-security/14-cultural-rights-and-consent.md)
- [`docs/07-security/15-selective-audit.md`](../blob/main/docs/07-security/15-selective-audit.md)
- [`docs/07-security/17-cross-domain-publication.md`](../blob/main/docs/07-security/17-cross-domain-publication.md)
- [`docs/07-security/18-offline-import-security.md`](../blob/main/docs/07-security/18-offline-import-security.md)
- [`docs/07-security/19-software-supply-chain.md`](../blob/main/docs/07-security/19-software-supply-chain.md)
- [`docs/07-security/20-break-glass-security.md`](../blob/main/docs/07-security/20-break-glass-security.md)
