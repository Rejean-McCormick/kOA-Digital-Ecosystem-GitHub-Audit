# Security

The local scanner reads repositories under explicit local roots without executing repository code, contacting GitHub or altering files. Scan reports remain local, gitignored, and may reveal file paths or operational metadata; do not publish them indiscriminately. Potential credential strings are never copied into reports: only rule names, file paths and line numbers appear. File and discovery budgets prevent runaway scans. Symlinks are not traversed.

Offline heuristics cannot establish the absence of vulnerabilities and do not replace CodeQL, dependency advisory databases, production/runtime tests or professional review. Historical PASS/FAIL results do not become contemporary security claims.
