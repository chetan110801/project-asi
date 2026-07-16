---
id: c-ap3-agents
sortkey: 2003
title: AP3 · Agents & cognitive architectures — the "a mind is a system, not one model" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap2-reasoning]
provides: [agents-cognitive-architectures, the-agent-loop, tool-use, agent-memory-reflection, planning-decomposition, skill-library-lifelong-agent, multi-agent-systems, march-of-nines, scaffolding-vs-model-debate]
resources: []
status: ready
reading_time: 33 min
rev: 1
created: 2026-07-15
updated: 2026-07-15
---

# AP3 · Agents & cognitive architectures — the "a mind is a system, not one model" bet

*This is the third big idea we look at for how to build a machine that can think in a general way. The first bets all worked on the **model itself** — make it bigger ([AP1](01_ap1-scale-and-foundation-models.md)), make it think longer ([AP2](02_ap2-reasoning-and-test-time-compute.md)). This bet says the model, however good, is only a **part.** A real mind is not one lump; it is a **system** — a thing built from several pieces working together: something that thinks, something that remembers, something that plans, something that acts on the world, and a loop that ties them together and learns from the result. So to get to a general mind, this bet says, you should **wrap the model in that system** — give it a memory, tools it can use, a way to plan, and a loop where it acts, sees what happened, and tries again. That wrapped-up whole is called an **agent.** This page explains it all from zero: the bet in one minute, the old idea it comes from, the four working pieces of an agent (grounded in the real systems people built), why it is taken seriously — and the four places it is stuck, including the sharpest doubt of all: is "agent-building" a real road to AGI, or just a temporary layer of software that each new, smarter model quietly makes unnecessary?*

