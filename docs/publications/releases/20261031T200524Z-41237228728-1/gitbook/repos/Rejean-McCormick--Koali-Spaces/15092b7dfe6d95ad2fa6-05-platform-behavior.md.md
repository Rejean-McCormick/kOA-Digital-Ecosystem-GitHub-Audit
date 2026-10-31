<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/08-runtime/05-platform-behavior.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 20e4eeeac8203c2c6538e4825be90004e79708b0606059a817c8a09b77041d1a -->

# Comportement Linux / Windows

**Classe : Normatif + Référence**

Linux est la cible complète d’intégration : presentation server + control Unix socket.

Windows est une cible de développement/smoke de la présentation. Le control Unix socket y est actuellement désactivé.

Un test Windows réussi ne constitue pas une preuve que la boundary kOA Linux fonctionne. Inversement, le code UI ne doit pas dépendre de chemins Linux pour pouvoir être qualifié localement.
