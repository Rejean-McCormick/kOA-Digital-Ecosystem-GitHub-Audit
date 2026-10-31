<!-- Frozen source: https://github.com/Rejean-McCormick/Akor/blob/cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb/README_TANDEM_EDU_P2_AKOR.md | commit: cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb | SHA-256: 186cdfb321645c00329ec9c9b77bfd17264dd1fa719bcb6d318d81c5ee7a9b82 -->

# AKOR — Tandem Education P2

Extraire cette archive **à la racine** de `akor` (au même niveau que `src/akor/preflight.py`). L'extraction n'applique pas le correctif.

1. `TANDEM_EDU_P2_AKOR` : `PREVIEW_TANDEM_EDU_P2_AKOR.cmd`
2. `INSTALL_TANDEM_EDU_P2_AKOR.cmd`
3. `VERIFY_TANDEM_EDU_P2_AKOR.cmd`

Rollback facultatif: `ROLLBACK_TANDEM_EDU_P2_AKOR.cmd`.

Le P2 implémente seulement une **revue synthétique hors ligne**. Les certificats d'identité, ACL réelles de classe, WorldRelease et admissions Orgo ne sont pas raccordés à cette étape. Ne pas utiliser ces fixtures comme jetons ni comme permissions d'enfant.

Le gestionnaire refuse toute divergence SHA-256 des sources sélectionnées et des fichiers d'ancrage avant écriture, sauvegarde l'état antérieur hors dépôt et vérifie les tests sur une copie temporaire.
