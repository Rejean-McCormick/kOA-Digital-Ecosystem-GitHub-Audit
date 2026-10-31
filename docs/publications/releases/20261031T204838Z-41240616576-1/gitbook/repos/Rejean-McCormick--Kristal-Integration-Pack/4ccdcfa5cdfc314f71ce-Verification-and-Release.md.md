<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Verification-and-Release | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 2ba78b542c482c985f1e3e9eedc6f54407f38c90926d42cc2f750086e7196376 -->

# Verifying and Releasing the Integration Pack

## Verify the source distribution

From the extracted Pack repository root:

```bash
python tools/verify_manifest.py
python -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/*.test.mjs
```

`MANIFEST.sha256.json` is the Pack's source integrity manifest. SHA-256 confirms the bytes measured by the manifest but **does not independently certify the publisher or the upstream provenance** of referenced external Framework/Wikidata data.

When testing v11, supply the **exact** Framework checkout; `v11_integration.py` explicitly rejects changed pinned files. Set `KRISTAL_FRAMEWORK_ROOT` and `KRISTAL_AUTHORING_KIT_ROOT` for integrated tests where applicable.

## CI

The Pack's `.github/workflows/ci.yml` installs Python 3.13 and Node 24, runs Python and Node checks, compiles selected Python files, and verifies the repository manifest. It contains **no publishing or deployment step**. Without the external checkouts, the workflow operates in unit-only mode.

## Wiki publishing (manual)

This documentation archive is formatted for a GitHub Wiki (one `Page-Title.md` per page, with `Home.md`, `_Sidebar.md`, and `_Footer.md`). To publish it:

1. Obtain permissions for the **correct GitHub repository's Wiki**.
2. Clone its `<repository>.wiki.git` repository, back it up and review differences against these files.
3. Copy these Markdown pages into that wiki checkout, commit with an appropriate reviewed message and push through your normal repository policy.
4. Open the GitHub Wiki and verify navigation, rendering and page permissions.

**No GitHub push has been performed by this wiki creation.** Publishing documentation must not be mistaken for deploying the Integration Pack or activating a Kristal.

See [[Qualification-and-Testing]] and [[Security-and-Trust-Boundaries]].
