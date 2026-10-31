# Documentation graph — offline source collection

`docs-collect` builds a **local private documentation index** from an owner-provided `repos.zip` that contains `repos/<folder>/...` trees. It neither runs project code nor extracts source files. Its output is evidence for a *future graph of components*, not a graph of verified runtime integrations or a repository admission decision.

```powershell
python -m koa_audit docs-collect --zip "C:\\path\\repos.zip" --out "reports\\documentation-index.json"
```

The collector reads the audit's 49-repository **baseline** (`data/initial_inventory.json`), rather than silently adding arbitrary ZIP folders to it. Roots matching the baseline are `inventory_match`; roots with a hexadecimal clone suffix and a known base are `snapshot_copy_candidate`; other roots are `unregistered_candidate`. For example **Kolor** and **Karacter** are new candidates relative to the 31 October baseline. Other candidate folders need identity and scope review. A ZIP folder name is not evidence of the remote, origin, current HEAD or version.

The index records a SHA-256 for the input ZIP and each selected document, its relative path, byte count and whether it came from a root document, `docs/` or `wiki/`. It never exports document text, source code, credentials, or qualification conclusions. Unrecognized paths, symlinks and excessive input are skipped or rejected. It does not fetch GitHub data and does not write to the source repositories.

**Private by default:** the index contains paths and must not be copied to GitHub Pages or `docs/`. The command creates a new `.json` file and never overwrites it. The consumer must separately confirm GitHub identity, owner authority, source revision and admissible contracts before turning a document citation into a graph edge or test assertion.

`python -m unittest tests.test_documentation_collector` runs the local unit tests.

## Accès à la documentation sur GitHub

Dans **Applications** et dans les fiches privées de validation, deux liens
indépendants sont disponibles pour chaque dépôt officiel :

- **Documentation GitHub (README)** → `https://github.com/owner/repo#readme`
- **Wiki GitHub (si disponible)** → `https://github.com/owner/repo/wiki`

Le collecteur inclut ces liens dans `github_links` uniquement quand le
`owner/repo` provient de l’inventaire officiel. Il ne devine jamais l’identité
GitHub d’un dossier ZIP inconnu. Les liens ne prouvent pas que README/wiki
existent ou qu’ils sont à jour ; ils n’influencent aucune qualification.

Kolor et Karacter apparaissent séparément dans « Dépôts repérés hors inventaire »
car leurs dépôts GitHub ont été constatés explicitement ; ils ne sont pas
automatiquement admis aux 49 dépôts. Les candidats à afficher sont tenus
à jour dans `docs/data/documentation-candidates.json`.
