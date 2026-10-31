<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0009-actionability-not-authority.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 14658137299f0b1594771738e462162f43e992164b52374e6041008a1cdd3b6b -->

# ADR-0009 — Actionability n'est pas une autorité d'exécution

- Statut : accepté

## Décision

`actionability.mode = automatic` est une information sémantique du Kristal. Elle ne confère aucune permission d'exécuter une opération.

## Conséquence

La recette `action-context` est purement informative. Toute future exécution doit passer par un contrat séparé d'autorisation et d'audit.
