<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Update-Notes-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 30502e042c8eb84f3b19160431d46f26a360672103a70498406d5620b9b6c9c4 -->

# Mise à jour du wiki — Framework v11 draft.4

**17 octobre 2026.** Révision synchronisée du Framework et de ce wiki à partir des archives fournies par l'utilisateur.

- Nouveau précontrôle read-only `tools/v11/interop_preflight.py` et documentation d'échange pour **diK `1.0.0-alpha.7`** et **Authoring Kit `4.0.0-draft.3`**.
- Navigation et pages v11 mises à jour, avec distinctions explicites entre Framework (contrats), Kit (production canonique) et diK (travail lexical).
- Contrats sémantiques v11, schémas `schemas/v11/*.schema.json`, tests TCK et engagements historiques v6–v10 **inchangés**.
- Nouveaux guides : [[diK-Authoring-Exchange-v11]], [[diK-Synchronization-v11]], [[Conformance-and-Ecosystem-v11]].
- Anciennes pages v6–v10 conservées comme références historiques. Le wiki demeure informatif : aucune publication GitHub, aucune activation de Kristal ou décision de crosswalk n'est effectuée.

**Ce qui n'est pas certifié :** import Wikidata complet sur des dizaines de Go, 300 langues réellement peuplées, revue cryptographiquement authentifiée, synchronisation/deltas exhaustive, reprise après panne physique, qualification de chaque instance diK+Kit en production.


## 28 October 2026 — UNESCO classification companion (no Framework version bump)

The Manager/Icon Generator subject-domain classification is consolidated on the pinned UNESCO Thesaurus reference spine (7 domains, 88 microthesauri). ISCED-F remains historical only; it is not an icon classification, a current filter or a source for automatic crosswalks. Arketype remains independent for structure/usage. A new optional Framework companion profile and read-only inspection tool are documented at [[UNESCO-Thesaurus-Classification-v11]]. Historical normative contracts and v11 TCK fixtures remain unchanged. Windows folder icons stay opt-in and disabled by default in Manager.
