<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/wiki/Installer-et-explorer | commit: fef1626a87dbddb30df47cf9d64b75f6d49b84c3 | SHA-256: b635b97962cb1e7ceb095dba545ada078b15ca5c5789fa5a18c359eded21bc7b -->

# Installer et explorer Ekole

## Installation locale Windows

Conserver une seule racine :

```text
C:\mycode\Ekole\
├── kristals\      # connaissances et cours sources
├── docs\wiki\     # ce wiki de documentation
├── site\          # projections Web
├── tools\         # outils de préparation et contrôle
└── LANCER_EKOLE_3_APPS.bat
```

Après installation du dépôt complet et de ses prérequis locaux, double-cliquer sur **`LANCER_EKOLE_3_APPS.bat`**.

Les adresses usuelles sont :

| Service | Adresse |
| --- | --- |
| Ekole Core | `http://127.0.0.1:8765/` |
| Ekole Élève | `http://127.0.0.1:8765/eleve/` |
| Ekole Enseignant | `http://127.0.0.1:8766/` |
| Album d'images (Enseignant) | `http://127.0.0.1:8766/images-album/` |
| Configurer les cadres | `http://127.0.0.1:8766/cadres-images/` |

L'accès à l'espace Enseignant doit passer par la session locale prévue. **Ne pas publier la racine complète `site/` sans sélectionner et vérifier l'export public Élève** : des ressources éditoriales ou corrigés peuvent se trouver en dehors de cette projection.

## Tester un cours

Exemple : `http://127.0.0.1:8765/eleve/?cours=qc-pri-ma-012` (fractions). Si une image d'illustration est présente et synchronisée, elle s'affiche; sinon, la description reste visible. L'album permet de retrouver l'emplacement attendu et de resynchroniser.

## GitHub et le wiki

Le wiki de documentation se trouve dans **`docs/wiki/`**. GitHub affiche ces Markdown dans le dépôt. La fonctionnalité distincte **GitHub Wiki** dispose de son propre dépôt; pour la remplir, il faut y recopier les pages séparément ou cloner le dépôt `*.wiki.git` et y importer `Home.md` et les autres pages.

## Validation et état du projet

Les contrôles d'intégrité locale ne certifient pas la pertinence pédagogique. Les couches Kristal v9/v10, SemantiK et Konstellation doivent être qualifiées selon leurs contrats propres; des dossiers candidats ne sont pas des publications officielles.
