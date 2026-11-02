<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/wiki/Security-Boundaries | commit: e707adff40a4b9a660647bec302236caf6d6edf6 | SHA-256: 255f8e057ae352da2922f517f58a7d5b9ac9f9503fcedb907077fd4286564f6d -->

# Security Boundaries

Konfid's boundaries are designed to answer a concrete question: **what information actually needs to cross each control point?**

## 1. Identity boundary

Google, Microsoft Entra, or a sovereign IdP authenticates the person. Konfid does not receive the person's password.

What crosses:

```text
issuer
subject
assurance
freshness
explicitly required claims
```

What must not cross into Konfid:

```text
password
recovery credential
MFA secret
```

## 2. Application → Konfid boundary

Applications remain the owners of business data.

For an access decision, Konfid preferably receives:

```text
principal
action
resource_class
resource_ref
scope
context
```

It does not need the full document when this metadata is sufficient.

## 3. Policy boundary

The Policy Runtime receives the context required to decide, not an arbitrary copy of the business database.

Authentication never replaces authorization.

## 4. Overwatch boundary

Overwatch observes semantic events and produces risk information.

It does not have:

- a shell on every system;
- a universal super-token;
- authority to silently modify a policy;
- authority to directly trigger a global shutdown.

## 5. Konfid → Orgo boundary

Orgo receives the context required for the human workflow: incident, proposed action, scope, risk, digest/references.

Orgo does not automatically become a copy of the protected data that triggered the incident.

## 6. Approval boundary

Orgo collects a human decision, but Konfid revalidates:

- approver identity;
- right to approve;
- scope;
- request digest;
- freshness;
- quorum;
- requester/approver/operator separation;
- current policy.

## 7. Execution boundary

The agent receives a bounded command:

```text
operation
specific target
scope
decision ref
expiry
idempotency key
```

It does not receive general administrator access on behalf of Konfid.

## 8. Evidence boundary

Audit evidence is separated from operational state.

The observed component must not be able to modify, on its own, all of the following:

- the action;
- the decision;
- its receipt;
- the entire historical evidence trail.

## 9. Tenant boundary

Each principal, grant, resource, and decision is bound to a validated tenant/scope.

A client-provided `tenant_id` is not, by itself, proof of authority.

Cross-tenant tests are part of the mandatory invariants.

## 10. Telemetry / audit boundary

Analytical telemetry is not the authoritative audit trail.

- telemetry is used to detect;
- audit is used to prove;
- the two may have different stores, access controls, and retention periods.

This avoids creating a huge event lake that unnecessarily contains all sensitive activity.

## 11. Forensic boundary

Enriched collection is possible only in an explicitly governed mode:

```text
scope
reason
authority
duration
classification
purge
```

Forensics is not the default mode.

## 12. Failure boundary

Vital functions retain resources separate from analytical functions.

Priority:

```text
P0 revoke / deny / isolate
P1 authorization
P2 security event ingestion
P3 analytics / reporting
```

A P3 overload must not make P0 unavailable.
