<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Security-and-Privacy | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: f3c7f7ac08f7ac97b087257ee9b86bfb7271dbfa67ba276f74580a9b7d070628 -->

# Security, Privacy, and Authority Boundaries

## Primary rule

**A visible file or inventory entry is not automatically authorized for reading.** Manager supplies observations; Discovery profiles suggest reading paths; authorization and Reader Policy are separate.

## Neutral-selector protections

The local catalog checks for the `local` deployment profile, loopback interface, existing root directory, immediate subdirectories, bounded names, rejection of entry-level symbolic links, and a maximum of 500 entries. Selection uses a cataloged ID rather than a browser-provided file path. Local reading is not intended for `lan`, `shared`, or `public` deployments.

## Protections for read data

1. Validate the formats and actual paths consumed.
2. Verify sizes, fingerprints, and derived-model invariants when declared.
3. Apply Reader Policy before queries, facets, plans, explanations, and counts.
4. Do not expose private Manager inventory paths in the interface.
5. Do not load parser, component, or renderer code based on unverified Arketype or Discovery recommendations.
6. Never modify canonical data through the reading path.

## Hosting and synchronization

**Public synchronization may immediately expose the bytes transferred**, even without a qualified immutable publication. Local-reader integration triggers **no** GitHub push, activation, or C2 authorization. Any publication pipeline must independently establish its mandate, scope, and required C1/C2/C3 evidence.

## Practical advice

- Keep the server on `127.0.0.1` when browsing local Kristals.
- Protect private Manager configuration files and any tokens.
- Back up before replacing Konstellation or archiving legacy launchers.
- Never assume that a file hash proves the logical State Commitment.

References: `docs/19-security.md`, `docs/runbooks/THREAT-MODEL.md`, `server/integrations/local-catalog.mjs`, Framework `docs/16_SECURITY_AND_CONFIDENTIALITY.md`.
