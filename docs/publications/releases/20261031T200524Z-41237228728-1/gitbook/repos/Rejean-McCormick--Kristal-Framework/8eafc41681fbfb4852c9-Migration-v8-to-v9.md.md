<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Migration-v8-to-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: e604f36eb0af11091706d0d58a42b0bf53bc99c9ca81d735b700dab3988c139b -->

# Migration: v8 → v9

V9 migration should be **additive and authority-first**.

## 1. Inventory authority

Classify existing material as:

```text
canonical domain payload
portable projection
derived index/runtime
source snapshot
build metadata
presentation/view
external reference
```

Do not optimize before source-of-truth boundaries are explicit.

## 2. Preserve inherited artifacts

Keep valid v6/v7/v8 artifacts valid under their original contracts. Do not remint identities merely to adopt v9.

## 3. Identify Logical Artifacts

Choose boundaries with coherent:

- schema;
- identity;
- authority;
- lifecycle;
- commitment rules.

Do not assume “one file = one Logical Artifact”.

## 4. Separate derived duplication

Move rebuildable structures such as `*_by_id`, reverse indexes, query/search indexes and AI context bundles to Runtime/Derived authority.

## 5. Define commitment normalization

Before changing storage, specify:

- ordered versus set-like collections;
- logical fields;
- excluded physical/presentation fields;
- null/absent/default semantics;
- commitment profile.

## 6. Create a State Snapshot

Compose the logical artifacts and pin external dependencies. At this point, physical storage can remain exactly as before.

## 7. Record Derivations

Make source normalization, projections and runtime builds explicit where reproducibility matters.

## 8. Optimize only where useful

Large relations may benefit from factorization/segmentation. Small research corpora may remain inline. Graph/DAG/AST can remain native.

## 9. Introduce immutable publication/atomic activation

Replace in-place release mutation with immutable snapshots selected by a mutable activation pointer.

## 10. Qualify independently

Use the Framework TCK and an independent examiner such as [[KristalDiag-v9]].
