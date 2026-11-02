<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/09-security/01-authorization-boundary.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 3a124074e0a29c21c9071989d6c5ad298dfe89f4a072dd588fc17ddf620bb9e8 -->

# Authorization boundary

**Classe : Normatif**

Koali peut : cacher, désactiver, marquer unavailable, choisir un safe fallback.

Koali ne peut pas : accorder un rôle, valider une mutation métier, créer un trust root, contourner une policy owner.

Toute commande propriétaire doit être revalidée par l’owner même si Koali avait affiché le contrôle à partir d’une capability snapshot valide.
