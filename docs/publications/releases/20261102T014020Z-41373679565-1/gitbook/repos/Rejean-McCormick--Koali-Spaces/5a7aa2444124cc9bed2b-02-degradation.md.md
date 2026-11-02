<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/10-offline/02-degradation.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 2f30e60c9e5257b3ab51e2fedfa75a4b59d9f4827d09789accf27501fa28aa2c -->

# Dégradation

**Classe : Normatif**

La dégradation doit être capability-scoped et visible. Une route peut être read-only pendant qu’une autre du même module reste unavailable.

Ne pas utiliser un unique booléen `online` pour déduire toutes les fonctions d’une application propriétaire. L’owner expose ses states pertinents.

Pour la Surface Layer, les axes access/runtime/connectivity/render restent distincts.
