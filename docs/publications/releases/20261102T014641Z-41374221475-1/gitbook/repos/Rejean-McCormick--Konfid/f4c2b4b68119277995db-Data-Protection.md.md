<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/wiki/Data-Protection | commit: e707adff40a4b9a660647bec302236caf6d6edf6 | SHA-256: e3c383e0feb3e05d2f03ac0f45db82e8b2adac29db69fd7becc0ad2d2e7631c5 -->

# How Data Remains Protected

Konfid's most important property is not only controlling **who can access data**. It is also reducing the number of places where that data needs to exist.

## Principle: protect without absorbing

Konfid operates as a **control plane**, not as a data lake.

When an application requests authorization, Konfid generally needs to know:

- who is acting;
- what action is being requested;
- what resource class is targeted;
- within which tenant/scope;
- what assurance level the session has;
- which policies apply;
- what risk state is known.

It generally **does not need the protected content itself**.

## Example: reading a personal record

```text
Personal data
       │
       │ remains in Konnaxion
       ▼
┌─────────────────┐
│    Konnaxion    │
│   full record   │
└────────┬────────┘
         │
         │ decision metadata only
         ▼
┌─────────────────┐
│     Konfid      │
│ principal       │
│ action          │
│ resource class  │
│ scope           │
│ context         │
└────────┬────────┘
         │
         │ ALLOW / DENY / STEP_UP
         ▼
┌─────────────────┐
│    Konnaxion    │
│ applies locally │
└─────────────────┘
```

This separation means that a compromise of the Control Plane does not automatically imply a copy of every business record.

## Matrix: what crosses a boundary and what does not

| Boundary | What may cross | What should not cross by default |
|---|---|---|
| Application → Konfid | principal, action, resource class, scope, context | full document, full record, message body |
| IdP → application / Identity & Trust | stable subject, required claims, assurance | user password sent to Konfid |
| Konfid → Policy Runtime | minimal authorization context | arbitrary business content |
| Konfid → Orgo | incident, proposed action, scope, summary/digest | full application database |
| Overwatch → Response | RiskSignal, reasons, references | root access, enforcement credential |
| Konfid → Agent | typed command, target, scope, expiry, decision ref | unrestricted shell, universal global secret |
| Application → Audit | semantic event, refs, digest | full payload unless explicitly required |

## Metadata remains protected

Even minimal metadata can be sensitive. Konfid therefore treats it as protected data:

- access scopes;
- roles;
- decision history;
- risk signals;
- principal identity;
- approvals;
- incident references.

It is itself subject to:

- tenant isolation;
- access control;
- defined retention;
- auditing of sensitive reads;
- encryption appropriate to the deployment;
- minimization;
- deletion/pseudonymization where possible and permitted.

## Sensitive evidence remains separate

Forensic evidence may be too sensitive or too large to circulate inside events.

Konfid then uses the **Claim Check** pattern:

```text
Evidence Store
  [sensitive evidence]
        │
        ├── protected URI
        └── integrity digest
              │
              ▼
        Konfid event
```

The event can prove that evidence existed and was not modified without copying its contents everywhere.

## No general-purpose surveillance

Overwatch is intended to recognize behavior that matters for security, for example:

- unusual bulk export;
- privilege escalation;
- abnormally broad access;
- risky sequence of operations;
- use of a suspended account;
- modification of a critical policy.

Its purpose is not to capture everything a user writes, reads, or views.

## Data minimization by architecture

Minimization does not rely only on a documentation rule. It is built into the contracts themselves:

```text
AuthorizationRequest
  actor
  action
  resource_class
  resource_ref
  scope
  context
```

If a policy can make a decision using this information, there is no architectural reason to transport the full document.

## Last line of defense: the data owner

Even when Konfid returns `ALLOW`, the system that owns the data still applies its own local validation.

```text
final_access = Konfid ALLOW
               AND local application policy ALLOW
```

This rule reduces the risk that a central error directly exposes all of an application's data.

## Summary

**Konfid protects data by controlling access, but also by refusing to become a transit or storage location when it does not need to.**

This model reduces:

- duplication of sensitive data;
- the number of systems containing raw content;
- the impact of a compromise;
- the risk of overly verbose logs;
- unnecessary transfers between services;
- the compliance and retention surface.
