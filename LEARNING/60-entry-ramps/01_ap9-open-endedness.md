---
id: c-ramp-ap9
sortkey: 6001
title: Ramp · AP9 open-endedness — every resource, and the route through them
domains: [frontier, approaches-to-agi, entry-ramps, resources]
level: core
prereqs: [c-shared-core, c-ap9-open-endedness]
provides: [ap9-reading-ladder, ap9-resource-inventory, qd-toolchain, ap9-first-experiment, ap9-venues]
status: ready
reading_time: 24 min
rev: 1
created: 2026-09-09
updated: 2026-09-09
---

# Ramp · AP9 open-endedness — every resource, and the route through them

*The bet you said you were drawn to: no human writes the goal. The system invents its own problems, and its own curriculum for solving them. This page is everything you need to get from the [approach card](../20-the-approaches/09_ap9-open-endedness.md) to doing work in it — every book, course, thesis, paper, blog, talk, library and venue I can find, why each one is here, and the order to take them in.*

> **You are here:** the first approach ramp in **⑥ Entry ramps**. The [card](../20-the-approaches/09_ap9-open-endedness.md) says what AP9 claims; the [deep dive](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md) opens the archive loop underneath it. **This page does not re-explain either** — it is the route in. Read [what actually stays](00_the-shared-core.md) first if you have not.

> **Where the facts come from:** a live web pass on **2026-09-09** — the `awesome-open-ended` community index, Lehman's dissertation, GECCO 2026 and ALIFE 2026 workshop calls, the ARC Prize 2026 ARC-AGI-3 competition page and technical report, the QDax and pyribs library papers, and the 2024–2026 paper record (Darwin Gödel Machine, AI Scientist v2, TerraLingua, *In Search of the Ingredients of Open-Endedness*). Everything dated below moves; the ladder's shape does not.

---

## In one minute

**There is no textbook for this field.** One popular book by its two founders, no university course anywhere, and a literature that is about eighty papers deep. That sounds like a problem and is actually the opportunity — a field small enough to read *completely* in a few months is a field where you can reach the frontier without permission.

The route: **one book** *(Stanley & Lehman's manifesto)* → **one thesis** *(Lehman's, which is the missing textbook)* → **four rungs of papers**, about thirty in total → **two libraries** *(pyribs, QDax)* → **one experiment you can run on a laptop**.

The single most important fact about the field in 2026: it has been **taken over by foundation models**. Every recent result — AlphaEvolve, the Darwin Gödel Machine, the AI Scientist, OMNI — is the same old archive loop with an LLM dropped into one or two slots. That is where the open questions are, and it means your LLM knowledge is not a detour from this approach. It is the entry ticket.

---

## Part 1 — the delta: what you must hold that the core doesn't give you

Six concepts. Everything else in this field is built out of these, and none of them is in a standard ML curriculum.

| # | Concept | Why it is here |
|---|---|---|
| 1 | **The archive** — keep a *set* of stepping stones, not a single best solution | The one mechanism under every open-ended method. If you understand only one thing, this. |
| 2 | **Behaviour space vs. search space** | Novelty is measured over what a solution *does*, not what it *is*. Choosing that space is the real design decision, and it is usually made badly. |
| 3 | **Novelty vs. quality vs. diversity** — and why QD wants all three | Novelty search alone fills the archive with garbage; the fix is the whole subfield. |
| 4 | **The minimal criterion** | POET's trick for keeping generated problems solvable-but-not-yet-solved. The generative half of open-endedness lives here. |
| 5 | **Deception and local optima** | The founding argument: the objective function itself is what blocks you. This is *why* the field exists, not a detail of it. |
| 6 | **Interestingness (and why it cannot be defined)** | The field's open wound. Novelty is computable; interestingness is not. Foundation models are the current, contested, patch. |

::: note
**Concepts 1–4 you already met** in the [AP9 deep dive](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md) — the archive loop, behaviour-space distance, MAP-Elites' grid, POET's minimal criterion. What that page gave you was the shape. What this ramp gives you is where to get the mechanics and the current literature.
:::

---

## Part 2 — books

**Be clear-eyed: there is one real book, and it is not a textbook.** This is genuinely true of the field, not a gap in searching. Open-endedness as a named research programme is about ten years old; nobody has written the textbook yet. What follows is the honest best available.

