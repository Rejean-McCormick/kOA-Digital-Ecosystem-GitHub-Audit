<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/wiki/Hors-ligne-et-sobriete | commit: fef1626a87dbddb30df47cf9d64b75f6d49b84c3 | SHA-256: 8a23c04d21460dcbf5bce43fac91f63039f67fb51dc4fce14548a349c0e5e8e2 -->

# Hors ligne, bande passante et sobriété

## Une architecture conçue pour s'exécuter localement

Le modèle visé d'Ekole est simple : **le contenu structuré est préparé à l'avance**, projeté en pages ou fichiers statiques, puis consulté avec un navigateur. Le fonctionnement normal des vues Élève et des exercices déterministes ne nécessite pas d'appels permanents à une IA distante.

Deux déploiements sont possibles :

- **Un poste local** : Ekole est lancé sur la machine, généralement sur `127.0.0.1:8765` (interface Enseignant séparée sur `8766`).
- **Un serveur d'école sur le réseau local** : plusieurs appareils consultent un **export Élève isolé** via le Wi-Fi de l'école, même sans accès Internet extérieur. Un tel déploiement nécessite une configuration réseau et des protections appropriées.

## Pourquoi cela peut être léger

Une grande partie des connaissances est constituée de **texte, identifiants et relations**. Les pages peuvent être mises en cache et les graphes locaux produits à l'avance. Les calculs des MiniLabs sont principalement des opérations déterministes modestes, sans inférence par grand modèle en continu.

**Attention :** la bande passante effective dépend aussi des **images, polices, vidéos, bibliothèques et appareils**. Une médiathèque riche peut être volumineuse. Le caractère « très faible consommation » est un objectif d'optimisation, pas une mesure publiée.

## Économie et écologie : une promesse à vérifier

L'absence d'API IA au moment de chaque réponse peut limiter les frais récurrents et certaines consommations de ressources externes; le stockage, les appareils, le réseau local, l'hébergement et la création initiale du contenu ont toutefois un coût matériel et énergétique. **Aucun bilan carbone comparatif n'a été établi** pour Ekole.

## Ce qui dépend encore d'Internet

L'usage peut être autonome *si les ressources sont installées et les liens externes facultatifs*. **GitHub**, la recherche de sources nouvelles, les mises à jour, l'hébergement public ou les échanges avec des outils d'IA durant l'édition, eux, peuvent exiger Internet. Hors ligne à l'exécution n'est pas synonyme de hors ligne pour tout le cycle de conception.
