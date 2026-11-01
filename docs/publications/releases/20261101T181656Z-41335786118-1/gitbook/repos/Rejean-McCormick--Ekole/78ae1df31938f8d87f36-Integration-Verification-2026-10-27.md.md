<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/blob/0ae6f634e223b7e2fafd68faf6f151730578e490/docs/Integration-Verification-2026-10-27.md | commit: 0ae6f634e223b7e2fafd68faf6f151730578e490 | SHA-256: c7bc430fb4aca3f4bc3123797d6a8a44e0f5b23d102fa646a0f62c51e792fdce -->

# Vérification des intégrations satellites — 27 octobre 2026

**Portée :** vérification statique des instantanés de code et de documentation datés du 27 octobre 2026. **Aucune qualification runtime, CI distante, publication ni autorisation de production n’est déduite de cet audit.**

## Deux contenus indépendants et publication

- `ekole-quebec` est un dépôt de contenu distinct : **202 fichiers `cours/*.json`** dans le snapshot (contenus candidats, **non certifiés par le ministère**).
- `ecole-pastorale` est également indépendant : **32 fichiers `cours/*.json`** et **7 parcours** décrits par son README. Il est en prototype local 0.4 / baseline de contenus 0.3, **non approuvé** pour publication publique ou ecclésiale.
- Les deux packs sont chargés par le moteur neutre `ekole/`; ils ne sont ni fusionnés ni des sous-projets autorisant l'autre corpus.
- `Konstellation-Light` **0.5.2** propose une prévisualisation statique et une démonstration C4 épinglée. La publication des vraies collections n'est pas autorisée par le seul lecteur.
- `Konstellation-Publisher` **0.2.0-alpha.2** ne fait plus de **déploiement distant réel** : le rollback est simulé localement. Il ne prouve ni C1/C2/C3 ni l'autorisation de publication.
- Éléments examinés : `ekole/README.md`, `ekole-quebec/README.md`, `ekole-quebec/cours/`, `ecole-pastorale/README.md`, `ecole-pastorale/pack.json`, `Konstellation-Light/README.md`, `Konstellation-Publisher/README.md`.

**Qualification restante :** exécuter la validation du chargement séparé des deux packs et les suites de tests en environnement local approprié ; obtenir les revues humaines et droits nécessaires avant toute publication.

## Mise à jour et preuve

Cette page décrit un état vérifié **sur fichiers**. Si le code, les contrats ou les captures de tests ont évolué depuis le snapshot, réexécuter les tests et réviser cette page avant publication.
