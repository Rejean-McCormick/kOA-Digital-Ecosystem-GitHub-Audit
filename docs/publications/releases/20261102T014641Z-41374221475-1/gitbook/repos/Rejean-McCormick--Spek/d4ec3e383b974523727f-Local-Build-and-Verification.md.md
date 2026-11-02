<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Local-Build-and-Verification | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: b32b16929278dc06befebfa3f2a2897ccdad65374d404eece38ed3d9e456d8b9 -->

# Local Build and Verification

## Commands

```bash
python -m spek check
python -m spek build --out dist --formats html,pdf,tex
python -m spek verify-site dist
```

The build generates a landing page, a per-language article page, TeX sources, and PDFs (if selected). Output is staged locally and replaced as an integral directory rather than silently mixed with older builds.

## Manifest

`dist/manifest.json` records:

- Build mode: `demonstration` or `production_candidate`.
- Article ID and ordered languages.
- Layout IDs and versions.
- Hashes of the input article, realization bundle, and layout definitions.
- SHA-256 checksums for every emitted file except the manifest itself.
- A status explicitly stating that the material is **built, not published or activated**.

Run `verify-site` before distributing a site. It refuses unknown extra files, altered checksums, symlinks and unsafe manifest paths.

## Rendering limitations

PDF uses ReportLab; `.tex` is generated separately and can be typeset using XeLaTeX. Cross-format visual parity is reviewed manually; a matching checksum is not an assertion that the scientific text is correct.

## Reproducibility

Given unchanged inputs, renderers should produce repeatable files. Keep versions of the compiler, environment, font availability, and upstream realization bundles when preserving research releases.

## Private Wiki drafts (separate, optional code overlay)

After installing the Spek/Arketype Wiki extension, `python -m spek build-wiki` emits Markdown plus a distinct draft `manifest.json`; `python -m spek verify-wiki <output>` checks its inventory. This verifies local file consistency, **not** SemantiK/GF attestations, signed C1/C2/C3 approvals, Wiki activation or public deployment. See [[Wiki Draft Workflow]].
