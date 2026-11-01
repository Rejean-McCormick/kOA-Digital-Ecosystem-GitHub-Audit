<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Status-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 0509258f8bac86e527f9604c05cba866917eade5668ac146e588b852ba48deae -->

**Historical v10 reference:** this page documents the frozen v10 hosted-network baseline. The **current proposed Framework draft is v11 `11.0.0-draft.4`**; see [[Home]], [[Kristal-v11]] and [[Status-v11]]. Its semantic identity/dictionary contracts are additive, not a replacement for historical v10 hosting.

---

# v10 Status & Compatibility Baseline

| Area | Status in the supplied snapshots |
| --- | --- |
| Framework proposed standard | `10.0.0-draft.3.2` — additive Reader Discovery profile |
| Semantic foundation | v9 State Snapshots and commitments unchanged |
| Inherited capability layers | v6 + v7 + v8 + v9 |
| GitHub reference host | `kristal.host/github/1.0` (optional profile) |
| Local/Authoring Kit | `3.3.0` (Reader Discovery producer) |
| Kristal Manager | `0.1.0-alpha.11` |
| GitHub Bootstrap/Setup | `1.1.0-alpha.10` |
| KristalDiag snapshot | v10 examiner; its README **targets `10.0.0-draft.2`**, not confirmed qualified for Framework draft.3 |

## What changed since v9

- **Draft.1/v10:** node manifests, host bindings, publications and directories around unchanged v9 state.
- **Draft.2:** tightened validation, verifiable publication bundles, managed GitHub workflow controls and commitment implementation hardening without redefining v9 commitments.
- **Draft.3.2:** noncanonical Arketype/reader-discovery profile, optional and separate from frozen v9 semantic commitments.
- **Draft.3:** GitHub AI/read-surface verification and collection indexes for scalable collection traversal, while preserving v9 semantics.

The Framework version, the diagnostic examiner's pinned target, and each tool version are **different version dimensions**. A successful check against one snapshot is not proof of full qualification against every later draft.

## Status interpretation

Draft is not the same as final. Capability claims should identify actual supported profiles and verification evidence; a validator's PASS is not epistemic authority.

See [[Conformance-v10]], [[Compatibility-v9-v10]], [[Toolchain-v10]] and [[Status-v9]] (historical v9 status).

*Sources: Framework `docs/00_STATUS.md`, `spec/v10/Conformance.md`; tool repositories' `VERSION` and `README.md` files in the supplied snapshots.*

**Updated local baseline:** Framework 10.0.0-draft.3.2 is the version of the updated package, not a claim that all companion tools have been qualified against it. The Manager/Bootstrap/Diag versions shown above refer to the older supplied snapshots and remain independently pinned. See [[Reader-Discovery-and-Arketype-v10]].
