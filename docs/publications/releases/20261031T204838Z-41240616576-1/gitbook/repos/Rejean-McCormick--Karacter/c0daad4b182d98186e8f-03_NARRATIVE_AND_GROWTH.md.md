<!-- Frozen source: https://github.com/Rejean-McCormick/Karacter/blob/c50db0afda429e4be45e41f67658061e49e9282f/docs/domain/03_NARRATIVE_AND_GROWTH.md | commit: c50db0afda429e4be45e41f67658061e49e9282f | SHA-256: d29ea7717008f8ecc50ff184be8359bc5aa5a168c91dcbe729b64f19794dd25f -->

# Narrative identity, conflict and growth

A compelling fictional character has more than numerical tendencies. The story layer explains **why decisions matter** and how a character can evolve without forcing the base personality to change.

## Core fields and author guidance

| Field | Meaning | King Klown reference |
|---|---|---|
| `desire` | Conscious external goal | Preserve the community's freedom |
| `need` | Inner truth, often less acknowledged | Learn to trust others' agency |
| `values` | Principles guiding difficult choices | Freedom, collective well-being, wonder |
| `fear` | Perceived threat to security/identity | Tyranny of rigid order or meaningless chaos |
| `limitingBelief` | Assumption shaping a coping strategy | Only hidden guidance can keep others safe |
| `contradiction` | Clash between aims/values/means | Protects autonomy while steering choices |
| `turningPoint` | Event that forces a difficult decision | Someone discovers he manipulated a choice |
| `possibleGrowth` | Plausible earned change | Become transparent while remaining playful |

**Writing principle:** Avoid generic labels alone, e.g. "wise and mysterious". The character has a story when their strategies and values can clash.

## Growth timeline

A `Milestone` records:

- `title`, `order`, optional fictional/story date and narrative context;
- what happened (`event`), what the character believed before and after, behavior they chose;
- relationships affected, lessons learned or rejected;
- optional `axisObservations[]` (how they acted in that specific scene), not automatic changes to their baseline axes.

**Critical distinction:** `observedBehavior` is contextual; it MUST NOT automatically rewrite `character.polarities`. User can explicitly choose "Apply as new baseline" with before/after preview, creating a reversible versioned edit.

## Character state versions

- Baseline version 1 is retained in character history on explicit major edits.
- Milestones belong to a chronological narrative timeline; they are not medical or psychological history.
- A character can have alternative imagined arcs; v6 P0 can use a single canonical milestone sequence; branching arcs are P2.
- Undoing/reordering milestones must not remove unrelated artwork or relationships.

## Prompt interaction

Portrait prompts are based primarily on appearance identity and select visible tendencies; a milestone influences the prompt only if user explicitly chooses a period/state. **No silent updates** to existing art from a narrative change.

## Evaluation heuristic for writing quality

Every new character should be able to answer:

1. What do they pursue?
2. What are they afraid of losing?
3. What strategy do they repeatedly use?
4. How could that strategy cause harm despite good intentions?
5. Which decision would test their beliefs?
6. What could they learn or choose not to learn?

These are author prompts, never mandatory psychological claims.
