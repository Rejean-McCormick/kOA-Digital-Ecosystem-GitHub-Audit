<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/runbooks/UPGRADE.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: e9366fc235dc5ec5243b0f571bde9cd539689ee41a0b0cc7debce93d70c7fa73 -->

# Runbook — Upgrade

1. Lire `CHANGELOG.md` et `docs/08-migration.md`.
2. Vérifier les versions de contrats exposées par `/api/version`.
3. Régénérer/valider le lockfile avec Node supporté.
4. Exécuter `npm ci && npm run release:check`.
5. Tester un import Kristal v6 avec loss report.
6. Tester migration d’un ExplorationState ancien si applicable.
7. Déployer en canary/staging.
8. Comparer erreurs, latence, recettes et taux de troncation.
9. Promouvoir ou rollback atomiquement.
