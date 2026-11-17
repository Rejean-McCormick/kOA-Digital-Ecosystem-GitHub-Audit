# kOA Digital Ecosystem Audit — correctif ciblé du snapshot 11171758

## À quoi sert cet overlay ?

Cet overlay concerne **uniquement le dépôt du site d'audit**, celui qui contient `docs/index.html` et `docs/assets/atlas.js`. Il **ne va pas** dans `HomePage\HomePage` (initkoa.org / Next.js).

Correctifs :

1. Sur mobile, les onglets de la fiche d'une application ne doivent plus agrandir toute la page. Ils défilent horizontalement **à l'intérieur** du panneau, tandis que les colonnes et boutons restent dans la largeur disponible.
2. Sur la version publique hébergée sur GitHub Pages, ne pas demander cinq ressources locales privées/facultatives qui ne sont pas publiées : `data/local-qualification.json`, `/api/kristal/atlas`, `/api/campaigns/summary`, `/api/review/summary` et `/api/validation/board`.
3. Sur le tableau de bord exécuté localement, ces cinq lectures restent **actives** : le correctif ne supprime aucune fonction d'audit privé.

Fichiers modifiés :

- `docs/assets/atlas.css`
- `docs/assets/atlas.js`

## Installation

1. Faire une copie ou un commit local du dépôt d'audit.
2. Décompresser l'overlay directement **à la racine du dépôt d'audit** (celle qui contient le dossier `docs`).
3. Accepter le remplacement de ces deux fichiers et d'aucun autre.
4. Vérifier localement `docs/index.html` avec l'outil habituel du dépôt, puis publier seulement selon ton processus normal lorsque tu le souhaites. Cette archive n'effectue aucun déploiement.

Pour retrouver le dépôt sur Windows, rechercher un dossier contenant `docs\assets\atlas.js`. Ne pas extraire dans le dépôt Next.js.

## Contrôles effectués ici

- Snapshot de base : `znapshot_kOA-D-E-GitHub-Audit_11171758.zip`.
- Syntaxe JS : `node --check docs/assets/atlas.js` — réussie.
- Analyse CSS : pas d'erreur structurelle.
- Chromium, simulation isolée à largeur 390 px d'un panneau de fiche Orgo : avant, largeur horizontale totale 442 px ; après, 390 px. **Le test est une maquette avec les vrais styles, pas une vérification du site public déployé.**
- Vérification statique des cinq appels privés conditionnés à la version publique.
- Intégrité du ZIP et arborescence vérifiées.

## Limites

- Les 404 du site public doivent être confirmées dans une nouvelle capture après publication ; le correctif couvre les cinq appels identifiés dans `atlas.js`, pas des ressources externes inconnues.
- Les contrôles visuels réels après déploiement ne sont pas faits ici.
- Aucun fichier d'inventaire ou donnée privée n'est inclus dans cet overlay.
