<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Migration-v9-to-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: ba96239ec237e23a03c383439d61601b7a836bce5eed2e8fcb72d9fd51bfea52 -->

# Migration v9 → v10 (additive)

This is an **operational adoption**, not a rewrite of existing logical states.

1. Retain v9 Logical Artifacts and immutable State Snapshots, including their existing commitments.
2. Create `.kristal/node.json` with a persistent `node_id`.
3. Add one or more host bindings under `.kristal/bindings/`.
4. Declare hosted capabilities in `.kristal/capabilities.json`.
5. Add a `kristal_directory` if node discovery is needed; keep private mappings private.
6. Continue verifying v9 logical/state commitments. Qualify the new host/publication contracts separately.

```text
V10 ADOPTION != V9 REWRITE
HOST MOVE != LOGICAL REVISION
```

For the managed GitHub path, use the declarative [[GitHub-Reference-Profile-v10]] and [[Workflow-GitHub-v10]]. For reader synchronization, use the exact derived [[GitHub-Read-Surfaces-v10]] contract; **Sync is neither Publication nor Activation**.

*Normative source: Framework `spec/v10/Migration-v9-to-v10.md`.*
