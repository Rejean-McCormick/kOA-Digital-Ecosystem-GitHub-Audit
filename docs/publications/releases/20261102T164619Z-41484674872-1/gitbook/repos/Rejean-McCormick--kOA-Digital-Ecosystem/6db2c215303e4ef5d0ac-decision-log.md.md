<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent/decision-log.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: b36906348a655ee33a67bfb516ffab2e3854d8dae3390af1ab0bbad7d23366ac -->

# Deployment decisions and open questions

## TANDEM-D01 — first target profile (user decision; 2026-10-18)

**Decided:** prioritize a **Linux VPS with Docker and Capsule Agent** for the first final Konnaxion↔Orgo release. Scope: first tandem production candidate only. This **does not** abandon kOA-Linux, nor approve deployment. kOA-Linux and its Node Agent remain independent owners for platform-specific profiles.

**Consequences:** design Lot1C measured-state/PEP against the actual Linux Docker executor and owner-managed container resources; require a distinct staging qualification; do not confuse local Windows Uvicorn/Celery/Neon proof with VPS qualification.

## Decisions still open (no defaults inferred)

- Host/operator, VPS hardening, Linux distribution, Docker/Compose versions, container/image registry and pinned artifact inventory.
- Hostname, inbound exposure profile, TLS termination, DNS, firewall and egress; a private-only phase is preferred until explicitly authorized, but not a deployment command.
- Secret store and trusted Ed25519 verification roots/policy version, key revocation procedure, signed verdict distribution to Agent.
- PostgreSQL topology for Konnaxion vs Orgo, migrations, backups, separate restore points, RPO/RTO and outbox fencing.
- Standalone vs federated OIDC `ready` / `enforce`, IdP identity and scope of Konfid/policy services (per ADR-0006; no blanket SSO).
- Exact RC gate acceptance, external operator sign-off, staging environment and production traffic cutover.

## Release states to retain

`LOCAL-E2E` (proven synthetic) → `INTEGRATION-RC` → `STAGING-RC` → `PRODUCTION` **only with owner qualification on exact artifacts, signed admission and explicit operator approval**. C0 does not advance stages.
