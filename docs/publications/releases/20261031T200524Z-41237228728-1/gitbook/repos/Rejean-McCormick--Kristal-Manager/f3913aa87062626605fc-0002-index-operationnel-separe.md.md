<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/0ebeb9141430cb35396e448f422522ea6aecdf8b/docs/11-decisions/0002-index-operationnel-separe.md | commit: 0ebeb9141430cb35396e448f422522ea6aecdf8b | SHA-256: 705595220667a12a04c17efad2a71030654df12b5da5a94c421ecca31e744480 -->

# ADR 0002 — Index opérationnel séparé du catalogue de contenu

**Date** : 2026-10-31 · **Statut** : PARTIELLEMENT LIVRÉ, évolution v2 CIBLE.

## Contexte

Les catalogues sémantiques de plusieurs dizaines/centaines de Mo ne sont pas adaptés à l'historique court des verdicts. Les rapports Arketype/Diag vivaient dans des dossiers différents, et rescanner effaçait leur présence en mémoire.

## Décision

Conserver `kristal-contenu-global.sqlite3` comme cache descriptif et `kristal-manager-operations.sqlite3` comme projection centrale des opérations. Référencer les gros rapports par URI/hashes, pas les recopier en entier. Les workspaces restent autorité.

## Conséquences

L'index se sauvegarde et se migre indépendamment du catalogue lourd. Il peut tomber en panne sans détruire le canon. Il faut cependant un protocole de réconciliation entre source, observation et preuve, et une explication de la fraîcheur.

## Alternatives rejetées

Une seule gigantesque table mélangeant assertions et verdicts; un CSV `BILAN` comme base de vérité; des attributs `row['diag_report']` exclusifs à la session.

## Validation

Index v1 conservé, migration vers modèle `runs/observations_v2` sans perte et tests AC-05/06/08/12/18. Les données historiques non vérifiées restent non actuelles.
