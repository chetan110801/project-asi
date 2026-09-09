---
id: c-shared-core
sortkey: 6000
title: What actually stays — the small permanent core, and everything you can look up
domains: [method, entry-ramps, resources]
level: core
prereqs: []
provides: [judgement-floor, three-piles-rule, once-rule, research-practice, compute-budget]
status: ready
reading_time: 12 min
rev: 3
created: 2026-09-09
updated: 2026-09-09
---

# What actually stays — the small permanent core, and everything you can look up

*You have learned maths, ML and DL before, forgotten them, and learned them again. That loop is not a discipline problem, it is a design problem: you were trying to retain things that were never worth retaining. This page keeps only what genuinely stays, and gives you permission to look up the rest — permanently.*

> **You are here:** the first page of **⑥ Entry ramps**. The [map](../APPROACHES_TO_AGI.md) says what the eleven bets are; [the plan](../THE_PLAN.md) says why doing beats reading. This group is the **resources and route into each bet** — one ramp per approach. This page is the short thing they all share. It is deliberately not a curriculum.

> **Where the facts come from:** a live web check on **2026-09-09** — Sutton & Barto's edition status, and current free-GPU quotas on Kaggle and Colab.

---

## In one minute

**Your prerequisites are already handled.** You are revising maths, ML, deep learning, NLP and LLM internals for data-science and MLE interviews. That is the trunk, and it will be fresher than any reading plan I could write. **Exactly one thing your interview prep does not cover is needed for the approaches you care about: reinforcement learning.** That is the only prerequisite on this page.

Everything else here is not curriculum. It is a sorting rule, so that the forget-and-relearn loop stops costing you anything:

- **🧠 Twenty concepts** you hold permanently, because each one detects a *specific kind of wrongness*. Without them you cannot tell a good result from a fake one — and that is the one thing you cannot outsource to me.
- **📖 Everything else** — proofs, formulas, algorithm variants, APIs — you look up, forever, without guilt.
- **🤖 The mechanical work** — implementation, algebra, reading papers with you, plots — you hand to me. That is what I am for.

**The rule that divides them: delegate execution, never delegate judgement.**

---

## Part 1 — the one prerequisite

| | |
|---|---|
| **Already covered by your interview prep** | SQL, DSA, pandas/NumPy, classical ML, deep learning basics, NLP, LLM internals, AI engineering, MLOps. Revise for the interviews; that revision *is* the trunk maintenance. Do not schedule a second pass for this project. |
| 🔴 **Not covered, and needed** | **Reinforcement learning.** It is load-bearing for AP2, AP3, AP4, AP9 and AP10 — five of eleven bets, including the ones you are drawn to. |
| **The concrete thing** | **Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.** — free at `incompleteideas.net`. *(Checked 2026-09-09: still the standard, no 3rd edition.)* **Chapters 1–6 and 13.** That is ~200 pages, not the whole book. |
| **Then, on demand only** | **Berkeley CS 185/285 (Spring 2026, Levine)** — free lectures — for the deep-RL half Sutton & Barto predates. Pull it when a paper you are reading needs it, not before. |
| **Optional, one gap worth knowing about** | **Information theory** — entropy, mutual information, description length. Not on your interview list and not in most ML courses. It matters only if you go near compression-as-intelligence arguments *(AP8, AP5)*. **MacKay, Ch. 1–6**, free. Two weeks. Skip until it bites. |

::: key
**Why this list is so short.** You already said the failure mode: you learn maths, forget it, relearn it. Adding a fourth pass would not fix that — it would repeat it. Prerequisites are for looking up. The only one named here is named because there is no way to look up an intuition for the TD error while reading a paper that assumes it.
:::

---

## Part 2 — the judgement floor

Twenty concepts. Not twenty chapters — twenty things you can explain out loud in two minutes each, without notes. Each earns its place by one test: **does not having it hide a particular kind of wrongness from you?**

