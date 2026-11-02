<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/blob/a5a2d855584d55d7ee5553207cb2e2b95d9c823d/docs/adr/0001-navigateur-sans-usb.md | commit: a5a2d855584d55d7ee5553207cb2e2b95d9c823d | SHA-256: e6b240b887a71d923c26eaf293ada4401f49e179543b22f40ae60ff2210c1980 -->

# ADR-0001 — Utilisation navigateur, sans clé USB

**Statut :** adopté comme référence · **date :** 2026-10-12.

## Contexte
Les Chromebooks scolaires peuvent restreindre les périphériques et exécutables locaux; les clés amovibles augmentent la surface d'attaque et la logistique.

## Décision
Remplacer les 20 clés physiques par des **Kristals virtuels** accessibles sur le site KOMPOSE. Un code de capsule temporaire sert de jonction, non de preuve d'identité suffisante.

## Conséquences
Déploiement navigateur, droits d'accès côté serveur, fonctionnalité possible même sans matériel, nouvelles exigences de sécurité et disponibilité réseau.
