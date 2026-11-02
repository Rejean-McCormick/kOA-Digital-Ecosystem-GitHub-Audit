<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/19-health-readiness.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 3d0fbd9d7dbe1aecec79c88671bde9977098974bc5073aa3d278cc8a43b6958d -->

# 19. Health et readiness

Une `local_module_surface` peut déclarer une référence de health locale admise.

Koali MAY utiliser la health pour :

- indiquer prêt / non prêt ;
- différer le chargement ;
- afficher un état dégradé ;
- fournir un diagnostic opérateur ;
- permettre un retry borné.

Koali MUST NOT utiliser la health comme preuve d'autorité ou de validité métier.

`LOCK-KS-SURF-070` — **Health ≠ authorization ≠ business validity.**

`LOCK-KS-SURF-071` — **Le health check ne doit pas exposer de secret au navigateur.**

---
