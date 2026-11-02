<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Wiki-Draft-Workflow | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 44c35e6e0d8525befe344cafc381508783fa55fa2018616843264477967fe563 -->

# Wiki Draft Workflow — Spek + SemantiK + Arketype

This guide concerns the **optional Spek Wiki/Arketype integration overlay**, installed separately from Spek 0.5. The following commands do not work on an unmodified Spek 0.5 checkout.

## Inputs for one selected Kristal

- `article.json`: a **derived** `kristal.layout-article-source/0.1` with explicit, already selected semantic units, evidence and ordered sections.
- `realizations.json`: `kristal.layout-realizations/0.1`, with the short expressions generated upstream by SemantiK Architect and bound to the keys expected by the article. For a real build, every used key declares SemantiK channel, qualification and runtime/request metadata.
- `archetype.json`: a typed, explicit `spek.wiki-archetype-binding/1.0` identifying an admitted Arketype slug (used in the collection orchestration).
- `state-snapshot.json`: the pinned v9 metadata provided for cross-checking a real source reference. This is **not** an independent JCS rehash or C1/C2 proof.

The current overlay does **not** automatically produce those files from raw Kristal assertions. A trusted upstream adapter is required, including a v6-compatible SemantiK communication projection and a real RuntimeSet capable of the selected utterances.

## Discover admissible templates

From the **Spek** root after installing the overlay:

```powershell
python -m spek list-wiki-templates
```

See [[Wiki Templates by Archetype]] for the exact 19-profile matrix.

## Non-publishable demonstration

```powershell
python -m spek build-wiki --source examples/article.json --realizations examples/realizations.json --archetype composition-hybride --slug spek-demo --language fr --out C:\private\spek-wiki-demo --demonstration
python -m spek verify-wiki C:\private\spek-wiki-demo
```

The resulting `Home.md`, `_Sidebar.md`, `Kristal-spek-demo.md` and `manifest.json` are **fixtures** for local inspection. They cannot be treated as a publication candidate for actual Kristals.

## Real, preapproved input preflight (not public publication)

```powershell
python -m spek build-wiki --source C:\private\kristal-ai\article.json --realizations C:\private\kristal-ai\realizations.json --archetype referentiel-semantique --slug kristal-ai --language fr --state-snapshot C:\private\kristal-ai\state-snapshot.json --out C:\private\wiki-ai-draft
python -m spek verify-wiki C:\private\wiki-ai-draft
```

The example paths are illustrative and only work when the declared files and semantic data really exist and satisfy the chosen layout. The renderer rejects missing required slots, unqualified/mismatched realization metadata or unsupported sections; it does **not** invent a result.

## Collection draft via Kristal-Manager / kristal-public

After installing the Manager + SemantiK and Spek/Arketype overlays, the Manager's publication panel provides a Spek Wiki composition action. Its private input bundle is expected to contain one folder per **C3-indexed slug**, with `article.json`, `realizations.json` and `archetype.json`. The `kristal-public` aggregation script checks that every indexed Kristal is accounted for and creates `Home.md`, `_Sidebar.md`, one `Kristal-<slug>.md` per entry, and a `manifest.json` tied to an explicit repository revision.

A *local* generated collection is still **PRIVATE_NOT_PUBLISHED** and does not prove authorization. The collection script will not push Git or publish the separate Wiki repository.

## Publication is a separate authorized step

1. Independently verify canonical identity/integrity, C1/C2/C3 permissions, SemantiK RuntimeSet release and disclosure/linguistic review.
2. Review the exact Markdown pages and any sensitive rendered prose/links.
3. Enable and initialize the target GitHub Wiki if necessary.
4. Explicitly push **only the approved pages** to `Rejean-McCormick/kristal-public.wiki.git`; the Spek documentation Wiki is a different repository.
5. Check the actual GitHub Wiki URL and the pinned public revision; do not treat an offline Markdown draft as a live site.

See [[Publishing the Wiki]], [[Epistemic and Security Boundaries]] and [[Kristal Wiki Architecture]].
