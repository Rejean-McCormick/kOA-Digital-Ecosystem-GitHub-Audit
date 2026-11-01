<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/02-host-experience/21-accessibilite.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 4917675df9cdf30197573eb20f98483d2ca2079d78dae2b62246a9abb7f3c5c0 -->

# 21. Accessibilité

Le host doit être accessible indépendamment de l'application hostée.

Minimum :

- nom du module accessible ;
- commande immersive accessible au clavier ;
- commande Retour à Koali accessible au clavier ;
- focus visible ;
- transition de mode annoncée si nécessaire ;
- `title` descriptif de l'iframe ;
- erreurs et états non transmis uniquement par couleur ;
- skip links Koali préservés en framed ;
- aucun focus trap permanent créé par le host.

`LOCK-KS-SURF-074` — **Le mode immersif doit rester quittable au clavier sans dépendre du contenu de l'iframe.**

`LOCK-KS-SURF-075` — **Koali ne peut pas déclarer l'application hostée conforme WCAG simplement parce que le host l'est.**

---
