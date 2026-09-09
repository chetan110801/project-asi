# PROJECT ASI

A long-term, self-improving system for understanding **intelligence** — human, machine, and beyond — and what would *really* be required to build AGI (Artificial General Intelligence) and ASI (Artificial Superintelligence).

This is not a single document. It is a **living system** that builds and improves its own roadmap over time. It may run for years.

> **Just here to learn/build?** Open **[`START_HERE.md`](START_HERE.md)** — that's all you need. The rest of this README documents the machinery (hidden from the IDE by default).

---

## The one-sentence idea

> Don't just build a roadmap. Build the **machine that builds and improves the roadmap** — and keep improving the machine.

---

## How this repository is organized

```
project-asi/
├── START_HERE.md              ← the learner's only entry point
├── approaches-to-agi.html     ← the built offline reader (open this to read) — `py -3 build_site.py`
├── build_site.py              ← builds approaches-to-agi.html from LEARNING/**/*.md
├── README.md                  ← this technical map (hidden from IDE by default)
├── AI_ONBOARDING.md           ← how a future AI tool should read this repo + its git history
├── .vscode/settings.json      ← hides the machinery folders from the IDE Explorer
│
├── INSTRUCTIONS/              ← the "operating system" of the project
│   ├── HARD_RULES.md                  ← ⭐ the live, binding standard (durability filter, live-SOTA
│   │                                     freshness pass, language rules, the final gate)
│   ├── MASTER_INSTRUCTION.md          ← the constitution.
│   ├── PRINCIPLES.md                  ← how we think (values + rules of reasoning)
│   ├── RESEARCH_METHOD.md             ← how we investigate questions
│   ├── LEARNING_METHOD.md             ← how YOU actually learn and remember
│   ├── DOMAIN_DISCOVERY_SYSTEM.md     ← how we find fields we didn't know we needed
│   ├── RESOURCE_COLLECTION_SYSTEM.md  ← how we choose what to read/watch
│   ├── KNOWLEDGE_PROCESSING_SYSTEM.md ← how we turn resources into understanding
│   ├── LEARNER_STRATEGY.md            ← the "direct & decide, don't implement-grind" learning strategy
│   ├── LEARNING_ARCHITECTURE.md       ← no-repeat ladder + dynamic insertion + change-tracking + freshness checklist
│   ├── BUILD_SYSTEM.md                ← the build engine (toward AGI/ASI)
│   ├── IDEA_EVALUATION_SYSTEM.md      ← how I judge ideas for feasibility before building
│   ├── MILESTONE_AND_SHOWCASE_SYSTEM.md ← dynamic practical goals + showable artifacts
│   ├── AGI_ASI_INVESTIGATION_SYSTEM.md← the actual map of paths to AGI/ASI
│   ├── OPEN_QUESTIONS_SYSTEM.md       ← the questions driving the whole project
│   ├── SELF_IMPROVEMENT_SYSTEM.md     ← how the system upgrades itself
│   ├── QUALITY_CONTROL_SYSTEM.md      ← how we catch our own mistakes
│   ├── VERSION_HISTORY.md             ← what changed, when, and why (human-readable evolution log)
│   └── GLOSSARY.md                    ← plain-language definitions of hard words
│
├── LEARNING/                 ← Part 1: the product — the investigation, as one readable book
│   ├── APPROACHES_TO_AGI.md       ← ⭐ THE SPINE. The eleven real bets on how to reach AGI.
│   ├── THE_PLAN.md                ← ⭐ the forward page: how to go from reading about AGI to working on it
│   ├── CONCEPT_REGISTRY.md        ← one home per concept (the no-repeat enforcer)
│   ├── WHATS_NEW.md               ← the change log for the learner
│   ├── 10-how-ai-works-today/     ← the shared base everything else builds on (2 pages)
│   ├── 20-the-approaches/         ← AP1–AP11, one page per bet (11 pages)
│   ├── 30-across-the-approaches/  ← threads running across all bets: the bounds; alignment (2 pages)
│   ├── 40-the-verdict/            ← the capstone: which bets actually get to AGI (1 page)
│   ├── 50-deep-dives/             ← optional side-branches, one level past a card (16 pages)
│   └── _legacy/                   ← the pre-v3.0 learn-first curriculum (kept, not maintained)
│
├── RESOURCES/                 ← Part 3: the catalog we gather into
│   ├── INDEX.md                   ← curated, validated resources BY DOMAIN (mostly free)
│   ├── PAPERS.md                  ← research papers (landmark→SOTA) + lab hubs + blogs + explainers
│   ├── LANDSCAPE.md               ← who's pursuing AGI/ASI and via which bets (labs, startups, paths)
│   ├── REQUESTS.md                ← prioritized acquisition list (paid books to obtain)
│   ├── corpus/                    ← (local, git-ignored) ~52k chunked .txt source files — the
│   │                                 grounding substrate modules are written FROM, not from memory
│   └── library/                   ← (local, git-ignored) where you drop purchased PDFs/EPUBs
│
├── REVIEWS/                   ← Part 4: self-critiques / audits (drive version upgrades)
│   ├── AUDIT_2026-06-20_v1.0.md
│   └── AUDIT_2026-07-21_v3.0.md   ← the cold read that produced THE_PLAN.md
│
└── (folders created later as the work grows)
    ├── BUILDS/       ← Part 2: code/experiments (created on the first build)
    ├── DOMAINS/      ← deep-dive folders per field, when needed
    ├── MAPS/         ← diagrams of how things connect (dependencies, bottlenecks)
    ├── ROADMAP/      ← the current best-guess path, always revisable
    └── SHOWCASE/     ← the growing shelf of artifacts proving real progress
```

> The folders in the last block don't exist yet. They are created the first time
> we actually do that kind of work, so the repo never fills up with empty shells.
> The whole project is tracked in **git** — see [`AI_ONBOARDING.md`](AI_ONBOARDING.md)
> for how to read the history end-to-end.

---

## How to use this project

- **Just want the big picture?** Read [`INSTRUCTIONS/MASTER_INSTRUCTION.md`](INSTRUCTIONS/MASTER_INSTRUCTION.md).
- **Want to read the investigation?** Open [`approaches-to-agi.html`](approaches-to-agi.html), or start at [`LEARNING/APPROACHES_TO_AGI.md`](LEARNING/APPROACHES_TO_AGI.md).
- **Want to know what happens next?** Read [`LEARNING/THE_PLAN.md`](LEARNING/THE_PLAN.md).
- **Want the rules the writing obeys?** See [`INSTRUCTIONS/HARD_RULES.md`](INSTRUCTIONS/HARD_RULES.md).
- **Hit a confusing word?** Check [`INSTRUCTIONS/GLOSSARY.md`](INSTRUCTIONS/GLOSSARY.md).

---

## The promise of this system (the "house rules")

1. **Truth over comfort.** We want what is *real*, not what is popular, hyped, or flattering.
2. **Simple words, deep ideas.** Language is kept easy. The thinking is kept expert-level.
3. **Nothing is final.** Every document can be challenged, versioned, and improved.
4. **Show the reasoning.** Claims come with evidence, uncertainty, and alternative views.
5. **Always ask "what are we missing?"** Incompleteness is assumed, not feared.

---

*Status: Living system · Version 3.0 (the investigation-first re-root) · Last updated: 2026-09-09*
