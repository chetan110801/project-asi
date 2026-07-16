---
id: c-verdict
sortkey: 4001
title: The verdict — judging the map: which bets actually get to AGI?
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap2-reasoning, c-ap3-agents, c-ap4-rl, c-ap5-world-models, c-ap6-brain-based, c-ap7-neurosymbolic, c-ap8-program-synthesis, c-ap9-open-endedness, c-ap10-embodiment, c-ap11-whole-brain-emulation]
provides: [the-one-crux, does-scale-absorb-it, the-four-families, scale-plus-ingredients, the-independent-viewpoint, how-to-rank-the-bets]
resources: []
status: ready
reading_time: 34 min
rev: 1
created: 2026-07-16
updated: 2026-07-16
---

# The verdict — judging the map: which bets actually get to AGI?

*You have now read all eleven bets on how to build a machine that can think in a general way. This page does the thing the whole map was **for**. A map that only lays the bets side by side is a reference book. The point of this project was never a reference book — it was **an independent viewpoint**: a clear, honest, defensible answer to the real question. Which of these bets is most likely to reach AGI? Which are not eleven separate races at all, but pieces of one machine? Which are dead ends dressed up as roads? This page builds that answer, one careful step at a time. First it shows that the eleven bets, which look so different, almost all end on the **same single question** — so the whole map quietly collapses onto **one axis of disagreement** *(an **axis** here = a single straight line along which things are arranged; here, one question that every bet takes a side on)*. Then it groups the eleven into **four families** and shows how they **combine** instead of compete. Then it states a viewpoint — a ranked, weighed judgement of what is most and least likely to be part of the answer — and, just as important, **the two ways that viewpoint could be wrong.** This is not the truth handed down; it is one well-grounded reading of the field, meant to be argued with, sharpened, and replaced as the evidence moves. That is what a research position is.*

> **You are here:** this is **The verdict** — the closing page of the map (see [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)). It is **not a twelfth bet.** It is a *judgement on the other eleven* — the "independent viewpoint" the project set out to build. AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one narrow task.
>
> **This page builds on every page below it**, so read the eleven approach cards first — it leans on all of them. Each is named again where it is used, with a one-line reminder, so you will not be lost; but the full argument of each lives on its own page, and this page does not re-make it. If a bet's name here is new to you, read that bet's page, then come back. Everything here is a *comparison across* the eleven, not a re-teach of any one.
>
> **Where the judgement comes from:** nothing on this page is a new fact about the world. Every claim is a *synthesis* — a drawing-together — of what the eleven cards already established, each of which was grounded in real sources and given a live web check (state-of-the-art **as of July 2026**). The *viewpoint* is a judgement built on those cards, and it is marked as a judgement, not a fact. Because the field moves monthly, the ranking is dated and meant to be revised; the *method* for ranking is the durable part.

---

## The judgement in one minute

Here is the whole verdict, as short as it goes — then the rest of the page earns it.

**The eleven bets are not eleven horses in one race. They are positions in a single argument, and the argument has one question at its centre: is making the models bigger *enough* on its own, or is a second ingredient needed — and if a second ingredient is needed, does the big model just *absorb* it *(take it in and make it part of itself)*, or does the ingredient stay a separate thing? Almost every card on the map ended on exactly this question. Once you see that, the map reorganises itself. The mainstream bets — scale, longer thinking, agents, reward — are not rivals; they are already fused into one working system, the thing every frontier lab actually ships. The "you need a second ingredient" bets — world-models, neurosymbolic, program-synthesis, open-endedness, embodiment — are mostly being *absorbed* as ingredients of that system rather than replacing it: their real wins so far run on top of big models, not instead of them. And the "copy the brain" bets — understand it, or copy it blind — are long-horizon insurance, valuable as ideas more than as near-term plans. So my viewpoint is not "bet X wins." It is: the winning path is scale **plus a stack of ingredients**, the big model keeps absorbing the best of its challengers (the pattern that has repeated for a decade), but the specific gaps those challengers name — handling true novelty, and running out of human data — are real and unclosed, so "scale alone is enough" is not proven and may still break. Watch those two gaps; they are where the whole thing could stall.**

That is the position. Now let me show my working — because a verdict you cannot check is just an opinion.

---

## First, a one-line reminder of the eleven

You have read them all. Here they are in one place, each in a single plain line, so the comparison below has everything in view at once. *(A **bet** here = a serious wager, by serious people, about how you actually reach AGI.)*

