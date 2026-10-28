# kOA-Digital-Ecosystem-GitHub-Audit

> **Centralized, read-only GitHub auditing for the kOA Digital Ecosystem. Monitors repository security, GitHub Actions, CodeQL, Dependabot, secret scanning, and validation coverage. Produces consolidated, traceable reports without modifying source repositories.**

## Why this repository exists

`kOA-Digital-Ecosystem` remains the architectural and inventory reference. This separate repository observes GitHub security and CI for the declared perimeter, while **preserving existing owners, workflows, qualified diagnostic evidence and authority boundaries**. This is not a new source of truth for product state, not a release approver, and not a remote scanner executor.

The supplied snapshot dated 2026-10-28 declares **49 public repositories** owned by `Rejean-McCormick`. The copy in `data/initial_inventory.json` removes local Windows checkout paths and is for offline bootstrap only. The scheduled workflow retrieves the **latest inventory from its owning repository pinned to a specific Git commit** and records the source commit and SHA-256 in the audit output. A snapshot does not prove all those GitHub repositories are currently accessible.

## What OBSERVE v0.2 implements

- Repository metadata including default branch, archived/disabled and pushed-at (no writes).
- Existing GitHub Actions workflow inventory and a bounded sample of default-branch runs.
- CodeQL *analysis evidence* on the default branch: most recent analysis age and commit, not just zero alerts.
- Open Dependabot alerts, code-scanning alerts and **counts only** for secret-scanning alerts. Access errors stay **UNKNOWN**, never zero.
- Explicit `ok`/`partial`/`unknown` observations, with pagination caps and contextual caveats.
- Historic diagnostics imported from **KonnaxionDiag, KorDiag, KristalDiag, LevelUpDiag Orgo, SemantiK Architect, Skope**, kept separate as non-authoritative, not reverified evidence.
- JSON, CSV (Excel-safe), concise Markdown summary, GitHub Actions weekly schedule, offline unit tests.
- Optional public-owner discovery to identify repositories missing from the declared inventory (not automatically adding them).

**Not included:** triggering CodeQL, cloning repositories, running arbitrary repository commands, branch protection proof, changing security settings, automatically fixing code, publication/release authorization, proving every language scanned, certified compliance, production runtime scanning, automatic trust verification of legacy attestations.

## Interface graphique Windows (.pyw) — startup diagnostiqué

Après extraction complète du ZIP, double-cliquer sur **`kOA_GitHub_Audit_Launcher.pyw`** (Windows, Python 3.11+ avec Tkinter). Si le fichier `.pyw` a été téléchargé seul, un assistant propose maintenant de sélectionner le dossier de projet extrait. En cas de fenêtre absente, utiliser **`DIAGNOSTIC_LAUNCHER.cmd`**, qui garde les erreurs visibles et indique un journal de démarrage dans `%LOCALAPPDATA%/kOA-GitHub-Audit/launcher-startup.log`. Trois onglets : **Audit GitHub** (prévisualisation hors ligne ou audit OBSERVE), **Import historique** (association explicite des rapports au dépôt cible) et **Rapports** (aperçu + ouverture des fichiers). L'interface reste réactive pendant l'exécution et offre une annulation. Aucun jeton n'est demandé, affiché ou enregistré par l'interface ; `KOA_AUDIT_TOKEN` / `GH_TOKEN` doit être présent dans son environnement pour les accès authentifiés.

Voir le [guide du lanceur Windows](docs/LAUNCHER_FR.md). Il ne modifie aucun dépôt cible et ne remplace pas les commandes CLI ni l'automatisation GitHub Actions.

## Quickstart

Python 3.11+; standard library only for runtime and tests.

```bash
# Offline scope preview: no GitHub connectivity required
python -m koa_audit plan --inventory-source bundled

# Small pilot; will query the GitHub API
export KOA_AUDIT_TOKEN='YOUR_READ_ONLY_TOKEN'  # set in your shell, never commit
python -m koa_audit audit --inventory-source bundled --limit 5 --out reports

# Full review against live inventory pinned to its current Git commit
python -m koa_audit audit --inventory-source github --require-auth \
  --discover-public-owner --workers 3 --out reports

# Offline tests
python -m unittest discover -s tests -v
```

