<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Organizations-People-and-Privacy | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 23abd2ffe4dee17c9eab8be7989b8f9063e3951bfaadcdb35e3dd40ec30b5c96 -->

# Organizations, People and Privacy

Orgo is multi-tenant. The **Organization** is the primary operational boundary.

## Organization

An Organization has its own:

- Cases and Tasks;
- profile and configuration;
- roles and permissions;
- people and user accounts;
- workflows and operational history;
- analytical views.

One organization's identifiers must not become a shortcut into another organization's data.

## User and Person are different

Orgo distinguishes a **User account** from a **Person profile**.

### User

A User is an actor who can authenticate and perform actions in Orgo.

### Person

A Person is a human subject represented in operational context.

A Person might be:

- an employee;
- a student;
- a patient or care recipient;
- a volunteer;
- a requester;
- another person involved in a Case.

That person may never log in to Orgo.

```text
User = actor/account
Person = subject/profile
```

This distinction is especially important in HR, care and education contexts.

## Visibility and authorization

Orgo can classify work by visibility and route it through labels, but those mechanisms are not substitutes for authorization.

Sensitive work should remain organization-scoped and role/permission-aware.

## External identities

When Orgo refers to an object or person owned by another system, the relationship should remain explicit. Orgo stores only the references and operational context it actually needs.
