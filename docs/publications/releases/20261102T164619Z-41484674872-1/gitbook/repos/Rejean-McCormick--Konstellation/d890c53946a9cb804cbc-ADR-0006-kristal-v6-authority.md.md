<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0006-kristal-v6-authority.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 6411e873614bb372ad141afa8e3aa21ca43b598ed09ee73c03730999be606a8f -->

# ADR-0006 — Kristal v6 reste l'autorité canonique

- Statut : accepté
- Portée : architecture 1.0

## Contexte

Konstellation construit des packs locaux, profils, timelines, graphes et autres dérivés pour rendre un Kristal navigable.

## Décision

`kristal_state` v6 reste l'autorité canonique. Tous les artefacts Konstellation sont des vues ou index dérivés.

## Conséquences

- l'identité d'un pack local ne remplace pas `state_id`/`content_hash` ;
- les pertes d'import sont explicites ;
- les projections peuvent être supprimées/recalculées ;
- les renderers ne créent jamais d'assertions.
