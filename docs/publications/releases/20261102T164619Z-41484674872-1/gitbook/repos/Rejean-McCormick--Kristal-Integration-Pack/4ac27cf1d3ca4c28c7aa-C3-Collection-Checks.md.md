<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/C3-Collection-Checks | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 38c0a8bff91ef0550a04acef75ce2638329181b6406d568e9a0e86699cf1eeb7 -->

# C3 Collection Readiness

`tools/check_c3_readiness.py` delegates to the collection owner's **local read-only** verifier, `tools/c3_collection.py`. It deliberately does not create an index or imitate the owner checker.

```bash
python tools/check_c3_readiness.py \
  --collection /path/to/kristal-public --mode scan

python tools/check_c3_readiness.py \
  --collection /path/to/kristal-public --mode validate-index
```

A missing owner script reports **`NOT_EVALUATED`**. A failed structural check reports **`C3_BLOCKED`**; a successful one reports **`C3_LOCAL_STRUCTURE_PASS`**. Both outcomes explicitly leave C1/C2 authorization and remote publication unverified.

The previously supplied public collection snapshot was missing `kristals/index.json`. This does not authorize the Integration Pack to invent a replacement public index or announce a successful publication.

**C3 structure ≠ independent C1 evidence ≠ C2 visibility grant ≠ deployed public release.** These are separate owner-controlled gates.

See [[Architecture-and-Ownership]], [[Security-and-Trust-Boundaries]], and [[Qualification-and-Testing]].