| Book | Status | Why it is here |
|---|---|---|
| **Stanley & Lehman, *Why Greatness Cannot Be Planned: The Myth of the Objective*** (Springer, 2015) | 🛒 **Buy it.** ~$25–30, ~150 pages | The field's manifesto, by the two people who started it. It is a *popular* book — no equations — and it is still the correct first thing to read, because it makes the argument the whole approach rests on: that an objective function is often the thing preventing you from reaching the objective. Everyone in this field has read it; it is the shared reference. Read it in a weekend. |
| **Eiben & Smith, *Introduction to Evolutionary Computing*** (2nd ed., Springer, 2015) | 🛒 Buy, or library | The standard textbook of the parent field. Novelty search and MAP-Elites *are* evolutionary algorithms, and papers assume you know selection, mutation, crossover, and population dynamics without saying so. You need Chapters 1–6, not the book. |
| **Yannakakis & Togelius, *Artificial Intelligence and Games*** (Springer) — **free** at `gameaibook.org` | 🆓 Free | Not obviously about open-endedness, and it matters anyway: open-ended systems are almost always evaluated in *game* environments, procedural content generation is a sister field, and Togelius is a central AP9 figure. The PCG chapter is the relevant one. |
| **Sutton & Barto**, Ch. 1–6, 13 — **free** | 🆓 Free | The RL prerequisite named in [the core](00_the-shared-core.md). AP9 methods generate *environments*; something still has to learn in them. |
| **Mitchell, *Complexity: A Guided Tour*** (OUP) | 🛒 Optional | Background on emergence and complex systems — the intellectual water this field swims in. Skip unless the ALife framing appeals to you. |

::: warn
**What not to do:** wait for a better book. It is not coming soon, and treating the absence as a blocker is how people stay out of young fields. The substitute for a textbook here is **one dissertation plus a paper ladder**, which is Parts 3 and 4.
:::

---

## Part 3 — theses: the missing textbook

In a field with no textbook, **PhD dissertations are the textbook.** A good one is 150–250 pages, written to be read by someone who does not yet know the field, with the full derivation and the full literature review — exactly what a textbook does, three years earlier.

| Thesis | Access | Why |
|---|---|---|
| ⭐ **Joel Lehman, *Evolution Through the Search for Novelty*** (UCF, 2012; advisor Kenneth Stanley) | 🆓 Free PDF — `joellehman.com/lehman-dissertation.pdf` | **The single most valuable document in this ramp.** It is the founding idea developed at book length by its inventor: why objective functions deceive, what novelty search is, how it behaves, where it fails, with the experiments. Read this instead of looking for a textbook. If you read one long thing about AP9, read this. |
| **Kenneth Stanley's NEAT dissertation** (UT Austin, 2004) | 🆓 Findable free | Background — the neuroevolution machinery Stanley built *before* novelty search, and which several AP9 systems still sit on. Optional, and lower priority than Lehman's. |
| **Recent QD and open-endedness dissertations** — Antoine Cully's group (Imperial College London), Jeff Clune's group (UBC) | 🆓 University repositories | I have not verified specific titles, so treat this as a search instruction rather than a citation: look up recent PhD theses from these two groups. In a field this young, a 2024–2026 thesis *is* the state-of-the-art review, and it will be free. |

---

## Part 4 — the paper ladder

About thirty papers, in five rungs. **This is the whole field.** Read in order; each rung assumes the one below.

**Column key** — 🟢 read it yourself, it is readable · 🟡 read the abstract and results, hand me the method · 🔴 hand to me first, then read with the summary beside you.

### Rung 1 · The founding idea (2008–2015)

| Paper | | Why |
|---|---|---|
| Lehman & Stanley, **Abandoning Objectives: Evolution Through the Search for Novelty Alone** (2011) | 🟢 | The origin. Rewarding *only* novelty beats rewarding the goal, on the goal. Everything downstream is a response to this. |
| Lehman & Stanley, **Evolving a Diversity of Virtual Creatures through Novelty Search and Local Competition** (GECCO 2011) | 🟢 | Novelty alone → novelty *plus* quality. This is the birth of quality-diversity. |
| Mouret & Clune, **Illuminating Search Spaces by Mapping Elites** (2015) | 🟢 | **MAP-Elites.** The archive becomes a grid you fill. The most-used algorithm in the field, and the one you will implement first. |
| Soros & Stanley, **Identifying Necessary Conditions for Open-Ended Evolution** (Chromaria, ALIFE 2014) | 🟡 | Asks the awkward question — what *conditions* must hold for open-endedness at all? Still unresolved, still cited. |
| Brant & Stanley, **Minimal Criterion Coevolution** (2017) | 🟡 | The seed of POET's key trick: keep what merely *qualifies*, not what scores best. |

