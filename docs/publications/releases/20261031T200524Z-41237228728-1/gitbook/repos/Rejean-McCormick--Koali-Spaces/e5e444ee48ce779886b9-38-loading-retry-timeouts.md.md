<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/38-loading-retry-timeouts.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 43254e84687399b10bd677e87d63c58e2a5bb4a52ccea479b5aa85e5dee66641 -->

# 38. Loading, retry et timeouts

Le host doit distinguer :

- lancement local en cours ;
- page qui charge ;
- health non prête ;
- target absente ;
- embed refusé ;
- erreur réseau locale ;
- erreur de politique.

Retry :

- utilisateur MAY déclencher un retry ;
- retry automatique MAY être borné pour readiness ;
- aucun retry infini ;
- aucun retry ne change d'origine ou de fournisseur.

`LOCK-KS-SURF-119` — **Pas de retry loop non bornée.**

`LOCK-KS-SURF-120` — **Pas de fallback provider pendant un retry.**

---