**The mainstream stack — most labs, most computer power, most money:**

- [AP1 · scale](../20-the-approaches/01_ap1-scale-and-foundation-models.md) — **make the model bigger.** One simple training job (guess the next word) plus enormous size, and skills appear on their own.
- [AP2 · reasoning](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — **let it think longer.** Spend computer power *at answer-time*: write out the steps, try many paths, check the work.
- [AP3 · agents](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) — **a mind is a system of parts.** Wrap the model in memory, tools, planning, and a loop, so it can *do* long jobs.
- [AP4 · RL from interaction](../20-the-approaches/04_ap4-rl-from-interaction.md) — **reward is enough.** Put the model in a world, give it a goal as a score to maximise, and let it learn by trial and error. *(RL = reinforcement learning — learning from reward, not from human answers.)*

**The "you need a second ingredient" dissents — respected, funded, unproven as *the* path:**

- [AP5 · world models / JEPA](../20-the-approaches/05_ap5-world-models-jepa.md) — **text is the wrong food.** Learn how the world *works* by watching it (mostly video), build an inner model of it, and plan against that model.
- [AP7 · neurosymbolic](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) — **join the learner and the reasoner.** Keep the flexible neural learner, bolt on an exact rule-following reasoner, so the whole both learns *and* reasons reliably.
- [AP8 · program synthesis / ARC](../20-the-approaches/08_ap8-program-synthesis-arc.md) — **scale is climbing the wrong ladder.** It grows stored *skill*, but intelligence is handling the *truly new* from little data; get it by searching for small programs, not by scaling.
- [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md) — **grow a mind, don't design it.** Copy how nature did it: run a process that never stops inventing new, interesting challenges, and let a mind grow out of it.
- [AP10 · embodiment](../20-the-approaches/10_ap10-embodiment.md) — **a mind needs a body.** Meaning is *earned* by acting on the physical world and sensing what changes, not read out of text.

**The "copy the one thing that works" bets — the brain as the only existence proof, long-horizon:**

- [AP6 · brain-based](../20-the-approaches/06_ap6-brain-based.md) — **understand the brain's method and rebuild it.** Reverse-engineer the one repeated cortical recipe, then copy *that method* into a machine.
- [AP11 · whole-brain emulation](../20-the-approaches/11_ap11-whole-brain-emulation.md) — **copy the brain blind.** Scan a real brain in full detail and duplicate the exact structure in a computer — understand nothing, copy everything.

Keep those eleven lines nearby. The rest of the page is one long, careful comparison of them.

---

## Part 1 — the map has only one real axis

When you first read the eleven cards, they feel like eleven different worlds: text, video, reward, logic, robots, brains. But look at where each one *ended* — at the honest "where it's stuck" section, the deepest doubt each faced. A striking thing happens: **almost all of them end on the same sentence.** Said in plain words, that sentence is:

> *"This is a real, useful idea — but is it a **separate road to AGI**, or just a **temporary layer** that a big enough model will eventually absorb into itself?"*

Let me show you it is really the same doubt each time, because this is the key that unlocks the whole map:

- [AP3 · agents](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) ended on it directly: in 2026 the hand-built scaffolding around the model (the memory, the planning graph, the critic) is *dissolving into the model* — a single model now plans and checks itself inside its own thinking. So is agent-building a road, or an **app layer** *(a thin wrapper of software built on top of the real thing)* that the next model absorbs?
- [AP5 · world models](../20-the-approaches/05_ap5-world-models-jepa.md) ended on it: maybe a big text model *already contains* a working model of the world, learned from words — so world-modelling is not a rival to scale but something scale produces on its own.
- [AP7 · neurosymbolic](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) ended on it: is the symbolic reasoner a real second half of the mind, or a **crutch** *(a temporary support you lean on until you no longer need it)* that scale eventually absorbs — the same doubt again?
- [AP8 · program synthesis](../20-the-approaches/08_ap8-program-synthesis-arc.md) lived it: its hardest test, ARC, was beaten by a *scaled* model (o3, late 2024) doing an expensive search — part new idea, part just more compute.
- [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md) ended on it: its recent wins are open-ended loops *wrapped around* foundation models — so is it a distinct road, or scale's outer loop?
- [AP10 · embodiment](../20-the-approaches/10_ap10-embodiment.md) ended on it: the winning robots are ordinary large models with actions bolted on — is the body a separate road, or scale's **last mile** *(the final short stretch of a long journey — the easy-sounding finish that is often the hardest part)*?
- Even [AP6](../20-the-approaches/06_ap6-brain-based.md) and [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md), the brain bets, ended on a cousin of it: they might be *right but too slow* — overtaken by scale long before they arrive.

Six of the eleven cards, independently, end on this exact question — and two more (the brain bets) end on a close cousin of it. That is not a coincidence. It means the map only *looks* like eleven separate worlds. **Underneath, there is one axis of disagreement**, and every bet is a position on it. Here is the axis, stated once and carefully.

### The axis: the scaling-suffices debate

The single question the whole field is really arguing about — you met it first on the [AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md), where it is called the **scaling-suffices debate** *(the argument over whether "scaling" — making models bigger with more data and more computer power — "suffices," meaning is by itself enough, to reach AGI)*. Lay the field out along it:

- **At one end: "scale is (almost) enough."** Keep making the model bigger and training it better, and the remaining abilities — reasoning, planning, world-knowledge — will keep appearing as they have so far. The extra ideas (AP2, AP3, AP4) are just ways of *spending* the intelligence scale already built, not separate sources of it. This end rests on **Sutton's Bitter Lesson** *(the hard-won finding, from the AP1 card, that over AI's whole history the methods that simply use more computer power keep beating the methods that build in clever human knowledge by hand)*.
- **At the other end: "scale is not enough — a second ingredient is required."** Bigger models will keep getting more fluent but will not, on their own, close a specific gap: handling genuinely new problems (AP8), truly understanding the world rather than words about it (AP5, AP10), reasoning that never breaks (AP7), or learning without end (AP9). To cross that gap you need a different idea, added on purpose.

