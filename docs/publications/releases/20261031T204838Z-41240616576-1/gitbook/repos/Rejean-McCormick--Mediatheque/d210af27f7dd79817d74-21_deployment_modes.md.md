<!-- Frozen source: https://github.com/Rejean-McCormick/Mediatheque/blob/21e8d732e6690ab15ced87179eb5b152386fe716/docs/21_deployment_modes.md | commit: 21e8d732e6690ab15ced87179eb5b152386fe716 | SHA-256: 28990483c5269669ce009eb1c2b2ed5d62ac61607c033e4256594b563e8c4729 -->

# Engine et instances

Médiathèque possède un **Engine unique** et un nombre quelconque d’instances.

```text
mediatheque/                  -> Engine, code uniquement
mediatheque-privee/           -> données/config locale privée
mediatheque-uckk/             -> configuration UCKK
mediatheque-universite-math/  -> configuration Université Math
```

Une différence de contenu, de site ou de fonds ne crée pas un nouvel Engine. Chaque instance choisit son backend et ses paramètres dans `mediatheque.instance.toml`.

Pour les instances filesystem/SQLite, le dossier d’instance est passé à l’Engine comme `KOA_CONTENT_ROOT`. Pour les instances Moodle, le manifeste sélectionne l’adapter Moodle partagé de l’Engine.
