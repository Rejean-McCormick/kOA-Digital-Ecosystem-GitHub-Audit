# kOA GitHub Audit v0.22.0 — OVERRIDE DIRECT (aucun patch)

Cette livraison contient **sept fichiers complets** modifiés ou ajoutés, et ce guide. Ce n'est PAS une copie intégrale du dépôt et elle ne contient aucun patch Git.

## Où extraire

Extrais **le contenu** du ZIP directement à la **racine du dépôt `kOA-Digital-Ecosystem-GitHub-Audit`**, là où se trouvent `pyproject.toml`, `README.md` et `kOA_GitHub_Audit_Launcher.pyw`.

- Exemple : `C:\mycode\<chemin-du-depot-audit>\` (adapte au chemin réel).
- **N'extrais pas dans `C:\mycode`** si le dépôt Audit se trouve dans un sous-dossier.
- Fusionne les dossiers `koa_audit`, `tests` et `docs` et accepte le remplacement des fichiers de même nom.
- Sauvegarde auparavant tes changements locaux dans les fichiers qui seront remplacés.

## Fichiers de l'override

- `README.md` — documentation d'utilisation du connecteur.
- `pyproject.toml` — version 0.22.0.
- `kOA_GitHub_Audit_Launcher.pyw` — nouvel onglet « Diagnostic écosystème ».
- `koa_audit/__main__.py` — commandes CLI d'import et de consultation.
- `koa_audit/ecosystem_diag.py` — adaptateur de métadonnées et contrôles de cohérence.
- `tests/test_ecosystem_diag_import.py` — tests automatisés.
- `docs/ECOSYSTEM_DIAG_BRIDGE.md` — contrats et limites du connecteur.
- `INSTALLATION_BRIDGE_AUDIT_FR.md` — le présent guide.

## Vérification et import

Ouvre PowerShell **dans la racine du dépôt Audit** après extraction :

```powershell
py -3 -m unittest tests.test_ecosystem_diag_import -v
py -3 -m koa_audit ecosystem-diag-import --input "C:\chemin\vers\latest.zip"
py -3 -m koa_audit ecosystem-diag-status
```

Ou lance `kOA_GitHub_Audit_Launcher.pyw`, puis **Outils avancés > Diagnostic écosystème** et importe un rapport ZIP, `summary.json`, ou un dossier de campagne.

Les observations normalisées sont stockées localement sous `%LOCALAPPDATA%\kOA-GitHub-Audit\ecosystem-diag\records\`. L'outil ne lance pas de tests de communication, ne modifie pas les applications, ne publie pas les traces et ne transforme pas un résultat importé en certification E2E.

## État de validation

Le connecteur a été testé sur `latest.zip` (13 niveaux, verdict `PARTIAL`). Les tests ciblés avaient réussi sur le snapshot de référence. La suite complète n'était pas entièrement disponible à cause d'une archive privée de revue historique absente. **Aucune modification GitHub distante n'est requise ou effectuée par cette livraison.**

Note : l'audit inventorie 49 dépôts officiels, contre 53 observés par le diagnostic dans le dernier rapport. Ce décalage n'est pas résolu automatiquement.