> **You are here:** this is the **AP3** page — the third bet on the "approaches to AGI" map (see [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)), and the seventh one written in full. AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. The short name for this idea is **agents** (a model wrapped in a loop, with memory and tools, chasing a goal) and its older, grander name is a **cognitive architecture** *(a full design of a mind as a set of parts — perception, memory, reasoning, action — wired together)*.
>
> **This page builds on four earlier rungs of the ladder**, all short and plain: [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — how today's AI works; [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the steady curve the models ride; [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — the bet on the model itself; and [AP2 · the "think longer" bet](02_ap2-reasoning-and-test-time-compute.md) — the reasoning model that sits *inside* every agent. A one-line reminder of each is given where it is used, so you will not get lost. **AP3 is the deep home for the idea of an *agent*.**
>
> **Where the facts come from:** the durable pieces are grounded in the real agent systems people built and published — **ReAct** (2022, the reason-and-act loop), **Reflexion** (2023, memory and self-correction), **Generative Agents** (2023, the memory-reflection-planning architecture), and **Voyager** (2023, a lifelong-learning agent with a growing skill library). The plain-spoken framing is from **Andrej Karpathy** (Dwarkesh Podcast, 2025 — "the decade of agents," the "march of nines"). Quotes from all of these are exact. Fresh check of the field, done on the web (**as of July 2026**): METR's task-length measurements, the 2026 agent benchmarks, and the live "does the scaffolding get eaten by the model?" debate. Each fast-moving number is dated below.

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**A single model, no matter how clever, only does one thing: you give it some words, it gives you some words back, and then it forgets everything. That is not what a mind is. A mind *keeps going*: it holds a goal, remembers what it has done, looks things up, uses tools, takes an action, sees what happened, and adjusts — over and over, for as long as the job takes. AP3's bet is that you get to a general mind not by growing one giant model but by *building that whole loop around a model.* You take a good reasoning model and you wrap it in a system: a memory so it does not forget, tools so it can reach the real world (search, a calculator, a web browser, code it can run), a planner so it can break a big goal into steps, and a feedback loop so it can act, check the result, and try again. The wrapped-up whole — model plus memory plus tools plus planning plus loop — is an *agent*. On this view, intelligence is not a single lump you scale up; it is an *architecture* — a set of parts, arranged so their teamwork does what no part could do alone.**

Why believe a mind is a system of parts rather than one big model? Because that is what every mind and every working machine we know actually looks like. Your own brain is not one organ doing one thing; it has separate systems for seeing, remembering, planning, and moving, all wired together. And when people take today's models and make them do real, multi-step jobs — fix a bug across a large codebase, research a question by reading twenty web pages, book a trip — they never just ask the model once. They build the loop. The agent is where AI stops being a thing that *answers* and starts being a thing that *does.*

That is the bet. The rest of this page explains **where the idea comes from**, **the four working pieces of an agent**, **why it is a serious road**, and **why it might still be wrong — or might not even be a separate road at all.**

---

## First, a one-line reminder of the base

Three quick reminders from the rungs below, so this page stands on its own.

- From [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md): **today's main AI is a text machine** trained to guess the next word in billions of pages of human writing; run in a loop, it writes. On its own it does exactly one step — words in, words out — and then it is done. *(New to you? Read that short rung first.)*
- From [AP1, the "make it bigger" bet](01_ap1-scale-and-foundation-models.md): the main way the field has improved AI is to *scale the model* — more data, more computer power, more knobs — and skills appear as a side-effect. AP3 leaves the model roughly as-is and works on the *system around it* instead.
- From [AP2, the "think longer" bet](02_ap2-reasoning-and-test-time-compute.md): a **reasoning model** spends extra computer power at answer-time, writing out its steps (a *chain of thought*) before it replies. This is the mind that sits *inside* an agent. AP2 made that mind think longer in one sitting; **AP3 puts that mind in a body** — gives it memory, tools, and a loop so it can act in the world, not just talk.

Now the one new idea this page adds. Every approach so far has asked *what kind of model* to build and *how to train or run it.* AP3 asks a different question: **once you have a decent model, what do you build *around* it to turn a thing-that-answers into a thing-that-gets-jobs-done?** Its answer is: a system of parts. To see why that is an old and serious answer — not just today's engineering fashion — we start with where the idea comes from.

---

## Part 1 — the old idea: a mind is an architecture

This bet is much older than today's models, and knowing its root makes it clearer.

Back at the very start of AI, in the 1950s–1990s, many researchers did not think "intelligence" was one trick to be discovered. They thought a mind was a **whole system that had to be designed** — a set of parts, each doing a job, wired together. They called such a design a **cognitive architecture** *(a full blueprint of a mind: how perception, memory, reasoning, and action fit together)*. The idea, from pioneers like Allen Newell and Herbert Simon, was that you build intelligence the way you build a machine — piece by piece: a part that takes in the world, a memory that stores what you know, a reasoner that decides what to do, and a part that acts. Famous attempts (SOAR, and ACT-R) tried to write down the *one architecture* that all thinking runs on. **[Established — this is documented AI history; SOAR and ACT-R are real, long-running research systems.]**

Those old systems were hand-built and brittle — every piece of knowledge had to be typed in by a person, and they broke the moment the world did something unexpected. So when the scaling era arrived (AP1), the whole "design the architecture" idea fell out of fashion. Why hand-build a mind's parts if you can just grow one big model that learns everything at once?

Here is the twist that brings the old idea back — and it is the heart of AP3. The big model turned out to be an amazing **part**, but not a whole mind. It is a superb reasoner-in-one-shot with **no memory** (it forgets everything after each turn), **no hands** (it cannot do anything but produce text), and **no way to check its own work** against the real world. So people started doing the obvious thing: **put the old architecture back — but with the giant model as the brain inside it.** Give it a memory. Give it tools. Give it a loop. That marriage — *the modern, learned model living inside the classic parts-of-a-mind design* — is exactly what an agent is. The old dream of a cognitive architecture, with a brain that finally works.

So the durable claim of AP3 is a single sentence: **intelligence is an architecture — a system of parts — and the model is only one part.** Now let us see the parts.

---

## Part 2 — the four working pieces of an agent

An agent adds four things to a bare model. We take them one at a time, and each is grounded in a real, published system so you can see it is not hand-waving. Keep one picture in mind throughout: a **loop.** The model *thinks*, then *acts*, then *sees what happened*, then thinks again — round and round until the goal is met.

### Piece 1 — the act loop: reasoning + tools (ReAct)

The first and most basic piece is the loop itself: letting the model **do something**, not just talk. A bare model can only write text. An agent lets that text be an **action** — a command it can actually run, like "search Wikipedia for X" or "run this code" — and then feeds the *result* of that action back to the model so it can decide the next step. A tool is just some outside thing the agent can call to reach past its own head: a web search, a calculator, a code-runner, a database *(store of facts)*.

The paper that set the pattern is called **ReAct** (2022) — the name is short for *Reason + Act*. Its starting point is a fact about people:

> "A unique feature of human intelligence is the ability to seamlessly combine task-oriented actions with verbal reasoning."
> *(ReAct, Yao et al., 2022)*

("Task-oriented actions" = doing things that move you toward the goal. "Verbal reasoning" = talking yourself through it in words.) When you cook, you *reason* ("I'm out of salt, I'll use soy sauce instead") and you *act* (open the fridge, taste the sauce), turn by turn, each helping the other. ReAct makes the model do the same — write a thought, take an action, read the result, write the next thought. The paper says exactly why this pairing is powerful:

> "reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments."
> *(ReAct, 2022)*

("Reasoning traces" = the written-out thinking steps. "Induce … plans" = work out a plan. "Handle exceptions" = deal with things going wrong. "Interface with" = connect to and use.) Read the two halves: **thinking keeps the plan on track; acting brings in real facts from outside.** And the payoff is not just tidiness — it fixes a real failure. A model reasoning alone, with no way to check anything, will confidently make things up (you met this as *hallucination* — fluent, confident, false — in the base rungs). Letting it *act* — go and look — grounds it in reality:

> "ReAct overcomes prevalent issues of hallucination and error propagation … by interacting with a simple Wikipedia API."
> *(ReAct, 2022)*

("Error propagation" = one early mistake feeding into the next, so wrongness spreads. "API" = a doorway one program uses to call another.) This is Piece 1: the model in a loop, using tools to touch the real world and correct itself. It is the floor everything else is built on.

### Piece 2 — memory and self-reflection (Reflexion, Generative Agents)

A bare model has no memory: after each turn it forgets. That is fine for one question, useless for a long job — you cannot pursue a goal for an hour if you forget what you did a minute ago. So the second piece is a **memory**: a place outside the model where the agent writes down what it has seen and done, and from which it can read back later.

But the sharpest version of memory is not just storage — it is **reflection**: the agent writes down *lessons from its own mistakes* and reuses them. The paper **Reflexion** (2023) built exactly this:

> "We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials."
> *(Reflexion, Shinn et al., 2023)*

Let us unpack that, because it is a beautiful idea. *"Reinforce … not by updating weights"* — normally, to make a model better you retrain it, slowly changing its billions of internal numbers (its *weights*). That is expensive and slow. *"Linguistic feedback"* means: instead, after the agent fails a task, it **writes itself a note in plain words** — "I failed because I forgot to check the input was valid" — and keeps that note in an *"episodic memory buffer"* *(a running diary of past attempts)*. Next time, it reads its own note first. So it **learns from experience without any retraining at all** — the lesson lives in written words, not in changed weights. The model stays fixed; the *system around it* gets smarter by remembering.

The fullest picture of memory-as-architecture came from **Generative Agents** (2023), which built a little town of software characters. To make them behave like people over days, the researchers gave each one a full memory system:

> "we describe an architecture that extends a large language model to store a complete record of the agent's experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior."
> *(Generative Agents, Park et al., 2023)*

("Synthesize … into higher-level reflections" = boil many small memories down into bigger lessons — from "I saw Sam buy bread, then buy milk" up to "Sam does the shopping." "Retrieve them dynamically" = pull up the right memory at the right moment.) Notice the shape: **store → reflect → retrieve → plan.** That is a cognitive architecture, exactly the Part 1 idea, built out of a language model. The model is the reasoner in the middle; the memory, the reflection, and the planning are *parts wired around it.* **[Established — these are real, published, reproduced systems.]**

### Piece 3 — planning: break a big goal into steps

The third piece answers a simple problem: a huge goal ("build me a website," "plan this trip") is too big to do in one thought. So the agent needs to **plan** — split the goal into smaller steps, do them in order, and track which are done. This is exactly the *decomposition* idea *(breaking one big problem into smaller solvable ones)*.

In today's agents, planning is done in two ways, and it is worth seeing both. The **old way** (the classic architecture) is a separate *planner* part: one component whose only job is to produce a step list, which another component then carries out. The **new way**, rising fast in 2026, is that the reasoning model does the planning *inside its own chain of thought* — it writes the plan, does a step, re-reads, adjusts the plan, all in one flowing trace, with no separate planner part *(this is the same [chain-of-thought](02_ap2-reasoning-and-test-time-compute.md) you met in AP2, now steering actions instead of just producing an answer)*. Which of these two ways wins turns out to be the crux of the whole approach — hold that thought; it comes back as the central doubt (Stuck #2).

### Piece 4 — lifelong skills: get better at the job over time (Voyager)

The fourth piece is the most ambitious: an agent that does not just finish one task but **keeps learning** — building up a growing kit of abilities, so it gets more capable the longer it runs. The clearest example is **Voyager** (2023), an agent set loose to play the game *Minecraft* with no human help. Its design shows all four pieces working together:

> "VOYAGER consists of three key components: 1) an automatic curriculum that maximizes exploration, 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement."
> *(Voyager, Wang et al., 2023)*

("Automatic curriculum" = it sets its own next challenge, from easy to hard, with no teacher. "Skill library of executable code" = when it works out how to do something — say, mine stone — it saves that as a little program it can call again later. "Iterative prompting … self-verification" = it tries, reads the error, checks its own work, and fixes it, over and over.) The key invention here is the **skill library.** Each new ability is saved as reusable code, and — crucially — new skills are built by *combining old ones*, so its powers **compound** *(build on each other and grow faster and faster)*. The paper notes a lovely bonus of storing skills this way:

> "The skills developed by VOYAGER are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting."
> *(Voyager, 2023)*

("Temporally extended" = they stretch over many steps, not one. "Interpretable" = a person can read and understand them. "Compositional" = they snap together like blocks. "Catastrophic forgetting" = the usual problem where a model learning something new *erases* what it knew before — a giant open problem for AGI.) This last point matters a lot: by keeping skills as separate saved code instead of cramming them into the model's weights, the agent *does not forget the old ones when it learns new ones.* The architecture **solves a problem the bare model has** — a small, clear example of the whole promise of AP3.

### The four pieces, together

Put them in one picture. An agent is a **reasoning model** (the brain, from AP2) placed inside a loop, with:

1. **Tools + an act-loop** — so it can *do* things and check reality (ReAct),
2. **Memory + reflection** — so it does not forget, and learns from its mistakes in plain words (Reflexion, Generative Agents),
3. **Planning** — so it can break a big goal into steps,
4. **A growing skill library** — so it gets better the longer it runs, without forgetting (Voyager).

None of these four is a bigger model. Each is a *part added around* the model. That is AP3's whole claim made concrete: **the road to a general mind runs through the *architecture*, not just the brain in the middle of it.**

---

## Why this is a serious idea, not just today's fashion

Three legs hold it up.

### Leg 1 — it is how the one working mind, and every real deployment, is built

The strongest argument is that **no mind we know of is a single lump.** Your brain has distinct systems — for seeing, for memory, for planning, for movement — that only *together* produce a thinking person. And when people actually put AI to real, multi-step work today, they never just call the model once; they build the loop, the memory, and the tools — because a bare model plainly cannot hold a goal across time. So AP3 is not a speculative theory; it is a description of **how every capable AI system in the real world is already put together.** Andrej Karpathy, who has built these systems for years, frames the finished agent in human terms — the thing you are really making is a **worker you can hand a job to**:

> "you should think of it almost like an employee or an intern that you would hire to work with you."
> *(Andrej Karpathy, Dwarkesh Podcast, 2025)*

That target — *a colleague, not a chatbot* — only makes sense for a system that remembers, plans, and acts over time. **[Established — that real-world capable AI is built as agent systems is simply current practice.]**

### Leg 2 — the pieces demonstrably add abilities the bare model lacks

This leg is concrete: each piece has been shown, in published work, to **fix a real weakness of the lone model.** Tools cut hallucination (ReAct went and *checked*, instead of guessing). Reflection let an agent learn from failure with no retraining (Reflexion). A skill library beat *catastrophic forgetting* — the model kept old abilities while gaining new ones (Voyager). None of these came from a bigger model; all came from **better architecture around the same model.** That is direct evidence for the core bet: arranging parts well buys you abilities that scaling the middle piece did not. **[Established — each result is a documented, reproduced finding.]**

### Leg 3 — the capability is climbing fast, and it is measurable

The last leg is that agents are not stuck — they are getting steadily, measurably better at exactly the thing that matters: **doing longer jobs on their own.** The nonprofit **METR** measures this with one clean number — the *task time horizon*: **the length of a job (measured by how long a human expert would take) that an agent can finish on its own with 50% reliability.** Their headline finding is a steady trend:

> "the length of tasks … that generalist frontier model agents can complete autonomously with 50% reliability has been doubling approximately every 7 months for the last 6 years."
> *(METR, "Measuring AI Ability to Complete Long Tasks," March 2025)*

At that writing (March 2025), the best model (Claude 3.7 Sonnet) had a 50%-reliability horizon of *about one hour* of expert work. Later analyses through early 2026 report the doubling has **sped up** — to roughly every 4 months since 2023 — with frontier 50%-horizons reaching **several hours** of autonomous work *(as of early 2026; the exact hour-counts come from non-primary trackers and should be treated as rough, dated snapshots — the durable fact is the doubling trend, not any single number).* Either way, the direction is not in doubt: the length of job an agent can carry alone is climbing on a steady curve. **[Established trend; specific 2026 hour-counts Contested — see the honesty box.]**

---

## So what does AP3 say intelligence is?

Pulling the legs together, here is AP3's answer to *"what is intelligence?"*:

- **Intelligence is an *architecture*** — a system of cooperating parts (a reasoner, a memory, a planner, tools, a loop), not a single model. The model is the brain; the mind is the whole assembly.
- **What it optimises** is *completing real, multi-step goals over time* — measured not by a one-shot answer but by how long and how reliably the system can act on its own toward a goal.
- **Its claim about the missing piece:** what a bare model lacks is not size or raw cleverness but **the rest of the mind** — memory, hands, a loop, the power to plan and to learn from what happens. Add those parts, wire them well, and thinking-in-one-shot becomes *acting-over-time*, which is what a mind actually does.

That is the bet. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP3 is the least speculative approach on the whole map — it is *how working AI is already built*, and its pieces have provably added real abilities. Hold that. But it has four deep troubles, and the second one is an attack on whether it is even a *separate approach to AGI* at all.

### Stuck #1 — errors compound, so long jobs fall apart (the march of nines)

This is the deepest, most stubborn problem, and it is pure arithmetic. An agent works in a *loop of many steps.* Suppose each single step is a very reliable 95% correct. Do twenty steps in a row and the chance that *all* of them are right is 0.95 multiplied by itself twenty times — about **36%.** A hundred steps and it is almost zero. Small per-step errors **compound** *(pile up and multiply)* into near-certain failure over a long job. And because an agent *feeds each step's output into the next step*, one early mistake doesn't just cost one step — it spoils every step after it. This is why agents that look great in a short demo so often collapse on a real, long task.

Karpathy has the sharpest name for the grind this creates. Getting an agent from "impressive demo" to "trustworthy worker" is not one push; it is a long series of them, each as hard as the last:

> "it's a march of nines. Every single nine is a constant amount of work … When you get a demo and something works 90% of the time, that's just the first nine. Then you need the second nine, a third nine, a fourth nine, a fifth nine."
> *(Karpathy, 2025)*

("A march of nines" = pushing reliability from 90% to 99% to 99.9% to 99.99% — each extra nine after the decimal point. "A constant amount of work" = every new nine costs *as much effort as the one before*, so it never gets easier near the end.) A demo that works nine times in ten feels almost done — but "almost" is the *first* nine, and a dependable worker needs several more, each a huge amount of work. This is the honest reason agents have been "one year away" for several years running, and it is exactly the gap METR's *50%-reliability* number hides: a job an agent finishes *half* the time is a world away from one you can *trust it to finish.* **[Established — the compounding of per-step errors is basic arithmetic; the "march of nines" is a documented, widely-echoed observation.]**

### Stuck #2 — is it a real road, or just a layer of software the model will absorb?

This is the sharpest doubt, and honesty demands it lead the rest. Everything an agent adds — the planning, the memory-handling, the tool-choosing, the loop — is **software wrapped around the model**, often called the *scaffolding* *(the outside structure holding the model up and telling it what to do next, like the poles and planks around a building under construction)*. The worry is this: **what happens to all that scaffolding when the model inside gets smarter?**

The pattern of the last few years is hard for the people who build scaffolding. Elaborate 2024-era agent systems — a "planner" part, a separate "router," a "critic" that checks the work, all wired into a big diagram — were built to *make up for what the models could not yet do.* Then the next model came out able to plan, route, and self-check *inside its own chain of thought*, and the fancy outside structure became useless extra work. As practitioners put it in 2026: the elaborate orchestrator-and-critic graphs of 2024 are dissolving, because a single agentic-thinking model now does the decomposition *inside the model* rather than in outside code *(as of 2026-07; a widely-argued practitioner view, not a settled fact).* This is exactly [Sutton's Bitter Lesson](01_ap1-scale-and-foundation-models.md) — the lesson from AP1 that hand-built human structure keeps losing to methods that just scale the model — **pointed straight at AP3.**

So the hard question: **is "building the architecture" a genuine path to AGI, or is it a temporary patch — an *app layer* — that each smarter model quietly absorbs?** If the parts keep getting absorbed into the model, then AP3 is not a rival approach to AGI at all; it is just *how you turn this year's model into a usable product while you wait for next year's.* AP3's defenders answer that *some* architecture is permanent — even a superhuman brain still needs an external memory and real tools to touch the world, exactly as a genius still needs a notebook and a web browser. Which parts are permanent mind-structure and which are throwaway patches for today's weaknesses is **genuinely unresolved**, and it is the single most important open question about this approach. **[Contested — the central live debate; as of 2026-07 it is unsettled.]**

### Stuck #3 — an agent can't be smarter than the mind inside it

The third crack is a ceiling. A loop, a memory, and a set of tools are powerful, but they **cannot create reasoning that the core model does not have.** If the model in the middle can't work out the right next step, letting it try in a loop mostly means it makes the *same* mistake more times, faster. Scaffolding can *organise* intelligence and *stop it leaking* (via memory and tools); it cannot *manufacture* intelligence that isn't there. So AP3 quietly **inherits every weakness of AP2 and [AP8](08_ap8-program-synthesis-arc.md)** — if the base model reasons brittlely, or fails on genuinely novel problems, the agent built on it fails too, just with more steps. This is why agent progress is chained to *model* progress: the biggest jumps in what agents can do have come not from cleverer scaffolding but from a better brain dropped into the same loop. **[Likely — broadly agreed; the exact division of credit between "better model" and "better scaffolding" is debated.]**

### Stuck #4 — the grand version (a society of agents) is still a promise

The fourth crack is about the most exciting claim: that you can go beyond one agent to **many agents working together** — a whole team, or even an "AI company," dividing the labour and combining results, the way human organisations achieve far more than any lone person. It is a thrilling idea. It also, as of 2026, **mostly does not work yet.** Karpathy, asked directly about multi-agent systems and an "AI civilization," is blunt that the field has barely begun:

> "We're mostly in the realm of a single individual agent, but that will change."
> *(Karpathy, 2025)*

He points out that the two things that make *human* groups so powerful — a shared **culture** they build up and pass on, and real **organisations** that coordinate many minds — have no convincing machine version yet. So the leap from "one useful agent" to "a productive society of agents" is, for now, a hope, not a demonstrated result. Multi-agent demos exist, but robust, genuinely-more-capable teams of agents do not. **[Contested / early — an active research frontier with no settled win.]**

### The big question under all of these

Every doubt above is one question: **is a mind something you *assemble* out of parts, or something you *grow* in the middle and let the parts fall out of?** AP3 says *assemble* — intelligence is the architecture, and the model is one component you wire into it. AP1 and AP2 say *grow* — make the model itself capable enough and the "parts" (planning, memory-use, tool-use) emerge inside it, needing little outside structure. The 2026 evidence pulls uncomfortably toward *grow*: the scaffolding really is dissolving into the models (Stuck #2), and the biggest agent gains really do come from better *models* (Stuck #3). So the live question is whether AP3 is a **separate destination** — a real, distinct route to AGI — or a **moving construction site** that each new model tears down and rebuilds smaller. *As of July 2026, this is genuinely open,* and it is the argument that decides whether "agents" is a science of minds or an engineering fashion. **[Contested — the key open question.]**

---

## ⚠️ Honesty box

- **AP3 is the most real and the least *distinct* of the approaches.** Its strength is that it is not speculation — it is how working AI is built, and its pieces provably add abilities (Legs 1–2). Its weakness is the mirror image: much of what it adds may be temporary scaffolding the models will absorb (Stuck #2), which makes it unclear whether it is a *separate bet on AGI* or just the *application layer* of AP1/AP2. Keep both halves in view. **[Contested.]**
- **"50% reliability" is doing a lot of hiding.** The headline that agents now do "hours-long tasks" is a *50%-of-the-time* number. A worker you can trust needs the far harder 99%+ — the march of nines (Stuck #1). Never read a 50%-horizon as "it can now be trusted to do this." **[Established.]**
- **The 2026 hour-counts are soft; the trend is solid.** METR's *doubling* finding and the ~1-hour figure (Claude 3.7 Sonnet, March 2025) are primary and firm. The "several hours by early 2026" and the specific leaderboard scores floating around come from secondary trackers, and some circulating model names/numbers are unverified. Trust the *shape of the curve*, date every point, and treat single hour-counts as rough. **[Established trend; Contested specifics.]**
- **Agents inherit their brain's flaws.** A loop cannot fix a reasoner that is wrong; it can only repeat it (Stuck #3). When an agent fails at something genuinely novel, suspect the *model* (see [AP8](08_ap8-program-synthesis-arc.md)'s "skill is not intelligence"), not the scaffolding. **[Likely.]**
- **Names and numbers age fast; the ideas don't.** ReAct, Reflexion, Generative Agents, Voyager, the specific 2026 benchmarks and model scores — these are 2022–2026 snapshots. The lasting parts are the **architecture idea** (a mind is a system of parts), the **four pieces** (act-loop/tools, memory/reflection, planning, skill-library), the **compounding-error / march-of-nines** problem, and the **scaffolding-vs-model** debate. The example systems will be replaced; the structure of the argument will not.

---

## How to use this (if you want to direct AI work)

- **First question about any agent: what are its parts?** When someone shows you an "AI agent," look past the demo and ask what pieces it has — what tools can it call, what does it remember, how does it plan, how does it recover from a mistake? A system with no memory and no way to check its own work will look great for one step and fall apart over ten. The architecture, not the demo, tells you what it can really do.
- **Always ask for the reliability *and* the horizon together.** "It does two-hour tasks" is meaningless without "at what reliability?" Push for the higher bar (how often does it finish *without* a human rescuing it?), because that gap — 50% versus 99% — is the whole march of nines, and it is where all the real cost and risk live.
- **Suspect the scaffolding is temporary.** Before you build an elaborate multi-part agent to work around today's model limits, ask which of those parts the *next* model will simply do on its own (Stuck #2). Build the parts that are permanent mind-structure — durable memory, real tools, a way to verify results — and be ready to throw away the parts that only patch this year's weaknesses.
- **Blame the brain before the harness.** When an agent fails on something genuinely new, more loops and more prompts usually won't save it — the ceiling is the model's own reasoning (Stuck #3). Spend the effort on a better core model or a genuinely novel capability, not on ever-fancier scaffolding around a brain that can't do the task.
- **Treat "a team of agents" as unproven.** Multi-agent "AI company" pitches are exciting and, as of 2026, mostly do not beat one good agent (Stuck #4). Demand evidence that the team actually outperforms the individual before betting on the org chart.
- **What you hand to others:** wiring the tools, building the memory store, writing the loop, tuning the prompts. **What you keep for yourself:** deciding which parts are real mind-structure versus throwaway patches, refusing to trust a 50%-reliability number, knowing that the loop can't out-think its model, and watching whether the field's gains are coming from *architecture* or from the *model* underneath (the argument that tells you if this is a road or a layer).

---

## Connections

- **Keep only three things:** ① AP3 = **a mind is a system, not one model.** You reach a general mind by *wrapping a reasoning model in an architecture* — an **act-loop with tools** (ReAct), a **memory that reflects** on its mistakes (Reflexion, Generative Agents), a **planner** that breaks goals into steps, and a **growing skill library** (Voyager) — turning a thing-that-answers into a thing-that-does. ② It is the least speculative bet (it is how real AI is built) and its pieces provably add abilities the bare model lacks. ③ It is stuck on four cracks: **errors compound over long jobs** (the march of nines; 50%-reliability hides this), **the scaffolding may just get absorbed by the next model** (is it a road or an app layer?), **it can't out-think the model inside it**, and **multi-agent "teams" don't yet beat one good agent.**
- **Down the ladder (already read):** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — the one-step text machine an agent wraps a loop around · [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the curve the model rides.
- **Its siblings:** [AP2 · the "think longer" bet](02_ap2-reasoning-and-test-time-compute.md) is the reasoning brain that sits *inside* the agent — AP3 gives that brain a body (memory, tools, a loop). [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) is AP3's rival for a deep reason: AP1's [Bitter Lesson](01_ap1-scale-and-foundation-models.md) predicts the agent's hand-built parts will be *absorbed* into bigger models (Stuck #2). And AP3 inherits the reasoning limits of [AP8 · skill is not intelligence](08_ap8-program-synthesis-arc.md) — a loop around a brittle reasoner is still brittle (Stuck #3).
- **The ideas it leads to:** [AP4 · RL from interaction](04_ap4-rl-from-interaction.md) gives the *reward-driven* version of the agent — an agent that learns its loop from reward in a world, rather than being scripted; [AP7 · neurosymbolic](07_ap7-neurosymbolic-and-hybrid-ai.md) and [AP9 · open-endedness](09_ap9-open-endedness.md) (both now written) bear on how an agent could *plan* and *keep learning* reliably. See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** That real AI is built as agent systems, and that the four pieces add real abilities — **[Established]**. That "agent architecture" is a *separate road to AGI* (rather than a temporary layer the models absorb), and that multi-agent teams will pay off — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP3 bet in one plain sentence, using the words *system*, *parts*, and *loop*.
2. Name the **four pieces** an agent adds to a bare model, and for each, one weakness of the lone model it fixes.
3. Explain the **act-loop** (ReAct) in your own words. Why does letting the model *act* reduce made-up answers (hallucination)?
4. What is **reflection** (Reflexion), and why is "learn without updating weights" surprising?
5. Do the arithmetic: if each step is 95% reliable, roughly what is the chance of getting 20 steps all right? What does this say about long tasks? (Stuck #1 — the march of nines.)
6. Explain the **scaffolding-vs-model** debate (Stuck #2). Why does the Bitter Lesson from AP1 make it the sharpest doubt about whether AP3 is a *separate* road to AGI?

## Revision notes

*Newest first.*
- `rev 1 (2026-07-15)` — created as the **AP3** deep-dive, the seventh approach card written (badge = AP index; sits at sortkey 2003, between AP2 and AP4 in reading order). Built to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)). Placed as a new rung that **builds on** [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md), [scaling](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), [AP1](01_ap1-scale-and-foundation-models.md), and [AP2](02_ap2-reasoning-and-test-time-compute.md) with short reminders-and-links; it is the **deep home for the *agent* idea** (the legacy `1200` LLM-agents row is hidden). Forward-references AP4/AP7/AP9 as later cards (no dependency on them, since AP3 is read before them). Grounded verbatim in the published agent systems — ReAct (reason+act loop, tools cut hallucination), Reflexion (verbal reflection in an episodic memory buffer, learning without weight updates), Generative Agents (store → synthesize reflections → retrieve → plan), Voyager (automatic curriculum + skill library of executable code + self-verification; skills compound and alleviate catastrophic forgetting) — plus Karpathy 2025 (the employee/intern framing, "the march of nines," single-agent-for-now). Classical cognitive-architecture lineage (Newell & Simon; SOAR, ACT-R) given as brief documented history, marked [Established]. Full live-web freshness pass (July 2026): METR's task-time-horizon doubling (primary: ~7-month doubling, Claude 3.7 Sonnet ~1 hr at 50% reliability, March 2025; secondary trackers report ~4-month doubling and multi-hour horizons by early 2026 — flagged as soft, dated snapshots); the 2026 agent benchmarks (SWE-bench Verified, GAIA, OSWorld/computer-use); and the live "scaffolding gets eaten by the model" / Bitter-Lesson-for-agents debate — surfaced as the central open question (Stuck #2). Four cracks: compounding errors / march of nines · scaffolding-vs-model (road or app layer?) · can't out-think its core model · multi-agent unproven.

---
*This is the seventh approach page written. The brain inside every agent is [AP2 · the "think longer" bet](02_ap2-reasoning-and-test-time-compute.md); its deepest rival is [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md), whose Bitter Lesson predicts the agent's parts get absorbed. The reward-driven version of the agent is AP4, coming next on the [map](../APPROACHES_TO_AGI.md). To see the one-step text machine an agent wraps a loop around, read [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md).*
