<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/a75b03c6799e1a8c1e7a5c794aa768210633d078/docs/11-decisions/0004-lecture-par-defaut.md | commit: a75b03c6799e1a8c1e7a5c794aa768210633d078 | SHA-256: c74f79e6b5d98b774ba3e15c816f2dd7aaae49f2f0d92712ca3bd39199e4d679 -->

# ADR 0004 — Lecture seule par défaut et publication contrôlée

**Date** : 2026-10-31 · **Statut** : PRINCIPE ACTIF.

## Contexte

Les opérations historiques ont déjà impliqué des overlays sur les 127 sources, des changements de fingerprint Discovery et un incident GitHub lié à une base SQLite de 189 Mo. Un gestionnaire de lecture ne doit pas transformer une analyse en modification de production.

## Décision

Le parcours standard n'écrit jamais dans `locals`, le canon, GitHub ou le registre de décisions approuvées. Les corrections futures sont des plans séparés utilisant le Kit, avec aperçu, sauvegarde, hash, approbation et tests. La publication Git est une fonction avancée opt-in.

## Conséquences

Les utilisateurs voient des propositions au lieu de corrections silencieuses. Les avertissements sémantiques peuvent persister jusqu'à revue justifiée : c'est voulu. La protection est mesurable par un diff source avant/après.

## Alternative rejetée

« Réparer automatiquement jusqu'à 127 PASS » en modifiant les capacités/empreintes, ou activer GitSink pour satisfaire d'anciens tests.

## Validation

AC-02, AC-14, AC-16 obligatoires; audit de code sur les endroits écrivant à `locals` et tests de subprocess/permission.