### Rung 2 · Generating the problems (2019–2022)

The move from "search openly" to "invent the tasks too" — the part that matches your interest most directly.

| Paper | | Why |
|---|---|---|
| ⭐ Wang, Lehman, Clune & Stanley, **POET: Paired Open-Ended Trailblazer** (2019) | 🟢 | **The centrepiece.** A system that endlessly generates its own environments *and* solves them, transferring solutions between them. This is "the agent designs its own goals" made concrete. |
| Wang et al., **Enhanced POET** (2020) | 🟡 | What broke in POET and how they patched it — more informative than the original about the field's real difficulties. |
| Dennis et al., **Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design** (PAIRED, 2020) | 🟡 | The RL-native formulation: environment design as a game between a generator and a solver. The bridge from AP9 into mainstream RL. |
| Jiang, Grefenstette & Rocktäschel, **Prioritized Level Replay** (2021) | 🟡 | A curriculum that costs almost nothing — a strong, simple baseline you should know before proposing anything fancier. |
| Parker-Holder et al., **Evolving Curricula with Regret-Based Environment Design** (ACCEL, 2022) | 🟡 | The current standard method for auto-curricula. If you build something here, this is what you compare against. |
| Open-Ended Learning Team (DeepMind), **Open-Ended Learning Leads to Generally Capable Agents** (2021) | 🟡 | What the approach looks like with a lab's compute behind it — and the clearest evidence that generated task-spaces produce *general* agents. |

### Rung 3 · The position papers — why anyone thinks this is the road to ASI

Short, argumentative, no maths. Read all four in one sitting.

| Paper | | Why |
|---|---|---|
| Stanley, Lehman & Soros, **Open-Endedness: The Last Grand Challenge You've Never Heard Of** (2017) | 🟢 | The field's founding call to arms. |
| Clune, **AI-GAs: AI-Generating Algorithms** (2019) | 🟢 | The strongest statement of the ambition: don't design the AI, design the *process that designs* the AI. This is the thesis your instinct is pointing at. |
| Hughes et al. (DeepMind), **Open-Endedness is Essential for Artificial Superhuman Intelligence** (2024) | 🟢 | The 2024 restatement with a formal definition — open-endedness relative to an observer — and a serious lab behind it. |
| Lehman et al., **Evolution and the Knightian Blindspot of Machine Learning** (2025) | 🟡 | The newest and sharpest critique of everything else in ML: that it has no way to handle genuine unknown-unknowns, and evolution does. |

### Rung 4 · The foundation-model turn (2022–2026) — where the field is *now*

The archive loop, with an LLM in one or more slots. **This is the live frontier and the rung where your existing LLM knowledge pays.**

| Paper | | Why |
|---|---|---|
| Lehman et al., **Evolution through Large Models** (ELM, 2022) | 🟡 | The hinge. An LLM as the *mutation operator* — variation stops being random. Everything after this is downstream. |
| Zhang, Clune et al., **OMNI: Open-endedness via Models of human Notions of Interestingness** (2023) | 🟢 | The direct attack on the field's open wound — use a foundation model to supply *interestingness*, the thing nobody can define. |
| Faldor, Clune et al., **OMNI-EPIC** (2024) | 🟡 | OMNI plus environments-as-code: the model writes the tasks themselves. |
| Wang et al., **Voyager** (2023) | 🟢 | An LLM agent in Minecraft that invents its own goals and grows a skill library. The most legible demo of your instinct working. |
| Ma et al., **Eureka** (2023) | 🟡 | An LLM *writes the reward function*. Directly relevant to your "but someone still designs the goal" objection. |
| Hu, Lu & Clune, **Automated Design of Agentic Systems** (ADAS, 2025) | 🟡 | The search space becomes *agent architectures*, written in code. |
| Lu et al., **The AI Scientist** (2024) · Yamada et al., **v2** (2025) | 🟡 | The loop pointed at research itself — generate hypothesis, run experiment, write paper. Contested, important, and the clearest picture of where this is heading. |
| ⭐ Zhang, Hu, Lu, Lange & Clune, **Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents** (ICLR 2026) | 🔴 | **The current headline.** An agent that rewrites its own code, keeping an archive of its own variants. Read this one with me. |
| Dharna, Lu & Clune, **Foundation Model Self-Play** (2025) | 🟡 | Open-ended strategy discovery without hand-written objectives. |
| Lu et al., **Automated Capability Discovery via Model Self-Exploration** (2025) | 🟡 | A model finding out what it can do, by itself. |
| ⭐ Earle et al., **In Search of the Ingredients of Open-Endedness** (2026) | 🟡 | **Newest, and the most useful for finding a question of your own** — it tries to isolate what actually makes a system open-ended rather than merely busy. |
| Paolo, Meyerson, Miikkulainen et al., **TerraLingua: Emergence and Analysis of Open-Endedness in LLM Ecologies** (2026) | 🟡 | Open-endedness emerging in populations of language models. |

