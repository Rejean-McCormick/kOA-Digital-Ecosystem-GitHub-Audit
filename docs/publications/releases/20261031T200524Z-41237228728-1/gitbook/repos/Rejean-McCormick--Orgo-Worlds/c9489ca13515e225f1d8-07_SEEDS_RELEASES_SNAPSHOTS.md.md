<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/07_SEEDS_RELEASES_SNAPSHOTS.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: f1fae3c7853d02682d2e1a983d79cf9c3983028de8b48542129df209f7906191 -->

# Seeds and releases

Phases 1–5 livrent : World, release, promotion et backfill `main`. Une release contient actuellement `label`, `config`, `content_hash`, parent et statut. Sa configuration n'est jamais modifiée par une route d'update.

Les snapshots complets et seed packs de contenu sont volontairement hors Phases 1–5; ils appartiennent à la phase suivante. Cette limite n'affecte pas l'isolation runtime ni le pinning des workers.
