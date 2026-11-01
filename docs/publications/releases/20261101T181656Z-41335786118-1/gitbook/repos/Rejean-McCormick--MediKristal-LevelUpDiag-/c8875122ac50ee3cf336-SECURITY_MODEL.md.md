<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal-LevelUpDiag-/blob/ce1c0dead57361ef21f9e3fcd8043711124ba41d/docs/SECURITY_MODEL.md | commit: ce1c0dead57361ef21f9e3fcd8043711124ba41d | SHA-256: 94d14cd38a5ff7f20cf40ee7e3a43b99c333418702ce5c6df604d181c148281f -->

# Security and non-mutation model

LevelUpDiag is diagnostic tooling, not a sandbox.

This MediKristal-specific suite reduces risk by:

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