Windows PowerShell:

```powershell
$env:KOA_AUDIT_TOKEN = "YOUR_READ_ONLY_TOKEN"
python -m koa_audit plan --inventory-source bundled
python -m koa_audit audit --inventory-source github --require-auth --out reports
Remove-Item Env:KOA_AUDIT_TOKEN
```

A classic PAT is not recommended for production. Prefer a **GitHub App installation token** with repository permissions: Metadata read, Contents read (to read the authoritative inventory), Actions read, Code scanning alerts read, Dependabot alerts read, Secret scanning alerts read. Some features require a suitable plan and additional GitHub settings. See [Deployment](docs/DEPLOYMENT.md).

## Outputs

- `reports/audit.json`: redacted, machine-readable observations and source inventory provenance.
- `reports/audit.csv`: one row per repository; `UNKNOWN_OR_PARTIAL` instead of a misleading zero.
- `reports/SUMMARY.md`: high-level coverage counts and alert lower bounds.

Reports can contain sensitive operational metadata. **Keep this repository and its artifacts private**. `reports/` is gitignored; workflow artifacts are retained for 14 days. No raw secret values, finding code snippets, API response bodies or legacy free-text findings are exported.

## Historical diagnostics integration

Existing specialist validators are not replaced. The `import-legacy` command accepts a **known summary JSON schema only** (or an exact member of a ZIP archive), stores SHA-256 provenance, tool, campaign, verdict and sanitized level counts, and marks all imported records as `historical_legacy`, `evidence_independently_verified=false`, `current_security_conclusion=NOT_ASSESSED`.

Example with the Orgo historical summary provided in your snapshot (change the path to your own):

```bash
python -m koa_audit import-legacy \
  --tool LevelUpDiag-Orgo --repo Rejean-McCormick/Orgo \
  --input 'LevelUpDiag-Orgo_Code_snapshot(1).zip' \
  --member verification/embedded/summary.json \
  --out .legacy/orgo-2026-10.json

python -m koa_audit audit --inventory-source github --require-auth \
  --legacy-dir .legacy --out reports
```

**Explicit target binding is mandatory.** The diagnostic tool's own repository is not always its target. `Kor` is not in the current 49-repository snapshot; a KorDiag import must not be silently relabeled as another repository. Legacy records for targets outside the selected inventory are counted as out of scope, not merged into other repositories.

See [Legacy sources](docs/LEGACY_DIAGNOSTICS.md) and [Architecture and trust](docs/ARCHITECTURE.md).

## Authority and integrity

1. `kOA-Digital-Ecosystem` owns the declared scope and architectural definitions.
2. GitHub owns its workflow runs, alert records and analysis metadata.
3. Each specialist diagnostic owns its qualification semantics and native evidence formats.
4. This repository owns **only observational aggregation**. It neither verifies prior cryptographic assurances nor grants acceptance, release or execution authority.
5. A `PASS` from a historic diagnostic is *not* a current security `PASS`; an API `404`, `403` or truncated result is *not* an empty alert list.

## Docs

[Architecture](docs/ARCHITECTURE.md) · [Lanceur Windows](docs/LAUNCHER_FR.md) · [Deployment](docs/DEPLOYMENT.md) · [Legacy diagnostics](docs/LEGACY_DIAGNOSTICS.md) · [Operations](docs/OPERATIONS.md) · [Security](SECURITY.md)

## License

No open-source license has been selected. Consult the owner before reusing or distributing outside this repository.

[Data contracts](docs/CONTRACTS.md) define the independent, non-authoritative observation formats. No cross-system authority is transferred by normalization.

**Documentation française :** [Guide rapide](docs/GUIDE_FR.md).
