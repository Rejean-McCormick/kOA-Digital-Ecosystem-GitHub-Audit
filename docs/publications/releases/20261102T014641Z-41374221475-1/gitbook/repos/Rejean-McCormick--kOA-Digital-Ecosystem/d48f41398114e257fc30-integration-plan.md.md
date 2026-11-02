<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/40-integration/orchestration-c0/integration-plan.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: fe00d0f368533d8c704a95076056b5cbbfae1a0e38675bca60f12030c32cd921 -->

# C0 — Workstream integration plan

| ID | Component owner | Start now | Integration depends on | Return to C0 |
|---|---|---|---|---|
| **C1** | Framework + Authoring + KristalDiag | Local qualification, current v10 read surface and proof fixture | Independent v10 proof accepted by C2/C3 | immutable sample, exact versions/commit, test results, receipts, schema validation |
| **C2** | Manager + GitHub Bootstrap | Policy implementation against private/synthetic fixtures | C1 evidence contract; specific authorization before public writes | revocable per-Kristal approval, exact file scope, fail-closed paths, replay tests |
| **C3** | `kristal-public` | Prepare default-state correction, collection-index build and tests privately | C1, C2, human Zoology authorization | correct state path, valid collection index, immutable release verification, post-release event |
| **C4** | Konstellation Light | Build verified external-collection reader on synthetic data | C3 release/index contract | reproducible catalog, versions, deep links, UI tests, last-known-good deploy behavior |
| **C5** | Kompiler + Integration Pack | Requalify bridge against 0.8; read-only fixture | C1/C3 qualified fixture for real E2E | tested Context Pack with provenance and no canon writes |
| **C6** | EncyKlopedia + Médiathèque | Bilateral v2 handoff receiver/receipts | C0 updates central historical + current map after C6 evidence | mapping, idempotency, integrity, rejection/retry tests, consumer receipt |

C0 remains responsible for cross-owner dispute resolution and status updates, **not** implementing any of those owner operations. C6 is independent of C3/C4 until a specific dependency is demonstrated.

## Merge rule

1. Isolated PRs in owning repositories may be prepared concurrently.
2. A shared interface cannot be merged as *qualified* until both producer and consumer sign off on exact versions and test evidence.
3. Publication- or visibility-changing steps require the upstream qualified receipts and user-specific authorization before entering public repositories.
4. C0 updates map/status only when the evidence is linked to the actual code artifact and has the appropriate integration scope.

## End-of-work report

```text
WORKSTREAM:
OWNER REPOSITORY / BRANCH / COMMIT:
PRODUCER → CONTRACT VERSION → CONSUMER:
CHANGED FILES:
TESTS RUN + RESULTS:
ARTIFACTS / RECEIPTS / DIGESTS:
BREAKING CHANGES OR NEW DEPENDENCIES:
UNRESOLVED DECISIONS / APPROVAL NEEDED:
C0 REGISTRY ROWS TO UPDATE:
SAFE NEXT INTEGRATION:
```

## Additional program lane — fleet navigation / harmonization

`C0-01` → obtain exact owner commitments, complete Manager runtime, approve v10 pins. `KNAV-01` (Manager read-only inventory) → `KNAV-02` (Konstellation local + qualified GitHub fleet aggregation) → `KNAV-03` (My Kristals browsing/enter/return). `KNAV-04` (concept-level semantic adapter) requires Kompiler/semantic read contracts; `C3-02` is a prerequisite only for **hosted** entries, not a read-only local inventory pilot. Arketype contributes explicit noncanonical pattern hints, not a second instance registry.

See [machine-readable v10 workstreams](../kristal-v10-alignment/workstreams.json) and [decision record](../kristal-v10-alignment/decisions.md). Existing C1–C6 release gates remain unchanged.
