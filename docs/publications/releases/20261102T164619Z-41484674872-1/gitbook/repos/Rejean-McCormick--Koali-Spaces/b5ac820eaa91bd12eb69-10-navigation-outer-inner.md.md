<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/02-host-experience/10-navigation-outer-inner.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 072720502e170cd2ec63ca94c9c201a5f669fb347d1480ee6e9205c5f36a6a91 -->

# 10. Navigation : outer navigation vs inner navigation

Deux navigations peuvent coexister en mode framed :

1. **Outer navigation** Koali : sélection de module, navigation de Space, raccourcis de contexte.
2. **Inner navigation** : navigation native de l'application hostée.

Cette duplication visuelle est acceptée par design. Elle est préférable à la fusion artificielle des responsabilités.

`LOCK-KS-SURF-035` — **La sidebar Koali est une contribution de présentation, pas l'autorité des routes internes du module.**

`LOCK-KS-SURF-036` — **Le module selector choisit un contexte de surface ; il n'accorde pas une permission applicative.**

`LOCK-KS-SURF-037` — **Koali ne déduit pas automatiquement toute la navigation interne d'une application par scraping ou introspection DOM.**

`LOCK-KS-SURF-038` — **Une navigation Koali vers une sous-route de module n'est valide que si cette route est déclarée/admise par le contrat de présentation applicable.**

---
