<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/05-integrations/33-konnaxion-capsule-manager.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 9e52d051bba8c287fc96d150e005d5d8555445aaae67cb7a4ddb9c72f361dab2 -->

# 33. Konnaxion Capsule Manager

Le Konnaxion Capsule Manager est une surface opérateur distincte de l'application Konnaxion utilisateur.

Il possède son propre modèle Manager/Agent/Builder et des opérations sensibles de lifecycle, réseau, backup, restore et Security Gate.

Règles Koali :

- l'UI Manager peut être hostée uniquement dans un contexte opérateur autorisé ;
- Koali ne remplace pas ses gates de sécurité ;
- la surface ne transforme jamais ses boutons en appels Docker directs depuis Koali ;
- les opérations privilégiées restent chez le Manager/Agent propriétaire ;
- son onboarding doit déclarer explicitement les restrictions de réseau et de permissions browser.

Cette surface ne doit pas apparaître comme une page normale d'un Space utilisateur général par simple découverte automatique.
