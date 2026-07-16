---
id: c-ap6-brain-based
sortkey: 2006
title: AP6 · Brain-based / neuro-grounded — the "copy the one thing that works" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap5-world-models, c-ap8-program-synthesis]
provides: [common-cortical-algorithm, cortical-column, mountcastle-big-idea, reference-frames, thousand-brains-theory, cortical-voting, predictive-brain, four-attributes-of-intelligence, neuromorphic-computing]
resources: []
status: ready
reading_time: 32 min
rev: 1
created: 2026-07-15
updated: 2026-07-15
---

# AP6 · Brain-based / neuro-grounded — the "copy the one thing that works" bet

*This is the sixth big idea we look at for how to build a machine that can think in a general way — and it is the most down-to-earth of them all. Every other approach guesses at intelligence and tries to build it from scratch: copy human text (AP1), think longer (AP2), chase reward (AP4), model the world (AP5), search for programs (AP8). This one asks a simpler question: **why guess?** We already have one working example of general intelligence sitting inside every human skull — the brain. So stop inventing; **reverse-engineer the brain and copy how it actually works.** Not the whole brain (that is a different bet, [AP11](11_ap11-whole-brain-emulation.md)), but the one part that makes us smart and flexible: the **neocortex**. Its champion is Jeff Hawkins, and his central claim is startling — the neocortex is not a bag of a thousand different tricks. It runs **one simple algorithm, copied about 150,000 times.** Find that one algorithm, and you have found the recipe for a general mind. This page explains it all from zero: the bet in one minute, the one-algorithm idea, what the algorithm seems to be, why serious people back it — and the four places it is stuck.*

> **You are here:** this is the **AP6** page — the sixth bet on the "approaches to AGI" map (see [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)), and the sixth one written in full. AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. The short name for this idea is **brain-based** (or *neuro-grounded*): build intelligence by copying the working design in the human brain, rather than inventing one.
>
> **This page builds on earlier rungs of the ladder**, all short and plain: [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) and [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — how today's AI works, and the bet this one doubts; [AP5 · world models / JEPA](05_ap5-world-models-jepa.md) — which AP6 pairs with, because the brain is itself a prediction-and-planning machine; and [AP8 · program synthesis / ARC](08_ap8-program-synthesis-arc.md) — which set the target this page aims at: *flexibility on the truly new.* A one-line reminder of each is given where it is used, so you will not get lost.
>
> **Where the facts come from:** Jeff Hawkins, *A Thousand Brains: A New Theory of Intelligence* (2021) — the fullest plain-spoken statement of this bet, from the founder of the research company Numenta. Quotes from it are exact. The durable root is Vernon Mountcastle's 1978 essay on the neocortex. Fresh check of the field, done on the web (**as of July 2026**): the **Thousand Brains Project** (Numenta's open-source effort, launched November 2024, made an independent nonprofit January 2025) and the state of **neuromorphic** *(brain-style)* computer chips. Each fast-moving fact is dated below.

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**We have exactly one example of a truly general mind: the brain. It learns almost anything, from very little, using about 20 watts of power — a dim light bulb. Every other approach tries to build intelligence by guessing what it is. This bet says the smart move is to copy the working example instead. And the key discovery is what makes it hopeful: the part of the brain that makes us smart — the neocortex, the wrinkled outer sheet — is not a pile of many special-purpose machines. It is *one* simple circuit, repeated about 150,000 times. Seeing, hearing, touching, language, and abstract thought all run on the *same* basic unit, just wired to different inputs. So you do not have to solve intelligence a thousand times over. You have to work out what that one repeated unit does — and then build it. Hawkins' answer to what it does: each unit builds little *models* of the world using map-like frames, and it learns by moving and constantly predicting what it will sense next. Intelligence, on this view, is thousands of such models working together and voting on what is out there.**

Why believe copying the brain is the road? Because it is the only thing we *know* is generally intelligent. Every other bet is a theory about what intelligence might be. The brain is proof of what it *is*. If you want to build a bird, it is at least worth studying the one bird that already flies.

