<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/blob/0ae6f634e223b7e2fafd68faf6f151730578e490/docs/PERSONNAGES_ALIGNMENT.md | commit: 0ae6f634e223b7e2fafd68faf6f151730578e490 | SHA-256: 3c0b3da0e44e53b9690befa5552f29b0d3d7743660ce0e373ec515032f3f97b3 -->

# Personnages — alignement du 28 octobre 2026

Cette couche est indépendante des images de cours, de leurs prompts, de leur importation et de leur publication. `visuals.py`, l’éditeur d’images et leurs API ne changent pas.

## Répartition

- Le paquet de contenu déclare un chemin facultatif `personnages` dans `pack.json`.
- Le catalogue définit les compagnons, leurs variantes et les médias des rôles. Le moteur ne contient pas leurs noms ni leurs fichiers.
- Kontexte conserve le sens et les identifiants des rôles. La référence `visual_id` est toujours `role-<id>`.
- Kompose reste inchangé : la projection fournit déjà `role_id`. Ekole résout `role-<role_id>` dans son catalogue.
- Le découpeur produit les fichiers prévus, sans publier ni modifier le catalogue.

## Exécution

Le pilote des compagnons conserve ses restrictions : `/eleve/`, paquet `primaire-qc`, serveur local et activation par `?page=parcours&pilote_compagnon=1`. Le choix reste dans `sessionStorage`. Les identifiants de personnages remplacent les identifiants d’univers; les anciens choix `quotidien`, `ferme`, `cosmos` se résolvent respectivement vers Mila, fermier, extraterrestre. Explorateur reste un rôle distinct.

Les images de rôles apparaissent dans les boutons et le panneau du rôle des missions. Une image absente laisse une initiale et le libellé; une erreur de décodage rétablit ce repli. Les variantes scolaires se résolvent avec l’année affichée. Lors d’une réponse, une pose disponible peut remplacer la variante debout; sinon celle-ci est conservée.

Un paquet sans catalogue reste fonctionnel et obtient un catalogue public vide. La couche personnages ne donne aucun droit, ne distribue aucune mission et n’évalue aucun élève.

## API séparée

- `GET /api/personnages/catalogue.json` : catalogue public sans chemins source, avec URL uniquement pour les fichiers prêts et présents.
- `GET /api/personnages/image/<visual_id>` : PNG déclaré, présent et marqué `pret`; sinon 404.

Les chemins doivent rester sous le dossier du catalogue; liens symboliques et traversées sont refusés. Les médias restent sur le même serveur. Les contrôles serveur portent sur taille et en-tête PNG; le navigateur assure le décodage et conserve le repli en cas d’échec. Les images sont relues à la requête; les changements du catalogue nécessitent un redémarrage du lanceur.

## Vérifications

Depuis le dossier `ekole` :

```sh
python -m unittest discover -s tests -p test_launcher.py
python -m unittest discover -s tests -p test_personnages.py
PYTHONPATH=. python -m unittest discover -s tests -p test_tandem_projection.py
node tests/test_personnages_ui.cjs
```

Le test inter-dépôts suppose `Kontexte` et `ekole-quebec` voisins. Le test pastoral existant exige un dépôt `ecole-pastorale`, absent du snapshot fourni; il n’est pas modifié.
