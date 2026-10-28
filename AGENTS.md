# Contributor instructions

Default mode is LOCAL_OBSERVE. All local commands must work offline and without any GitHub token. Do not send local code, scan contents, or report paths to external services. Do not execute or modify target repositories. Treat legacy diagnostic results as separate historical evidence, never current security PASS. Do not overstate vulnerability coverage; local static heuristics do not execute CodeQL or check CVE advisories. Keep source repository authority separate from observation.

The `local-triage` command only reads local Git metadata and targeted source lines; it exports metadata-only ZIPs and MUST NOT export raw secrets, workflows or source code.

The `dashboard-publish` command must export only deliberately allowlisted aggregate numeric data. Never place `reports/audit.json`, `reports/audit.csv`, .env content, local paths, repo names, file paths or raw triage ZIPs under `docs/` or inside a Pages deployment. Treat local `LOCAL_OBSERVE` and remote `OBSERVE` as different datasets; unknown API coverage is not a zero-vulnerability result. No automatic push to GitHub.
