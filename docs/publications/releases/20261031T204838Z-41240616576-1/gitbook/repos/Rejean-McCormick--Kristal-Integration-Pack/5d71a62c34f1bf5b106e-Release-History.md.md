<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Release-History | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 07ea5e86abfcb97ede9e9986f08c123245eae5f830bb89f6196d95f6578483ad -->

# Release History

## 0.3.0-alpha.1 — October 17, 2026

- Updated the v11 reader pin to **Framework 11.0.0-draft.4** and its 13 reviewed files.
- Added `tools/v11_handoff.py` and `v11-handoff` Node mode for **read-only** diK-to-Kit preflight.
- Added verification of the alpha.7 `dik-job.json` receipt binding, including the content-addressed directory name and idempotency key.
- Confirmed a temporary demo-workspace path with **Authoring Kit 4.0.0-draft.3**: preflight, import/register, explicit select, `check-v11`.
- Preserved historical v6/Kompiler bridge compatibility and existing overlay safety restrictions.
- Recorded **29 Python and 15 Node passing tests** in the source qualification report.

## 0.2.0-alpha.1

- Introduced Framework v11 reading, lexical coverage, derived view and exact contract pinning at the **draft.3** baseline.
- Retained older Konstellation/Kompiler bridge behavior separately.

## Earlier candidate releases

- Developed the guarded local Kompiler CLI and a historical Konstellation overlay with status/preview/rollback.
- Qualified selected local protocol compatibility, but did not establish production multiuser Konstellation, GitHub publishing, or full browser deployment.

Older qualification notes in the source `docs/` are **historical** and must not be silently reused as proof of tests against the latest versions.

See [[Qualification-and-Testing]] and [[Compatibility-Matrix]].
