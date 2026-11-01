<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/10-offline/03-recovery.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 5bbaf62fa8257bac4062ea34f1c86913745aba48ecbd6435240fb92c552faec4 -->

# Recovery de présentation

**Classe : Normatif**

Koali conserve le dernier Space validé et un chemin de rollback. Le recovery de présentation ne restaure pas les données métier.

Après perte d’un runtime child, Koali peut retenter readiness ou proposer un fallback ; il ne recrée pas l’état interne du child.

La reprise réseau ne déclenche pas de synchronisation cross-system implicite.
