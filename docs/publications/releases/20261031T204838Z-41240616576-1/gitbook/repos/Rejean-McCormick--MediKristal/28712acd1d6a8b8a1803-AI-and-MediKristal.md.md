<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/AI-and-MediKristal | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: ec5ce025553c9fd99ae49da218cff82431b024b869c85ded0a231d6635c93a15 -->

# AI and MediKristal

MediKristal is **not an AI system**. It is a governed medical knowledge system that AI can consult.

## Why this matters

A large language model can be excellent at:

- understanding a natural-language question;
- extracting candidate entities;
- comparing documents;
- summarizing evidence;
- generating an explanation;
- helping a reviewer navigate a complex corpus.

But none of those capabilities should silently create medical authority.

## Desired architecture

```text
User question
    ↓
AI or conventional interface
    ↓
structured MediKristal query
    ↓
versioned governed medical knowledge
    ↓
protocol / evidence / provenance result
    ↓
AI may explain the result
```

The AI is a **reader, interface, and optional reasoning assistant**. It is not the owner of the corpus.

## Retrieval instead of memorized authority

A central purpose of MediKristal is to let AI systems retrieve formalized medical knowledge instead of depending exclusively on statistical memory learned from uncontrolled text corpora.

The desired pattern is:

```text
Structured substance → Optional AI
```

not:

```text
Unstructured documents → AI reconstructs the medical truth every time
```

## Potential AI roles

AI can assist with:

- natural-language querying;
- semantic search;
- candidate terminology mappings;
- extraction of candidate assertions from publications;
- comparing guideline versions;
- summarizing evidence for reviewers;
- explaining graph paths;
- identifying conflicts or missing mappings;
- multilingual interaction when allowed by policy.

A tool such as [SenTient](https://github.com/Rejean-McCormick/SenTient) can help reconcile unstructured material into **candidate knowledge**, which remains subject to review.

## What AI cannot silently do

AI should not silently:

- create promoted medical knowledge;
- approve its own mapping;
- erase conflicting evidence;
- rewrite provenance;
- transform terminology into a treatment rule;
- alter historical knowledge states;
- hide the protocol or source behind an answer.

## Fail visibly

When the governed corpus does not support an answer, the system should be able to return:

```text
unknown
insufficient evidence
conflicting evidence
outside validated scope
unsupported language realization
```

These are valid results.

## AI and Smart Vote

AI may summarize arguments or help professionals inspect evidence, but it is not a certified medical expert and does not receive professional voting authority merely because it can generate fluent text.
