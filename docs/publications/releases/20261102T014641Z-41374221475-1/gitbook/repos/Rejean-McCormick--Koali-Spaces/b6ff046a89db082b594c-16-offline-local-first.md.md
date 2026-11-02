<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/16-offline-local-first.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 0a55f6da1f51af8e0971a311203baa5b71a1e317d2a12974a53a578d4e82f9c3 -->

# 16. Offline et local-first

Le browser-rendered de Koali ne doit pas être interprété comme Internet-dependent.

Le shell, ses assets, ses icônes, sa localisation et ses manifests runtime nécessaires doivent rester locaux.

Pour une application hostée :

- si son runtime local est disponible, la surface peut être disponible hors Internet ;
- si le module dépend d'une ressource distante optionnelle, l'état dégradé doit être visible ;
- si le module ne possède aucun runtime local admis, Koali ne doit pas simuler une disponibilité ;
- une panne Internet ne doit pas causer un fallback silencieux vers un fournisseur externe.

`LOCK-KS-SURF-059` — **Aucun asset distant requis pour le shell ou le renderer.**

`LOCK-KS-SURF-060` — **Pas de substitution externe silencieuse lorsqu'un runtime local manque.**

`LOCK-KS-SURF-061` — **Un module `unavailable` reste indisponible ; le renderer ne fabrique pas son contenu.**

`LOCK-KS-SURF-062` — **L'état offline/degraded est une information de disponibilité, pas une autorité métier.**

---
