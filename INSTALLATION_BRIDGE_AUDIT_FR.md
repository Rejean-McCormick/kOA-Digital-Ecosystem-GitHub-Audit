# Patch kOA Digital Ecosystem — GitHub Audit 0.22.0

Ce ZIP est **un overlay de 7 fichiers modifiés/ajoutés**, pas une copie complète du dépôt. Il ne contient pas les données `docs/publications/releases/`, les registres privés ni les rapports de diagnostic. L'outil n'exécute aucune application ou test inter-repos.

## Installation recommandée (Git)

1. Trouver le clone local du dépôt `kOA-Digital-Ecosystem-GitHub-Audit` et sauvegarder tes changements en cours.
2. Placer `KOA_GitHub_Audit_v0.22.0_Diagnostic_Bridge.patch` à un endroit accessible.
3. Ouvrir PowerShell et exécuter :

```powershell
cd "C:\mycode\CHEMIN_REEL_DU_REPO_AUDIT"
git status --short
git apply --check "C:\chemin\KOA_GitHub_Audit_v0.22.0_Diagnostic_Bridge.patch"
git apply "C:\chemin\KOA_GitHub_Audit_v0.22.0_Diagnostic_Bridge.patch"
py -3 -m unittest tests.test_ecosystem_diag_import -v
```

Remplace le chemin de dépôt par le vrai clone local. `git apply --check` refuse les modifications incompatibles et ne modifie rien. N'ajoute pas `--3way` ou `--reject` sans inspecter les conflits.

**Alternative sans Git** : extraire le ZIP à la racine du clone d'audit en fusionnant les dossiers, après sauvegarde des fichiers. Attention : l'extraction peut écraser des changements locaux.

## Importer les résultats v5

Depuis le clone GitHub Audit :

```powershell
py -3 -m koa_audit ecosystem-diag-import --input "C:\chemin\latest.zip"
py -3 -m koa_audit ecosystem-diag-status
```

Dans l'application `kOA_GitHub_Audit_Launcher.pyw`, ouvrir **Outils avancés > Diagnostic écosystème** puis importer `latest.zip` (ou `summary.json`).

Les observations sont conservées sous `%LOCALAPPDATA%\kOA-GitHub-Audit\ecosystem-diag\records\`. Elles ne sont ni publiées ni promues en certification. Les inventaires audit (49) et diagnostic (53) restent à réconcilier avec la source d'autorité.

## Tests effectués

- Import réel de `latest.zip` : 13 résultats LevelUpDiag cohérents, aucun détail de chemin importé, `PARTIAL` conservé.
- `20` tests ciblés réussis, notamment sécurité de ZIP, famille source, refus d'une preuve incohérente, non-certification automatique et CLI existante.
- Démarrage Tkinter testé sous Xvfb et présence du nouvel onglet.
- Le reste de la suite complète ne peut pas être qualifié depuis ce snapshot : l'archive privée `private_evidence/KOA-REVUE-2026-10-30.zip`, requise par 26 tests existants, est absente.

## Déploiement GitHub

Aucune modification de `main` et aucune publication Pages. La création d'une branche GitHub par le connecteur a répondu `403 Resource not accessible by integration`; il faut appliquer ce patch dans le clone puis utiliser Git depuis l'environnement autorisé, après revue.
