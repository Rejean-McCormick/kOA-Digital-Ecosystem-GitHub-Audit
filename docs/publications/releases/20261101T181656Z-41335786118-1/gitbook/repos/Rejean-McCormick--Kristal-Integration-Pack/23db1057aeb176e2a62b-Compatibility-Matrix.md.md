<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Compatibility-Matrix | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 0036a3761ecf61e429b44b83b67e0be4763fb7b1b3f5e0691c1568952cebfca1 -->

# Compatibility Matrix

This matrix distinguishes **source compatibility** from **completed end-to-end qualification**.

| Interface | Pinned or expected version | Evidence and limit |
| --- | --- | --- |
| Framework v11 | Exact `11.0.0-draft.4` checkout | `VERSION` plus 13 SHA-256-pinned files; local tests reported |
| Framework v11 view format | `kristal.integration.read-view/v11.0-draft.1` | Consumer accepts structurally compatible older draft.3-derived views; structural reading is not revalidation of canon |
| diK import receipt | `dik.large-import/1.0-candidate` from `1.0.0-alpha.7` | Synthetic shape, hash and idempotency key tested; **no actual diK binary output tested** |
| Authoring Kit | `4.0.0-draft.3` | Temporary copy of demo workspace passed import/register/select/check; Kit itself has a Framework draft.3 pin |
| Arketype | `1.6.0` | Ecosystem documentation baseline; not runtime-qualified by this Pack |
| Kompiler protocol | `kompiler.capabilities` and `kompiler.context-pack` `1.0`/`1.1` | Local bridge validation; historical C5 against Kompiler 0.8 |
| Legacy state projection | Kristal v6 | Only derived from a compatible v7 Surface via Kompiler |
| Legacy Konstellation overlay | Historical unmodified `1.0.0-rc.2` source | Candidate with strict install refusal; no new production build or live browser requalification |
| Konstellation app runtime | Node.js 24.15+ recommended in upstream release environment | Pack's stand-alone CLI can use Node 22+; does not certify host application |

The Pack does **not** silently upgrade the Kit's own Framework pin, reinterpret old schema content, or bypass independent approval requirements.

See [[Prerequisites-and-Pinning]], [[Qualification-and-Testing]], and [[Limits-and-Roadmap]].
