<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Kristal-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5a3f061c3a4eea99f3a4a312766ec1edb391668c64ee2132b8b1449e72f999ea -->

**Historical v10 reference:** this page documents the frozen v10 hosted-network baseline. The **current proposed Framework draft is v11 `11.0.0-draft.4`**; see [[Home]], [[Kristal-v11]] and [[Status-v11]]. Its semantic identity/dictionary contracts are additive, not a replacement for historical v10 hosting.

---

# Kristal v10 — Hosted Kristal Network Architecture

**Working Framework baseline:** `10.0.0-draft.3.2` (13 October 2026 update). **Status:** proposed standard / draft, not final.

V10 builds a portable hosted network *around* the v9 Semantic State Architecture. It describes how a Kristal node is hosted, published and found without changing what its logical state means.

```text
v6  portable epistemic state
 + v7  semantic identity / Kristall
 + v8  language, query and derived readers
 + v9  Logical Artifacts, State Snapshots, commitments
 + v10 nodes, host bindings, publications, directories
```

## One boundary, four concerns

```text
SEMANTIC STATE != HOSTING != PUBLICATION LOCATION != DISCOVERY DIRECTORY
```

- **Semantic state (v9):** exact immutable State Snapshot, Logical Artifacts and pinned commitments.
- **Hosting (v10):** Node Manifest and replaceable Host Bindings.
- **Publication (v10):** verifiable immutable records that connect exact states to distributed bytes; activation is a separate transition.
- **Discovery (v10):** mutable directories and reader indexes; neither defines epistemic authority nor v9 federation membership.

**Migration is additive.** V10 does not rename v9 schemas or force rehashing/revisions on host migration, mirroring, publication, indexing or sync. Existing v6/v7/v8/v9 contracts retain their own meaning.

## Core contract names

| v10 hosted-network contracts | inherited v9 semantic contracts |
| --- | --- |
| `kristal_node_manifest` | `kristal_logical_artifact` |
| `kristal_host_binding` | `kristal_state_snapshot` |
| `kristal_publication` | `kristal_derivation` |
| `kristal_directory` | `kristal_materialization_manifest` |
| `kristal_v10_capabilities` | `kristal_exchange`, `kristal_activation` |

The first **optional** reference host profile is `kristal.host/github/1.0`; GitHub is not a core semantic dependency.

## Read next

- [[Status-v10]] and [[Version-Stack-v6-v7-v8-v9-v10]]
- [[Core-Invariants-v10]] and [[Architecture-v10]]
- [[Nodes-and-Collections-v10]], [[Host-Bindings-v10]], [[Publication-and-Discovery-v10]]
- [[GitHub-Reference-Profile-v10]], [[GitHub-Read-Surfaces-v10]]
- [[Migration-v9-to-v10]] and [[Conformance-v10]]
- [[Kristal-v9]] for the unchanged semantic-state architecture.

*Normative source in supplied Framework snapshot: `spec/v10/01-core-spec/kristal-v10-core-spec.md`, `docs/00_STATUS.md` and `schemas/v10/`.*

## Reader Discovery (optional operational profile)

The three derived, noncanonical reader-discovery documents from Authoring Kit 3.3.0 describe Arketype type/usage, tracked physical bytes and advisory parser strategies. They do not modify any v9 commitment. See [[Reader-Discovery-and-Arketype-v10]].
