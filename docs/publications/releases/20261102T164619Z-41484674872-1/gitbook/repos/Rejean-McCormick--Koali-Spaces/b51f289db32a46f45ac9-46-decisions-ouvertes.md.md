<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/00-governance/46-decisions-ouvertes.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 5a7f7f6bfaa07e16aaee1f6dd7eda1fcf3bb530b208bd9e34e09a581337ed0d1 -->

# 46. Décisions ouvertes — ne pas inventer

Les points suivants sont volontairement **ouverts** :

1. `OPEN-KS-SURF-001` — catalogue final des transports admis et stratégie par application. L’ADR doit comparer au minimum : iframe vers origine locale enregistrée, gateway path same-origin, et origine locale dédiée par application. La v1.1 verrouille l’abstraction `transport_profile_ref`, pas l’implémentation finale.
3. `OPEN-KS-SURF-003` — protocole parent/child `postMessage` versionné éventuel.
4. `OPEN-KS-SURF-004` — palette exacte des accents de contexte par module.
5. `OPEN-KS-SURF-005` — Browser Fullscreen API éventuel.
6. `OPEN-KS-SURF-006` — politique exacte de persistance du display mode entre sessions.

Un développeur peut expérimenter localement derrière un feature flag. Une expérience ne devient pas canonique par usage, par réussite technique ou par génération IA.

Aucun `OPEN-KS-SURF-*` ne peut être fermé par un patch de code seul.
