# kOA Graph — Publication bilingue FR / EN / Bilingual publishing

## Français

Cette interface publique est **statique**. Le sélecteur `FR / EN` apparaît dans le centre de pilotage (`docs/index.html`) et dans les observations techniques (`docs/observations.html`). Le choix est conservé localement dans le navigateur (`localStorage`) et peut être préselectionné avec `?lang=en` ou `?lang=fr`. Les sources techniques, documents et rapports demeurent dans leur langue d’origine. **Aucune traduction ne modifie les preuves ni les résultats d’audit.**

Le dépôt comprend déjà `.github/workflows/dashboard-pages.yml` qui publie le répertoire `docs/` sur GitHub Pages. Il faut configurer une fois **Settings → Pages → Build and deployment → Source: GitHub Actions**, pousser les fichiers du système de publication sur `main`, puis **déclencher le workflow manuellement** en choisissant « Tous », « Sélection » ou « Retour ». Depuis la mise en place des publications datées, un push ordinaire ne modifie plus le site public. Voir [Publications datées](PUBLICATIONS_DATEES_FR_EN.md). Les fichiers Python ne s’exécutent **pas** sur GitHub Pages; les campagnes, identifiants et preuves privés restent sur le poste local.

### Déploiement (depuis un clone local)

```bash
# À la racine de Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit
git apply --check koa-graph-bilingual.patch
git apply koa-graph-bilingual.patch
python -m unittest tests.test_documentation_collector tests.test_github_documentation_links -q
git add docs koa_audit tests
git commit -m "feat: publish bilingual FR/EN kOA Graph interface with GitHub docs links"
git push origin main
```

Le patch de la livraison correspond au snapshot fourni du 31 octobre 2026. En cas de modifications récentes du dépôt, vérifier le diff avant application. Le site attendu, **si Pages est activé**, suit le format `https://<owner>.github.io/<repo>/`. Il n’est pas garanti actif tant qu’un déploiement réussi n’a pas été constaté.

## English

The published UI is a **static website**. The `FR / EN` switch is available in the Command Center (`docs/index.html`) and Technical Observations (`docs/observations.html`). The browser remembers the preference locally; `?lang=en` and `?lang=fr` are supported. Source documents, engineering reports and evidence remain in their original language; **translation never changes audit results**.

The repository already includes the GitHub Pages workflow `.github/workflows/dashboard-pages.yml`. In **Settings → Pages**, select **GitHub Actions** as the deployment source. Push the setup files once, then explicitly start the **dated publication** GitHub Actions workflow. Ordinary repository pushes will not update the published site. See [Frozen documentation releases](PUBLICATIONS_DATEES_FR_EN.md). GitHub Pages cannot run Python backends; local private results and campaigns must stay private.
