<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/kOA-Linux-Responsibilities | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: fe9db96ebb72862d3eac9643d83e6b7b9f9bfb3a08777258858a547d41043af6 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Operating-System Responsibilities

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## Host and deployment

- maintained Linux host and selected immutable-image mechanism;
- boot, service management and recovery environment;
- deployment profiles and overlays;
- hardware and resource envelopes;
- local storage, networks and device access.

## Security and trust

- service identities and least privilege;
- trust roots, signatures and artifact verification;
- rootless service boundaries where applicable;
- narrow privileged host operations;
- secrets, keys and data-at-rest controls;
- network and publication boundaries.

## Runtime governance

- policy bundle activation;
- authorization and disclosure checks;
- receipts for critical transitions;
- audit routing and selective evidence preservation;
- AI and external-integration restrictions.

## Lifecycle and resilience

- release sets and compatibility;
- verified activation and rollback;
- offline bundles and transport;
- backup, restore and disaster recovery;
- capability degradation and health;
- export, transfer and credible exit.

## Integration

kOA-Linux owns the boundary, not the subsystem internals. It mounts or references pinned official documentation and validates compatibility before activation.

## Sources

- [README.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/README.md)
- [docs/02-system/00-system-overview.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/00-system-overview.md)
- [docs/06-lifecycle/02-release-model.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/06-lifecycle/02-release-model.md)
- [docs/07-security/01-security-baseline.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/01-security-baseline.md)
- [docs/08-operations/00-operating-model.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/08-operations/00-operating-model.md)
