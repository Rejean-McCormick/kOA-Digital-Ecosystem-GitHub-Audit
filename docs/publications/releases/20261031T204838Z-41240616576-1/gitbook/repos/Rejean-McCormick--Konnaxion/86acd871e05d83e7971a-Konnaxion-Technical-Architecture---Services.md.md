<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Konnaxion-Technical-Architecture-%26-Services | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: bf29bc888b40e2000aaf3ba3449f4d3b00c371d7290ba40febf889c9330291d0 -->

# Konnaxion – Technical Architecture & Services

## 1. System identity

Konnaxion is a shared full-stack ecosystem system/platform.

Current implementation stack:

- Next.js + React + TypeScript frontend;
- Django + Django REST Framework backend;
- PostgreSQL;
- Celery + Redis for asynchronous execution;
- OpenAPI/drf-spectacular for API description.

## 2. Responsibility map

```text
Konnaxion
│
├── shared platform
│   ├── users/auth
│   ├── moderation/audit
│   ├── navigation/search
│   └── shared frontend/runtime infrastructure
│
├── ethiKos civic domain
│   ├── Korum
│   └── Konsultations
│
├── contextual intelligence
│   ├── EkoH
│   └── Smart Vote
│
├── keenKonnect
├── KonnectED
├── Kreative
├── TeamBuilder
├── Kontrol
├── Konsensus UI
└── Reports / Insights
```

Logical responsibility does not require a separate Django app for every named product area.

## 3. Global invariants

1. One authoritative owner per state.
2. No direct cross-domain database write as an integration mechanism.
3. Source facts and derived readings remain distinct.
4. EkoH context does not become a civic vote.
5. Smart Vote does not silently replace the baseline.
6. UI/reporting does not acquire ownership of the data it presents.
7. External ecosystem systems integrate through explicit contracts.

## 4. ethiKos / Korum

Canonical backend package:

```text
backend/konnaxion/ethikos/
```

Implemented source objects include:

- `EthikosCategory`;
- `EthikosTopic`;
- `EthikosStance`;
- `EthikosArgument`;
- `ArgumentSource`;
- `ArgumentImpactVote`;
- `ArgumentSuggestion`;
- `DiscussionParticipantRole`;
- `DiscussionVisibilitySetting`.

Korum is the logical structured-deliberation capability over these ethiKos-owned records.

## 5. EkoH

Canonical backend package:

```text
backend/konnaxion/ekoh/
```

Implemented state includes:

- `ExpertiseCategory`;
- `UserExpertiseScore`;
- `UserEthicsScore`;
- `ScoreConfiguration`;
- `ScoreHistory`;
- `ConfidentialitySetting`;
- `RatingVisibilitySetting`;
- `RatingAccessScope`;
- `RatingScopeSubject`;
- `RatingAccessGrant`;
- `ContextAnalysisLog`.

EkoH expertise is domain-bounded. Its contextual-analysis service records non-authoritative analysis rather than silently mutating expertise scores. Rating disclosure is resolved server-side by the EkoH rating-access service.

The canonical expertise taxonomy is **UNESCO ISCED-F 2013 / CITE-F 2013**. EkoH uses a version-pinned domain-bearing profile of **10 broad / 26 narrow / 77 detailed = 113 categories**; see [[EkoH Expertise Taxonomy|EkoH-Expertise-Taxonomy]].

## 6. Smart Vote

Canonical backend package:

```text
backend/konnaxion/smart_vote/
```

Important current objects:

- `Consultation`;
- `ConsultationRelevance`;
- `SourceConsultationBinding`;
- `VoteModality`;
- `Vote`;
- `VoteResult`;
- `VoteLedger`.

Current API entry points:

```text
POST /api/v1/smart-vote/cast/
GET  /api/v1/smart-vote/readings/ethikos-topic/<topic_id>/
```

The ethiKos reading path is the canonical architecture pattern to preserve:

```text
EthikosTopic / EthikosStance
        ↓ read only
SourceConsultationBinding
        ↓
ConsultationRelevance + EkoH context
        ↓
Smart Vote reading
        ↓
baseline + advisory reading
```

## 7. keenKonnect

Canonical backend package:

```text
backend/konnaxion/keenkonnect/
```

Current model families:

- `Project`;
- `ProjectResource`;
- `ProjectMessage`;
- `ProjectTask`;
- `ProjectTeam`;
- `ProjectRating`;
- `Tag`.

## 8. KonnectED

Canonical backend package:

```text
backend/konnaxion/konnected/
```

Current model families include certification paths/evaluations, peer validation, portfolio/interoperability, knowledge resources/recommendations, learning progress, offline packages, mentorship, co-creation and forums.

## 9. Kreative

Canonical backend package:

```text
backend/konnaxion/kreative/
```

Current model families include artworks, galleries, collaboration sessions, traditions, virtual exhibitions, digital archives/documents, AI catalogue entries and cultural partners.

## 10. TeamBuilder

Canonical backend package:

```text
backend/konnaxion/teambuilder/
```

Current core state:

- `Problem`;
- `ProblemChangeEvent`;
- `BuilderSession`;
- `Team`;
- `TeamMember`.

## 11. Kontrol

Canonical backend package:

```text
backend/konnaxion/kontrol/
```

Current state includes `AuditLog`, `ModerationTicket` and `KonsensusConfig`, plus administrative/reporting views.

## 12. Frontend route families

Current App Router families include:

```text
/ethikos/*
/ekoh/*
/keenkonnect/*
/konnected/*
/kreative/*
/konsensus/*
/kontrol/*
/reports/*
/teambuilder/*
/search
```

A route is a presentation surface, not an ownership declaration.

## 13. External boundaries

### Orgo

No active adapter is present in the current snapshot. Future integration must use command/query/event/artifact/receipt semantics. `Orgo Case ≠ EthikosTopic` and `Orgo Task ≠ Konnaxion consultation`.

### Kristal

No active adapter is present. If Konnaxion consumes Kristal artifacts, it must preserve Kristal epistemic semantics and must not take ownership of kOA-Linux local Runtime Pack activation.

### SemantiK Architect

No active adapter is present. A future integration is a generation/presentation boundary; Architect does not own Konnaxion source state.

### kOA-Linux

When Konnaxion is deployed under kOA-Linux, kOA-Linux owns host/platform responsibilities while Konnaxion retains domain authority.
