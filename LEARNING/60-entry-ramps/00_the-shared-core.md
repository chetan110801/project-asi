---
id: c-shared-core
sortkey: 6000
title: The shared core — what every approach needs before its own ideas make sense
domains: [method, entry-ramps, resources]
level: core
prereqs: []
provides: [trunk-curriculum, maths-floor, dl-floor, rl-floor, research-skills, owned-library-audit]
status: ready
reading_time: 26 min
rev: 1
created: 2026-09-09
updated: 2026-09-09
---

# The shared core — what every approach needs before its own ideas make sense

*The eleven bets do not need eleven separate educations. They share a trunk, and the trunk is most of the work. This page is that trunk: the topics every approach assumes you already have, the single best resource for each, an audit of what is already on your shelf, and — the part most reading lists leave out — the test that tells you when you are done with a layer and should stop.*

> **You are here:** this is the first page of **⑥ Entry ramps**, the group that answers *how do I actually learn one of these well enough to work on it.* The [map](../APPROACHES_TO_AGI.md) says what the bets are; the [verdict](../40-the-verdict/01_which-bets-get-to-agi.md) ranks them; [the plan](../THE_PLAN.md) says why doing beats reading. This group says **what to study, in what order, from which book**. Read this page first. Every approach ramp that follows lists only what it needs *beyond* this page.

> **Where the facts come from:** a live web check on **2026-09-09** — the Sutton & Barto edition status, Stanford CS336 (Spring 2026), Berkeley CS 185/285 (Spring 2026), the current free-PDF status of Murphy, Prince, Bishop and Goodfellow, and current free-GPU quotas on Kaggle and Colab. Plus a direct read of your own `local_resources/` shelf on the same date. Book prices and quotas move; the structure of the trunk does not.

---

## In one minute

There are six layers under every approach on the map: **maths → machine learning → deep learning → transformers → reinforcement learning → research skills.** Roughly seventy percent of what any two approaches demand of you is in those six layers, which is why learning them once is the cheapest thing you will ever do in this project.

You already own good books for four of the six. The real gaps are **information theory**, **reinforcement learning proper** (you have implementation books but not the standard text), and **research practice** — the last being the one that decides whether you become someone who does research or someone who reads it.

The most important idea on this page is not a book. It is this: **learn the floor of each layer, then stop and pull the rest on demand.** A trunk studied to completeness takes three years and ends with you no closer to a result. A trunk studied to its floor takes a few months and lets you start reading the actual papers in your lane, which is where the rest of the maths will find you — in context, attached to a reason.

---

## How to use this page

1. **Read Part 1 first.** It audits the ~250 books you already own against the six layers. You are better supplied than you think, and buying what you already have is the most common way to waste money at this stage.
2. **Work Part 2 top to bottom, to the floor only.** Each layer has a *done-when* test. When you pass it, move on. Do not finish the book.
3. **Fill the gaps in Part 3.** Everything critical there is free.
4. **Use Part 4 to choose a lane.** It shows which approaches each layer unlocks — some bets need far less of the trunk than others, and that is a legitimate reason to pick one.

::: warn
**One discipline, or this page becomes a trap.** The trunk is a *prerequisite*, not an achievement. Nobody has been hired into a lab for finishing a textbook. The point of the floor is to make the papers in your chosen approach readable — nothing more. If you catch yourself three months in and still on Layer 0, you have misread the page.
:::

---

## Part 1 — what is already on your shelf

Audited against `local_resources/` on 2026-09-09. **Where a filename is ambiguous I say so rather than guess** — several of your files are named by topic (`LA (Adv).pdf`, `Math for ML.pdf`) and I cannot tell the exact edition without opening them.

