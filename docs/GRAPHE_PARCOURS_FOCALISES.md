# kOA Graph — Parcours focalisés (FR / EN)

## Principe

Le graphe à parcours focalisés rend **une seule interaction centrale lisible**, avec
ses services, variantes et boucles autour. Il **ne transforme pas le réseau kOA
en une chaîne obligatoire**. Une application peut être autonome et apparaître
dans plusieurs parcours, chaque fois pour un rôle distinct.

À la date du registre initial, trois vues existent :

- **Décision → Travail → Retour** : Konnaxion → IK → Orgo → IK → Konnaxion.
  Développe notamment les opérations Kristal liées à Orgo, les Worlds, le diagnostic et la présentation facultative.
- **Sources → Kristal → Lecture** : acquisition → conservation des sources → Da’at → Kristal → Konstellation.
  Distingue la remise de preuves encore à qualifier, l'autorité sémantique, l'authoring, les diagnostics et les contextes de lecture.
- **Connaissance → Publication** : Kristal → Konstellation → Spek → document composé.
  Met SemantiK Architect, le Runtime Orchestrator, Kompiler et les réalisations indépendantes **dans les branches** ; elles ne sont pas toutes obligatoires pour Spek.

Sélectionner une étape, une branche ou une flèche montre **sa provenance**, son
contrat exact lorsque connu et son niveau de preuve : *qualifié localement*,
*implémenté côté propriétaire*, *documenté*, *candidat* ou *facultatif*.
Ce sont des statuts **de relation**, pas des certificats globaux d'application.

## Comment mettre à jour les parcours

1. Éditer `docs/inventory/graph-focus.v1.json` dans le dépôt **kOA-Digital-Ecosystem**.
2. Pousser ce dépôt, puis installer/pousser le code de lecture dans **kOA-Digital-Ecosystem-GitHub-Audit**.
3. Exécuter **kOA Graph - publication datee FR EN** avec :
   `mode=selected`, `repositories=kOA-Digital-Ecosystem`, `preview_only=false`.
4. Ouvrir `https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/#cartographie`.

**Ne pas choisir `republish` pour une première activation** : ce mode ne
recollecte pas le nouveau fichier source. Les autres dépôts conservent leurs
copies datées lors de la publication ciblée du dépôt architecte.

Le collecteur génère `docs/data/focus-paths.json` et une copie immutable dans
`docs/publications/releases/<release_id>/focus-paths.json`, avec commit de la
source d'autorité. Le site public ne lit aucune preuve privée ni API GitHub en direct.

## English

Focused paths show one central interaction and the contextual systems around
it. They are **not** a mandatory pipeline or a deployment claim. Each edge
has an explicit owner, scope-limited maturity and source-document reference.
Edit the owner registry, push both repositories, then run the manual publication
in **selected** mode for `kOA-Digital-Ecosystem` once. The public graph reads
only the frozen publication, not live repositories.
