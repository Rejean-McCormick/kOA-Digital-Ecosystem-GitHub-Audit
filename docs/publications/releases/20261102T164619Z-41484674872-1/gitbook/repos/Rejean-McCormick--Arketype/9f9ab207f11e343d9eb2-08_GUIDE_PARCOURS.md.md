<!-- Frozen source: https://github.com/Rejean-McCormick/Arketype/blob/2844b444d2af4c11047486284958bf7afedfbb23/docs/08_GUIDE_PARCOURS.md | commit: 2844b444d2af4c11047486284958bf7afedfbb23 | SHA-256: 7261c4630b8f5e3f615638a3e97efd53f85a07516e1f779bae60199f8d7cde36 -->

# Choosing an archetype

Start with the responsibility and shape of the knowledge, not the eventual application's screen layout.

- **Ordered steps or a conditional workflow?** `procedure-protocole` or `parcours-pedagogique`.
- **Entities, concepts and sourced relations?** `referentiel-semantique`.
- **Independent nodes with parent and peer references?** `federation-topologie`.
- **Sparse checkpoints with external proof references?** `carte-jalons-preuves`.
- **Diagnosis and competing causal hypotheses?** `diagnostic-causal`.
- **Species, object types or natural classification?** `taxonomie-classification`.
- **Changes over time?** `registre-evenementiel`.
- **Comparative observed system condition?** `etat-systemes`.
- **A person-related or operational dossier?** `dossier-suivi`, optionally combined with separate testimony and event references.
- **Distinct layers over a shared subject?** `interpretations-couches` or `modele-multiplexe`.
- **Several independently owned kinds?** `composition-hybride`.

Then inspect the JSON archetype record, read its integrity boundary, and use `python arketype.py create ... --dry-run` to preview a neutral instance.
