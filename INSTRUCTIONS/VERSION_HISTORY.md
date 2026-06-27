# VERSION HISTORY
**What changed, when, and why.** The memory of the project. Nothing is final; everything here shows *how the thinking evolved*. We never silently overwrite the past.

`Part of: PROJECT ASI — Living Instruction System`
`Status: Living document · Last updated: 2026-06-27`

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

## v1.5 — 2026-06-20 — *AGI/ASI landscape map*

**What changed:** Added [`RESOURCES/LANDSCAPE.md`](../RESOURCES/LANDSCAPE.md) — a web-gathered map of the real-world actors racing toward AGI/ASI: the **research bets** (scale+reasoning, agents, world models/JEPA, neurosymbolic, brain-inspired, safety-first), mapped to our P1–P7 path framework; the **players** (OpenAI, Anthropic, Google DeepMind, xAI, Meta/FAIR, Microsoft; new labs SSI, Thinking Machines, AMI Labs, Mistral; the Chinese bloc — DeepSeek, Qwen, Moonshot, Zhipu, etc.); and the **chokepoints** (Nvidia/TSMC/ASML, compute, energy, data, geopolitics). Cross-linked from `AGI_ASI_INVESTIGATION_SYSTEM`.

**Why:** The learner asked to gather the research paths, ideas, startups, and companies currently pursuing AGI/ASI across the internet.

**Expected benefit:** Connects the abstract path framework to who is actually betting what — useful for the learner's "form an independent view" and "career/startup" goals.

**Trade-offs / caveats:** This is the project's **most perishable** file — figures are *as-reported (June 2026)* and flagged for re-verification; the durable value is the *structure of bets*, not the numbers. Strong anti-hype caveats included.

---

## v1.6 — 2026-06-20 — *Learner strategy, freshness checklist, hidden machinery, book curation*

