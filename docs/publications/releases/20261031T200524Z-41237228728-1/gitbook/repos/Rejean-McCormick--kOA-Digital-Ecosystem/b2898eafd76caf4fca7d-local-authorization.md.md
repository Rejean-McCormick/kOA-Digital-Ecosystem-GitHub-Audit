<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/identity-oidc/local-authorization.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 76e5e8d466ba1bfbe3911b606541dd0ba59495a97820963cad6ab81649099ec6 -->

# Local Authorization

**Status:** Normative (kOA)

Federation answers **who is authenticating**. Each application answers **what that local account may do**.

## Orgo

Orgo remains authoritative for organization memberships, RBAC, workflow administration rights, task/case access, and tenant authorization.

## Konnaxion

Konnaxion remains authoritative for its participation, moderation, deliberation, distribution, and application-specific permissions.

## UCKK-Moodle

UCKK-Moodle remains authoritative for enrolments, course/context roles, capabilities, academic permissions, and its own publication/administrative permissions. It is not the owner of Konnaxion/eThikos civic decisions.

## No universal role table

The ecosystem MUST NOT assume equivalence such as:

```text
Moodle teacher == Orgo supervisor == Konnaxion moderator
```

Mappings MAY be configured locally, but remain application policy rather than identity truth.
