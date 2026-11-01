<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflow-Activate-Rollback-Downgrade | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: eb92f3bf51bd7a7ae6ac41f10f0fe5e7ce9031c7f3994f13c1e8a1beec320258 -->

# Workflow: Activate, Roll Back, Downgrade

V9 makes activation an explicit operation over immutable published snapshots.

## Activation

An activation decision selects an exact State Snapshot commitment for a channel such as `production`.

Typical inputs include:

- target State commitment;
- expected previous State commitment;
- validation/recognition status;
- environment/tenant scope;
- runtime/materialization compatibility;
- v8 lexical/query profile compatibility;
- operational owner policy.

The pointer transition should be atomic within the claimed transport/profile.

## Compare-and-swap

A publisher may require that the current active commitment still equals the base it built from. If not, activation must fail/rebase rather than silently overwrite another publication.

## Rollback

Rollback selects a retained prior immutable snapshot.

```text
ROLLBACK != HISTORY REWRITE
```

Do not rewrite newer canonical history to pretend it never existed.

## Downgrade

Dropping from v9 to v8/v7/v6 may lose materialization/lifecycle conveniences. It must not rewrite semantic claims to simulate those capabilities.

```text
DOWNGRADE LOSS != SEMANTIC REWRITE
```

## Legacy Runtime Packs

Older Runtime Pack consumers may remain compatibility targets. Treat them as derived materializations bound to inherited canonical source state.
