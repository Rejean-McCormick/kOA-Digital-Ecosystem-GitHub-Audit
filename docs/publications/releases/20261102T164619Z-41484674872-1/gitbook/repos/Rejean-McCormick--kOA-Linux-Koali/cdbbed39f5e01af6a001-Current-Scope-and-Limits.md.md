<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Current-Scope-and-Limits | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: a318095d9128b56d43ae525993da4ca032a28d40bbf666886e1cedb245ba5da0 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Current Scope and Limits

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## What is complete in this repository

The documentation corpus defines and validates a contract-first target architecture for kOA-Linux Operating System. It includes system principles, profiles, component boundaries, security, lifecycle, operations, conformance, schemas, accepted ADRs, generators and validators.

## What remains implementation-dependent

The repository does not prove that every component is already implemented or production-tested. Evidence is still required for final host distribution choices, immutable image mechanisms, production key custody, hardware assurance, capacity limits, database isolation at scale, regulatory profiles and production implementations of internal services.

## Subsystem dependency

The detailed user behavior of Ariane, Konnaxion, Orgo, SenTient, and SemantiK Architect belongs to those subsystem specifications. The kOA-Linux repository currently reserves documentation mount points for pinned official subsystem documentation.

## Public-site status distinctions

- Konnaxion, Orgo, Kristal and the governance model are described as core parts of the kOA ecosystem.
- Semantik Architect is described as an independent experimental architecture for deterministic multilingual rendering.
- SenTient is explicitly described as conceptual or experimental and not production-ready.
- The wiki therefore distinguishes **intended capability**, **specified boundary**, and **production evidence**.

## No silent completion claims

A validated documentation tree proves consistency of the documentation and contracts. It does not by itself prove performance, security, usability, legal compliance or operational readiness on every target deployment.

## Sources

- [Repository implementation status](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/README.md)
- [docs/01-constitution/01-scope-and-non-goals.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/01-constitution/01-scope-and-non-goals.md)
- [docs/09-conformance/00-conformance-model.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/09-conformance/00-conformance-model.md)
- [SenTient status](https://initkoa.org/technology/sentient)
- [Semantik Architect status](https://initkoa.org/technology/architect)
