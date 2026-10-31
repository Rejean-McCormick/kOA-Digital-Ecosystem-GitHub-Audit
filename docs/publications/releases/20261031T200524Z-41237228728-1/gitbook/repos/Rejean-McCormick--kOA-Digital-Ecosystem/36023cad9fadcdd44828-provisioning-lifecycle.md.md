<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/identity-oidc/provisioning-lifecycle.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 67770525db0a2e1647942b68266d21c94e2fc3a9175197a8fbf68871280519b1 -->

# Provisioning & Identity Lifecycle

**Status:** Normative (kOA)

## 1) Provisioning modes

Applications MAY use pre-provisioning, invitations, approved JIT provisioning, or local account creation. The mode is local policy.

## 2) First federated login

```text
validate issuer + subject
-> exact identity lookup
-> if linked: use existing local account
-> if not linked: apply local provisioning policy
```

## 3) Linking existing accounts

Existing accounts MUST NOT be silently linked by email alone.

Acceptable linking requires proof/control such as an authenticated local session, administrator approval, signed invitation, or another controlled migration process.

## 4) Attribute authority

| Attribute | Authority |
|---|---|
| issuer / subject | IdP |
| Orgo role | Orgo |
| Konnaxion role | Konnaxion |
| Moodle enrolment/capability | Moodle |
| display name / email | deployment policy |

## 5) Deactivation

Disabling one local account does not automatically disable or delete accounts in other applications.

IdP deactivation blocks future federated authentication; whether local login remains possible is local policy.

## 6) Audit/history

Identity lifecycle changes MUST preserve required business and audit history. Deletion, anonymization, and retention are governed by application and legal policy rather than federation alone.
