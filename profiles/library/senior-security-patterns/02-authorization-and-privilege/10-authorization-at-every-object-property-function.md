# SEC-10 — Authorization at Object, Property, and Function

## Core principle

“Endpoint requires auth” is not meaningful protection if a caller can select another tenant's object, write protected fields, or invoke an admin function through the same API model. Mature APIs authorize at all three levels: object, property and function.

## Security invariant

For every externally influenced identifier and mutable field, the service must prove the caller may access that object, may modify that property, and may invoke that function in the current context. Serialization schemas do not replace authorization schemas.

## Senior architecture

Use explicit command DTOs rather than binding database models. Resolve resources under tenant/owner predicates. Mark server-owned fields as impossible to submit. Maintain distinct read/write views when sensitivity differs. Centralize function permission naming but evaluate against the concrete resource.

## Application to the supplied ecosystem

Apply this rigor to Konnaxion civic objects, Orgo Cases/Tasks, Konfid grants/delegations/responses and Koali Space administration. Security-critical records should reject mass assignment of status, owner, authority source, policy version, approval state or audit metadata.

## Failure modes / anti-patterns

- Generic PATCH of ORM objects.
- IDs are UUIDs so BOLA is considered impossible.
- Admin-only fields hidden in UI but accepted by API.
- One broad `write` scope for unrelated mutations.
- Authorization before object resolution, with no owner/tenant predicate.

## Evidence that proves the control

Negative tests enumerate object IDs across tenants and mutate every writable property. OpenAPI/request schemas exclude server-owned security fields. Authorization coverage tests map every mutating route to object/property/function checks.


## Reference anchors

- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
