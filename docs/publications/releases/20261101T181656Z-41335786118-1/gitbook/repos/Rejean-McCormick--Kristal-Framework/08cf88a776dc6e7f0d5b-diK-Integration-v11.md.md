<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/diK-Integration-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: fbb0887abcf369d0243b9462d529848e3eaea9dd09abe6823bf82c1d23c6525e -->

# diK — interopérabilité des dictionnaires (v11 draft.4)

**diK `1.0.0-alpha.7` est une application externe au Framework**, pas un nouveau namespace d'identités ni un serveur nécessaire à l'exécution du canon.

## Autorité

**Framework** définit les contrats; **diK** importe, concilie et indexe des couches lexicales, mesure la couverture et propose des migrations; **Authoring Kit `4.0.0-draft.3`** est responsable des graphes et registres canoniques, de l'enregistrement des nouveaux artefacts et de la sélection explicite. Voir [[diK-Authoring-Exchange-v11]].

## Couverture : ne pas inventer les traductions

Pour chaque graphe, inventorier distinctement les KQ et KP, puis compter par langue déclarée : `direct`, `fallback` explicitement autorisé, `missing`, `conflicted`. Les KP ne doivent jamais être comptés dans les KQ. Les anciens mots non résolus ne produisent **pas** une couverture 100 % canonique.

```bash
python tools/v11/dik_coverage.py \
  --graph examples/v11/semantic-graph.example.json \
  --registry examples/v11/identity-registry.example.json \
  --crosswalk examples/v11/external-crosswalk.example.json \
  --catalog examples/v11/dictionaries/catalog.json --locales fr,en,fr-CA
```

## Flux diK → Kit contrôlé

```bash
python tools/v11/interop_preflight.py \
  --catalog /exports/dik/catalog.json \
  --registry /project/canon/domain/v11/registry.json \
  --crosswalk /project/canon/domain/v11/crosswalk.json \
  --kit-import-candidate
```

La fiche de l'outil est [[diK-Authoring-Exchange-v11]]. Le corpus Framework illustratif contient une couche *curated* et ne constitue pas un candidat `--kit-import-candidate` prêt à promouvoir.

## Import et évolution des Wikidata Q/P

Le code diK alpha.7 prend en charge des dumps locaux et des checkpoints SQLite, les différences lexicales et des observations de redirection. Cela ne change aucune identité `KQ`/`KP` ni une correspondance `exactMatch` sans revue. Voir [[diK-Synchronization-v11]].

## Plans legacy

Un plan diK est un **document non exécutable** : pointeur JSON exact, valeur source, rôle sémantique, identifiant cible KQ/KP et décision humaine traçable. L'Authoring Kit ne convertit que les formats qu'il comprend explicitement, dans une **nouvelle** révision du canon. Aucun remplacement global de mots.

**Attention :** le précontrôle local Framework n'est ni une certification de toutes les versions de diK ni une approbation d'édition. Voir [[Conformance-and-Ecosystem-v11]].
