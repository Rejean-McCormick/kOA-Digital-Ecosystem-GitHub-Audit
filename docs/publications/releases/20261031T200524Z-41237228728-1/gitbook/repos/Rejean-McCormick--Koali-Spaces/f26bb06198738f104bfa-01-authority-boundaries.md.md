<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/02-architecture/01-authority-boundaries.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: ade0566733687e63a328adbad539ee94c8daae73d894d3fdbb0ed8ecfff125cb -->

# Frontières d’autorité

**Classe : Normatif**

| Sujet | Koali Spaces | kOA host | Application propriétaire |
|---|---|---|---|
| shell global | propriétaire | déploie/encadre | non |
| Space definition active | présente/consomme | admet/active selon profile | contribue manifest |
| capability authorization | non | projection/autorité selon owner | vérifie ses actions |
| module UI interne | héberge | non | propriétaire |
| business data | non | selon composant owner | propriétaire |
| process lifecycle | demande bornée au besoin | owner/broker | expose readiness |
| routing global | propriétaire | non | contribue entry route |
| routing interne app | non | non | propriétaire |
| presentation preferences | propriétaire | backup coordination | non |

Une surface ne transfère aucune colonne de propriété à Koali.
