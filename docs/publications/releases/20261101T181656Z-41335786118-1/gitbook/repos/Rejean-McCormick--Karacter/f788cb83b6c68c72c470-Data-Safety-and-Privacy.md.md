<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Data-Safety-and-Privacy | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 13b38f72835e688981005461296337cf59dc698f83c2f4e7931df9d4bc2f08d7 -->

# Data Safety and Privacy

Karacter is designed as an **offline-first, single-user local application**. Its ordinary editing and simulation workflows do not require an account or cloud database.

## Where information lives

| Data | Normal location |
|---|---|
| Character profiles and universes | Browser IndexedDB workspace store |
| Relationships, simulations, canonical events | Same workspace store |
| Portraits and expression/action images | IndexedDB binary asset store |
| Language and active-character preferences | Workspace preferences |
| Downloaded TXT, JSON and ZIP | Folder chosen by your browser/device |

The browser origin matters: `file://...`, `http://localhost:8080`, and `http://127.0.0.1:8080` can use **different storage contexts**. Browser privacy settings or clearing site data can remove your records.

## Prevent data loss

1. Always keep a **complete backup ZIP** outside browser storage.
2. Wait for **Saved locally** after important edits.
3. If **NOT SAVED** appears, stop destructive work and use **Retry save**.
4. Before changing versions, browser profiles or ports, export a backup.
5. Verify a restoration with a real image and a story event before relying on it.

## Import, deletion and rollback

Deletion of a character and its linked images is designed to occur within one IndexedDB transaction. Import restoration is likewise designed to replace workspace data and binary assets transactionally. This protects against certain partial failures but does not protect against an erased browser profile, defective disk, malware, or loss of an unexported local collection.

A full JSON/ZIP restore **replaces** your current working workspace. Back up before confirming.

## Scope and limitations

- No built-in account synchronization, shared cloud project or multi-device merge.
- No guaranteed conflict resolution between two tabs editing the same local collection.
- No embedded image generator; a copied prompt may be submitted to an external service **only by your own action**.
- A full data-safety or accessibility certification on every real browser is **not claimed** by the current release.

For the software and supplied fictional character records, consult [Technical Reference](Technical-Reference) and [King Klown Universe](King-Klown-Universe).

**Next:** [Character Sheets and Backups](Character-Sheets-and-Backups) · [Troubleshooting](Troubleshooting)
