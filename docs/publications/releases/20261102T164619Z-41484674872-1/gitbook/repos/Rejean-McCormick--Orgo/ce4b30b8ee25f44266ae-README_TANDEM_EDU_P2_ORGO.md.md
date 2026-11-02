<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/blob/381ab137d087794ffcb381532c7d2eabcdd60bb5/README_TANDEM_EDU_P2_ORGO.md | commit: 381ab137d087794ffcb381532c7d2eabcdd60bb5 | SHA-256: 1b52285a307dc0514735b06d4472254d7105bbb990c4879ac8462b9ed47ff497 -->

# ORGO — Tandem Education P2

Extraire cette archive **à la racine** de `orgo` (au même niveau que `apps/api/prisma/schema.prisma`). L'extraction n'applique pas le correctif.

1. `TANDEM_EDU_P2_ORGO` : `PREVIEW_TANDEM_EDU_P2_ORGO.cmd`
2. `INSTALL_TANDEM_EDU_P2_ORGO.cmd`
3. `VERIFY_TANDEM_EDU_P2_ORGO.cmd`

Rollback facultatif: `ROLLBACK_TANDEM_EDU_P2_ORGO.cmd`.

Le P2 implémente seulement une **revue synthétique hors ligne**. Les certificats d'identité, ACL réelles de classe, WorldRelease et admissions Orgo ne sont pas raccordés à cette étape. Ne pas utiliser ces fixtures comme jetons ni comme permissions d'enfant.

Le gestionnaire refuse toute divergence SHA-256 des sources sélectionnées et des fichiers d'ancrage avant écriture, sauvegarde l'état antérieur hors dépôt et vérifie les tests sur une copie temporaire.
