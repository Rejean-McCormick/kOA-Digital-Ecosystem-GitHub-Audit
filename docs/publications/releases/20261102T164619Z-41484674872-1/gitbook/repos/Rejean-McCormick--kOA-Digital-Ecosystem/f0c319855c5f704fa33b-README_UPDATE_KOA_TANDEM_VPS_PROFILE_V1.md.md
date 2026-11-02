<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/README_UPDATE_KOA_TANDEM_VPS_PROFILE_V1.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: fdb83029a120df3ce30c661d18c56bed6c72455c72fa672717f585e315e1ce67 -->

# kOA Digital Ecosystem — Tandem VPS Docker Capsule Agent profile (C0 V1)

**Install target:** `C:\mycode\kOA_Digital_Ecosystem`. Extract this ZIP **at the root of that repository**, not inside Capsule Manager or KonnaxionDiag.

**Intent:** record the user's choice of **Linux VPS + Docker + Konnaxion Capsule Agent** as first final tandem profile, without changing the architecture authorities and without claiming remote Agent deployment or GO LIVE. No online service, API, Neon, PostgreSQL Orgo, key or private data is touched. All repo documentation is **English**, as required by `AGENTS.md`.

## Commands — PowerShell 7

```powershell
cd C:\mycode\kOA_Digital_Ecosystem
.\PREVIEW_KOA_TANDEM_VPS_PROFILE.cmd
.\INSTALL_KOA_TANDEM_VPS_PROFILE.cmd
.\VERIFY_KOA_TANDEM_VPS_PROFILE.cmd
```

Run `ROLLBACK_KOA_TANDEM_VPS_PROFILE.cmd` only if needed; it refuses to overwrite newer changes.

The installer checks SHA-256 before writing, tests a staged copy **before** updating source files, saves originals in `C:\mycode\Tandem_Local\koa_vps_profile\backups`, then verifies. Re-running is idempotent. A local repo file that differs from the original snapshot or desired patch blocks installation without overwriting anything. Python 3.10+ is required. The installer **does not install packages or automatically push/publish**.

## Exact scope

- New machine-readable C0 VPS profile (`deployment-profile.json`), decision log, owners, G0–G8 acceptance and evidence ledger.
- Links from repo root, technical docs, release operations, authority map and current status.
- A standard-library validation script + ten permanent negative/positive tests, included in CI. The frozen Kristal v6 knowledge-projection registry and the ten historical C0 interface entries are **unchanged**.

**Already observed (local):** FakePlant E2E + Lot1A (40 targeted tests) + Lot1B (71 tests) have user-provided results. **Pending:** Lot1C Agent-owned measurement/Ed25519 KonnaxionDiag PEP invocation; exact deployed images/host/commit; VPS test, recovery, final release G0–G8. This ZIP **does not patch Capsule Agent** and does not configure a VPS.

The command scripts pause at the end only so error output remains visible; they do not ask for a confirmation or authorization.
