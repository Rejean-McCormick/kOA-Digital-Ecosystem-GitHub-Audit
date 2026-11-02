<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Integration-Interaction-Kernel.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: dba0d1bc7b21ba928aaae6e449ad88c4924213613ad1f6c3a8256468380ee4bb -->

# Integration — Interaction Kernel

Interaction Kernel (IK) is the **selectively adopted system-of-systems protocol/Profile layer** for explicit cross-product boundaries. IK owns transport/profile semantics, not participant databases or epistemic state.

## Adoption rule

```text
IK profile defined
    ≠ profile adopted by every system
    ≠ profile qualified in every deployment
```

kOA-Linux keeps its own canonical internal/component contracts unless an owner explicitly adopts/maps an IK profile.

## Qualified Konnaxion ↔ Orgo profiles

- `governance.decision.execute/1.0.0`;
- `accountability.impact.publish/1.0.0`.

The qualified boundary covers durable delivery, Signal→Workflow→Case→Task execution, durable impact return, idempotent replay and divergent replay rejection. See [`../2-Technical-Reference/40-integration/orgo-konnaxion/index.md`](../2-Technical-Reference/40-integration/orgo-konnaxion/index.md).

## Knowledge-boundary profiles

The current frozen knowledge-contract baseline uses:

- `kristal.build.request/2.0.0`;
- `kristal.artifact.ready/2.0.0`.

These profiles connect EncyKlopedia/Da’at/Kristal/UCKK contract surfaces. Their use does not transfer acquisition, epistemic or projection authority to IK.

## Rules

- Konnaxion↔Orgo is direct by default; no forced Kristal hop.
- Da’at remains the mapping/ACL boundary for IK-facing Kristal work.
- Profile admission does not imply Kristal validation/recognition.
- Source-owned artifacts remain source-owned; ArtifactRefs identify immutable boundary artifacts without moving the live database record.
- IK must not create a distributed transaction spanning participant databases.
- Durable interactions preserve idempotency identity and terminal receipt semantics.

- `kristal.revision.request/2.0.0` is the aligned v6 revision boundary.
