<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Core-Concepts | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: a3f17695778972af65e75b0743ad0fe7f0348b9cd0d79cd02af9d140091141db -->

# Core Concepts

## Canonical state

Kristal's canonical knowledge has upstream governance. Spek neither rewrites nor replaces it; compilation starts from a **derived editorial projection**.

## Semantic unit

A stable identifier, type (`claim`, `premise`, `qualification`, etc.), epistemic status and optional evidence references. Units remain identifiable in output HTML.

## Realization

A localized short expression bound by `realization_key`, `language`, and declared qualification state. SemantiK Architect can supply these through an explicit upstream bridge; the shipped demo uses manually prepared fixture sentences. The optional Wiki integration accepts frozen qualified declarations but does not itself invoke SemantiK.

## Layout

A versioned, typed contract describing allowed information and cardinality. The layout produces **reading order and visual hierarchy**, while semantic units carry the subject matter. Layouts are not scientific evidence.

## Spek sheet and article

A **Spek sheet** is a rendered section such as a result card. A larger article is an ordered composition of sheets; it need not mimic long prose to explain a finding, method, argument, or comparison.

## Build artifact

HTML, PDF, and XeLaTeX are derived representations. Their manifest records source/realization/layout fingerprints and output checksums.

## Publication versus activation

Local build, language verification, scientific review, disclosure authorization, public deployment and Kristal activation are distinct, governed actions. Neither CI success nor a `production_candidate` manifest permits skipping the upstream gates.

## Arketype profile and Wiki page

An Arketype profile is a content-structure compatibility choice, **not** a new Spek layout contract. In the optional Wiki extension it constrains which of the eight Spek layouts may appear in a page. Spek assembles the selected sections into GitHub Wiki Markdown only after the upstream owner has supplied typed units and realizations. See [[Wiki Templates by Archetype]].
