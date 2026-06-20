# CONCEPT REGISTRY — one home per concept
**The no-redundancy enforcer.** Before explaining *anything*, check here. If a concept is listed, **link to its home — don't re-explain**. If it's not, explain it once in the right module, then add it here.

`Status: Living index · System Version: 1.2 · Last updated: 2026-06-20`

> Rule (from [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §5): every concept has exactly **one canonical module**, which lives in one **domain folder**. This table maps **concept → home module (`id` + folder) → one-line pointer**. It does *not* hold the explanation itself (that would be repetition) — it points to it. (Folders for planned modules: see [`00_MAP.md`](00_MAP.md).)

---

| Concept | Canonical home (`id` → file) | Status | One-line pointer |
|---|---|---|---|
| intelligence (working definition) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Doing the *right thing* across many situations to reach goals. |
| generality (general vs narrow) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Many problem types vs one; the core of "G" in AGI. |
| "AGI is many forms" (flight analogy) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Probably a family of forms, not one finish line. |
| system | `c-system` → 0200 | ⬜ | Parts + relationships that produce behavior. *(planned)* |
| feedback loop | `c-feedback` → 0250 | ⬜ | Output looping back to change input. *(planned)* |
| entropy / information | `c-entropy` → 0300 | ⬜ | Surprise, measured; the unit is the bit. *(planned)* |
| computation | `c-computation` → 0400 | ⬜ | What a machine can mechanically do. *(planned)* |
| probability / uncertainty | `c-probability` → 0500 | ⬜ | Reasoning with what we don't fully know. *(planned)* |
| learning (in a system) | `c-learning` → 0600 | ⬜ | Improving from experience/data. *(planned)* |

---

## How to use this table
- **Writing a new module?** For each idea you mention, find its row. Listed → write *"(see [home])"*. Missing → this idea needs a home; either it belongs in the module you're writing (add the row, pointing here) or it needs its own module (insert one — [`LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §8).
- **`id` is stable** even if the file is renumbered, so these pointers survive reordering.
- Rows are added the moment a concept gets its canonical explanation — never before (no empty promises), but planned homes may be pre-listed as ⬜ to reserve the slot.