That is the bet. The rest of this page explains **the one-algorithm idea**, **what the algorithm seems to be** (models, frames, prediction, and voting), **why serious people back it**, and **why it might still be wrong.**

---

## First, a one-line reminder of the base

Three quick reminders from the rungs below, so this page stands on its own.

- From [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) and [AP1](01_ap1-scale-and-foundation-models.md): **today's main AI is a text machine** trained to guess the next word in billions of pages of human writing. It works by statistics over huge data — a design that owes almost nothing to how a brain works. Hawkins' whole complaint is that this is why it stays narrow. *(New to you? Read those two rungs first.)*
- From [AP5 · world models](05_ap5-world-models-jepa.md): that approach said intelligence is having a **world model** — an inner copy of how the world changes, used to plan *(short version: predict "if I do this, what happens next?" before acting)*. Hold that idea; AP6 says the brain is *exactly* such a machine, built in biology. AP6 is the world-model bet grounded in the one working brain.
- From [AP8 · program synthesis](08_ap8-program-synthesis-arc.md): Chollet's line that **skill is not intelligence** — real intelligence is handling the genuinely new, flexibly, from little data *(a mind, not a memory)*. AP6 accepts that target completely, and answers it by pointing at the brain, the one system that truly has this flexibility.

Now the one new idea this page adds. AP1 tries to *grow* intelligence from data; AP8 tries to *search* for it; AP5 tries to *learn* a world model from video. AP6 says: **don't design it and don't grow it — copy it.** There is a finished, working blueprint. Read it, understand it, and rebuild it in a machine. Everything below is about what that blueprint says.

---

## Part 1 — Mountcastle's big idea: the brain runs one algorithm

Start with the organ itself. The **neocortex** *(neo = new; cortex = the outer layer — so "the new outer layer of the brain")* is the wrinkled sheet covering the outside of your brain. It is about the size of a large dinner napkin, folded up to fit in the skull, and in humans it makes up about **70 percent** of the brain. It is where seeing, hearing, touching, language, and thinking happen. If there is a seat of general intelligence, this is it. So the whole question, for this bet, is: **what does the neocortex do, and how?**

In 1978, a neuroscientist named Vernon Mountcastle gave an answer so simple that it still splits the field. He noticed that when you cut into the neocortex, *every part looks nearly the same* under the microscope — the slice responsible for vision looks like the slice for touch, which looks like the slice for language. His explanation was radical:

> "Put shortly, there is nothing intrinsically motor about the motor cortex, nor sensory about the sensory cortex. Thus the elucidation of the mode of operation of the local modular circuit anywhere in the neocortex will be of great generalizing significance."
> *(Vernon Mountcastle, 1978, quoted in Hawkins, A Thousand Brains, 2021)*

Unpack that slowly. "Intrinsically" = in its own nature, built-in *(so: there is nothing about the vision area that is *specially* for vision, or about the movement area that is *specially* for movement)*. "The mode of operation of the local modular circuit" = how one small repeated unit works. "Of great generalizing significance" = it would explain the whole thing. In plain words: **every part of the neocortex is running the same basic operation.** What makes the vision area "vision" is not a special vision-circuit — it is just that this patch happens to be wired to the eyes. Wire the same patch to the ears and it does hearing; wire it to other patches and it does language and thought. Hawkins puts the size of the claim in a way that lands:

> "Darwin proposed that the diversity of life is due to one basic algorithm. Mountcastle proposed that the diversity of intelligence is also due to one basic algorithm."
> *(Hawkins, 2021)*

("Algorithm" = a fixed method or recipe a system follows.) This is the heart of AP6. Just as all of life's endless variety runs on **one** recipe (evolution), all of intelligence's variety — vision, music, maths, speech — may run on **one** cortical recipe. The repeated unit that runs it has a name: the **cortical column** *(a tiny vertical unit of brain tissue, about one square millimetre across, running through the full thickness of the sheet)*. A human neocortex is roughly **150,000** of these columns, packed side by side like short strands of spaghetti. Mountcastle's bet: they are all doing the same thing.

