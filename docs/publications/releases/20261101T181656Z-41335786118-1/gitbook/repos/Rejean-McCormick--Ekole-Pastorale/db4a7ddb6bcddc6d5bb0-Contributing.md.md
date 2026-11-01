<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Contributing | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: ede4fcfccd3fe00f6c54f36213cc52d95c6da2561ab14c4dcbad06731c6ba070 -->

# Contributing

Thank you for contributing to the Ekole Pastorale prototype. This is a Catholic education content project built on reusable Kristals, not a fork of Ekole Core.

## Scope of a contribution

Contributions may cover teaching design, biblical or historical references, witness documentation, accessibility, safeguarding, test coverage, projection tooling, and English-language developer documentation.

Keep responsibility with the right repository:

- **Ekole Core:** general-purpose learner/teacher engine, no Catholic-specific logic.
- **Ekole Pastorale:** Catholic curriculum, teaching configuration, and generated content pack.
- **Kristal sources:** canonical semantic and educational content; generated Ekole files are derived.
- **Historical Catho corpus:** source ownership and identity migration need separate review.

## Proposed change workflow

1. Open a concise issue or design note explaining the purpose, affected units, and source references.
2. Edit canonical Kristal data rather than generated JSON where possible.
3. Identify whether the change touches Scripture, doctrine, historic attribution, privacy, or minors.
4. Add evidence and request the appropriate editorial review; do not conflate a saint's biography with Church doctrine.
5. Run the Framework checks, build the relevant state, regenerate derived views, and run tests.
6. Confirm that the change preserves the two-branch prerequisite invariant and teacher/learner privacy boundaries.
7. Submit a reviewable change set with a summary of sources, tests, and known limitations.

## Local checks

```bash
python3 -m unittest discover -s tests -v
python3 demarrer_pastorale.py --verifier
```

After a canonical edit, see [Authoring and Projection](Authoring-and-Projection.md) for the required build order.

## Contributions do not imply publication approval

A merged pull request is not an ecclesiastical endorsement and does not itself authorize public distribution. The prototype's `publication_autorisee` flags must remain false until a competent decision is documented.

## Licensing

The supplied repository snapshot does **not** include a top-level license. Contributors and maintainers should establish an explicit license and confirm third-party rights before inviting broader reuse or redistribution. Do not assume that Scripture translations, photographs, or historical editions can be copied without permission.

## Wiki maintenance

Edit Markdown pages in `wiki/` and verify the internal links. The GitHub Wiki is a **separate Git repository** and must be updated separately unless the maintainers automate synchronization. See [Publishing the GitHub Wiki](Publishing-the-GitHub-Wiki.md).
