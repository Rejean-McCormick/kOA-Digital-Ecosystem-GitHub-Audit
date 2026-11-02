<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/adr/ADR-0005-bounded-selection-tree.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 84a00331eb2a7964aeb75acc8126832bfa57f8fa86b1eea269ed7ff2485a2bd5 -->

# ADR-0005 — Arbre de sélection borné

Statut : proposé pour v0.2.

Contexte : les filtres plats v0.1 ne représentent pas un pivot conservant la sélection d’origine. Un langage graphe libre ajouterait trop de sémantique et de surface d’exécution au pilote.

Décision : sélection typée, filtres conjonctifs, liens existentiels vers des sous-sélections; profondeur bornée. Les pivots réécrivent cet arbre. L’interface visuelle et les backend adapters partagent le même QuerySpec.

Conséquences : multi-sauts bornés et pivots complets sans variables libres; OR général, cycles, contraintes universelles et qualification arbitraire d’assertions sont différés. Un besoin impossible à exprimer doit être refusé ou conduire à une nouvelle version documentée.

Décisions associées : politique de lecture distincte de Lens; état visuel distinct de requête; lecteur Kristal à qualifier avant projection RDF; SA facultatif.
