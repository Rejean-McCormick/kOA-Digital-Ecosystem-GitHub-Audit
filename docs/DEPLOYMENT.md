# Deployment: one private GitHub repository

1. Create a **private**, separate repository: `kOA-Digital-Ecosystem-GitHub-Audit` (do not put the observer inside the architectural `kOA-Digital-Ecosystem` repository).
2. Upload the contents of this project to that repository. Do not upload ZIP snapshots containing source trees, local paths or historical raw findings.
3. Create a GitHub App installed on the selected account/repositories. Grant **read-only** permissions: repository Metadata (included by default), Contents (for inventory), Actions, Code scanning alerts, Dependabot alerts, Secret scanning alerts. For optional public repository discovery, the code queries public account endpoints; private discovery is not implemented. No Actions write, Contents write, Administration write or Secrets write.
4. In the new repository, set Actions variable `KOA_AUDIT_APP_ID` to the App ID and Actions secret `KOA_AUDIT_APP_PRIVATE_KEY` to its private key. The workflow mints a short-lived installation token using `actions/create-github-app-token@v2`.
5. Fallback (less preferred): create secret `KOA_AUDIT_READ_TOKEN` containing a tightly scoped, expiring read-only token. Never define both unless you understand precedence: the GitHub App token takes priority.
6. Run the **Audit tool CI** workflow, then trigger **kOA ecosystem GitHub observation** through `workflow_dispatch`.
7. Confirm 49 entries under current live inventory, correct source SHA, and whether the observed statuses are complete. Read the access gaps before interpreting a zero count.
8. Review workflow artifacts (retention 14 days), protect the observer repository and grant artifact access only to trusted maintainers.
9. Keep the weekly schedule only after the pilot succeeds. The workflow's successful execution means the collection process completed, not that all 49 repositories passed security validation.

## Workflow permissions and current GitHub rules

The default `GITHUB_TOKEN` for this central repository does **not** generally provide security-alert access to all other repositories. Use an App installed on the audited repositories. GitHub API feature/plan restrictions can yield `403` or `404`; the observer records those as unknown, not as no vulnerabilities. For broad enterprise policy enforcement, organization-managed security configurations are separate and **not** created by this repository.

## Recommended supply-chain hardening before production

Consider pinning every GitHub Action to a reviewed full-length immutable commit SHA and updating via Dependabot. The supplied YAML uses maintained major-version tags for portability, **not SHA pinning**. Enable branch protection/review and security alerting on this observer itself; the auditor must be protected as a sensitive operational component.

## Failure modes

- Missing App/PAT token: workflow fails deliberately with `--require-auth` (no apparent success with anonymous API limits).
- Missing remote inventory/access: fails before starting a partial batch; does not silently substitute an old snapshot.
- Insufficient per-repository permissions: report shows unknown for affected categories.
- API pagination cap: result is marked partial and count is a lower bound.
- Unsupported CodeQL analysis or no default branch: coverage unknown/not observed, not PASS.
