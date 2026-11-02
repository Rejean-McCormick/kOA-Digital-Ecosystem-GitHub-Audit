<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Crisis-Field-and-Air-Gapped-Use | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: fef3e3a06f9766df2ee37a8b713e84dc1da7bc8a5f6249e9d5667df0a519821c -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Crisis, Field, and Air-Gapped Use

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## Intended environment

A field team, crisis unit, remote institution or high-assurance environment may operate with intermittent or no network access. The deployment must preserve local knowledge, operational work, evidence and recovery without pretending that remote services are available.

## Local capabilities

- verified procedures and knowledge packs;
- local search and navigation;
- offline Orgo cases and tasks;
- local files and evidence;
- local policy evaluation where required;
- queued synchronization and publication;
- removable-media updates with verification;
- backup and restore without cloud dependency.

## Safety rules

- stale or unverified data remains visibly labeled;
- conflicts are reviewed under declared strategies;
- failed verification blocks activation;
- emergency or break-glass actions are bounded, logged and reviewed;
- offline does not remove accountability.

## Sources

- [Kristal offline scenarios](https://initkoa.org/technology/kristal/portability-and-offline)
- [Orgo offline-first resilience](https://initkoa.org/platforms/orgo/guarantees)
- [docs/03-profiles/12-sovereign-offline.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/03-profiles/12-sovereign-offline.md)
- [docs/07-security/18-offline-import-security.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/18-offline-import-security.md)
