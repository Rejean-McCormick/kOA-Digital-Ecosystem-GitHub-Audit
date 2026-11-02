<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Publishing-the-GitHub-Wiki | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: dd9962041375dfc3a6d75a849e8cc92e99316b6bafd67c445d6d35dacacb190b -->

# Publishing the GitHub Wiki

The Markdown pages in this repository's `wiki/` directory are **source files** for a GitHub Wiki. Merely committing `wiki/` to the main repository **does not automatically publish them** to the Wiki tab. GitHub Wikis use a **separate Git repository**.

## Before you publish

- Confirm the correct GitHub repository and that its Wiki feature is enabled.
- Make sure you have permission to edit the wiki.
- Review the content: this documentation describes an **unapproved local prototype**, not an authorized Church school.
- Keep the teaching material language distinction: documentation is in English, course content is in `fr-CA`.

## Option A — GitHub web interface

Open the repository's **Wiki** tab, enable the wiki if permitted, then create or edit pages using the filenames and content from `wiki/`. The homepage is `Home.md`; `_Sidebar.md` and `_Footer.md` provide navigation and context.

## Option B — Publish via Git

After initializing the Wiki from GitHub if required, clone its dedicated repository. Replace `<OWNER>` and `<REPO>` with the actual repository coordinates; do not copy these placeholders verbatim.

```bash
git clone https://github.com/<OWNER>/<REPO>.wiki.git
```

Copy the contents of the main repository's `wiki/` directory **into the root** of that clone (not into a nested `wiki/` folder). Keep any existing custom wiki pages that still matter, or review deletions before proceeding.

```bash
cd <REPO>.wiki
git status
git add *.md
git commit -m "Document Ekole Pastorale in English"
git push
```

The repository name in these commands is illustrative; use your actual local directory. Run `git status` before committing and pushing. If the wiki is not yet initialized, create the first page in GitHub's UI before cloning.

## Naming and links

All pages use UTF-8 Markdown with **LF line endings** and a **single final newline**. No page contains a NUL (`\x00`) character. Internal links use relative Markdown page paths so they remain readable in a local checkout.

## Update discipline

1. Edit `wiki/*.md` in the main content repository.
2. Review the changes, check internal links, and check for NUL bytes.
3. Commit the source documents.
4. Push the corresponding Markdown files into `<REPO>.wiki.git`.
5. Review the rendered Wiki in GitHub to confirm navigation works.

This workflow intentionally does not rewrite the canonical Kristals or derived Ekole course files.
