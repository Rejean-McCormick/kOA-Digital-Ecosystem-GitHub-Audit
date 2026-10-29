# SEC-18 — Tenant Isolation Is End-to-End

## Core principle

Multi-tenancy fails when only the database query is tenant-scoped but caches, queues, metrics, object stores, rate limits, audit streams or background workers are not. Tenant is a security dimension across every stateful boundary.

## Security invariant

Every tenant-bearing operation MUST derive tenant context from authenticated authority, not user input alone, and propagate it through storage keys, cache keys, queues, outbox leases, policy, audit and observability. Cross-tenant operations are explicit privileged operations.

## Senior architecture

Use composite keys/constraints including tenant, row-level or application-level predicates, per-tenant sequencing where needed, and tenant-aware resource limits. Partition caches and idempotency scopes. Validate tenant on worker dequeue, not only API enqueue.

## Application to the supplied ecosystem

Konfid already checks authenticated caller tenant against request tenant and uses per-tenant audit chains. Apply the same invariant to IK idempotency stores, artifact caches, Runtime Pack registries, Koali projections and AI memory stores.

## Failure modes / anti-patterns

- Tenant ID accepted from request body without caller binding.
- Global idempotency key namespace.
- Cache keyed only by object ID.
- Shared vector/AI memory namespace.
- Audit export worker can emit records under wrong tenant after retry.

## Evidence that proves the control

Cross-tenant property tests span API, worker, cache and restore paths. Database uniqueness and foreign keys encode tenant where possible. Metrics avoid leaking tenant-sensitive labels while quota/rate-limit enforcement remains tenant-aware.


## Reference anchors

- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
