<!-- Frozen source: https://github.com/Rejean-McCormick/kristal-public/blob/9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd/docs/UPDATE_REPORT_2026-10-27.md | commit: 9a017c89e5fabb6d21f2a97fbe2f55cebd5cb2fd | SHA-256: 9f7e738da82a6de1c9f6d114f6d674326b4d5468ff812531ff0eb7481cdb2a6c -->

# kristal-public — 2026-10-27 reviewable C1/C2 evidence patch

## Input

`kristal-public(1).zip`, 26 source files, supplied in the conversation. No private corpus, Git metadata or genuine approval receipts were supplied.

## Change summary

- **Preserved exactly** all eight protected owner-managed files:
  `.kristal/node.json`, `.kristal/bindings/github.json`, `.kristal/capabilities.json`, `.kristal/bootstrap-state.json`, `.github/workflows/kristal-publish.yml`, `.github/workflows/kristal-qualify.yml`, `state/state-snapshot.json`, `kristals/zoology/state/state-snapshot.json`.
- Existing C3 validator and independent local readiness audit remain unchanged.
- New `tools/c123_offline.py` checks independent signed external C1/C2 Ed25519 receipts, distinct trusted keys, expiration, explicit local revocation, exact clean Git SHA, C3 index/surface digests, state reference/commitment and scoped files. Never returns publication authorization.
- New `requirements-security.txt` and `.gitignore` for Python test caches and private local staging.
- New tests of signed positive synthetic fixtures and deliberate rejection of compromised/expired/revoked/mismatched receipts and dirty/missing Git checkouts.
- The **unmanaged** `.github/workflows/c3-regression-tests.yml` now installs `cryptography` and executes those tests. Bootstrap-managed workflows remain untouched, sealed and read-only.
- New docs detail the external trust policy, receipt wire shape and remaining immutable publication work. Previous source inventory preserved as `docs/historical/SOURCE_UPDATE_INVENTORY_2026-10-12.json`; top-level inventory regenerated for this ZIP.

## Checks

- Before: **20/20** local standard-library unit tests.
- After: **34/34** local tests with `cryptography` installed, including 14 added synthetic signature/negative tests.
- `tools/repository_audit.py --repo .`: **C3 BLOCKED**, because `kristals/index.json` and complete Zoology surface are missing; **5 Bootstrap-managed fingerprints DRIFT**, unchanged from source. C1/C2/immutable publication NOT VERIFIED.
- No live issuer identity, revocation freshness, signature by actual operator, tag-lock protections, GitHub Release, remote code modification or actual public upload tested or performed.

## What is intentionally out of scope

- `cryptography` is an optional dependency of the new verifier, **not** a new public-release capability.
- The ZIP itself is a file snapshot without `.git`; a real signed-receipt preflight needs an actual clean Git checkout and protected external C1/C2 evidence. This cannot pass on this incomplete source snapshot.
- No fabricated Zoology source index, no fake signature authority, and no reactivation of the publication workflow.
- This is not a certified cryptographic protocol or a formally ratified Kristal C1/C2 normative standard. A security and owner review is required before relying on it as input to an external enforcement gate.

## Install/review

Back up the old repository, then replace **code files only** from the archive. Keep existing `.git/` and local data safe. Do **not** assume that copying this archive supplies the missing real source surface/index, and do not use GitSink for publishing. Review Git diff and run:

```shell
python -m pip install -r requirements-security.txt
python -m unittest discover -s tests -v
python tools/repository_audit.py --repo .
```

**Expected:** tests pass, but real release readiness remains BLOCKED. GitHub workflows require owner-reviewed reconciliation with Bootstrap; no workflow in this delivery performs a public write.
