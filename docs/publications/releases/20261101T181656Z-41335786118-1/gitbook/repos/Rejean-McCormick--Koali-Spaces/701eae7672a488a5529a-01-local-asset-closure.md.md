<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/10-offline/01-local-asset-closure.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 30f94fe170a4499bffad1db3214fd29d213eff23b3fc78fae3018146f52fcd9e -->

# Fermeture locale des assets

**Classe : Normatif**

Pour une surface déclarée local/offline : scripts, CSS, fonts, icons et localisation essentiels sont installables localement. Aucun CDN public n’est une dépendance obligatoire du rendu de base.

Le build actuel inventorie `.next/static` et `public` dans le runtime packagé.

La présence de web technology ne signifie pas dépendance Internet.
