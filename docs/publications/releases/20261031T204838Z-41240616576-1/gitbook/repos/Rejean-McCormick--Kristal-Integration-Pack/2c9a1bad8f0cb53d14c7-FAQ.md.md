<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/FAQ | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 8a0449d79b6b838838dfd69ebaf81f54b06399ebb67c6970b53671d653105980 -->

# Frequently Asked Questions

### Does the Integration Pack install diK?
No. It accepts eligible catalogs and can validate an alpha.7 job receipt. diK runs separately and the Kit adopts catalog revisions separately.

### Can I use the Framework draft.3 checkout with Pack 0.3?
Not for **new pinned v11 validation or handoff**. These commands require exact Framework `11.0.0-draft.4`. The Node read-view consumer can structurally read older derived draft.3 views; this is not equivalent to validating a draft.3 checkout as the active Framework.

### Does a green `v11-handoff` report activate the catalog?
No. Only a distinct, reviewed **Authoring Kit** action can register and then select the new revision.

### Why are KQ and Wikidata Q not interchangeable?
KQ is a Kristal semantic identity. Q is an external Wikidata identifier. `exactMatch` must be separately reviewed and accepted; matching a label does not create identity.

### Can I overwrite a report file using `--out`?
No. The v11 tools deliberately create reports exclusively and refuse an existing path.

### Can I run `tools/install.py --apply` on the supplied Konstellation snapshot?
No. It already contains a differing owner integration. The recorded status recommends `DO_NOT_REINSTALL_EXISTING_INTEGRATION`.

### Does a successful C3 scan make an artifact public?
No. It checks local structure only. C1 evidence, C2 authorization and actual remote release are separate decisions.

### Is a Context Pack the same as a v11 canonical semantic graph?
No. Context Packs and derived projections are reader surfaces, not immutable semantic commitments or an identity registry.

### Was the diK alpha.7 binary tested with this Pack?
The source qualification explicitly says **no**. It tested a synthetic receipt matching the documented contract and a real Kit demo handoff sequence.

See [[Getting-Started]], [[Qualification-and-Testing]], and [[Glossary]].
