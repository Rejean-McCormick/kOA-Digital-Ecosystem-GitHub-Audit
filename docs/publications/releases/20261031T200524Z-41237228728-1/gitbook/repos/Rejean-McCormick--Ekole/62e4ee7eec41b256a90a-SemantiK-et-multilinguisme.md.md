<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/wiki/SemantiK-et-multilinguisme | commit: fef1626a87dbddb30df47cf9d64b75f6d49b84c3 | SHA-256: fe7d3002327f344753b8990109bddb98bbeb9801e6eb36be46eed5e7c7d8af14 -->

# SemantiK Architect : du sens vers des phrases

## Pourquoi séparer les connaissances de la langue ?

Une relation sémantique peut être stable même lorsque sa formulation varie selon la langue ou l'âge de l'élève. C'est le rôle visé de **SemantiK Architect** : produire des **phrases** à partir d'une structure de sens et de règles linguistiques explicites, plutôt que demander à un modèle de langage distant d'inventer une réponse au moment de l'apprentissage.

```text
Assertion contextualisée et sourcée
       │
       ▼
Contrat de réalisation (langue, registre, variantes permises)
       │
       ▼
SemantiK Architect (réalisation contrôlée d'une phrase)
       │
       ▼
Phrase relue, liée à sa source, présentée par Ekole
```

Cette séparation est prometteuse pour la **cohérence multilingue** : une même assertion peut recevoir plusieurs réalisations linguistiques sans modifier sa vérité. Elle facilite également la vérification des nombres, des négations et du contexte.

## Fiabilité = architecture + tests linguistiques

Il serait excessif d'affirmer que toutes les traductions sont déjà fiables. Dans le dépôt de conception examiné, **`fr-CA` est la seule langue documentée comme originale**, et le port de réalisation SemantiK reste à qualifier. Le multilinguisme fiable est donc **un objectif techniquement bien posé**, conditionné à des grammaires, vocabulaires, tests et validations humaines dans chaque langue.

SemantiK produit des **phrases** et non automatiquement des pages ou paragraphes pédagogiques complets. Ekole organise ces phrases en explications, activités et parcours par une couche éditoriale distincte.

## Le bénéfice hors ligne

Une réalisation grammaticale installée sur place peut, si son implémentation et ses données sont incluses, fonctionner sans API de génération distante. Cela réduit l'exposition des données des enfants à un service externe et peut limiter les coûts d'usage. Cela ne supprime ni les besoins de contrôle de qualité ni le coût du développement initial.
