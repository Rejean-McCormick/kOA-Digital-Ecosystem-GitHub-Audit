<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Arketypes-ARK-20-and-ARK-21 | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: 1fd48c22d3dcfe6917f7728cde992577500ef63c054a2c4605a148c602a5a571 -->

# Arketypes: ARK-20 and ARK-21

`extension-arketype/` provides **two candidate** profiles for Arketype 1.5. They are intended to be reusable beyond Catholic education: the vocabulary of a specific Catholic school belongs to that school's content and configuration, not to a universal engine or template.

## ARK-20 — Federated Learning Unit

**Model slug:** `unite-formation-federee`

ARK-20 models the *educational unit*, including:

- instructional goals and time allocation;
- prerequisites and membership in a teaching branch;
- source references and provenance expectations;
- session progression and activities;
- observable work products and assessment criteria;
- teacher versus learner output boundaries;
- pastoral safeguarding requirements in this content specialization.

The `pastorale.unite-native/1.1-draft` schema in `contracts/` is an **experimental school-specific editorial contract**, not an upstream Kristal Framework rule.

## ARK-21 — Witness, Virtues, and Sources

**Model slug:** `temoin-vertus-sources`

ARK-21 supports biographies and other witness records that cannot be reduced to their authored texts alone. For a saint, it distinguishes:

- verified or attributed writings;
- documented events and actions;
- virtues and their historical evidence;
- later biographies and hagiographical traditions;
- extraordinary events and attributed miracles, kept in a separate evidentiary category.

The initial instance is `kristals-temoins/francois-assise/` (Francis of Assisi). Its witness record is **independent** of the course `EPC-MSG-012`. The demonstration dossier deliberately does **not** assert that it has certified any miraculous claim.

The `pastorale.temoin-native/0.1-draft` schema is likewise **experimental**.

## Creating templates versus filling them

Arketype templates are intentionally **empty** of canonical entities: creating a template must not invent global KQ/KP/KA/KS identifiers, doctrinal assertions, or source evidence.

The extension package contains:

```text
extension-arketype/
├── installer_deux_archetypes.py
├── installer_extension.py                 # Legacy ARK-20-only installer
└── overlay/
    ├── archetypes/                        # Candidate type definitions
    └── modeles/                           # Empty v11-ready templates
```

## Try the extension in a controlled Arketype checkout

Do not install directly into your only working copy of Arketype without a backup or a version-control checkpoint.

```bash
python3 extension-arketype/installer_deux_archetypes.py   --arketype /path/to/arketype --dry-run

python3 extension-arketype/installer_deux_archetypes.py   --arketype /path/to/arketype

python3 /path/to/arketype/arketype.py show temoin-vertus-sources

python3 /path/to/arketype/arketype.py create   --type temoin-vertus-sources   --slug witness-demo   --title "Witness Demo"   --parent /path/to/existing/parent   --authoring v11
```

The parent path must exist. `installer_extension.py` is retained for compatibility but installs only ARK-20. The extension installer does not repair unrelated validation failures in an older Arketype snapshot.

## What these profiles do not do

- They do **not** modify Ekole Core.
- They do **not** turn Catholic terminology into a Core requirement.
- They do **not** migrate the historic Catho corpus automatically.
- They do **not** grant ecclesiastical publication or doctrinal approval.

Related: [Architecture](Architecture.md), [Kristal Framework v11](Kristal-Framework-v11.md), and [Catho Reference Integration](Catho-Reference-Integration.md).
