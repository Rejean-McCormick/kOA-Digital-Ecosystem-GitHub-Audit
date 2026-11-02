<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Governance-and-Safeguarding | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: d80d15206c826a0f1748d64a6493c822e4da1f7866505c5a3f77c975e467dfa6 -->

# Governance and Safeguarding

This repository is Catholic in editorial identity but currently remains an **unapproved local educational prototype**. Technical generation and successful testing must not be presented as ecclesiastical approval.

## Independent reviews before release

1. **Scriptural and historical accuracy:** references, sources, genre and translation rights.
2. **Catholic doctrine:** dogma, magisterial teaching, theological opinion, and contemporary applications clearly distinguished.
3. **Pedagogical quality:** learning goals, age appropriateness, lesson activities, assessment fairness, and accessibility.
4. **Safeguarding:** protection of minors and vulnerable people; trauma-informed, non-coercive practice.
5. **Copyright and privacy:** images, quotations, licensed texts, personal data, consent, and retention.
6. **Ecclesiastical authority:** competent approval if an official Church association, mandate, or recognition is sought.

The prototype currently has no recorded approval satisfying these requirements. Do not set publication flags to true merely to make an interface appear production-ready.

## Pastoral safety boundaries

- **Abuse and violence:** protect the person first; follow applicable reporting obligations and refer to qualified professionals. Never make forgiveness or reconciliation a prerequisite for safety.
- **Illness and healing:** never discourage medical care, promise miraculous recovery, or blame illness on weak faith.
- **Spiritual pressure:** respect conscience, privacy, and the right not to share beliefs or personal experiences.
- **Poverty:** distinguish voluntary spiritual simplicity from structural deprivation and involuntary poverty.
- **Indigenous communities and New France history:** contextualize missionary and colonial histories; represent affected communities fairly, with appropriate sources.
- **Private revelations and attributed miracles:** document actual ecclesial status and separate devotional claims from definitive Church teaching.

## Confidentiality

Use fictional cases for classroom exercises involving trauma or spiritual direction. Personal counseling files, contact lists, and private spiritual journals must not be added to curriculum Kristals or learner projections. In Quebec, instructors must understand the applicable limits to confidentiality and reporting.

## Separation of teacher and learner material

The current projection generates teacher-oriented `cours/` files and separate learner-oriented `publications/eleve/` files. Learner exports omit internal teacher guidance and safeguards. This separation reduces exposure but does not replace privacy review or security testing.

## Publication decision

Recommended release sequence:

**Propose → source review → doctrine review → safeguarding review → pedagogical review → rights review → ecclesial approval when applicable → signed publication decision → regenerate → test learner UI.**

A successful `build-v9`, `projeter_ekole.py`, or `--verifier` step fulfills only a technical part of this process.

Related: [Editorial Principles](Editorial-Principles.md) and [Contributing](Contributing.md).
