# VERSION HISTORY
**What changed, when, and why.** The memory of the project. Nothing is final; everything here shows *how the thinking evolved*. We never silently overwrite the past.

`Part of: PROJECT ASI — Living Instruction System`
`Status: Living document · Last updated: 2026-06-20`

---

## How to read this

- **Major version (1.0 → 2.0):** a big rethink of how the system works.
- **Minor version (1.0 → 1.1):** improvements, fixes, added documents.
- Each entry records: **what changed**, **why**, **expected benefit**, **trade-offs**.

---

## v1.0 — 2026-06-20 — *Initial system*

**What changed:** Created the founding `INSTRUCTIONS/` operating system: `MASTER_INSTRUCTION`, `PRINCIPLES`, `RESEARCH_METHOD`, `LEARNING_METHOD`, `DOMAIN_DISCOVERY_SYSTEM`, `RESOURCE_COLLECTION_SYSTEM`, `KNOWLEDGE_PROCESSING_SYSTEM`, `AGI_ASI_INVESTIGATION_SYSTEM`, `OPEN_QUESTIONS_SYSTEM`, `SELF_IMPROVEMENT_SYSTEM`, `QUALITY_CONTROL_SYSTEM`, `GLOSSARY`, plus root `README`.

**Why:** To establish the "machine that builds the roadmap" before building any roadmap — a living, self-improving research and learning system about intelligence, AGI, and ASI.

**Expected benefit:** A consistent, rigorous, simple-language framework that can grow for years.

