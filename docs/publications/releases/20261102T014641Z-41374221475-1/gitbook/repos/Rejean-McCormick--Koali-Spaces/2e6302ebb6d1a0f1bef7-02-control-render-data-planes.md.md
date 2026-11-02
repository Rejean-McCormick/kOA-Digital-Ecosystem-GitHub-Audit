<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/02-architecture/02-control-render-data-planes.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: ad959efddbe16c7be5babd88c4d3c3f6863c5f369f3adc1238f3de2754239f06 -->

# Control plane, render plane et data plane

**Classe : Normatif**

## Control side Koali

Résout : Space actif, manifests admis, capabilities projetées, thème, registrations, availability et safe fallbacks.

## Render side browser

Reçoit uniquement des descriptors minimisés nécessaires au rendu. Le browser ne reçoit pas de secrets, credentials de service ou détails de lifecycle privilégié.

## Data plane propriétaire

Les données métier circulent entre l’application et ses APIs selon ses propres contrats. Koali ne devient pas un proxy métier générique simplement parce qu’il héberge l’UI.

Pour une vue agrégée Koali, utiliser des providers/projections déclarés et non autoritatifs.
