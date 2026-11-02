<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/12-operations/02-backup-restore.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 1796187a40aa07a25091bd0ba66189e62595e9e399b9c7a83dbe2c6d8a9fe837 -->

# Backup et restore

**Classe : Normatif**

Koali backup coordination porte seulement sur l’état de présentation nécessaire : Space actif validé, préférences locales sûres et références de rollback selon policy.

Les données métier des owners sont sauvegardées par leurs propres mécanismes.

Un restore Koali ne doit jamais écrire dans les stores d’une application intégrée.
