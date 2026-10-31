<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/90-reference/adr/adr-0006-common-identity-oidc.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 8c7a8ce0385b54bcfc8fe62ae731c1a90c06dce8b2140bee2ef8cfe451ed5bc6 -->

# ADR-0006: Common Identity via Optional OIDC Federation

**Status:** Accepted  
**Date:** 2026-09-11  
**Decision Owner:** Ecosystem Architecture  
**Scope:** Human identity across Orgo, Konnaxion, and UCKK-Moodle

---

## 1) Context

Orgo, Konnaxion, and UCKK-Moodle participate in a shared ecosystem while retaining distinct ownership, authorization, data, and standalone operation.

A common login experience is desirable, but a shared user database, password synchronization, or runtime authorization dependency would violate ecosystem trust and autonomy boundaries.

## 2) Decision

kOA adopts:

```text
standalone-first
+ optional OIDC federation
+ local authorization
```

The canonical federated identity key is `(issuer, subject)`.

Each application MUST retain its own local account identifier and authorization model. Email MUST NOT be the ecosystem identity key. Passwords MUST NOT be synchronized between applications.

A common IdP MUST NOT become the sole administrative recovery dependency; critical deployments retain a documented local break-glass path.

Machine-to-machine integrations use dedicated service identities rather than human SSO tokens.

## 3) Consequences

Positive:
- coherent SSO experience;
- local roles remain independently governable;
- applications remain standalone-capable;
- no shared user database;
- IdP adoption does not require rewriting local business identifiers.

Costs:
- account linking/provisioning must be implemented per application;
- duplicate-account and lifecycle policy must be explicit;
- deployments must manage federation and recovery paths.

## 4) Implementation profile

See `../../40-integration/identity-oidc/`.

## 5) Rejected alternatives

### Shared password/user database
Rejected because it couples availability, security blast radius, schema evolution, and application ownership.

### Email as global identity key
Rejected because email is mutable and may collide or be recycled.

### Orgo or Konnaxion as mandatory identity authority
Rejected because it breaks standalone operation and confuses product authority with authentication.

### Universal ecosystem role table
Rejected because equivalent human identity does not imply equivalent permissions across applications.
