<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Manager/blob/0ebeb9141430cb35396e448f422522ea6aecdf8b/docs/11-decisions/README.md | commit: 0ebeb9141430cb35396e448f422522ea6aecdf8b | SHA-256: b8fc107205b0eb8015883c61ab32b14bbfb463cb61001ec73a19deed282640ea -->

# Registre des décisions d'architecture (ADR)

Une décision est un compromis explicite, daté et contestable. Elle est conservée avec son contexte et ses conséquences; remplacer une décision implique un nouvel ADR qui la supersède, non l'édition silencieuse de l'ancienne justification.

| ADR | Décision | Statut initial |
|---|---|---|
| [0001](0001-monolithe-modulaire.md) | Monolithe modulaire local | proposée / cible |
| [0002](0002-index-operationnel-separe.md) | SQLite opérationnel distinct du catalogue | en partie livré |
| [0003](0003-examinateur-independant.md) | KristalDiag indépendant derrière port | en partie livré |
| [0004](0004-lecture-par-defaut.md) | Lecture seule et publication séparée | principe actif |
| [0005](0005-un-seul-parcours-ui.md) | Une entrée métier et fonctions avancées | en partie livré |

Les ADR utilisent les éléments fournis au 31-10-2026; leur adoption finale reste à confirmer dans le dépôt et les tests Windows.
