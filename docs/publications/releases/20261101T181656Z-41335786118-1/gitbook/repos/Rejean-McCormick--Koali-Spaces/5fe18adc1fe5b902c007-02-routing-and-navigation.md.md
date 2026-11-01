<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/03-space-model/02-routing-and-navigation.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 29d783970ccb80f0a37e1ddbdd0bd3a5c3ecf1579f7d41497306aa75cce3cd2d -->

# Routes et navigation

**Classe : Normatif**

Chaque route possède `route_id`, `module_id`, `path`, `page_ref`, label, availability, offline behavior, deep-link policy, aliases, safe fallback et capability policy.

Règles :

- pas de collision de path/alias ;
- pas de path distant ;
- route stable malgré localisation ;
- deep link contrôlé indépendamment du menu ;
- safe fallback explicite ;
- le module propriétaire conserve ses routes internes lorsqu’il est hébergé comme application complète.

Le route composer choisit le match le plus spécifique et ne transforme pas la visibilité en autorisation.


## Product / Surface

Le produit et la surface sont deux axes distincts. Le produit détermine l’owner du domaine et des routes ; la surface détermine quelles routes/navigation/widgets sont présentés pour un contexte d’usage. Changer de surface ne change ni l’owner, ni l’autorisation, ni le contrat de route.

Une surface peut être retirée sans supprimer les routes qu’elle projetait. Inversement, retirer un produit admis retire toutes ses surfaces du registre intégré sans modifier les manifests des autres produits.
