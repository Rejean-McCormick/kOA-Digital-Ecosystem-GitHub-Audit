<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Quickstart | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: e6d004ed5faf49721c1e282dee75587b29efae82c7e12c7cf662e5366327923b -->

**v11 note:** the active *proposed* standard is [[Kristal-v11]] (`11.0.0-draft.4`). This document retains the foundational v9/v10 workflow; for a new strict KQ/KP graph use [[Authoring-Kit-v11]] and [[Dictionary-Management-v11]]. For older text-identified graphs use [[Legacy-Migration-v11]], never a global word replacement.

---

# Quickstart — v9 semantic state + optional v10 network

**Current hosted-network baseline:** v10 `10.0.0-draft.3.2`. For GitHub, use [[Workflow-GitHub-v10]] and [[GitHub-Reference-Profile-v10]]. The workflow below is the **minimal inherited v9 semantic-state path** and remains valid.

The smallest v9 deployment can keep existing canonical bytes and add only the new state envelope.

## Minimal architecture

```text
existing canonical artifact
        │
        ├── Logical Artifact descriptor + commitment
        │
        └── State Snapshot
                 │
                 ├── existing v8 query/language companions
                 └── optional materialization/runtime profiles
```

## Existing v6 state

An unchanged `kristal_state/6.0` may be adopted as one Logical Artifact. You do not need to decompose it simply because v9 exists.

## Domain-native canon

If the domain already has a richer native canon — for example a recipe ProcedureGraph — preserve it as the Logical Artifact and keep the v6 state as a declared projection.

## Logical commitment

The commitment identifies normalized logical content, not the filename, compression or storage URI.

## State Snapshot

Compose exact artifact commitments. External dependencies are pinned, not `latest`.

## Runtime/query

Reuse the v8 rule:

```text
READ MODEL != CANONICAL STATE
```

## Lifecycle

Build candidate → validate → publish immutable snapshot → atomically activate.

## Next steps

- [[Version-Stack-v6-v7-v8-v9]]
- [[Logical-Artifacts]]
- [[State-Snapshots-v9]]
- [[Identity-and-Commitments-v9]]
- [[Materialization-v9]]
- [[Conformance-v9]]
