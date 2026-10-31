<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/blob/381ab137d087794ffcb381532c7d2eabcdd60bb5/docs/Technical-Reference/TANDEM_EDUCATION_P2_REVIEW_ONLY.md | commit: 381ab137d087794ffcb381532c7d2eabcdd60bb5 | SHA-256: 58091db66d9a7f39946de4937ea8507b999208fe547df21f49fad760a2653284 -->

# Orgo P2 — plan hors ligne des activités Ekole

`node tools/tandem-education/review-plan.mjs <intent.json> <scope-review.json>` consomme une intention Akor synthétique et la revue de portée Orgo_Worlds associée (vérifiée par SHA-256).

Le résultat indique **11 intentions de tâches et 1 intention de Case** dans la fixture Fête de la sorcière, sans appel API, sans workflow publié, sans DB, sans émission de tâche. La sortie `orgo.tandem-synthetic-review-plan/1.0` est un **plan de revue non exécutable**, et non un workflow Orgo prêt à importer.

Aucune identité enfant, approbation enseignante, permission réelle ou release autorisée n'est validée ici. Tous les champs d'admission et de publication restent `false`.

L'étape ultérieure devra raccorder le service d'identité d'Orgo et Orgo_Worlds autoritaire, avec l'ACL réelle tenant/World/release et le consentement/contrôle enseignante, avant d'appeler les API existantes d'Orgo. Aucun endpoint et aucune migration ne sont introduits.
