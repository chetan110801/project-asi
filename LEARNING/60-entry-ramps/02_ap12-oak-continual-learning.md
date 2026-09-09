---
id: c-ramp-ap12
sortkey: 6002
title: Ramp · AP12 OaK & continual learning — every resource, and the route through them
domains: [frontier, approaches-to-agi, entry-ramps, resources]
level: core
prereqs: [c-shared-core, c-ap12-oak, c-continual-learning]
provides: [ap12-reading-ladder, continual-learning-resources, plasticity-toolchain, ap12-first-experiment, collas-venue]
status: ready
reading_time: 22 min
rev: 1
created: 2026-09-09
updated: 2026-09-09
---

# Ramp · AP12 OaK & continual learning — every resource, and the route through them

*The second approach ramp, and the bet that sits closest to what you said you wanted: an agent that learns everything itself, forever, with nobody feeding it. This page is every book, thesis, survey, paper, course, talk, library and venue for it — what exists, what doesn't, and the order to take them in.*

> **You are here:** the second ramp in **⑥ Entry ramps**. The [AP12 card](../20-the-approaches/12_ap12-oak-experience-only-agents.md) says what the bet is; the [continual-learning page](../30-across-the-approaches/03_continual-learning-and-plasticity.md) covers the obstacle underneath it. **This page re-explains neither** — it is the route in. Read [what actually stays](00_the-shared-core.md) first.

> **Where the facts come from:** a live web pass on **2026-09-09** — the Alberta Plan paper (arXiv 2208.11173) via ar5iv; Dohare et al., *Nature* 2024; Dohare's University of Alberta dissertation located in the institutional repository; the continual-learning survey literature (Parisi 2019; the TPAMI comprehensive survey, arXiv 2302.00487; the LLM survey, arXiv 2404.16789; the continual-RL survey, arXiv 2506.21872); Chen & Liu's *Lifelong Machine Learning*; CoLLAs and RLC as venues; the loss-of-plasticity, Forager and Agar.io codebases; and the Oak Lab founding plus the 8 September 2026 Sequoia podcast. Dated things below will move fast — the lab is two months old.

---

## In one minute

**This ramp has an unusual shape, and noticing it saves you months.** It splits into two literatures that barely talk to each other:

- **Continual learning** is a *mature, well-supplied ML subfield*. Real textbook, several excellent surveys, a dedicated conference, benchmarks, libraries. You could study it like any other topic.
- **OaK and the Alberta Plan** are a *research programme two months into having a lab*. One position paper, a handful of talks, no textbook, no course, almost no results.

**You want both, in that order.** The first gives you the technical ground and a field you can publish in this year. The second gives you the thesis that makes it matter — and it is where the ambition lives.

The one document that bridges them: **Shibhansh Dohare's PhD thesis, *Learning Forever using Artificial Neural Networks*** (University of Alberta, supervised by Sutton). It is the *Nature* result at book length, and it is free.

---

## Part 1 — the delta: what you must hold beyond the core

Five concepts. Three you already have from the [cross-cutting page](../30-across-the-approaches/03_continual-learning-and-plasticity.md); two are new here.

| # | Concept | Why it is here |
|---|---|---|
| 1 | **Catastrophic forgetting vs. loss of plasticity** | The distinction everything rests on. Get these the wrong way round and you will read the whole literature wrong. |
| 2 | **The stability–plasticity dilemma** | Why you cannot just fix both, and why every method is a trade rather than a solution. |
| 3 | **The three method families** — replay · regularisation · architecture | The taxonomy every paper positions itself inside. |
| 4 | **Step-size adaptation and meta-learning the learning rate** 🆕 | The technical heart of OaK's second special property, and a whole small literature of its own. Per-weight learning rates, tuned online. |
| 5 | **Options and temporal abstraction** 🆕 | An *option* is a skill with a start condition, a policy and a stopping condition — the "O" in OaK, and the classic RL machinery for acting over extended time. Comes from Sutton's own earlier work; assumed without explanation in every OaK talk. |

::: note
**Concept 5 is the one to check yourself on.** Options are standard RL and are covered in Sutton & Barto, but they are the piece most people skip on a first pass through the textbook — and OaK is *built* out of them. If "option" is not solid, the FC-STOMP loop will read as hand-waving when it is not.
:::

---

