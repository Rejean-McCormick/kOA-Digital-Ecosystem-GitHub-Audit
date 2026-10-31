<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/04-shell/00-global-shell.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: fbf88ecaaee7d148a9cd73ebed06c41c63f18acb52ffad06d240c08dfe28ee69 -->

# Global Shell

**Classe : Normatif**

Le shell desktop est composé d’une bande supérieure et d’un corps :

```text
+---------------------+---------------------------------------------+
| Product selector    | Context header                              |
+---------------------+---------------------------------------------+
| Surface navigation  | Main workspace                           |
|                     |                                             |
+---------------------+---------------------------------------------+
```

Composants actuels : `GlobalShell`, `ModuleSelector` (product selector compatible), `ProductSurfaceSelector`, `SharedTopBar`, `ActiveModuleSidebar`, `MainPageSurface`, `SkipLinks`.

En mode intégré, le shell est rendu une fois. Le content owner n’instancie pas une deuxième navigation Koali autour de sa contribution. En mode standalone, le produit peut rendre les mêmes primitives Koali dans son propre entry point sans dépendre de Koali Spaces.
