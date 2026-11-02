<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/wiki/Publishing-the-Wiki | commit: 04b4db906ad2da43e747669effb072f32fabcf18 | SHA-256: 3d1d23072510ade2c9751afb69f6d6e15d172a7ec3238a1aeca4373223fcb9ce -->

# Publishing This GitHub Wiki

This package is a **GitHub Wiki repository export**, not the Karacter application and not a Karacter workspace backup.

## Quick publication guide

1. Open your Karacter GitHub repository and enable its **Wiki** feature if needed.
2. Create an initial wiki page in the GitHub web interface (this initializes the separate wiki repository).
3. Clone the wiki using the URL displayed by GitHub:

   ```sh
   git clone https://github.com/OWNER/REPOSITORY.wiki.git
   ```

4. Copy the Markdown files from this archive's **`Karacter.wiki/`** directory into the **root** of the cloned wiki repository, replacing older versions as appropriate.
5. Check `git status`, inspect the changes, and publish:

   ```sh
   git add .
   git commit -m "Update Karacter wiki for 7.4"
   git push
   ```

6. Open the wiki's **Home** page and verify the **sidebar**, **footer**, and a few links.

`_Sidebar.md` and `_Footer.md` are recognized by GitHub as the persistent navigation/sidebar components. `Home.md` is the primary entry page. See [GitHub's official wiki documentation](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages).

## About GitSink.bat

The supplied wiki archive contains the existing `GitSink.bat` utility from your previous wiki. It was **preserved unchanged** for compatibility. It stages **all** changes in the wiki Git repository, makes a commit if necessary, and executes `git push` whenever you run it. Only run it after inspecting your changes and confirming the remote destination; it is not executed by unzipping this archive.

## Avoid a common mistake

- **Wiki ZIP:** documentation files for your GitHub Wiki.
- **Karacter application ZIP:** HTML/CSS/JS project source.
- **Karacter Backup ZIP:** characters, events, relationships and portraits.

These are three different things. Do **not** import the wiki ZIP into Karacter's **Import file** control.

## Keeping documentation current

Use the main application repository's release notes and `/docs` as the versioned implementation source. Whenever screens, file formats, or built-in universes change, update the relevant wiki page, the version statement on [Home](Home), and navigation if needed. The wiki is separate from normal app code commits and must be published separately.

**Next:** [Home](Home) · [Technical Reference](Technical-Reference)
