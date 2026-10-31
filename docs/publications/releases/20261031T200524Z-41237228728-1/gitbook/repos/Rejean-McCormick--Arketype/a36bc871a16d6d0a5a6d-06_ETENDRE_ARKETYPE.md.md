<!-- Frozen source: https://github.com/Rejean-McCormick/Arketype/blob/2844b444d2af4c11047486284958bf7afedfbb23/docs/06_ETENDRE_ARKETYPE.md | commit: 2844b444d2af4c11047486284958bf7afedfbb23 | SHA-256: acee2c7e2bad8bffd78c16c9da8fd632345f75dedfdfd672e40a93f211c5185a -->

# Extending Arketype

1. Decide whether the proposed idea is a **new structural archetype**, a **situated profile**, or simply an **assembly** of existing forms.
2. Give new archetypes stable IDs and slugs; preserve existing identifiers that may be referenced by other users.
3. Write the metadata record in `archetypes/` and add it to `catalogue.json`.
4. Describe the visual pattern and situated reader diagram in `inventaires/`; every new archetype should have a labeled illustration.
5. Initialize a **new independent** stub via the bundled Authoring Kit. Never duplicate another workspace's `state_ref` or its build receipt.
6. Add noncanonical design candidates, provenance considerations, integrity rules and English documentation.
7. Run the full library tests, `validate --check-kit`, and `build-v9` for any newly initialized template.
8. Regenerate the HTML and optional PDF and refresh `INVENTAIRE.json`.

The repository intentionally keeps technical slugs and schema keys stable. Translate reader-facing prose without renaming machine identifiers in place.
