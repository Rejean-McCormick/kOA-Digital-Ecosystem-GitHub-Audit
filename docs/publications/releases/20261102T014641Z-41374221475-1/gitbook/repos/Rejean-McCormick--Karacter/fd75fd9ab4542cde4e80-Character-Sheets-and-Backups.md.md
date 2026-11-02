<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Character-Sheets-and-Backups | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 37081a2b82f3440be2dc290e5222ec9df14f0f5ea4aa1e06e2a054ae354969ce -->

# Character Sheets and Backups

Karacter is local-first. Your working library lives in browser storage; **external backups are essential**.

## Pick the right export

| Format | Intended use | Image bytes? | Complete shared timeline? |
|---|---|---|---|
| **Character TXT** | Edit or share one character | No | No |
| **Story TXT** | Read or share a character's accepted events | No | Not a full workspace |
| **Comparison TXT** | Share two reactions under shared conditions | No | No |
| **Prompt TXT** | Reuse image-generation instructions | No | No |
| **Complete JSON** | Restore whole working library | **Yes** | **Yes** |
| **Complete ZIP** | Portable workspace backup with companion TXT files/prompts | **Yes** (in `karacter-backup.json`) | **Yes** |

## Export a complete ZIP backup

1. Wait for **Saved locally** in the top bar.
2. Open **Backup / Export**, then choose the complete ZIP option.
3. Save the downloaded file outside the app folder, ideally with a date in your backup directory.
4. Keep more than one recent copy. Test restore in a separate browser profile or local origin before relying on it.

The full ZIP normally contains `karacter-backup.json`, a manifest, per-character sheet copies and prompts. The JSON carries **image bytes and SHA-256 checksums**, character records, story events, runs, relationships and other workspace data.

## Import a standardized file

Version 7.4 has **one Import file action**, not one import button per bundled universe.

- **Character TXT:** adds or replaces a single character after confirmation. Portrait bytes and shared story history are not contained in the TXT; be careful when replacing an existing ID.
- **Complete JSON/ZIP:** previews an import and then **replaces the current workspace** after confirmation. Take a safety backup first.
- **Earlier Karacter backups:** supported formats can be migrated; review any warnings and the character data afterward.

**Important:** the ZIP you download for this **GitHub Wiki** is *not* a Karacter application backup. Do not feed `Karacter.wiki.zip` into **Import file**.

## TXT editing details

A current character export begins:

```text
KARACTER CHARACTER SHEET v6
```

Plain-text sections such as `[NAME]` and `[MOTIVATION]` are paired with a machine-readable `[JSON_RECORD]` section. Keep the markers and JSON valid if you edit it manually. Each polarity stores an integer left score from **0 through 6**; the right score is derived as `6 - leftScore`.

The TXT sheet's **v6** label is a portable data format version, **not** the Karacter 7.4 application version.

## What happens if an import fails?

The current implementation uses IndexedDB transactions for workspace and artwork writes, aiming to avoid partially restored data. A visible **NOT SAVED** warning means local persistence has failed; do not close the tab assuming changes were committed. Save/export a safety copy and use **Retry save**.

## After restoring

Check universe counts, one edited character, one accepted story event, and at least one image in each relevant theme/mode. Local browser behavior on your device still needs direct validation after closing and reopening the browser.

**Next:** [Data Safety and Privacy](Data-Safety-and-Privacy) · [Troubleshooting](Troubleshooting)
