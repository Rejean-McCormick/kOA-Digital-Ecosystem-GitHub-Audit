<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Versioning-and-Migration | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 6dbb9bd41f1cfe268bbc1a05595ad53fc299ad22c5c60996e5c17174b165bcd9 -->

# Versions, history and migration

**Current code snapshot:** standalone **Skope 0.15.0-alpha.1** (`VERSION`, server constant and Windows launcher). Historical materials are included so maintainers can understand compatibility and safe overlays.

| Version | Main milestone | Migration implication |
| --- | --- | --- |
| 0.13.x integrated | Skope embedded in EncyK pipelines | Historical code/data contract; not the current standalone runtime |
| 0.14.0 | Standalone split from EncyK checkout | Own `skope/` package and scope library; uses existing data files |
| 0.14.1 | One launcher + selectable local Kristal | Remove obsolete Catho-specific launcher; keep local settings and data |
| 0.14.2 | Scope Explorer overlay/dashboard | UX-only overlay; existing graph and acquisition workflows retained |
| 0.14.3 | Individual identity reconciliation | Separate review database and audit; no source roster mutation |
| 0.14.4 | Batch identity triage and research navigation | Rank, stage unverified proposals, export reviewer CSV, attest + atomic commit |
| 0.15.0-alpha.1 | Native v11 Kristal portfolio enrichment (CLI) | Inventories, bounded name discovery, draft/reviewed seeds, verified-source acquisition and claim proposals; **no canonical publication** |

### Package metadata

This release aligns `VERSION` and `skope/api.py::SERVER_RELEASE` to `0.15.0-alpha.1`, and `pyproject.toml` to `0.15.0a1` (PEP 440). Historical README headings describe older milestones; the appended 0.15 section and dedicated release notes describe current features. The browser UI is unchanged aside from version reporting; portfolio workflows remain CLI only.

## Safe upgrade procedure

1. Stop old server(s) using port `8767`.
2. Preserve data on `D:` and local/ignored settings on `C:`.
3. Extract updated standalone code into `C:\mycode\Skope` (not an EncyK code checkout), merging code files as intended.
4. Use **only** `Start_Skope.cmd`; remove obsolete `Start_Skope_Catho.cmd` *if present*.
5. Restart Python and hard refresh the browser (`Ctrl+F5`).
6. Check `/api/config`, `/api/scope-profiles/catalog`, `/api/meta` and `/api/diagnostics/reader`.
7. Test on fixtures before starting long work; no data migration or full dump scan is implied by upgrade.
8. Use a new `--work` directory for each new portfolio input/index identity; do not reuse state from a changed ZIP or source. `Run_Portfolio_Prepare.cmd` defaults to `portfolio-work/` and will refuse a changed source in the same directory.

## Compatibility contract

Skope owns `skope/fastio.py` and `skope/scope_common.py`, but **consumes** historical EncyK compact SQLite and sidecar formats. Compatibility means it reads supported, already-prepared formats; it does **not** promise to create them. Historical on-D QID job/evidence locations are retained.

## Release hygiene recommendation

For the next tag, align `pyproject.toml`, `README.md`, `README_FR.md`, `VERSION` and API release constant. Document migration checks explicitly, without modifying existing evidence. See [Known Limitations](Known-Limitations).
