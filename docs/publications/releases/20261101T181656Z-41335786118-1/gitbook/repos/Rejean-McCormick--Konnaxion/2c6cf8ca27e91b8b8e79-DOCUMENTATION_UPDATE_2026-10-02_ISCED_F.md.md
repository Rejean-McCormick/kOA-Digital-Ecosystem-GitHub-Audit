<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/blob/59601fb9cd74fb8f9d8037ed97a0441f285242a1/docs/DOCUMENTATION_UPDATE_2026-10-02_ISCED_F.md | commit: 59601fb9cd74fb8f9d8037ed97a0441f285242a1 | SHA-256: e889e6c4a6b10d3ec9cc951fa5f1c207db0fac5de45560bc353fc444eaf6e60c -->

# Documentation update — EkoH / ISCED-F 2013

**Date:** 2026-10-02

This pass aligns the Konnaxion documentation and wiki with the current EkoH expertise taxonomy contract.

## Canonical correction

- Replaces the misleading phrase **“26 ISO-based domains”**.
- Declares **UNESCO ISCED-F 2013 / CITE-F 2013** as the external taxonomy backbone.
- Distinguishes the complete ISCED-F classification (**11 broad / 29 narrow / about 80 detailed**) from the EkoH domain-bearing profile (**10 broad / 26 narrow / 77 detailed = 113 categories**).
- Documents `ExpertiseCategory.code`, `parent`, `depth` and `path`.
- Documents `python manage.py load_isced` as the synchronization command.
- Pins EkoH explicitly to ISCED-F 2013 pending an explicit future migration/crosswalk.
- Clarifies that taxonomy identifiers are not credentials, expertise scores or universal voting weights.

## New reference

`Technical-Reference/EkoH Smart Vote/EkoH - Expertise Taxonomy (ISCED-F 2013).md`

## Historical documents

Older EkoH/Smart Vote documents that called themselves “canonical” or used obsolete taxonomy counts are retained as historical material but now carry an explicit supersession/taxonomy notice.
