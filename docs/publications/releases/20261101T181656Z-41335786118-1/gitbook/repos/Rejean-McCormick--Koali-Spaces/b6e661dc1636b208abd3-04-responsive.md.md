<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/05-design-system/04-responsive.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 8b6996dcc02b536f0082e7a4b4117a7670b216f11ac73eed0807709b9245b6cc -->

# Responsive behavior

**Classe : Normatif**

Desktop : module selector + topbar, sidebar persistante, surface principale.

Narrow/mobile : module selector reste accessible, sidebar -> drawer, widgets secondaires -> overflow, contenu reflow sans masquer le contexte actif.

Une application hébergée doit obtenir un viewport utile sans que Koali impose une largeur desktop artificielle.
