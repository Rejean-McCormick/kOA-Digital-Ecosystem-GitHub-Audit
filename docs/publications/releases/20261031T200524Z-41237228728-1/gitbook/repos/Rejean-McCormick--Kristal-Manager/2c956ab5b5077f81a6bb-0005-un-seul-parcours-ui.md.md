<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/0ebeb9141430cb35396e448f422522ea6aecdf8b/docs/11-decisions/0005-un-seul-parcours-ui.md | commit: 0ebeb9141430cb35396e448f422522ea6aecdf8b | SHA-256: 21f8720d76f626fdffdb6bc25201bac587f10751efad69589981f13c8d1932f3 -->

# ADR 0005 — Simplifier l'interface par parcours, pas par onglets

**Date** : 2026-10-31 · **Statut** : PARTIELLEMENT LIVRÉ / CIBLE.

## Contexte

Inventaire, analyse globale, diagnostics, Arketype, catalogue, fichiers, registres et imports ont leurs propres panneaux. Le problème n'est pas leur nombre technique, mais des points d'entrée concurrents et l'absence de vue de statut commune.

## Décision

Organiser autour de la liste des Kristals, de leur fiche et d'un centre d'analyse/diagnostic relié à la sélection. Chaque opération a un déclencheur principal et un résultat visible. Les outils avancés restent disponibles, mais cessent de concurrencer le parcours usuel.

## Conséquences

L'opérateur sait où commencer et où retrouver les rapports. Des anciens menus pourront subsister temporairement comme raccourcis délégués, à retirer après tests de parité. Aucune capacité legacy supprimée sans inventaire et validation.

## Références

Principes UX-05 (objet), UX-06/07 (actions près des résultats), UX-15 (parcours dominant), UX-16 (écrans concurrents), UX-17 (statut réel), UX-18 (préservation).

## Validation

Tests de parcours de bout en bout, de sélection conservée et de statuts non contradictoires; voir [matrice](../08-qualite/matrice-acceptation.md).
