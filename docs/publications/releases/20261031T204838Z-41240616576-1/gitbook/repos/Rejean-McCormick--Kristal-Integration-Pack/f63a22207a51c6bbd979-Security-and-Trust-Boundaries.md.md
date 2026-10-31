<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Security-and-Trust-Boundaries | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: ef8d9b09b81eac8cd162d84fb6f5dc7f0af1695fb841d51df10ebcd359484499 -->

# Security and Trust Boundaries

The Pack is intentionally **read-only by default** and rejects operations it cannot authorize or verify.

## Framework v11 / diK

- Run only the **exact SHA-256-pinned** Framework `11.0.0-draft.4` validators and preflight code.
- Keep KQ/KP/KA/KS separate from display terms and Wikidata Q/P identifiers.
- Accept only reviewed `accepted + exactMatch` crosswalk semantics; no fuzzy-label identity inference.
- Preserve originals. Reports generated with `--out` must go to new paths.
- A diK `dik-job.json` receipt proves consistency of selected files, not approval, upstream authenticity or authority to select a catalog.
- Kit catalog registration and selection always remain **distinct, explicit owner operations**.

## Local Kompiler access

The stand-alone bridge permits **loopback HTTP only** (`localhost`, `127.0.0.1`, `[::1]`), disallows redirects, embeds no URL credentials and applies a 30-second request timeout and 8 MB response cap. The legacy Konstellation overlay uses its own origin/scope/size checks; the supplied security notes describe a default **2 MB** response cap there.

Secrets belong in scoped environment variables (for example `KOMPILER_TOKEN`), never in committed source or wiki examples. Derived Context Packs and projection receipts can still expose confidential data.

## Multiuser warning

**Do not enable the legacy Kompiler route for shared/multiuser traffic.** The source documentation does not demonstrate an unavoidable mapping from every Konstellation reader's policy and target privileges to each upstream Kompiler request. A global service credential is not a substitute for per-reader authorization.

## Publication and owner boundaries

- The Pack does not publish to GitHub, rewrite private/public collections, operate Manager, create signed commitments, or activate Kristals.
- C3 structural diagnostics are not independent C1 or C2 grants.
- Historical overlay installation/rollback is guarded and does not supersede Konstellation owner review.
- `GitSink.bat` and `ZmartZnap.pyw` are retained provenance utilities, not part of the documented v11 operation flow; do not run them for this workflow.

See [[Installer-and-Rollback]], [[diK-to-Authoring-Kit-Handoff]], and [[Limits-and-Roadmap]].
