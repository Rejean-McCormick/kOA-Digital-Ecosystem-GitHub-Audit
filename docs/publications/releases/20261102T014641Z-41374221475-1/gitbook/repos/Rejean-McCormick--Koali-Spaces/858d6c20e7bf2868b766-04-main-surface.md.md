<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/04-shell/04-main-surface.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: f2233d327524b9fa27ca76491c6bc390586f9e6a98a888b3e3abb272075c08f6 -->

# Main Page Surface

**Classe : Normatif**

`MainPageSurface` est le workspace global de contenu du mode intégré. Il reçoit :

- pages globales Koali ;
- module shell pages ;
- registered component surfaces ;
- local module application surfaces.

La future implémentation doit déléguer le choix au `SurfaceRenderer` plutôt qu’à une collection de placeholders dans les routes dynamiques.


Le mécanisme d’inspector contextuel, lorsqu’un produit le déclare, est une primitive de composition adjacente au workspace. Son contenu reste product-owned ; Koali Spaces ne transforme pas un `inspector_ref` en logique métier générique.