Every card is a point between these two ends. And the reason the "road or app layer?" doubt keeps appearing is that the two ends are fighting over each bet: the scale camp says "your idea is just a layer we will absorb," and the second-ingredient camp says "no, our idea is a missing piece scale cannot supply." **That fight — repeated eleven times — is the whole map.** Once you hold that, judging the bets becomes possible, because you are no longer ranking eleven unrelated things. You are answering one question, eleven times: *for this idea, is scale the source, or only the fuel?*

---

## Part 2 — the eleven are four families, and they combine

The second thing that dissolves on a close read is the idea that the bets *compete*. Mostly, they don't. They **stack** — several of them are already running together inside one system. Sorting the eleven into four families makes this clear, and makes the ranking in Part 3 possible. *(A **family** here just means a group of bets that share a core idea and tend to be used together.)*

### Family A — the mainstream stack (AP1 + AP2 + AP3 + AP4)

These four are **not four bets; they are four layers of one machine.** Look at what a frontier AI system actually is in 2026, and you see all four at once, fused:

- a huge pretrained model ([AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md)) —
- that thinks in steps before answering ([AP2](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)) —
- wrapped in memory, tools, and a loop so it can do long jobs ([AP3](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md)) —
- and trained on reward, not just human text, so it learns from checkable success ([AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)).

That single description is today's leading systems. The four "bets" are the four things you do in order to build one. This is why arguing "AP1 versus AP2" is a category mistake *(treating things of one kind as if they were rival things of another kind — here, treating layers of one system as competing systems)*. They are the layers of the current winner. Any honest verdict starts by treating Family A as **one combined bet that is already winning**, not four bets to rank against each other.

### Family B — the "second ingredient" dissents (AP5, AP7, AP8, AP9, AP10)

These five each name a **specific gap** they say the mainstream stack cannot close by scaling, and each proposes the missing ingredient. Line up the gaps, and notice they are exactly the gap-list from the [top of the map](../APPROACHES_TO_AGI.md) — the honest list of what today's systems still lack:

