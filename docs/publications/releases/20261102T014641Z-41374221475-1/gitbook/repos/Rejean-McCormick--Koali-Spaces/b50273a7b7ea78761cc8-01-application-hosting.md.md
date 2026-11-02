<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/11-integrations/01-application-hosting.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: a7a98a0f3c9574db51b968de12877f809c4fa12d542e8b155cb78d55a559daca -->

# Hébergement d’application

**Classe : Normatif**

Mode normal : application nested dans la main surface avec chrome Koali minimal. Mode immersive : Koali masque module selector/topbar/sidebar/padding pour donner le viewport à l’application, tout en gardant une sortie parent-owned.

Le child garde son shell interne. Koali ne tente pas de mapper chaque page interne dans sa sidebar.

L’ApplicationHost n’est pas un process manager et ne résout pas de runtime secret côté browser.
