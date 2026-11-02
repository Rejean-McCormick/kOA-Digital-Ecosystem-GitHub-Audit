<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/wiki/Architecture-semantique | commit: fef1626a87dbddb30df47cf9d64b75f6d49b84c3 | SHA-256: 44abbdd72907012cb4369154247fc72091e97609305206dbdfd186f09baba072 -->

# Architecture sémantique d'Ekole

## L'idée : séparer les faits, les explications et les applications

Ekole cherche à **séparer ce qui est connu de la manière dont on l'enseigne**. La source de vérité d'un domaine est son Kristal; le cours, l'interface et l'exercice sont des vues qui l'utilisent sous des contrats explicites.

```text
Kristals autonomes (domaines : sociétés, sciences, temps, etc.)
      │ notions, assertions sourcées, relations, périodes
      ├──────────────────────────┐
      ▼                          ▼
Kristals de cours          Navigation Konstellation
      │ objectifs                 │ graphe de découverte
      ▼                           │
Projection pédagogique ───────────┘
      ├── Présentation Élève + ressources visuelles
      ├── Réalisation linguistique SemantiK (intégration progressive)
      ├── Exercices MiniLab avec réponses déterministes
      └── Outils de revue et de publication Enseignant/Core
```

## Un Kristal n'est pas un cours

Un **Kristal** peut porter des classes, des événements, des rôles, des tâches, des ressources, des perspectives, des assertions ou des règles. Par exemple, `societes-autochtones-quebec` peut servir indépendamment du cours `qc-pri-us-009`. Le cours référence une **sélection contextualisée** plutôt que de devenir propriétaire de l'encyclopédie.

Les modèles peuvent être polymorphes : graphe, événement, état, contrat, contenu éducatif. Le projet n'impose donc pas un schéma scolaire unique aux connaissances du monde.

## Relations d'abord, mais relations typées

Une relation **historique** (« échange avec »), une relation **conceptuelle** (« partie de »), une relation **de provenance** (« attesté par ») et une relation **pédagogique** (« nécessite de comprendre ») n'ont pas le même sens. L'absence d'une assertion n'établit pas sa fausseté.

Chaque assertion sensible devrait conserver au minimum : identifiant stable, contexte temporel, auteur ou perspective, provenance, statut de revue et restrictions éventuelles.

## Projection plutôt que duplication

Ekole peut composer des vues statiques d'un contenu déjà préparé. La source canonique reste dans le Kristal. Une projection élève **ne doit pas divulguer** les banques de corrigés, les sources de travail confidentielles ni les ressources non autorisées.

Le chemin vers des [standards RDF/JSON-LD](Web-semantique-et-standards.md) est une **perspective d'interopérabilité**, pas une certification que l'ensemble des Kristals est déjà une base RDF native.