**What changed:**
1. **Added [`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md)** — the learner is an AI-era **founder/director** (ESL, daily study, ~6–12mo to "found-a-DeepMind" readiness). Strategy: **learn to direct and decide, not to implement what the AI automates** — cut implementation grind, keep (and deepen) conceptual understanding, orchestration, system design, and the build track. Includes the founder's "what it takes + which expert team you'd need" map. *(Honest correction baked in: you can't direct/judge what you don't understand — so conceptual depth is non-negotiable.)*
2. **Added the Module Generation & Freshness Checklist** (`LEARNING_ARCHITECTURE` §13) — every file, every time, must pass: **SOTA-vs-outdated** (books may be stale; web-check fast-moving topics), grounded, ESL-simple, prerequisites covered/linked, cross-domain referenced (no repetition), theory+practice, director-altitude.
3. **Hid the machinery from the IDE** — `.vscode/settings.json` (`files.exclude`) hides INSTRUCTIONS/REVIEWS/README/AI_ONBOARDING/RESOURCES-catalogs so the learner sees only **study + build + their books**; added [`../START_HERE.md`](../START_HERE.md) as the single friendly entry point. Files still exist + stay in git.
4. **Added book-curation process** (`RESOURCES/library/CURATION.md`, local) — criteria to keep/skip each book the learner drops in, including **outdated-detection** (superseded methods, old editions), with per-file verdicts.
5. New house rule #9; doc table + cross-links updated.

**Why:** The learner specified an optimal, founder-level learning style (delegate the automatable, master the direct-able), wanted the behind-the-scenes hidden, asked for a strict per-file SOTA/groundedness/simplicity/prereq recheck, and is relocating the repo to hold many books that need vetting.

**Trade-offs:** More machinery — but it's now *hidden* from the learner by design, so it doesn't add to their cognitive load. Still gated: modules aren't mass-produced until the relocation + first books are in place.

---

## v1.7 — 2026-06-22 — *Library curated → KEEP-BROAD (11.5 GB → 4.8 GB)*

**What changed (final state):** Curated `local_resources/` from **11.46 GB / 3,507 files → 4.81 GB / 252 files**. The removed ~6.6 GB is **non-book clutter only**: Google-Cloud **certification Zoom recordings** (4.9 GB), DeepLearning.AI **course-slide screenshot** repos (1,618 files), a **Python cheat-sheet repo cloned 3×** + macOS `._` junk, Python official-docs PDFs, slide dumps, and exact-duplicate copies. **Every content-rich book is kept, across ALL domains** — including "dummies" and cross-domain titles (quantum/blockchain/crypto) and the academic "AI-for-industry" volumes. A full **backup of all originals** is retained externally (`Downloads\Learning_Resources\New folder (2)`).

**How we got there (honest record):** A first pass over-cut on a **filename-only** heuristic (down to ~1.1 GB), deleting the academic application volumes as a "flood." The learner corrected this in two steps — *"don't delete by filename, check the actual content"* and then *"keep content-rich resources broadly, even partial value"* — so all books were **restored from backup** and re-judged by **opening their content** (`pdftotext`). Net result: light curation, broad keep.

**Also:** content pass **corrected a misattribution** (`Introduction_to_Probability.pdf` = **Bertsekas & Tsitsiklis**, not Blitzstein) and confirmed newest editions (ISLP 2023, UDL Nov-2024, AIMA 4e); **~30 best books promoted to [`../RESOURCES/INDEX.md`](../RESOURCES/INDEX.md)** with `r-` ids + a new **📕 = local copy** marker; manifest + [`../RESOURCES/library/CURATION_VERDICTS.md`](../RESOURCES/library/CURATION_VERDICTS.md) updated.

**Lesson logged (standing method rule):** never delete a learning resource on filename alone — open the content first; bias to **keep** content-rich material broadly; only non-book clutter/duplicates get cut. The `rm` deletes were permanent (Git Bash bypasses the Recycle Bin); the external backup is what made recovery possible — keep it.

---

## v1.8 — 2026-06-22 — *Free-resource gap-fill + landmark-complete paper map (incl. robotics & AI-for-science)*

**What changed:**
1. **[`../RESOURCES/INDEX.md`](../RESOURCES/INDEX.md) — 7 web-verified free resources added** (each link fetched & confirmed live this session): **Stat 110** (Blitzstein probability, math) · **CS336 Language Modeling from Scratch** (Stanford — build an LLM end-to-end) · **Hugging Face Courses** (LLM/Agents/Deep-RL/Diffusion) · **Speech and Language Processing** (Jurafsky & Martin, Jan-2026 draft — the canonical NLP textbook) · **Spinning Up in Deep RL** (OpenAI) · **AlphaFold: A Practical Guide** (EMBL-EBI, AI-for-science) · **ARENA** (hands-on alignment/mech-interp curriculum + code).
2. **[`../RESOURCES/PAPERS.md`](../RESOURCES/PAPERS.md) — rebuilt into a landmark-complete map.** Section D went from 6 era-buckets to **13 era + area sections (~110 papers)**: foundations → DL breakthrough → transformers → scaling/reasoning → **alignment/RLHF** (Christiano→DPO→Sleeper Agents + interpretability) → **RL** (PPO/SAC + AlphaGo→CICERO) → **efficiency & systems** (MoE, FlashAttention, RoPE, ZeRO, vLLM, QLoRA) → **diffusion** → **multimodal** (CLIP/Whisper/LLaVA) → **agents & RAG** → **post-transformer** (Mamba/S4/RWKV) → **robotics & embodied AI** (World Models, RT-1/2, PaLM-E, Open X-Embodiment, π0) → **AI for science & the intersected frontier** — deliberately broad per the learner: biology/medicine (AlphaFold 2/3, ESM, AlphaMissense, Med-PaLM, Evo), math & algorithms (AlphaTensor/AlphaDev, FunSearch/AlphaGeometry), code (AlphaCode, SWE-bench), physics/materials/weather (tokamak-fusion control, GNoME, GraphCast/GenCast), **space & astronomy** (exoplanets, gravitational waves, M87 black-hole imaging), **quantum computing × AI** (Quantum ML, AlphaQubit), **neuroscience & BCI** (fMRI language/image decoding, speech neuroprosthesis), **decentralized/web3 AI** (Petals, DiLoCo, zkML — flagged earlier-stage), and an **emerging-frontiers** block (AlphaChip, RFdiffusion, autonomous "self-driving" labs, world models/Genie, TabPFN).

**Why:** The learner asked to (a) fill missing free high-quality resources online, and (b) make the paper catalog *complete* — **every field and domain where AI is making a vast difference on the way to AGI/ASI**, robotics and all intersected sciences included. Rationale: the strongest evidence of progress toward general capability is AI moving the frontier of *other* disciplines, so the map must show those vectors, not just core ML.

**Expected benefit:** A learner/director can now see the whole research landscape — core methods *and* every applied frontier — from one catalog, with verified free entry points to study each.

**Trade-offs / honesty:** This is broader than the "4 well-chosen beat 300" rule, so the discipline shifts to **landmark-grade per area** (one canonical paper per advance, not exhaustive lists). Per the file's standing QC note, **arXiv IDs are best-effort from a known-paper set and must be auto-verified before any module cites them** — titles + authors + year are the stable handle. Nature/Science papers list the venue (free author/lab copies exist); nothing here needs to be purchased.

---

## v1.9 — 2026-06-22 — *Learning philosophy sharpened (no coding grind) + idea-deepened paper map*

**What changed:**
1. **[`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §3 — added the "deciding test"** (the learner's own framing): include a topic **iff "I'll need to rely on / understand it to build and direct AI" — even if AI can do it.** Exclude pure **execution skills (coding/programming and similar mechanical work)**: mastering them is an *"assumed achievement,"* not a real one. Real achievement = understanding deep enough to *originate and judge*.
2. **Dropped the planned CUDA/GPU-programming + TinyML *coding* course section** from `INDEX.md` (it was researched & link-verified, then cut). Reason: it's delegatable execution — exactly what §3 says to skip. The *concepts* of compute/scaling/efficiency remain (domain 40 + PAPERS D6 + scaling-laws papers + **Sutton's *Bitter Lesson*** essay, newly added to PAPERS §C).
3. **[`../RESOURCES/PAPERS.md`](../RESOURCES/PAPERS.md) deepened with ~35 idea-defining landmarks** (understanding, *not* engineering variants): D0 history-of-ideas (Minsky&Papert, Neocognitron, SVM, Deep Belief Nets); D1 the **attention origin** (Bahdanau 2014); D3 **instruction-tuning** (FLAN) + **test-time-compute reasoning** (o1); D4 the **safety framing** (Concrete Problems, AI Safety via Debate, Unsolved Problems, process supervision); D7 diffusion mechanisms (DDIM/ControlNet/DiT); D9 retrieval & tool-use origins (DPR, Self-RAG, WebGPT); D10 architecture ideas (efficient-attention, Hyena, Jamba); D11 founding robotics results (Levine 2016, Dactyl/sim2real, SayCan); D12 capability breadth (RoseTTAFold, MatterGen, ChemCrow, NeuralGCM). Catalog ≈ **145 papers**.

**Why:** The learner clarified the whole point — *understand everything needed to build/direct AGI/ASI; skip what is only a hollow skill-demo (coding above all).* This reshapes both what we catalog and, more importantly, **how every future module is written**.

**Trade-offs / honesty:** Same arXiv-ID caveat as v1.8 (best-effort; auto-verify before any module cites). The added breadth is *map-of-ideas* value, not hoarding — each entry is justified as understanding-relevant; coding-skill resources are deliberately excluded.

---

## v2.0 — 2026-06-22 — *The book starts: foundation rungs 0200–0600 written*

**What changed:** Began **producing the actual learning content** (Task C). Wrote six new modules — the foundations spine now runs unbroken **0100 → 0600**:
1. [`0200 What is a system?`](../LEARNING/00-foundations/0200_what-is-a-system.md) — parts + relationships → **emergence**; intelligence as a system property (`c-system`).
2. [`0250 Feedback loops & control`](../LEARNING/00-foundations/0250_feedback-loops-and-control.md) — negative/positive loops, control, the seed of agency/learning and the intelligence-explosion debate (`c-feedback`).
3. [`0300 Information & entropy`](../LEARNING/00-foundations/0300_information-and-entropy.md) — bit, surprise, **compression ≈ understanding**; what cross-entropy loss measures (`c-entropy`).
4. [`0350 Just-enough linear algebra`](../LEARNING/30-math-and-theory/0350_just-enough-linear-algebra.md) — vectors-as-meaning, matrices-as-motion, why GPUs; shelved in `30-math/`, slotted early on the spine (`c-linear-algebra`).
5. [`0400 Computation`](../LEARNING/00-foundations/0400_computation.md) — what a computer does, universality, abstraction layers, complexity, hard limits (`c-computation`).
6. [`0500 Probability & uncertainty`](../LEARNING/00-foundations/0500_probability-and-uncertainty.md) — Bayes & base rates, expected value, distributions/fat tails (`c-probability`).
7. [`0600 What it means to learn`](../LEARNING/00-foundations/0600_what-it-means-to-learn.md) — capstone: learning as a generalizing error-loop, the four flavors (incl. self-supervised), overfitting, the **Bitter Lesson** (`c-learning`).

Bookkeeping kept in lock-step: ~25 concepts added to [`CONCEPT_REGISTRY`](../LEARNING/CONCEPT_REGISTRY.md), [`00_MAP`](../LEARNING/00_MAP.md) statuses flipped to ✅, [`WHATS_NEW`](../LEARNING/WHATS_NEW.md) delta lines added, both folder READMEs updated.

**Why:** The machinery (v1.0–v1.9) existed to enable exactly this — the learner asked to **start the book**. Foundations first because every later chapter (minds, machine intelligence, frontier) stands on these rungs.

**Expected benefit:** A real, readable, non-repeating spine the learner can climb today — and a worked demonstration that the architecture (DRY, ladder, dynamic insertion, freshness checklist, director-altitude) produces good content, not just rules.

**Trade-offs / honesty:** Every module ran the §13 freshness checklist and is pitched at director-altitude per `LEARNER_STRATEGY` §3 (concepts/judgment, no coding grind). Fast-aging claims are tagged (e.g. self-supervised-as-SOTA in 0600) for periodic re-check. Major version bump (1.9 → 2.0) marks the shift from *building the system* to *producing the content*.

---

## v2.1 — 2026-06-22 — *The "minds" chapter: natural intelligence (rungs 0700–0900)*

**What changed:** Continued the book into [`10-minds/`](../LEARNING/10-minds/) — the spine now runs unbroken **0100 → 0900**:
1. [`0700 The brain — a 10-minute working model`](../LEARNING/10-minds/0700_the-brain-working-model.md) (`c-brain`) — neuron/synapse/plasticity (what artificial neural nets borrowed), the brain as a **prediction machine**, and an honest gap-list where the brain still beats AI (≈20 W, sample-efficiency, no catastrophic forgetting, embodiment).
2. [`0800 How a child's mind bootstraps`](../LEARNING/10-minds/0800_child-mind-bootstraps.md) (`c-development`) — the child as the existence proof of general intelligence from little data; five director-relevant features (sample-efficiency, core-knowledge priors, active/causal learning, intrinsic curiosity, social scaffolding) framed as a map of what current AI lacks.
3. [`0900 Evolution & general intelligence`](../LEARNING/10-minds/0900_evolution-and-general-intelligence.md) (`c-evolution`) — evolution as a gradient-free optimizer; the **inner/outer (mesa) alignment** cautionary tale via humans-vs-evolution; intelligence as contingent and **cumulatively cultural**. Sets up alignment (1900) and society (2000).

Bookkeeping in lock-step: ~14 concepts → `CONCEPT_REGISTRY` (incl. mesa-optimization seed), `00_MAP` statuses ✅, `WHATS_NEW` deltas, `10-minds/_README` updated.

**Why:** The learner said "continue straight into 0700–0900." Natural intelligence is the one worked example of AGI; it both inspired AI and marks where AI still falls short — essential grounding before the machine-intelligence chapter.

**Expected benefit:** The learner can now trace a single argument from "what is intelligence" through systems/learning into brains, development, and evolution — and arrives at the machine-intelligence chapter already holding the brain-inspiration and alignment-analogy hooks those modules will reuse.

**Trade-offs / honesty:** Several claims here are live theories, tagged accordingly — predictive processing & cortical uniformity (0700) **[Likely → Speculative]**, developmental priors/stages (0800) **[Likely/Contested]**, mesa-optimization-applied-to-AI (0900) **[Contested/Speculative]**. The developmental-cognition canon (Gopnik, Spelke, Piaget, Vygotsky) is cited by name but not yet a held resource — flagged for `REQUESTS.md` if a later module needs depth. Minor bump (2.0 → 2.1): more content along the same architecture.

---

## v2.2 — 2026-06-27 — *The machine-intelligence CORE: how we actually build AI (rungs 1000–1300)*

**What changed:** Wrote the chapter the whole project points at — [`20-machine-intelligence/`](../LEARNING/20-machine-intelligence/) — so the spine now runs unbroken **0100 → 1300**. Four core rungs, each framed as a *special case of [0600 Learning](../LEARNING/00-foundations/0600_what-it-means-to-learn.md)* and linking **back** to foundations/minds rather than repeating them:
1. [`1000 Machine learning — learning from examples`](../LEARNING/20-machine-intelligence/1000_machine-learning-from-examples.md) (`c-machine-learning`) — model = function with tunable **parameters/weights**; the five parts of every ML system; **gradient descent** (the downhill walk promised at 0600); train/validation/**test** split; **bias–variance**; and the calibration that **classical ML (boosting/trees) still beats deep learning on tabular data** — "AI ≠ deep learning."
2. [`1100 Neural networks & deep learning`](../LEARNING/20-machine-intelligence/1100_neural-networks-deep-learning.md) (`c-neural-networks`) — artificial neuron (links back to [0700](../LEARNING/10-minds/0700_the-brain-working-model.md)), layers/depth as stacked matrix-math ([0350](../LEARNING/30-math-and-theory/0350_just-enough-linear-algebra.md)), **backpropagation** (credit assignment), and the load-bearing idea **representation learning** (the model learns its own features); architectures (CNN/RNN/transformer) = inductive bias; black-box/brittleness honesty box.
3. [`1200 Reinforcement learning & agents`](../LEARNING/20-machine-intelligence/1200_reinforcement-learning-and-agents.md) (`c-reinforcement-learning`) — learning to **act** from reward (the control loop of [0250](../LEARNING/00-foundations/0250_feedback-loops-and-control.md) with a learned policy); value/return, explore-vs-exploit, temporal credit assignment; **reward hacking** as the live, concrete form of the 0900 mesa/Goodhart story; deep RL & **self-play** (DQN/AlphaZero); the **LLM-agent** frontier (prediction → action → higher stakes).
4. [`1300 Language models (LLMs) — how they actually work`](../LEARNING/20-machine-intelligence/1300_language-models-how-llms-work.md) (`c-language-models`) — *capstone.* **Next-token prediction** (predict ⇒ compress ⇒ understand, [0300](../LEARNING/00-foundations/0300_information-and-entropy.md)); the **transformer & attention** (dot-product similarity, [0350](../LEARNING/30-math-and-theory/0350_just-enough-linear-algebra.md)); the three stages **pretrain → fine-tune → RLHF**; emergence/scaling; chain-of-thought & **test-time compute** (AI's "slow" mode, [0700](../LEARNING/10-minds/0700_the-brain-working-model.md)); and a hard honesty box on **hallucination** and the open "do they understand?" debate.

Bookkeeping in lock-step: **35 concepts** added to `CONCEPT_REGISTRY`, `00_MAP` statuses 1000–1300 → ✅, `WHATS_NEW` milestone delta, `20-machine-intelligence/_README` filled in, version → **2.2** across files.

**Why:** The hand-off flagged this as the chapter the learner most wants depth in — "where we actually build it." With foundations (what learning/computation/probability are) and minds (the one worked example) in place, the learner is ready to see ML/DL/RL/LLMs as **four variations of one error-reducing loop**, not four mysteries.

**Expected benefit:** The learner can now reason about, budget for, and *direct* a modern AI system — knowing what a model/loss/gradient is, what deep learning's real trick is (representation learning), why agents raise the stakes, and exactly what an LLM can and cannot do — with every claim tagged and every hard word linked to its one home.

**Trade-offs / honesty:** Fast-moving frontier content is explicitly tagged as **2026 snapshots** (reasoning/test-time compute, the LLM-agent surge) and flagged for re-check; "emergence" is presented with its **[Contested]** mirage rebuttal; and the "do LLMs understand?" question is deliberately left **open** with both sides stated. Specific landmark results (AlexNet, AlphaZero, the transformer, InstructGPT/RLHF, o1-era reasoning) are named from `PAPERS.md` — arXiv IDs there remain best-effort and should be auto-verified before any module cites an ID directly (standing follow-up). Minor bump (2.1 → 2.2): more content along the same architecture.
