---
id: c-ramp-ap9
sortkey: 6001
title: Ramp · AP9 open-endedness — every resource, and the route through them
domains: [frontier, approaches-to-agi, entry-ramps, resources]
level: core
prereqs: [c-shared-core, c-ap9-open-endedness]
provides: [ap9-reading-ladder, ap9-resource-inventory, qd-toolchain, ap9-first-experiment, ap9-venues]
status: ready
reading_time: 35 min
rev: 3
created: 2026-09-09
updated: 2026-09-09
---

# Ramp · AP9 open-endedness — every resource, and the route through them

*The bet you said you were drawn to: no human writes the goal. The system invents its own problems, and its own curriculum for solving them. This page is everything you need to get from the [approach card](../20-the-approaches/09_ap9-open-endedness.md) to doing work in it — every book, course, thesis, paper, blog, talk, library and venue I can find, why each one is here, and the order to take them in.*

> **You are here:** the first approach ramp in **⑥ Entry ramps**. The [card](../20-the-approaches/09_ap9-open-endedness.md) says what AP9 claims; the [deep dive](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md) opens the archive loop underneath it. **This page does not re-explain either** — it is the route in. Read [what actually stays](00_the-shared-core.md) first if you have not.

> **Where the facts come from:** a live web pass on **2026-09-09** — the `awesome-open-ended` community index, Lehman's dissertation, GECCO 2026 and ALIFE 2026 workshop calls, the ARC Prize 2026 ARC-AGI-3 competition page and technical report, the QDax and pyribs library papers, and the 2024–2026 paper record. **Part 5 additionally rests on a direct YouTube sweep** run the same day — ten topic queries plus lab-channel enumeration, ~130 distinct videos, durations and channels read off the platform.
>
> **Rev 3 adds an independent audit of Parts 2–4**, run the same day and deliberately *without* the community index: every paper in Part 4 was checked against the **arXiv API** — title, author list, first-version date, journal reference — and a separate 22-query sweep of arXiv looked for what the ladder was missing. Every arXiv id below was confirmed in that pass. The full report, including what it got wrong: [`REVIEWS/AUDIT_2026-09-09_ap9-ladder.md`](../../REVIEWS/AUDIT_2026-09-09_ap9-ladder.md). Everything dated below moves; the ladder's shape does not.

---

## In one minute

**No textbook has open-endedness as its subject, and no full course exists** — one popular book by its two founders, one textbook *chapter* on its founding mechanism, one conference tutorial, and a literature about eighty papers deep. That sounds like a problem and is actually the opportunity: a field small enough to read *completely* in a few months is a field where you can reach the frontier without permission.

