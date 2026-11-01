<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/blob/1a9116cb6d7cfe0eabd4dfbae5e10c4173152d14/docs/EDUCATIONAL_PRIVACY.md | commit: 1a9116cb6d7cfe0eabd4dfbae5e10c4173152d14 | SHA-256: bf25fec0130c64244f64fa66e7a8751d1740d5a9743233df535c9c4b93ed8687 -->

# Educational data security and publication boundary

Spek's HTML and `document.json` are downloadable static artifacts. **A browser-only role filter is never an access boundary.** Do not export school records, teacher solutions, learner identifiers, private diagnoses, classroom-only rights, per-student progress, consent records, photographs or multimedia links requiring authorization. Do not rely on a hidden panel, CSS blur, `robots.txt`, or a school UI to secure static content.

`import-educational` uses a strict whitelist and refuses unknown nested fields, unfamiliar classifications, incomplete exports, evidence from teacher/private locations, unreferenced realization entries, and nonpublic Kompose sessions. It also records the input projection SHA-256. **This is structural validation, not a privacy audit or verification of true export authority.** An operator must review all text, source references and linked media before even a private demo is shared. The importer never grants scientific, curriculum, language or publication approval; the original Kristal state is unchanged.

Use test data before approved exports. GDPR/Quebec education privacy, parental/guardian consent and the institution's retention and revocation processes require their own review. Static deployments cannot provide immediate revocation of downloaded copies. The Spek GitHub Pages workflow continues to reject demonstration builds.
