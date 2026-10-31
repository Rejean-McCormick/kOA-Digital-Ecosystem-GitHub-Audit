<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Status-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 325e19eae3a5674f2e1f2f5c410bfa9f29304e733d922e08881d70880e2827d7 -->

# Statut — Kristal Framework v11 draft.4

**Version Framework :** `11.0.0-draft.4` (révision d'outillage/documentation). **Contrats de sémantique stricts :** schémas v11 et vecteurs TCK **inchangés** depuis `11.0.0-draft.3`. Le standard reste **draft**; il n'est pas ratifié ni qualifié en production.

## Périmètre vérifié du Framework

- Identités canoniques opaques KQ/KP/KA/KS dans leur namespace, dictionnaires séparés par langue, crosswalk Wikidata Q/P externe `accepted + exactMatch` avec preuves KS.
- Validateurs, schémas, fixtures et TCK v11 ; historique v6–v10 et engagements v9 préservés.
- **Draft.4 :** nouvel outil `tools/v11/interop_preflight.py` en lecture seule pour vérifier un catalogue diK contre le registre/crosswalk du producteur et l'éligibilité à l'import Kit.
- Les tests du Framework sont des preuves **locales** et ne rendent pas automatiquement diK, Kit ou le wiki normatifs.

## Versions applicatives connues au 17 octobre 2026

| Application | Version livrée dans la conversation | Frontière et réserves |
|---|---|---|
| Framework | `11.0.0-draft.4` | Nouveau précontrôle, schémas et TCK v11 toujours à la base draft.3 |
| diK | `1.0.0-alpha.7` | CLI/atelier, imports locaux reprenables, lexiques, conflits, Wikidata, propositions ; non certifié sur dump réel massif |
| Authoring Kit | `4.0.0-draft.3` | Producteur canonique, enregistrement/sélection explicite de catalogues candidats, reprise de certaines transactions |
| Integration Pack | `0.2.0-alpha.1-v11` (référence fournie historiquement) | Lecteur/projection ; qualification croisée finale non établie dans ce snapshot |
| Arketype | `1.5.0` (mention du précédent wiki) | Compagnon optionnel de scaffold ; version non revérifiée pour cette livraison |

## Pas encore établi

Conformité stable de toute la pile, WIkidata intégralement traduit en 300 langues, collision résolue sans revue, import réel multi-Go testé, KQ globalement alloués ou toute migration legacy automatiquement réversible. Les approbations de diK sans signature restent des décisions déclaratives.

**Machine authority :** `VERSION`, `contracts/release.json`, `spec/v11`, `schemas/v11`, `tck/v11`, compatibility locks dans le même dépôt. Ce wiki est explicatif, pas normatif.

**Voir :** [[diK-Authoring-Exchange-v11]] · [[diK-Synchronization-v11]] · [[Conformance-and-Ecosystem-v11]].
