<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-Orgo/blob/79d495e637838784a1e137a7cf83722354f020f2/docs/SECURITY_MODEL.md | commit: 79d495e637838784a1e137a7cf83722354f020f2 | SHA-256: 0f654953376a28339f067abf352d07dd88c33f6e58b0ac44873a7bd391d209f0 -->

# Security and non-mutation model

LevelUpDiag is diagnostic tooling, not a sandbox.

The neutral frame reduces risk by:

- not auto-executing discovered project commands;
- using `shell=False`;
- bounding external commands with timeouts;
- blocking declarations marked mutating or networked unless explicitly enabled;
- excluding diagnostic source/evidence from target scans;
- redacting common credential assignments in command output;
- never recording the matched secret value in security-hygiene findings;
- checking target-relative working directories;
- sampling tracked Git state before/after a campaign.

The generic security level is a **hygiene heuristic**, not proof that the repository is secure. Findings are warnings because generic pattern matching can produce false positives.