## Part 2 — books and surveys

Unlike [AP9](01_ap9-open-endedness.md), this field *does* have real reference material — for the continual-learning half. For OaK itself there is nothing, and that is not going to change soon.

| What | Status | Why |
|---|---|---|
| ⭐ **Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.** | 🆓 Free | Mandatory here in a way it is not for other approaches — OaK *is* an RL architecture and assumes the whole book. **Ch. 1–6 for the base, plus the options / temporal-abstraction material.** This is the one prerequisite named in [the core](00_the-shared-core.md), and this is the ramp where it is unavoidable. |
| **Chen & Liu, *Lifelong Machine Learning*, 2nd ed.** (Morgan & Claypool, 2018) | 🛒 Buy / library | The nearest thing to a textbook for the field. Covers lifelong learning across supervised, unsupervised and RL settings. **Caveat worth knowing: it predates the plasticity work entirely**, so it is strong on forgetting and silent on the failure AP12 cares about. Read it for the framing and the vocabulary, not for the current picture. |
| **Parisi et al., *Continual lifelong learning with neural networks: A review*** (Neural Networks 113, 2019) | 🆓 Free | The classic review, and the one that connects the ML problem to the biological one. Still the best single orientation. |
| ⭐ **Wang et al., *A Comprehensive Survey of Continual Learning: Theory, Method and Application*** (TPAMI; arXiv 2302.00487) | 🆓 Free | **The one to actually work through.** Modern, thorough, and it is where the replay/regularisation/architecture taxonomy is laid out properly. Treat this as the textbook the field doesn't have. |
| **A Survey of Continual Reinforcement Learning** (arXiv 2506.21872) | 🆓 Free | The RL-specific version, and RL is where AP12 lives. Newer, narrower, directly relevant. |
| **Continual Learning of Large Language Models: A Comprehensive Survey** (arXiv 2404.16789) | 🆓 Free | The frontier-facing version — continual pre-training, continual fine-tuning, continual alignment. Read it to see where the money is, and to find questions that are commercially live rather than only philosophically interesting. |

::: warn
**There is no book on OaK, and no course.** The Alberta Plan paper is the only written statement of the programme; everything else is talks. Do not wait — the substitute is Part 3.
:::

---

## Part 3 — theses and the primary programme documents

| What | Access | Why |
|---|---|---|
| ⭐ **Shibhansh Dohare, *Learning Forever using Artificial Neural Networks*** (PhD, University of Alberta; supervisors Richard Sutton and A. Rupam Mahmood) | 🆓 Free — University of Alberta institutional repository | **The single most valuable document in this ramp.** The first author of the *Nature* plasticity paper, at thesis length: what plasticity is, how it is lost, how it is measured, and what continual backprop does about it. This is the technical core of AP12 written to be read by someone entering the field. Read this before any paper. |
| ⭐ **Sutton, Bowling & Pilarski, *The Alberta Plan for AI Research*** (arXiv 2208.11173, 2022) | 🆓 Free | The programme's founding document — the common model of the intelligent agent, the four commitments, and twelve research steps. Short, unusually clear, and it explains *why* the work looks the way it does. |
| **Khurram Javed's PhD work** (University of Alberta) — including **MRCL**, meta-learning representations that accelerate future learning and resist forgetting | 🆓 Findable free | He is Oak Lab's cofounder, so his research line is half of what the lab will do. I did not verify a thesis title — treat this as a search instruction, not a citation. Start from MRCL and follow his publication list. |

---

## Part 4 — the paper ladder

Four rungs, roughly twenty papers. Column key: 🟢 read it yourself · 🟡 abstract and results yourself, method with me · 🔴 hand to me first.

### Rung 1 · The problem, measured

| Paper | | Why |
|---|---|---|
| ⭐ Dohare, Hernandez-Garcia, Lan, Rahman, Mahmood & Sutton, **Loss of plasticity in deep continual learning** (*Nature*, 2024) | 🟢 | **The foundation of the whole bet.** Read it first, read it properly, and pay attention to what is actually being measured — the ability to learn *new* tasks, not memory of old ones. |
| Abbas et al., **Loss of Plasticity in Continual Deep Reinforcement Learning** (CoLLAs 2023) | 🟡 | The same failure in RL, which is AP12's actual setting. Also your introduction to CoLLAs, the venue in Part 8. |
| Dohare et al., **Maintaining Plasticity in Deep Continual Learning** (arXiv 2306.13812) | 🟡 | The earlier, longer version of the *Nature* work, with more of the experimental detail the journal format cut. |
| **Directions of Curvature as an Explanation for Loss of Plasticity** (arXiv 2312.00246) | 🔴 | One of the serious attempts at *why* it happens. Read with me — this is where the maths starts. |

