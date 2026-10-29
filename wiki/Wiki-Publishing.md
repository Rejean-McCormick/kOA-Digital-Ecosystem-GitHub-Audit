# Publishing the GitHub Wiki

These English Wiki pages are bundled as source Markdown under the main repository's `wiki/` directory. **That directory is not the live GitHub Wiki.** GitHub stores wiki content in a **separate Git repository**.

## One-time setup

1. Open the GitHub repository: [kOA-Digital-Ecosystem-GitHub-Audit](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit).
2. Open its **Wiki** tab. If unavailable, a repository administrator may need to enable the Wiki under **Settings → Features**.
3. If this is a new wiki, create and save a simple **Home** page in the GitHub interface. This initializes the wiki repository for cloning.

Official GitHub documentation: [Adding or editing wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages).

## Publish the prepared pages

The main application archive includes a helper script **`PUBLISH_WIKI.ps1`**, which uses your existing Git for Windows credentials. It copies only Markdown pages from `wiki/`, shows a diff/status, asks for your approval, then performs a normal commit and push **to the Wiki repository only** (never force-pushes).

From PowerShell 7 inside the extracted audit repo:

```powershell
pwsh -NoProfile -File .\PUBLISH_WIKI.ps1
```

Or follow the manual workflow:

```powershell
# Clone the separate Wiki Git repository once it has a Home page
 git clone https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit.wiki.git
# Copy the .md pages from the application wiki/ folder to this clone.
# Review changes, commit, and push normally.
```

If your authenticated Git user lacks write access, publication will stop; your local documents remain intact.

## Safety and privacy

- Publish only documentation and descriptions already intended for readers.
- Do **not** copy private report JSON, `.env`, credential material, manual assessment notes, or detailed triage archives into the Wiki.
- The Wiki publisher never changes audited source repositories or the GitHub Pages dashboard.
- `_Sidebar.md` and `_Footer.md` become the Wiki navigation elements.
- The **GitHub Wiki may be public** when the audit repository is public. Check visibility before publishing.
