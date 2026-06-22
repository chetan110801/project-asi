# CONCEPT REGISTRY — one home per concept
**The no-redundancy enforcer.** Before explaining *anything*, check here. If a concept is listed, **link to its home — don't re-explain**. If it's not, explain it once in the right module, then add it here.

`Status: Living index · System Version: 2.0 · Last updated: 2026-06-22`

> Rule (from [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §5): every concept has exactly **one canonical module**, which lives in one **domain folder**. This table maps **concept → home module (`id` + folder) → one-line pointer**. It does *not* hold the explanation itself (that would be repetition) — it points to it. (Folders for planned modules: see [`00_MAP.md`](00_MAP.md).)

---

| Concept | Canonical home (`id` → file) | Status | One-line pointer |
|---|---|---|---|
| intelligence (working definition) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Doing the *right thing* across many situations to reach goals. |
| generality (general vs narrow) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Many problem types vs one; the core of "G" in AGI. |
| "AGI is many forms" (flight analogy) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Probably a family of forms, not one finish line. |
| system | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Parts + relationships that produce behavior. |
| emergence | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | The whole does what no part can (e.g. intelligence). |
| reductionism vs holism | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Zoom-in to fix parts; zoom-out to see behavior. |
| feedback loop | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Output looping back to change input. |
| negative / positive feedback | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Balancing → stability; reinforcing → runaway. |
| control (setpoint / error) | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Goal → measure → correct → repeat. |
| entropy / information / bit | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Surprise, measured; the unit is the bit. |
| compression (≈ understanding) | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Predict well → remove entropy → compress. |
| vector / embedding | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | A point in a space of meaning; nearness = similarity. |
| matrix (as transformation) | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | An action that moves a whole space at once. |
| dot product / similarity | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | Alignment of two vectors; the engine of retrieval/attention. |
| computation | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | What a machine can mechanically do. |
| universality / stored-program | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | One machine runs any program; a program is just data. |
| algorithm / complexity | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | A recipe; how its cost grows (cheap vs explosive). |
| uncomputability / hard limits | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | Some problems no machine can ever solve. |
| probability / uncertainty | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Reasoning with what we don't fully know. |
| conditional probability | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | P(A given B) — odds after evidence. |
| Bayes' rule / base rate | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Update belief = prior × likelihood; mind the base rate. |
| expected value | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Probability-weighted average; how to decide under risk. |
| distribution / fat tails | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | The full spread; rare extremes can dominate. |
| learning (in a system) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Improving from experience by an error-reducing loop. |
| generalization vs overfitting | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Transfer to unseen cases vs memorizing the training set. |
| supervised / unsupervised / RL / self-supervised | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Four flavors = same loop, different feedback. |
| inductive bias / no free lunch | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Can't learn without assumptions; none is best at everything. |
| objective function (Goodhart) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | The system gets what you measure, not what you meant. |

---

## How to use this table
- **Writing a new module?** For each idea you mention, find its row. Listed → write *"(see [home])"*. Missing → this idea needs a home; either it belongs in the module you're writing (add the row, pointing here) or it needs its own module (insert one — [`LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §8).
- **`id` is stable** even if the file is renumbered, so these pointers survive reordering.
- Rows are added the moment a concept gets its canonical explanation — never before (no empty promises), but planned homes may be pre-listed as ⬜ to reserve the slot.
