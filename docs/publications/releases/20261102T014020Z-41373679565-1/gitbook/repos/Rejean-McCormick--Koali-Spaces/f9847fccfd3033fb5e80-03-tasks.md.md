<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/07-global-surfaces/03-tasks.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: cbd5042efa4cb4b38cd5c68676ea5775590c53b2c310591dec0421b0492efe94 -->

# Tasks

**Classe : Cible produit**

Tasks est une work queue agrégée, pas un moteur de tâches.

Item minimal : `task_id`, owner, title, summary, status, priority, due time optionnel, target route, presentation badge.

L’exécution, l’autorisation et le changement de statut restent chez le propriétaire. Koali peut afficher « pending », « attention », « done » selon une projection ; il ne marque pas une tâche terminée localement sans receipt/owner response.
