# SEC-32 — Security Delta Release Gates

## Core principle

A generic test suite treats all changes equally, but security risk is highly non-uniform. A migration touching grants, a workflow change, or an auth middleware change deserves different evidence than a CSS update.

## Security invariant

Release policy SHOULD classify security-sensitive deltas and automatically require stronger review/tests/evidence for them. The gate is based on what changed, not only on test pass/fail.

## Senior architecture

Maintain sensitive path/rule sets: authentication, authorization, policy, migrations of security state, audit, crypto, CI workflows, deployment manifests, network/egress and privileged adapters. Trigger targeted property tests, threat-model update, security owner review or staged rollout.

## Application to the supplied ecosystem

Konfid's SECURITY.md already highlights auth/authz, policy, enforcement, audit, identity/key and security-state migration changes. Generalize this pattern across the 41-repository ecosystem so every product has a machine-readable “security delta” map.

## Failure modes / anti-patterns

- Security review is a manual label someone remembers to add.
- Database migration passes structurally but changes privilege semantics.
- Workflow file change bypasses app security review.
- Generated OpenAPI drift not checked for new privileged routes.
- Threat model updated once a year regardless of architecture changes.

## Evidence that proves the control

PR automation identifies security-sensitive files and blocks without required owners/tests. Release record lists triggered security gates. Diff tests detect newly exposed routes/scopes/permissions. Threat model references the change when trust boundaries move.


## Reference anchors

- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
