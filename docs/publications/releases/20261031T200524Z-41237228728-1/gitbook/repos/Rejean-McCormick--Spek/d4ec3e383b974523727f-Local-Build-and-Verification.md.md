<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Local-Build-and-Verification | commit: 931abd10aa17501162a185fc13019300769a67db | SHA-256: 79fd1d376ffe2c12017fe5c3f1ced9a062004befb9b880399b06713a861dd43c -->

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
