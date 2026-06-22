---
id: c-computation
sortkey: 0400
title: Computation — what a computer actually does
domains: [computer-science, computation, theory]
level: foundational
prereqs: [c-system]
provides: [computation, universality, stored-program, abstraction-layers, algorithm, complexity, uncomputability]
resources: [r-aima, r-essential-math-ai]
status: ready
reading_time: 9 min
rev: 1
created: 2026-06-22
updated: 2026-06-22
---

# Computation — what a computer *actually* does
*After this rung you'll know what a computer does at bottom (almost nothing — but unimaginably fast), why that's enough to do *everything*, and where the hard walls are: what's slow, what's impossible, and what no amount of AI can get past. This is the ground every AI system runs on.*

## Why this rung matters
You will spend your career deciding what to compute, on what hardware, at what cost. To direct that well you need the true shape of computation — not the magic-box story. The punchlines below (universality, abstraction layers, complexity, hard limits) are the reality checks that keep a founder from chasing the impossible or overpaying for the merely hard.

## The idea (start concrete)
Open up everything a computer does and you reach a shockingly short list. It can:
- **store** a bit (the storage **bit** — recall the *information* bit at [0300](0300_information-and-entropy.md); here it's just a switch that's 0 or 1),
- **move** bits from one place to another,
- do **tiny logic and arithmetic** on bits — AND, OR, NOT, add two numbers.

That's essentially it. A modern chip just does these **billions of times per second**, across billions of switches (transistors). Every video call, every game, this sentence, and every AI model is **layers of that, and nothing more**. The awe isn't in any single step — it's in the *scale and arrangement* (an emergent system behavior — [0200](0200_what-is-a-system.md)).

## The idea that makes it powerful: stored programs + universality
Two discoveries turned that tiny toolkit into the most flexible machine ever built.

**1. A program is just data (the stored-program idea).** Instructions and the data they work on are *both* bits living in the same memory. So a program can be stored, copied, changed — even **written by another program**. This is why software eats the world, and it's the seed of something you'll lean on constantly: **an AI model's "weights" are data, yet they act like a program** — a program *learned from examples* instead of written by hand (forward link: [0600](0600_what-it-means-to-learn.md), [1000](../20-machine-intelligence/)).

**2. Universality (Turing).** A simple enough machine — a "universal" one — can compute **anything that can be computed at all**, given enough time and memory. One machine, all possible programs. Your laptop and a giant datacenter differ in *speed and size*, not in *what is computable*. **[Established]** (Turing, 1936; the Church–Turing thesis — see [`PAPERS.md`](../../RESOURCES/PAPERS.md)).

> The combination is the whole game: a machine that can run *any* program, and programs that are *just data* you can generate and learn. That's why "intelligence as software you grow" is even thinkable.

## Abstraction layers — why you work near the top
Nobody builds an app by flipping transistors. Computing is a **stack of layers**, each hiding the mess below it:

```
transistors  →  logic gates  →  machine instructions  →  programming languages
             →  libraries/apps  →  AI models  →  you, directing in plain language
```

Each layer lets you think in bigger ideas and *forget* the layer beneath. You operate near the **top** — specifying intent, composing systems — and trust (but verify) the layers below. **This is the technical reason the "director, not implementer" strategy works:** the abstractions are real, so you can command outcomes without toggling bits. Knowing the stack *exists*, though, tells you where to look when a leak in a lower layer (a hardware limit, a numerical bug) breaks the illusion.

## Algorithms and cost (just the instinct)
An **algorithm** is a recipe: a finite list of steps that turns an input into an output. The thing a director must feel is **how the cost grows as the problem grows** — its **complexity**:
- **Cheap / scalable:** cost grows gently (e.g. *linearly* — twice the data, twice the time). You can throw scale at it.
- **Brutal / infeasible:** cost grows *explosively* (e.g. *exponentially* — each extra item doubles the work). At "exponential," even modest sizes become impossible for *any* computer, ever.

You don't need to analyze this by hand (delegate that). You need the reflex: *"Does this plan scale, or does it explode?"* A huge amount of AI is precisely the art of **replacing an explosive exact search with a cheap, learned approximation that's good enough** (chess engines, protein folding, language). Hold that pattern — it explains why "just learn it" so often beats "compute it exactly."

## The hard walls (the reality a founder must respect)
Computation has limits that **no algorithm, no AI, no budget** escapes:
- **Some problems are uncomputable.** There are precise questions *no* program can ever answer in general — the classic is the **halting problem** (you can't build a general program that decides whether any given program will eventually stop). **[Established]** (Turing).
- **Some are computable but intractable** — solvable in principle, but the time/energy needed dwarfs the universe. "Possible on paper" ≠ "possible in practice."
- **Physical floors.** Computation costs energy and time; there are thermodynamic limits to how cheaply a bit can be erased (link to [1500 Energy](../40-compute-and-physical/)). Intelligence — natural or artificial — is *bounded* by these.

These walls matter enormously for the AGI question: any mind, including a superintelligence, runs on physics and computation and **cannot step outside these limits**. Smarter doesn't mean *omnipotent*; it means *better within the bounds*. **[Established]** that the limits exist; **[Contested]** how close to them today's systems are, and how much room is left.

## How a director uses this
- **Sort problems into cheap / hard / impossible** before committing resources. The most expensive mistakes are funding the intractable or the uncomputable.
- **Reach for learned approximation** when exact computation explodes — that instinct is the core of modern AI strategy (and connects straight to the *Bitter Lesson* you'll meet at [0600](0600_what-it-means-to-learn.md)).
- **Respect the stack.** When something behaves strangely, suspect a leaky lower layer (precision, memory, hardware) — knowing the layers exist tells you where to send the AI to dig.
- **What you delegate:** writing the algorithms and the complexity analysis (the AI does this well). **What you own:** classifying feasibility, choosing exact-vs-learned, and budgeting against the walls.

## Connections
- **Stands on:** [0200 What is a system?](0200_what-is-a-system.md) (computing power is emergent from simple parts) and the *bit* from [0300](0300_information-and-entropy.md).
- **Leads to:** linear algebra & why-GPUs ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)), learning as "grown software" ([0600](0600_what-it-means-to-learn.md)), compute & chips ([1400](../40-compute-and-physical/)), energy limits ([1500](../40-compute-and-physical/)).
- **Contested?** Universality, uncomputability, complexity — **[Established]**. How near current AI sits to the physical/practical limits — **[Contested]**.

## Proof-of-learning *(do one, from memory)*
1. Name the three primitive things a computer really does — then explain how "a program is just data" follows from them.
2. What does **universality** say is the difference between your phone and a supercomputer? What's the *same*?
3. Give one problem that's **impossible** and one that's merely **intractable**, and say why the distinction matters when you're spending a budget.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-22)` — created.

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md).*
