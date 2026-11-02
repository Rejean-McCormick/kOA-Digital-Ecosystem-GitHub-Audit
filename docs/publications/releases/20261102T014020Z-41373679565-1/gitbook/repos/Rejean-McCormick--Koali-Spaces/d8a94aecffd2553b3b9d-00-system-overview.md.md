<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/02-architecture/00-system-overview.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 1701962e6e6ec01bd1819c09df1dd434447290ec3b57d335f12783615148c5fa -->

# Architecture système

**Classe : Normatif**

```text
                    kOA host authorities
       identity / governance / lifecycle / resources
                              |
                    capability + state projections
                              v
+------------------------- Koali Spaces -------------------------+
| control-side                                                     |
| Space + product manifests + surfaces + theme + runtime registrations |
|        -> resolution / filtering / activation                    |
|                                                                  |
| render-side                                                      |
| GlobalShell -> Product/Surface projection -> SurfaceRenderer      |
|             -> page/component/ApplicationHost                      |
+------------------------------+-----------------------------------+
                               |
                     declared app boundary
                               v
         Konnaxion / Orgo / UCKK / Architect / ...
        own UI + own router + own APIs + own business state
```

Koali Spaces est volontairement mince sur l’autorité et riche sur la composition d’expérience.


## Product autonomy

Koali Spaces ne constitue pas un parent runtime obligatoire pour les interfaces propriétaires. Le shell intégré consomme un registre de manifests admis. Chaque produit reste owner de son entry point standalone, de son router, de ses pages, de ses commandes métier et de ses inspectors métier. Le registre intégré peut perdre un produit sans obliger les autres produits à changer leur code source.
