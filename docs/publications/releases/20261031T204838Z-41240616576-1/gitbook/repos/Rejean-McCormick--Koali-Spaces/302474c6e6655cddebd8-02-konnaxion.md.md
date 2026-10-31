<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/11-integrations/02-konnaxion.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 3826eec76cfafb7f57684f36127f8182329afc88e6a293c5e8485038e182e71a -->

# Konnaxion

**Classe : Boundary d’intégration**

Konnaxion est une application/système propriétaire avec Next.js UI, backend et routes internes riches.

Koali fournit : launch context, frame/immersive hosting, entry route, availability, accent contextuel et navigation de retour.

Konnaxion conserve : modules internes, routes `/ethikos/*`, `/konnected/*`, `/konsensus/*`, `/kreative/*`, reports, auth, APIs, workflows et business state.

Ne pas créer une copie Koali des pages Konnaxion. Ne pas renommer ses routes pour convenance du shell.


Konnaxion peut conserver son entry point standalone tout en exposant au shell intégré les mêmes routes et une ou plusieurs `surface_profiles`. Koali Spaces ne devient pas le runtime obligatoire de Konnaxion, et Orgo ou un autre produit ne doit pas importer le shell privé de Konnaxion pour obtenir une grammaire UX commune.
