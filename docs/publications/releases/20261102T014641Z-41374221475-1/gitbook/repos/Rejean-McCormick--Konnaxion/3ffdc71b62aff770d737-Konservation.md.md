<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Konservation | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 64255b9c670da3b6dac86674870a18df208627a3598c79fe097f17df6bc0da0d -->

# Konservation — Kreative Preservation and Archives

Konservation is the cultural-preservation/archive capability inside **Kreative**. It is a product capability, not a separate ecosystem system.

Canonical backend:

```text
backend/konnaxion/kreative/
```

## Current preservation/creative models

- `KreativeArtwork`;
- `Gallery`;
- `CollabSession`;
- `TraditionEntry`;
- `VirtualExhibition`;
- `DigitalArchive`;
- `ArchiveDocument`;
- `AICatalogueEntry`;
- `CulturalPartner`;
- `Tag`.

## Current UI

Relevant surfaces include:

```text
/kreative/traditions-archive
/kreative/community-showcases/*
/kreative/creative-hub/*
/kreative/collaborative-spaces/*
```

## Ownership

Archive/catalogue/presentation metadata remains Kreative-owned. AI catalogue assistance or external storage does not silently become the source authority for the cultural object.