### Rung 2 · The methods

| Paper | | Why |
|---|---|---|
| Wang et al., **Comprehensive Survey of Continual Learning** (2302.00487) | 🟡 | Do this instead of reading twenty method papers. Then read the three or four it convinces you matter. |
| **Addressing Loss of Plasticity and Catastrophic Forgetting** (ICLR 2024) | 🟡 | Explicitly attacks both failures at once, which almost nothing else does. The key paper for understanding the trade rather than one side of it. |
| Javed & White, **MRCL — Meta-Learning Representations for Continual Learning** | 🟡 | Oak Lab's cofounder's line of work: learn representations that make *future* learning easier. |
| **Continual Learning as Computationally Constrained RL** (arXiv 2307.04345) | 🔴 | Reframes the whole problem as a resource-constrained RL problem. Hard, and clarifying if you get through it. |

### Rung 3 · The programme

| Paper / source | | Why |
|---|---|---|
| ⭐ **The Alberta Plan** (2208.11173) | 🟢 | The vision, the four commitments, the twelve steps. |
| **Reward-Respecting Subtasks for Model-Based RL** (arXiv 2202.03466) | 🟡 | The technical paper under FC-STOMP's "SubTask" stage — how an agent generates sub-goals that still serve the top-level reward. This is the mechanism your interest is actually about. |
| Silver, Singh, Precup & Sutton, **Reward is Enough** (2021) | 🟢 | AP12's third principle. Already covered in [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) — read it here as the assumption AP12 inherits, along with the published rebuttals AP4 lists. |
| Silver & Sutton, **Welcome to the Era of Experience** (2025) | 🟢 | The short, readable statement of why human data is the ceiling. |
| **The OaK talks** — RLC-2025, AGI-2025, NeurIPS-2025 invited talk, MIT CSAIL Dertouzos lecture | 🆓 | The architecture exists mainly as these. Watch one; the NeurIPS and RLC versions are the technical ones. |

### Rung 4 · The frontier and the argument against

| Source | | Why |
|---|---|---|
| **Continual Learning of LLMs survey** (2404.16789) | 🟡 | Where the industry's version of this problem actually is. |
| **A Survey of Continual RL** (2506.21872) | 🟡 | The nearest thing to a state-of-the-art review for AP12's setting. |
| **Sutton's "LLMs are a dead end" interview** (Sept 2025) | 🟢 | The clearest statement of the position, in his own words, at length. |
| **The published counter-arguments** | 🟢 | Read at least one. The strongest lines: that Sutton understates how much humans learn by imitation; and that the Bitter Lesson's own logic favours whatever scalably converts compute into capability, which right now is pre-training. **Do not skip this rung** — a bet you have only seen argued for is a bet you cannot judge. |

---

## Part 5 — courses, talks, people

::: warn
**No course on OaK exists.** For the continual-learning half there is also no dedicated course, but the surveys are good enough to substitute — which is *not* true in [AP9](01_ap9-open-endedness.md), where nothing written exists at all. This field is better documented; it is just newer at the top.
:::

| What | Access | Why |
|---|---|---|
| **Berkeley CS 185/285 — Deep RL** (Spring 2026, Levine) | 🆓 | The RL machinery. Necessary here, not optional as in other ramps. |
| **The OaK talks** (RLC-2025 / AGI-2025 / NeurIPS-2025) | 🆓 | The architecture's primary source. |
| ⭐ **The Sequoia podcast, Sutton & Javed, 8 Sept 2026** | 🆓 | The one you found. The clearest statement of what Oak Lab is actually doing, and the most current thing in this ramp. |
| **Sutton's Dwarkesh interview, Sept 2025** | 🆓 | The long-form version of the LLM critique. |

