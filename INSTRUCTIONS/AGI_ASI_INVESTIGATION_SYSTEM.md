# AGI / ASI INVESTIGATION SYSTEM
**The map of possible paths to advanced machine intelligence — and how we judge them.** This is a *framework for investigating*, not a set of answers. It holds many competing ideas at once and weighs them honestly.

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 1.0 · Status: Living document · Last updated: 2026-06-20`

---

## 1. First, what are we even talking about?

The words are slippery. We keep three meanings separate:

- **AGI** — one system that handles *many different* problem types about as well as a capable human, including problems it wasn't specifically trained for.
- **ASI** — a system *far beyond* the best humans at essentially everything that matters.
- **"Advanced machine intelligence"** — a deliberately looser term for big capability jumps that don't fit either label cleanly.

> **Honest warning:** "AGI" is not a precise target like "boiling point of water." It's more like the word "flight." There are many kinds of flight (insect, bird, balloon, jet, rocket). Asking "what is *required* for flight?" has no single answer — it depends which kind. We treat AGI the same way: probably many forms, not one finish line. We hold the definition itself as an **open question**, not a settled fact.

---

## 2. The plausible paths (held side by side, none assumed correct)

We do **not** assume AGI comes from LLMs, or RL, or neuroscience, or any one field. We track multiple paths and keep score.

| # | Path | One-line idea | Biggest strength | Biggest doubt |
|---|---|---|---|---|
| P1 | **Scale current methods** | Keep making today's deep-learning systems bigger, with more data/compute. | Has produced surprising, real jumps. | May hit walls (data, energy, reasoning, reliability) that scale alone won't cross. |
| P2 | **Scale + new ingredients** | Today's systems *plus* missing pieces (memory, planning, tools, agents, world-models). | Targets known gaps directly. | We don't yet know if the gaps close or just move. |
| P3 | **Neuroscience-inspired** | Copy principles of how brains learn (not the exact wiring). | The brain is the one proof general intelligence is possible. | We don't understand the brain well enough yet; copying the wrong level may not help. |
| P4 | **Whole-brain emulation** | Scan and simulate a real brain in enough detail. | If it worked, it would *guarantee* general intelligence. | Needs scanning + compute + neuroscience far beyond today; maybe decades+. |
| P5 | **Neurosymbolic / hybrid** | Combine pattern-learning (neural) with logic/symbols/reasoning. | Pattern *and* precise reasoning are both needed; pure versions of each have known weaknesses. | Hard to combine cleanly; long history of partial success. |
| P6 | **Reinforcement learning / agents** | Intelligence emerges from acting, getting feedback, and improving in rich environments. | How animals and humans actually learn; ties intelligence to *doing*. | Sample-hungry; needs rich worlds; reward design is hard and dangerous. |
| P7 | **A new paradigm** | The real path is an idea not yet invented. | Most past leaps came from *new* ideas, not scaling old ones. | Unpredictable by definition; can't be planned, only prepared for. |

These are not exclusive. The truth may be a **blend** (e.g., scaled agents with symbolic reasoning and brain-inspired memory). The point is to keep all paths alive and update their scores as evidence comes in.

> **Who's actually taking each path** (real labs, startups, and their bets — OpenAI, Anthropic, DeepMind, xAI, SSI, AMI Labs/JEPA, DeepSeek, etc.): see the live map in [`../RESOURCES/LANDSCAPE.md`](../RESOURCES/LANDSCAPE.md). *(That file is a fast-aging snapshot; this file is the durable framework.)*

---

## 3. How we judge each path (the scorecard)

For every path, we keep an updatable estimate of:

- **Feasibility** — could it work *in principle*? (vs. some hidden impossibility)
- **Evidence so far** — what real results support or hurt it?
- **Dependencies** — what else must exist first? (compute, data, theory, energy, breakthroughs)
- **Bottlenecks** — the specific thing most likely to block it.
- **Timeline (with huge error bars)** — and the *reference class* of similar past predictions.
- **Risks** — what goes wrong if it works, *and* if it fails.
- **Unknowns** — the honest "we don't know" list.
- **Confidence tag** — Established / Likely / Contested / Speculative / Unknown (from [`PRINCIPLES.md`](PRINCIPLES.md)).

We never give a single number and call it truth. We give a range, the reasoning, and the strongest opposing view.

---

## 4. The cross-cutting bottlenecks (true for almost every path)

Whatever the path, these constraints keep appearing. Each deserves its own deep study (and likely its own domain):

- **Compute** — raw processing power; tied to chips, money, and physics.
- **Chips & fabrication** — a *very* small number of companies and machines (e.g., advanced lithography) make the best chips. A real-world chokepoint.
- **Energy** — thinking costs power; data centers are bumping into grid and physics limits. The **thermodynamics of computation** sets hard floors.
- **Data** — quality, quantity, ownership, and whether we're running out of the good kind.
- **Algorithms / theory** — we may be missing core ideas about *how learning and reasoning should work at all*.
- **Reliability & alignment** — a system that's powerful but uncontrollable or untrustworthy is not a solution; it's a new problem. (See risk note below.)
- **Money & economics** — who can afford the next jump, and what they expect back.
- **Talent** — a thin layer of people who can push the frontier.

A path can be theoretically fine and still die on a single bottleneck. We track the bottlenecks as carefully as the paths.

---

## 5. The "what would change our mind?" rule

For each path, we write down **in advance** what evidence would raise or lower our estimate. Example: "If scaling another 10× brings no improvement in reasoning reliability, lower P1." This keeps us honest — it lets reality *correct* us instead of letting us defend a favorite.

---

## 6. The danger we never ignore

Studying *how* to build powerful intelligence is inseparable from *whether and how* it stays safe and controllable (alignment), and *who controls it* (governance, geopolitics). These are not a side topic — a path that produces uncontrollable or catastrophically misused power has not "succeeded." Safety, control, and governance are part of the success criteria, not optional extras.

---

## 7. What this document is *not*

It is **not** a prediction of when AGI arrives or which path wins. Anyone certain about that is selling something. This is a *living scoreboard* that gets less wrong over time as evidence comes in. Its job is to make our uncertainty **organized and honest**, not to fake confidence.

The questions it can't yet answer go to [`OPEN_QUESTIONS_SYSTEM.md`](OPEN_QUESTIONS_SYSTEM.md).
