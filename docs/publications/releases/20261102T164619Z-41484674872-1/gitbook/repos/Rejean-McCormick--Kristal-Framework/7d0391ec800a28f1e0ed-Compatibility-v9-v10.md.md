<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Compatibility-v9-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 6be045932a059557fa493c17d943926a9129b99d935a9910dff029027ea0b7e1 -->

# Compatibility: v9 Semantic State → v10 Hosted Network

V10 intentionally reuses v9 Logical Artifacts, State Snapshots and commitment profiles. There is **no generic v10 rewrite or rehash requirement**.

| Change | v9 logical revision? |
| --- | --- |
| Rename/move a GitHub repository | No |
| Add a second Host Binding or mirror | No |
| Rebuild an AI/read projection or collection index | No |
| Repack/redistribute a physical materialization | No, if logical content is unchanged |
| Change hosted visibility, workflow or Release locator | No, by itself |
| Change the logical content or exact member commitments | Yes, under the relevant logical contract |

## Draft.2 commitment verifier hardening

The reference JavaScript implementation corrected locale-sensitive comparison and false-positive verification of an unsupported commitment profile. Framework `spec/v10/Semantic-State-Compatibility.md` calls these implementation conformance fixes, not redefinitions of v9 commitments. Preserve historical bytes when investigating objects built by non-conforming implementations; do not silently rewrite old commitments.

## Boundary

Hosting identifiers must not enter the v9 logical or state commitment **unless the domain's own semantic contract explicitly makes those values logical**.

See [[Migration-v9-to-v10]], [[Core-Invariants-v10]], [[Version-Stack-v6-v7-v8-v9-v10]].
