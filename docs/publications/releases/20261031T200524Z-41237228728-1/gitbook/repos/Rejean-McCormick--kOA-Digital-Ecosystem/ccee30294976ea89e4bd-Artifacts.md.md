<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/Artifacts.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 29a8b93887fdd6cd9ea447f95543e0ad03210a643c4e7fc4235ce28b5bcf2c56 -->

# Ecosystem artifacts

Artifacts remain authoritative at their owning system/component.

| Family | Owner | Examples |
|---|---|---|
| Civic/governance | Konnaxion | DecisionRecord, consultations, readings |
| Operational/work | Orgo | Signal, WorkflowVersion, Case, Task, IntegrationOperation |
| Acquisition evidence | EncyKlopedia | source/provider evidence, immutable harvest handoff, referent candidates |
| Knowledge/reference | Kristal | Referent Registry entries, Kristal State, validation/recognition references, Reader Policy, derived Runtime/query projection manifests |
| Consumer projection | UCKK / Univers-Cité | scope/view configuration, Moodle materialization, derived glossary/media presentation |
| Platform release | kOA-Linux | Release Set, registered release-channel/artifact contracts, lifecycle receipts |
| Runtime Pack local state | `kristal_runtime` | verification record, active Runtime Pack record, activation/rollback receipts, runtime health |
| Privileged node lifecycle | kOA Node Agent | privileged-operation/activation/recovery receipts |
| Presentation | Koali Spaces | Space definition, runtime registration, surface descriptors, Space lifecycle state |
| Cross-system reference | source + adopted contract | ArtifactRef, ExportManifest or equivalent source-owned references |
| Ecosystem build evidence | kOA integration layer | Build Record as non-authoritative correlation/reproducibility evidence |

## Authority-preserving knowledge layers

```text
1. Acquisition evidence
   source/provider-owned facts + EncyKlopedia immutable handoff
       ↓
2. Kristal v6 knowledge artifacts
   referents, assertions, valuations, applicability, roles, validation/recognition
       ↓
3a. Runtime/query materialization
    Runtime Pack / derived indexes / read models

3b. Consumer projection
    UCKK / Moodle / glossary / media presentation
```

Layers 3a/3b are derived and rebuildable. Neither becomes a second source of epistemic truth.

## Operational source state

Mutable product state remains product-owned. When knowledge is derived from it, the boundary uses an immutable source export/evidence reference with provenance rather than dual-writing the same record into Kristal.

## Release and activation

The **kOA-Linux Release Set** is the platform compatibility artifact. Active Runtime Pack state is owned by `kristal_runtime`; privileged host transitions may be executed by kOA Node Agent where required. Digital Ecosystem defines no parallel release or activation authority.