**People to follow:** Richard Sutton · Khurram Javed *(Oak Lab cofounder — his research line is the lab's)* · Shibhansh Dohare *(the plasticity result; his site hosts the code)* · A. Rupam Mahmood (Alberta) · Michael Bowling and Patrick Pilarski (Alberta Plan coauthors) · Amii, the Alberta institute, which hosts much of the talk material.

---

## Part 6 — code and testbeds

This ramp is unusually well supplied with runnable things, which is why the first experiment is cheap.

| What | Use it for |
|---|---|
| ⭐ **`github.com/shibhansh/loss-of-plasticity`** | The *Nature* paper's own code. **This is where your first experiment runs.** |
| **Forager** (arXiv 2605.01131) | A lightweight testbed for continual learning with partial observability in RL. Deliberately small — built so experiments are cheap. |
| **"The Cell Must Go On" — Agar.io for continual RL** (arXiv 2505.18347) | A continual-RL environment that never ends, which is the point. |
| **LibContinual** (arXiv 2512.22029) | A library of continual-learning methods, for comparing against baselines rather than reimplementing them. |

---

## Part 7 — your first experiment

Two. The first is a reproduction; the second is the one only you are positioned to do.

### ① Reproduce the plasticity result *(Kaggle free tier, a weekend or two)*

**Question:** Does loss of plasticity appear where the paper says it does — and how quickly?

**Why this one.** [THE_PLAN](../THE_PLAN.md) Phase 2 argues reproduction is the cheapest possible contact with reality, and this is an unusually good candidate: the code is public, the effect is large, and the small settings (permuted MNIST, slowly-changing regression) run without a serious GPU. You find out immediately whether you can get a published result to run — a skill nobody tells you is separate from understanding the paper.

**Then vary one thing.** How does the decay curve change with network width? With the choice of activation function? With how fast the task distribution shifts? Any of those is a real question with an unpublished answer at small scale.

### ② The AP9 × AP12 question *(your two interests, intersecting)*

Here is something worth noticing. The [continual-learning page](../30-across-the-approaches/03_continual-learning-and-plasticity.md) rates [AP9](../20-the-approaches/09_ap9-open-endedness.md) as **highly dependent on continual learning, and almost entirely unexamined for it.** Open-ended systems generate an endless stream of new problems — which means their solvers face exactly the long task sequence that kills plasticity. Most open-endedness work runs for too few generations to notice.

**The question: does an open-ended system's solver lose plasticity, and if so, is that what makes open-ended runs stall?**

"They stall and nobody knows why" is a known complaint in AP9. "Networks silently lose the ability to learn over long task sequences" is a measured phenomenon in AP12. **Nobody appears to have checked whether the second explains the first.**

::: key
**Why this is a genuinely good first research question.** It is cheap — a MAP-Elites or POET-style run with plasticity metrics logged alongside the usual coverage and QD-score. It is unclaimed, as far as I can tell from this pass. It sits exactly where your two stated interests meet. It is publishable at a workshop either way — a negative result rules out an explanation the field has been guessing at. And it is precisely the kind of cross-approach question the [synthesis argument](00_the-shared-core.md) says these ramps exist to produce.

**Caveat, stated honestly:** I checked one search pass, not the literature. Before investing, do step ② of THE_PLAN's loop — ground it twice, once against the corpus and once against the live web — and expect to find someone has partly done it. That is normal and does not kill the question; it sharpens it.
:::

---

## Part 8 — where to publish, and the lab

| Venue | What it takes | Notes |
|---|---|---|
| ⭐ **CoLLAs — Conference on Lifelong Learning Agents** | Full papers, plus a workshop track | **The dedicated venue for exactly this.** Small, focused, and where the continual-RL plasticity work appears. Far more reachable than a mainline ML conference and the right target for a first paper. |
| **RLC — Reinforcement Learning Conference** | Full papers | Newer RL-specific conference; where Sutton gave the OaK talk. The right home for the RL-flavoured version of your work. |
| **NeurIPS / ICLR continual-learning workshops** | Short papers | Higher visibility, and workshops accept partial and negative results. |
| **arXiv + a clean repo** | The work itself | How this field circulates in practice. |

**On Oak Lab specifically.** It is deliberately small, two months old, and it will hire from people who show up with relevant work — which is the whole reason this ramp ends in an experiment rather than a reading list. **A reproduction of the plasticity result plus one honest variation is a more legible credential to that particular lab than any qualification**, because it is literally their research programme. That window is open now and it will narrow.

---

## Part 9 — the best idea in this bet

*(What a synthesis would take, and what it would leave.)*

**Take: that learning must never stop, and that this is measurable.** Not the architecture — the *diagnostic*. AP12's most transferable contribution is the observation that "can this system still learn?" is a question you can ask of any of the twelve bets, that almost nobody asks it, and that the answer is often no. That is a genuine tool, and applying it across approaches is one of the few things an outsider can do that a well-funded lab is not currently doing.

**Leave: the purity.** The refusal of all human data is the bet's most distinctive commitment and its weakest link. It is a principled position that discards the only signal that has ever produced broad competence about the world, on the argument that human text caps you at human ability. That argument is real — but "capped at human ability" is a ceiling nobody is anywhere near, and refusing the ladder because it ends short of the roof is a strange way to climb. A synthesis would keep continual learning and drop the purity: a system that starts from human knowledge and then never stops learning from its own experience. Sutton would say that is the crutch. Which of you is right is exactly the kind of thing an experiment could eventually settle, and that is the best reason to work on it.

---

## ⚠️ Honesty box

- **The paper list is inventoried, not read.** Assembled from surveys and search on 2026-09-09 with the key items verified. The 🟢/🟡/🔴 tags are estimates from abstracts and venue.
- **Khurram Javed's thesis is a search instruction, not a citation.** I verified Dohare's dissertation title and repository; I did not verify Javed's.
- **Part 7's second experiment may already be done.** I found no sign of it in one pass. One pass is not a literature review, and the honest expectation is that something adjacent exists. Ground it before investing.
- **The CoLLAs and RLC descriptions are from paper venues, not from reading their calls.** Check current dates, formats and fees before targeting either.
- **Part 9 is an argument, not a finding.** "Keep the continual learning, drop the purity" is my reading. Sutton's whole position is that the purity *is* the idea and that hybrids inherit the ceiling. He may be right; I have given his side its strongest form on the [card](../20-the-approaches/12_ap12-oak-experience-only-agents.md).
- **Everything about Oak Lab is two months old.** Staffing, focus, funding, whether it hires at all — all unknown and all likely to change. Do not build a plan that depends on one lab.

---

## Connections

- The bet: **[AP12 · OaK & the experience-only agent](../20-the-approaches/12_ap12-oak-experience-only-agents.md)** · the obstacle: **[Continual learning — why the networks go dead](../30-across-the-approaches/03_continual-learning-and-plasticity.md)**.
- Its parent, whose frame and critiques it inherits: **[AP4 · RL from interaction](../20-the-approaches/04_ap4-rl-from-interaction.md)** and the two AP4 deep dives.
- The cousin, and the other half of Part 7's second experiment: **[Ramp · AP9 open-endedness](01_ap9-open-endedness.md)**.
- The prerequisite and the sorting rule: **[what actually stays](00_the-shared-core.md)**.

---

## Check yourself *(try one, from memory)*

1. This ramp splits into two literatures with very different maturity. Name them and say which you start with, and why.
2. Which single document is the technical core of this bet, and who supervised it?
3. What is an *option*, and why does FC-STOMP collapse into hand-waving without it?
4. Rung 4 insists you read the counter-arguments. Give the two strongest, in one line each.
5. Part 7's second experiment connects AP9 and AP12. State the question in one sentence, and say why a negative result would still be worth publishing.

---

## Revision notes

- **rev 1 · 2026-09-09 · new.** Second ramp in group ⑥, written immediately after [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md) and the [continual-learning page](../30-across-the-approaches/03_continual-learning-and-plasticity.md), from the same live web pass. Follows the template set by [the AP9 ramp](01_ap9-open-endedness.md) with one structural difference forced by the material: this field splits into a *mature* half (continual learning — textbook, surveys, benchmarks, a dedicated conference in CoLLAs) and an *embryonic* half (OaK — one position paper, some talks, a two-month-old lab), and the ramp is built around that split rather than pretending to uniform depth. Locates Dohare's Alberta dissertation as the missing textbook, the Alberta Plan as the programme's only written statement, and CoLLAs as the reachable venue. Part 7's second experiment proposes an AP9 × AP12 intersection question — does plasticity loss explain why open-ended runs stall — flagged as unverified against the literature.
