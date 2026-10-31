<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Contributing-and-ADRs | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: a73b65f4bab833ff7389d2fa1c68fe7343f7f9e520c5b2e79da141e14a90ac13 -->

# Contributing, Versioning, and Architecture Decisions

v0.2.0 is a reference repository for **local validation, preview and simulation**, designed to support future integrations. Under ADR 0008, **Orgo** owns all real Tandem Task/Case/Signal operations. Its invariants must survive even if other services eventually absorb the functions.

## Contribution process

1. Explain the need and impacts on students, teachers, content, security, and data.
2. Identify affected domain aggregates, ports, and contracts.
3. Add/update tests, schemas, and examples **without real children's data**.
4. Propose an **ADR** for new structural decisions.
5. Run [[Testing-and-Validation|validation]] and clearly identify unimplemented behavior.

## Architecture Decision Records

Located in `docs/adr/`:

| ADR | Decision |
|---|---|
| 0001 | Browser access; no mandatory USB keys |
| 0002 | Kristal knowledge is separate from its guardian |
| 0003 | Deterministic reader without generative AI |
| 0004 | Teacher-approved role assignment |
| 0005 | Contextualized historical perspectives |
| 0006 | Independent KOMPOSE; optional KOR integration |
| 0007 | Pause/resume, phases, and dependencies in the local reference model |
| **0008** | **Orgo is the only operational authority for real Tandem workflows; KOMPOSE validation and simulations do not alter Orgo state** |

## What each artifact is for

- **ADRs:** decisions, rationale, alternatives, and consequences.
- **Contracts:** required data structures, routes, and events.
- **Wiki:** readable team guide, not a replacement for normative schemas.
- **Changelog:** delivered changes and limitations by release.

## Licensing

The repository includes `LICENSE-TO-DECIDE.md`: **no redistribution license has been selected yet**. Do not assume it is open source or can be freely republished.

[[Home|← Home]] · [[Open-Decisions|Open decisions →]]
