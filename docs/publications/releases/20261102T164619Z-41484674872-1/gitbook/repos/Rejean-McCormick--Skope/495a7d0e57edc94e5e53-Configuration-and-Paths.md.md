<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Configuration-and-Paths | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 12d5345b8ebe37f5c915d5959fe2e3d0e702e7b905d80eb28503d8d1a58fc9a4 -->

# Configuration and filesystem paths

## Default deployment

| Component | Source / default | Access intent |
| --- | --- | --- |
| Code repository | `C:\mycode\Skope` | Code and scope JSON |
| Main launcher | `Start_Skope.cmd` | Starts Python 3.12 server on `127.0.0.1:8767` |
| Scope catalog | `<repo>/scopes/*.json` | Validated read of JSON; refreshed in UI |
| Extraction profiles | `<repo>/config/extraction-profiles/*.json` | Read-only profile definitions |
| Workspace settings | `<repo>/config/kristals.local.json` | Local, gitignored selection/paths; written only on user action |
| Kristal discovery | `C:\mycode\Kristal\locals` | Read `kristal.workspace.json` manifests |
| Compact index | `D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite` | **Read only** |
| Dump | `D:\EncyKlopedia\10_sources\wikidata\dumps\current\...json.bz2` | Existing source, **read only** |
| Fast locator and sidecars | `D:\EncyKlopedia\30_working\wikidata-fast` (with compatibility fallback) | Existing access aids, not rebuilt by Skope |
| QID jobs | `D:\EncyKlopedia\30_working\skope-large-scopes/<job>` | New working files |
| Extraction jobs | `D:\EncyKlopedia\30_working\skope-extractions/<job>` | New working files |
| Full-record evidence | `D:\EncyKlopedia\20_evidence\scope-snapshots/<scope>/wikidata-*` | New evidence snapshots |
| Portfolio working state | `--work` argument (`portfolio.sqlite`, CSV, cached lookup and outputs) | New local files only, never a source corpus write |
| `Run_Portfolio_Prepare.cmd` default | `<repo>/portfolio-work` | First-pass working CSV/state; choose another path for large jobs |
| Identity decisions | `D:\EncyKlopedia\30_working\skope-reconciliation/<job>` | Separate reviewer decisions and reports |

**Important:** paths in the bundled extraction profiles refer to a specific historical dump (`wikidata-20260922-all.json.bz2`) and manifest. They are *configuration examples*, **not proof that that dump exists on another installation**. Adapt profiles in a controlled manner only after matching the verified local source.

**Portfolio prerequisites:** the existing compact index is used for discovery, while the already verified full dump and fast locator are needed for `skope portfolio acquire`. An installed extraction profile chooses that source; its filename/domain label does not filter the portfolio. Portfolio state pins the input source and index identity; change either and use a **new** work folder.

## Overrides

- `SKOPE_DB` is the default database for `python -m skope` unless `--db` is explicitly supplied.
- The bundled launcher uses an explicit `--db` value, which takes precedence over `SKOPE_DB`.
- `KRISTAL_LOCALS_ROOT` changes the default scan root before server startup.
- `--kristal <folder>` selects an initial workspace for CLI/scripted starts; selection is also possible in the UI.
- `--host` must be `127.0.0.1`, `localhost`, or `::1`; `--port` defaults to `8767`.

## Data-root contract for large jobs

QID collection and extraction derive their data root from the index location. For those workflows, the SQLite file must reside under a directory literally named `30_working/wikidata`. Simply passing any arbitrary test `.sqlite` path may allow a read-only preview but **will not** satisfy their working-directory checks.

Do not put secrets or private workspace paths into the committed scope profile library. No complete production corpus is bundled with Skope.
