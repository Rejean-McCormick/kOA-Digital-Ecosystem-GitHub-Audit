<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/04-runtime-and-security/20-parent-child-communication.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: c4f441182d7073cbd6ee7313fb14e28de8bf092b2e2df071dcab8f1bb05286ab -->

# 20. Communication parent ↔ application

Par défaut, aucune communication métier parent/child n'est implicite.

Un futur bridge `postMessage` peut être utile pour :

- signaler un changement de taille ;
- demander une navigation explicitement admise ;
- signaler un changement de titre ;
- demander une sortie immersive ;
- signaler un besoin d'ouverture externe.

Il ne doit pas être utilisé pour contourner les APIs propriétaires.

`LOCK-KS-SURF-072` — **Aucun protocole `postMessage` générique ne donne accès aux données ou commandes métier.**

`LOCK-KS-SURF-073` — **Tout message doit avoir un type allowlisté, une version, une origine validée et une validation de payload.**

`OPEN-KS-SURF-003` — **Le protocole parent/child n'est pas requis pour le MVP du renderer.** Ne pas le créer sans besoin concret.

---
