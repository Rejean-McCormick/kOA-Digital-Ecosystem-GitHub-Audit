# Troubleshooting

## The launcher does not open when double-clicked

- Extract the **whole ZIP** before launching; do not copy only a `.pyw` into an unrelated folder.
- Check that Python **3.11+** with Tkinter is available.
- Run `DIAGNOSTIC_LAUNCHER.cmd` from the application folder to see the error and get a diagnostic log.
- Make sure the application can access its `koa_audit`, `profiles`, `data`, and `docs` folders.

## Browser preview shows `ERR_EMPTY_RESPONSE`

The fixed v0.6.1+ launcher prevents the local HTTP server from trying to write logging output into a nonexistent `pythonw.exe` console. Close older app windows and stale browser tabs, then open **Tableau de bord → Aperçu dans le navigateur** again with the current launcher.

- The preview uses a temporary `127.0.0.1` port and only works while the application is running.
- Closing the application stops the preview server; this is expected.
- A local preview is not evidence that GitHub Pages is already deployed.

## Some repositories are missing or duplicated

- Check the selected local root and search-depth limit.
- Repositories outside the inventory may be discovered but do not automatically become part of the 49-name reference.
- A repository with two local clones may be marked ambiguous; review both locations manually. The app does not delete or select clones automatically.

## CodeQL / Dependabot / Secret Scanning reports say `unknown`

Offline mode can only inspect local configuration, not platform alert status. The optional GitHub API observation may be limited by HTTP 401/403/429 or unavailable features. **Unknown is not zero**.

## The dashboard looks out of date

- Check the dashboard's **last published snapshot** timestamp.
- Generate a fresh aggregate from an already available audit report; no new scan is necessary solely to republish.
- GitHub Pages updates only after the aggregate is pushed and deployed. The browser checks for a newer aggregate approximately every three minutes.

## GitHub Pages publication is rejected

- Verify Git credentials and write permission for the **audit repository**.
- If workflow file permissions are denied, the Git push may fail. Do not use a force push.
- If needed, configure **Settings → Pages → Source: GitHub Actions** once.

## Profile import or checklist changes are missing

- Check that you selected the correct inventory repository and profile type before importing.
- Ensure the Markdown file is nonempty and within the app's size restrictions.
- Manual checklist records persist in `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\assessments.json`, not in the extracted app folder.

## GitHub Wiki is not showing the new pages

The Wiki and Pages are separate. Saving files under `wiki/` in the main repo does **not** publish them into the GitHub Wiki. Follow [Wiki Publishing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Wiki-Publishing).
