<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Contributing-and-Development | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 0654b5cdd8d2c734f193b45035904cdadcb3a436d7a137208ebdb0d0dedc852d -->

# Contributing and Development

The Karacter codebase is designed for local editing without a build system. Before developing a feature, read the versioned **main repository** specifications under `docs/`.

## Local workflow

1. Clone/download the **main Karacter application repository**.
2. Open it in a code editor and serve it with `python -m http.server 8080`.
3. Make a **full ZIP backup of test data** before schema-changing experiments.
4. Implement behavior and update its tests.
5. Run `npm test` (Node.js 20+).
6. Check the English/French interface, one existing character, John Doe, one story event and a restored image.
7. Update this wiki only after the implementation has changed.

## Project design rules

- Preserve **0–6 linked polarity totals** and avoid moral ranking.
- Simulations must remain **hypotheses** until a user canonizes one.
- No automatic rewriting of a character's polarity axes from narrative events.
- Keep source-backed King Klown information distinct from **creative interpretation**.
- Never delete or overwrite user edits simply because a bundled pack changes.
- Preserve stable IDs, character relationships, and existing image bytes during migration.
- Test the schema, backup, and restoration path for every new persisted field.
- Make important new UI labels available in **EN and FR**.

## Where to document changes

| Change | Update |
|---|---|
| Product feature or workflow | Main `docs/product/`, relevant wiki page |
| Character/polarity model | Main `docs/domain/`, `docs/schemas/`, tests |
| Storage or migration | Main `docs/technical/`, migration tests, backup wiki |
| Source-canon interpretation | Main `docs/universe/` and evidence metadata |
| UI/translation | `src/i18n.js`, UX docs, bilingual wiki |
| Public release | `docs/RELEASE_*`, `README.md`, wiki version statements |

## Manual checks still matter

Node and isolated UI tests are useful, but they do not replace **real browser close/reopen persistence tests**, accessible navigation checks or testing on physical mobile devices.

For the actual module map, see [Technical Reference](Technical-Reference).
