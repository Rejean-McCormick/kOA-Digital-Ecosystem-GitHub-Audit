<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Troubleshooting | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 6189f422491e792aef385a34fd0ff960da3753dc19f51c4c1f79a81f4bf97d44 -->

# Troubleshooting

Use this checklist before changing or reinstalling files. **Export a complete ZIP first whenever possible.**

## Only a few characters are visible

- Choose **All universes** above the character list.
- Clear the search box.
- Confirm you opened **Karacter 7.4**, not an older 4.x or 5.x folder.
- A clean v7.4 project should have built-in **King Klown** and **Blank Universe** filters. An existing browser profile can have additional custom records.

## I cannot find the old “Import Canon” buttons

Those buttons were deliberately removed. Built-in characters are packaged with Karacter. **Import file** is only for standardized external TXT/JSON/ZIP data.

## John Doe has no personality axes

Expected: **Blank Universe** is intentionally minimal. Open **Understand → Studio** and add axes as needed.

## I see an old 1–7 score

You are probably viewing an obsolete HTML file. In v7.4, each axis has **two linked 0–6 sliders** whose total is six. Do not mix JavaScript from different project versions.

## The page is blank or buttons do nothing

- Extract the complete release folder, not just `index.html`.
- Confirm `src/` and `assets/` are beside `index.html`.
- Use a modern browser with JavaScript enabled.
- Open the browser developer console for module or syntax errors.
- Prefer `python -m http.server 8080` from the application folder to avoid `file://` restrictions.

## My data disappeared after moving the application

Browser storage is **origin-specific**. A different folder under `file://`, browser profile, host, or port may expose a different local database. Return to your previous origin if possible, export **Backup ZIP**, then import it at the new origin.

## I see NOT SAVED / NON ENREGISTRÉ

The local save did not complete. Use **Retry save**; check available browser storage, blocked IndexedDB, and whether another tab holds an old database connection. Do not assume unsaved changes are durable. Make a safety export if possible.

## An image is missing

Verify selected **character**, **visual theme**, **image mode**, and **universe filter**. Images are saved in separate slots and the gallery may be filtered. A TXT import does not contain image bytes.

## An imported ZIP is rejected

Only **Karacter backup ZIPs**, not arbitrary ZIP files, can be imported. The app's ZIP reader expects the supported, uncompressed archive structure. If you compressed a saved JSON yourself with a different ZIP method, extract the JSON first and try importing it directly. This GitHub Wiki ZIP is **not** an application backup.

## Importing my backup replaced my current library

Complete JSON/ZIP restore replaces the workspace after confirmation. If you exported a safety backup, restore it to recover the prior state. Single-character TXT imports have a different workflow.

## The prompt did not change after an axis edit

A manually edited prompt may remain fixed until **Regenerate** is clicked. The prompt text is not the same thing as the persisted personality profile.

## A batch image was skipped

Check the strict filename pattern, character slug, theme ID and mode. The batch operation reports unmatched/ambiguous files and may skip them. See [Portrait Gallery](Portrait-Gallery).

## Languages are mixed

The UI is bilingual, but user-supplied narrative texts and source-pack material do not translate automatically. Technical errors can also remain in their original language.

## Reporting a bug

Record the **Karacter version**, operating system, browser, exact URL/origin, steps to reproduce, whether a backup restores correctly, and any console error. Avoid sharing private authored text or entire backups publicly unless you intend to.

**Next:** [Installation](Installation) · [Data Safety and Privacy](Data-Safety-and-Privacy)
