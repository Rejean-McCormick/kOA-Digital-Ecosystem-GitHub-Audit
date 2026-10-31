<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0010-controlled-renderer-registry.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: af74abd4a29e932f2bbb742fa3fdca9d0e96b6fe2fe8cec8905597fb7a506707 -->

# ADR-0010 — Registry contrôlé de renderers

- Statut : accepté

## Décision

Les renderers exécutables appartiennent à Konstellation ou à une extension opérateur explicitement approuvée. Un Kristal ne peut pas fournir du JavaScript, du HTML ou un composant Svelte à exécuter.

## Conséquences

- surface d'attaque réduite ;
- UX cohérente ;
- tests centralisés ;
- accessibilité contrôlable ;
- les extensions passent par des contrats déclaratifs.
