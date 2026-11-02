<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/diK-Authoring-Exchange-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 338ac9e1ea7ba4e2508546872093c6f5b6a3891f0d22d40a68ebfe0b5854e5b0 -->

# diK alpha.7 ↔ Authoring Kit draft.3 — échange contrôlé

**Statut :** complément documentaire de Kristal Framework **11.0.0-draft.4**, basé sur les contrats sémantiques v11 de **draft.3**, non modifiés dans leur contenu. Ce document ne constitue ni une approbation de mapping, ni une certification en production.

## Répartition des responsabilités

| Composant | Autorité | Produit ou vérifie | Ne fait pas |
|---|---|---|---|
| Framework v11 draft.4 | Contrats KQ/KP/KA/KS, schémas, cohérence, règles de provenance | Précontrôle read-only, TCK, rapports | Certifier une équivalence Q↔KQ automatiquement |
| diK 1.0.0-alpha.7 | Applications lexicales, conciliation, imports | Catalogues immuables, couches Wikidata, propositions de revues | Écrire un canon KQ/KP ni adopter seul une migration |
| Authoring Kit 4.0.0-draft.3 | Création canonique, enregistrement, sélection explicite | Graphes v11 et catalogues révisés validés, contrôle Logical Artifact | Convertir implicitement tous les mots en KQ |
| Integration Pack v11 | Consommation/adaptation | Projections lecture seule | Modifier un graphe par traduction |

## Parcours de confiance

1. Faire produire par diK un nouveau `catalog.json` avec couches SHA-256; seule une correspondance Wikidata acceptée et exacte peut fournir une entrée KQ/KP. Le nom du snapshot doit être stable; vérifier les sources indépendamment.
2. Valider le catalogue du **projet cible** avec `tools/v11/interop_preflight.py` du Framework. Lui donner **le registre et le crosswalk approuvés par l'Authoring Kit cible**, pas de substituts créés par diK.
3. Avec `--kit-import-candidate`, le Framework refuse les couches `curated`/`external` importées : le Kit draft.3 ne promeut dans ce circuit que les couches Wikidata, en préservant ses propres corrections curatées.
4. **Dans l'Authoring Kit**, `import-dik-catalog` crée une révision distincte. Enregistrer l'artefact puis appeler explicitement `select-v11-catalog`; cela ne publie aucun Kristal vers un hôte.
5. Contrôler `check-v11`, puis `coverage-v11`. Les chiffres directs, de repli et manquants ne sont pas interchangeables.
6. Toute migration canonique reste une activité séparée du producteur autorisé, avec décisions approuvées, rôles et références exactes. Lire [[Legacy-Migration-v11]].

## Précontrôle Framework

```bash
python tools/v11/interop_preflight.py \
  --catalog /exports/dik/catalog.json \
  --registry /projet-kit/canon/domain/v11/registry.json \
  --crosswalk /projet-kit/canon/domain/v11/crosswalk.json \
  --kit-import-candidate \
  --output /rapports/dik-preflight.json
```

Ce contrôle vérifie la forme, les empreintes, les correspondances acceptées, les KS et les namespaces. Il n'écrit ni catalogue actif, ni graphe, ni état v9. Un résultat `preflight_pass` **ne vaut pas sélection ou approbation humaine**.

**Attention :** l'exemple Framework de base comprend une couche française `curated` et ne passe donc pas `--kit-import-candidate`. Exécuter l'exemple sans ce drapeau pour inspecter un catalogue général.

## Projections réversibles

La projection compacte de diK sépare le `canonical_graph` contenant les véritables KQ/KP et un `lexicon.entries` dédupliqué; l'outil qui restaure doit utiliser les IDs préservés, jamais retrouver un KQ par un mot français, anglais ou autre. Une vue purement épurée qui omet les codes n'est pas une source suffisante pour restaurer le canon.

## Limites et statut

- diK alpha.7 apporte un import local avec checkpoint SQLite, mais n'est pas certifié pour toute Wikidata ni 300 langues réellement peuplées.
- Kit draft.3 a un journal de récupération partielle; les pannes physiques, signatures de réviseurs et activités multi-hôte ne sont pas certifiées.
- Framework draft.4 ajoute l'**outil de précontrôle**, sans modifier les schémas `schemas/v11` de draft.3. Les preuves de conformité locales ne remplacent pas les essais croisés exhaustifs.
- Les événements Wikidata Q/P nouveaux ou redirigés restent des **observations**, non des remplacements automatiques de KQ/KP.

**Voir aussi :** [[diK-Integration-v11]] · [[Authoring-Kit-v11]] · [[Dictionary-Management-v11]] · [[Conformance-v11]] · [[Status-v11]].
