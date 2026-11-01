<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/CLI-Reference | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: e62f1361305061f3605eac98990913f121fc44e6b26fe89ecd12ee5be95e8878 -->

# Command-line Reference

Run commands from the Integration Pack repository root. Paths in examples are illustrative and must refer to actual checkouts or data.

## Framework v11 — Python

```text
python tools/v11_integration.py check|coverage|view \
  --framework DIR --registry FILE --graph FILE \
  --crosswalk FILE --catalog FILE \
  [--locale TAG | --locales TAG,TAG] [--out NEW_FILE]
```

- `check`: no locale flags.
- `coverage`: optional `--locales`, not `--locale`.
- `view`: required `--locale`, not `--locales`.
- All operations validate the pinned Framework first.

## Framework v11 — Node bridge

```text
node tools/kristal-bridge.mjs v11 --operation check|coverage|view \
  --framework DIR --registry FILE --graph FILE \
  --crosswalk FILE --catalog FILE [--locale TAG|--locales TAG,TAG] [--out NEW_FILE]
```

## diK/Kit handoff — Python or Node

```text
python tools/v11_handoff.py --framework DIR --catalog FILE \
  --registry FILE --crosswalk FILE [--graph FILE] [--locales TAG,TAG] \
  [--kit-import-candidate] [--dik-job FILE] [--out NEW_FILE]

node tools/kristal-bridge.mjs v11-handoff --framework DIR \
  --catalog FILE --registry FILE --crosswalk FILE \
  [--graph FILE] [--locales TAG,TAG] \
  [--kit-candidate yes] [--dik-job FILE] [--out NEW_FILE]
```

The `dik-job.json` check is allowed only in candidate mode. None of these commands **registers** or **selects** a catalog.

## Historical local Kompiler CLI

```text
node tools/kristal-bridge.mjs doctor
node tools/kristal-bridge.mjs run --query FILE --out NEW_FILE
node tools/kristal-bridge.mjs project --pack FILE --out NEW_DIRECTORY [--surface ID]
node tools/kristal-bridge.mjs author --action inspect|status|check|read-surface|build-v9|publish-v9 \
  --tool FILE --workspace DIR [--confirm ACTION]
```

The CLI rejects unsupported commands, unknown or duplicated flags, and arbitrary shell arguments. `author` write actions also require `KRISTAL_ALLOW_WRITE=1`.

## Installer, C3, checks

```text
python tools/install.py KONSTELLATION_PATH --status
python tools/install.py KONSTELLATION_PATH                  # preview
python tools/install.py KONSTELLATION_PATH --apply          # legacy only, guarded
python tools/install.py KONSTELLATION_PATH --rollback
python tools/check_c3_readiness.py --collection DIR --mode scan|validate-index
python tools/verify_manifest.py
```

See [[Framework-v11-Reader]], [[Legacy-Kompiler-Bridge]], [[Installer-and-Rollback]], and [[C3-Collection-Checks]].
