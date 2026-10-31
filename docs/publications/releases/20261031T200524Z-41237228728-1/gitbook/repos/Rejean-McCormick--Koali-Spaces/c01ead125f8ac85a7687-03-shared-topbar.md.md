<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/04-shell/03-shared-topbar.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 9d9e53f2cf7716d43f218e19882e57715ad44b3bff9110c2d6d2a8377dff26db -->

# Shared Top Bar

**Classe : Normatif**

La top bar partagée porte un ensemble de présentation borné :

- contexte Space/module actif ;
- surface produit active seulement lorsque plusieurs surfaces admises existent ;
- widgets globaux/module réellement utiles ;
- attention shell compacte uniquement lorsque le shell est dégradé, hors ligne ou indisponible.

En fonctionnement normal `ready`/online, Koali n’affiche pas en permanence de badge technique de readiness, d’icône réseau sain ou de bouton refresh. Les détails transport/runtime appartiennent à Health.

Les widgets `status`/`counter`/`resume` liés à un provider utilisent le contrat `projection_ref` corrigé et ne sont rendus que lorsque le `GlobalProjectionRuntime` fournit leur valeur typée.

En mode immersif d’une application, la top bar Koali peut être masquée selon la Surface Layer, mais une sortie Koali explicite reste disponible.
