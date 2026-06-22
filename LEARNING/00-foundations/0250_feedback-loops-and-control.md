---
id: c-feedback
sortkey: 0250
title: Feedback loops & control
domains: [systems-thinking, control-theory, cybernetics]
level: foundational
prereqs: [c-system]
provides: [feedback-loop, negative-feedback, positive-feedback, control, setpoint-error]
resources: [r-tsironis-complex, r-sutton-barto]
status: ready
reading_time: 8 min
rev: 1
created: 2026-06-22
updated: 2026-06-22
---

# Feedback loops & control
*After this rung you'll recognize the single most important kind of relationship inside a system — a **loop** where output bends back to change input — and you'll see that "learning," "agency," "stability," and even "intelligence explosion" are all this one idea wearing different clothes.*

## Why this rung matters
Almost everything that *steers itself* toward a goal — a thermostat, a body, a guided missile, a learning algorithm, a company, an economy — runs on feedback. Once you can see loops, you can see *why* systems are stable or runaway, and *where* to intervene. For an AI builder this is foundational: **training is a loop, agency is a loop, and the scariest AGI scenarios are loops.**

## The idea (start concrete)
A **feedback loop** is when a system's **output loops back to change its own input**.

Picture a thermostat. It compares the room (say 18°) to a **setpoint** (21°). The gap — the **error** — switches the heater on. The room warms, the error shrinks, and at 21° it shuts off. Room cools, error grows, heater kicks back on. Round and round. The loop *holds the room at the goal* with no one watching.

That's the skeleton of all control: **goal → measure → compare → correct → repeat.**

## The two flavors (this split explains a lot)

**Negative (balancing) feedback → stability.** The loop *counteracts* change and pulls toward a target.
- Thermostat, cruise control, steering a car, your body holding 37°, a market correcting an over-priced stock.
- Effect: self-correcting, goal-seeking, stable. This is what makes a system *reliable*.

**Positive (reinforcing) feedback → explosive growth or collapse.** The loop *amplifies* change — more leads to more.
- Compound interest, a viral post, a microphone next to its speaker (the squeal), a bank run, an arms race, a fire.
- Effect: runaway. Tiny starts become huge, fast. Nothing grows forever in the real world, so positive loops eventually hit a limit (or break the system).

> Same machinery, opposite character. **Negative loops keep things where you want them; positive loops take things somewhere new — fast, for better or worse.**

## Two complications a director must respect
- **Delay breeds oscillation.** If feedback arrives late, you over-correct. The classic example is a shower with slow pipes: you crank the heat, nothing happens, you crank more — then it scalds. Loops with **lag overshoot and wobble**. Many real AI failures (and policy failures) are just delayed feedback.
- **Loops nest and tangle.** Real systems are webs of loops fighting and reinforcing each other. That tangle is exactly what makes complex systems hard to predict (the "complex dynamical systems" view — see resources).

## Why this is everywhere in AI
This one idea is the backbone of the machine-intelligence chapters, so plant it now:
- **Learning is a negative feedback loop.** Predict → measure the **error** → adjust to shrink it → repeat. That's training in one line (you'll meet it as "gradient descent" at [1000](../20-machine-intelligence/) and learning itself at [0600](0600_what-it-means-to-learn.md)).
- **An agent is a control loop.** Sense the world → act → see the result → adjust. Reinforcement learning is literally control by reward ([1200](../20-machine-intelligence/); reward as the feedback signal — see `r-sutton-barto`).
- **Alignment is a control problem.** "How do we keep a powerful system locked onto the goal we *meant*?" is a question about feedback, setpoints, and what happens when the system optimizes the *measured* signal instead of the real intent (**reward hacking** — the loop succeeds while the goal fails). Picked up at [1900](../60-frontier/).
- **The "intelligence explosion" is a positive feedback loop.** AI that improves AI, which improves faster still — recursive self-improvement. Whether that loop is real and how steep it is, is a central open question. **[Contested / Speculative]**

## How a director uses this
- **Design the loop, not just the parts.** Ask of any system: *What's the goal (setpoint)? What's measured? How does error feed back? How fast?* Most behavior — good and bad — falls out of those answers.
- **Hunt the loop when things break.** Runaway costs, drift, instability, gaming the metric — these are loop pathologies, not part failures. Fix the wiring.
- **Mind the signal you choose.** A system optimizes *exactly* the feedback you give it, not what you wished you'd given it. Choosing the right feedback signal is one of the highest-leverage — and most dangerous — decisions you'll make.
- **What you delegate:** the math of controllers and optimizers (the AI builds them). **What you own:** what the loop is *for*, what it measures, and whether it's stable.

## Connections
- **Stands on:** [0200 What is a system?](0200_what-is-a-system.md) — a loop is the key *relationship* between parts.
- **Leads to:** [0600 Learning](0600_what-it-means-to-learn.md) (learning = an error-reducing loop), RL & agents ([1200](../20-machine-intelligence/)), alignment ([1900](../60-frontier/)), and the intelligence-explosion debate ([1800](../60-frontier/)).
- **Contested?** Feedback/control basics — **[Established]**. Recursive self-improvement / fast takeoff — **[Contested → Speculative]**.

## Proof-of-learning *(do one, from memory)*
1. Give one **negative** and one **positive** feedback loop from your own life, and say what each does to stability.
2. Why does *delay* in a loop cause overshoot? Use the shower example or your own.
3. In one sentence, explain why "the AI optimizes the signal you gave it, not the goal you meant" is a feedback problem.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-22)` — created.

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md).*