| Dissent | The gap it names | The ingredient it adds |
|---|---|---|
| [AP5 · world models](../20-the-approaches/05_ap5-world-models-jepa.md) | grounding — knowing the world, not just words about it | learn from video; build and plan in an inner world model |
| [AP7 · neurosymbolic](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | reasoning that never breaks (systematic, reliable) | an exact rule-following reasoner joined to the learner |
| [AP8 · program synthesis](../20-the-approaches/08_ap8-program-synthesis-arc.md) | handling *true novelty* from little data | search for small programs, guided by the model |
| [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md) | learning that never stops; running out of data | a process that generates its own endless new challenges |
| [AP10 · embodiment](../20-the-approaches/10_ap10-embodiment.md) | meaning tied to the real physical world | give it a body; learn by acting and sensing |

Here is the decisive fact about Family B, and it is the crux of the whole verdict: **every real, checkable win these dissents have produced so far runs *on top of* a big model, not instead of one.** The world-model system V-JEPA 2 is built from large learned networks; [AP7's](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) triumph AlphaGeometry uses a big *neural* model to guess the move that the rule-engine then checks; [AP8's](../20-the-approaches/08_ap8-program-synthesis-arc.md) ARC scores come from *scaled* models doing search; [AP9's](../20-the-approaches/09_ap9-open-endedness.md) recent wins (AlphaEvolve, the Darwin Gödel Machine) are open-ended loops *around* foundation models; [AP10's](../20-the-approaches/10_ap10-embodiment.md) best robots are web-trained models with actions added. So the honest 2026 reading is uncomfortable for the dissents: **so far, they are being absorbed as ingredients of the mainstream stack, not winning as separate paradigms.** *(A **paradigm** = a whole way of doing something, a complete approach — as opposed to a single technique inside one.)* That is the Bitter Lesson happening in slow motion, live, across five bets at once.

But — and this is why the dissents are not dismissed — **naming a real gap is itself valuable even if scale ends up filling the gap.** The dissenters are the field's best *gap-finders*: they tell you exactly where the mainstream stack is weak (novelty, grounding, endless learning), which is exactly where it might stall. Whether the fix comes from *their* ingredient or from *more scale*, they are pointing at the real trouble. Hold both halves: **weak so far as separate roads, invaluable as maps of the weak spots.**

### Family C — the data-wall answers, hiding inside A and B (AP4 + AP9 + AP10)

Now a subtler pattern, one the four-family split reveals. Three bets — reward ([AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)), open-endedness ([AP9](../20-the-approaches/09_ap9-open-endedness.md)), embodiment ([AP10](../20-the-approaches/10_ap10-embodiment.md)) — are all really answers to *one* problem that the [scaling page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) named: the **data wall** *(the point where the supply of good human text to train on runs out — "we have but one internet," and the models have nearly read all of it)*. If you cannot get more human text, where does new training experience come from?

- [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) answers: from the model's *own* successes and failures at checkable tasks (learn from reward, not from us). Silver and Sutton's 2025 phrase for this was the **"era of experience."**
- [AP9](../20-the-approaches/09_ap9-open-endedness.md) answers: from an endless stream of *self-generated* new challenges the system invents for itself.
- [AP10](../20-the-approaches/10_ap10-embodiment.md) answers: from a body's stream of real sensing and acting in the physical world.

This is why these three are rising in importance right now: the data wall is arriving, and they are the three doors out of it. That reframes them. They may not be separate *destinations* (separate kinds of mind); they may be the **fuel supply** for the mainstream stack once the internet runs dry. A door out of the data wall is not a rival to scale — it is what lets scale keep going. Seeing this is worth more than any single ranking: **the most important thing several "dissents" are actually doing is keeping the mainstream bet alive past its biggest limit.**

### Family D — the brain bets, the long game (AP6 + AP11)

The last two stand apart. Both start from the one hard fact no other bet can match — *the brain is the only thing we know for certain is generally intelligent* — and both are, on any honest timeline, **the slowest roads on the map.** [AP6](../20-the-approaches/06_ap6-brain-based.md) wants to understand the brain's method and rebuild it; [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md) wants to copy a brain in full detail without understanding it at all. Their value is not that they will likely arrive first — they almost certainly will not. Their value is **twofold**: they are *insurance* (if the mainstream stack hits a wall it cannot climb, the one known working design is the fallback), and they are the map's cleanest *thought experiments* about the deepest question — how much understanding does building a mind actually require? ([AP6](../20-the-approaches/06_ap6-brain-based.md) says "the algorithm"; [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md) says "none"). Judge them as ideas and as insurance, not as this decade's likely winner.

---

## Part 3 — the independent viewpoint (a ranked read)

Now the part a reference book never gives you: a judgement. I will rank the eleven bets — but *not* by "which wins alone," because Part 2 showed that is the wrong question. I rank them by a better one:

> **How likely is this bet to be *part of the path that actually reaches AGI*?** — whether as the engine, an ingredient, or the fuel.

That question rewards a bet for *doing real work on the path* even if it never wins by itself, and it marks down a bet that is interesting but likely to be overtaken *(passed and left behind by a faster approach)*. Here is the ranking, with the reason and an honesty tag on each. *(**[Established]** = the cards make this near-certain; **[Likely]** = the balance of evidence leans this way; **[Contested]** = serious people disagree and it is genuinely open.)*

| Rank | Bet | Why it sits here | How sure |
|---|---|---|---|
| **1** | [AP1 · scale](../20-the-approaches/01_ap1-scale-and-foundation-models.md) | Everything else on the map runs *on* it. Even its challengers win only when built on a big model. It is the floor of the whole field. | **[Established]** it is part of the path |
| **2** | [AP2 · reasoning](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Went from idea to *standard* in one year; every frontier lab ships it. The clearest recent capability jump came from here. | **[Established]** |
| **3** | [AP4 · RL from interaction](../20-the-approaches/04_ap4-rl-from-interaction.md) | The engine *inside* AP2's reasoning, and the leading answer to the data wall (learn from your own checkable experience). Already fused into the stack. | **[Established]** |
| **4** | [AP3 · agents](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | The *form* every capable system is deployed in. Its status as a *separate* bet is shrinking (the scaffolding is dissolving into the model) — but the capability it names is central. | **[Likely]** (as a layer, not a separate road) |
| **5** | [AP5 · world models](../20-the-approaches/05_ap5-world-models-jepa.md) | Names the realest gap (grounding), and the 2025–26 surge is large and serious. Most likely of the dissents to supply a true missing ingredient — or to be what scale grows on its own. | **[Contested]** — real gap, unproven as a separate road |
| **6** | [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md) | A strong data-wall answer (self-generated challenges) and it copies the *one* process that provably made a mind (evolution). But it cannot yet define or measure what it optimises. | **[Contested]** |
| **7** | [AP8 · program synthesis](../20-the-approaches/08_ap8-program-synthesis-arc.md) | Owns the sharpest true criticism on the map — *skill is not intelligence* — and the ARC test keeps exposing a real novelty gap. But as a *standalone* road it keeps being partly absorbed (o3 beat ARC-AGI-1 with a scaled model). | **[Contested]** — invaluable critique, weak as a separate paradigm |
| **8** | [AP10 · embodiment](../20-the-approaches/10_ap10-embodiment.md) | Almost surely *necessary for a robot* AGI and a real data source — but a bodiless model got far on text alone, so a *body* may not be needed for the *mind*. Hot as engineering, unproven as the key. | **[Contested]** |
| **9** | [AP7 · neurosymbolic](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Its real wins (AlphaGeometry) are beautiful but trapped in tidy checkable domains, and "neurosymbolic" is so broad it is hard to call a single distinct bet. Likely absorbed as a technique (models calling tools), not a paradigm. | **[Contested]** — most likely to dissolve into "just what good systems do" |
| **10** | [AP6 · brain-based](../20-the-approaches/06_ap6-brain-based.md) | The deepest idea and the best insurance, but we still do not know the brain's algorithm, and the brain-ignoring bets are years ahead. A long game. | **[Likely]** as insurance / **[Contested]** as this decade's path |
| **11** | [AP11 · whole-brain emulation](../20-the-approaches/11_ap11-whole-brain-emulation.md) | The longest horizon by far (a wiring diagram is not yet a running worm), and even total success yields a human-level mind we cannot explain. An idea to understand, not a plan to join. | **[Established]** it is the slowest / **[Contested]** whether it ever arrives |

Read the ranking correctly. The top four are not "better bets" — they are the parts of the machine that is *already working*, so they are near-certain to be on the path. The middle five are the field's honest doubts about that machine, ranked by how likely each is to name a gap scale truly cannot fill on its own. The bottom two are the long game. **No bet on the map is a proven dead end** — that is an important honesty point, and I will not pretend otherwise. The weakest claim I will make is softer and more defensible: *some bets (AP7, AP8 as anti-scale paradigms) look more like ingredients-and-critiques than separate roads, and one (AP11) is very unlikely to arrive in time.*

### The viewpoint, stated plainly

Putting the ranking and the four families together, here is the position — the thing this whole project was built to produce:

**The most likely path to AGI is scale *plus a stack of ingredients* — not scale alone, and not any single challenger replacing scale.** The mainstream stack (AP1+AP2+AP3+AP4) is the engine and is winning; it keeps *absorbing* the best ideas of its challengers rather than being overthrown by them, which is the Bitter Lesson repeating yet again. *But* the challengers name two real, unclosed gaps that could still stall the whole thing, and these are the two things to watch above all else:

1. **The novelty gap** ([AP8](../20-the-approaches/08_ap8-program-synthesis-arc.md), [AP7](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md)) — today's systems still break on genuinely new problems, and no amount of fluency has closed that. If it turns out scale *cannot* close it, one of the second-ingredient bets stops being an ingredient and becomes the road.
2. **The data wall** ([AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md), answered by [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)/[AP9](../20-the-approaches/09_ap9-open-endedness.md)/[AP10](../20-the-approaches/10_ap10-embodiment.md)) — human text is nearly used up, so whether scale keeps climbing now depends on the data-wall answers working. If experience, self-generated challenges, and embodied data *don't* substitute for the missing internet, the scaling curve bends and the mainstream stack slows.

So the bet I would actually make, if forced: **scale-plus-ingredients gets there, with reasoning-and-reward (AP2/AP4) as the live edge and world-models/open-endedness (AP5/AP9) as the ingredients most likely to matter next — but the honest probability that "scale alone" is enough is neither near 1 nor near 0, and anyone claiming certainty either way is claiming more than anyone can know.** That last clause is not a hedge; it is the single most defensible claim in the whole field, and Part 4 is why.

---

## Part 4 — the two ways this viewpoint is wrong

A viewpoint you cannot break is a belief, not a research position. So here, deliberately, are the two ways my own verdict could be wrong — and they pull in *opposite* directions, which is exactly why honest people land in the uncertain middle.

### Break #1 — I under-rate scale (the skeptics have been wrong for a decade)

The strongest case *against* my respect for the dissents is history. For ten years, the smartest critics of scale kept naming a gap — "it can't do X" — and then a bigger model did X, and the critics pointed to a new gap Y instead. Reasoning was supposed to be impossible for a next-word predictor; then chain-of-thought and reasoning models did it. Grounding was supposed to require a body; then text-trained models turned out to know a great deal about the physical world. **The Bitter Lesson has an almost unbroken winning streak, and betting against it has been the losing side of every round so far.** If that streak simply continues, then the middle five families are *all* app layers, my ranking over-credits them, and the answer is closer to "scale (plus the cheap tricks of AP2/AP3/AP4) is basically enough." A fair verdict has to hold this: **my instinct to respect the gap-finders may just be the same mistake their predecessors made.**

### Break #2 — I over-rate scale (the walls are real and arriving)

The opposite case is just as strong. Two of the walls are not predictions; they are *here*. The **data wall** is arriving now — labs already lean on synthetic and reward-based data because the good human text is nearly exhausted ([scaling page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md)). The **novelty gap** is measured, not guessed — on the ARC-AGI-2 test built to resist memorising, the best frontier model scored around **37.6%** while ordinary people score around **60%** (as of late 2025, per the ARC Prize). And the very fact that the frontier *quietly stopped* betting on pure pretraining scale and moved to test-time compute ([AP2](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)) is itself evidence that scale-alone was *already* judged insufficient by the people with the most information. If these walls hold, then "scale plus cheap tricks" stalls, and a *real* second ingredient — a genuine world model, genuine program synthesis, a genuine open-ended process — becomes not optional but the real path. In that world my ranking *under*-credits the dissents.

### Why the honest answer is the uncertain middle

Notice that Break #1 and Break #2 cannot both be fully right, and neither can be ruled out from where we stand in July 2026. That is not a failure of analysis; **it is the analysis.** The correct confidence on "does scale suffice?" is genuinely somewhere in the wide middle — and the strongest, most defensible thing a research position can say is exactly that, *plus* a clear statement of what evidence would move it: a frontier model that robustly solves ARC-style novelty with no task-specific training would swing it toward Break #1 (scale wins); a frontier model that visibly *stops improving* as human data runs out, with the data-wall answers failing to substitute, would swing it toward Break #2 (a real second ingredient is needed). Until one of those happens, **the map stays live, and so does the argument.** That is why this page ends not with a winner, but with a lens, a ranking, and two things to watch.

---

## ⚠️ Honesty box

- **This is a viewpoint, not a fact.** Every other page on the map grounds its claims in real sources. This page *synthesises* those pages into a judgement, and a judgement — however careful — is contestable. Read it as one well-supported reading you can argue with, not as settled truth. **[Contested by design.]**
- **"Scale-plus-ingredients" is a position, and the field's best people disagree with it in both directions.** Some serious researchers think scale alone is nearly enough; others think it is a dead end without a new paradigm. My middle position is defensible, not proven. **[Contested.]**
- **No bet here is a proven dead end.** It is tempting, in a verdict, to declare losers. The honest evidence does not support that. The most I claim is that some bets look more like *ingredients and critiques* than separate roads (AP7, AP8), and one is very unlikely to arrive in time (AP11). That is a weaker, truer claim than "these lose." **[Established as an honesty limit.]**
- **The ranking is dated and will move.** It reflects the field as of July 2026. A single big result — a frontier model that cracks true novelty, or a scaling curve that visibly bends at the data wall — could reorder it within months. The *method* (find the one axis, group into families, rank by "part of the path," name the breaks) is the durable part; the ordering is a snapshot. **[Established core, dated specifics.]**
- **Beware the two easy stories.** "Scale is all you need" and "scale has hit a wall" are both clean, quotable, and probably too simple. The uncomfortable middle — scale keeps winning *and* names real gaps it has not yet closed — is less quotable and more likely true. Distrust any verdict (including a future version of this one) that sounds too certain. **[Contested.]**

---

## How to use this (if you want to direct AI work, or form your own view)

- **Judge any new "approach to AGI" with the one axis first.** When someone pitches a method, don't ask "is it clever?" Ask the Part 1 question: *is scale the source of its power, or only the fuel?* — i.e. does it work *without* a big model, or is it a layer on top of one? That single question sorts hype from substance faster than any other.
- **Treat the mainstream stack as one thing, not four.** When comparing systems, remember AP1+AP2+AP3+AP4 are layers of one machine. A claim that "agents beat reasoning" or "RL replaced scale" is usually a category mistake — they are parts of the same system.
- **Use the dissents as a weak-spot map, not as horses.** AP5/AP7/AP8/AP9/AP10 each point at a real gap in the mainstream stack (grounding, reliable reasoning, novelty, endless learning, physical meaning). Whether or not their specific fix wins, that is *where to look for trouble* — and where the next real breakthrough is most likely to come from.
- **Watch the two gauges.** *(A **gauge** = a measuring dial you keep an eye on to see which way things are going.)* The novelty gap (are ARC-style scores climbing without task-specific training?) and the data wall (is scaling still buying gains as human text runs out?). These two dials decide whether "scale-plus-ingredients" keeps improving smoothly or stalls. Everything else is detail. *(The data-wall gauge — and the compute and energy ceilings beside it — get their own deep page: [The bounds](../30-across-the-approaches/01_the-bounds-data-compute-energy.md).)*
- **Hold your own confidence in the middle, and say what would move it.** The mark of understanding this map is *not* picking a winner; it is being able to state a position, its two failure modes, and the exact evidence that would change your mind. That is what a research position looks like, and it is the whole point of the project.
- **What you delegate vs what you keep:** hand the *building* to others and to AI (training runs, robot engineering, connectome tracing). **Keep for yourself** the judgement this page teaches — reading the one axis, refusing the two easy stories, knowing which gap could stall the field, and updating your view as the two gauges move. That judgement is the AI-proof part; it is what a research scientist actually does.

---

## Connections

- **Keep only three things:** ① The eleven bets have **one axis** — *is scale the source of intelligence, or only the fuel?* ([the scaling-suffices debate](../20-the-approaches/01_ap1-scale-and-foundation-models.md)). Almost every card ends on this one question, so the map is really one argument, not eleven. ② They form **four families:** the mainstream **stack** (AP1+AP2+AP3+AP4 — four layers of one winning machine), the **second-ingredient dissents** (AP5/AP7/AP8/AP9/AP10 — each names a real gap, but each wins so far only *on top of* a big model), the **data-wall answers** (AP4/AP9/AP10 — the fuel supply once human text runs out), and the **brain bets** (AP6/AP11 — long-horizon insurance). ③ The **viewpoint:** the likely path is **scale plus a stack of ingredients**; scale keeps absorbing its challengers (the Bitter Lesson repeating), *but* two named gaps — **true novelty** and the **data wall** — are real and unclosed, so "scale alone" is unproven; hold your confidence in the middle and watch those two gauges.
- **This page reads last** — it leans on all eleven cards. Down the ladder: [① How AI works today](../10-how-ai-works-today/01_guessing-the-next-word.md) and [the scaling / data-wall page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the shared base every bet is built on.
- **The whole deck it judges:** [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md) · [AP2](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) · [AP3](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) · [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) · [AP5](../20-the-approaches/05_ap5-world-models-jepa.md) · [AP6](../20-the-approaches/06_ap6-brain-based.md) · [AP7](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) · [AP8](../20-the-approaches/08_ap8-program-synthesis-arc.md) · [AP9](../20-the-approaches/09_ap9-open-endedness.md) · [AP10](../20-the-approaches/10_ap10-embodiment.md) · [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md). The full [map / spine is here](../APPROACHES_TO_AGI.md).
- **How sure are we?** That the map has one axis and that the mainstream stack is currently winning — **[Established]**. That the dissents so far win only on top of big models — **[Established, as of July 2026]**. That "scale plus ingredients" is the *right* verdict, and the exact ranking — **[Contested, dated, and revisable]** — which is the honest and intended state of a research position.

## Check yourself *(try one, from memory)*

1. State the **one axis** that runs under all eleven bets, in a single plain sentence using the words *scale* and *enough*.
2. Why is comparing "AP1 versus AP2" called a **category mistake** on this page? What is the right way to see AP1+AP2+AP3+AP4?
3. Name the **four families** and give one bet in each.
4. What is the single most important fact about the "second-ingredient" dissents (AP5/AP7/AP8/AP9/AP10) as of July 2026 — the fact that decides how this page ranks them?
5. The verdict says the path is "scale plus a stack of ingredients." Name the **two gaps** that could still stall it, and which bets name each.
6. Give the **two opposite ways** this viewpoint could be wrong (Break #1 and Break #2), and explain why the honest confidence lands in the middle.

## Revision notes

*Newest first.*
- `rev 1 (2026-07-16)` — created as **The verdict** — the map's capstone and the project's promised **independent viewpoint** ([spine §1](../APPROACHES_TO_AGI.md)), written the day the eleventh approach card completed the deck. It is a **synthesis, not a twelfth bet:** it introduces no new grounded facts, only a judgement drawn across the eleven cards (each already grounded + live-SOTA'd to July 2026). Placed in a new final reading group (**③ The verdict**), reading **after** all eleven approach cards, and leaning on every one of them via short reminder-then-link (no re-teach — DRY [§4.2](../../INSTRUCTIONS/HARD_RULES.md)). Structure: the judgement in one minute → a one-line reminder of the eleven → **Part 1** (the map has one axis — the scaling-suffices debate; shown by the "road or app layer?" doubt recurring in six cards, plus two more on a close cousin) → **Part 2** (the eleven are four families that *combine*: the mainstream stack A, the second-ingredient dissents B, the data-wall answers C, the brain bets D — with the key finding that every dissent's real win so far runs *on top of* a big model) → **Part 3** (a ranked read by "how likely to be *part of the path*," with a full table + the "scale-plus-ingredients" viewpoint) → **Part 4** (the two opposite ways the viewpoint breaks, and why the honest confidence sits in the middle) → honesty box → director's use → connections → check-yourself. Built to the simplest-English + progressive-ladder standard ([HARD_RULES §6.5](../../INSTRUCTIONS/HARD_RULES.md)): every medium-or-hard term glossed (axis, paradigm, category mistake, app layer, crutch, last mile, data wall, family), one new step at a time, no prerequisite used before its card taught it. Numbers reused from the cards are consistent (ARC-AGI-2 ~37.6% vs humans ~60%, late 2025; the data wall from the scaling page). **§7.0 recheck done:** consistency checked against all eleven cards + the spine's heat ratings + the registry; every cross-link verified to point to a live card; §6.5a idiom/flourish sweep; confidence tags on every ranked row and every honesty-box bullet; the viewpoint framed throughout as a *revisable position*, not a fact (matches the spine's "living / revisable" and the user's reward-for-self-critique style).

---
*This is the closing page of the map — the independent viewpoint the whole project was built to reach. It judges, it does not add: the eleven bets it weighs are [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md) through [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md), and the full [map is here](../APPROACHES_TO_AGI.md). The verdict is deliberately unfinished — a research position lives by being argued with and revised as the two gauges (true novelty, the data wall) move. The project's own path continues in reading group ③, the two cross-cutting threads this verdict leaned on but did not open: **[The bounds — data, compute, energy](../30-across-the-approaches/01_the-bounds-data-compute-energy.md)** (✅ written — the physical/economic ceilings behind the data-wall gauge, as a race between efficiency and demand) and **alignment / recursive self-improvement** (still to be written); both are also sketched in the [map's §4](../APPROACHES_TO_AGI.md).*
