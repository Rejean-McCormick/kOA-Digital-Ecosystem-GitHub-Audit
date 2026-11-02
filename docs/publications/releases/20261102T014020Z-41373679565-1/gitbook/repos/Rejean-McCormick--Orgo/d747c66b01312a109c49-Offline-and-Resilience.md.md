<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Offline-and-Resilience | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 075d547307f7a76b9d5bc07a486dc750189b94509982e4b971f6f619a4934b84 -->

# Offline and Resilience

Orgo is designed with **offline and local operation** in mind.

That does not mean every external integration is magically available without a network. It means Orgo's own operational model can distinguish local work from synchronization and can represent offline/sync inputs explicitly.

## Offline signals

Offline or synchronized input is treated as a Signal, then processed through normal Orgo rules.

```text
local/offline input
→ synchronization or ingestion
→ organization scope
→ workflow evaluation
→ Case / Task when appropriate
```

Offline sync is not a shortcut around the normal Task/Case lifecycle.

## Resilience through explicit state

Because Tasks, Cases, assignments and events are explicit, an organization can reason about what is pending, what has been completed and what still needs reconciliation after connectivity returns.

## External systems

If a workflow depends on another system that is unavailable, Orgo can still retain its own workflow context. The external operation remains incomplete until the external owner actually accepts or performs it.