### Rung 5 · Safety — non-optional here specifically

An open-ended system is, by construction, one that produces things you did not specify. That is the whole point and the whole danger, and this is the one approach where the safety literature is part of the technical literature.

| Paper | | Why |
|---|---|---|
| Ecoffet, Clune & Lehman, **Open Questions in Creating Safe Open-Ended AI** (2020) | 🟢 | By the field's own founders. Short, honest, unresolved. |
| Sheth et al., **Safety is Essential for Responsible Open-Ended Systems** (2025) | 🟢 | The 2025 restatement. |
| Cross-reference: **[Alignment, control and self-improvement](../30-across-the-approaches/02_alignment-control-and-self-improvement.md)** | — | Already written, and AP9 is the approach it most directly concerns. |

---

## Part 5 — courses, talks and channels

::: warn
**There is no university course on open-endedness.** Anywhere. I looked. This is not a gap in my search — the field is too young and too small to have been taught. **In this field, conference talks replace lecture series**, and the talks below are the substitute. Do not wait for a course.
:::

| What | Access | Why |
|---|---|---|
| ⭐ **Jeff Clune — *Open-ended and AI-generating algorithms in the era of foundation models*** (2025) | 🆓 YouTube | The best single hour available. The whole programme, current, from the person driving it. **Watch this first, before any paper.** |
| **Tim Rocktäschel — *Open-Endedness, World Models, and the Automation of Innovation*** (2025) | 🆓 YouTube | The DeepMind view; connects AP9 to AP5. |
| **Kenneth Stanley — *Novel Opportunities in Open-Endedness*** (2022) | 🆓 YouTube | The founder's framing. |
| **Jeff Clune — *Endlessly Generating Increasingly Complex and Diverse Learning Environments*** (2019) | 🆓 YouTube | The POET talk. Watch alongside the POET paper. |
| **Berkeley CS 185/285 — Deep RL** (Spring 2026, Levine) | 🆓 YouTube + site | The RL machinery, on demand. Not an AP9 course. |
| **Evolutionary computation courses** — Glasgow (Coursera, free audit), IIT Guwahati (NPTEL, free) | 🆓 Free | The EC half, if Eiben & Smith is too dry. Neither mentions open-endedness. |
| **`quality-diversity.github.io`** | 🆓 | The QD community's own hub — algorithms, papers, tutorials. |
| ⭐ **`github.com/jennyzzt/awesome-open-ended`** | 🆓 | **The living index of the entire field**, maintained by a Clune-group researcher. Everything in Part 4 came from here plus verification. Star it; it is your update feed. |

**People to follow:** Jeff Clune (UBC / DeepMind) · Kenneth Stanley · Joel Lehman *(also writes unusually good essays — the LLM poetry-breeding and life-changing-books pieces are worth reading for how a researcher plays)* · Tim Rocktäschel (DeepMind / UCL) · Antoine Cully (Imperial, QD) · Julian Togelius (NYU, games + PCG) · Sakana AI (the AI Scientist line) · Jenny Zhang (DGM).

---

## Part 6 — code

| Library | Use it for |
|---|---|
| ⭐ **pyribs** — `docs.pyribs.org` | **Start here.** A deliberately bare-bones QD library, plain Python, no exotic dependencies, with real tutorials. Designed to be readable by someone with basic Python. This is where your first experiment runs. |
| **QDax** — JAX-based, from Cully's group | Hardware-accelerated QD when pyribs gets too slow, plus RL and multi-objective baselines. Move here when speed matters, not before. |
| **The Darwin Gödel Machine and AI Scientist repos** | Reading material more than tooling — read them to see what a modern open-ended system actually looks like in code. |
| **ARC-AGI-3 agent harness** *(ARC Prize)* | The interactive benchmark, if you take the route in Part 8. |

---

## Part 7 — the open problems

Where the field is genuinely stuck, as of 2026. These are your candidate questions.

