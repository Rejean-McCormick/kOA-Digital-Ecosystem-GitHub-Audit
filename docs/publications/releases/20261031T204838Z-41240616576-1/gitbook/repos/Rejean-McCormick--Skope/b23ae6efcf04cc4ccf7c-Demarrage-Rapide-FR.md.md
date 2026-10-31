<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Demarrage-Rapide-FR | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: f24b93b2c16022e409c2e21df66f00d9ba8ce9e41db7d9a7f1b001550d0648cd -->

# Démarrage rapide — Skope 0.15.0-alpha.1

## Installation Windows

1. Décompresser le projet dans `C:\mycode\Skope` (avec `Start_Skope.cmd` et `skope/` à la racine).
2. Vérifier la présence de l'index SQLite **déjà finalisé** : `D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite`.
3. Installer Python **3.12** à l'emplacement attendu par `Start_Skope.cmd` et les dépendances adaptées à cet interpréteur.
4. Lancer `Start_Skope.cmd`, garder la console ouverte et accéder à `http://127.0.0.1:8767`.

## Explorer sans risque de collecte automatique

1. Dans **00 · Active Kristal**, choisir un workspace si nécessaire, puis **Activate selected**. Pour explorer Wikidata sans cible, garder **aucun** Kristal actif.
2. Dans **00 · Scope catalog**, sélectionner un profil JSON et sa passe.
3. Cliquer sur **Apply scope settings**, vérifier la racine QID, les propriétés P, le sens de parcours, la profondeur et les limites.
4. Cliquer sur **Calculate scope** puis **Open Scope Explorer** et examiner Graphe, Entités, Convergence et Manifeste.
5. Ne lancer **Start batch QID collection** que si une liste persistante de QID est voulue et que les critères ont été contrôlés.

## Pour conserver les enregistrements JSON complets

Attendre qu'une collecte QID soit `completed`, choisir un profil d'extraction, exécuter **Check sources** et contrôler le manifeste du dump ainsi que les index/lecteurs d'accès aléatoire déjà présents. L'extraction doit être validée et déclenchée explicitement. **Aucun scan complet ni construction d'index ne sera lancé automatiquement.**

## Pour la réconciliation Catho

Activer le Kristal-Catho, sélectionner `catho-recognised-authors`, contrôler la liste des personnes, puis lancer explicitement la campagne si nécessaire. Pour une campagne déjà existante, ouvrir **Identity batches**, analyser les identités non résolues et exporter `human-review-template.csv`. Les suggestions sont *non confirmées*. Chaque confirmation exige la vérification humaine d'une source documentaire, son URL, une justification, un contrôle préalable et une attestation.

## Nouveau : traiter un portefeuille v11

Glisser ton ZIP v11 sur `Run_Portfolio_Prepare.cmd` (ou utiliser `python -m skope portfolio prepare`). Le programme crée un inventaire et un CSV de candidats **non approuvés**, sans modifier les Kristals. L’acquisition des fiches Wikidata et la préparation de propositions se font ensuite par la CLI avec une source vérifiée. Voir [Enrichissement des Kristals](Enrichissement-Kristals-FR).

## Vérifier la version

```text
GET http://127.0.0.1:8767/api/config
GET http://127.0.0.1:8767/api/diagnostics/reader
```

Pour le détail, voir [Home](Home), [Troubleshooting](Troubleshooting) et [Safety and Provenance](Safety-and-Provenance).
