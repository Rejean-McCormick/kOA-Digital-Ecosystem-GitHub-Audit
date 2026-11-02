<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/01-product/02-space-concept.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 082b7226b1e27b3d1e015083eadfa9f01419c67116c2d295daacd2c7e52b89e8 -->

# Concept de Space

**Classe : Normatif**

Un **Space** est une configuration d’expérience validée qui :

- possède `space_id`, titre et version ;
- sélectionne des module instances ;
- définit un module par défaut ;
- applique ordre et labels publics ;
- référence un thème ;
- définit le comportement offline du shell ;
- configure la top bar globale.

Un Space ne contient pas de business state et ne transporte pas d’extension exécutable arbitraire.

Exemple conceptuel :

```text
Space « École »
├── Accueil
├── Apprendre       -> UCKK / learning surfaces admises
├── Bibliothèque    -> Mediatheque/Kristal surfaces
├── Travail         -> Orgo
├── Communauté      -> Konnaxion
└── Créer           -> SemantiK Architect
```

Les labels ci-dessus sont des labels publics ; les `module_id` restent stables.