**Trade-offs:** A first draft. Built in good faith but unaudited — known to contain blind spots (that's expected and is the point of v1.1).

---

## v1.1 — 2026-06-20 — *First audit + Milestone & Showcase system*

**What changed (summary — see [`../REVIEWS/AUDIT_2026-06-20_v1.0.md`](../REVIEWS/AUDIT_2026-06-20_v1.0.md) for the full audit):**

1. **Added `MILESTONE_AND_SHOWCASE_SYSTEM.md`** *(new file)* — *dynamic*, achievable, practical intermediate goals ("checkpoints"), each ending in a **showable artifact** (not only code — an explainer, a map, a toy build, a prediction, a teach-back). Includes a **mastery ladder (L0–L4)**, a **bias-to-action / momentum rule**, a **Prediction Ledger**, **system-health signals**, and a **North-Star (decision-relevance) anchor**. Directly fixes the audit's top finding: the "build endless structure, produce nothing concrete" failure mode and the absence of visible progress.
2. **Honesty correction (caught by running our own quality control on the audit):** the first draft of the audit *overclaimed* — it called predictions, AI-failure checks, and ~9 domains "missing" when v1.0 already had them. Corrected. The accurate v1.1 deltas are therefore narrower and listed below.
3. **Domain map:** added the two **genuinely absent** fields — **decision theory & epistemics** and **data economics** — to `DOMAIN_DISCOVERY_SYSTEM.md`, and added the **"listed ≠ engaged" discipline** (a named-but-never-studied field is a blind spot in disguise; the map is a work queue, not a trophy).
4. **Prediction Ledger** (in the new milestone doc) — v1.0 already *required* falsifiable predictions but had **nowhere to record and resolve them**; the ledger closes that loop so reality can correct us.
5. **System-health signals** — v1.0 had no way to tell improvement from mere motion; added lightweight signals (artifacts shipped, depth reached, questions sharpening, predictions resolving, new domains entered, last time we were wrong).
6. **Master instruction:** added house rule #6 (**bias to action; show your work**), registered the new document, and elevated the "AGI is many forms, not one finish line" caution so it governs all files. Updated `README` and cross-links.
7. **Honestly logged as *not* solved:** the deepest weakness — the same AI both writes and reviews — is named as a **standing limitation**, with external falsifying feedback set as the headline goal for v1.2. We refuse to let existing checklists create false comfort.

**Why:** The user asked for (a) a hard self-audit, (b) practical, dynamically-spaced intermediate goals with something to showcase, and (c) full git history. The audit independently flagged the same progress gap as the system's #1 failure mode, so (a) and (b) converged.

**Expected benefit:** The system now *produces visible progress*, *makes predictions accountable*, *turns its domain list into a work queue*, and *names its own unfixable-by-documents limits* instead of hiding them.

**Trade-offs:** More moving parts. Mitigated by keeping the milestone system lightweight and by the "beware system astronomy" guardrail — the machinery must stay simple enough to actually use.

---

## v1.2 — 2026-06-20 — *Learn/Build architecture + dynamic, non-redundant files + idea-judging*

**What changed (from a detailed learner clarification of how the project should actually work):**

1. **Confirmed the North Star and the four parts.** The project is now explicitly **LEARN + BUILD + GATHER + SYSTEM**, all serving one combined goal: understanding *and* building toward AGI/ASI, toward an eventual career/startup/research path and an independent viewpoint. (Recorded in `MASTER_INSTRUCTION` §1 and `MILESTONE_AND_SHOWCASE_SYSTEM` §2.)
2. **Added `LEARNING_ARCHITECTURE.md`** *(new)* — the heart of the learn-engine. Defines: **DRY** (one concept, one canonical home; link, never repeat), the **dependency ladder** (foundational → advanced, always grounded), **dynamic insertion** via numbering gaps (new topics slot *between* existing files → read only the new file), and **dynamic intra-file change-tracking** (`rev` counter + `## Revision notes` + inline `*(updated revN)*` markers + the WHATS_NEW feed → read only what *changed* inside a file you'd already read, with git as the exact backup).
3. **Added `BUILD_SYSTEM.md`** *(new)* — the build-engine: a build ladder (toy → serious), the **AI/human division of labor** (I do the coding/heavy lifting and narrate it; you guide and learn), and the learn↔build loop.
4. **Added `IDEA_EVALUATION_SYSTEM.md`** *(new)* — I now **judge inputs before implementing**: every idea (the learner's or mine) passes five tests (true / feasible / viable / simplest / on-mission); I give a green/yellow/red verdict with plain reasons. Includes an honest capability check and a worked verdict on the "build a website" idea (🟡 — do it later as a static-site *view*, not a duplicated app now).
5. **Scaffolded the actual workspaces:** `LEARNING/` (the `00_MAP` ladder, `CONCEPT_REGISTRY`, `WHATS_NEW` feed, `_TEMPLATE`, and the first real module **`0100_what-is-intelligence`** as a working demonstrator) and `RESOURCES/` (`INDEX` seed catalog + `REQUESTS` list, with honest copyright/access limits stated).
6. **New house rules** #7 (*judge inputs, then implement*) and #8 (*don't repeat; link instead*) in `MASTER_INSTRUCTION`. Updated the doc table, `README`, and cross-links.

**Why:** The learner specified that the system must (a) gather resources and distil them into simple-but-deep notes, (b) build toward AGI/ASI with me doing the heavy lifting, (c) never repeat explanations across files, (d) let new material be inserted *between* already-read files, (e) let *changes inside* a file be read on their own, and (f) have me judge their ideas for what's practical. v1.2 turns each of those into a concrete mechanism.

**Expected benefit:** The project becomes *usable*, not just well-designed — there's now a real ladder to climb, a real way to build, a real catalog to gather into, and real rules that keep it non-redundant and re-read-free as it grows.

**Trade-offs:** Many more parts. Mitigated by: the DRY rule (less total text over time, not more), the idea-evaluation filter (we don't build everything), and the "system astronomy" guardrail (the demonstrator module 0100 already exists, proving we're producing content, not just scaffolding).

---

## v1.3 — 2026-06-20 — *Resource gathering + domain folders + the single-book scheme*

**What changed:**

1. **Gathered a *validated* resource base** (went online; checked official sources, not face value). [`RESOURCES/INDEX.md`](../RESOURCES/INDEX.md) now lists curated, mostly-free entry points **by domain** — university open-courseware (MIT OCW, Stanford, Berkeley) and canonical open textbooks (MML, MacKay, Goodfellow, Sutton & Barto, d2l, Nielsen, Neuronal Dynamics, Quantum Country, BlueDot AI-safety, 3Blue1Brown, etc.).
2. **Produced a prioritized cross-domain acquisition list** ([`RESOURCES/REQUESTS.md`](../RESOURCES/REQUESTS.md)) for the paywalled books worth buying (P1/P2/P3), and set up a **local, git-ignored `RESOURCES/library/`** for purchased PDFs/EPUBs — so copyrighted files stay off the public repo while I can still read them to write notes.
3. **Reorganized `LEARNING/` into seven domain folders** (`00-foundations`, `10-minds`, `20-machine-intelligence`, `30-math-and-theory`, `40-compute-and-physical`, `50-world-and-society`, `60-frontier`), each with a landing-page `_README`. Moved the demonstrator `0100` into `00-foundations/`.
4. **Reconciled "domain folders" with "one continuous book"** via `LEARNING_ARCHITECTURE` **§11** (folders = shelves where files live; the global sort-key + `00_MAP` = the single reading spine threading across them) and **§12 the chunk pipeline** (modules are woven from semantic *chunks* of many resources — never one-module-per-book — which is what makes it read as one authored, incremental book).

**Why:** The learner specified that resources must be gathered (prioritizing validated academic sources), broken into semantic chunks, segregated into domain folders with cross-references, yet still read as a single continuous incremental book — and asked for an acquisition list of paywalled items to obtain.

**Expected benefit:** A real, validated, browsable resource base; a clear, copyright-safe path to obtain paid materials; and a concrete organization that is both tidy-by-domain and readable-as-one-book.

**Trade-offs:** More structure up front. Gated: actual *book content* (the modules) is **not** mass-produced yet — pending the learner's approval of this scheme and the first resources landing in `library/`. Scaffolding is reversible via git.

---

## v1.4 — 2026-06-20 — *Papers, blogs & explainers catalog*

**What changed:** Added [`RESOURCES/PAPERS.md`](../RESOURCES/PAPERS.md) — a curated catalog of **landmark → state-of-the-art research papers** (by era/theme, oldest to newest), the primary **lab research hubs** (DeepMind, OpenAI, Anthropic, FAIR, Google Research, Microsoft Research, BAIR), the best **blogs/explainers** (colah, Distill, Lil'Log, Illustrated/Annotated Transformer, Karpathy, Neel Nanda), and **living SOTA trackers** (arXiv, Papers With Code, Raschka's lists) so the frontier list never goes stale. Recent/SOTA entries were web-verified; classic arXiv IDs included with a "verify before citing" note (QC hallucination guard).

**Why:** The learner asked for research papers (latest SOTA → oldest) across valid sources and labs, plus famous blogs/explainers, with any paywalled items flagged for the buy-list.

**Expected benefit:** A primary-source backbone (not just textbooks) to chunk into modules, and a sustainable way to follow the moving frontier.

**Trade-offs:** None material — almost everything is free; the buy-list ([`REQUESTS.md`](../RESOURCES/REQUESTS.md)) stays books. Still gated: modules aren't mass-produced until the scheme is approved.

---

## v1.5 — *(next)*

*Open. Most likely: on approval, begin writing the foundational modules (0200–0600) by chunking the gathered resources/papers; receive the first P1 books into `RESOURCES/library/`; and the standing goal — external, falsifying feedback.*
