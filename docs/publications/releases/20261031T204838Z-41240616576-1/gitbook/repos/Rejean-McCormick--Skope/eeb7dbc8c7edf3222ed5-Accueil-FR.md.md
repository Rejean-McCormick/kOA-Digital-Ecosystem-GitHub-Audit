<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Accueil-FR | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: fc9f8afe909f77eff74b78a6c575b8585a3270d6bf855dcbae75168324c120ec -->

# Skope — documentation française

**Skope 0.15.0-alpha.1** est une application locale, autonome et *offline-first* pour explorer les données Wikidata déjà indexées, préparer des scopes JSON, collecter des identifiants QID, extraire des enregistrements JSON complets et effectuer une réconciliation d'identités contrôlée par un humain et préparer **l’enrichissement en lot des Kristals v11**, directement par la CLI Skope.

> **Principe fondamental :** explorer un index n'est pas prouver un fait. Une suggestion de correspondance n'est pas une identité confirmée. Un dossier Kristal sélectionné n'est jamais modifié automatiquement.

**Nouveau :** [Enrichissement des Kristals (FR)](Enrichissement-Kristals-FR). Ce parcours natif charge un portefeuille v11, recherche des Q/P dans l’index local, récupère des entités complètes depuis le dump vérifié et produit des **propositions**, pas des écritures canoniques. Il n’existe pas encore de tableau de bord Web pour ces opérations.

## Démarrer

Suivre [Démarrage rapide (français)](Demarrage-Rapide-FR). Le wiki technique complet est disponible en anglais sur [Home](Home).

## Parcours documentés

| Besoin | Documentation |
| --- | --- |
| Installation et dépendances | [Installation](Installation) |
| Utilisation de l'interface | [User Interface](User-Interface) |
| Enrichissement de 104 Kristals v11 | [Enrichissement Kristals (FR)](Enrichissement-Kristals-FR) · [Portfolio Enrichment](Portfolio-Enrichment) |
| Sélection de Kristal | [Kristal Workspaces](Kristal-Workspaces) |
| Profils/scopes JSON | [Scope Recipes](Scope-Recipes) · [Scope Catalog](Scope-Catalog) |
| Exploration des graphes | [Scope Explorer](Scope-Explorer) |
| Collecte massive de QID | [QID Collection](QID-Collection) |
| Extraction du JSON Wikidata complet | [Full-Record Extraction](Full-Record-Extraction) |
| Campagne auteurs Catho | [Catho Authors Campaign](Catho-Authors-Campaign) |
| Réconciliation des identités | [Identity Reconciliation](Identity-Reconciliation) · [Batch Identity Review](Batch-Identity-Review) |
| API et ligne de commande | [API Reference](API-Reference) · [CLI Reference](CLI-Reference) |
| Fiabilité, preuves et limites | [Safety and Provenance](Safety-and-Provenance) · [Known Limitations](Known-Limitations) |

**Attention :** cette archive ne contient ni les volumineuses données Wikidata de production, ni les index d'accès rapide, ni les workspaces Kristal. Les tests sur fixtures ne valident pas automatiquement l'exécution sur le disque `D:` du poste Windows.
