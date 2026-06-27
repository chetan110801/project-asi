# HARD RULES — the binding standard for collection & synthesis
**The strict, non-negotiable rules for what we collect and how every module is written.** This is the project's `_DOS_AND_DONTS` (modeled on the learner's "hy" system). It is a **final gate**: no module is "done" until it passes §7. Where this adds detail to [`MASTER_INSTRUCTION.md`](MASTER_INSTRUCTION.md), the constitution still wins; this never contradicts it (and §8 forbids drift).

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 2.4 (new in v2.4) · Status: Living / binding · Last updated: 2026-06-27`

> **Priority order when rules collide** (from "hy"): **1) miss nothing that matters → 2) understand deeply → 3) grounded & non-repeating → 4) simple & beautiful → 5) concise.** Concise is **last** — never cut depth, coverage, or a gloss to be short.

---

## §1. SCOPE — what we collect (broadened, learner 2026-06-27)
1.1 Collect a **rich corpus across every crucial science/technology domain that can drastically affect humanity and advance society — prioritizing the path to AGI/ASI.** Examples (non-exhaustive, a living queue — see [`DOMAIN_DISCOVERY_SYSTEM.md`](DOMAIN_DISCOVERY_SYSTEM.md)): brain & neuroscience, cognitive science, AI/ML/DL/RL/LLMs, agents, robotics, math & theory, information & computation, hardware/chips/compute, energy, quantum computing, biology/biotech, materials, physics, complex systems, blockchain/web3/decentralization, economics & data, governance/safety/alignment.
1.2 **Study domains independently, foundations → advanced** (like math/physics/chemistry/biology as separate subjects), each on its own shelf — **then merge concepts across domains where they connect.** (This is already the architecture: domain folders = shelves; [`../LEARNING/00_MAP.md`](../LEARNING/) = the one concept-by-concept spine threading across them. See [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md).)
1.3 **Collect all media types** that carry rich understanding: textbooks, books, research papers & publications, lecture courses, survey/review papers, blogs/essays by serious practitioners, recorded debates & interviews, podcasts, and video/YouTube (transcripts). Debates/disagreements between experts are high-value ([`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md) §4).
1.4 **Take as many sessions as needed.** Collection is a sanctioned, multi-session campaign because every collected source is **destined to be processed** into grounded modules (see §3) — it is *not* the "giant unread library" the anti-hoarding rule warns against (reconciliation: [`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md) §1 amended v2.4). Order the *processing* by leverage (understanding-per-hour) × AGI/ASI-relevance.

## §2. THE DURABILITY FILTER — timeless principles, not transient specifics (learner 2026-06-27)
2.1 We learn the **grounded, objective reality that sustains the test of time** — the **reason and objective behind** things — **not** the static, replaceable specifics.
2.2 Worked example (the learner's): a 2012 NLP algorithm later replaced by a 2020 one — **we do NOT memorize either algorithm.** We learn **why** the problem exists, what objective each approach optimizes, and the trade-offs — so we could **invent the next one.** The transient artifact appears only as a brief illustration of the enduring idea, never as the point.
2.3 This is the existing **Durability / slow-aging** criterion ([`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md) §3, §5) made a **hard rule.** It also reconciles "collect every domain" with the *"rely-on-to-build" test* ([`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §2–§3): include the **enduring conceptual foundations** of each crucial domain; skip **execution grind and transient specifics.**
2.4 Fast-aging facts (current SOTA, who's ahead, latest model) are included only when decision-relevant, and **tagged as dated snapshots** ([`QUALITY_CONTROL_SYSTEM.md`](QUALITY_CONTROL_SYSTEM.md) §4 staleness).

## §3. THE CORPUS — the grounding substrate
3.1 Collected sources are extracted to **greppable text, chunked, organized by source**, in [`../RESOURCES/corpus/`](../RESOURCES/corpus/). Method: [`../RESOURCES/corpus/_CORPUS_BUILD.md`](../RESOURCES/corpus/_CORPUS_BUILD.md). Targets: [`_ACQUISITION_PLAN.md`](../RESOURCES/corpus/_ACQUISITION_PLAN.md). Status: [`_COVERAGE_MAP.md`](../RESOURCES/corpus/_COVERAGE_MAP.md).
3.2 **Legality is absolute:** only legally-free sources or the learner's own owned copies enter the corpus; **nothing pirated.** The corpus **text stays local** (git-ignored, like `local_resources/`); only the **synthesized modules** are published — exactly as "hy" publishes `Synthesis/`, not `_corpus/`.

## §4. SEGREGATION & FLOW — concept-by-concept, not book-by-book
4.1 Modules are organized **by concept, in a dependency order where each concept builds on the ones before** — never "book 1, then book 2." (This is the "hy" flow and the existing dependency ladder, [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md).)
4.2 **One concept → one canonical home** (DRY, house rule #8); everywhere else **link, don't restate.** Log every concept in [`../LEARNING/CONCEPT_REGISTRY.md`](../LEARNING/CONCEPT_REGISTRY.md).
4.3 Big topics **split into several grounded sub-rungs** via numbering gaps (e.g. "LLMs" → a cluster), each at full depth, rather than one shallow file.

## §5. SYNTHESIS DEPTH — EXHAUSTIVE on the conceptual axis (v2.3)
5.1 **Render every enduring idea, mechanism, argument, distinction, key result, example, trade-off, failure mode, and live debate** the sources hold on the topic. **Miss nothing** that bears on understanding-to-direct. (Coverage beats brevity.)
5.2 **Implementation/execution stays delegated** — modules are not coding tutorials and don't grind proofs; render math/mechanism for *complete insight*, leave the code/derivation to "direct the AI." ([`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §7b: *cut implementation depth, never conceptual depth.*)
5.3 Use the **five depth devices** on every important idea: plain read → deeper principle → *what it rules out* → why it matters; per example, *why this example*; **anticipate the objection** and resolve it; **name the exact misconception**; **show each idea click onto the one before.**

## §6. LANGUAGE — two axes that never conflict (the 8-year-old bar + glossing)
6.1 **Axis 1 — reading ease (the 8-year-old bar):** explaining prose reads as if for a bright 8-year-old. **One idea per sentence**; split any two-step sentence; plainest connective words (*uses* not *employs*, *so* not *hence*). Read-aloud test. **Reading ease is sentence-shape only — never soften the idea, the depth, or the content.**
6.2 **Axis 2 — vocabulary richness + MANDATORY GLOSSING (learner 2026-06-27):** keep the real vocabulary — every **medium-to-advanced word, phrase, collocation, idiom, and technical/scientific term** — and **gloss each inline in plain parentheses: the general meaning *and* the in-context meaning, in very simple words**, e.g. `gradient (the slope/steepness of something; here: the direction of steepest change in the error)`. Gloss the **first** time an item appears; a short reminder if it returns much later. The reader is a **non-native learner** — when in doubt, gloss it.
6.3 The two axes coexist: simple **sentence frames** carrying **rich, glossed** terms. The file **grows** as a result — that is wanted (concise is last). If 3+ glosses jam one sentence, **split the sentence** (axis 1); do **not** drop a gloss (axis 2).
6.4 Keep the project voice: concrete-example-first, confidence tags `[Established]/[Likely]/[Contested]/[Speculative]`, the **⚠️ honesty box** where hype is common, and the **"How a director uses this / what you delegate vs own"** section.

## §7. THE FINAL GATE — run on EVERY module before it's "done"
*(Adapted from "hy" §11 + [`QUALITY_CONTROL_SYSTEM.md`](QUALITY_CONTROL_SYSTEM.md). Switch hats: write, then re-read as harsh critic + confused beginner.)*
- [ ] **Grounded (F):** every factual claim, number, and quote traces to a corpus line; quotes are **verbatim** (grep them); a paraphrase posing as a quote is a defect.
- [ ] **Complete (B):** diff against the source(s); every enduring idea/argument/distinction/example is **present or cross-linked** — nothing important dropped. (Transient specifics may be compressed; enduring concepts may not.)
- [ ] **Non-repeating (C / DRY):** each idea once, in its home; different *angles* are good; cross-link what another rung owns.
- [ ] **Glossed (G):** word-by-word sweep — **zero bare** medium-to-advanced/technical items; every gloss gives general + context meaning in simple words; never a hard word used to explain a hard word.
- [ ] **Simple (H):** the 8-year-old read-aloud bar passes; two-step sentences split; fancy connectives swapped for plain ones.
- [ ] **Deep (D):** the five depth devices present on the important ideas; nothing merely asserted.
- [ ] **Honest:** confidence tags on contested claims; strongest opposing view stated; fast-aging claims tagged as snapshots; not pretending to more certainty than we have.
- [ ] **Structure:** builds on earlier rungs (links back, doesn't re-lay groundwork); registry + WHATS_NEW + `00_MAP` updated; freshness checklist ([`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §13) passed.

## §8. META-RULE — consistency on every rule change (learner 2026-06-27)
8.1 **Whenever a rule is added or edited, check the whole rule set for consistency** — confirm existing rules can co-exist with the change. If two rules conflict, **resolve it** (one must change) and record the resolution; never leave a silent contradiction. (This makes binding the **Consistency** check already in [`QUALITY_CONTROL_SYSTEM.md`](QUALITY_CONTROL_SYSTEM.md) §2 and house rule #8's spirit; the constitution [`MASTER_INSTRUCTION.md`](MASTER_INSTRUCTION.md) §8 already mandates a contradiction-check before finalizing.)
8.2 Record every rule change in [`VERSION_HISTORY.md`](VERSION_HISTORY.md) with the reconciliation, and mirror standing changes into the relevant docs + auto-memory. Nothing is final (house rule #3).

---

## Reconciliations on record (so future sessions see these are intentional, not contradictions)
- **"Collect everything" vs. anti-hoarding** ([`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md) §1): the corpus is **destined for processing**, not a trophy shelf; the understanding-per-hour metric now governs **processing order**, not whether to collect. Amended there v2.4.
- **"Every domain" vs. "listed ≠ engaged"** ([`DOMAIN_DISCOVERY_SYSTEM.md`](DOMAIN_DISCOVERY_SYSTEM.md)): collecting a domain's corpus is necessary but **not** "covered" — a domain counts as covered only when it has produced grounded modules.
- **8-year-old bar** supersedes the older "12-year-old" wording in the module gates — [`QUALITY_CONTROL_SYSTEM.md`](QUALITY_CONTROL_SYSTEM.md) §2 and [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §13 — for learning modules (stricter bar; same intent). *(The Feynman teach-back in `LEARNING_METHOD.md` and the public explainers in `MILESTONE_AND_SHOWCASE_SYSTEM.md` keep "12-year-old" — those are the learner's own outputs to others, a different context, not the module reading bar.)*
- **Exhaustive depth** vs. "director-altitude / don't implement-grind": split by axis — conceptual = exhaustive, execution = delegated ([`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §7b).