| Layer | What you own | Verdict |
|---|---|---|
| **Maths — linear algebra** | `Math for ML.pdf` *(almost certainly Deisenroth, Faisal & Ong — free online)*, `LA (Adv)`, `LA (Applied)`, `LA (A-Z)`, `LA (Practical) for DS`, `Essential Math for AI` | **Covered, oversupplied.** Five overlapping books is four too many. Pick one and delete the rest from your reading plan, not your disk. |
| **Maths — calculus** | Strang *Calculus*, `Multivariate Calculus`, Apex, several Dummies | **Covered.** You need far less of this than you own. |
| **Maths — probability & statistics** | `Introduction_to_Probability.pdf`, `Statistics (Advanced)`, ESL (`ESLII_print12_toc.pdf`), Dummies | **Covered.** ESL is a reference, not a course — do not read it front to back. |
| **Maths — optimization** | Boyd & Vandenberghe, *Convex Optimization* (2009) | **Covered, and it is the standard.** Free from Stanford. |
| **Maths — information theory** | — | 🔴 **GAP.** Nothing on your shelf. See Part 3. |
| **ML foundations** | Bishop *PRML* (2006), ESL, Géron *Hands-On ML* 1st/2nd/**3rd**, Raschka, *ML Yearning* | **Covered, strongly.** Use Géron 3rd; treat PRML and ESL as references. |
| **Deep learning** | Prince *Understanding Deep Learning*, Bishop & Bishop *Deep Learning: Foundations and Concepts* (2023), Goodfellow *Deep Learning* (2018 printing) | **Covered, excellently.** You own the three best books in the field. Goodfellow predates transformers — keep it for the fundamentals chapters only. |
| **Transformers & LLMs** | *NLP with Transformers*, *Hands-On LLMs*, *Building Transformer Models*, Huyen *AI Engineering*, Huyen *Designing ML Systems*, several agent books | **Covered for *use*, thin for *internals*.** These teach you to build with models. CS336 teaches you to build one. See Layer 3. |
| **Reinforcement learning** | *Grokking Deep RL* (Morales), a multi-agent RL text, RL-for-finance, plus the `RL-CS234` course folder | 🔴 **PARTIAL GAP.** You have implementation-first books and course slides but not the standard text. This matters — see Part 3. |
| **AI, general** | *AIMA* 3rd **and** 4th edition, *A Brief History of Intelligence*, ~200 survey/edited volumes | **Covered.** AIMA 4th is the only one you need; most of the 2024–26 edited volumes are conference proceedings in book clothing and are not study material. |
| **Research practice** | — | 🔴 **GAP.** Nothing, and this is the important one. See Layer 5. |

::: key
**The finding:** your shelf is strong on *understanding* and weak on *doing*. You own three world-class deep learning textbooks and no book on how to run an experiment. That is exactly the imbalance [THE_PLAN](../THE_PLAN.md) diagnosed from a different direction — it is the same problem showing up in your bookshelf.
:::

---

## Part 2 — the six layers

Each layer: what it is, **why every approach needs it**, the one thing to use, and the test that says stop.

### Layer 0 · The maths floor

Four topics, and you need much less of each than a maths degree implies. The floor is *"I can read the equations in a paper without stopping"*, not *"I could prove these theorems."*

| Topic | Why every approach needs it | Use this | Done when |
|---|---|---|---|
| **Linear algebra** | Every model is matrices. Every architecture argument — attention, embeddings, low-rank adapters, JEPA's latent space — is a claim about vector spaces. | **Mathematics for ML, Part I** *(you own it; free at mml-book.github.io)*. Watch **3Blue1Brown, *Essence of Linear Algebra*** first — 15 free videos, and it builds the geometric intuition the books assume. | You can say what an eigenvector *is* geometrically, why SVD is a change of basis, and read a paper's tensor shapes without re-deriving them. |
| **Probability** | Every loss function is a likelihood in disguise. KL divergence appears in RLHF's leash, in VAEs, in information theory, in JEPA's collapse guards. | **Harvard Stat 110** (Blitzstein) — free lectures + free book — *or* the `Introduction_to_Probability.pdf` you own if it turns out to be Blitzstein & Hwang. | Expectation, variance, conditional independence, Bayes' rule, **KL divergence** and maximum likelihood are automatic, not looked up. |
| **Calculus & optimization** | Training is gradient descent. Everything about convergence, learning rates and loss landscapes is calculus. | Enough multivariable calculus for the **chain rule**, then **Boyd Ch. 1–5** for convexity *(you own it, free)*. | You have derived backpropagation for a two-layer network **by hand, once**. Once is enough and it is not optional. |
| **Information theory** | 🔴 The gap. Entropy, mutual information and description length are the vocabulary of compression-as-intelligence — which is the formal spine of [AP8](../20-the-approaches/08_ap8-program-synthesis-arc.md), and shows up again in JEPA, in scaling laws and in every "what is intelligence" argument on the map. | **MacKay, *Information Theory, Inference, and Learning Algorithms*** — free PDF from Cambridge, Ch. 1–6 and 8. | You can explain why "compression is understanding" is a *claim* and not a metaphor. |

::: note
**How long:** two to three months at evenings pace if you are rusty, three weeks if you are not. It is the least glamorous layer and the one that silently blocks everything else. Do not skip information theory because it is the one you own no book for — it is the layer that makes [the formal theory dive](../50-deep-dives/01_ap8-deep-dive-the-formal-theory-of-intelligence.md) readable.
:::

### Layer 1 · Machine learning foundations

The pre-deep-learning material. It is short, you own it, and skipping it produces people who can fine-tune a model but cannot tell you why their evaluation is lying to them.

| Use this | Why | Done when |
|---|---|---|
| **Géron, *Hands-On ML*, 3rd ed.** — Parts I–II *(you own all three editions; use the 3rd)* | Code-first, current, and it teaches the experimental hygiene the theory books skip. | You can explain bias–variance, overfitting, regularisation, train/val/test discipline, and cross-validation — and you have written a training loop from scratch. |
| **ESL / PRML** *(you own both)* | **Reference only.** Look things up in them. Reading either cover to cover is a months-long detour with no payoff at your stage. | — |

### Layer 2 · Deep learning

You own the three best books in existence here. The decision is which one, and the answer is: **one of them, not three.**

| Use this | Why | Done when |
|---|---|---|
| **Prince, *Understanding Deep Learning*** *(you own it)* | The shortest honest treatment — 544 pages, free updated PDF, 68 exercise notebooks. Prince deliberately optimised for "shortest book that is still true", which is exactly your constraint. | You can explain why depth helps, what normalisation and residual connections actually do, and why initialisation matters. |
| **Bishop & Bishop (2023)** *(you own it)* | The alternative if you prefer a probabilistic framing. **Pick one of these two, never both** — they cover the same ground at different depths. | — |
| **Karpathy, *Neural Networks: Zero to Hero*** — free video series | 🔑 **The single highest-value item on this page.** You build backpropagation from nothing, then build a GPT. It converts you from someone who understands deep learning to someone who has *made* one, and that conversion is the whole gap [THE_PLAN](../THE_PLAN.md) is about. | You have a working transformer you wrote yourself, trained on something small, and you can explain every line. |
| **Goodfellow (2016/18)** *(you own it)* | Historical fundamentals. Predates transformers entirely. Chapters 5–9 only. | — |

### Layer 3 · Transformers and LLMs — the current substrate

Nearly every 2026 approach either *is* a language model, *uses* one as a component, or *defines itself against* one. You cannot judge AP1 through AP9 without knowing how this machine works internally.

| Use this | Why | Done when |
|---|---|---|
| **Stanford CS336 — *Language Modeling from Scratch*, Spring 2026** — lectures free on YouTube, assignments and notes free at cs336.stanford.edu | The best current course anywhere on how these models actually work: tokenization, architecture, GPUs/TPUs, systems, scaling laws, data, alignment. You build the thing. *(The paid Stanford Online version is $7,875 — the materials you need are free.)* | You can explain attention, the KV-cache, tokenization's consequences, and the difference between pre-training and post-training — and you have trained a small LM end to end. |
| Your LLM shelf — *NLP with Transformers*, *Hands-On LLMs*, Huyen's *AI Engineering* | These teach **applying** models. Useful, but they are not the internals. Read them for the vocabulary, not the understanding. | — |
| Already done: **[AP1 · anatomy of a scaling law](../50-deep-dives/07_ap1-deep-dive-anatomy-of-a-scaling-law.md)** and **[AP3 · inside the agent loop](../50-deep-dives/08_ap3-deep-dive-inside-the-agent-loop.md)** | You have already read the conceptual half of this layer. CS336 supplies the mechanical half. | — |

### Layer 4 · Reinforcement learning

The layer with a real hole in it. RL is load-bearing for **AP2, AP3, AP4, AP9 and AP10** — five of eleven bets — and it is the trunk layer you are least equipped for.

| Use this | Why | Done when |
|---|---|---|
| 🔴 **Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.** — **free** at incompleteideas.net. *(Checked 2026-09-09: still the standard; there is no 3rd edition.)* | The field's one canonical text, and the missing book on your shelf. Chapters 1–6 and 13 are the floor. Everything modern is a variation on what is in here. | You can explain the **TD error**, the exploration/exploitation trade-off, and policy gradient — and connect each to something in [AP4 · the engine](../50-deep-dives/04_ap4-deep-dive-the-engine.md), which you have already read. |
| **Berkeley CS 185/285 — *Deep RL*, Spring 2026** (Levine) — lectures free on YouTube, materials at rail.eecs.berkeley.edu/deeprlcourse | The deep-RL half Sutton & Barto predates. Levine's course is the field's default graduate course and the Spring 2026 recordings are up. | You can follow a modern RL paper's method section. |
| **OpenAI *Spinning Up in Deep RL*** — free | The shortest path from theory to running code. Implement one algorithm from it. | You have a working PPO or DQN you understand. |
| *Grokking Deep RL* *(you own it)*, `RL-CS234` folder | Implementation-first companion; Stanford's RL course materials. Good support, not a substitute for Sutton & Barto. | — |
| Already done: **[AP4 · the engine](../50-deep-dives/04_ap4-deep-dive-the-engine.md)** and **[AP4 · the reward is the whole game](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md)** | You have the conceptual map of this layer already — TD learning, actor–critic, RLHF, DPO, verifiable rewards. What is missing is the mechanics underneath it. | — |

### Layer 5 · Research practice — the layer nobody sells you a book for

This is where you are weakest, it is not optional, and it is the difference between the two futures in your plan. It has four parts.

**① Reading papers.** Use the standard three-pass method: pass one, five minutes — title, abstract, intro, conclusion, figures; decide whether to continue. Pass two, an hour — full read, skip proofs, interrogate the experimental setup and the tables. Pass three, only for papers you intend to build on — reconstruct the work as if you were the author, and find what they did not check.

You already said you cannot read papers optimally yet. Two things fix that faster than practice alone: do pass one yourself *before* asking me for help — the skill is in deciding what deserves pass two — then hand me the paper and ask for the parts you got stuck on. That way you build the judgement and I supply the density. Handing me a paper cold trains nothing.

**② Keeping a lab notebook.** One file per experiment: the question, the setup, the command that ran it, the result, and what you now believe that you did not believe before. Change one variable at a time. This is unglamorous and it is the entire difference between an experiment and fiddling.

**③ Writing it up — especially when nothing happened.** A negative result written clearly is a real artifact and is usually more informative than a positive one. It is also the thing you can show a lab.

**④ Knowing your compute budget.** Checked 2026-09-09:

| Where | What you get | Notes |
|---|---|---|
| **Kaggle Notebooks** | **~30 GPU-hours/week**, guaranteed, P100/T4 (16 GB), ~12h session cap; ~20 TPU-hours | Predictable and fixed. Also where ARC Prize runs. **Start here.** |
| **Google Colab free** | ~15–30 GPU-hours/week on T4, median ~22 | Variable with demand; no published hard quota. |

::: key
**The rule that follows from ④:** if the smallest honest version of your experiment does not fit in 30 GPU-hours, shrink it or pick another question. This is Part 3 of [THE_PLAN](../THE_PLAN.md) restated as a weekly budget.
:::

---

## Part 3 — the gaps, ranked

Everything critical is free. Buy nothing until you have used these.

| Rank | What | Cost | Why it is ranked here |
|---|---|---|---|
| **1** | **Sutton & Barto, 2nd ed.** *(incompleteideas.net)* | Free | Five of eleven approaches sit on RL and you have no canonical text. Biggest single hole on your shelf. |
| **2** | **Karpathy, Zero to Hero** | Free | Not a gap in knowledge — a gap in *having built one*. Highest value per hour of anything here. |
| **3** | **MacKay, information theory** *(Cambridge, free PDF)* | Free | The only trunk topic with zero coverage on your shelf, and it underwrites the compression-as-intelligence arguments across the map. |
| **4** | **Stanford CS336 Spring 2026** | Free | The internals of the substrate every other bet is measured against. |
| **5** | **Berkeley CS 185/285 Spring 2026** | Free | Modern deep RL; the half Sutton & Barto predates. |
| **6** | **Murphy, *Probabilistic ML: An Introduction*** *(probml.github.io, draft free)* | Free | Optional. Take it only if you want the probabilistic framing deeper than Prince gives. Volume 2 (~$138) is a reference for later, not now. |

::: warn
**What not to buy.** Nothing on this page needs to be bought. Also: the ~200 edited volumes in your library with titles of the form *"Artificial Intelligence and X, 2025"* are conference proceedings in book covers. They are not wrong, but they are not study material, and no amount of reading them will move you toward a result. Do not let their number make the shelf feel more complete than it is.
:::

---

## Part 4 — what each layer unlocks

The trunk is not equally weighted across the bets. This is the first cut of the router — the full version comes in the next page of this group, once each approach has been surveyed properly.

| Approach | Trunk layers it leans on hardest | Roughly what it needs *beyond* the trunk |
|---|---|---|
| **AP1 · Scale** | 0, 2, 3 | Systems and distributed training. Mostly closed to you without a cluster. |
| **AP2 · Reasoning** | 0, 3, 4 | Search, verification, process reward models. |
| **AP3 · Agents** | 3, 4, 5 | Context engineering, tool protocols, evaluation design. |
| **AP4 · RL from interaction** | 0, 4 | Post-training pipelines, preference modelling. |
| **AP5 · World models / JEPA** | 0, 2 | Self-supervised learning, energy-based models, video representation. |
| **AP6 · Brain-based** | 0, 2 | Computational neuroscience, predictive coding, spiking networks. |
| **AP7 · Neurosymbolic** | 0, 1 | Logic, probabilistic programming, program semantics. |
| **AP8 · Program synthesis / ARC** | 0 *(incl. information theory)*, 2 | Program search, type systems, test-time training. |
| **AP9 · Open-endedness** | 1, 4 | Evolutionary computation, quality-diversity, archive methods. |
| **AP10 · Embodiment** | 2, 4 | Control, robotics, imitation learning. Needs hardware. |
| **AP11 · Whole-brain emulation** | 0 | Connectomics, biophysics. Needs a lab. |

::: key
**Read that table as a cost map, not a menu.** AP8 and AP9 need the least beyond the trunk — no cluster, no robot, no wet lab — which is a large part of why [THE_PLAN](../THE_PLAN.md) lands where it does. Cheap-to-reach is a legitimate reason to pick a lane when you are starting alone.
:::

---

## Part 5 — how long this actually takes

Honest numbers, assuming evenings and weekends alongside a job.

| Layer | To the floor | Notes |
|---|---|---|
| 0 · Maths | 6–10 weeks | Less if your linear algebra and probability are current. Information theory is ~2 weeks of it. |
| 1 · ML foundations | 2–3 weeks | You own the books; this is revision for most people with a data background. |
| 2 · Deep learning | 4–6 weeks | Half of it is Karpathy, and that half is hands-on-keyboard, not reading. |
| 3 · Transformers | 6–8 weeks | CS336 is a real course with real assignments. Doing the assignments is the point. |
| 4 · RL | 6–8 weeks | Only if your chosen approach needs it — check Part 4 before spending this. |
| 5 · Research practice | Ongoing | Starts the day you run your first experiment, not before. |

**Total to a floor across all six: roughly six to nine months of evenings.** But that is the wrong number to plan around, because you should not do all six before starting. **Layers 0–2 plus Karpathy, then pick a lane and pull Layers 3 or 4 as your lane demands** — that is three to four months before you are reading real papers in a chosen approach, which is the point at which this stops being study and starts being work.

---

## ⚠️ Honesty box

- **This page is a plan, not a result.** None of it has been tested on you. The time estimates are conventional ranges, not measurements, and the honest error bar on "six to nine months" is large in both directions.
- **The shelf audit is partly inferential.** Several of your files are named by topic rather than by title (`LA (Adv).pdf`, `Math for ML.pdf`, `Introduction_to_Probability.pdf`). I matched them to the most likely standard texts and said so where I was guessing. Open them before relying on the mapping.
- **"Done when" tests are judgement calls.** They are the floors I would set; a supervisor might set them higher. They are deliberately low because the failure mode at your stage is over-preparing, not under-preparing.
- **I have not verified every free PDF link today.** The status of Sutton & Barto, CS336, CS 185/285, Murphy, Prince, Bishop and Goodfellow was checked on 2026-09-09; individual URLs move. If one is gone, the book is not.
- **The biggest risk in this page is that you follow it.** A trunk is a comfortable place to stay, and every week spent here is a week not spent on contact with reality. The correct relationship to this page is to use it and leave it.
- **One thing I cannot supply.** Nothing here builds the judgement of *which question is worth asking*. That comes only from the loop in [THE_PLAN](../THE_PLAN.md) — from being wrong in a way you cannot argue with.

---

## Connections

- Why doing beats reading, and the loop this trunk feeds into: **[THE_PLAN](../THE_PLAN.md)**.
- What the eleven bets actually are: **[the map](../APPROACHES_TO_AGI.md)**; which look strongest: **[the verdict](../40-the-verdict/01_which-bets-get-to-agi.md)**.
- The conceptual halves of Layers 3 and 4, already written: **[AP1 · anatomy of a scaling law](../50-deep-dives/07_ap1-deep-dive-anatomy-of-a-scaling-law.md)**, **[AP3 · inside the agent loop](../50-deep-dives/08_ap3-deep-dive-inside-the-agent-loop.md)**, **[AP4 · the engine](../50-deep-dives/04_ap4-deep-dive-the-engine.md)**, **[AP4 · the reward is the whole game](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md)**.
- Why information theory is a trunk topic and not a curiosity: **[AP8 · the formal theory of intelligence](../50-deep-dives/01_ap8-deep-dive-the-formal-theory-of-intelligence.md)**.

---

## Check yourself *(try one, from memory)*

1. Name the six layers of the trunk in order, and say which two your current shelf does not cover.
2. What is the *done-when* test for linear algebra, and why is it set at reading rather than proving?
3. Five of the eleven approaches lean on reinforcement learning. Name three of them, and say what the one missing book on your shelf is.
4. Why does Part 4's table say AP8 and AP9 are the cheapest to reach — and why is "cheap to reach" a legitimate reason to choose a lane rather than a lazy one?
5. What is the failure mode this page warns about most, and what is the earliest sign you have fallen into it?

---

## Revision notes

- **rev 1 · 2026-09-09 · new.** First page of the new group ⑥ (entry ramps), created in response to the learner's request for per-approach resources — books, courses, papers, everything, foundations through state of the art. Written as a shared trunk first, so the per-approach pages can carry only their delta and the same book is never recommended twice. Grounded in a live web pass (Sutton & Barto edition status, CS336 Spring 2026, CS 185/285 Spring 2026, free-PDF status of Murphy/Prince/Bishop/Goodfellow, Kaggle and Colab quotas) and in a direct audit of the learner's own ~250-book `local_resources/` shelf.