| # | Concept | The wrongness it lets you detect |
|---|---|---|
| 1 | Gradient descent; non-convex loss surfaces | "It didn't converge" vs "it converged somewhere useless" |
| 2 | Overfitting and the generalisation gap | A beautiful training curve that means nothing |
| 3 | Train / validation / test discipline, and **leakage** | The most common way a result is silently fake |
| 4 | Bias–variance and model capacity | Blaming the data when the model was too small, or the reverse |
| 5 | Maximum likelihood — that most loss functions *are* one | Treating a loss choice as arbitrary when it is a claim about a distribution |
| 6 | **KL divergence** — what it measures | Why RLHF needs a leash; why a VAE has that second term |
| 7 | Entropy and compression | Whether "compression is understanding" is argument or decoration |
| 8 | A matrix as a linear map; what a latent space *is* | Slogans about "abstract representations" that never cash out |
| 9 | Softmax; what attention actually computes | Architecture claims that are really re-parameterisations |
| 10 | Autoregressive next-token prediction, and its limits | What a language model structurally can and cannot represent |
| 11 | Scaling laws — the curve's shape, "compute-optimal" | Extrapolations that quietly leave the fitted range |
| 12 | The `C ≈ 6ND` budget identity | Whether a proposed experiment is affordable — in seconds |
| 13 | Pre-training vs post-training (SFT / RLHF / RLVR) | Which stage a claimed capability actually came from |
| 14 | Reward, return, value, and the **TD error** | Nearly every RL paper's method section |
| 15 | Policy-based vs value-based; actor–critic | The fork under every algorithm name you will meet |
| 16 | Exploration vs exploitation | Why an agent plateaus without being broken |
| 17 | Credit assignment | The real problem hiding behind "it learns from experience" |
| 18 | **Goodhart / benchmark contamination** | A number going up while the thing gets no better — the field's most common illusion |
| 19 | Sample efficiency vs asymptotic performance | Comparisons that are not comparisons |
| 20 | Inductive bias | That an architecture choice is a claim about the world, not a detail |

::: note
**You already hold roughly half of these** from the eleven approach pages you have read — items 9–13 and 17–20 are covered there conceptually. Items 14–17 arrive with Sutton & Barto. That leaves a handful, and they are the ones your interview revision covers anyway. **This is not a study plan. It is a checklist to notice gaps against.**
:::

---

## Part 3 — what you are allowed to forget

Permanently, deliberately, without guilt: **every proof** · **every closed form and exact formula** *(nobody recalls the Adam update; everyone knows what Adam does and when it misbehaves)* · **algorithm variants** *(know the category, forget which of six added which term)* · **library syntax and APIs** *(pure delegate — this is what I am for)* · **hyperparameter defaults** · **history and lineage**, except where a mistake is instructive.

### The once rule

Four things you do **exactly once**. Then let the details go — the residue is what stays, and reading cannot produce it.

| Do once | What survives after you forget the details |
|---|---|
| Derive backpropagation by hand for a two-layer network | Gradients stop being magic |
| Build a transformer from scratch *(Karpathy, Zero to Hero — free)* | Attention stops being a diagram; you know what each part costs |
| Implement one RL algorithm end to end *(OpenAI Spinning Up — free)* | You know what "it's just PPO" actually involves |
| Run one experiment that fails for a boring reason | The permanent instinct to check the boring reasons first |

::: key
**This is the answer to your forgetting problem.** You do not remember what you read; you remember what you used. So the floor is kept alive by *use* — every approach ramp in this group ends with an experiment that exercises it — not by revision. Anything you forget that never came back was correctly forgotten.
:::

---

## Part 4 — research practice, and your compute

The one thing your interview prep genuinely does not touch, and the only skill on this page that compounds.

**Reading papers.** Three passes. **One**, five minutes: title, abstract, intro, conclusion, figures — decide whether to continue. **Two**, an hour: full read, skip proofs, interrogate the experimental setup and the tables. **Three**, only for papers you will build on: reconstruct it as if you were the author, and find what they did not check.

> **How to use me on this properly.** Do pass one yourself, always — the skill is deciding what deserves pass two, and that skill is judgement, so it cannot be delegated. Then hand me the paper and ask for the parts you got stuck on. Handing me a paper cold trains nothing; handing me a paper *after* deciding it matters trains everything.

**Keeping a lab notebook.** One file per experiment: the question, the setup, the exact command, the result, and what you now believe that you did not believe before. Change one variable at a time.

**Writing it up, especially when nothing happened.** A clean negative result is a real artifact and usually more informative than a positive one. It is also the thing you can show a lab.

**Your compute** *(checked 2026-09-09)*:

| Where | What you get | Notes |
|---|---|---|
| **Kaggle Notebooks** | ~**30 GPU-hours/week**, guaranteed, P100/T4 (16 GB), ~12h session cap | Predictable and fixed. Also where ARC Prize runs. **Start here.** |
| **Google Colab free** | ~15–30 GPU-hours/week on T4, median ~22 | Variable with demand; no published hard quota. |

**The rule that follows:** if the smallest honest version of your experiment does not fit in 30 GPU-hours, shrink it or pick another question.

---

## Part 5 — what each approach needs beyond this page

Each ramp in this group opens by naming its own delta. This is the summary, so you can see the shape before you pick where to go deep.

