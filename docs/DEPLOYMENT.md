# Tableau de bord GitHub Pages

1. Dans l'application locale, le bouton **Publier sur GitHub** prépare les données publiques dans le dépôt; il ne déploie **plus automatiquement** le site public.
2. Sur le dépôt d'audit : **Settings > Pages > Build and deployment > Source : GitHub Actions** (une seule fois).
3. Pour figer une nouvelle version : **Actions → kOA Graph - publication datee FR EN → Run workflow**. Choisir `selected` ou `all`, avec `preview_only=true` d'abord; `preview_only=false` déclenche l'approbation et la publication.
4. Les pushes dans `docs/` ne déclenchent plus de déploiement : seul le workflow manuel approuvé change la version publique.
5. Le mode `rollback` permet de republier une version datée antérieure. Voir [guide complet](PUBLICATIONS_DATEES_FR_EN.md).

Sans rapport récent, le bouton utilise l'historique agrégé intégré. Les données publiées sont des compteurs anonymisés, et non des fichiers de diagnostic. Git doit être déjà authentifié sur le PC; aucun jeton ne doit être entré dans l'interface.

## Interface bilingue kOA Graph / Bilingual UI

Le sélecteur **FR / EN** est inclus dans `docs/index.html` et `docs/observations.html`, sans build ni GitBook. Voir [le guide de publication](PUBLISH_FR_EN.md) pour les réglages Pages et la protection des données privées.

The **FR / EN** language switch is included in the two public UI pages. Existing `.github/workflows/dashboard-pages.yml` publishes `docs/` directly. No GitBook or additional hosting is required.

## Graphe source et interface unifiée (mise à jour 2026-10-31)

Pour publier le graphe de composants, appliquer d'abord `docs/inventory/graph-registry.v1.json` dans **kOA-Digital-Ecosystem**, puis mettre à jour le code de **GitHub Audit**. Lancer `mode=all` une première fois pour figer ce registre source avec la documentation; utiliser ensuite `mode=selected` pour actualiser certains dépôts, ou `mode=republish` pour mettre à jour uniquement la présentation.

Sur GitHub Pages, l'onglet Applications est la page d'accueil; chaque fiche peut ouvrir les documents **copiés à la date de publication**. L'application Windows conserve seule l'audit privé.
