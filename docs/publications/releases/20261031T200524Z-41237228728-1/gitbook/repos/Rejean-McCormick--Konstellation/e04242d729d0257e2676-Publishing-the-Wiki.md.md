<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Publishing-the-Wiki | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 080c0bc5a8e9a9f6f12692062b6b10133763aa6f8596c34b6e50995ba7caf735 -->

# Publishing This Wiki on GitHub

This package is structured for a **GitHub Wiki Git repository**: `Home.md` is the home page, `_Sidebar.md` is the navigation menu, and `_Footer.md` is the footer. Other `.md` files are individual pages.

## Publish without overwriting an existing wiki

1. Enable **Wiki** in the Konstellation repository's GitHub settings, if permitted.
2. Back up or clone the existing wiki. If content already exists, compare and merge changes before replacing `Home.md` or `_Sidebar.md`.
3. Clone the **wiki Git repository** (not the source repository), replacing the organization placeholder:

```powershell
git clone https://github.com/ORGANIZATION/Konstellation.wiki.git
```

4. Copy the `.md` files from this ZIP to the **root** of the `.wiki` repository.
5. Check internal links and review private data before publishing publicly.
6. Commit and push **after review**:

```powershell
git add *.md
git commit -m "docs(wiki): add English Konstellation wiki"
git push
```

GitHub may require wiki initialization through the UI or sufficient repository permissions. These instructions **do not assume** a connected GitHub account, write access, or an existing wiki.

## Alternative

Keep these same `.md` files in the Konstellation repository's `docs/wiki/` directory and link them from `README.md`. This is a **documentation set**, not a platform change.

## Maintenance guidance

Update `Sources-and-Status.md` as snapshots evolve. **Never present a draft as a final standard**; clearly identify limitations of experimental features.