### Why this is more than a curiosity

Four pieces of evidence make the one-algorithm idea more than a guess, and each one matters:

1. **The circuits look the same everywhere.** As Hawkins notes, if you found two silicon chips with nearly identical wiring, you would assume they do nearly the same job. The neocortex's detailed wiring is remarkably uniform across regions — the same argument applies.
2. **It grew too fast to invent.** The huge human neocortex appeared in just a few million years of evolution — "probably not enough time for multiple new complex capabilities to be discovered by evolution, but it is plenty of time for evolution to make more copies of the same thing." Copying one working unit is cheap; inventing many new ones is not.
3. **It rewires itself.** In people born blind, the *visual* part of the neocortex gets no useful signal from the eyes — and it quietly takes on new jobs, handling hearing or touch instead. A patch built *only* for vision could not do that. A patch running a general recipe can.
4. **It learns things evolution never prepared it for.** As Hawkins puts it, "our brains did not evolve to program computers or make ice cream — both are recent inventions." That we can learn these at all means the brain cannot be a bag of pre-built skills. It must run "a general-purpose method of learning." This, he says, is the most convincing evidence of all.

Here is why this is the deepest reason to take AP6 seriously. **If intelligence is one algorithm, the problem is finite.** You do not need to solve vision, then language, then reasoning, then planning, each as a separate mystery. You need to crack **one** thing — what a cortical column does — and the rest follows. That is a very different, and far more hopeful, shape of problem than "invent a mind." So — what does a column do?

---

## Part 2 — what the one algorithm seems to be

Hawkins' life work at Numenta is a proposed answer. It has four linked parts. Take them one at a time.

### Piece 1 — the brain stores *models*, not facts

Old-style AI tried to store knowledge as **facts and rules** — "a stapler has a top; pressing the top makes a staple come out" — and it drowned. Every word needed defining, every rule needed a hundred more rules, and the machine still did not *know* what a stapler was. This is the **knowledge-representation problem**, and Hawkins says today's text machines did not solve it either — they "avoided it completely, relying on statistics and lots of data instead." The brain does something wholly different:

> "The brain takes a completely different approach to storing knowledge about a stapler: it learns a model. The model is the embodiment of knowledge."
> *(Hawkins, 2021)*

