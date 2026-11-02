<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Publishing-the-Wiki | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 8bb523b3a0cde227beae4f50d112785bb4c477f63b385094f1efc47b46c19ef4 -->

# Publishing the Wiki

**Important:** This page documents two different targets. Neither a ZIP update nor a local Spek compilation performs a GitHub push.

## A. Spek software documentation Wiki (this Wiki)

Its editable source is in the **Spek main repository** under `wiki/*.md`; GitHub serves the live Wiki from the separate `OWNER/Spek.wiki.git` repository. To publish documentation changes:

1. Review the proposed Markdown diffs in a local Spek checkout.
2. Enable **Wikis** for the Spek repository if not already enabled.
3. Create a `Home` page using the GitHub Wiki UI if the Wiki Git repository does not exist.
4. Update the source `wiki/` pages in the main repository.
5. Use the existing sync script first **without** `--push` to inspect the local diff, then with `--push` only after review.

```bash
./scripts/sync-wiki.sh OWNER/Spek
./scripts/sync-wiki.sh OWNER/Spek --push
```

Do **not** extract an archived `.git/` directory over an existing local clone: it can overwrite branch metadata or the origin remote. The updated documentation ZIP intentionally excludes `.git/`.

## B. Kristal knowledge Wiki (distinct repository)

The public Kristal knowledge Wiki is intended for `Rejean-McCormick/kristal-public.wiki.git`, **not** Spek's documentation Wiki. Its Markdown pages are built from approved Kristal semantic projections via **SemantiK Architect and Spek's optional Arketype Wiki overlay**.

A Wiki draft is not a publication: it must be reviewed, C1/C2/C3 gates must pass, and the target repository Wiki must be enabled/initialized before an authorized Git push. The current overlay deliberately does **not** automate that final push.

See [[Wiki Draft Workflow]] and [[Epistemic and Security Boundaries]].

GitHub documentation: <https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages>.
