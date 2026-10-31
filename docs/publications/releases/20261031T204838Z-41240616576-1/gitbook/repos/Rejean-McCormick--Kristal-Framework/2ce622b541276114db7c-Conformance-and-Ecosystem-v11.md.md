<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Conformance-and-Ecosystem-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c52fe805b94911b38d108763f91ee1a380b9530756b0a246824f4976f8b3bc4c -->

# Qualification v11 — Framework, diK et Authoring Kit

**Niveaux de preuves distincts :** validation locale ≠ échange entre dépôts ≠ conformité normative ratifiée ≠ autorisation de publication.

## Critères

- **Framework `11.0.0-draft.4` :** `python tools/validate_all.py` vérifie localement schémas, fixtures, compatibilité historique, scripts de référence et précontrôle diK/Kit. Les schémas v11 et leurs TCK ont conservé les règles de draft.3; la version draft.4 met à jour l'outillage et les explications.
- **diK `1.0.0-alpha.7` :** application distincte, importer/tester le snapshot de sortie avec les schémas v11 exacts; une réussite locale ne prouve pas ses performances sur le miroir complet.
- **Authoring Kit `4.0.0-draft.3` :** sélection explicite d'un nouveau catalogue, création d'une révision de graphe seulement par producteur autorisé; le dépôt Framework ne commande ni état de production ni réseau.

## Refus obligatoires

Le contrôle doit **refuser** une mauvaise empreinte de couche, un namespace discordant, une référence KQ/KP absente du registre, une correspondance Wikidata non acceptée, une preuve KS non enregistrée, une incompatibilité de type Q/P, ainsi que les couches curatées importées par le chemin réservé au Kit. Les références en langue naturelle ne doivent pas occuper les positions canoniques KQ/KP.

## Restant ouvert

- Source Wikidata complète et deltas, multi-namespace, métriques de production, 300 langues peuplées, interopérabilité de tous les snapshots concrets.
- Approbations cryptographiquement authentifiées et reprise après panne du système.
- Contrôle des builds, engagements et publications sur les dépôts cibles et les machines cibles.

**Outils :** [[Conformance-v11]] · [[diK-Authoring-Exchange-v11]] · [[Legacy-Migration-v11]].
