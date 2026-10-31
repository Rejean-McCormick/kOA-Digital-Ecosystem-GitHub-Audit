<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Core-Concepts | commit: 931abd10aa17501162a185fc13019300769a67db | SHA-256: cf554c782650dc2dd19bca7b12520e38f5e91c0643db81dd4738e537cbbca80a -->

# Core Concepts

## Canonical state

Kristal's canonical knowledge has upstream governance. Spek neither rewrites nor replaces it; compilation starts from a **derived editorial projection**.

## Semantic unit

A stable identifier, type (`claim`, `premise`, `qualification`, etc.), epistemic status and optional evidence references. Units remain identifiable in output HTML.

## Realization

A localized short expression bound by `realization_key`, `language`, and declared qualification state. SemantiK can eventually provide these; the present demo uses manually prepared fixture sentences.

## Layout

A versioned, typed contract describing allowed information and cardinality. The layout produces **reading order and visual hierarchy**, while semantic units carry the subject matter. Layouts are not scientific evidence.

## Spek sheet and article

A **Spek sheet** is a rendered section such as a result card. A larger article is an ordered composition of sheets; it need not mimic long prose to explain a finding, method, argument, or comparison.

## Build artifact

HTML, PDF, and XeLaTeX are derived representations. Their manifest records source/realization/layout fingerprints and output checksums.

## Publication versus activation

Local build, language verification, scientific review, disclosure authorization, public deployment and Kristal activation are distinct, governed actions. Neither CI success nor a `production_candidate` manifest permits skipping the upstream gates.
