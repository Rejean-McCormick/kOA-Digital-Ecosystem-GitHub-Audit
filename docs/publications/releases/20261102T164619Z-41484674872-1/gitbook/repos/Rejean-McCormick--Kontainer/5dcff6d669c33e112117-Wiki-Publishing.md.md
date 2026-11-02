<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Wiki-Publishing | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 6a4baad90970242cb389f074df1b2d9a67f1e90535c76f46672c70b66d4b4083 -->

# Publishing this Wiki

These pages are **GitHub Wiki-ready Markdown**, but no remote repository has been changed by their creation. To publish them:

1. Create or enable **Wiki** on the intended GitHub repository (where available).
2. Clone that repository's `.wiki.git` URL using your normal GitHub authentication.
3. Copy all `.md` files from this bundle into the root of the wiki checkout.
4. Review titles, ownership, and any repository naming choices. The software delivered in the source archive remains **Kristal-Container 1.0.0rc1** with module `kristal_container`.
5. Commit and push through the repository's normal review and permission process.

```bash
# Replace ORG/REPO with the actual owner and repository
# git clone https://github.com/ORG/REPO.wiki.git
# cp /path/to/Kontainer-GitHub-Wiki/*.md REPO.wiki/
# cd REPO.wiki
# git add . && git commit -m "Add Kontainer English wiki" && git push
```

The repository's source documentation and its `docs/FORMAT.md` remain the implementation-level reference. Adapt any branding, links, policies, licensing, and release status as the project evolves; do not turn unsupported capability statements into assurances.
