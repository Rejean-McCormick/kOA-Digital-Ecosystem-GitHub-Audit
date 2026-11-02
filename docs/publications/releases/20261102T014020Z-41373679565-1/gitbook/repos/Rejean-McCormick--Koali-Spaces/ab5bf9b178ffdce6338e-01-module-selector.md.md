<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/04-shell/01-module-selector.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 3d1900ef53cd0b282fbcf540c5918572f96e9522a1dc7c98e570b703c6610dde -->

# Module Selector

**Classe : Normatif**

Le selector en haut à gauche affiche dynamiquement les produits/modules : enabled dans le Space, admis et compatibles avec les capabilities visibles. La liste n’est pas un catalogue produit hardcodé dans le shell.

Sélectionner un produit/module choisit la route home sûre de sa surface par défaut en fonction du network state et des capabilities.

Le label public vient du Space lorsqu’il existe, sinon du manifest.

Cible : supporter `home_route_override`, icon refs, localisation des labels et reprise de dernière route sûre par module.


La sélection de produit et la sélection de surface sont distinctes. `ProductSurfaceSelector` n’est affiché que lorsqu’un manifest expose plusieurs surfaces admises.
