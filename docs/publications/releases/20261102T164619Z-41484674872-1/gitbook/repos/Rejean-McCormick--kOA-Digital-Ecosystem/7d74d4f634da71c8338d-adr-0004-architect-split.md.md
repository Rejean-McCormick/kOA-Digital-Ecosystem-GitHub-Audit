<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/90-reference/adr/adr-0004-architect-split.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: a37fd868031e0b91bd4fa416d29205e541aa2bb9894f058670ab5836d2a343fd -->

# ADR-0004: Architect Strategy / Render split

- **Status:** Accepted; v5 semantics were amended by ADR-0008 and the active v6 knowledge interpretation is governed by ADR-0013

## Decision

Keep planning/strategy and rendering as separable responsibilities. Both consume material according to an explicit Reader Policy/Profile and preserve the source artifact's declared status/valuation/authority semantics.

Neither role may assign Kristal validation or authority recognition, mutate authoritative Kristal state by side effect, or manufacture factual claims through presentation.

## Historical v5 amendment

The earlier assumption that Architect consumed only “canonical truth after validation + compilation” was superseded. Kristal v5 permitted Reader Policies that exposed Working, disputed or lower-certainty material with labels. Strict production surfaces could still choose reference-only policies.

## Active v6 amendment

Under Kristal Standard `6.0.0`, Architect/SA surfaces preserve `kristal_state` semantics including typed `valuations[]`, `coordinates`, `applicability`, `record_role`, `actionability`, provenance/evidence, validation/recognition and `artifact_status`. Reader or rendering policy may filter or present these semantics but does not transfer authority or execution rights.
