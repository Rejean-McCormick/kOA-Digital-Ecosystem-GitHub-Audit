# Bridge privé : Diagnostic du kOA Digital Ecosystem → GitHub Audit

**Version 0.22.0 — ingestion passive, aucun test relancé.**

## Décision architecturale

Les deux moteurs restent séparés : **Diagnostic du kOA Digital Ecosystem** vérifie les relations inter-repos, API, événements, contrats et parcours E2E ; **GitHub Audit** observe la conformité, les sources et la gouvernance. L'audit n'importe que des **métadonnées normalisées de campagne** du premier outil ; il ne crée ni preuve de sécurité, ni qualification de production, ni validation globale E2E.

## Importer une campagne

Dans l'application Windows : `Outils avancés → Diagnostic écosystème → Importer ZIP / summary.json` (ou `Importer dossier de campagne`). Le ZIP `latest.zip`, qui contient `latest/summary.json` et `latest/levels/Nxx/result.json`, est accepté.

Depuis la racine du dépôt, avec Python 3.11+ :

```powershell
py -3 -m koa_audit ecosystem-diag-import --input "C:\chemin\latest.zip"
py -3 -m koa_audit ecosystem-diag-status
```

Les imports sont stockés par défaut dans `%LOCALAPPDATA%\kOA-GitHub-Audit\ecosystem-diag\records\`. L'option `--out` est possible pour un JSON privé hors de `docs/`. Un `run_id` déjà importé avec une empreinte différente est refusé. Des imports répétés identiques n'écrasent pas les fichiers existants.

## Données retenues

- Schéma et famille source strictement vérifiés : `levelupdiag.campaign-summary.v2` et `Diagnostic du kOA Digital Ecosystem`.
- `run_id`, dates UTC, verdict déclaré, niveaux et leurs verdicts.
- Compteurs limités : dépôts présents/déclarés/tronqués ; relations ; routes et appels API ; corrélations de traces ; parcours E2E déclarés/étayés.
- Hash SHA-256 du résumé et des résultats de niveaux ; validation de cohérence des 13 résultats lorsqu'ils sont fournis.
- Limites explicites : aucune signature indépendante, aucune correspondance garantie avec un HEAD Git, inventaires 49/53 non harmonisés, certification E2E **non établie**.

Les chemins absolus, endpoints, identifiants de corrélation, payloads de traces, descriptions libres de constats et secrets ne sont **pas conservés**. L'archive source n'est pas copiée dans l'audit. Le SHA-256 assure l'identification du contenu importé, **pas** la preuve d'authenticité de son auteur.

## Frontières de confiance

- La provenance et le périmètre restent distincts de l'autorité d'inventaire (`kOA-Digital-Ecosystem`).
- Le registre audit historique par dépôt (`import-legacy`) est distinct de l'import inter-repos ; pas de rattachement automatique de la v5 à un dépôt de l'inventaire.
- `49` dépôts officiels côté audit versus `53` trouvés par le diagnostic : **différence à réconcilier par le registre source**, sans ajout/suppression automatique.
- Les résultats importés ne changent aucun des cinq jalons de qualification, ni les profils, ni les tests internes.
- **GitHub Pages exclu** : aucune donnée du bridge ne doit être injectée dans `docs/data`, les exports publics ou une synchronisation GitHub.

## Limites de la première intégration

La première intégration est un **registre local de campagnes**. Elle n'atteste pas encore chaque frontière individuellement : le snapshot `latest.zip` ne contient pas le fichier détaillé de relations `snapshot.json`. L'étape suivante, après révision du diagnostic kOA, sera d'introduire un contrat d'export de preuves de frontière versionné, avec identifiants officiels et liens vers les preuves privées.
