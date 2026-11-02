<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/identity-oidc/identity-model.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 96627861c5dbc17aae4d2946209e470d34fba8df30570b17ff89d7f5448ff6f6 -->

# Common Identity Model

**Status:** Normative (kOA)

## 1) Concepts

```text
Person
FederatedIdentity
LocalAccount
Membership
Role / Permission
```

A `Person` may have zero or more federated identities and zero or more application-local accounts.

A `FederatedIdentity` is identified by:

```text
issuer + subject
```

A `LocalAccount` is identified only inside its owning application.

## 2) Relationship

```text
Person
  |
  +-- FederatedIdentity (issuer, subject)
  |
  +-- Orgo account ------ memberships ------ Orgo roles/permissions
  +-- Konnaxion account - memberships ------ Konnaxion roles
  +-- Moodle account ---- enrolments ------- Moodle roles/capabilities
```

## 3) Email is an attribute

Email MUST NOT be used as the ecosystem-wide identity key because it can change, collide, be recycled, or differ by context.

A matching email MAY assist a controlled linking workflow but MUST NOT silently merge accounts.

## 4) Multiple issuers

Subject values are scoped to their issuer namespace:

```text
issuer A / subject 123
!=
issuer B / subject 123
```

## 5) Service identities

Machine-to-machine integrations MUST use service identities or scoped credentials separate from human SSO identities.
