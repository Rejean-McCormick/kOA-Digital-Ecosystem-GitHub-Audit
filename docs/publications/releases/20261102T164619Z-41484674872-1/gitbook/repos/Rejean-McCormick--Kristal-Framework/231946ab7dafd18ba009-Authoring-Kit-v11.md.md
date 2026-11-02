<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Authoring-Kit-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: a8e2455770b19eb79e300507b006eb2eabc2422ed9b594c55d62384465c4f7b0 -->

# Authoring Kit 4.0.0-draft.3 — producteur de Kristal v11

**Profil compatible :** Framework `11.0.0-draft.4` avec contrats sémantiques stricts v11 restés compatibles avec `draft.3`. L'Authoring Kit draft.3 conserve son **pin** contre les sources `11.0.0-draft.3` tant qu'il n'a pas été indépendamment requaliﬁé sur ce nouveau snapshot.

## Rôles

L'Authoring Kit crée les graphes et registres canoniques; diK produit des catalogues/dictionnaires, mesures et propositions. Le Framework vérifie les contrats. Les identifiants Q/P de Wikidata ne deviennent jamais des KQ/KP canoniques. Voir [[diK-Authoring-Exchange-v11]].

## Parcours v11 strict

```bash
python tools/kristal.py check-v11 ./My-Kristal
python tools/kristal.py coverage-v11 ./My-Kristal --locales fr,en,fr-CA
python tools/kristal.py check ./My-Kristal
python tools/kristal.py build-v9 ./My-Kristal
```

Ces commandes viennent du dépôt **Authoring Kit**, pas du Framework ou de diK. L'activation du profil v11 se fait explicitement via `enable-v11`, sur un projet pourvu des artefacts nécessaires. Les anciens Kristals v9/v10 restent valides sous leurs propres contrats.

## Import d'un catalogue diK

```bash
python tools/kristal.py import-dik-catalog ./My-Kristal \
  --catalog /immutable/dik/output/catalog.json \
  --revision wd-review-001 --register \
  --artifact-id urn:project:dik:wd-review-001 \
  --contract-id project.v11.lexical-catalog
python tools/kristal.py select-v11-catalog ./My-Kristal \
  --catalog canon/domain/v11/dictionaries/dik-revisions/wd-review-001/catalog.json
python tools/kristal.py check-v11 ./My-Kristal
```

Un catalogue ne devient pas actif parce qu'il vient de diK. Le Kit ajoute une nouvelle révision avec contrôle des hashes et du namespace, en conservant les corrections curatées existantes. `recover-v11` propose `status`, `finish`, `rollback` sous conditions ; les pannes système physiques ne sont pas encore totalement qualifiées.

## Limites

Pas de traduction automatique de tous les héritages, pas d'authentification cryptographique des réviseurs et pas de démonstration de reprise multi-processus après panne de courant. Le Kit ne résout pas de façon implicite les conflits de lexiques. Voir [[Legacy-Migration-v11]] et [[Conformance-and-Ecosystem-v11]].
