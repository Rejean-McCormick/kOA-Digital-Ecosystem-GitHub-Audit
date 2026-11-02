<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0008-planner-renderer-separation.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 20c48928744f4c299fa135eee6441b9813ce64df689874f62ff95d9f95548753 -->

# ADR-0008 — Séparer planner, projection et renderer

- Statut : accepté

## Décision

Le Navigation Planner choisit les recettes. Le Projection Service construit des DTOs bornés. Le Renderer affiche ces DTOs.

## Raisons

- testabilité ;
- sécurité ;
- déterminisme ;
- réutilisation cross-domain ;
- possibilité de fallback ;
- possibilité d'optimiser projection et UI indépendamment.

## Interdiction

Un renderer ne doit pas exécuter sa propre logique de policy ou inventer une query cachée hors contrat.
