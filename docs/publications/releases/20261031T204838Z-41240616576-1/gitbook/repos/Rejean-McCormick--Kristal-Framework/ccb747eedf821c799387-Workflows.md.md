<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflows | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c749d3e8ce9644ea617a74a016304bb44ed5f0c436e88bad1047143aefa29243 -->

# Workflows

**V10 operational entrypoint:** [[Workflow-GitHub-v10]] separates Local Kit semantic build, Manager derived reader Sync, GitHub Setup qualification/immutable publication, and optional activation. The v9 workflow below is preserved as the state lifecycle foundation.

Kristal v9 separates semantic authoring, derivation, materialization, publication and read-side access.

## Canonical authoring

```text
source / observation / domain model
        ↓
normalize under domain contract
        ↓
validate semantic/epistemic rules
        ↓
Logical Artifact commitment
```

## State construction

```text
Logical Artifacts + pinned external refs
        ↓
State Snapshot
```

## Physical build

```text
State / Artifact
        ↓
Materialization profiles
        ↓
Exchange + Runtime
```

## Publication

```text
BUILD
  ↓
VALIDATE
  ↓
PUBLISH immutable snapshot
  ↓
ACTIVATE channel
```

## Query/language

V8 query, lexical and AI-context workflows remain derived/access-side layers around the v9 state.

See:

- [[Workflow-Build-and-Validate]]
- [[Workflow-Publish-and-Distribute]]
- [[Workflow-Activate-Rollback-Downgrade]]
- [[Build-Publish-Activate-v9]]
- [[Migration-v8-to-v9]]
