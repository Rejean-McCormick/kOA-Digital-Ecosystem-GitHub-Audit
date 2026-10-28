# Guide rapide — kOA-Digital-Ecosystem-GitHub-Audit

Ce dépôt est un **observateur central, pas un outil de correction**. Il utilise l'inventaire officiel de `kOA-Digital-Ecosystem`, lit les validations GitHub déjà en place et peut consolider des résumés historiques de diagnostics spécialisés. Il ne modifie aucun des dépôts cibles.

## Interface Windows

Pour utiliser le dépôt sans terminal, **double-cliquer sur `kOA_GitHub_Audit_Launcher.pyw`** (Windows avec Python 3.11+ / Tkinter). Prévisualiser d'abord le périmètre avec l'inventaire `bundled`, puis lancer un audit en lecture seule avec un jeton configuré. Consulter les rapports dans le troisième onglet. [Instructions complètes](LAUNCHER_FR.md).

## Mise en route

1. Créer un dépôt GitHub **privé** nommé `kOA-Digital-Ecosystem-GitHub-Audit`.
2. Copier tous les fichiers de cette archive à sa racine.
3. Exécuter `python -m unittest discover -s tests -v` : les tests sont hors ligne.
4. Exécuter `python -m koa_audit plan --inventory-source bundled` : affiche le périmètre initial de 49 dépôts sans accès réseau.
5. Configurer une GitHub App en **lecture seule**, installée sur les dépôts visés. Renseigner la variable Actions `KOA_AUDIT_APP_ID` et le secret `KOA_AUDIT_APP_PRIVATE_KEY`.
6. Dans **Actions**, lancer le workflow « kOA ecosystem GitHub observation » manuellement. Consulter l'artifact `koa-github-observation`.
7. Vérifier les permissions refusées, contrôles non observés, dernières analyses CodeQL et doublons éventuels avant d'envisager un ajout de contrôles.

## Importer les anciens diagnostics

Les sources gérées sont KonnaxionDiag, KorDiag, KristalDiag, LevelUpDiag-Orgo, LevelUpDiag-SemantiK et LevelUpDiag-Skope. Un import explicite accepte un JSON de synthèse ou un membre précis d'un ZIP :

```powershell
python -m koa_audit import-legacy `
  --tool LevelUpDiag-Orgo `
  --repo Rejean-McCormick/Orgo `
  --input "LevelUpDiag-Orgo_Code_snapshot(1).zip" `
  --member "verification/embedded/summary.json" `
  --out ".legacy/orgo.json"

python -m koa_audit audit --inventory-source github --require-auth `
  --legacy-dir .legacy --out reports
```

La synthèse conserve le verdict natif et la provenance de l'ancien outil **sans valider les signatures ni prouver qu'il est encore à jour**. Les autres projets de l'inventaire restent sans verdict historique jusqu'à import explicite de leurs véritables rapports.

## Interprétation

`UNKNOWN` n'est jamais un résultat sain. `PASS` historique ne vaut pas `PASS` de sécurité actuelle. Zéro alerte ouverte ne prouve pas qu'une analyse CodeQL a été lancée. Certaines validations sont locales (Windows, VPS, Android, serveur, environnement externe) et ne doivent pas être relancées à l'aveugle dans GitHub Actions.

Pour le détail des permissions, lire `docs/DEPLOYMENT.md`. Pour les limites et les frontières d'autorité, lire `docs/ARCHITECTURE.md`.
