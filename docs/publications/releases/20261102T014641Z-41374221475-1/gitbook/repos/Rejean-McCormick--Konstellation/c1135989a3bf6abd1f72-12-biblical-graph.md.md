<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/12-biblical-graph.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 497ff35bee5fa9b47b8cdcad1ad72bf9722bf14b4697b0af86b19b89e180bbfd -->

# Biblical Graph — exemple de corpus, pas architecture universelle

Ce document existe pour conserver la documentation du corpus biblique intégré aux snapshots historiques de Konstellation.

## Statut

Le Biblical Graph est un **exemple de Kristal/corpus** utilisé pour tester :

- graphes relationnels ;
- alias d'entités ;
- navigation par Lens ;
- Astrolabe configuré ;
- enrichissement Théophile.

Ses concepts ne doivent pas être codés dans le planner générique.

## Règle d'isolation

Les labels, relations et suggestions propres au corpus sont fournis par :

- données ;
- Lens ;
- navigationHints éventuels ;
- configuration d'exemple.

Ils ne doivent pas devenir des branches comme `if (corpus === biblical)` dans le moteur de navigation 1.0.

## Provenance

Toute importation externe doit conserver sa licence, sa source et son chemin de transformation. Les relations éditoriales projetées ne doivent pas être présentées comme influence historique si le corpus ne l'affirme pas explicitement.