The route: **one book** *(Stanley & Lehman's manifesto)* → **one textbook section you already own** *(Iba §2.6, for the mechanics)* → **two theses** *(Lehman's for the founding half, Samvelyan's for the environment-design half)* → **six rungs of papers**, about forty in total → **two libraries** *(pyribs, QDax)* → **one experiment you can run on a laptop**.

What *does* exist in quantity is **video** — a 2½-hour ICML tutorial, a dozen full-length talks, three channels doing line-by-line paper walkthroughs, a decade of long-form interviews with the founders, and a recorded academic workshop series almost nobody has watched. Part 5 is the map of it, and for you specifically it is the most useful section on this page: **paper explainers are the fastest available fix for not yet being able to read papers cold.**

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

**There is no textbook *of open-endedness*, and there is more book-length material than rev 2 of this page admitted.** The precise, defensible claim: nobody has written a textbook whose subject is open-endedness — the named research programme is only about ten years old. What rev 2 said instead was *"there is one real book"* and *"nobody has written the textbook yet,"* and both are false, because the field's founding mechanism is taught as a **section of a 2025 evolutionary-computation textbook** that was sitting in this project's own corpus the whole time.

::: warn
**How that error happened, because it is the same error twice.** Rev 1 of Part 5 said no course existed "anywhere — I looked," on the strength of one GitHub list. Rev 2 fixed that sentence and then wrote *this* one — a second confident negative, asserted without searching, in the section right above it. **The rule this page now runs on: never state that something does not exist until you have run the same search against something you know *does* exist.** A search that returns nothing looks identical whether the thing is absent or your tool is broken. Both times here, it was the tool.
:::

| Book | Status | Why it is here |
|---|---|---|
| **Stanley & Lehman, *Why Greatness Cannot Be Planned: The Myth of the Objective*** (Springer, 2015) | 🛒 **Buy it.** ~$25–30, ~150 pages | The field's manifesto, by the two people who started it. It is a *popular* book — no equations — and it is still the correct first thing to read, because it makes the argument the whole approach rests on: that an objective function is often the thing preventing you from reaching the objective. Everyone in this field has read it; it is the shared reference. Read it in a weekend. |
| ⭐ **Hitoshi Iba, *Deep Swarm and Evolution for Generative Artificial Intelligence*** (CRC Press, 1st ed., 2025) | 📁 **Already in your corpus** — `RESOURCES/corpus/textbooks/hitoshi-i-deep-swarm-and-evolution-for-generative-artif/` | **The closest thing to a textbook treatment you have, and you already own it.** §2.6 is titled *"Novelty search"* and derives it properly — fitness versus novelty, distance to previously discovered individuals, why the objective deceives — citing Lehman & Stanley directly. **MAP-Elites** is in the index (p. 57), as is *progressive minimal criteria novelty search* (p. 55). It is a book about evolutionary computation for generative AI, **not** about open-endedness, so it will not give you POET or the foundation-model turn. What it gives you is the mechanics of Rung 1 written by a textbook author instead of a paper author, in text you can grep. Read §2.6 before Rung 1. |
| **Eiben & Smith, *Introduction to Evolutionary Computing*** (2nd ed., Springer, 2015) | 🛒 Buy, or library | The standard textbook of the parent field. Novelty search and MAP-Elites *are* evolutionary algorithms, and papers assume you know selection, mutation, crossover, and population dynamics without saying so. You need Chapters 1–6, not the book. **If Iba's §2.6 lands, you may not need this at all** — check before spending. |
| **Yannakakis & Togelius, *Artificial Intelligence and Games*** (Springer) — **free** at `gameaibook.org` | 🆓 Free | Not obviously about open-endedness, and it matters anyway: open-ended systems are almost always evaluated in *game* environments, procedural content generation is a sister field, and Togelius is a central AP9 figure. The PCG chapter is the relevant one. |
| **Sutton & Barto**, Ch. 1–6, 13 — **free** | 🆓 Free | The RL prerequisite named in [the core](00_the-shared-core.md). AP9 methods generate *environments*; something still has to learn in them. |
| **Mitchell, *Complexity: A Guided Tour*** (OUP) | 🛒 Optional | Background on emergence and complex systems — the intellectual water this field swims in. Skip unless the ALife framing appeals to you. |

::: warn
**What not to do:** wait for a better book. It is not coming soon, and treating the absence as a blocker is how people stay out of young fields. The substitute for a textbook here is **one dissertation plus a paper ladder**, which is Parts 3 and 4.
:::

---

## Part 3 — theses: the missing textbook

Iba's §2.6 (Part 2) will give you novelty search, and nothing after it. For everything else, **PhD dissertations are the textbook.** A good one is 150–250 pages, written to be read by someone who does not yet know the field, with the full derivation and the full literature review — exactly what a textbook does, three years earlier.

| Thesis | Access | Why |
|---|---|---|
| ⭐ **Joel Lehman, *Evolution Through the Search for Novelty*** (UCF, 2012; advisor Kenneth Stanley) | 🆓 Free PDF — `joellehman.com/lehman-dissertation.pdf` | **The single most valuable document in this ramp.** It is the founding idea developed at book length by its inventor: why objective functions deceive, what novelty search is, how it behaves, where it fails, with the experiments. Read this instead of looking for a textbook. If you read one long thing about AP9, read this. |
| **Kenneth Stanley's NEAT dissertation** (UT Austin, 2004) | 🆓 Findable free | Background — the neuroevolution machinery Stanley built *before* novelty search, and which several AP9 systems still sit on. Optional, and lower priority than Lehman's. |
| ⭐ **Mikayel Samvelyan, *Robust Agents in Open-Ended Worlds*** (2025) | 🆓 Free — **arXiv 2512.08139** | **Verified, and it covers the half Lehman's does not.** Lehman gives you the *founding* half — novelty and divergent search. This gives you **environment design, auto-curricula and robustness**: the UED lineage that runs PAIRED → PLR → ACCEL. Samvelyan wrote MAESTRO and Rainbow Teaming (Rungs 2 and 4), so this is the literature review for three ladder papers at once. Read it after Rung 2, not before. |
| **Recent QD dissertations** — Antoine Cully's group (Imperial College London), Jeff Clune's group (UBC) | 🆓 University repositories | Still a **search instruction, not a citation** — I have not verified specific titles from these two groups. In a field this young a 2024–2026 thesis *is* the state-of-the-art review, and it will be free. *(Rev 2 said this and pointed nowhere. Rev 3 at least points at Samvelyan's above, which is real.)* |

---

## Part 4 — the paper ladder

About **forty** papers, in **six** rungs. **This is the whole field.** Read in order; each rung assumes the one below.

**Column key** — 🟢 read it yourself, it is readable · 🟡 read the abstract and results, hand me the method · 🔴 hand to me first, then read with the summary beside you.

::: note
**Dates.** Each entry gives the **arXiv first-version year**, with the venue after it where they differ — because rev 2 mixed the two and quietly misordered the field's history. Where an arXiv id is shown, it was verified against the arXiv API on 2026-09-09.
:::

### Rung 1 · The founding idea (2008–2016)

| Paper | | Why |
|---|---|---|
| Lehman & Stanley, **Abandoning Objectives: Evolution Through the Search for Novelty Alone** (*Evolutionary Computation*, 2011) | 🟢 | The origin. Rewarding *only* novelty beats rewarding the goal, on the goal. Everything downstream is a response to this. |
| Lehman & Stanley, **Evolving a Diversity of Virtual Creatures through Novelty Search and Local Competition** (GECCO 2011) | 🟢 | Novelty alone → novelty *plus* quality. This is the birth of quality-diversity. |
| ⭐ **Pugh, Soros & Stanley, Quality Diversity: A New Frontier for Evolutionary Computation** (*Frontiers in Robotics and AI* 3:40, 2016) | 🟢 | **The paper that named the subfield**, free and open access. Rev 2 taught you quality-diversity as delta-concept #3 without ever citing the paper that defined it as a research programme. It is also the clearest single statement of *why* nature's divergent-and-local-optimising search is a different thing from optimisation. |
| Mouret & Clune, **Illuminating Search Spaces by Mapping Elites** (2015 · arXiv 1504.04909) | 🟢 | **MAP-Elites.** The archive becomes a grid you fill. The most-used algorithm in the field, and the one you will implement first. |
| ⭐ **Cully, Clune, Tarapore & Mouret, Robots that can adapt like animals** (2014 · arXiv 1407.3501 · ***Nature* 521, 503–507, 2015**) | 🟢 | **The result that made anyone care about MAP-Elites.** A six-legged robot loses a leg and recovers a working gait in under two minutes, by searching a behaviour map built *before* the damage. Rev 2 gave you the algorithm paper and not the demonstration — which is backwards, because this is the one that shows what an archive is *for*. |
| Secretan et al., **Picbreeder: A Case Study in Collaborative Evolutionary Exploration of Design Space** (*Evolutionary Computation*, 2011) | 🟡 | Humans collaboratively evolving images, and the source of the field's favourite anecdote — that nobody *aiming* at a car would have found the car. Here because Rung 4's Earle et al. (2026) is a direct replication of it, and that paper is unreadable without knowing what Picbreeder was. |
| Soros & Stanley, **Identifying Necessary Conditions for Open-Ended Evolution** (Chromaria, ALIFE 2014) | 🟡 | Asks the awkward question — what *conditions* must hold for open-endedness at all? Still unresolved, still cited. |
| Brant & Stanley, **Minimal Criterion Coevolution** (GECCO 2017) | 🟡 | The seed of POET's key trick: keep what merely *qualifies*, not what scores best. |

::: key
**The reference shelf — two papers to consult, not to read straight through.** Keep these open while you do Part 8's experiment rather than reading them now:

- **Cully & Demiris, *Quality and Diversity Optimization: A Unifying Modular Framework*** (2017 · arXiv **1708.09251**) — shows that novelty search, MAP-Elites and their variants are **one algorithm with swappable parts** (container, selector, scoring). The single most useful thing to have read before you design a QD experiment, because it tells you which knob you are actually turning.
- **Chatzilygeroudis, Cully, Vassiliades & Mouret, *Quality-Diversity Optimization: a novel branch of stochastic optimization*** (2020 · arXiv **2012.04322**) — the field's survey. Use it as a map when a paper cites something you do not recognise.
:::

### Rung 2 · Generating the problems (2019–2022)

The move from "search openly" to "invent the tasks too" — the part that matches your interest most directly.

| Paper | | Why |
|---|---|---|
| ⭐ Wang, Lehman, Clune & Stanley, **POET: Paired Open-Ended Trailblazer** (2019 · arXiv 1901.01753) | 🟢 | **The centrepiece.** A system that endlessly generates its own environments *and* solves them, transferring solutions between them. This is "the agent designs its own goals" made concrete. |
| Wang, Lehman, Rawal, Zhi, Li, Clune & Stanley, **Enhanced POET** (2020 · arXiv 2003.08536 · ICML 2020) | 🟡 | What broke in POET and how they patched it — more informative than the original about the field's real difficulties. **Read its stagnation discussion carefully**: it names the two ways an open-ended run dies (domains stop getting harder; solvers get stuck below what is solvable). That is the sharpest statement of open problem #1 anyone has written, and Part 8's second experiment aims straight at it. |
| Dennis et al., **Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design** (PAIRED, 2020 · arXiv 2012.02096) | 🟡 | The RL-native formulation: environment design as a game between a generator and a solver. The bridge from AP9 into mainstream RL. |
| Jiang, Grefenstette & Rocktäschel, **Prioritized Level Replay** (2020 · arXiv 2010.03934 · ICML 2021) | 🟡 | A curriculum that costs almost nothing — a strong, simple baseline you should know before proposing anything fancier. |
| Parker-Holder et al., **Evolving Curricula with Regret-Based Environment Design** (ACCEL, 2022 · arXiv 2203.01302 · ICML 2022) | 🟡 | The current standard method for auto-curricula. If you build something here, this is what you compare against. |
| Samvelyan, Khan, Dennis, Jiang et al., **MAESTRO: Open-Ended Environment Design for Multi-Agent RL** (2023 · arXiv 2303.03376 · ICLR 2023) | 🟡 | UED once there is a *second agent* in the world, so the environment and the opponent both have to be generated. The step from "design a level" to "design a situation", and the natural place this line goes next. |
| Open-Ended Learning Team (DeepMind), **Open-Ended Learning Leads to Generally Capable Agents** (2021 · arXiv 2107.12808) | 🟡 | What the approach looks like with a lab's compute behind it — and the clearest evidence that generated task-spaces produce *general* agents. |

### Rung 3 · The position papers — why anyone thinks this is the road to ASI

Short, argumentative, no maths. Read all four in one sitting.

| Paper | | Why |
|---|---|---|
| Stanley, Lehman & Soros, **Open-Endedness: The Last Grand Challenge You've Never Heard Of** (O'Reilly, 2017) | 🟢 | The field's founding call to arms. |
| Clune, **AI-GAs: AI-Generating Algorithms** (2019 · arXiv 1905.10985) | 🟢 | The strongest statement of the ambition: don't design the AI, design the *process that designs* the AI. This is the thesis your instinct is pointing at. **Clune explains it himself** in a TWIML interview already sitting in your corpus — see Part 5 ⑤. |
| Hughes et al. (DeepMind), **Open-Endedness is Essential for Artificial Superhuman Intelligence** (2024 · arXiv 2406.04268 · ICML 2024) | 🟢 | The 2024 restatement with a formal definition — open-endedness relative to an observer — and a serious lab behind it. |
| ⭐ **Xu, Zhu & Van Roy, An Information-Theoretic Definition for Open-Ended Learning** (2026 · arXiv 2606.08369) | 🟡 | **A rival formalisation, and you should read it against Hughes.** Rev 2 presented "relative to an observer" as *the* formal definition of open-endedness. It is not the only one — this is a competing attempt from a different tradition, two years later. Open problem #1 says nobody can measure open-endedness; these two papers are the two serious tries, and **they disagree**. Disagreement is where a question of your own comes from. |
| Lehman, Meyerson, El-Gaaly, Stanley & Ziyaee, **Evolution and the Knightian Blindspot of Machine Learning** (2025 · arXiv 2501.13075) | 🟡 | The newest and sharpest critique of everything else in ML: that it has no way to handle genuine unknown-unknowns, and evolution does. |
| Kumar, Clune, Lehman & Stanley, **Questioning Representational Optimism in Deep Learning: The Fractured Entangled Representation Hypothesis** (2025 · arXiv 2505.11581) | 🟡 | All three founders plus Kumar, making the companion argument: that what gradient descent builds inside a network is *tangled and duplicated* where open-ended search builds something ordered and reusable — so the two produce different kinds of mind, not just different scores. If it holds, it is the technical reason this bet is not merely a different route to the same place. Speculative, contested, and the most interesting thing the founders have published recently. |

### Rung 4 · The foundation-model turn (2022–2026) — where the field is *now*

The archive loop, with an LLM in one or more slots. **This is the live frontier and the rung where your existing LLM knowledge pays.**

| Paper | | Why |
|---|---|---|
| Lehman, Gordon, Jain, Ndousse, Yeh & Stanley, **Evolution through Large Models** (ELM, 2022 · arXiv 2206.08896) | 🟡 | The hinge. An LLM as the *mutation operator* — variation stops being random. Everything after this is downstream. |
| Zhang, Lehman, Stanley & Clune, **OMNI: Open-endedness via Models of human Notions of Interestingness** (2023 · arXiv 2306.01711 · ICLR 2024) | 🟢 | The direct attack on the field's open wound — use a foundation model to supply *interestingness*, the thing nobody can define. |
| Faldor, Zhang, Cully & Clune, **OMNI-EPIC** (2024 · arXiv 2405.15568) | 🟡 | OMNI plus environments-as-code: the model writes the tasks themselves. |
| Wang et al., **Voyager** (2023 · arXiv 2305.16291) | 🟢 | An LLM agent in Minecraft that invents its own goals and grows a skill library. The most legible demo of your instinct working. |
| Ma et al., **Eureka** (2023 · arXiv 2310.12931 · ICLR 2024) | 🟡 | An LLM *writes the reward function*. Directly relevant to your "but someone still designs the goal" objection. |
| Ecoffet, Huizinga, Lehman, Stanley & Clune, **First return, then explore** (Go-Explore, 2020 · arXiv 2004.12919 · ***Nature* 590, 580–586, 2021**) | 🟡 | **The archive idea's biggest win outside evolution.** Remember promising states, *return* to them deliberately, then explore from there — and Montezuma's Revenge and Pitfall, the two exploration problems deep RL could not touch, fall. This is the strongest evidence for Part 10's claim that the archive is the portable idea, and rev 2 omitted it while citing the same authors' safety paper. |
| Lu, Hu & Clune, **Intelligent Go-Explore** (2024 · arXiv 2405.15143 · ICLR 2025) | 🟡 | Go-Explore with a foundation model deciding which states are interesting. Read straight after the above: it is the same algorithm with the hand-designed part replaced, which is the whole pattern of this rung in one comparison. |
| Hu, Lu & Clune, **Automated Design of Agentic Systems** (ADAS, 2024 · arXiv 2408.08435 · ICLR 2025) | 🟡 | The search space becomes *agent architectures*, written in code. **Its first author explains it** in a TWIML episode in your corpus — Part 5 ⑤. |
| Samvelyan et al., **Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts** (2024 · arXiv 2402.16822) | 🟡 | MAP-Elites pointed at LLM red-teaming — a QD archive whose cells are *attack styles*. Here for a blunt reason: it is the clearest example of this approach doing something a company will pay for, which matters if you want the lab job on the way. |
| Lu, Lu, Lange, Foerster, Clune & Ha, **The AI Scientist** (2024 · arXiv 2408.06292) · Yamada et al., **v2** (2025 · arXiv 2504.08066) | 🟡 | The loop pointed at research itself — generate hypothesis, run experiment, write paper. Contested, important, and the clearest picture of where this is heading. **Three of its authors are interviewed in your corpus** — Part 5 ⑤. |
| ⭐ Zhang, Hu, Lu, Lange & Clune, **Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents** (2025 · arXiv 2505.22954 · **ICLR 2026**) | 🔴 | **The current headline.** An agent that rewrites its own code, keeping an archive of its own variants. Read this one with me. |
| Iacob, Jovanović, Shen, Burkhardt, Kurmanji, Tastan et al., **The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators** (2026 · arXiv 2606.26294) | 🔴 | The DGM's successor problem: if an agent rewrites itself against a *fixed* evaluator it will learn to game the evaluator, so evolve the evaluator too. **Note who wrote it — not Clune's group.** The idea has escaped its founding lab, which is usually the sign a field is real. |
| Dharna, Lu & Clune, **Foundation Model Self-Play** (2025 · arXiv 2507.06466 · RLC 2025) | 🟡 | Open-ended strategy discovery without hand-written objectives. |
| Lu, Hu & Clune, **Automated Capability Discovery via Foundation Model Self-Exploration** (2025 · arXiv 2502.07577 · ICLR 2025) | 🟡 | A model finding out what it can do, by itself. *(Listed at ICLR under "…via Model Self-Exploration" — the arXiv title changed.)* |
| Kumar, Lu, Kirsch, Tang, Stanley, Isola & Ha, **Automating the Search for Artificial Life with Foundation Models** (ASAL, 2024 · arXiv 2412.17799) | 🟡 | The loop pointed at **artificial life** — a foundation model searching cellular-automata rule spaces for interesting worlds. The bridge from this rung back to the ALife tradition Part 5 ⑥ covers, and Stanley's own return to it. |
| ⭐ Earle, Arulkumaran, Dai, Kumar, Togelius & Risi, **In Search of the Ingredients of Open-Endedness: Replicating Picbreeder with Large Vision-Language Models** (2026 · arXiv 2605.23908 · GECCO 2026) | 🟡 | **Read the full title — rev 2 of this page did not, and described the paper wrongly.** It is a **replication**: re-run Picbreeder (Rung 1) with vision-language models standing in where the humans used to be, and see whether the open-ended magic survives the substitution. That is a sharper and more useful thing than the "isolate the ingredients" study rev 2 promised, because it is a *controlled* test of the rung's central assumption — that a foundation model can stand in for human taste. |
| Paolo, Warner, Shahrzad, Hodjat, Miikkulainen & Meyerson, **TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies** (2026 · arXiv 2603.16910) | 🟡 | Open-endedness emerging in populations of language models. |

### Rung 5 · Where it breaks — the case against

::: warn
**Rev 2 had no rung like this, and that was the worst structural fault on the page.** Rungs 1–4 are the field explaining why it is right, and Rung 6 is the field worrying about the consequences of being right. **Nowhere did anyone argue that the approach does not work.** You cannot judge a bet you have only heard defended — the same sentence this page already uses about the Doom Debates video in Part 5 ④, and it applies twice as hard to the papers.
:::

| Paper | | Why |
|---|---|---|
| ⭐ **Batra, Tjanaka, Nikolaidis & Sukhatme, Quality Diversity for Robot Learning: Limitations and Future Directions** (2024 · arXiv 2407.17515 · GECCO 2024) | 🟢 | **The strongest technical attack on the field's flagship method, and it is short.** The argument: a large share of published QD results are set up so that "learn an archive of behaviourally diverse policies" is solving a problem that **one goal-conditioned policy plus a classical planner already solves** — at constant space instead of one policy per cell, and with better generalisation to task variants. If that is right, much of the QD literature is measuring the wrong thing. Read it **before** you design Part 8's experiment, because it tells you which comparisons a reviewer will demand. |
| Enhanced POET's stagnation analysis *(Rung 2, re-read for this purpose)* | 🟡 | Not a separate paper — a re-read with a hostile eye. The authors themselves document that their system stalls in two distinct ways. Take that seriously and open problem #1 stops being abstract. |
| Soros & Stanley, *Identifying Necessary Conditions* *(Rung 1, re-read for this purpose)* | 🟡 | The founding worry, from inside: after a decade nobody has shown that any implemented system meets the conditions the field's own theorists set for open-endedness. |

::: key
**The honest state of the critique literature: it is thin.** One good technical takedown, plus the field's own admissions. That is genuinely different from AP1 or AP4, where the critiques are numerous and organised. **Read that fact as information about the field, not as evidence that the bet is safe** — a young field with few critics usually means few people have looked hard, not that it survived scrutiny. It is also an opening: a careful negative result here has little competition.
:::

### Rung 6 · Safety — non-optional here specifically

An open-ended system is, by construction, one that produces things you did not specify. That is the whole point and the whole danger, and this is the one approach where the safety literature is part of the technical literature.

| Paper | | Why |
|---|---|---|
| Ecoffet, Clune & Lehman, **Open Questions in Creating Safe Open-Ended AI: Tensions Between Control and Creativity** (2020 · arXiv 2006.07495) | 🟢 | By the field's own founders. Short, honest, unresolved. |
| Sheth, Wehner, Abdelnabi, Binkyte & Fritz, **Safety is Essential for Responsible Open-Ended Systems** (2025 · arXiv 2502.04512) | 🟢 | The 2025 restatement. *(Later versions are retitled "Safety Must Precede the Deployment of Open-Ended AI" — same paper, same id.)* |
| Cross-reference: **[Alignment, control and self-improvement](../30-across-the-approaches/02_alignment-control-and-self-improvement.md)** | — | Already written, and AP9 is the approach it most directly concerns. |

---

## Part 5 — video: the one tutorial, the talks, the channels, the archive

::: warn
**There is no full university course on open-endedness** — no semester of lectures, no problem sets, nowhere. But an earlier version of this page said flatly that *nothing* course-like existed "anywhere — I looked", and that was wrong: it was written from one GitHub list, without searching YouTube at all. There **is** a two-and-a-half-hour ICML tutorial, and there **is** an archived academic workshop series. Both are below. The corrected claim: **no course, but far more teaching material than the field's size suggests, scattered across seven different kinds of place.**
:::

### ① Start here — the orientation talks

Watch **one** of these before reading any paper in Part 4.

| Talk | Length | Why |
|---|---|---|
| ⭐ **Jeff Clune — *Open-ended and AI-generating algorithms in the era of foundation models*** (2025) | ~86–112 min | The best single item available: the whole programme, current, from the person driving it. **Posted in at least three places** — Clune's own channel, the Schwartz Reisman Institute, and alphaXiv. The alphaXiv posting is the longest and carries the most Q&A. |
| **Tim Rocktäschel — *Open-Endedness, World Models, and the Automation of Innovation*** (2025) | ~65 min | The DeepMind view; connects AP9 to AP5. Also posted in more than one place. |
| **Kenneth O. Stanley — *Novel Opportunities in Open-Endedness*** (UCL DARK) | ~52 min | The founder's framing, delivered to a research audience rather than a general one. |
| **Google DeepMind — *Open-Ended Learning Leads to Generally Capable Agents*** | ~15 min | Short official summary of the XLand result. Watch before the paper in Rung 2. |

### ② The one real tutorial ⭐

| What | Length | Why |
|---|---|---|
| **ICML 2019 Tutorial — *Recent Advances in Population-Based Search for Deep Neural Networks*** *(Evolving AI Lab; uploaded 17 June 2019)* | **152 min** | **The closest thing to a course that exists.** A full conference tutorial on the machinery under AP9 — neuroevolution, novelty search, quality-diversity, population-based methods. It is from 2019, so it predates the foundation-model turn entirely: take it for the *mechanics*, and let Part 4's Rung 4 supply the last six years. |

### ③ Paper explainers — the direct answer to "I can't read papers yet"

**Use these deliberately: watch the explainer, then read the paper the same day.** The video gives you the shape, so the paper's method section has somewhere to land. This is the fastest available fix for the reading gap, and it is the reason this section exists.

| Channel | What they cover here |
|---|---|
| **Yannic Kilcher** | **POET** (~34 min) · **Enhanced POET** (~16 min) · **ACCEL / regret-based environment design** (~44 min). Close walkthroughs of three of Rung 2's core papers. |
| **Connor Shorten** | **Novelty search** (~12 min) · **Enhanced POET** (~19 min) · **coevolution of agents and environments** (~9 min). Shorter and gentler than Kilcher. |
| **Aleksa Gordić — The AI Epiphany** | **POET** (~45 min), slower and more thorough than either. |

### ④ Long-form interviews — where the argument actually happens

Talks tell you what someone thinks. Interviews tell you *why*, and what they concede under pressure. In a field this young that is worth more than usual.

| Source | What |
|---|---|
| ⭐ **Machine Learning Street Talk** | The deepest well by far: **at least six Kenneth Stanley conversations** (*Why Greatness Cannot Be Planned* ~166 min · *AI Isn't Creative* ~136 min · *On Art and Subjectivity* ~85 min · *Why Every AI Model Is An Impostor* · *On Creativity and Serendipity* · and with **Julian Togelius** on AGI, games and diversity ~70 min), plus **Tim Rocktäschel** (*The AI Paradigm That Nobody Talks About*, ~55 min), **Joel Lehman** (*Can Machines Love?*, ~118 min), and an episode on **POET** (~73 min). |
| **Brain Inspired — BI 086, Ken Stanley: Open-Endedness** | ~96 min. Neuroscience-facing framing. |
| **The Jim Rutt Show EP130** · **Super Data Science** · **TWIML** (Rocktäschel, twice) | Alternative framings — useful if one interviewer's angle does not land for you. |
| ⭐ **Doom Debates — debate with Kenneth Stanley** | ~157 min. **Watch this one.** It is the only item in this ramp where someone argues *against* him at length. Rung 3 gives you the case for; this is the case against, and you cannot judge a bet you have only heard defended. |

| ⭐ **MLST — *Don't Invent Faster Horses*, Prof. Jeff Clune** | **The one rev 2 missed entirely.** Clune is an author on roughly half of Rung 4 and had no interview listed on this page at all. If you listen to one thing before Rung 4, this. |

---

### ⑤ Author interviews you already own — the shortcut for the reading problem ⭐

You said you cannot yet read frontier papers cold, and that Part 5 ③ (third-party explainers) is the fix. **There is a better fix, and it is already on your disk.** The corpus holds recorded interviews with the **authors of six papers on this ladder** — the author explaining their own paper, at length, to a good interviewer, in text you can grep and read at your own speed.

**Use them the way ③ says to use explainers: listen or read first, then take the paper the same day.**

| In your corpus | The ladder paper it opens |
|---|---|
| `twiml-ai-podcast/8L4lDCCAsMQ_accelerating-intelligence-with-ai-generating-algorithms-with…` | **AI-GAs** (Rung 3) — Clune on his own manifesto |
| `twiml-ai-podcast/5cuRo0bCmPY_is-artificial-superintelligence-imminent-with-tim-rockt-schel` | **Open-Endedness is Essential for ASI** (Rung 3) |
| `twiml-ai-podcast/C5EyZAYlW7E_automated-design-of-agentic-systems-with-shengran-hu-700` | **ADAS** (Rung 4) — by its first author |
| `machine-learning-street-talk/1kwbp8hRRfs_can-ai-improve-itself-chris-lu-robert-lange-cong-lu` | **The AI Scientist** (Rung 4) — three of its authors together |
| `machine-learning-street-talk/EInEmGaMRLc_when-ai-discovers-the-next-transformer-robert-lange` | **Darwin Gödel Machine** (Rung 4 ⭐) — a co-author |
| `twiml-ai-podcast/1igh4oas1Ls_genie-3-…-jack-parker-holder` | **ACCEL** (Rung 2) — by its first author, here on world models |

::: key
**How to search the corpus, and the trap that hid all of this.** `RESOURCES/corpus/` holds **6,174** files. An accurate sweep finds **58** mentioning *open-endedness*, **16** mentioning *novelty search*, **15** mentioning *quality diversity*, and **55** mentioning *Kenneth Stanley* — far more than rev 2's "six Stanley conversations."

**Use `grep -rli "your term" RESOURCES/corpus/`.** Two other ways of searching return **zero on this corpus and look like a real answer**: `grep -F` is broken in this environment, and ripgrep-based tools skip the corpus entirely because it is gitignored by design. Rev 3's own audit fell into both and briefly concluded the corpus held nothing. **A search returning nothing is not evidence of absence until you have run it against something you know is there.**
:::

### ⑥ Lab channels — subscribe, don't binge

| Channel | What it is |
|---|---|
| **Evolving AI Lab** | Jeff Clune's lab. The ICML tutorial, the 2025 foundation-models talk, and visual result-demos (novelty search, curiosity search, soft robots). |
| **UCL DARK** | Tim Rocktäschel's group — talks including Max Jaderberg on the DeepMind open-ended learning result. |
| **eplexUCF** | Kenneth Stanley's UCF lab. Mostly **short demo clips and paper supplementary material**, not lectures — good for seeing what these systems actually produce, not for learning from. |
| **Inria Flowers** | Pierre-Yves Oudeyer's group — **intrinsic motivation, curiosity-driven learning, autotelic agents**. Adjacent to AP9 rather than inside it, and directly relevant if what draws you is agents that set their own goals. |

### ⑦ The workshop archive — the part nobody surfaces ⭐

The **Open-Ended Evolution (OEE) workshop series** is recorded and public, and it is effectively invisible to normal search: most of these have **fewer than 300 views**.

- **OEE3** (ALIFE 2018, Tokyo) — the full workshop, session by session, on **Tim Taylor's channel**: individual talks of 20–35 minutes (Hiroki Sayama on *evolved open-endedness vs open-ended evolution* and on the *cardinality leap*; Josh Bongard on *the role of embodiment*; Tim Taylor on *routes to open-endedness*; plus the open discussion sessions), and **Dave Ackley's** *Finding Life in the Shadows* on his own channel.
- **OEE1** (ECAL 2015, York) — session recordings on the **ECAL 2015** channel.

**Why bother with a 2018 workshop.** This is the field arguing with *itself* about what open-endedness even is — the definitional fight that Part 7's open problem #1 says is still unresolved. It is the best available preparation for proposing a measure of your own, and almost nobody working in the foundation-model era appears to have watched it.

### ⑧ ALife channels — for intuition, not rigour

Not research, and genuinely useful for building a feel for what "open-ended" looks like when you watch one run: **Emergent Garden** (*Artificial Life*), **The Bibites: Digital Life** (*The Evolution of Predation in a Simulated Ecosystem*), **Dave Ackley**, **Lana Sinapayen**, **Tim Taylor**. An hour here is worth more than it sounds before you start designing behaviour spaces.

### ⑨ The written hubs

| What | Why |
|---|---|
| ⭐ **`github.com/jennyzzt/awesome-open-ended`** | The living index of the field's *papers*, maintained by a Clune-group researcher. **Note its limit, learned the hard way: its Videos section lists four items.** Excellent for papers; not a video guide, and this page's first version mistook it for one. |
| **`quality-diversity.github.io`** | The QD community's hub — algorithms, papers, tutorials. |

**People to follow:** Jeff Clune (UBC / DeepMind) · Kenneth Stanley · Joel Lehman *(also writes unusually good essays)* · Tim Rocktäschel (DeepMind / UCL) · Antoine Cully (Imperial, QD) · Julian Togelius (NYU, games + PCG) · Pierre-Yves Oudeyer (Inria Flowers, intrinsic motivation) · Sakana AI · Jenny Zhang (DGM).

---

## Part 6 — code

| Library | Use it for |
|---|---|
| ⭐ **pyribs** — `docs.pyribs.org` | **Start here.** A deliberately bare-bones QD library, plain Python, no exotic dependencies, with real tutorials. Designed to be readable by someone with basic Python. This is where your first experiment runs. |
| **QDax** — JAX-based, from Cully's group *(Lim, Allard, Grillotti & Cully, 2022 · arXiv 2202.01258)* | Hardware-accelerated QD when pyribs gets too slow, plus RL and multi-objective baselines. Move here when speed matters, not before. **Read its paper for the reason it exists** — QD's cost is dominated by evaluating a whole population, which parallelises almost perfectly, and that single fact is why a laptop-scale QD experiment is even possible. |
| **The Darwin Gödel Machine and AI Scientist repos** | Reading material more than tooling — read them to see what a modern open-ended system actually looks like in code. |
| **ARC-AGI-3 agent harness** *(ARC Prize)* | The interactive benchmark, if you take the route in Part 8. |

---

## Part 7 — the open problems

Where the field is genuinely stuck, as of 2026. These are your candidate questions.

1. **Nobody can measure open-endedness.** There is no accepted metric. Hughes et al. (2024) define it relative to an *observer*; Soros & Stanley have been asking since 2014. A system that "keeps producing new things" and one that has quietly started cycling look identical on most plots. **This is the field's biggest unsolved problem and the most attackable one on a laptop.**
2. **Novelty is not interestingness.** Novelty is computable and it fills your archive with junk. Foundation models are the current patch (OMNI), which relocates the problem: now interestingness means *what a human-trained model finds interesting*, which caps you at human priors. Exactly the objection your instinct is reaching for.
3. **It does not scale past toy domains.** POET's environments are 2D walkers. Nearly everything in Rung 2 lives in small worlds, and it is unclear whether the mechanisms survive contact with anything bigger.
4. **The foundation-model turn may be a ceiling in disguise.** If the LLM supplies the variation, the interestingness and the curriculum, is the system open-ended — or is it exploring the space the LLM already contains? *(This is the same question [AP4 #2](../50-deep-dives/16_ap4-deep-dive-the-reward-is-the-whole-game.md) asks about RL: source or tool?)*
5. **Safety is unresolved and structural**, not a bolt-on. See Rung 6.
6. **The method may be measuring the wrong thing.** Batra et al. (Rung 5) argue that many quality-diversity results solve problems a single goal-conditioned policy already solves. If that generalises, a chunk of the field's evidence base is weaker than it looks — and this is the open problem most likely to change what you think the approach is worth.

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

- **The paper list is inventoried, not read.** Rev 3 verified that every entry **exists and is correctly attributed** — arXiv id, author list, first-version year, venue — but verification is not reading. I have read the ones this project's [AP9 card](../20-the-approaches/09_ap9-open-endedness.md) and [deep dive](../50-deep-dives/06_ap9-deep-dive-the-open-ended-engine.md) were grounded in. The 🟢/🟡/🔴 difficulty tags remain estimates from abstracts and venue.
- **Rev 2 described a starred paper wrongly, and the way it was wrong is instructive.** *In Search of the Ingredients of Open-Endedness* was summarised from the half of its title before the colon; the half after it says what the paper actually does. **A title is not an abstract.** If any other description on this page feels like it could have been written without opening the paper, assume it was, and check.
- **The five oldest Rung 1 entries were not re-verified.** *Abandoning Objectives*, *Virtual Creatures*, *Chromaria*, *Minimal Criterion Coevolution* and *The Last Grand Challenge* are journal, GECCO and O'Reilly items with no arXiv record, so the automated pass could not touch them. They are the most-cited and least likely to be wrong, which is why they were left — not because they were checked.
- **One thesis entry is still a search instruction.** Lehman's dissertation and Samvelyan's I verified, including ids. The Cully-group and Clune-group theses I did not — that row tells you where to look, not what to cite.
- **Discovery was arXiv-first and one-sided.** The sweep that found Rung 5 and the additions used the arXiv API across 22 queries. **Semantic Scholar was rate-limited throughout and its citation graph was never queried** — so anything that is well-cited but poorly matched by keyword search could still be missing. A citation-graph pass around POET and Hughes 2024 is the obvious next increment, and has not been done.
- **This page has now asserted a false negative twice, in two different revisions.** Rev 1: *"no course exists anywhere — I looked"* (built from one GitHub list, no YouTube search). Rev 2: *"nobody has written the textbook yet"* (no corpus search, and the corpus held Iba). Rev 3 then did it a third time inside its own audit, concluding the corpus contained no AP9 material at all, because two different search tools returned zero for two different broken reasons. **Three for three.** The page now carries the rule in Part 2 and the method in Part 5 ⑤; treat every remaining negative claim here as the least reliable thing on the page.
- **"No full university course" is still a negative, and negatives are hard.** I searched properly and found a tutorial but no course. Given the record above, weight that accordingly.
- **The critique rung is thin because I found little, not because little exists.** Rung 5 has one strong technical critique. I did not run a dedicated adversarial search — "quality diversity does not work", failed replications, rebuttals — and that search would be the single most valuable next pass on this page.
- **Video durations and channel names are read off the platform; view counts are not quoted** because they date immediately. Titles are given in enough detail to search for, since video URLs rot.
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

1. No textbook has open-endedness as its subject. What three things stand in for one here — and why is "there is no textbook" a claim this page got wrong twice before stating it carefully?
2. What is the archive, and why is it the one mechanism under every open-ended method?
3. POET generates its own environments. What stops it generating ones that are impossible or trivial?
4. The field's biggest unsolved problem is measurement. Say why "it keeps producing new things" is not enough.
5. Foundation models supply interestingness, which novelty search could not. What does that fix, and what does it quietly cap?

---

## Revision notes

- **rev 3 · 2026-09-09 · Parts 2–4 independently audited; a sixth rung added.** Rev 2 rebuilt Part 5 and then admitted in its own honesty box that *"Parts 2, 3 and 4 lean on the same index for their spine, and were verified only in places."* This revision closes that, using the arXiv API rather than any curated index: every Part 4 entry checked for title, authors, first-version date and venue, plus a 22-query independent sweep for what was missing. Full report: [`REVIEWS/AUDIT_2026-09-09_ap9-ladder.md`](../../REVIEWS/AUDIT_2026-09-09_ap9-ladder.md).
  **What held:** 19 entries verified exactly right, including every load-bearing paper in Rungs 1–3 and the Darwin Gödel Machine's ICLR 2026 venue.
  **What did not:** *In Search of the Ingredients of Open-Endedness* was described from its truncated title and is actually a **Picbreeder replication with vision-language models** — corrected, and Picbreeder added to Rung 1 so it can be read. Part 2's *"nobody has written the textbook yet"* was false: **Iba's *Deep Swarm and Evolution for Generative AI* (CRC Press, 2025)** has a section on novelty search and MAP-Elites in its index, and has been in the corpus all along. Dates were a mix of preprint and venue years and are now both. TerraLingua's author order was wrong.
  **What was added:** a new **Rung 5 · Where it breaks** — rev 2 had *no paper arguing the approach fails*, which was the worst structural fault on the page — led by Batra et al.'s QD critique. Plus the paper that **named** quality-diversity (Pugh, Soros & Stanley 2016), **Go-Explore** and its *Nature* result, **Cully et al.'s *Nature* damaged-robot result**, a **verified thesis** for the environment-design half (Samvelyan 2025), a **rival formal definition** of open-endedness (Van Roy's group, 2026), MAESTRO, Rainbow Teaming, ASAL, Intelligent Go-Explore, the Fractured Entangled Representation paper, the Red Queen Gödel Machine, and the QD reference shelf.
  **The finding that mattered most** is in Part 5 ⑤: the corpus holds **author interviews for six ladder papers** — including the only Jeff Clune interview, which rev 2 missed while listing six Stanley ones. For a reader who cannot yet take papers cold, that was the most valuable thing already on the disk. The audit also caught itself asserting a third false negative, from two silently broken search tools; the method note in Part 5 ⑤ exists so the next person does not repeat it.
- **rev 2 · 2026-09-09 · Part 5 rebuilt after a fair challenge.** The learner asked whether the many open-endedness videos and playlists on YouTube had actually been used. They had not: rev 1's four talks all came from the Videos section of `awesome-open-ended`, with no YouTube search performed, and the page nonetheless claimed that nothing course-like existed anywhere. A direct sweep — ten topic queries plus lab-channel enumeration, ~130 distinct videos — produced the rebuilt section: the **ICML 2019 tutorial** (152 min, the nearest thing to a course, which falsifies the old claim), **three paper-explainer channels** (Kilcher, Shorten, Gordić — the fastest fix for not yet reading papers cold), **~10 long-form interviews** including the Doom Debates episode that argues *against* Stanley, **four lab channels**, and the **OEE workshop archive** (OEE3 at ALIFE 2018 and OEE1 at ECAL 2015, mostly under 300 views each — the field arguing with itself about its own definition, which is Part 7's open problem #1). It also surfaced that `RESOURCES/corpus/transcripts/machine-learning-street-talk/` already held **six** Stanley conversations as searchable text, none of which rev 1 cited. Honesty box updated with the failure mode: a curated index tells you what its maintainer curated, and its gaps are invisible from inside it.
- **rev 1 · 2026-09-09 · new.** First approach ramp in group ⑥, written first *(rather than AP1)* because the learner identified their interest as systems where the agent sets its own goals rather than a human writing the reward — which is AP9. Built from a live web pass: the `awesome-open-ended` community index cross-checked against searches, Lehman's dissertation located and verified free, GECCO 2026 / ALIFE 2026 workshop formats, the ARC Prize 2026 ARC-AGI-3 track (prize structure, 30 September 2026 milestone, humans 100% vs frontier 0.51%), pyribs and QDax, and the 2024–26 record through the Darwin Gödel Machine (ICLR 2026) and *In Search of the Ingredients of Open-Endedness* (2026). Establishes the ramp template for the remaining ten: delta concepts → books → theses → paper ladder in rungs → courses/talks → code → open problems → first experiment → venues → **the best idea in this bet**, the last existing so that eleven ramps compose into one synthesis rather than eleven reading lists.
