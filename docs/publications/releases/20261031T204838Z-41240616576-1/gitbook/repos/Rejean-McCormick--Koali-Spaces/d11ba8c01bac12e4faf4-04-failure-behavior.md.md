<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/09-security/04-failure-behavior.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 585849f79eb6ac70b3a1522714e08a87d46538263aabc9c4636176d650dd6172 -->

# Fail-closed et erreurs visibles

**Classe : Normatif**

- manifest invalide -> contribution rejetée ;
- module optionnel manquant -> omis/unavailable selon policy ;
- module required manquant -> activation bloquée ;
- capability absente -> route/widget non admis ou access denied ;
- runtime child indisponible -> surface unavailable/degraded, jamais substitution silencieuse ;
- control state absent en production -> 503/unavailable ;
- assets offline incomplets -> ne pas revendiquer la disponibilité offline.
