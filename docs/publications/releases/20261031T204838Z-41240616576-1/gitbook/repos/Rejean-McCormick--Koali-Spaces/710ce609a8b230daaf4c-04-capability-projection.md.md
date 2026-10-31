<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/03-space-model/04-capability-projection.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 2af275659febc22147593e9181a6a32358de940528965363de6f5113e3082b60 -->

# Capability projection

**Classe : Normatif**

Koali reçoit une snapshot non autoritative dont :

- `source` doit identifier kOA ;
- `may_grant_capabilities` doit être `false` ;
- `capabilities` est une liste dédupliquée.

Koali utilise cette liste pour :

- filtrer modules ;
- filtrer sidebar ;
- filtrer widgets ;
- choisir safe routes ;
- présenter `access_denied`/`unavailable`.

Koali ne peut pas ajouter une capability à la snapshot ni interpréter l’absence d’une capability comme une permission alternative.
