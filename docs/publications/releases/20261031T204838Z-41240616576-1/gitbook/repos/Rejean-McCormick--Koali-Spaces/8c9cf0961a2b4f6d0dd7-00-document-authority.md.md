<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/00-governance/00-document-authority.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: d8e9805793724e0bd462f667fd2427d977fc6ca06f7296d79f51dae849226636 -->

# Autorité documentaire

**Classe : Normatif**

Koali Spaces possède sa documentation interne. kOA-Linux possède la boundary hôte : membership de profile, lifecycle hôte, resource envelope, admission d’artifacts, exposition réseau/storage, health integration et capability projections.

La documentation Koali Spaces possède :

- architecture interne du shell ;
- modèle de présentation ;
- runtime interne non privilégié ;
- gestion de l’état de présentation ;
- conventions UX ;
- Surface Layer ;
- providers globaux ;
- règles de développement et de qualification du repository.

Les applications hébergées possèdent leur propre :

- UI interne ;
- router interne ;
- API ;
- modèle métier ;
- validation ;
- permissions ;
- workflow ;
- stockage.

En cas de conflit, une règle de boundary du propriétaire de l’autorité l’emporte sur une préférence de présentation Koali.
