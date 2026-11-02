<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/03-space-model/00-space-definition.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 1378712ec9a40e39c26d9c3325cdceb7963cb86a82557e35396350d885f7a8aa -->

# Space Definition

**Classe : Contrat + Normatif**

Le schéma local est `contracts/koa/space-definition.schema.json`.

Champs structurants :

- `space_id`, `title`, `version` ;
- `default_module_id` ;
- `module_instances[]` ;
- `global_topbar[]` ;
- `appearance` ;
- `offline_policy` ;
- `authority_boundary`.

Un `module_instance` peut adapter `public_label`, `public_icon_ref`, `home_route_override`, `order`, `enabled`, `required`.

`authority_boundary` doit confirmer que le Space est presentation-only, ne peut accorder de capability, ne transporte pas de business state et ne transporte pas d’extension exécutable.
