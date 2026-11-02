<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/blob/a5a2d855584d55d7ee5553207cb2e2b95d9c823d/docs/adr/0007-session-pause-et-dependances.md | commit: a5a2d855584d55d7ee5553207cb2e2b95d9c823d | SHA-256: baf50ed08619419a58cf1e244ce0d3ac686bb71b455dfc4467fd40579173b1ac -->

# ADR 0007 — Pause/reprise et graphe de missions

**Décision : acceptée le 2026-10-12.**

Une session possède un état versionné, un état `suspendue` temporaire et un ancien état de reprise. La progression collective utilise un graphe acyclique de `depends_on` et des transitions séquentielles de phases. Les exceptions pédagogiques sont possibles avec trace enseignante, sans dérogation aux règles de sécurité et de droits.

## Conséquences

- Transactions optimistes obligatoires en production.
- Définitions de missions validées contre références manquantes et cycles.
- Cas de secours pour gardien absent; transfert proposé, non automatique.
