# Mise à jour locale — kOA Graph (audit)

Snapshot de base : `znapshot_kOA-D-E-GitHub-Audit_11161842.zip`.

- Entrées « Connexions / Connections » dans l'en-tête, la navigation et la cartographie.
- Page statique bilingue `docs/connections.html`, recherche, filtres et même projection publique JSON que le site Next.js.
- Lien de contexte vers `/connections?repo=...` depuis les fiches d'application quand l'inventaire partagé le permet.
- `scripts/generate-koa-connections.mjs` regénère la projection depuis la copie versionnée du registre local.
- Remplacement du chemin de logo inexistant `docs/assets/logo.svg` par un monogramme `docs/assets/koa-mark.svg` clairement provisoire, sans prétendre restaurer le logo historique.
- L'interface d'audit FR/EN existante et ses sources/qualifications sont préservées.

La diffusion statique concerne uniquement `docs/`. Le snapshot contient des données locales à traiter comme privées. Aucune synchronisation GitHub ni aucun déploiement effectués.
