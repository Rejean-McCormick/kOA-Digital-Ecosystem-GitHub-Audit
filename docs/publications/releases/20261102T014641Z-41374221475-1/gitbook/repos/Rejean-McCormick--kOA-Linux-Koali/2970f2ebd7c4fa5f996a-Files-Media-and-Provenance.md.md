<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Files-Media-and-Provenance | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 263c102848723c2f027d2d508faa87d0d3481d6e6aaaaf0ceea77873bb6c2088 -->

<!-- Explanatory wiki projection. Normative authority remains in the repository and subsystem documentation. -->

# Files, Media, and Provenance

> **Reading model:** The main path explains what the kOA ecosystem enables. The technical reference explains how kOA-Linux hosts, isolates, verifies, and operates those capabilities. Product-specific details remain in each subsystem's own documentation.

## Local authority

The **kOA Mediatheque** owns media and file records held by the local installation: identity, version, verified hash, managed content reference, metadata, provenance, rights, restrictions, relations, collections, languages, renditions, lifecycle, import/export history, backup, and restore state.

## Cultural context

Konnaxion's Kreative and Konservation layers add cultural context, creator and community authority, consent, exhibitions, collaboration, and rights-aware discovery. They should link to local media records rather than silently replace their authority.

## External UCKK objects

An object published to UCKK becomes a distinct UCKK object. A resource imported from UCKK becomes a distinct local kOA object. Provenance relates the records without merging databases or lifecycles.

## AI boundary

AI may propose tags, descriptions, translations, accessibility text, or duplicate candidates. The owning workflow accepts, rejects, or corrects those candidates; AI does not silently define meaning, rights, or authority.

Repository sources:

- [kOA Mediatheque system boundary](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/12-koa-mediatheque-system-boundary.md)
- [kOA Mediatheque component](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/04-components/koa-mediatheque.md)
- [UCKK publication bridge](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/04-components/uckk-publication-bridge.md)
