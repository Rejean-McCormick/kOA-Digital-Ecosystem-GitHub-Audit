# Kristal — local repository source

The kOA dashboard can read the semantic catalogs from the local **Kristal kOA Ecosystem** repository without exporting them to GitHub Pages.

Default folder on Windows:

```text
C:\mycode\Kristal\locals\Kristal-kOA-Ecosystem
```

In **Écosystème**, verify or browse to the folder, click **Vérifier Kristal**, then open the center of operations. The **Kristal canonique · 49 dépôts** map reconciles exact GitHub repository identities with the official 49-repository audit inventory. Choose a repository, then the **Kristal (local)** detail tab for its canonical description, explicitly mapped components and sourced/claimed semantic relations.

The reader loads only these canonical editorial catalogs:

- `knowledge-base/sources/repositories.json`
- `knowledge-base/sources/components.json`
- `knowledge-base/sources/relations.json`

Kristal may contain more repositories and components than the audit's bounded 49-repository inventory; these sets are intentionally not merged. Semantic relationships are not evidence of integration tests or production certification. Missing component links are simply missing mappings, not quality defects. Data refresh is read-only and requires no scan, credential or GitHub request.

The local API route is `/api/kristal/atlas`. It is served only by the Windows preview on loopback and returns allowlisted semantic information. The site published to GitHub Pages keeps its static curated map and cannot read your computer's local folder.
