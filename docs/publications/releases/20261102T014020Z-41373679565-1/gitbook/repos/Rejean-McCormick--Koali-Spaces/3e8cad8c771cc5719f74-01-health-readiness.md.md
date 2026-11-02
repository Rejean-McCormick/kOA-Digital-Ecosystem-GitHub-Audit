<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/12-operations/01-health-readiness.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: f5c9603dc5dd3e1d4845f4d1bcf952a18f16fec9553b867832a7e762afdd16ee -->

# Health et readiness

**Classe : Normatif**

Le control health actuel mappe : `ready` -> healthy/ready, `offline|degraded` -> degraded mais ready, autres -> unavailable/non-ready.

À terme, distinguer health du shell, readiness de l’active Space et health des child runtimes.

Un child unhealthy ne rend pas nécessairement Koali unhealthy si le module est optionnel.
