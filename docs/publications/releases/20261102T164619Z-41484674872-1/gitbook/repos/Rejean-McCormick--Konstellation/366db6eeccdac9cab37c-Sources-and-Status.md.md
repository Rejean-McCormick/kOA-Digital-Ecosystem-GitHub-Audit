<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Sources-and-Status | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: dcad4aeb1b76f521d5c98a3f2c58b8ac33a945640dd9b7ced3c140c393af027e -->

# Sources, Traceability, and Wiki Status

## Source material consulted

This edition was prepared from archives **provided in the conversation** and their local source code:

| Archive / repository | Role in this wiki |
| --- | --- |
| `Konstellation_selecteur_Kristal_neutre.zip` | Neutral-selector baseline and initial reader behavior |
| `znapshot_Konstellation_10171209.zip` | October 17 source snapshot used for the semantic-display patch |
| `Konstellation_lecteur_v10_presentation_FR_2026-10-17.zip` | **Newest inspected code baseline** for French semantic-display behavior |
| `RAPPORT_Konstellation_presentation_semantique_FR_2026-10-17.md` | Scoped patch changes, test evidence, and untested boundaries |
| `znapshot_Konstellation_10160729.zip` | Earlier baseline and historical context |
| `Kristal-Framework_Code_snapshot(1).zip` | `10.0.0-draft.3.2` contracts and architecture |
| `Kristal_Manager_v10_alpha14_maj.zip` | Local operational checks and candidate contracts |
| `Kristal-Authoring-Kit_Code_snapshot(2).zip` | Discovery, derivation generation, and checks |
| `Arketype_Code_snapshot(1).zip` | Structure and usage-profile library |
| `znapshot_interaction_kernel_10151705(2).zip` | Interaction boundary separation |
| `Daat(2).zip` | Provided reference; **not modified** |
| `A-Kristal-Catho_compatible_v10_lecture_locale.zip` | Local reading case and Catho derivations |

## Priority source documents

**Konstellation:** `docs/37-semantic-display-fr-2026-10-17.md`, `src/lib/semantic-display.mjs`, `tests/semantic-display.test.mjs`, `src/components/Astrolabe.svelte`, `src/components/Explorer.svelte`, `server/integrations/kristal-local-v10.mjs`, `README.md`, `package.json`, `docs/LOCAL_SELECTOR_2026-10-16.md`, `docs/33-kristal-v10-local-reader.md`, `docs/35-parcours-locaux-catho.md`, `docs/36-correctif-registre-relations-catho.md`, `docs/24-api-contracts.md`, `docs/19-security.md`, `docs/IMPLEMENTATION.md`, `docs/VALIDATION-v1.0-RC.md`, `server/integrations/`, `src/components/`, and `contracts/`.

**Framework:** `docs/00_STATUS.md`, `docs/28_V10_ECOSYSTEM_ALIGNMENT.md`, `docs/29_READER_DISCOVERY_INTEGRATION.md`, `profiles/reader-discovery/README.md`.

**Manager:** `docs/VALIDATION_MANAGER_ALPHA14.md`, `docs/V10_ALIGNMENT.md`, `docs/KONSTELLATION_INVENTORY.md`.

**Arketype:** `arketype/docs/ECOSYSTEM_ALIGNMENT.md`, `arketype/docs/12_USAGE_PROFILES_AND_SCOPES.md`.

## Editorial rules

- Distinguish **implemented**, **experimental**, **proposed**, and **qualified**.
- A historical targeted test is not evidence of full qualification.
- When discrepancies arise, **verified contracts and code** take precedence over this summary.
- Do not copy private Kristal names, private paths, or credentials into a public wiki without review.
- Code or standard changes require corresponding documentation and test updates.

**Edition updated: October 17, 2026 (English wiki, semantic-display revision).** This package revises documentation only: no remote GitHub repository, Catho corpus, or Windows browser installation was modified. The October 17 implementation is **French-specific**, scoped, and experimental; no universal internationalization or semantic certification is claimed.
