<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd/README.md | commit: 9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd | SHA-256: 82c6ecf6bf59c9832fda93e4a6c05e80a1e866704ad134f8d3a832606f1c20fa -->

# kristal-public

**Kristal v10 GitHub collection host — public, read-only structural controls, publication sealed.**

This repository holds node metadata, state snapshots, and *eligible* derived read surfaces for explicitly approved Kristals. It is **not** the semantic owner of the hosted states, not the Authoring Kit, not a fact-validation service, and not an automatic publication authority.

> **Current snapshot status (2026-10-12): `BLOCKED` for hosted collection qualification.**
> `kristals/index.json`, the Zoology Manager sync manifest, and Zoology's complete AI read surface are absent in the source snapshot. Its root genesis state is **not** Zoology. No legitimate C1 qualification or C2 approval for public exposure is established by this repository.

## Quick local checks

Python 3.10+; no network, token, credential, or third-party dependency required for these commands:

```bash
python -m unittest discover -s tests -v
python tools/repository_audit.py --repo .
python tools/repository_audit.py --repo . --strict
python tools/c3_collection.py --repo . scan
```

`repository_audit.py` prints a machine-readable, read-only local report: observed node/root identities, discovered slugs, collection integrity, C1/C2 verification status, and managed-file SHA drift. Without `--strict` it returns 0 to allow inspection even of an incomplete repository; with `--strict` it exits nonzero for integrity failures or detected Bootstrap drift.

`scan` and `validate-index` are deliberately **blocked on the supplied snapshot**. A green regression-test job does **not** mean the collection is publishable.

## C1/C2 signed evidence preflight (new — still sealed)

A separate offline tool, `tools/c123_offline.py`, can now verify **real Ed25519 signatures** for externally issued C1 qualification and C2 approval receipts against an independently protected trust policy **outside this repository**, while requiring a clean exact Git commit and a structurally valid C3 collection. It checks exact digest/scope binding, expiration, revocation lists and independent signing keys. **It never authorizes a public write or creates a release**; proof of issuer legitimacy, fresh revocation state, genuine approvals and immutable remote release remain external obligations.

See [Signed C1/C2 Gate](docs/C123_SIGNED_GATE.md) and [Immutable Release Plan](docs/IMMUTABLE_RELEASE_PLAN.md). The current Zoology read surface and index are still absent; current publication state remains **BLOCKED**. Unit tests use ephemeral synthetic signers and do not constitute real approval.

## Repository map

| Path | Purpose |
| --- | --- |
| `.kristal/node.json` | v10 collection node identity and roles |
| `.kristal/bindings/github.json` | Replaceable host locator and declared GitHub visibility |
| `.kristal/capabilities.json` | Declared compatibility and capabilities; not independent proof |
| `.kristal/bootstrap-state.json` | Historical Bootstrap-managed file fingerprints; **do not rewrite automatically** |
| `state/state-snapshot.json` | Collection root/genesis state, with no members |
| `kristals/zoology/state/state-snapshot.json` | Independently identified Zoology v9 snapshot |
| `kristals/<slug>/.kristal/sync-manifest.json` | Manager-generated exact read-surface manifest, when genuinely available |
| `kristals/index.json` | Derived, verifiable collection discovery index, **currently absent** |
| `tools/c3_collection.py` | Local C3 structural index/surface validator and optional candidate index generator |
| `tools/repository_audit.py` | Local status, identity and Bootstrap-drift diagnostics; never authorizes publication |
| `tools/c123_offline.py` | Detached external C1/C2 Ed25519 receipt verification (read-only, no publication permission) |
| `requirements-security.txt` | Optional cryptographic verifier dependency for locally executed C1/C2 checks |
| `.github/workflows/kristal-qualify.yml` | Bootstrap-managed C3 integrity check; fails closed on incomplete collection |
| `.github/workflows/kristal-publish.yml` | Bootstrap-managed **sealed**, read-only candidate check; always blocks publication |
| `.github/workflows/c3-regression-tests.yml` | Independent, read-only Python regression suite for C3 tooling |

## Controlled future ingestion (not performed here)

A **legitimate** first surface must be produced from an authorized domain workspace by Authoring Kit 3.2.4+ and the actual Kristal Manager, with identity, provenance, file list, bytes, ready status and digest verified. On an isolated, access-controlled staging copy, Manager can generate the exact `kristals/<slug>/` surface, its sync manifest, and `kristals/index.json`. Only then can `python tools/c3_collection.py --repo . validate-index` give **structural** PASS. No placeholder or fabricated index is acceptable.

Even a structural PASS does **not** establish independent C1 qualification, authorized C2 public exposure, a verified immutable publication, or activation. A push to a **public** repository already exposes bytes — authorization must precede any public synchronization, PR, upload, or release.

For the detailed sequence, see [Staging Intake](docs/STAGING_INTAKE.md), [C3 Handoff](docs/C3_HANDOFF.md), [Framework Pin Review](docs/FRAMEWORK_PIN_REVIEW.md), and [Release Gate Checklist](docs/RELEASE_GATES.md).

## Boundaries

- Preserve canonical v9 identity and Logical/State Commitments; Git SHA and read-surface digest do not replace them.
- Keep node identity separate from hosted member states. The memberless root genesis **must not** be substituted for Zoology.
- Manager owns read-surface synchronization/index generation; Bootstrap owns node configuration and managed workflow reconciliation; C1 qualifies independently; C2 grants exact authorization; C3 checks hosting integrity.
- Konstellation and Konstellation Light consume approved, policy-checked reader projections; they do not confer knowledge authority.
- The repository's two existing managed GitHub workflows remain deliberately sealed/read-only until owners jointly approve a trusted C1/C2/C3 gate. Changing tracked workflow files would require Bootstrap reconciliation.

**No public publication, activation, remote push, or semantic-state migration was performed in this offline update.**
