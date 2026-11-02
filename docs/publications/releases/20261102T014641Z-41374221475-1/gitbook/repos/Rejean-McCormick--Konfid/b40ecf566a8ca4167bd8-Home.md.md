<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/wiki/Home | commit: e707adff40a4b9a660647bec302236caf6d6edf6 | SHA-256: 13b61bf828311385b3e8d81c46e44a10a8ad810b6dc41a8432eaff86c4020563 -->

# Konfid — Is It Secure? Are the Data Protected?

**Yes — by design, Konfid follows modern security practices and, above all, adds architectural boundaries that significantly reduce data exposure.**

The short answer is:

> **Konfid protects access to data without becoming a central copy of that data.**
>
> Sensitive business data stays, as much as possible, in the systems that own it. Konfid mainly receives the identity information required for a decision, the resource class, the scope, the decision, and evidence references — not the full content.

This architecture follows a **Zero Trust** model, separates authentication from authorization, applies least privilege, bounds permissions by scope, requires additional controls for critical actions, and preserves independent evidence of important decisions.

## The most important question: where does the data go?

Consider an HR record in Konnaxion.

```text
User
    │
    ▼
Konnaxion ──────────────── keeps the HR record
    │
    │ authorization request
    │
    │ principal=P123
    │ action=employee.read
    │ resource_class=HR.RECORD
    │ scope=organisation-ABC
    ▼
  Konfid
    │
    │ ALLOW / DENY / STEP_UP
    ▼
Konnaxion
    │
    ▼
local record access
```

**The HR record itself does not need to pass through Konfid.**

Konfid can make a decision using metadata such as:

```text
principal = P123
action    = employee.read
resource  = HR.RECORD
scope     = organisation-ABC
decision  = ALLOW
policy    = access-hr/42
```

The protected content remains with its owner.

## What Konfid actually stores

Konfid still needs to retain certain information in order to operate correctly. Some of it may itself be considered personal data:

- technical principal identifier;
- authorized account bindings;
- roles, grants, scopes, and delegations;
- authentication assurance level;
- security decisions;
- risk signals;
- incident and approval references;
- audit metadata and references required for accountability.

The distinction matters: **Konfid minimizes the data it centralizes and avoids absorbing business content when a reference or classification is sufficient.**

## What should not pass through Konfid by default

Konfid is designed not to unnecessarily transport or store:

- the full contents of HR records;
- full email bodies;
- project documents;
- medical records;
- private messages;
- customer files;
- user passwords;
- bearer tokens in logs;
- application secrets;
- keystrokes or general-purpose content surveillance.

When sensitive evidence absolutely must be retained, Konfid can use a **protected reference + integrity digest** instead of copying the evidence into security events.

```text
resource_ref   = sealed://evidence/9282
digest         = sha256:...
classification = restricted
```

## Multiple control points prevent a leak from spreading

Security does not depend on a single firewall or a single administrator.

```text
Authentication
Google / Entra / IdP
        │
        ▼
Identity & Trust
        │
        ▼
Stable principal
        │
        ▼
      Konfid
 authorization / scope
        │
        ▼
Owning application
 final local validation
        │
        ▼
      data
```

And for a security action:

```text
unusual activity
        │
        ▼
Overwatch
 produces a signal
        │
        ▼
Policy / Response
 decides what is allowed
        │
        ▼
Human approval if required
        │
        ▼
Bounded local agent
        │
        ▼
Receipt + independent audit
```

This way, no component automatically receives every power.

## Current standards and practices

Konfid is designed to align with principles and controls recognized today, including:

- **NIST SP 800-207 — Zero Trust Architecture**: no implicit trust based only on the network or possession of a system;
- **NIST Cybersecurity Framework 2.0**: governance, identification, protection, detection, response, and recovery;
- **IETF RFC 9700 / BCP 240**: current security best practices for OAuth 2.0;
- **OpenID Connect** for federated identity;
- **OWASP ASVS 5.0** for application security verification;
- **CIS Controls v8.1** for operational cybersecurity controls;
- principles of **least privilege**, **defense in depth**, separation of duties, expiration, revocation, idempotence, and auditing.

This does not mean that a code repository is automatically “NIST-certified,” “OWASP-certified,” “CIS-compliant,” or “ISO-certified.” Formal compliance or certification depends on the real deployment, configuration, operations, and often an independent audit. Konfid is designed to provide the mechanisms and evidence needed to support that assurance.

## Why Google Login does not weaken this model

Google or Microsoft may authenticate a user, but they do not decide that user's Konfid permissions.

```text
Google
  "this account has authenticated"
        │
        ▼
Konfid
  "may this principal perform THIS action
   on THIS resource in THIS scope?"
```

Email is not used as the canonical identity. Federation relies on a stable identity such as `issuer + subject`.

A valid login therefore is not enough to:

- become an administrator;
- export a large volume of data;
- modify a policy;
- approve one's own critical action;
- trigger a shutdown.

## Protection against excessive actions

Overwatch cannot directly trigger a destructive shutdown.

```text
OBSERVE
  ↓
STEP_UP_AUTH
  ↓
RATE_LIMIT
  ↓
REVOKE_SESSION
  ↓
SUSPEND_GRANT
  ↓
SUSPEND_ACCOUNT
  ↓
ISOLATE_SERVICE
  ↓
FREEZE_TENANT
  ↓
EMERGENCY_SHUTDOWN
```

Policy chooses the smallest response that is reasonably sufficient.

For critical operations, Konfid can require:

- recent strong authentication;
- multiple distinct approvers;
- requester different from approver;
- mandatory justification;
- exact scope;
- expiration;
- reevaluation immediately before execution;
- execution receipt;
- independent audit.

## What if a system is compromised?

The architecture is designed to limit the **blast radius**.

A compromised Konnaxion should not automatically become a Konfid administrator. A compromised Orgo should not be able to fabricate a valid quorum by itself. A compromised Overwatch detector should not possess credentials allowing it to arbitrarily isolate infrastructure. An execution agent should accept only an allowlist of typed operations.

The central rule is:

> **No single component should be able to authenticate, authorize, approve, execute, and erase the evidence of a critical action on its own.**

## So, is it secure?

**Konfid's target architecture is designed to be secure according to modern practices, with defense in depth, Zero Trust, least privilege, separation of powers, auditing, and data minimization.**

Most importantly, protection does not rely only on encryption or a strong login: **sensitive data is deliberately prevented from crossing certain boundaries when it is not required for the decision.**

The final security of a deployment still depends on its actual configuration, keys, infrastructure, integrations, load and security testing, and operational procedures.

## Read next

- [How Data Remains Protected](Data-Protection)
- [Why Konfid Is Secure](Why-Konfid-Is-Secure)
- [Security Boundaries](Security-Boundaries)
- [Standards and Assurance](Standards-and-Assurance)
- [Semantic Activity and Audit](Semantic-Activity-and-Audit)
