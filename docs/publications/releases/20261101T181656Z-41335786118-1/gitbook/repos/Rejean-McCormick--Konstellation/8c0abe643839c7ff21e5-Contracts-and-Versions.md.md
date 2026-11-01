<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Contracts-and-Versions | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 9a739a563d90bb131e13cbce2f4c58d0c754db785dee018ae2d018d01719c732 -->

# Contracts, Versions, and Normative Status

| Component | Reference in the examined sources | Scope |
| --- | --- | --- |
| Konstellation | `1.0.0-rc.2` | Application release candidate; final qualification not achieved |
| Kristal Framework | `10.0.0-draft.3.2` | **Proposed** network standard retaining the v9 state model |
| Semantic state | `schema_version: "9.0"` | Artifacts, snapshots, commitments, materializations |
| Reader Discovery | `kristal.discovery/1.0` | **Noncanonical** discovery declaration |
| Reader Inventory | `kristal.reader-inventory/1.0` | Recorded files and fingerprints |
| Reader Profile | `kristal.reader-profile/1.0` | Reader guidance, not permissions |
| Local Manager | `kristal.manager-local-inventory/0.1-candidate` | Candidate operational export |
| Manager alpha.14 | `kristal.manager-operational-assessment/0.2-candidate` | Local diagnosis, not a certificate |
| Konstellation relation registry | Repository JSON Schema contract, version 0.2 | Domain limited to 10 types per definition |
| NavigationPlan / projections | Repository 1.0 contracts | **Derived** rendering plans and projections |

## Critical distinctions

```text
File SHA-256 ≠ State Commitment
Git commit ≠ State Commitment
Fresh Discovery ≠ certified canonical integrity
Manager export ≠ permission to read
Build ≠ C1 qualification
Synchronization ≠ immutable publication ≠ activation
Read projection ≠ Kristal canon
```

The Framework defines conformance contracts; a reader **does not replace** its verifiers. Manager can coordinate local diagnostics; it does not become an epistemic authority.

## Sources of truth

Exact definitions are found in Konstellation's `contracts/*.schema.json` and the Framework's `contracts/`, `spec/v9/`, `spec/v10/`, and `profiles/reader-discovery/`. This wiki reports what was **observed in the snapshots** and changes no contracts.

See [[Ecosystem and Responsibilities|Ecosystem-and-Responsibilities]] and [[Manager and Discovery|Manager-and-Discovery]].
