<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/blob/9d4f7e74ed87b5a4c8d284dad891029d834911e4/docs/runbooks/INCIDENT.md | commit: 9d4f7e74ed87b5a4c8d284dad891029d834911e4 | SHA-256: 27e889145e8d5852fe6e67bacb776300bc914dee6b04793a1c66ae8b61aca74f -->

# Runbook — Incident

## Données à collecter

- `requestId` ;
- `buildId` / version ;
- endpoint ;
- recipe/renderer ;
- profil de déploiement ;
- Reader Policy et ensemble de rôles (sans token) ;
- métriques de latence/troncation/cache ;
- code erreur structuré.

Ne pas copier de payloads sensibles dans les logs/tickets par défaut.

## Projection dégradée

Basculer vers le fallback déclaré en conservant QuerySpec, focus et historique. Corriger la projection/renderer, jamais le Kristal canonique.

## Fuite policy suspectée

Retirer l’instance du trafic, reproduire avec le même ensemble de rôles/policy, tester toutes les surfaces secondaires, corriger et ajouter un test négatif avant reprise.

## Saturation

Réduire LOD/budgets ou affiner la sélection avant d’augmenter les caps. Vérifier mémoire, result size, cache hit/miss, temps de planning et projection.