1. **Nobody can measure open-endedness.** There is no accepted metric. Hughes et al. (2024) define it relative to an *observer*; Soros & Stanley have been asking since 2014. A system that "keeps producing new things" and one that has quietly started cycling look identical on most plots. **This is the field's biggest unsolved problem and the most attackable one on a laptop.**
2. **Novelty is not interestingness.** Novelty is computable and it fills your archive with junk. Foundation models are the current patch (OMNI), which relocates the problem: now interestingness means *what a human-trained model finds interesting*, which caps you at human priors. Exactly the objection your instinct is reaching for.
3. **It does not scale past toy domains.** POET's environments are 2D walkers. Nearly everything in Rung 2 lives in small worlds, and it is unclear whether the mechanisms survive contact with anything bigger.
4. **The foundation-model turn may be a ceiling in disguise.** If the LLM supplies the variation, the interestingness and the curriculum, is the system open-ended — or is it exploring the space the LLM already contains? *(This is the same question [AP4 #2](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md) asks about RL: source or tool?)*
5. **Safety is unresolved and structural**, not a bolt-on. See Rung 5.

---

## Part 8 — your first experiment

Two, in increasing ambition. **Do the first one; it fits in a weekend.**

### ① The behaviour-descriptor experiment *(laptop, no GPU, one weekend)*

**Question:** In MAP-Elites, how much of the result is determined by the choice of behaviour space rather than the algorithm?

**Why this one.** It aims straight at open problem #2 and at delta-concept #2 — the design decision everyone makes and almost nobody justifies. It needs no GPU. And it is the kind of question where a careful negative result is publishable as a workshop abstract.

**How.** Run pyribs' MAP-Elites tutorial to completion. Then change *only* the behaviour descriptor — two or three different definitions of "different" for the same domain — and measure how coverage, QD-score and the shape of the archive move. Write down what you expected before you run it.

**What you learn even if nothing interesting happens:** the whole QD toolchain, the metrics the field uses, and how to run a controlled comparison. That is the [once rule](00_the-shared-core.md) being paid.

### ② ARC-AGI-3 *(the ambitious one)*

An agent dropped into a handcrafted world with **no instructions, no rules, no stated goals** — it must explore, work out how the world works, discover what winning means, and carry that forward. That is your stated interest, built into a benchmark with a public leaderboard.

**The numbers as of the March 2026 launch:** humans **100%**, the best frontier model **0.51%**. The gap is not a compute gap.

**The competition:** ARC Prize 2026, the ARC-AGI-3 track carries **$850,000** — a $700K grand prize plus **milestone prizes at 30 June 2026 (passed) and 30 September 2026**. Entry is free, submissions run on Kaggle, no internet at evaluation, and **all code must be open-sourced to be eligible**.

::: warn
**The September milestone is about three weeks away** from today's date on this page (2026-09-09). That is not enough time to enter well from a standing start, and rushing it would produce a bad submission with your name on it. Treat the deadline as information about the *shape* of the opportunity, not as this month's target — the competition and the benchmark both continue.
:::

---

## Part 9 — where to publish, with no affiliation

You said you want to produce something novel and publish it yourself. This is more possible in AP9 than in almost any other approach on the map, because the venues are small, workshop-friendly, and used to independent submissions.

| Venue | What it takes | Notes |
|---|---|---|
| **GECCO workshops** (ACM, evolutionary computation) | **Extended abstract: 4 pages** including references, or a full paper at 8 | The realistic first publication. Workshops explicitly invite early-stage ideas. *Note: from 1 January 2026 ACM is fully open access, so budget for an APC unless a fee waiver applies.* |
| **ALIFE conference** — ALIFE 2026, Waterloo, 20 August 2026, with an open-world/ALife workshop track | Workshop papers and abstracts | The field's other home. Friendlier to unusual work than a mainline ML conference. |
| **ICLR / NeurIPS workshops** on open-endedness, agents, or ALOE | Short workshop papers | Higher visibility, higher bar, no APC. Watch the calls each cycle. |
| **arXiv + a public repo** | Nothing but the work | Not peer review, and in this field it is genuinely how work circulates. A clean repo plus a clear write-up is a real artifact. |

::: key
**The realistic first target** is a four-page GECCO workshop abstract on a negative or partial result — for example, the behaviour-descriptor experiment above, done carefully. That is a genuinely achievable first publication within a year, and it is a far better thing to show a lab than a certificate.
:::

---

## Part 10 — the best idea in this bet

*(What a synthesis would take from AP9, and what it would have to leave behind.)*

**Take: the archive.** Not novelty search, not MAP-Elites specifically — the underlying move, which is to **keep a diverse population of stepping stones instead of converging on a single best solution, and to generate the next problem from what you already have.** That idea is portable into every other approach on the map, and it is already leaking into them: it is what the Darwin Gödel Machine does to agent code, what AlphaEvolve does to programs, what auto-curricula do to RL environments. If you build a synthesis, this is the piece AP9 contributes.

**Leave: the belief that novelty is a sufficient signal.** The founding result — abandon objectives, reward novelty alone — is a beautiful and genuine discovery, and it does not scale. In any rich space, "new" is cheap and infinite. Every serious system since 2011 has had to smuggle quality, or a minimal criterion, or a human notion of interestingness back in. **The honest reading is that open-endedness needs a taste function, and nobody has one that isn't borrowed from humans.** That is what your instinct — less human intervention, more the system itself — will collide with first, and it is exactly where a new idea would be worth the most.

---

## ⚠️ Honesty box

- **The paper list is inventoried, not read.** I assembled Rungs 1–5 from the community index plus verification of the key items, and I have read the ones this project's [AP9 card](../20-the-approaches/09_ap9-open-endedness.md) and [deep dive](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md) were grounded in. The 🟢/🟡/🔴 difficulty tags are estimates from abstracts and venue, not from having read every one.
- **Two thesis entries are search instructions, not citations.** Lehman's dissertation I verified, including the URL. The Cully-group and Clune-group theses I did not — I am telling you where to look, not what to cite.
- **The "no university course exists" claim is a negative, and negatives are hard.** I searched and found none; a course may exist somewhere I did not look. The positive part — that conference talks are how this field transmits — I am confident about.
- **Prices and deadlines move.** The book price, the ARC Prize milestone dates, GECCO's open-access charges: all checked 2026-09-09, all subject to change. Re-check before acting on any of them.
- **Part 10 is an opinion.** "Take the archive, leave novelty-as-sufficient-signal" is my reading of the field's arc, not a consensus. The field's founders would put it differently, and Lehman's 2025 Knightian-blindspot paper is a live argument that the novelty side has been given up on too early.
- **This ramp cannot tell you whether AP9 is right for you.** It can only make the field reachable. Whether the instinct that drew you here survives contact with the open problems in Part 7 is something only Part 8 answers.

---

## Connections

- The bet itself: **[AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md)** · the mechanism: **[AP9 deep dive — the open-ended engine](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md)**.
- The neighbours in your cluster: **[AP8's ARC-AGI-3 turn](../50-deep-dives/03_ap8-deep-dive-the-research-frontier.md)** *(an agent with no stated goals)* · **[AP4 · the reward is the whole game](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md)** *(where the hand-written reward runs out)* · **[AP5 · learning without a teacher](../50-deep-dives/05_ap5-deep-dive-learning-without-a-teacher.md)** *(no labels, no teacher)*.
- Why this approach's safety literature is technical, not ethical garnish: **[Alignment, control and self-improvement](../30-across-the-approaches/02_alignment-control-and-self-improvement.md)**.
- The prerequisite and the sorting rule: **[what actually stays](00_the-shared-core.md)**.

---

## Check yourself *(try one, from memory)*

1. Why does this field have no textbook, and what are the two things that replace one?
2. What is the archive, and why is it the one mechanism under every open-ended method?
3. POET generates its own environments. What stops it generating ones that are impossible or trivial?
4. The field's biggest unsolved problem is measurement. Say why "it keeps producing new things" is not enough.
5. Foundation models supply interestingness, which novelty search could not. What does that fix, and what does it quietly cap?

---

## Revision notes

- **rev 1 · 2026-09-09 · new.** First approach ramp in group ⑥, written first *(rather than AP1)* because the learner identified their interest as systems where the agent sets its own goals rather than a human writing the reward — which is AP9. Built from a live web pass: the `awesome-open-ended` community index cross-checked against searches, Lehman's dissertation located and verified free, GECCO 2026 / ALIFE 2026 workshop formats, the ARC Prize 2026 ARC-AGI-3 track (prize structure, 30 September 2026 milestone, humans 100% vs frontier 0.51%), pyribs and QDax, and the 2024–26 record through the Darwin Gödel Machine (ICLR 2026) and *In Search of the Ingredients of Open-Endedness* (2026). Establishes the ramp template for the remaining ten: delta concepts → books → theses → paper ladder in rungs → courses/talks → code → open problems → first experiment → venues → **the best idea in this bet**, the last existing so that eleven ramps compose into one synthesis rather than eleven reading lists.
