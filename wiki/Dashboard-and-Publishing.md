# Dashboard and Publishing

The browser dashboard lives in `docs/index.html`; it uses the supplied kOA logo and brand color **`#1e6864`**. The dashboard displays **aggregate published snapshots**, not live information from your computer.

## Two separate data views

- **Local Audit** (`LOCAL_OBSERVE`): reference inventory coverage, inspection limits, heuristic findings, local engineering surface and configured-control indicators.
- **GitHub / CI** (`OBSERVE`): metadata visibility, latest observed CI conclusions, unknown security-alert coverage, and API limitations.

These views are **not blended**. Data with no access or with API errors remains **unknown**, not zero. No score on the dashboard certifies project completion or security.

## Local preview

In the launcher, open **Tableau de bord**, then **Aperçu dans le navigateur**. It starts a local HTTP server bound to `127.0.0.1`, opens the browser, and works only while the application remains open. This server does not publish information online.

If the browser shows `ERR_EMPTY_RESPONSE`, ensure you are using the launcher from v0.6.1 or newer. See [Troubleshooting](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Troubleshooting).

## Update from existing reports (no rescan)

In **Tableau de bord**, select a previously generated local or GitHub `audit.json` and use **Mettre à jour le tableau de bord**. Alternatively:

```powershell
python -m koa_audit dashboard-publish --audit-json reports/audit.json --out docs
```

The aggregate file is `docs/data/dashboard.json`. It keeps a bounded campaign history and allowlists public-safe numeric fields. It intentionally omits full repository identities, source paths, Git SHAs, raw security findings, private-key material and profile notes.

## Optional GitHub Pages deployment

1. In the desktop app, use **Publier sur GitHub (1 clic)**. This publishes the allowlisted aggregate and the Pages workflow to the **audit repo only**, using the Git credentials already configured on Windows.
2. If the first deployment is not enabled, set **Settings → Pages → Build and deployment → Source: GitHub Actions** in the audit repository.
3. `.github/workflows/dashboard-pages.yml` deploys the static `docs/` content when the relevant push lands on `main`.

The application does **not** force-push, mutate the 49 source repositories, publish the full `audit.json`, or rerun a full audit as part of this action. The existing Git authentication must have permission to push files and workflows.

### Update frequency

The browser requests the published aggregate file roughly every **three minutes**. The contents change only when a new aggregate is published. GitHub Pages cannot read `C:\mycode` on your PC.

## Important privacy distinction

GitHub Pages generally serves a **public site**. The detailed engineering profiles, checklist assessments, and audit reports stay **local** in this version; only carefully limited summary counts are published. Always review `docs/data/dashboard.json` before first publication.

The [GitHub Wiki](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Home) is a **separate** documentation service and is not populated automatically by the Pages workflow.
