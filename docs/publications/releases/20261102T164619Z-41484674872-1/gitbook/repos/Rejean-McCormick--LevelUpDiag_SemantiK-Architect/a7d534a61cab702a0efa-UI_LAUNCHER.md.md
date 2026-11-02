<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag_SemantiK-Architect/blob/4c8505150eae36193bc32cff587ba0860d608f2f/docs/UI_LAUNCHER.md | commit: 4c8505150eae36193bc32cff587ba0860d608f2f | SHA-256: 980a1de75fae165441e1a11721455b31100887703a9650b63a10a33ea6ff333d -->

# LevelUpDiag Windows UI

`LevelUpDiag_UI.pyw` is a thin desktop shell over the existing LevelUpDiag CLI. It does not duplicate diagnostic logic.

## Launch

Double-click `RUN_LEVELUPDIAG_UI.vbs`.

The VBS launcher uses Windows Script Host, prefers `pythonw.exe`, and falls back to a hidden `python.exe`. The UI pack does not ship a batch-file UI launcher because a `.bat` file itself can flash `cmd.exe` when double-clicked.

## Behavior

The UI starts `levelupdiag.py` as a subprocess. This preserves the CLI's worker isolation and report format. Output is streamed into the UI. The selected target is passed using the existing global `--target` option.

Campaign results are read from:

```text
<TARGET>/.levelupdiag/latest/summary.json
<TARGET>/.levelupdiag/runs/<RUN_ID>/...
```

The UI does not install Python packages, does not use uv, does not start SemantiK Architect services, and does not modify tracked target files.

## Stop

On Windows, Stop uses `taskkill /T /F` for the active LevelUpDiag process tree. This is intentionally limited to the PID started by the UI.

## UI state

The launcher remembers target, campaign, jobs, and fail-fast in `.levelupdiag_ui.json` beside the tool. This file is gitignored.


## No-console Windows mode

Double-click `RUN_LEVELUPDIAG_UI.vbs` for the silent desktop launcher. It prefers `pythonw.exe` and falls back to a hidden `python.exe`. Windows subprocesses launched by the UI and diagnostic engine use `CREATE_NO_WINDOW`, preventing console flashes during Doctor, campaigns, workers, Git checks, tests, and process termination.
