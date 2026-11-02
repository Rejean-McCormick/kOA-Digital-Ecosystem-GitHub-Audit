<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/EkoH | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 5c554c1cff28a0710d78c01f15c641f6b8882060715197d899f67554f4e4d409 -->

# EkoH — Expertise, Ethics and Rating Access

EkoH is a Konnaxion **domain/service boundary**, not a global reputation authority and not a voting engine.

Canonical backend:

```text
backend/konnaxion/ekoh/
```

## Current data model

- `ExpertiseCategory` — hierarchical expertise taxonomy;
- `UserExpertiseScore` — user/domain expertise score;
- `UserEthicsScore` — governed ethics/reliability context;
- `ScoreConfiguration` — scoring configuration;
- `ScoreHistory` — score-change trace;
- `ConfidentialitySetting` — identity privacy;
- `RatingVisibilitySetting` — rating visibility policy;
- `RatingAccessScope` — hierarchical disclosure scope;
- `RatingScopeSubject` — subject membership in a scope;
- `RatingAccessGrant` — viewer grant;
- `ContextAnalysisLog` — contextual analysis record.

## Canonical expertise taxonomy

EkoH uses **UNESCO ISCED-F 2013 / CITE-F 2013** as its external domain hierarchy. The full classification contains 11 broad / 29 narrow / about 80 detailed fields; the default EkoH expertise-bearing profile contains **10 broad (`01`–`10`) / 26 substantive narrow / 77 substantive detailed = 113 categories**.

The taxonomy is hierarchical (`code`, `parent`, `depth`, `path`) and version-pinned. An ISCED-F category identifies a domain; it does not by itself prove expertise or create voting influence. See [[EkoH Expertise Taxonomy|EkoH-Expertise-Taxonomy]].

## Expertise semantics

Expertise is **domain-bounded**. A high score in one category is not universal authority in another category.

The multidimensional scoring path normalizes evidence axes and stores bounded domain scores. Lack of expertise is neutral rather than negative merit.

## Context analysis

The current contextual-analysis path is deliberately **non-authoritative**: analysis can be recorded without silently modifying `UserExpertiseScore`.

## Privacy and disclosure

Rating visibility is decided server-side. The current access resolver applies a deterministic order including self, staff, scoped grants, public policy and deny behavior.

Identity confidentiality and rating visibility are separate policies.

## Smart Vote relationship

```text
EkoH context
    ↓
explicit consultation/lens context
    ↓
Smart Vote reading
```

EkoH may influence a declared advisory reading. It does not own the source vote/stance and does not assign a universal personal voting power.

## K-Port

K-Port is an **EkoH evidence application/gateway**. It can normalize/qualify evidence entering the EkoH boundary; it is not a peer system of Konnaxion and does not own EkoH scores.
