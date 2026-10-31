<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Getting-Started | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: ba77e4252e25b76ad38e8b585c9fbab180fa85de00acfffd5c38c16f9ba76a6f -->

**v11 note:** the active *proposed* standard is [[Kristal-v11]] (`11.0.0-draft.4`). This document retains the foundational v9/v10 workflow; for a new strict KQ/KP graph use [[Authoring-Kit-v11]] and [[Dictionary-Management-v11]]. For older text-identified graphs use [[Legacy-Migration-v11]], never a global word replacement.

---

# Getting Started

**For a new hosted-network deployment (v10 `10.0.0-draft.3.2`):** first identify or preserve the exact v9 semantic state below; then add a node manifest, host binding(s) and capabilities. The GitHub host profile is optional. Use [[Migration-v9-to-v10]], [[GitHub-Reference-Profile-v10]] and [[Workflow-GitHub-v10]] for the operational path.

The steps below remain the **v9 semantic authoring foundation**, not the full v10 host setup.

Kristal v9 does **not** require rewriting valid v6/v7/v8 material. Adoption starts by identifying what is already canonical and what is derived.

## 1. Identify the native canon

Ask:

- What data structure actually owns the domain meaning?
- Which files are portable projections?
- Which are read indexes/caches?
- Which external systems retain authority?

Do not choose a storage codec first.

## 2. Preserve inherited contracts

Keep existing `kristal_state/6.0`, KQ/KP/KA/KS and v8 query/language artifacts valid under their original rules.

## 3. Define Logical Artifact boundaries

Choose domain units with coherent schema, identity, authority and lifecycle.

A tiny v6 state can remain one Logical Artifact. A complex research system may have several native artifacts.

## 4. Define commitments

For every native contract, define:

- ordered vs set-like collections;
- logical fields;
- default/null/absent semantics;
- excluded physical metadata;
- commitment profile.

## 5. Create an immutable State Snapshot

Pin exact owned artifact commitments and any external state/artifact dependencies.

## 6. Declare Derivations where reproducibility matters

Separate build provenance from epistemic provenance.

## 7. Materialize only as needed

- small artifact → inline;
- huge homogeneous relation → factorized/segmented;
- graph/DAG/AST → keep native if appropriate;
- query/search indexes → Runtime/Derived.

## 8. Preserve v8 language/query layers

Lexical Kristals, KQP and AI context compilation remain valid read-side capabilities around the v9 state.

## 9. Publish then activate

```text
BUILD → VALIDATE → PUBLISH IMMUTABLE SNAPSHOT → ACTIVATE
```

## 10. Claim only implemented conformance profiles

See [[Conformance-v9]] and [[KristalDiag-v9]].
