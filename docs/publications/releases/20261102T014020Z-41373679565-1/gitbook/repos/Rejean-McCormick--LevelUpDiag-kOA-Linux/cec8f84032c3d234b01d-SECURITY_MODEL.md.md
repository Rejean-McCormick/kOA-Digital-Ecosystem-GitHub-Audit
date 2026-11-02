<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-kOA-Linux/blob/5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5/docs/SECURITY_MODEL.md | commit: 5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5 | SHA-256: b8cf498f59c451104f4d8bdc5dba9524477b95100313ce214bca861732f806a3 -->

# Security model

LevelUpDiag-Koali remains read-oriented and bounded:

- commands execute as argument arrays with `shell=false`;
- stdout/stderr capture is bounded and redacted;
- target mutation is disabled by default;
- network use is disabled unless explicitly enabled;
- referenced gate reports are accepted only from bounded paths inside the target repository;
- worker timeouts remain explicit.

Git tracked-state protection is now **mode-scoped**:

- DEBUG: disabled; Git provenance is not a prerequisite for diagnosis;
- VALIDATION: disabled globally; N02 can still observe repository state when selected;
- RELEASE: enabled and tracked-state mutation during diagnostics is an error.

This keeps release provenance strict without making Git formalities part of ordinary system debugging.
