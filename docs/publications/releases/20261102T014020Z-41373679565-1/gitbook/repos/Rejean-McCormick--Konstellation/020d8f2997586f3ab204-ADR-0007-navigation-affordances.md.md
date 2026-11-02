<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0007-navigation-affordances.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 488bacc32e48400741e73a3a77971267e84f7678a07477f0cfb25992dcbc51cf -->

# ADR-0007 — Utiliser des affordances de navigation dérivées

- Statut : accepté

## Contexte

Le terme capability est déjà utilisé dans l'écosystème pour des capacités runtime. Konstellation a besoin de représenter la pertinence d'une structure pour la navigation.

## Décision

Utiliser le terme **affordance de navigation** pour `temporal`, `proof`, `hierarchy`, etc. Une affordance est dérivée, scorée et accompagnée d'evidence.

## Conséquences

- elle n'est pas canonique ;
- elle n'est pas une permission ;
- les aliases `capabilities` peuvent être lus pour compatibilité, mais ne sont plus la terminologie cible ;
- les recettes s'appuient sur des affordances plutôt que sur des catégories métier.
