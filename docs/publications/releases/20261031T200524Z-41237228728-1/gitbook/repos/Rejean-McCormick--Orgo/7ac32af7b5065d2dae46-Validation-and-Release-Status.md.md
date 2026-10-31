<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Validation-and-Release-Status | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 23c209faf864c2f840a75895992e98209a675fbb7cbda5d0c7efc1db83932327 -->

# Validation and Release Status

This page summarizes the current validation state of Orgo without replacing the detailed technical evidence kept in the main repository documentation.

## Current development status

As of **2026-09-17**, the current Orgo development tree has passed the complete local automated validation chain available in LevelUpDiag:

| Campaign | Result | What it establishes |
| --- | --- | --- |
| `database` | PASS | Native PostgreSQL migration and database integration validation |
| `deep` | PASS | Architecture, types, tests, production builds, dependency audit and related repository checks |
| `browser` | PASS | Required Chromium journeys against a real local Orgo API and PostgreSQL runtime |
| `acceptance` | PASS | Backup/restore plus an isolated production-like Docker deployment and browser acceptance |

The successful acceptance run completed **9/9 required levels** with no warnings, failures, errors or blocked levels.

## Production-like acceptance evidence

The automated acceptance path validated:

- repository-shipped PostgreSQL backup and restore procedures;
- restoration of **70/70 expected tables**;
- restoration of the expected Prisma migration history (**1/1 migration record** in the acceptance database);
- startup of an isolated Docker Compose stack containing PostgreSQL, API, web and worker services;
- API, web and worker health checks;
- disposable account/seed preparation;
- **24/24 Chromium browser journeys** against that isolated stack;
- automatic cleanup of the temporary containers, network and volume;
- dependency audit reporting **0 vulnerabilities** for the validated dependency state.

Dynamic loopback ports are used by the acceptance harness so the production-like stack does not require the normal development ports to be free.

## Release baseline

The published tagged baseline remains:

- **`v0.1.0-rc.1`**

That tag is an immutable historical release-candidate baseline. The newer 2026-09-17 acceptance evidence applies to the later development tree and does **not** by itself move, replace or promote the RC1 tag.

A future RC or production release should be cut intentionally from an identified clean commit with its validation evidence retained for that exact state.

## What is not claimed

The green local acceptance chain is strong production-like evidence, but it is not the same as a real production deployment.

This status does not claim live interoperability with deployment-specific external providers that were not configured during acceptance, including for example:

- SMTP or SMS providers;
- external webhooks;
- a real OIDC Identity Provider;
- Konnaxion / kOA ecosystem services;
- Kristal / Da’at integrations;
- other provider-specific credentials or hosted infrastructure.

Those remain separate acceptance boundaries when a deployment enables them.

## Practical interpretation

Orgo's current development tree is **locally production-acceptance green** for the automated scope above.

The next release step is not another generic local test pass; it is to identify the exact release commit, retain its evidence, and then intentionally decide whether to cut a new release candidate or production release.