| Approach | What it needs beyond this page | Entry cost |
|---|---|---|
| **AP1 · Scale** | Distributed training, systems | 🔴 needs a cluster |
| **AP2 · Reasoning** | Search, verification, process reward models | 🟢 low |
| **AP3 · Agents** | Context engineering, tool protocols, evaluation design | 🟢 low |
| **AP4 · RL from interaction** | Post-training pipelines, preference modelling | 🟡 medium |
| **AP5 · World models / JEPA** | Self-supervised learning, energy-based models, video | 🟡 medium |
| **AP6 · Brain-based** | Computational neuroscience, predictive coding, spiking nets | 🟡 medium |
| **AP7 · Neurosymbolic** | Logic, probabilistic programming, program semantics | 🟡 medium |
| **AP8 · Program synthesis / ARC** | Program search, test-time training, information theory | 🟢 low |
| **AP9 · Open-endedness** | Evolutionary computation, quality-diversity, archive methods | 🟢 low |
| **AP10 · Embodiment** | Control, robotics, imitation learning | 🔴 needs hardware |
| **AP11 · Whole-brain emulation** | Connectomics, biophysics | 🔴 needs a lab |

::: key
**On breadth then depth.** You have already done the breadth — the eleven approach pages *are* the breadth pass. These ramps are the depth machinery: each one gives you the books, courses, theses, papers, code and people for one bet, so that whichever you go deep in, the route is already laid.

**One amendment worth holding.** Your aim is to take the best idea out of each approach and combine them, which is how DeepMind itself was founded. That is legitimate — but a synthesis is only real if you know *where each piece breaks*, and you learn that by hitting the break yourself, not by reading that it exists. Combining approaches you have only read about produces a sentence anyone can write. So: **breadth across eleven for the map, depth in one for the calibration.** Every ramp therefore ends in an experiment, not a reading list.
:::

---

## ⚠️ Honesty box

- **The twenty-item floor is my judgement, not a standard.** Nobody publishes such a list and a different researcher would swap five entries. What I stand behind is the *rule* that generated it, not the list.
- **"Delegate execution, never judgement" is easy to say and hard to police.** Under time pressure it is genuinely tempting to accept a result you cannot check. That temptation is the real risk in an AI-accelerated research plan and no page removes it. The 🧠 pile being actually in your head is the only defence.
- **I cannot supply the judgement of which question is worth asking.** That comes only from the loop in [THE_PLAN](../THE_PLAN.md) — from being wrong in a way you cannot argue with.
- **This page was cut down from a much longer one.** Rev 1 and 2 contained a full six-layer prerequisite curriculum with books. It was removed because you already have those prerequisites and are revising them anyway. If that turns out to be wrong, the material is in git history, not lost.

---

## Connections

- The eleven bets: [the map](../APPROACHES_TO_AGI.md) · the ranking: [the verdict](../40-the-verdict/01_which-bets-get-to-agi.md) · why doing beats reading: [THE_PLAN](../THE_PLAN.md).
- The first ramp, and the one nearest your stated interest: **[AP9 · open-endedness](01_ap9-open-endedness.md)**.
- The conceptual half of the RL prerequisite, already written: [AP4 · the engine](../50-deep-dives/04_ap4-deep-dive-the-engine.md) and [AP4 · the reward is the whole game](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md).

---

## Check yourself *(try one, from memory)*

1. State the rule that decides whether something goes in the 🧠, 📖 or 🤖 pile — in one sentence, no examples.
2. Your interview prep covers nearly the whole trunk. Name the one thing it does not, and say which five approaches need it.
3. Why is "derive backpropagation by hand" a *once* task rather than a memorised one?
4. What is the honest limit on delegating paper-reading to an AI, and which pass must always be yours?

---

## Revision notes

- **rev 3 · 2026-09-09 · cut by two-thirds.** The learner clarified their position: a year of data-science apprenticeship, currently revising maths, ML, DL, NLP, LLM internals, AI engineering and MLOps for DS/MLE interviews — so the prerequisites are already handled and being refreshed on a different schedule. Rev 2's six-layer curriculum with per-layer book recommendations was therefore redundant and was removed wholesale; what remains is the one genuine gap (**RL — Sutton & Barto Ch. 1–6, 13**), the judgement floor, the permission-to-forget list, the once rule, research practice, and the per-approach cost map. Also removed: the owned-library audit and the ranked-gaps table, both of which existed to service the deleted curriculum. Title changed to match what the page now is.
- **rev 2 · 2026-09-09.** Introduced the three piles (internalise / reference / delegate), the rule *delegate execution, never judgement*, the twenty-item judgement floor, the permission-to-forget list and the once rule; replaced "choose a lane" with *breadth for the map, depth in one for calibration*.
- **rev 1 · 2026-09-09 · new.** First page of group ⑥, written as a shared trunk so the per-approach ramps carry only their delta.
