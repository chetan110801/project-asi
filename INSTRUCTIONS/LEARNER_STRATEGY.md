# LEARNER STRATEGY
**How *this specific learner* should learn — and how that shapes every module I write.** This is the "be optimal" rule turned into a concrete teaching strategy.

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 1.6 (new in v1.6; §3 deciding-test refined in v1.9; §7b EXHAUSTIVE depth standard added v2.3) · Status: Living document · Last updated: 2026-06-27`

---

## 1. The learner, precisely
- Smart, ambitious, **ESL** (simple language always), studies **daily**.
- Aim: in roughly **6–12 months**, be **world-class enough to found something like DeepMind** — i.e., to *lead and build* toward AGI/ASI, not to be a rank-and-file researcher.
- Model of work: **entrepreneur (you) + employee (me)**. You set direction and judge; I do the heavy technical labor and explain it.

## 2. The core strategy: learn to *direct and decide*, not to *implement*

> **Don't spend your scarce time learning what the AI can already do for you.** Spend it on what makes you a great *director* of that AI and a great *founder*.

**Skip the grind** (I handle these on demand; you don't memorize them):
- hand-deriving algorithms, coding standard models from scratch, API/framework syntax, proofs for their own sake, rote math you'd never do by hand.

**Master instead** (this is where your hours go):
- **Concepts & intuition** — what each idea *is*, *why* it works, *when* it wins or fails (high-level *and* enough low-level intuition to smell when something's wrong).
- **Trade-offs & judgment** — choosing between approaches; reading the landscape.
- **Orchestration** — *what* to ask the AI for, *when*, and *how*; how to specify, verify, and combine its outputs.
- **System design** — how the pieces fit into something that works end-to-end.
- **Build-by-directing** — getting real things built (me coding, you steering), so understanding becomes capability.

## 3. The honest correction (the one non-negotiable)
"Let the AI do it" has a limit: **you cannot direct or judge what you don't understand at all.** A founder who understands *nothing* can't tell good work from broken work, can't make architecture calls, and gets fooled. So:

> We cut **implementation depth**, never **conceptual depth**. You will understand ideas deeply enough to *lead* — just not waste time on what's automatable.

This is the difference between **understanding-to-implement** (skip) and **understanding-to-direct-and-decide** (master).

**The deciding test (the learner's own words, v1.9):** the question is *not* "can AI already do this?" — AI can do plenty you will still need to understand. The question is **"will I have to *rely on* this — understand it — to build and direct AI?"**
- **Yes → learn it, even though AI can do it for you.** Understanding you depend on to *originate and judge* the work always counts.
- **Pure execution skill whose only payoff is proving you can do it — coding/programming first of all, and similar mechanical work → skip.** That is an **"assumed achievement," not a real one**: it re-proves a skill a tool already covers and does *not* advance the purpose (building AGI/ASI).

So **real achievement = understanding deep enough to originate and judge**; **assumed achievement = demonstrating a skill the AI already provides.** We optimize every hour for the first.

## 4. World-class, minus the unnecessary
"World-class" here = **clarity and judgment at the frontier**, not encyclopedic technical recall. High-level abstractions *and* key low-level mechanisms — taught for *insight*, with the grind delegated.

## 5. End-to-end: knowledge to actually *build* it
The curriculum doesn't stop at "understand intelligence." It includes the **founder's build-map**:
- **What it takes** to build toward AGI/ASI: compute, data, money, time, the real bottlenecks.
- **The team** you'd need if you can't build alone — *which expert roles in which fields* (e.g., ML research, systems/infra, hardware, data, product, safety), and how to recognize and work with them.
- **The practical build track** — real projects (agents, RL, etc.), small → serious. (See [`BUILD_SYSTEM.md`](BUILD_SYSTEM.md).)

## 6. Theory **and** practice, always
- **Theory** — for understanding: abstractions, high-level pictures, and the load-bearing low-level mechanisms.
- **Practice** — for capability: building real things by directing me.
Every domain on the ladder carries both; a concept isn't "done" until you can *use* it (or direct its use), not just recite it.

## 7. What this means for how I write each module
Modules are written for a **director-founder**, not an exam-taker:
- lead with intuition, analogy, and "why it matters / when you'd use it";
- include "**how you'd get this built with the AI**" where relevant;
- **render the full conceptual depth — do NOT collapse it.** *(changed v2.3, 2026-06-27 — learner asked for the fuller, exhaustive treatment "even at the cost of length.")* See §7b.
- always pass the freshness/quality checklist in [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §13.

## 7b. The depth standard: EXHAUSTIVE on the conceptual axis *(added v2.3, 2026-06-27)*
The learner wants modules at the depth of their **"hy" knowledge system** — *miss nothing, grounded in real sources* — and explicitly accepts the length. This does **not** reverse §2–§3; it **applies** them ("cut implementation depth, never conceptual depth"). The two axes stay split:
- **Conceptual / understanding axis → EXHAUSTIVE (never cut, now never collapsed).** For every topic on the ladder, render **every idea, mechanism, argument, distinction, key result, example, trade-off, failure mode, and live debate** the **source corpus** contains that bears on understanding-to-direct. Ground each claim in a real source ([`../RESOURCES/corpus/`](../RESOURCES/corpus/)); quotes verbatim. Nothing important is summarized away or hidden behind a "go deeper" pointer — it is written out, in simple language, in full.
- **Implementation / execution axis → still delegated (§2).** Modules are *not* coding tutorials and don't reproduce every formal proof step-by-step. Render the math/mechanism as far as needed for **complete insight** (further than before), and leave the actual coding / rote derivation to "you'd direct the AI to do X."
- **Consequence — modules get long, and big topics SPLIT.** Expect ~hy scale (multiple thousands of words). When a topic is large, **split it into several grounded sub-rungs** via the numbering gaps ([`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md) §8) — e.g. "LLMs" becomes a cluster of rungs — each at full hy depth, rather than one shallow file. **Coverage and depth beat brevity** (brevity is last), exactly as in the hy standard.
- **Reader is still ESL** (§1): full depth, but **simple sentence shapes (8-year-old bar) + mandatory inline glossing.** *(ADOPTED v2.4, 2026-06-27 — learner asked for it: every medium-to-advanced word / phrase / collocation / idiom / technical term gets its **general + in-context meaning in very simple words, in brackets** beside it. Binding rules: [`HARD_RULES.md`](HARD_RULES.md) §6.)*
