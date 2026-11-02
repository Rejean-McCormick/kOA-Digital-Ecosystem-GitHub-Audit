<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Portable-Knowledge-with-Kristal | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 3bd179fa95a0e06b9ffdff70b4330c34892c5b8e28f0d762e1654fd72cc6efba -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Portable Knowledge with Kristal

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## What a Kristal provides

A Kristal is a portable, verifiable epistemic artifact. It allows knowledge to move between people, organizations and systems while keeping provenance, integrity, assertion status, certainty, authority, scope and reader policy visible.

The purpose is not to label every statement as universally true. A Kristal can preserve uncertainty, disagreement, symbolic material, research claims and scoped recognition without flattening them into one confidence score.

## User outcomes

A person or organization can:

- carry a knowledge package between systems;
- verify the package locally;
- browse and query it without a central server;
- inspect sources and status;
- compare versions;
- combine knowledge from several authorities without silently merging their claims;
- preserve durable references that do not depend on a live webpage.

## Offline Runtime Packs

A Runtime Pack is a read-optimized package for local browsing and query. The canonical exchange and provenance remain distinct from the local runtime projection. When verification fails or a pack is outdated, the system exposes that status rather than silently treating it as current authority.

## Role of kOA-Linux Operating System

The operating system stores, verifies, activates, pins, updates and rolls back Runtime Packs. It also enforces resource limits and reader/disclosure policy at the local boundary.

## Sources

- [Kristal](https://initkoa.org/technology/kristal)
- [What a Kristal does](https://initkoa.org/technology/kristal/overview)
- [Portability and offline](https://initkoa.org/technology/kristal/portability-and-offline)
- [docs/04-components/kristal-runtime.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/04-components/kristal-runtime.md)
- [docs/06-lifecycle/08-kristal-artifacts.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/06-lifecycle/08-kristal-artifacts.md)
