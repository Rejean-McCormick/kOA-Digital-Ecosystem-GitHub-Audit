# Security

The local scanner reads repositories under explicit local roots without executing repository code, contacting GitHub or altering files. Scan reports remain local, gitignored, and may reveal file paths or operational metadata; do not publish them indiscriminately. Potential credential strings are never copied into reports: only rule names, file paths and line numbers appear. File and discovery budgets prevent runaway scans. Symlinks are not traversed.

Offline heuristics cannot establish the absence of vulnerabilities and do not replace CodeQL, dependency advisory databases, production/runtime tests or professional review. Historical PASS/FAIL results do not become contemporary security claims.

## GitHub Pages public dashboard (v0.5.0)

The optional dashboard writes ONLY allowlisted aggregate counts to `docs/data/dashboard.json` and ships a static browser client. It never publishes raw `audit.json`, `audit.csv`, repo names, exact file paths, Git SHAs or secret-bearing code excerpts. Previous dashboard snapshots are also re-sanitized on each update. The source report remains in the ignored `reports/` folder.

GitHub Pages generally serves **public** sites. Inspect the aggregate JSON before enabling publishing. The application does not automatically git commit or push a dashboard, and will never send the full local audit report to GitHub.

La publication v0.6 ne copie aucun rapport brut ou fichier source, uniquement docs/data/dashboard.json (liste d’attributs autorisés) et le workflow GitHub Pages. Vérifier les permissions de GitHub Pages : site potentiellement public.
