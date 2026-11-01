<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/blob/a5a2d855584d55d7ee5553207cb2e2b95d9c823d/docs/adr/0002-kristal-savoir-distinct-du-gardien.md | commit: a5a2d855584d55d7ee5553207cb2e2b95d9c823d | SHA-256: 745ce3003128fa996886d8969910f514cddcf9063021523380efb61072a75c4f -->

# ADR-0002 — Séparer savoir, garde et lecture

**Statut :** adopté comme référence · **date :** 2026-10-12.

## Décision
`Kristal` est un contenu éditorial versionné; `Custody` attribue temporairement une responsabilité à un élève; `AccessGrant` donne un droit de lecture autonome. Un gardien absent ne rend pas le savoir indisponible.

## Motivation
Éviter l'appropriation par un élève, préserver vérifiabilité et possibilité de médiation humaine.
