# Guide rapide — kOA Audit local

Le mode recommandé est **LOCAL_OBSERVE** : un audit en lecture seule des copies Git sur votre ordinateur. Aucun jeton GitHub ni accès Internet n'est requis. Ouvrez `kOA_GitHub_Audit_Launcher.pyw`, choisissez `C:\mycode` ou votre répertoire de projets, puis cliquez sur **Scanner localement**. Le rapport est placé dans `reports/`.

Les vérifications couvrent les fichiers GitHub Actions, la présence des configurations CodeQL/Dependabot, les manifestes de dépendances et quelques règles de sécurité statiques. Elles n'exécutent pas les workflows et ne vérifient pas les vulnérabilités par base CVE. Les résultats historiques des outils spécialisés restent des preuves distinctes, sans promotion en état de sécurité actuel.

Voir [Launcher](LAUNCHER_FR.md) et [README](../README.md).