("Embodiment" = the thing that carries or *is* it, not a description of it.) Picture a tiny working stapler in your head — same shape, same moving parts. To answer "what happens when you press the top?", you do not look up a rule; you *press the little model and watch.* **The knowledge is not a list of facts about staplers; it is a working model of a stapler.** That is how the brain knows anything — a coffee cup, a bicycle, another person: by holding a small, runnable model of it. *(Notice this is exactly [AP5's world model](05_ap5-world-models-jepa.md) — "predict what happens next" — but AP6 says the brain builds a separate little model for every object, not one big model of everything.)*

### Piece 2 — the models live in *reference frames*

How does a lump of brain tissue hold a "model" of a 3-D object? Hawkins' answer is the boldest part of the theory: with **reference frames.** A reference frame is just a **map with a coordinate system** — a way of giving every point a location, like the grid of squares on a paper map that lets you say "the library is at square D4." The brain already has cells that do exactly this for *physical space*, so you can find your way around a room: **grid cells and place cells** *(brain cells that fire to tell you where you are — their discovery won the 2014 Nobel Prize in Medicine)*. Hawkins' leap is that the neocortex uses the *same* map-making machinery for **everything** — not just rooms, but objects (a map of a stapler's parts), your own body, and even **abstract ideas like mathematics.** Knowledge is stored *at locations in these frames.* Thinking, on this view, is *moving through a reference frame* — going from one location to the next and reading off what is stored there. This is why the theory says even abstract thought is, underneath, a kind of navigation.

### Piece 3 — it learns by moving and *predicting*

A column is not a passive picture-taker. It is a **sensory-motor system** *(it both senses and acts — it takes input and moves)*, and it learns through movement:

> "With every movement, a column predicts what its next input will be. Prediction is how a column tests and updates its model."
> *(Hawkins, 2021)*

Read that carefully — it is the engine. As your eyes flick or your finger slides over an object, the column *predicts* what it should sense next, then checks. A correct prediction confirms the model; a wrong one corrects it. This is the **predictive brain** *(the idea that the brain is constantly guessing its own next input and learning from the errors)* — and it is the same prediction-and-planning core as [AP5](05_ap5-world-models-jepa.md), which is why the two bets are cousins. You cannot learn a house without walking through it; you cannot learn a stapler without turning it in your hand. Movement plus prediction is how every model gets built.

### Piece 4 — the "thousand brains": many models, voting

Here is the twist that names the theory. There is **not one model** of the coffee cup in your head. There are **thousands** — one in each column that senses part of it (from your fingertips, from different parts of your vision), each slightly different but complementary. Hawkins:

> "knowledge of any particular item is distributed among thousands of complementary models."
> *(Hawkins, 2021)*

So why do you perceive **one** cup, not a thousand fragments? Because the columns **vote:**

> "columns vote. Your perception is the consensus the columns reach by voting."
> *(Hawkins, 2021)*

("Consensus" = the shared answer everyone agrees on.) Each column casts its guess through long-range connections; the guesses that agree win, and the network settles on one answer — *cup.* This voting is the theory's proposed solution to a classic puzzle (how scattered, distorted inputs from many senses become one clean perception). **This is why it is the "Thousand Brains" theory: intelligence is not one model of the world, but thousands of models, voting.**

Put the four pieces together and you have AP6's proposed recipe: **thousands of columns, each building models of the world in map-like reference frames, learning by moving and predicting, and voting to reach a single perception.** That is what Hawkins bets the one cortical algorithm is.

---

## Part 3 — the blueprint as an engineering spec

The above is neuroscience. AP6's payoff is turning it into a build-list for machines. Hawkins gives **four attributes** he says any truly intelligent machine must have — a minimum baseline for AGI, and a sharp contrast with today's AI, which has almost none of them:

1. **Learning continuously.** We learn every waking moment without erasing what we knew. Today's text machines are trained once, then frozen; teaching them something new means retraining from scratch. The brain avoids this with a neuron trick — a new memory forms new connections on one branch without disturbing the others *(so new learning does not overwrite old — the opposite of today's "catastrophic forgetting," where a network learning a new task wipes out the last one)*.
2. **Learning via movement.** You build a model of anything — a room, an app, even a piece of maths — by *moving through it* and seeing what comes next. Intelligence is active, not a snapshot.
3. **Many models that vote.** Knowledge is spread across thousands of complementary models that vote — which is what makes the system robust and flexible, and easy to wire to any mix of senses.
4. **Reference frames.** Knowledge is stored in general-purpose map-like frames — the backbone that lets a system represent 3-D structure, change, and relationships. Most neural networks have nothing like this; they just attach a label to an input.

This four-part list is AP6's real contribution: not "the brain is amazing," but a concrete claim about *what is missing* from current AI and what a genuine mind-machine must include. Hawkins states the conclusion without hedging:

> "I believe the future of AI will be based on brain principles. Truly intelligent machines, AGI, will learn models of the world using maplike reference frames just like the neocortex … I don't believe there is another way to create truly intelligent machines."
> *(Hawkins, 2021)*

---

## Why this is a serious idea, not one man's hunch

Three legs hold it up.

### Leg 1 — it is the only existence proof of general intelligence

This is the strongest and simplest leg. **The brain is the one thing we know for certain is generally intelligent.** Not a theory of intelligence — the real thing, walking around, learning language and maths and ice-cream-making, on about 20 watts, from far less data than any text machine. Every rival bet (scale, reward, world models, program search) is a *guess* about what intelligence is; some may be right, but none is proven. AP6 starts from the one proven case and says: copy that. When you are trying to build something that has only ever existed in one form, studying that form is not a detour — it is the obvious first step. **[Established — the brain is the only known general intelligence; that copying it is the *best* route is the bet.]**

### Leg 2 — the one-algorithm idea reframes the whole problem

AP6 is not only "look at the brain"; it is a specific, testable claim that changes the *shape* of the problem. If Mountcastle is right that the neocortex is one algorithm copied 150,000 times, then AGI is not a thousand hard problems but **one.** And that single claim is backed by real evidence — the uniform circuitry, the too-fast evolution, the rewiring of blind people's visual cortex, and the flexibility to learn things evolution never prepared us for (Part 1). Even the way the brain measures intelligence lines up with [AP8](08_ap8-program-synthesis-arc.md): Hawkins writes that "intelligence is determined by how a machine learns and stores knowledge about the world … not because we can do one thing particularly well, but because we can learn to do practically anything." That is the same *skill-is-not-intelligence* target, reached from biology. **[Likely — the one-algorithm idea is well-argued and has real evidence, but remains a live scientific hypothesis, not settled fact.]**

### Leg 3 — the bet is now real code and silicon

For decades this was one researcher's mission. As of **2026**, it is a funded, open, growing effort — the clearest sign the field takes it seriously.

- **The Thousand Brains Project.** In **November 2024**, Numenta released an **open-source** software framework that builds AI on these exact principles — sensorimotor learning, columns, reference frames, voting (it comes with a research paper, *"The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence,"* 2024). In **January 2025** it became an independent non-profit, with the patents placed under a free-use pledge, calling for researchers worldwide to build on it. The theory has left the page and become working code anyone can run and extend *(as of 2026)*. **[Established / dated — the project and its open-source release are real; whether it scales to general intelligence is unproven.]**
- **Brain-style chips (neuromorphic computing).** Separately, engineers are building **neuromorphic** hardware — chips wired to work more like a brain, with many small units that compute only when they "spike," instead of one big processor grinding through everything *(neuromorphic = shaped like the nervous system)*. Intel's **Loihi 2** and IBM's **NorthPole** are the leaders; vendors report very large energy savings — on the order of **tens to a thousand times** less power than a normal AI chip for certain tasks *(as of 2026; these are reported figures, and the honest caveat is in Stuck #3)*. If intelligence really is brain-shaped, brain-shaped hardware could run it far more cheaply than today's power-hungry chips. **[Likely / dated — the efficiency gains are real for narrow tasks; general use is not yet here.]**

---

## So what does AP6 say intelligence is?

Pulling the legs together, here is AP6's answer to *"what is intelligence?"*:

- **Intelligence is** what the **neocortex** does: a system of **thousands of models** of the world, each built in a map-like **reference frame**, learned by **moving and predicting**, and **voting** to a single perception. Not fluent talk (AP1), not reward-chasing (AP4) — a model-building, sensorimotor machine.
- **How it is built** is by **copying** the one working design, not designing a new one or growing it from data.
- **Its claim about the missing piece:** today's AI fails to be general because **it is not built like the one thing that works.** It has no continuous learning, no movement, no many-models voting, and — most of all — no reference frames. Add the brain's four attributes, AP6 says, and you cross from narrow skill to a real, flexible mind.

That is the bet. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP6 stands on the one undeniable fact in the whole field — the brain exists and is generally intelligent — and it offers a specific, evidence-backed theory (one algorithm; models in reference frames; voting) plus a concrete build-list. Hold that. Now the four places it is truly stuck.

### Stuck #1 — we don't actually know the algorithm yet

This is the honest heart of it. AP6's plan is "copy the cortical algorithm" — but **nobody has the algorithm.** Mountcastle proposed that one exists and where it lives, but, in Hawkins' own words, Mountcastle "didn't know what the cortical algorithm was." Hawkins' Thousand Brains Theory is a *proposal* for it, and even he is careful to say how much is missing: "the number of things we don't understand about the brain in general, and the neocortex in particular, is large." And the founding idea is still contested — Mountcastle's one-algorithm claim, Hawkins notes, "continues to polarize the neuroscience community." **You cannot reverse-engineer what has not yet been reverse-engineered.** AP6's whole promise rests on a theory of the cortical column that is unfinished and disputed. **[Contested — the central open problem; the algorithm is a hypothesis, not a known quantity.]**

### Stuck #2 — how much of the biology is the algorithm, and how much is just biology?

Suppose we did understand the brain. A hard question remains: **which parts do you copy?** The brain is a messy, wet, 20-watt tangle of chemistry, evolved under constraints a machine does not share — it must be built from cells, run on sugar, and fit through a birth canal. Some of its design is the *real algorithm of intelligence*; some is just biology's workaround for being made of meat. Copy too little and you miss the magic; copy too much and you drown in irrelevant detail. The classic warning is flight: **airplanes do not flap their wings.** The Wright brothers succeeded by taking the *principle* of a wing (lift) and dropping the *biology* (feathers, flapping). Brain-based AI needs the same move — extract the principle, skip the meat — but **nobody yet knows which parts of the brain are the principle and which are the feathers.** Guess wrong and you either fail or waste decades simulating detail that never mattered. **[Contested — a deep, unsolved judgement call at the core of the approach.]**

### Stuck #3 — the approach that ignores the brain is winning the race

Here is the hardest fact for this bet. AP6 says you cannot get real intelligence without brain principles — yet the approaches that **ignore** the brain have produced the most capable AI in history. Today's text machines ([AP1](01_ap1-scale-and-foundation-models.md)) break almost every one of Hawkins' four rules — they are frozen after training, they do not move, they have no reference frames — and by his theory they *should not* be intelligent. And in a narrow sense he is right: they still fail at true novelty ([AP8](08_ap8-program-synthesis-arc.md)). But they are also astonishingly useful, and no brain-based system is remotely as capable. The uncomfortable truth as of 2026: **the "wrong" approach is years ahead of the "right" one.** This feeds the sharpest doubt — maybe you *don't* need to copy the brain, just as planes did not need feathers. Even the brain-style hardware is a caution here: neuromorphic chips are impressive on narrow tasks but, as of 2026, **no production, general-purpose neuromorphic product has shipped** — the software and the demand to justify them lag far behind the hardware. **[Contested — the strongest evidence against AP6 is the success of everything that ignores it.]**

### Stuck #4 — it is a multi-decade bet, and it may arrive too late

Even granting the theory, AP6 is **slow.** The Thousand Brains Project (Leg 3) can learn models of individual objects — genuinely interesting as neuroscience, but tiny next to what a text machine does today. Reverse-engineering the neocortex, then turning that into a scalable machine, is plausibly a **multi-decade** project with no guarantee the payoff arrives before some other approach reaches AGI first. A bet can be *correct in principle* and still *lose the race* — if scale, or reasoning, or world models get there in five years, "the brain was the right blueprint all along" becomes a footnote, not a victory. AP6's deepest risk is not being wrong; it is being right too late. **[Likely — the timeline gap between brain-based AI and the frontier is real and large as of 2026.]**

### The big question under all of these

Every doubt above is one question: **is the brain the *necessary blueprint* for intelligence, or just *one way* evolution happened to build it — a way we need not copy, any more than planes copy birds?** AP6 bets it is the blueprint: the brain is the only proof that general intelligence is possible at all, so the surest route is to understand and rebuild it. The critics answer that scale is *already flying without feathers* — narrow still, but flying — and that we may reach a mind by a route evolution never took. And note the twist that ties AP6 to its siblings: Hawkins' brain is a **prediction machine that builds models of the world**, which is exactly [AP5](05_ap5-world-models-jepa.md)'s bet in biology; it is what [AP1](01_ap1-scale-and-foundation-models.md)'s text machines most plainly lack; and its built-in reference-frame machinery is a candidate answer to [AP8](08_ap8-program-synthesis-arc.md)'s open question — *where do broad priors come from?* So the live 2026 question is whether brain-based AI is **the true road to AGI that the others are only approximating**, or **a beautiful, correct, and too-slow science project** that the frontier will overtake. *As of July 2026, this is genuinely open.* **[Contested — the key open question.]**

---

## ⚠️ Honesty box

- **"The brain is the only proof" is strong; "so copy it" is a bet.** That the brain is the one known general intelligence is a fact. That copying it is the *best or only* route to machine AGI is a wager — and the current evidence (Stuck #3) is that approaches ignoring the brain are far ahead. Keep the fact apart from the bet. **[Contested.]**
- **The core theory is unproven and disputed.** The one-algorithm idea and the Thousand Brains Theory are serious, evidence-backed *hypotheses*, not settled neuroscience (Stuck #1). Hawkins himself stresses how much of the brain we still do not understand. Treat the theory as promising and open, not established. **[Contested.]**
- **Planes don't flap.** The deepest unanswered question is *how much* biology is essential versus incidental (Stuck #2). "Copy the brain" only works if you copy the right layer of abstraction — and nobody yet knows which layer that is. **[Contested.]**
- **Being right is not the same as winning.** AP6 could be correct that intelligence is brain-shaped and still lose the race to a faster approach (Stuck #4). A correct-but-too-slow bet still misses AGI. **[Likely.]**
- **Numbers and names age fast.** The Thousand Brains Project's launch, the neuromorphic chips (Loihi 2, NorthPole), the reported energy figures — these are 2021–2026 snapshots, and some efficiency numbers come from the vendors themselves. The lasting parts are the **one-algorithm idea** (Mountcastle), the proposed **mechanism** (models in reference frames, learned by movement and prediction, voting), the **four attributes** an intelligent machine needs, and the **four cracks.** The products around them will change.

---

## How to use this (if you want to direct AI work)

- **First question about any "brain-inspired" claim: which brain principle, at which level?** "Inspired by the brain" is nearly meaningless on its own — today's neural networks are "brain-inspired" and share almost nothing with a real cortex. Ask *what specific principle* (continuous learning? reference frames? prediction-by-movement?) and *at what level* (the wet biology, or the abstract algorithm?). Most of the confusion, and most of the hype, lives in that gap (Stuck #2).
- **Use Hawkins' four attributes as a checklist.** Continuous learning, learning via movement, many models voting, reference frames. When judging whether a system is on a path to *general* intelligence rather than narrow skill, ask which of the four it actually has. Today's frontier AI has close to none — which is exactly why it is powerful yet brittle.
- **Separate "the brain proves it's possible" from "the brain shows us how."** The first is solid and worth remembering when someone claims AGI is impossible. The second is the open bet. Do not let the certainty of the first create false confidence about the second.
- **Watch the race, not just the theory.** AP6 may be right in principle and still be overtaken (Stuck #4). When allocating attention or money, weigh not only "is this the correct account of intelligence?" but "will it deliver before the alternatives?" A correct theory that ships in 2050 loses to a rough one that ships in 2030.
- **Take reference frames seriously even outside AP6.** The single most portable idea here is that a general mind needs *general-purpose, map-like structure* for representing the world — objects, space, and abstract relations. Whether or not the full brain theory holds, "does this system have a way to represent structure and location, or does it only attach labels?" is a sharp question to ask of any AI.
- **What you hand to others:** simulating columns, building the neuromorphic chip, running the framework. **What you keep for yourself:** judging which brain principles are load-carrying versus incidental, refusing to accept "brain-inspired" as an argument, and weighing correctness against the clock.

---

## Connections

- **Keep only three things:** ① AP6 = **copy the one working example of general intelligence — the brain**, specifically the **neocortex.** Its key discovery (Mountcastle): the neocortex is **one algorithm, copied ~150,000 times** (the *cortical column*) — so AGI is one problem, not a thousand. ② Hawkins' proposed algorithm: each column builds little **models** of the world in map-like **reference frames**, learns by **moving and predicting** its next input, and thousands of these models **vote** to one perception (the *Thousand Brains Theory*); a real machine needs four attributes — **continuous learning, learning via movement, many models voting, reference frames.** ③ It is stuck on four cracks: **we don't know the algorithm yet**, **which biology to copy is unknown** (planes don't flap), **the brain-ignoring approaches are winning the race**, and **it may be right but too slow.**
- **Down the ladder (already read):** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — the text machine AP6 says is built nothing like a mind.
- **Its siblings:** [AP5 · world models / JEPA](05_ap5-world-models-jepa.md) is AP6's closest cousin — the brain *is* a prediction-and-planning world model, built in biology; [AP1 · scale](01_ap1-scale-and-foundation-models.md) is the rival whose success (Stuck #3) is the strongest case *against* needing the brain; [AP8 · program synthesis](08_ap8-program-synthesis-arc.md) sets the target (skill ≠ intelligence, flexibility on novelty) that AP6 answers from biology, and AP6's reference frames are a candidate answer to AP8's "where do priors come from?"
- **The ideas it leads to:** now written — [AP10 · embodiment](10_ap10-embodiment.md) (the brain's "learning via movement" needs a body — AP10 is its deep home) and [AP11 · whole-brain emulation](11_ap11-whole-brain-emulation.md) (copy the brain *neuron by neuron* instead of extracting its algorithm — the more literal, more extreme cousin, and AP6's **opposite twin**: understand the algorithm vs copy everything and understand nothing); and the cross-cutting [alignment & self-improvement](../30-across-the-approaches/02_alignment-control-and-self-improvement.md) page (the risk axis across all bets). See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** That the brain is the one known general intelligence, and Mountcastle's evidence — **[Established / Likely]**. That the Thousand Brains Theory *is* the cortical algorithm, that copying the brain is the best route to AGI, that it will get there in time — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP6 bet in one plain sentence, using the words *brain*, *copy*, and *neocortex*.
2. What is **Mountcastle's big idea**, and why does it make AGI feel like *one* problem instead of a thousand? (Use the Darwin comparison.)
3. Explain how the brain stores knowledge as a **model** rather than facts and rules. (Use the tiny-stapler picture.)
4. What is a **reference frame**, and what is surprising about Hawkins' claim that the brain uses the *same* kind of frame for a coffee cup and for mathematics?
5. Name Hawkins' **four attributes** of an intelligent machine. Which one is about *catastrophic forgetting*?
6. Give the "**planes don't flap**" objection in your own words. Why is "how much biology to copy?" such a hard question? (Stuck #2.)

## Revision notes

*Newest first.*
- `rev 1 (2026-07-15)` — created as the **AP6** deep-dive, the sixth approach card written (badge = AP index; the `03`/`07` slots stay open for the still-unwritten AP3/AP7). Built to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)). Placed as a new rung that **builds on** [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md), [AP1](01_ap1-scale-and-foundation-models.md), [AP5](05_ap5-world-models-jepa.md) (the predictive/world-model cousin), and [AP8](08_ap8-program-synthesis-arc.md) (the skill-vs-intelligence target) with short reminders-and-links — no re-teach. Grounded verbatim in Jeff Hawkins, *A Thousand Brains* (2021): Mountcastle's "nothing intrinsically motor about the motor cortex" and the Darwin/one-algorithm parallel; the four evidence lines; the model-not-rules account of knowledge; reference frames (grid/place cells); "with every movement, a column predicts what its next input will be"; the thousand-brains "columns vote" mechanism; the four attributes of an intelligent machine; "I don't believe there is another way to create truly intelligent machines"; and the honest "we are far from that" / "continues to polarize." Full live-web freshness pass (July 2026): the **Thousand Brains Project** (Numenta's open-source framework, Nov 2024; independent nonprofit Jan 2025; the 2024 paper) and **neuromorphic** hardware (Intel Loihi 2, IBM NorthPole, reported energy figures) — each dated and source-graded, with the vendor-number and "no production product shipped" cautions surfaced in the honesty box and Stuck #3.

---
*This is the sixth approach page written. Its closest cousin is [AP5 · world models / JEPA](05_ap5-world-models-jepa.md) (the brain as a biological world model); its sharpest rival is [AP1 · scale](01_ap1-scale-and-foundation-models.md) (whose success is the case against needing the brain). The ideas it leads to are on the [map](../APPROACHES_TO_AGI.md). To see the target it aims at — flexibility on the truly new — read [AP8 · program synthesis / ARC](08_ap8-program-synthesis-arc.md).*
