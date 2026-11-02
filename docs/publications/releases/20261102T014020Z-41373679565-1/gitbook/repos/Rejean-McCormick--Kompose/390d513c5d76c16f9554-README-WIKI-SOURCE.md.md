<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/README-WIKI-SOURCE | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 51e66437a15bd41f39b2795b2be591022afa4d06096636b2badd05a82e1ee158 -->

# KOMPOSE GitHub Wiki Source

This folder is the **English-language local wiki source updated against the supplied v0.2.0 code snapshot on 2026-10-27**. It is **not** an independently verified, published GitHub wiki or a new software release. These Markdown pages can be imported into GitHub's separate wiki Git repository, usually `<OWNER>/<REPO>.wiki.git`, after creating and enabling the wiki.

- `Home.md`: homepage.
- `_Sidebar.md`: sidebar navigation.
- `_Footer.md`: persistent footer.
- `Tandem-Orgo-Boundary.md`, `Kontexte-B6-Preview.md`, and `Ekole-P1-Preview.md`: current operational boundary and safe local example guides.
- Remaining `*.md` files: topic pages.

## Synchronization

A GitHub wiki uses a **separate Git repository** from the project's source code. Changes must be synchronized intentionally. Avoid `git push --force` on any collaboratively edited wiki.

Wiki page links use GitHub's double-bracket page-link syntax (page name and optional display label). The normative source of structural contracts remains `contracts/`: this wiki explains the system and links to paths in the code repository.

## Publish after creating the GitHub repository

1. Publish the KOMPOSE source to a GitHub repository under appropriate access permissions.
2. Enable the **Wiki** feature and create its first page.
3. Clone the wiki using the URL shown by GitHub (`git clone https://github.com/OWNER/REPO.wiki.git`).
4. Copy the reviewed `*.md` pages from this directory to the wiki checkout (including `_Sidebar.md` and `_Footer.md`); omit `README-WIKI-SOURCE.md` if you do not want it published as a wiki page. Preserve unrelated wiki files.
5. Run `git add . && git commit -m "docs: publish English KOMPOSE wiki" && git push`.

Publication and GitHub permissions remain with the repository owner. **No online wiki is created by the provided archives.**
