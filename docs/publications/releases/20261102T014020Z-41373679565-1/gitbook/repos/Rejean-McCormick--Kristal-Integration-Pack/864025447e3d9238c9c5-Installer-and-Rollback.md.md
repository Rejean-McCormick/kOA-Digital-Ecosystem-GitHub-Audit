<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Installer-and-Rollback | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 373b97406772fa027fefea306880b44c35e7f00f39cf7ba20dfcf4c7ef5a056a -->

# Legacy Installer: Preview, Status and Rollback

`tools/install.py` is retained for historical Konstellation overlays. It **must not** be used to force an old bridge onto a newer or already integrated checkout.

## Read-only status

```bash
python tools/install.py /path/to/Konstellation --status
```

Inspect `existing_integration`, recorded patch hashes, installed overlay equivalence and `recommendation`. A result of `DO_NOT_REINSTALL_EXISTING_INTEGRATION` means **stop and request owner review**.

## Preview and apply — legacy unmodified host only

```bash
python tools/install.py /path/to/Konstellation
# Review the preview and current checkout BEFORE any write.
python tools/install.py /path/to/Konstellation --apply
```

`--apply` is a write operation. It is restricted to an independently verified **unmodified** historical Konstellation `1.0.0-rc.2` source. Take a backup and obtain operator authorization first. Do not use it on the already integrated snapshot described in this release.

## Guarded rollback

```bash
python tools/install.py /path/to/Konstellation --rollback
```

Rollback uses the recorded backup and refuses to overwrite owner modifications made after installation. A refused rollback is a deliberate safety gate, not a request to delete or rewrite hashes manually.

## Scope limits

- Rollback concerns this historical **source overlay**, not a published Kristal, GitHub release or canonical state.
- The v11 preflight and reader tools run directly; they do **not** require overlay installation.
- A source overlay is not host authorization or an application production qualification.

See [[Konstellation-Overlay]], [[Troubleshooting]], and [[Security-and-Trust-Boundaries]].
