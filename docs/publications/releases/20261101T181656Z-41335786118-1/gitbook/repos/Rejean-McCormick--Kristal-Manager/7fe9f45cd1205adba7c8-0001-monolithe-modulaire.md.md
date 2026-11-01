<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/0ebeb9141430cb35396e448f422522ea6aecdf8b/docs/11-decisions/0001-monolithe-modulaire.md | commit: 0ebeb9141430cb35396e448f422522ea6aecdf8b | SHA-256: f51c0092942780eee4354e657a1b3dfcfcd82b8bf1a53252b6baa415b6654abb -->

# ADR 0001 — Monolithe modulaire local

**Date** : 2026-10-31 · **Statut** : PROPOSÉ pour le futur dépôt.

## Contexte

Manager est une application Python locale Tk avec de nombreux modules fonctionnels et 127 sources en répertoires voisins. La fragmentation provient d'entrées UI et de stockages concurrents, non de la nécessité de scalabilité réseau.

## Décision

Une application Manager, des ports/domaines internes avec imports dirigés, et un seul contrat public par moteur. Les opérations lourdes KristalDiag sont des subprocess bornés; pas de broker, microservices ou serveur central obligatoire. Les modules peuvent être testés sans UI.

## Conséquences

Gains : installation Windows simple, moins de duplication et d'outillage réseau, refactoring graduel, tests rapides. Coûts : discipline stricte des imports et responsabilité de migrer `gui.py` progressivement; éviter un « monolithe spaghetti » renommé.

## Alternative rejetée

Fusionner tous les contrôles et modules dans un `gui.py` unique ou, inversement, déployer un backend/distributed event bus pour 127 locaux.

## Validation

Un test de frontière interdit `tkinter` et `sqlite3` dans `domain/`, et limite les imports inter-modules aux API publiques. Toutes les commandes CLI/GUI utilisent les mêmes use cases.
