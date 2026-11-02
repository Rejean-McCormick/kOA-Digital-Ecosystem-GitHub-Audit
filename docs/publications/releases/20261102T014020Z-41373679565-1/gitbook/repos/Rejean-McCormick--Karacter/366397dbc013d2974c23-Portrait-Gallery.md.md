<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Portrait-Gallery | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 29d95a709469efb53c0acd4ec4a81fd70455043591f52daf93303e35762b5ea4 -->

# Portrait Gallery

Karacter's Gallery stores imported image assets by **character + visual theme + image mode**. The same character can therefore have a portrait, an expression sheet, and an action illustration in several visual themes.

## Import a single image

1. Select a character in **Create** or open **Gallery**.
2. Choose the intended theme and image mode.
3. Click the image area or **Select image**, then choose a file. Drag-and-drop also works in the Create image area.
4. Review the **square crop preview**. Adjust zoom and horizontal/vertical position.
5. Confirm to save the cropped PNG into the selected image slot.

The single-image importer supports **PNG, JPEG, WEBP and AVIF** with a **30 MB input limit**. The app creates a square output; it does not rename or overwrite your original source file on your disk.

## Batch import

Use **Gallery → Batch import** for up to **30 files** in one operation. Filenames must match known characters and themes unambiguously:

```text
karacter_<character-slug>_<theme-id-slug>_<portrait|expressions|action>.png
```

The app shows the proposed mapping before import. Unknown or ambiguous filenames are skipped and reported. Existing images are not silently overwritten; the batch workflow requires approval. Batch images use **center cropping**, so choose the single-image workflow when framing matters.

## Gallery filters

Filter by **theme** and **image mode**. The sidebar's **universe selection** also limits the gallery to characters in the displayed universes. To view all artwork, choose **All universes** and clear the gallery theme/mode filters.

## Download and remove

Gallery tiles provide image downloads and removal controls. Removing an image deletes that stored slot, not the entire character. Deleting a character can remove its associated artwork, so export a full backup first.

## Storage is not a folder

The `assets/` folder in the source project contains static app assets. Imported artwork is stored in browser **IndexedDB** for the selected local origin. It does not automatically appear as a PNG in your extracted project folder.

An **individual TXT sheet has no image bytes**. Use a full **JSON/ZIP backup** to preserve the gallery. See [Character Sheets and Backups](Character-Sheets-and-Backups).

**Next:** [Visual Themes and Prompts](Visual-Themes-and-Prompts) · [Data Safety and Privacy](Data-Safety-and-Privacy)
