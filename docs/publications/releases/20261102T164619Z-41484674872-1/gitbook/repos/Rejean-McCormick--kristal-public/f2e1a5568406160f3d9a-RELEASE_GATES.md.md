<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/88d3e2035d1eedc9234d5c7c2c4bc6694a07311a/docs/RELEASE_GATES.md | commit: 88d3e2035d1eedc9234d5c7c2c4bc6694a07311a | SHA-256: 786eca2611a797f5af8910b06010dcadcacf5b3b641d956bfe07959f4bcba0e2 -->

# Release gates: C3 structural integrity is not publication approval

| Gate | Evidence | Current supplied snapshot |
| --- | --- | --- |
| G0: approved Framework revision | Full SHA and matching v10 contract set, independent of branch names | **NOT VERIFIED** |
| G1: real Kit read surface | Exact non-sensitive, ready files from Authoring Kit, with source state and provenance | **ABSENT for Zoology** |
| G2: Manager sync manifest and collection index | Checked file list/size/SHA, `surface_digest`, `index_digest`, exact state ref | **BLOCKED: index and Zoology manifest absent** |
| G3: C3 structural audit | `validate-index` PASS on exact staged bytes | **BLOCKED** |
| G4: independent C1 qualification | Authenticated receipt bound to exact state/revision/scope | **NOT VERIFIED** |
| G5: C2 authorization before public upload | Real signer, revocation, scope, paths and visibility | **NOT VERIFIED** |
| G6: public synchronization | Protected, reviewed write by authorized operator with exact scope | **NOT AUTHORIZED by this repository** |
| G7: immutable publication | Separate verified release/tag/attestation after approval | **DISABLED in existing workflow** |
| G8: activation / consumer intake | Independently authorized channel and pinned reader release | **NOT VERIFIED** |

The `kristal-qualify.yml` workflow is named historically: its checks are C3 structural checks **only**. It cannot replace C1 or C2. The `kristal-publish.yml` workflow is intentionally `contents: read`, always ends `BLOCKED`, and contains **no** GitHub Release operation.

The `c3-regression-tests.yml` workflow is only a unit-test job and may pass while the actual hosted collection is incomplete. A build, a successful test or a green badge does not authorize a public write. Publishing a pull request containing confidential bytes to a public repository already exposes them; permission must precede that step.

Do not release real Kristals until each gate is proved on the **same exact revision**, with operator and domain-owner approval.
