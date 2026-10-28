# Architecture — LOCAL_OBSERVE

`kOA-Digital-Ecosystem` conserve l'autorité sur l'inventaire et les frontières. Le dépôt d'audit local ne possède **aucune autorité de release**, ne modifie aucun repo et n'appelle aucune API dans le mode `local-audit`.

1. **Discover** : explorer des racines explicites pour trouver `.git` (sans suivre les liens symboliques), profondeur bornée.
2. **Bind** : relier à l'inventaire initial de 49 projets par URL origin GitHub quand disponible, sinon par dossier si non ambigu. Les dépôts sans correspondance restent `LOCAL/name`.
3. **Observe** : analyser les fichiers présents (avec limites), manifestes, déclarations CI, configurations CodeQL et Dependabot, indices de secrets et motifs statiques à examiner.
4. **Aggregate** : JSON, CSV, Markdown local uniquement ; distinguer `REVIEW`, `PARTIAL`, `INSPECTED_NO_PATTERN_MATCH` et `NOT_PERFORMED_OFFLINE`.
5. **Historical import** : les résumés spécialisés restent historiques et non autoritaires, et n'effacent jamais les observations nouvelles.

Pas d'exécution du code des dépôts, pas de clonage/fetch, pas de base CVE et pas d'inspection de l'état GitHub distant. Chaque observation garde sa portée et sa limite de confiance.
