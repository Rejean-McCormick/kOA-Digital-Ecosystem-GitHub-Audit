<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd/docs/FRAMEWORK_PIN_REVIEW.md | commit: 9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd | SHA-256: e68c811a8b8a3b19f32d65825cd6b9df6859ef87639a8bcb451c1b51ffbad766 -->

# Framework pin and managed-file reconciliation

**Requires joint C0 / Framework / Bootstrap / C1 / C2 review. No pin is automatically changed by this repository update.**

## Observed references

- Existing repository workflows reference `Rejean-McCormick/KristalV10@27c0c7db3d79a4597c1c964fe8281fa35b5f858a` and run the commands available at that revision.
- The supplied Framework snapshot reports `10.0.0-draft.3.1`; a Bootstrap example references `Rejean-McCormick/Kristal-Framework@fe54a88271e2ad7522abacdfbde90f9397954053`.
- These are different repository/revision strings. Similar naming does **not** establish equivalent contracts, complete tool coverage or immutable compatibility. Compare `contracts/contract-set.json`, compatibility locks and the exact CLI paths at each approved SHA before changing a workflow pin.

## Bootstrap-managed hashes

`.kristal/bootstrap-state.json` tracks five paths: node descriptor, host binding, capabilities and two GitHub workflows. The five tracked SHA-256 values **do not match** their current bytes in the supplied snapshot. This may reflect intentional post-Bootstrap C3 changes; it must not be silently treated as trusted reinstallation.

Run:

```bash
python tools/repository_audit.py --repo .
```

The audit reports drift **without editing anything**. Before future Bootstrap `apply`, its owner must inspect `doctor` / `plan`, classify each file as Bootstrap-owned, C3-owned, or shared, and explicitly approve any reconciliation. **Do not run `--adopt-managed` merely to silence drift**, replace custom C3 workflows, regenerate node IDs or rewrite hashes to fit an unrelated version.

## Approval requirements

Document the approved Framework SHA, compatibility-lock digest, C1 verifier and C2 signer trust roots, node ID, managed-file ownership, GitHub branch rulesets and a rollback plan. Then submit an independently reviewable, scoped PR. This repository does not infer or grant any of those approvals.
