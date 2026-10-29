# SEC-43 — Compromise-Ready Recovery

## Core principle

Disaster recovery restores availability; security recovery restores trustworthy authority. Restoring a compromised database or old credentials can reintroduce attacker persistence and replay old privileged intents.

## Security invariant

Recovery plans MUST identify trust that can be safely restored versus trust that must be re-established: credentials, keys, sessions, grants, outbox items, policy, release artifacts and audit heads. Recovery resumes writers only after reconciliation.

## Senior architecture

Maintain clean recovery artifacts, independent backups, key/credential rotation playbooks and last-known-good release sets. Restore in isolation, validate schema/integrity/audit, rotate compromised trust, reconcile external effects, then re-enable bounded traffic.

## Application to the supplied ecosystem

Konfid's runbook already warns that database restore can replay old intents and requires outbox reconciliation. Apply the same thinking to Orgo work queues, Konnaxion state projections, activation commands and release automation: restoring state must not silently resurrect expired authority.

## Failure modes / anti-patterns

- Restore backup and immediately start workers.
- Old sessions/API keys become valid again.
- Restored outbox re-executes destructive command.
- Backup admin can also delete production and backups.
- Last-known-good image uses a revoked key/policy with no recovery rule.

## Evidence that proves the control

Recovery exercise proves no duplicate privileged effects. Credential/session revocation survives or is re-established after restore. Audit head reconciles with external authority. Recovery produces a new governed release/trust state, not an invisible time travel.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
