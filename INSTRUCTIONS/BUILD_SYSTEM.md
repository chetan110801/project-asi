# BUILD SYSTEM
**The second engine: building toward AGI/ASI, step by step.** Understanding is one half of the project; *making things* is the other. This document defines how we build, who does what, and how building and learning feed each other.

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 1.2 (new in v1.2) · Status: Living document · Last updated: 2026-06-20`

> Builds on, doesn't repeat: progress/artifacts are tracked by [`MILESTONE_AND_SHOWCASE_SYSTEM.md`](MILESTONE_AND_SHOWCASE_SYSTEM.md); prerequisites come from the ladder in [`LEARNING_ARCHITECTURE.md`](LEARNING_ARCHITECTURE.md). This doc adds only what's specific to *building*.

---

## 1. Why build at all (not just read)

Three reasons building is half the project, not a hobby:
1. **Building is the deepest test of understanding.** You can fool yourself reading; you can't fool a program that won't run or a model that won't learn.
2. **It's the path to your North Star** — confidence → career / startup / serious research. That confidence comes from *having built things*, not just knowing about them.
3. **It touches reality** — the project's biggest weakness is reviewing itself (see [`REVIEWS/AUDIT_2026-06-20_v1.0.md`](../REVIEWS/AUDIT_2026-06-20_v1.0.md)). A build that works or fails is feedback no amount of self-review can fake.

---

## 2. The division of labor (this is the optimal part)

We split work by who is best at it — that's the "be optimal" rule you set:

| I (the AI) do | You do |
|---|---|
| Write the code, configs, scripts, boilerplate | Decide direction and goals |
| Run experiments, debug, handle tooling | Review results and ask "why?" |
| Explain *every* step in simple language | Build understanding from the explanations |
| Produce the showable artifact | Guide, choose, and learn the *why* behind each choice |
| Surface trade-offs and options | Make the calls |

> **Key:** I do the mechanical heavy lifting so your time goes to *understanding and steering*, not fighting tools. But every build is also a **lesson** — I narrate what I'm doing and why, so you could do it yourself next time. Building without learning is just outsourcing; we don't do that.

---

## 3. The build ladder (small → ambitious)

Like the learning ladder, builds go from tiny and safe to large and real. Rough rungs:

1. **Toy reproductions** — rebuild a classic idea in the smallest form (e.g., a tiny neural net from scratch, a 1-page learning algorithm). *Goal: see the mechanism with your own eyes.*
2. **Modifications** — change a toy and predict what happens, then check. *Goal: turn understanding into intuition.*
3. **Mini-systems** — combine a few pieces into something that does a real (small) task. *Goal: systems thinking, not just parts.*
4. **Original experiments** — test a question of *ours* that doesn't have a textbook answer. *Goal: research taste.*
5. **Serious projects** — the kind that could become a portfolio, paper, or startup seed. *Goal: the North Star.*

Each rung's target is set dynamically (per [`MILESTONE_AND_SHOWCASE_SYSTEM.md`](MILESTONE_AND_SHOWCASE_SYSTEM.md) §4) — reach by real effort, never trivial, never crushing.

---

## 4. Every build is grounded in the learning ladder

A build can only use concepts you've climbed to. So:
- Before a build, we list its **prerequisite modules** (from the learning ladder). Gaps become new learning modules first (inserted dynamically).
- After a build, the lessons it taught can *create* new modules or sharpen old ones — building feeds the ladder back.

This two-way link (learn → build → learn) is the project's main loop made concrete.

---

## 5. Where builds live

When building starts, code and experiments live under `BUILDS/` (created on first use), one folder per project, each with:
- a short `README` (goal, prerequisites, what was learned),
- the code/notebooks,
- a results/notes file,
- a link to the **showable artifact** on the `SHOWCASE/` shelf and any **prediction** logged in the Prediction Ledger.

Reproducibility is a default: another person (or AI) should be able to re-run and understand it.

---

## 6. Honesty about limits

- **Compute & access:** big AI builds need hardware, data, and money we may not have. We scale ambition to what's actually runnable, and say so plainly — a working tiny thing beats a grand thing that never runs.
- **I make mistakes in code too:** builds get the same [`QUALITY_CONTROL_SYSTEM.md`](QUALITY_CONTROL_SYSTEM.md) treatment (test it, don't trust it; verify, don't assume).
- **Frontier ≠ toy:** rebuilding a small version teaches the *idea*, but the real frontier has engineering and scale challenges a toy hides. We'll name that gap whenever it matters, not pretend the toy is the whole story.
