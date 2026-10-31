<!-- Frozen source: https://github.com/Rejean-McCormick/Mediatheque/blob/21e8d732e6690ab15ced87179eb5b152386fe716/docs/22_uckk_boundary.md | commit: 21e8d732e6690ab15ced87179eb5b152386fe716 | SHA-256: bd0723a8e173751c67f364ce6194dbc791f59ea8cf3c5024cbf1cd3f68b85301 -->

# Frontière des instances UCKK / Math

UCKK et Université Math sont des **instances** du même concept Médiathèque, pas deux Engines.

- Engine partagé : `../mediatheque/`.
- Adapter Moodle partagé : `../mediatheque/integrations/moodle/mod_uckkarchive/`.
- Instance UCKK : `../mediatheque-uckk/`, `sitekey = "uckk"`.
- Instance Université Math : `../mediatheque-universite-math/`, `sitekey = "math"`.
- Les données restent dans leur backend Moodle respectif; elles ne sont pas copiées dans l’Engine.
- L’instance privée locale reste filesystem + SQLite et ne partage pas sa DB avec Moodle.
- Les échanges restent explicites et auditables.
