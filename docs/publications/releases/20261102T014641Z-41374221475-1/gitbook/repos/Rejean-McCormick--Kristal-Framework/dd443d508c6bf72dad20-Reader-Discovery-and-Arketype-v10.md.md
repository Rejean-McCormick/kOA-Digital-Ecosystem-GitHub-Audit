<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Reader-Discovery-and-Arketype-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: f697cce128c3e74f5a573867577ccc06c48af6355b029547e45060357860726f -->

# Reader Discovery et classification Arketype — v10 draft.3.2

Le Framework intègre un **profil complémentaire non canonique** pour les Kristals créés avec Local Authoring Kit 3.3.0. Il facilite la spécialisation des lecteurs selon le type de Kristal, sa structure physique et sa taille réellement mesurée. Ce profil n'est **pas** une nouvelle identité sémantique ni un format de publication.

## Les trois niveaux

| Dimension | Origine | Exemples | Emploi |
| --- | --- | --- | --- |
| Classification et usage | Arketype 1.4.0 / déclaration du Kristal | `ARK-08`, `PRF-15`, `diagnosis` | Prioriser les index et les parcours |
| Données physiques | Kit 3.3.0 | JSON, JSONL, segments, volumes, SHA-256 | Vérifier ce qui sera réellement lu |
| Stratégie de lecture | Moteur compatible | JSON On-Demand, document stream JSONL, chargeur de graphe | Choisir le parseur, les limites et le cache |

Une fédération UCKK, un graphe de preuves mathématiques, un dossier scolaire et un diagnostic automobile peuvent utiliser la même architecture v9, mais bénéficier de stratégies de lecture différentes. Le profil d'usage **ne détermine pas seul** le codec ni la mémoire nécessaire.

## Contrats

```text
kristal.discovery.json          -> kristal.discovery/1.0
  derived/reader-inventory.json -> kristal.reader-inventory/1.0
  derived/reader-profile.json   -> kristal.reader-profile/1.0
```

`kristal.discovery.json` permet de repérer `state_ref`, la classification Arketype déclarée, l'organisation physique, une taille résumée, les deux fichiers dérivés et une empreinte des entrées. L'inventaire contient les fichiers **locaux enregistrés et mesurés** (taille, SHA-256, types médias) et les descriptions des segments éventuellement distants ou absents. Le profil de lecteur contient des **suggestions non exécutables**, par artefact.

La classe `tiny | small | medium | large | massive` est déterminée à partir des octets locaux suivis par le Kit. La fédération est une **organisation**, pas une taille. Les fichiers non enregistrés et les objets externes n'entrent pas dans le total mesuré. Une valeur `null` pour la taille maximale des enregistrements JSONL veut dire « inconnue », pas « zéro ».

## Lecture sûre et simdjson

1. Si les trois fichiers sont absents : revenir à la lecture générique contrôlée. S'ils sont partiels : ne pas les considérer comme valides.
2. Vérifier leurs schémas et leur cohérence (`state_ref`, empreinte, tailles, parcours de fichiers).
3. Appliquer les règles d'autorisation, vérifier chemins, présence, taille et SHA-256 des objets locaux ; contrôler aussi le format physique réel.
4. En JSON, une lecture On-Demand peut convenir dans la limite de la mémoire/capacité du parseur. En JSONL, **mesurer une borne de taille par document** avant de dimensionner les blocs de streaming. Compression/chiffrement requièrent un adaptateur et un contrôle préalable.
5. Les profils de lecture non reconnus retombent sur la stratégie générique. Les conseils Arketype ne donnent aucun droit de lecture ou d'exécution.

## Exemple Framework

```bash
cd reference/js
node bin/kristal-ref.mjs inspect-reader-discovery ../../profiles/reader-discovery/examples/demo-kristal --verify-files
```

Le Framework vérifie les documents et peut produire un `reader_plan` consultable. Il **n'embarque pas simdjson**, ne produit pas une configuration directement exécutable et ne peut pas reconstruire de manière indépendante l'empreinte complète des sources du Kit. Utiliser `python tools/kristal.py check <kristal>` dans le Kit pour vérifier la fraîcheur des métadonnées dérivées.

## Frontières à préserver

```text
Discovery locale != répertoire d'hébergement v10
Profil de lecteur != preuve de conformité sémantique v9
Inventaire de fichiers != autorisation d'accès
Synchronisation GitHub != publication != activation
```

Une projection publique contenant la classification et l'inventaire peut révéler des informations sur le corpus ; la diffusion reste un choix explicite soumis à la politique de confidentialité. Le contrôle des engagements logiques v9 demeure séparé.

**Sources de référence dans le dépôt Framework :** `spec/v10/Reader-Discovery-Profile.md`, `profiles/reader-discovery/README.md`, `docs/29_READER_DISCOVERY_INTEGRATION.md` et les schémas JSON du profil.
