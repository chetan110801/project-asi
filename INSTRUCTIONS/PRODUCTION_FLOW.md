# PRODUCTION FLOW — how we turn the corpus into study material
**The operating flow for producing grounded learning modules now that the corpus spans 31 domains.** This is the *how-we-work* layer. It sits on top of three docs and never restates them: [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) (the **shape** of content — DRY, ladder, numbering gaps, read-only-the-change), [`HARD_RULES.md`](HARD_RULES.md) (the **standard** every module must pass), and [`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) (the **depth policy** — direct-and-decide, not implement).

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 2.5 (new in v2.5) · Status: Living / binding · Last updated: 2026-07-02`

> **Why this exists (the problem in two lines).** The gathering campaign built a corpus of ~54,000 text files across **31 folders**, organized *by source* (`textbooks/`, `courses/`, `transcripts/`, `papers/`, `frontier-rnd/`) **and** *by discipline* (`physics/`, `biology/`, …) at once — so no domain lives in one place, and quality inside the source dumps swings from gold to noise. The old flow (one global linear spine + equal exhaustive depth for every module) cannot sequence 31 disciplines, cannot find the scattered grounding fast, and would make writing effectively unbounded. v2.5 fixes exactly those failures **without** discarding anything that worked.

---

## The six components

### ① Depth Tiers — calibrated depth per domain (the anti-drowning rule)
Not every domain earns the same depth. Before writing, each domain gets a **depth budget** set by the *rely-on-to-build* test ([`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §2–§3) × AGI/ASI-relevance ([`HARD_RULES.md`](HARD_RULES.md) §1.4):
- **Core (exhaustive — full hy standard):** you must deeply understand it to build/direct AGI/ASI. Written to the full [`HARD_RULES.md`](HARD_RULES.md) §5 depth.
- **Bridge (working depth — you decide, you don't build):** materially feeds AGI; render enough to reason and choose well, not every mechanism.
- **Literacy (compact conceptual map):** the broad sciences/engineering that shape a founder-director's worldview and show *how each field pushes AGI* — the enduring core + the connection, **not** textbook reproduction.

The **tier assignment table** is the one home in [`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) (co-located with the depth/breadth audit). Reconciliation with "cover every domain": a Literacy module still *covers* the domain (HARD_RULES §Reconciliations — a domain is covered only when it yields grounded modules); tiering sets **how deep**, not **whether**.

### ② The Atlas — the grounding index (fixes the scattering)
For each domain, a map of **every corpus source that touches it across all folders**, tagged by level (elementary / undergrad / grad / research) and quality. It is the table a writer greps *before* drafting, so grounding stops being needle-in-a-haystack. It doubles as a **living depth/breadth audit** of the whole corpus. Home: [`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) (master) + per-domain slices `_ATLAS_<domain>.md` at the corpus root (root-level so they publish; sub-folder `.md` is git-ignored). **Built just-in-time per domain** as that domain reaches the front of the queue — never all 31 upfront (that would be the over-scaffolding this project warns against).

### ③ Trunk & Branches — replaces the one impossible spine
- **The Trunk** = the AGI/ASI reading spine — today's [`../LEARNING/00_MAP.md`](../LEARNING/00_MAP.md), extended. The *one* deep narrative that genuinely reads as a single book (intelligence → foundations → minds → machine intelligence → compute/data/scaling → paths to AGI → alignment → governance → ASI). Core + Bridge live here. **This is the primary product.**
- **The Branches** = domain shelves (`physics`, `chemistry`, `biology`, engineering…), each a *local* mini-ladder at its tier depth, **not** forced into the global reading order, each ending in a **"how this domain feeds AGI/ASI" capstone** that links into the Trunk.
- **The Web** = the cross-links in [`../LEARNING/CONCEPT_REGISTRY.md`](../LEARNING/CONCEPT_REGISTRY.md) binding branch concepts to their trunk usage.

This keeps "reads like one book" *true for the thing that matters* while letting 31 domains live as appropriately-deep, browsable branches.

### ④ The Queue — dynamic, leverage-ordered "what's next"
A living ledger: every planned module scored by **leverage (understanding-per-hour) × AGI/ASI-relevance × corpus-readiness**. Always write the top; re-sort as modules finish and as gaps surface. This is what makes the flow *optimal* (highest-value first) and *dynamic* (order is never frozen). Home: [`../LEARNING/_QUEUE.md`](../LEARNING/_QUEUE.md).

### ⑤ The Assembly line — the repeatable per-module pipeline
One module, start to finish:
1. **PICK** the top of the [`_QUEUE.md`](../LEARNING/_QUEUE.md).
2. **INDEX** — if the domain's Atlas slice doesn't exist yet, build it (component ②).
3. **GATHER** — grep the Atlas slice → pull the relevant chunks across all folders into a scratch **evidence file** (verbatim, with source paths).
4. **OUTLINE** — list the concepts + run the dependency check ([`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §8). If a prereq module is missing, **insert it first** (numbering gap) — never assume.
5. **DRAFT** — to [`../LEARNING/_TEMPLATE.md`](../LEARNING/_TEMPLATE.md), with the five depth devices ([`HARD_RULES.md`](HARD_RULES.md) §5.3) and mandatory glossing (§6), at the domain's tier depth.
6. **GROUND-CHECK** — the final gate ([`HARD_RULES.md`](HARD_RULES.md) §7): every claim/number/quote grep'd **verbatim** against the corpus; a paraphrase posing as a quote is a defect.
7. **SELF-CRITIQUE** — re-read twice, as harsh critic *and* as confused beginner; fix.
8. **REGISTER & ANNOUNCE** — CONCEPT_REGISTRY + `00_MAP`/branch map + `WHATS_NEW` updated; commit.

### ⑥ Self-healing — how the flow stays dynamic
- **Write pulls gather.** A module that can't ground a needed claim triggers a **surgical GET** (one source), not a gathering session. This is the standing answer to "do we have enough?" — you find real holes *by writing*, then patch them.
- **Staleness.** Fast-aging claims tagged as dated snapshots ([`HARD_RULES.md`](HARD_RULES.md) §2.4); the freshness checklist ([`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §13) runs every time.
- **External red-team (optional).** A finished Core module may be attacked by an independent model (e.g. the Claude science app) as *falsifying feedback* — never as a source (memory-generated synthesis is exactly what we don't cite).

---

## ⭐ THE PER-FILE GATE — every rule for producing one study-material file
**The single anti-inconsistency contract.** Run top-to-bottom for *every* file, every time; a file is not "done" until all pass. Each rule's full home is linked — this is the checklist, not a re-teach (DRY). The **step order** for actually building the file is the assembly line (⑤ above); this is the **rule set** those steps must satisfy.

**Rule 0 — PURPOSE (the content test): AI-proof wisdom, not memorization.** [[`HARD_RULES.md`](HARD_RULES.md) §2.5 + §2]
The file exists to give **durable understanding and wisdom that survives even when AI does all the execution** — *not* a reference sheet. For **every item**, ask: *"Is this here so the learner **understands and can judge** it, or so they can **reproduce** it?"* Keep the durable part (why it exists · what it optimizes · what it rules out · trade-offs · failure modes · the live debate — enough to direct an AI and invent the next one); **delegate the recipe** (functions, libraries, frameworks, algorithm steps, definitions-to-recite, calculations, architecture templates) to the AI. Timeless principles, never transient specifics.

**Rule 1 — DEPTH (tier).** [[`HARD_RULES.md`](HARD_RULES.md) §5.4 + §5.1 + [`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) §1]
Write to the domain's tier: **Core** exhaustive · **Bridge** working depth · **Literacy** compact map + "how it feeds AGI." Conceptual axis rendered in full; execution axis delegated (§5.2).

**Rule 2 — GROUNDING (truth).** [[`HARD_RULES.md`](HARD_RULES.md) §3 + §7 + [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §13.1]
Every claim/number/quote traces to a corpus line; **quotes verbatim (grep them)** — a paraphrase posing as a quote is a defect. Run the SOTA/not-outdated check; web-check fast-moving claims. Confidence tags `[Established]/[Likely]/[Contested]/[Speculative]`, the strongest opposing view stated, fast-aging facts tagged as snapshots.

**Rule 3 — STRUCTURE (extended DRY + ladder + dynamic layout).** [[`HARD_RULES.md`](HARD_RULES.md) §4.2 · §4.4 · §4.5 + [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §8 + [`../LEARNING/_TEMPLATE.md`](../LEARNING/_TEMPLATE.md)]
**Extended DRY:** any idea / argument / theory / example is *explained* once, in one home — **within this file and across all files**; everywhere else reference it (a §4.2a one-line refresher is fine, a re-explanation is a defect). A genuinely new *viewpoint/angle* (something not already said) is welcome and should be discussed; **restating the same substance in different vocabulary is the forbidden repetition** — the test is substance, not wording. **Self-containedness:** a one-line plain refresher of a borrowed prereq at the point of use, then link — never a bare link. Stands only on earlier rungs; a missing prereq is inserted first via a numbering gap. **Dynamic layout, not a rigid form (§4.4):** choose the per-file structure that makes *these* ideas easiest to grasp; the template is a palette of required ingredients, not a fixed order. **Visual ease (§4.5):** break big paragraphs into small ones; use lists/tables/analogies/whitespace so complex ideas read easily. **Length is free** — as long as the ideas require; never trim depth/coverage/examples/glosses to shorten.

**Rule 4 — DEPTH DEVICES.** [[`HARD_RULES.md`](HARD_RULES.md) §5.3]
On every important idea: plain read → deeper principle → *what it rules out* → why it matters; *why this example*; anticipate-the-objection & resolve it; name-the-exact-misconception; show it click onto the previous rung. Nothing merely asserted.

**Rule 5 — LANGUAGE.** [[`HARD_RULES.md`](HARD_RULES.md) §6]
8-year-old **sentence shapes** (one idea per sentence, plainest connectives) carrying **full, glossed vocabulary** — every medium/advanced/technical term glossed inline (general + in-context meaning, simple words). **Zero bare hard items.** If 3+ glosses jam a sentence, split it; never drop a gloss.

**Rule 6 — DIRECTOR VALUE.** [[`HARD_RULES.md`](HARD_RULES.md) §6.4 + [`LEARNER_STRATEGY.md`](LEARNER_STRATEGY.md) §5–§6]
Include "**How a director uses this / what you delegate vs. own**," the ⚠️ **honesty box** where hype is common, and "how you'd get this built with the AI" where relevant.

**Rule 7 — REGISTER & ANNOUNCE.** [[`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §8–§9]
Update CONCEPT_REGISTRY + the Trunk/branch map + WHATS_NEW; on an edit, bump `rev` + add a Revision note (read-only-the-change); commit to git.

**Rule 8 — CONSISTENCY (the anti-contradiction rule).** [[`HARD_RULES.md`](HARD_RULES.md) §8]
Before "done," confirm the file **contradicts no other module and no rule**. If it does, resolve it (one side must change) and record the resolution — **never leave a silent contradiction.** A changed concept must reconcile with its registry entry.

> **The eight in one breath:** *AI-proof purpose → right depth for the tier → grounded & true → DRY & laddered → deep (the five devices) → simple & fully glossed → director value → registered → contradiction-free.*

---

## What v2.5 keeps unchanged (do not reinvent)
DRY / one-home, numbering-gap insertion, the dependency ladder, dynamic insertion + `rev`/Revision-notes (read only the change), the final gate, the 8-year-old + glossing bar, exhaustive-concept / delegated-execution, and the frontmatter schema — all from [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) + [`HARD_RULES.md`](HARD_RULES.md). v2.5 **adds** five things: depth tiers (①), the Atlas (②), Trunk & Branches (③), the leverage Queue (④), and the codified assembly line (⑤).

## Consistency (per HARD_RULES §8)
- **Tiers vs. "cover every domain":** resolved — tiers set depth, not inclusion; a domain still counts as covered only when it yields grounded modules.
- **Atlas vs. anti-hoarding:** the Atlas indexes corpus *destined for processing*; it is a working index, not a trophy.
- **Trunk & Branches vs. "one book":** the single-book promise is kept for the Trunk (the AGI/ASI narrative); branches were never going to read as one line across all of science, and pretending otherwise was the old flow's break.
- **Just-in-time Atlas vs. "plan before building":** we scaffold the *system* fully but populate the *index* per-domain on demand — the leverage rule ([`HARD_RULES.md`](HARD_RULES.md) §1.4) applied to indexing itself.
