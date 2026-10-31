<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/blob/a5a2d855584d55d7ee5553207cb2e2b95d9c823d/docs/adr/0008-tandem-orgo-operational-authority.md | commit: a5a2d855584d55d7ee5553207cb2e2b95d9c823d | SHA-256: 08b4afa703c00b43116895b5bba3a2492f76db310f01508fd8e0c857089a150b -->

# ADR 0008 — Orgo est l'unique autorité opérationnelle des missions Tandem

**Décision adoptée pour l'intégration P1 (aperçu seulement).**

L'ADR 0006 demeure valable pour l'autonomie de **l'application** KOMPOSE vis-à-vis de KOR.
Elle ne donne **pas** à KOMPOSE un droit d'orchestration concurrent à Orgo.
L'ancienne machine `lifecycle.apply_session_command` reste une **simulation de référence**
compatible avec les tests historiques; ses événements et états ne sont pas des `Case`,
`Task`, `Signal` ou des décisions d'autorisation Orgo.

- **Kontexte** : sources de situations, rôles, étapes, références de fragments.
- **KOMPOSE** : préparation de capsule, contenu, diagnostic, casting sous supervision,
  validations et simulations locales, **sans mutation d'exécution Orgo**.
- **Orgo** : seul propriétaire des tâches réelles, transitions, dispatch, autorisations de
  dévoilement et réconciliation.
- **Orgo_Worlds** : tenant / World / WorldRelease, hors Work.
- **Ekole** : projection enseignant et apprentissage; aucune maîtrise inférée d'un `Task done`.

Le nouveau `verify-ekole-preview` contrôle exclusivement la structure d'un JSON
`ekole.tandem-teacher-preview/1.0`. Ses sorties `runtime_admitted=false`,
`permissions_verified=false` et `world_release_verified=false` sont obligatoires.
Une mention d'autorité `orgo` est une **déclaration de propriété**, pas un jeton signé.
Aucune connexion réseau, identité réelle, revue officielle ou livraison de fragment.

Un futur raccordement Orgo exige authentification, isolation du tenant/World,
version de workflow vérifiée, revue enseignante, tests d'absence/rejeu et contrôle
transactionnel; aucun `apply` automatique ne découle de cet ADR.
