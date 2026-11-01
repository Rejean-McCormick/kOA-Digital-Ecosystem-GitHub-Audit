<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Municipality-and-Public-Service | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 7ca05b85a23ec6a8903dc817804822ba749670f64e3a2bd825adc402e6f9ef41 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Municipality and Public Service

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## Intended environment

A municipality or public-service organization can separate public participation from private operational handling. Konnaxion receives knowledge, proposals and civic input; governance rules define legitimate decisions; Orgo routes service requests and decisions to accountable departments.

## Example flow

```text
citizen report
→ public or private intake
→ case classification
→ responsible municipal function
→ response window
→ escalation if overdue
→ recorded outcome
→ public update when disclosure policy permits
```

## Benefits of the architecture

- public transparency without exposing private case details;
- continuity when staff change;
- offline operation for field offices;
- multilingual public explanations;
- traceable decisions and appeal paths;
- portable institutional memory.

## Sources

- [Orgo guarantees](https://initkoa.org/platforms/orgo/guarantees)
- [Konnaxion](https://initkoa.org/platforms/konnaxion)
- [docs/07-security/16-public-evidence-and-private-proof.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/16-public-evidence-and-private-proof.md)
