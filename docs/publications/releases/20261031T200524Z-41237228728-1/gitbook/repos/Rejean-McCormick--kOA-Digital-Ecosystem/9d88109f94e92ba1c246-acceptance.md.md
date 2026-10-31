<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/orchestration-c0/acceptance.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: c38b2b73e9998d0d2d588a3617c43d80c736a53b1da9a414a0f3ec84d0933da7 -->

# C0 — Evidence-based acceptance criteria

| Gate | Evidence required | Can C0 assert passed now? |
|---|---|---|
| A1: Zoology local state reconstructs | `check`, domain tests, `build-v9`, stable v6/v9 commitments | **Yes, local/internal only**, from C0 investigation |
| A2: Zoology independent v10 qualification | Diag report with exact input commit/digests, schema + manifest proofs | **No** |
| A3: Public eligibility | Explicit authorization scope for Zoology + policy/rights review + no disallowed bytes | **No** |
| A4: Github sync & publication | Manager sync manifest, verified qualification, immutable release, exact commit & receipt, replay/abort tests | **No** |
| A5: Light catalogue | Verified collection index + readable revision(s), rehydration and UI tests, post-publish event | **No** |
| A6: Kompiler read-only | v10 adapter / Context Pack verified with immutable input provenance | **No** |
| A7: EncyK→Médiathèque handoff | Real consumer's receipt; duplicate/replay/invalid digest/refusal tests | **No** |

## Zoology reference values (verification fixture, never an approval)

- State ref: `urn:kristal:state:kristal-zoology`.
- State commitment: `sha256:2503493eed8b2515107f9c32eed48286845f5468838ad3ae7b4a8f66a65f2ac8`.
- Portable artifact commitment: `sha256:f0d64c2bdfa8fe860449eea1a3e6e6b96a0b55aa76a5b5c5f13a3ebf1c5e7f56`.
- Rebuilt `build-v9` matches historical snapshot (internal check only). Domain tests 5/5; domain validator PASS. `build-ai` + `check-ai` passed on private temporary copy, **not enabled** in the original workspace snapshot.
- Public repository snapshot currently contains Zoology **state only** and no `kristals/index.json` in the supplied copy; its root state is distinct and empty. Light still bundles `demo-v9-small`.

Acceptance needs **results from the actual consuming and publishing interfaces**, not just a good-looking screenshot or a unit-test green badge.

## Additional v10 navigation gate (2026-10-12)

**A8: fleet navigation** — Konstellation can list **authorized** local instances via a Manager-provided read-only interface, keep private names/counts inaccessible to unauthorized users, distinguish local/hosted/unready/revision status, and enter/return from a selected Kristal. Until a fixture and browser E2E tests exist, **C0 cannot assert A8 passed**. Hosting-only v10 file topology is not generic semantic concept navigation.
