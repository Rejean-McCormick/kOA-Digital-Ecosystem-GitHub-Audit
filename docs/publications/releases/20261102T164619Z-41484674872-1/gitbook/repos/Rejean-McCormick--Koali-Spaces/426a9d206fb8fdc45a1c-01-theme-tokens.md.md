<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/05-design-system/01-theme-tokens.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 5dc26ecad99924f17f138bf9bd61fcd0362bc5700474553c0d08999ed4e7e8d6 -->

# Theme tokens

**Classe : Contrat + Normatif**

Token families : accent, density, radius, spacing, typography, focus, surface family, semantic color policy.

Le bridge actuel mappe ces tokens vers Ant Design `ConfigProvider`. Les tokens Koali sont sémantiques ; la valeur d’un token ne doit pas devenir une condition métier.

Semantic error/warning/success conservent leur signification et ne sont pas remplacés par la couleur de marque.
