# Profile batch validation

- 13 source snapshots from `EP.zip` mapped to 13 independently generated engineering profiles.
- Each profile has its exact nested snapshot SHA-256, capture timestamp and indexed archive entry count.
- 12 profiles belong to the bundled 49-repository inventory; one is explicitly supplemental.
- Machine-readable `ENGINEERING_METRICS.json` counts were cross-checked against the exported CSV index.
- Source snapshots were not bundled and source project code was not executed.
- No current cyclomatic complexity, code coverage, CI success or security quality grade is claimed.
- The desktop application test suite passes and a GUI profile-selector smoke test was run in a virtual display.
