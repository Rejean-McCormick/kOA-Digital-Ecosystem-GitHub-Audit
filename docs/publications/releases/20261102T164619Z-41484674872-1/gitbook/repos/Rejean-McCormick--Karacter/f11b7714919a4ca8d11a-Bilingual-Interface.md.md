<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Bilingual-Interface | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: f6a2d676aea8f331f77ee140d9f1965a7fd5e8df11bf65cafad68af878fd0e15 -->

# Bilingual Interface — English / Français

Karacter 7.4 provides an interface switch between **English (EN)** and **French (FR)**. Use the button in the top bar.

## What changes

- Primary navigation: Create, Understand, Simulate, Story and Gallery.
- Supported interface labels, help text and action controls.
- Generated simulation explanations where localization is implemented.
- Save-state indicators such as **Saved locally / Enregistré localement**.

## What does not change

- **User-authored text**: names, biographies, custom scenarios and narrative notes remain in the language you wrote them.
- Character IDs, linked polarity scores, stored artwork and canonical events.
- Data-format keys and backup structure.

The locale preference is stored with the workspace, subject to local persistence. The current application makes no translation-service call.

## Example

A character named **King Klown** retains the same profile under EN and FR. Switching the UI is not the same thing as translating all of its narrative prose.

## If parts remain untranslated

Some source-pack descriptions, custom templates, older authored text or technical error messages may still appear in their original language. This does not mean the character was changed. You may edit personal text manually if you want bilingual copies.

For localization architecture and future contributions, see [Technical Reference](Technical-Reference) and [Contributing and Development](Contributing-and-Development).

**Next:** [Getting Started](Getting-Started) · [Troubleshooting](Troubleshooting)
