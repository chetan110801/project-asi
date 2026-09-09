---
id: c-ap12-oak
sortkey: 2012
title: AP12 · OaK & the experience-only agent — the "learn it all yourself, forever" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap4-rl, c-ap9-open-endedness]
provides: [oak-architecture, alberta-plan, experience-only-bet, big-world-hypothesis, fc-stomp, continual-learning-as-prerequisite, sutton-llm-critique]
resources: []
status: ready
reading_time: 22 min
rev: 1
created: 2026-09-09
updated: 2026-09-09
---

# AP12 · OaK & the experience-only agent — the "learn it all yourself, forever" bet

*The twelfth bet, and the one that argues the other eleven have the wrong shape. Its claim: a mind cannot be **trained and then shipped**. It has to be a single agent that starts knowing nothing, learns only from its own stream of experience, and never stops learning — not for a moment, not after deployment, not ever. Everything else, on this view, is a detour. The bet is unusual in two ways: it comes from the person who wrote the field's textbook and won its Turing Award, and it rests on a measured, published failure of today's networks — that they lose the ability to learn at all.*

> **You are here:** this is the **AP12** page — a twelfth bet added to the [map](../APPROACHES_TO_AGI.md) on 2026-09-09, after the original eleven were written. It was missing, and the miss is documented in the revision notes below. The short name is **OaK** *(Options and Knowledge — Richard Sutton's proposed architecture)*, and the wider programme it belongs to is the **Alberta Plan**.
>
> **This page builds on rungs you have already climbed.** [AP1 · scale](01_ap1-scale-and-foundation-models.md) — for the **Bitter Lesson**, which Sutton wrote and which this bet claims the industry has misread. [AP4 · RL from interaction](04_ap4-rl-from-interaction.md) — for **reward**, **value**, **policy**, **model-based RL**, and the *"reward is enough"* claim, all of which AP12 inherits wholesale and does **not** re-argue. [AP9 · open-endedness](09_ap9-open-endedness.md) — for what it means for a system never to converge. Each is reminded in one line where used.
>
> **Where the facts come from:** a live web pass on **2026-09-09**. Sutton, Bowling & Pilarski, *The Alberta Plan for AI Research* (arXiv 2208.11173, 2022) read via its HTML rendering. Dohare, Hernandez-Garcia, Lan, Rahman, Mahmood & Sutton, *"Loss of plasticity in deep continual learning"*, **Nature**, 2024. Sutton's OaK talks at **RLC-2025**, **AGI-2025** and as a **NeurIPS 2025 invited talk**, plus the MIT CSAIL Dertouzos lecture listing. The **Oak Lab** founding (announced 14 July 2026, Sutton with Khurram Javed) and the Sequoia Capital podcast episode published **8 September 2026**. Sutton's *"LLMs are a dead end"* interview, September 2025. **Everything here is under two months old in places and will move fast.**

---

## The bet in one minute

**Every other approach on this map assumes a shape: gather data, train a model, then use it. AP12 says that shape is the mistake, and that no amount of scaling fixes it. A real mind is not a thing you finish training. It is an agent that wakes up knowing nothing, is given only three signals — what it sees, what it does, and how well things went — and from those alone builds everything: its own features, its own sub-goals, its own skills, its own model of how the world works, and its own plans. It keeps doing this forever. There is no training phase and no deployment phase; every moment is both. The bet is that intelligence *is* that process, and that anything which stops learning has stopped being intelligent.**

Two things make this more than a philosophical preference.

**First, it names a measured defect in everything else.** Today's networks do not merely *choose* not to learn after deployment — they largely *cannot*. Train one on a long sequence of tasks and its ability to learn new things decays until it is nearly gone. That is a published, quantified result, not a worry. So "keep learning forever" is not an extra feature to bolt on later; on this view it is a missing capability that blocks the whole road.

**Second, it comes from an unusually credentialled place.** Richard Sutton wrote the field's standard textbook, won the 2024 Turing Award for reinforcement learning, and wrote **the Bitter Lesson** — the essay [AP1](01_ap1-scale-and-foundation-models.md) rests on. His 2025 position is that the industry has misread his own essay: scaling language models on human text is not the bitter lesson's recommendation, because it is still **built on human data**, which is exactly the human-knowledge crutch the essay warned against. In September 2025 he put it bluntly, saying large language models are a dead end. In August 2025 he said the field, having become an industry, had to an extent lost its way.

---

## First, a one-line reminder of the base

- **The Bitter Lesson** *(from [AP1](01_ap1-scale-and-foundation-models.md))* — methods that just use more computation eventually beat methods that build in human knowledge. AP12 accepts this completely and argues that training on human text *violates* it.
- **Reward, value, policy, model** *(from [AP4](04_ap4-rl-from-interaction.md))* — the standard RL frame. AP12 is built inside it and does not re-argue it.
- **Model-based RL** *(also [AP4](04_ap4-rl-from-interaction.md))* — learning a model of the world and planning with it, rather than acting reflexively. OaK is a model-based architecture.

---

## Why this is a serious idea, not a trick

### Leg 1 — the measurement: today's networks go dead

This is the empirical foundation, and it is the part of AP12 that is not opinion.

Train a standard deep network on one task, then another, then another, in sequence — the way a life is lived rather than the way a dataset is served. Something strange happens. It is **not** mainly that the network forgets the old tasks, which is the failure everyone knows about. It is that the network gradually **loses the ability to learn the new ones**. Its capacity to absorb anything at all wears out.

Sutton's group measured it and published it in **Nature** in 2024. On a version of ImageNet repurposed into a long sequence of tasks, accuracy fell from about **89% on an early task to about 77% by the two-thousandth**. The network was not confused. It was, in their term, no longer **plastic**.

::: key
**Two opposite failures, and the field mostly knows only one.** *Catastrophic forgetting* is losing information you already had. **Loss of plasticity is losing the ability to take new information in.** They are opposite ends of the same dilemma — a system needs stability to keep what it knows and plasticity to learn what it doesn't — and a fix for one can worsen the other. Almost all of continual-learning research has aimed at forgetting. AP12's claim is that plasticity is the one that blocks AGI. *(Full treatment: [continual learning — why the networks go dead](../30-across-the-approaches/03_continual-learning-and-plasticity.md).)*
:::

The proposed fix, **continual backpropagation**, is deliberately unglamorous: give every weight its own learning rate rather than one global rate, tune those rates continuously, and keep injecting fresh randomly-initialised units to replace ones that have gone inert. Sutton's position is that loss of plasticity is *curable* with the right algorithm — but that until it is reliably cured, nothing else in this bet can be built.

### Leg 2 — the argument: the big world hypothesis

Why should an agent have to keep learning forever? Because of a claim about the world rather than about the agent.

**The big world hypothesis:** the world is vastly more complex than any agent that lives in it, and vastly more complex than any simulator of it. No model an agent can hold will ever be more than a rough approximation of a small local piece. Therefore the approximation must be **updated continuously and forever** — not because the algorithm is imperfect, but because the mismatch between a small agent and a big world is permanent.

Read that against how current systems work and the critique writes itself: a frontier model is trained once and then **its weights never change**. Whatever it learned about the world is frozen at a date. Under the big world hypothesis that is not a deployment convenience, it is a category error.

Sutton's sharper version of the same point: a language model can predict **what a person would say**. It cannot predict **what will happen**. Those are different capabilities, and only the second is a model of the world. His estimate — offered as a rough judgement, not a measurement — is that today's models represent roughly a quarter of what intelligence involves.

### Leg 3 — the architecture: OaK, and how an agent builds its own abstractions

The Alberta Plan is the research programme; **OaK is the proposed architecture**. It is a model-based RL architecture with three unusual properties:

1. **Every component learns continually.** Not some. All of them, at every timestep.
2. **Every learned weight has its own step-size**, and those step-sizes are themselves meta-learned by online cross-validation — the machine tuning its own learning rates, per weight, forever.
3. **Abstractions in space and time are created continually**, by a repeating five-stage loop.

That loop is the heart of it, and it is the part that matches "the agent designs its own goals":

| Stage | What happens | Plain version |
|---|---|---|
| **F**eature **C**onstruction | The agent builds new features of its own state | *"Here is something worth noticing"* |
| **S**ub**T**ask | A feature is turned into a sub-goal — attain it | *"Let me try to make that happen"* |
| **O**ption | A skill is learned that achieves the sub-task | *"Here is how I make it happen"* |
| **M**odel | A transition model of that skill is learned | *"Here is what happens when I do it"* |
| **P**lanning | The model is used to improve policy and value | *"Now I can plan with it"* |

**FC-STOMP.** And then it recurses: the features that turn out to help with planning become the raw material for the next, more abstract round of feature construction. Over the whole thing sits a feedback process that continually judges how useful each feature, sub-task, option and model is, and decides what to keep and what to develop further.

::: note
**Nobody writes the sub-goals.** That is the property you would come to this bet for. In ordinary RL a human specifies the reward *and*, usually, the task structure. In OaK the only human input is the top-level reward signal; every sub-goal below it is invented by the agent out of features it invented, and kept or discarded on evidence. This is a different mechanism from [AP9's](09_ap9-open-endedness.md) archives and populations, aimed at the same target.
:::

**The four commitments** of the Alberta Plan, which explain a lot of what looks strange about the bet:

- **Experience only.** All learning is grounded in three signals — observation, action, reward. Nothing that is internal to the environment but invisible to the agent may be used.
- **No human-curated shortcuts.** No special training sets, no human assistance, no privileged access to the world's internals.
- **Temporal uniformity.** All moments are treated alike. There is no training phase and no deployment phase; learning and planning happen on every timestep.
- **Computational realism.** Methods must scale with computation — the Bitter Lesson, applied to itself.

### So, what does AP12 say "intelligence" is?

**Intelligence is a continuing process, not an artifact.** It is what a single agent does when it is embedded in a world too big to model, given only its own senses, actions and a reward, and never allowed to stop updating. On this definition a frozen model is not a weak intelligence — it is a *recording* of one.

---

## Judging the bet: where it is stuck

### Stuck #1 — it is a proposal, not a result

This is the honest headline and Sutton says it himself: **OaK cannot be built yet**, because reliable ongoing deep learning — the plasticity problem in Leg 1 — is still missing. So the architecture is a design for something whose foundational component does not yet work.

Compare that with the other bets. AP1 has GPT-scale models. AP2 has reasoning models. AP4 has AlphaZero. **AP12 has a diagram, a Nature paper about why the diagram cannot be implemented, a two-month-old lab, and a Turing Award winner's conviction.** That is a real bet, and it is a much earlier-stage one than its pedigree makes it sound.

### Stuck #2 — the reward hypothesis is inherited, and it is contested

AP12's third founding principle is that all goals reduce to maximising a scalar reward. That is [AP4's](04_ap4-rl-from-interaction.md) *"reward is enough"* claim, and **every critique of it lands here unchanged** — sparse and mis-specified rewards, reward hacking, and the published arguments that a single scalar cannot capture open real-world goals. AP12 does not answer those; it assumes past them. If the reward hypothesis is wrong, AP12 is wrong with it.

There is a sharper version specific to AP12. The bet's appeal is that the agent invents its own sub-goals — but it invents them *in service of a top-level reward that a human still writes*. The human intervention has been pushed up a level, not removed. That is a real advance and it is not the same as elimination.

### Stuck #3 — "no human data" throws away the one thing that demonstrably works

The commitment to experience alone is principled and expensive. Human text is the only training signal that has ever produced a system with broad competence about the world, and AP12 refuses it on principle.

The counter-argument from the other side of the debate: an agent starting from nothing must rediscover, from its own experience, what humanity took a hundred thousand years and a shared language to accumulate. Sutton's answer is that this is exactly the point — an intelligence trained on human text is **capped at human ability**, while one that learns from the world is not. Both halves of that are arguable, and the disagreement is currently the sharpest live dispute in the field.

One published counter-jab worth knowing: Sutton's position leans on the claim that animals do not learn by supervised imitation, which several critics say understates how much human children learn precisely by copying.

### Stuck #4 — nothing at scale has been shown

Every demonstration in this programme is small. The plasticity results are on MNIST- and ImageNet-scale sequences. The testbeds are deliberately lightweight. There is no equivalent of "and then it beat the world champion", and the stated milestone — a trillion-parameter agent running on **20 watts** within five to ten years — is an aspiration with no public path to it.

::: warn
**Note the shape of that number.** Twenty watts is roughly the human brain's power budget. Quoting it is a statement of ambition and of what the bet believes is *possible*, not a projection from anything currently working. Treat it as rhetoric with a point, not as a roadmap.
:::

### The big question under all of these

**Is continual learning a missing component, or a missing paradigm?**

If it is a component, the other bets absorb it: someone solves plasticity, it becomes a standard trick, frontier models start updating after deployment, and AP12 turns out to have been a valuable critique of AP1 rather than a rival to it.

If it is a paradigm, then every system trained-then-frozen is on a road that ends, and the whole industry is optimising the wrong object. **Sutton is betting the second.** Nothing yet decides between them, and the evidence that would — a system that learns continually at scale, or a convincing demonstration that frozen models keep improving without it — does not exist on either side.

---

## ⚠️ Honesty box

- **This is the least settled card on the map, by a wide margin.** Every other approach has at least one working system to point at. This one has a research programme, a measured obstacle, and a lab that is two months old.
- **The card is built on talks, a podcast, a position paper and one Nature paper** — not on a body of results. That is not a flaw in the sourcing; it is the actual state of the bet, and you should read the confidence accordingly.
- **I have not watched the OaK talks in full.** The architecture description above comes from written summaries of RLC-2025 / AGI-2025 / NeurIPS-2025 and from the Alberta Plan paper. FC-STOMP and the three special properties are well-attested across independent write-ups; finer details may be off.
- **The Sutton-versus-LLM debate is live and I am not neutral ground.** I have given his position its strongest form and the main counters, but this is an argument in progress between serious people, and the summary above compresses it.
- **Dates decay unusually fast here.** Oak Lab was announced 14 July 2026; the podcast is from 8 September 2026. Anything about the lab's staffing, funding or output will be stale within months.
- **This card was missing for two months and that is a process failure, not bad luck.** See the revision notes.

---

## How to use this (if you want to direct AI work)

- **When someone says a model "learns from user feedback", ask whether the weights change.** Usually they do not — what changes is a prompt, a retrieved document, or a fine-tune run offline on a schedule. That distinction is the whole of AP12's critique and it is easy to check.
- **Treat "continual learning" as two questions, not one.** *Does it forget?* and *can it still learn?* Systems are routinely evaluated on the first and almost never on the second.
- **Discount the trillion-parameters-on-20-watts framing** when judging the work, and judge the plasticity results instead. Those are measurable and they are where the bet is actually being tested.

---

## Connections

- **Its parent:** [AP4 · RL from interaction](04_ap4-rl-from-interaction.md) — AP12 is built inside AP4's frame and inherits both its bet and its critiques; AP4's *"era of experience"* is the philosophy AP12 makes into an architecture.
- **Its target:** [AP1 · scale](01_ap1-scale-and-foundation-models.md) — AP12 argues that AP1 misreads the Bitter Lesson, which AP1 rests on.
- **Its cousin:** [AP9 · open-endedness](09_ap9-open-endedness.md) — same goal (a system that sets its own problems and never converges), different machinery (one continually-learning agent, not a population and an archive).
- **The obstacle, in full:** [Continual learning — why the networks go dead](../30-across-the-approaches/03_continual-learning-and-plasticity.md).
- **Where to actually start on it:** [Ramp · AP12 — OaK and continual learning](../60-entry-ramps/02_ap12-oak-continual-learning.md).

---

## Check yourself *(try one, from memory)*

1. Catastrophic forgetting and loss of plasticity are opposite failures. State each in one line, and say which one AP12 claims blocks AGI.
2. What is the big world hypothesis, and what does it imply about shipping a model with frozen weights?
3. Walk through FC-STOMP. At which stage does the agent invent something a human would normally have specified?
4. Sutton wrote the Bitter Lesson, which AP1 rests on. On what grounds does he say AP1 misreads it?
5. AP12 says the agent designs its own sub-goals. What does a human still supply, and why does that matter?

---

## Revision notes

- **rev 1 · 2026-09-09 · new — and a documented miss.** Added as a twelfth bet after the learner found Sutton and Javed's Sequoia podcast (published 8 September 2026) and asked whether the map covered it. It did not: a project-wide grep for "OaK" and "Alberta Plan" returned **zero hits**. Only the philosophy was present, as Silver & Sutton's *"Era of Experience"* inside [AP4](04_ap4-rl-from-interaction.md).

  **Why the miss happened, stated plainly.** The map's v3.0 was written on **2026-07-14**; Oak Lab was announced on **2026-07-14**. The same day — so the lab itself could not have been caught. But that only excuses part of it: the OaK talks were given at RLC-2025 and AGI-2025 in **August 2025**, the plasticity paper is from **Nature 2024**, and the Alberta Plan is from **2022**. All three predate the map by a year or more and all three were missed. This is precisely the staleness [`HARD_RULES §2.6`](../../INSTRUCTIONS/HARD_RULES.md) and finding **D1** of the [2026-07-21 audit](../../REVIEWS/AUDIT_2026-07-21_v3.0.md) exist to prevent, and it got through anyway — which says the freshness pass needs to cover *named research programmes*, not only benchmark numbers.

  Placed as its own card rather than folded into AP4 because none of the eleven describes it: AP4 covers the *bet* (reward is enough) not this architecture; [AP3](03_ap3-agents-and-cognitive-architectures.md) covers LLM agent loops, a different tradition; [AP9](09_ap9-open-endedness.md) shares the goal but not the mechanism. Grounded in the Alberta Plan paper (arXiv 2208.11173) read via ar5iv, the Nature 2024 plasticity paper, written summaries of the RLC/AGI/NeurIPS 2025 OaK talks, the Oak Lab founding, and the September 2025 "dead end" interview with its published counter-arguments.
