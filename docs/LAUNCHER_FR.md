# Lanceur Windows — audit 100 % local

## Démarrage

1. Décompresser **tout** le ZIP.
2. Double-cliquer sur `kOA_GitHub_Audit_Launcher.pyw` (Python 3.11+ avec Tkinter).
3. Onglet **Audit local** : choisir la racine où se trouvent les dépôts, habituellement `C:\mycode`.
4. Cliquer sur **Découvrir les dépôts locaux**. Confirmer les chemins détectés.
5. Cliquer sur **Scanner localement**. Le traitement reste en lecture seule et le journal s'affiche à l'écran.
6. Onglet **Rapports** : consulter `SUMMARY.md`, `audit.csv`, `audit.json`.

**Aucun jeton GitHub, aucune connexion réseau, aucune configuration de compte.**

- **Profondeur** : combien de niveaux de dossiers explorer (4 par défaut).
- **Nombre de dépôts** : `0` pour tous ; `5` pour tester d'abord cinq dépôts.
- **Max fichiers par dépôt** : limite l'inspection ; un dépôt tronqué est marqué `PARTIAL`.
- **Limiter à l'inventaire** : sinon tous les Git locaux sont scannés, y compris les projets nouveaux.
- **Diagnostics historiques** : ne cocher que si le dossier d'imports normalisés existe.

La présence de fichiers CI, Dependabot ou CodeQL indique seulement une **configuration locale**. Aucun workflow distant n'est exécuté. Les recherches de secrets sont basées sur des expressions régulières heuristiques, et aucune base CVE n'est consultée.

## Si la fenêtre ne démarre pas

Lancer `DIAGNOSTIC_LAUNCHER.cmd` : les erreurs Python restent visibles. Le journal externe est situé dans `%LOCALAPPDATA%\kOA-GitHub-Audit\launcher-startup.log`. Si le `.pyw` est lancé seul, il permet de sélectionner le dossier complet du projet, mais il ne contient pas le scanner à lui seul.

## Ligne de commande (sans interface)

```powershell
python -m koa_audit local-plan --root 'C:\mycode'
python -m koa_audit local-audit --root 'C:\mycode' --out reports
```

## Confidentialité

Les rapports contiennent des chemins locaux et des indicateurs potentiellement sensibles : ne pas les publier. Les contenus de secrets ne sont jamais exportés. Aucun fichier du dépôt audité n'est modifié.
