<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/diK-Synchronization-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 09eebc1b6cc20e2d830ee5eecaf591de0ee5bd9b0de60c486d2cb61dcbc1b5cd -->

# diK — synchronisation Wikidata et évolution des identifiants

Ce guide décrit les **capacités connues de diK 1.0.0-alpha.7**, application externe au Framework draft.4. Elles sont **non normatives** : `schemas/v11` et le canon Kristal KQ/KP ne changent pas avec un import.

## Sources, vérification, reprise

- `dik sync fetch` : acquisition explicite d'un dump HTTPS officiel et tentative de reprise `Range` / `If-Range`; pas de récupération réseau implicite pendant la résolution de dictionnaires.
- `dik sync import-mirror` : import seulement quand une empreinte SHA-256 amont est fournie et vérifiée indépendamment du manifeste téléchargé.
- `dik sync import-large` : import en flux depuis un dump local JSON/JSONL, gzip/bzip2; checkpoints SQLite et sortie immuable. Le flux compressé doit être **rejoué** depuis le début jusqu'au checkpoint (pas de seek arbitraire).
- `dik sync diff` : différences lexicales entre snapshots conservés, sans effacer les couches locales révisées.
- `dik sync evolution` et `extract-redirects` : rapports de redirections externes et collisions à revoir, sans modifier les KQ/KP; l'adaptateur API ciblé n'est pas un moteur exhaustif d'import des redirects.

## Une absence n'est pas une suppression sémantique

Un QID manquant, une langue non traduite ou une redirection ne signifie pas qu'un concept Kristal doive être supprimé, fusionné ou renuméroté. Les correspondances `accepted + exactMatch` exigent des preuves et une revue. Les homonymes dans 300+ langues ne sont pas une identité.

## Performance et limites

L'index SQLite du chemin `import-large` est **dérivé** et réparable, pas le dépôt canonique. La mémoire utilisée pour les identités déjà approuvées dans le crosswalk reste proportionnelle au nombre de correspondances chargées; le dump complet Wikidata et les 300 langues réellement peuplées ne sont **pas** qualifiés industriellement. Le benchmarking synthétique diK ne vaut pas une preuve de débit sur un miroir massif.

**Guide de promotion :** [[diK-Authoring-Exchange-v11]]. **Versions et limites :** [[Status-v11]].
