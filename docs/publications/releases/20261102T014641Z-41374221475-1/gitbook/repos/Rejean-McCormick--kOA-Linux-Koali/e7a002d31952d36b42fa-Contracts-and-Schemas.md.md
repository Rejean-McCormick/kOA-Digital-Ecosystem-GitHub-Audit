<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Contracts-and-Schemas | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: f1920b516604a2679fb10db744ffa35b3ea8473288f32efd0202667561c7d48b -->

<!-- Explanatory wiki projection. Normative authority remains in the repository and subsystem documentation. -->

# Contracts and Schemas

> **Reading model:** The main path explains what the kOA ecosystem enables. The technical reference explains how kOA-Linux hosts, isolates, verifies, and operates those capabilities. Product-specific details remain in each subsystem's own documentation.

The technical corpus uses source contracts for system, component, subsystem-boundary, profile, integration, toolchain, and artifact facts.

Key directories:

- `docs/contracts/components/` — internal kOA-Linux components;
- `docs/contracts/subsystems/` — boundaries for independently owned systems;
- `docs/contracts/profiles/` — deployable operating envelopes;
- `docs/contracts/integrations/` — optional external services and platforms;
- `docs/contracts/artifact-contracts/` — exchanged records, packages, manifests, and receipts;
- `docs/generated/` — rebuildable discovery projections.

Use [Related Wikis](Related-Wikis) for product-internal behavior. The kOA-Linux contracts define only the operating and exchange boundaries for those products.

Repository entry points:

- [System contract](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/contracts/system.contract.json)
- [Generated component catalog](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/generated/component-catalog.md)
- [Generated subsystem catalog](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/generated/subsystem-catalog.md)
- [Generated profile catalog](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/generated/profile-catalog.md)
- [Generated integration catalog](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/generated/integration-catalog.md)
