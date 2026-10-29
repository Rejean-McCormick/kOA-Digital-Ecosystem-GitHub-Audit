# Tableau de bord GitHub Pages

1. Dans l'application : onglet **Tableau de bord**, bouton **Publier sur GitHub (1 clic)**.
2. Si nécessaire, sur le dépôt d'audit GitHub : **Settings > Pages > Build and deployment > Source : GitHub Actions** (une seule fois).
3. Le workflow `.github/workflows/dashboard-pages.yml` déploie automatiquement le site à chaque modification de `docs/` sur `main`.
4. Pour actualiser les données, utiliser le bouton de publication; aucun audit global n'est relancé.

Sans rapport récent, le bouton utilise l'historique agrégé intégré. Les données publiées sont des compteurs anonymisés, et non des fichiers de diagnostic. Git doit être déjà authentifié sur le PC; aucun jeton ne doit être entré dans l'interface.
