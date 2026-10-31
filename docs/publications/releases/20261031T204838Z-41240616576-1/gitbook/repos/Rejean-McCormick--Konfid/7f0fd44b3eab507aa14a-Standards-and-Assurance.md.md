<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/wiki/Standards-and-Assurance | commit: e707adff40a4b9a660647bec302236caf6d6edf6 | SHA-256: bb585dd08563b0a8c53dc5c68a68176ed6a2689f8b18e372726260dc7bdaf51e -->

# Security Standards and Assurance

## Short answer

Konfid is designed to align with **current security standards and practices** applicable to a distributed identity, authorization, and control architecture.

The main references are:

- **NIST SP 800-207 — Zero Trust Architecture**;
- **NIST Cybersecurity Framework 2.0**;
- **IETF RFC 9700 / BCP 240 — Best Current Practice for OAuth 2.0 Security**;
- **OpenID Connect** for federated identity;
- **OWASP ASVS 5.0** for application security verification;
- **CIS Critical Security Controls v8.1**;
- modern practices for least privilege, defense in depth, separation of duties, expiration, rotation, revocation, idempotence, auditing, and supply-chain security.

## Important: alignment is not certification

Software does not automatically become “NIST-certified,” “OWASP-certified,” or “CIS-compliant” simply because its architecture applies their principles.

Complete assurance also depends on:

- the actual deployment;
- TLS/PKI/KMS configuration;
- secret management;
- the policies actually enabled;
- network controls;
- operations and procedures;
- load and failure testing;
- incident response;
- an independent audit when required.

Konfid is designed to facilitate this assurance and produce the required evidence, but it does not turn an unverified configuration into a certification.

## Mapping to modern principles

### Zero Trust

No implicit trust is granted solely because a call originates from an internal network or a known service.

Each important action is based on:

- identity of the calling service;
- identity of the human actor, when applicable;
- action;
- resource;
- scope;
- context;
- policy;
- risk state.

### Modern OAuth/OIDC

Federated identity is separated from application authorization. Stable identifiers such as `issuer + subject` are preferred over email.

User tokens are not reused as generic service-to-service credentials.

### Least privilege

Access is bounded by role, action, resource, scope, duration, and context.

Privileged operations are typed and allowlisted rather than exposing general-purpose remote administration.

### Defense in depth

A critical action may pass through several successive controls:

```text
IdP
 ↓
Identity & Trust
 ↓
workload identity
 ↓
Konfid policy
 ↓
application local policy
 ↓
approval / step-up
 ↓
privileged agent allowlist
 ↓
receipt
 ↓
independent audit
```

### Accountability

Critical decisions produce reason codes, policy references, correlation IDs, receipts, and minimized audit events.

### Resilience

Konfid explicitly designs for:

- retries;
- duplicates;
- network delays;
- Orgo failure;
- telemetry overload;
- temporary loss of an upstream dependency;
- reconciliation;
- canary deployment;
- rollback.

## Public references

- NIST SP 800-207 — https://doi.org/10.6028/NIST.SP.800-207
- NIST CSF 2.0 — https://doi.org/10.6028/NIST.CSWP.29
- IETF RFC 9700 — https://www.rfc-editor.org/rfc/rfc9700.html
- OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/
- CIS Controls v8.1 — https://www.cisecurity.org/controls

## What to ask before a sensitive deployment

To answer “is it secure?” professionally, you should be able to show:

1. which controls are implemented;
2. which tests are automated;
3. which dependencies are qualified;
4. which secrets/keys are used in production;
5. how tenants are isolated;
6. how data is minimized;
7. how privileged actions are authorized;
8. how audit evidence is protected;
9. how backups/restores are tested;
10. which penetration test or independent audit has been performed.

The appropriate statement is therefore:

> **Konfid is designed according to current standards and practices, with an architecture that reduces data exposure by design. The security of a given deployment must then be verified through its operational controls and testing.**
