---
id: c-bounds
sortkey: 3001
title: The bounds — the walls scaling runs into: data, compute, energy
domains: [frontier, approaches-to-agi, cross-cutting]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-verdict]
provides: [the-three-bounds, the-data-stock-ceiling, the-compute-trend, the-cost-wall, moores-law-slowdown, the-energy-wall, the-landauer-limit, algorithmic-efficiency, jevons-paradox, economic-not-physics-walls]
resources: []
status: ready
reading_time: 30 min
rev: 1
created: 2026-07-16
updated: 2026-07-16
---

# The bounds — the walls scaling runs into: data, compute, energy

*You have read the eleven bets and the verdict that judged them. This is the first of two pages that run **across** all of them — not a new bet, but a fact that every scale-based bet has to live with. The mainstream bet on this map is "make it bigger" ([AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md)). But "bigger" is not free. To make a model bigger you need three real, physical things in ever-larger amounts: **text to train on** (data), **computer power to train with** (compute), and **electricity to run the machines** (energy). Each of these has a ceiling. This page walks through all three ceilings — how close each one is, what happens when you hit it, and the honest question at the end: are these ceilings **hard walls that stop scale**, or **soft walls that keep moving back** as we get cleverer? This is the physical, arithmetic side of the whole "is scale enough?" argument — the side made of tokens, chips, and watts, not opinions. It explains everything from zero: the three walls in one minute, each wall in turn, why they might not bind after all, and what all of it means for the map you just read.*

> **You are here:** this is **The bounds** — the first page in reading group **③ Across the approaches** (see the map, [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)). AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. A **bound** here means *a limit — a ceiling you cannot go past* (like a speed limit, but set by physics and supply, not by law). This page is not a bet; it is the set of ceilings **every** bet has to respect.
>
> **This page builds on rungs you have already climbed**, each with a short plain reminder where it is used, so you will not get lost: [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the steady line "make it bigger" rides, and the fact that good text is finite; [AP1 · the "make it bigger" bet](../20-the-approaches/01_ap1-scale-and-foundation-models.md) — the mainstream bet these walls press on; and [The verdict](../40-the-verdict/01_which-bets-get-to-agi.md) — which named the **data wall** as one of its two "gauges" (the two dials that decide whether scale keeps improving). **This page is the deep home for the three bounds: the data stock, the compute trend and its cost, and the energy wall.**
>
> **Where the facts come from:** the durable ideas are grounded in real sources — Sevilla et al.'s *"Compute Trends Across Three Eras of Machine Learning"* (2022) for the compute history, David MacKay's *"Sustainable Energy — without the hot air"* (2008) for the way to reason about energy, Dario Amodei (2024) and the "will scaling work?" debate for the data question, and Rolf Landauer's 1961 physical limit. A live web check of the field (**as of July 2026**) supplies the current numbers — the size of the text stock, the price of a frontier training run, data-centre electricity use, and the newest power deals. Every fast-moving number below is dated, because it will age.

---

## The three bounds in one minute

Here is the whole page, as short as it goes.

**Making an AI model bigger burns three limited resources, and each one is running toward a ceiling.**

1. **Data — the fuel.** A model learns by reading text. Good human text is a **one-time supply**, and the biggest models have nearly read all of it. Best estimate: the useful pile runs out around **2028**.
2. **Compute — the engine.** Training a frontier model has needed **more and more** computer power, doubling every few months for over a decade — far faster than chips themselves get better or cheaper. That gap is paid for in money, and the price of a single training run is climbing toward **billions of dollars**.
3. **Energy — the power.** All that computer power runs on electricity. AI data-centres already use as much power as a mid-sized country, and their demand is set to **double by 2030** — fast enough that companies are buying whole nuclear power stations just to run them.

None of the three is a wall built by physics that says "scale is impossible." (The one true physics floor, the **Landauer limit**, is astronomically far below where we are.) They are **economic and supply walls**: you run out of *cheap text*, *affordable chips*, and *available electricity* long before you run out of what physics allows. So the real question this page ends on is not "can scale go on forever?" but "**does the money-and-electricity ceiling arrive before scale reaches AGI — or do we keep getting clever enough to push the ceiling back?**" That question sits directly under the whole [scaling-suffices debate](../20-the-approaches/01_ap1-scale-and-foundation-models.md).

That is the shape. Now each wall in turn.

---

## First, a one-line reminder of the base

Four quick reminders from pages you have already read, so this page stands on its own.

- From [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): **making a model bigger makes its mistakes fall in a steady, predictable line.** "Bigger" means three dials turned up together — **size** (the count of adjustable inner numbers, called *parameters*), **data** (how much text it reads, counted in *tokens* — a token is a chunk of text about the size of a short word), and **compute** (how much number-crunching the training does, measured in *FLOPs* — the count of tiny arithmetic steps). Those three dials are exactly the three walls this page is about. *(New to this? Read that rung first; it is short.)*
- Also from [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): the **data wall** — good human text is a **limited pile** ("we have but one internet"), and the field is already turning to other tricks because the pile is running low. That page owns the *idea* of the data wall and the tricks (machine-made text, extra polishing, thinking longer at answer-time). This page adds the part that page did not: the **actual size of the pile and when it empties.**
- From [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md): the **"make it bigger" bet** stands on that steady line, backed by the **Bitter Lesson** *(Sutton's finding that, across AI's whole history, methods that just use more computer power keep beating methods that build in clever human knowledge by hand)*. These walls are the physical price of that bet.
- From [The verdict](../40-the-verdict/01_which-bets-get-to-agi.md): the whole map turns on one question — **is scale the *source* of intelligence, or only the *fuel*?** — and it named two "gauges" to watch. One of them was the data wall. This page opens up that gauge, and two more beside it.

Now the one new idea this page adds. All three dials — data, compute, energy — cost **real, limited things** that grow harder to get the more you demand. The steady line from the scaling page assumes you can *keep turning the dials*. This page asks the blunt physical question that assumption hides: **how far can each dial actually turn before you run out of the thing it costs?** Everything below is that question, answered one dial at a time.

---

## Wall 1 — the data wall: running out of fuel

Start with the fuel, because it is the wall arriving first.

You already met the data wall on the [scaling page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): good human text is finite, and the biggest models have read most of it. That page gave you the *idea*. Here is the missing part — the **numbers** — because a wall you can measure is a very different thing from a worry.

### How much text is left, and when it runs out

A research group called **Epoch AI** *(an organisation that measures trends in AI — how fast compute, data, and model size are growing)* did the arithmetic. Their estimate, **as of 2024**: the total useful pile of human-written public text — quality-checked and counting for sensible re-reading — is about **300 trillion tokens** *(300 million million word-chunks)*. That sounds enormous, and it is. But the models are eating it fast. Epoch's projection: if training keeps growing the way it has, the frontier will have **used up the good text stock around 2028**, with an honest range of **2026 to 2032**. **[Likely — a measured projection, but it depends on trends continuing; SOTA as of 2026-07.]**

Two details make this sharper, and honest:

- The date **moved.** Epoch's *first* estimate (2022) said the good text would run out around **2024.** It did not — because the field found ways to squeeze more out of the web (careful filtering turned "low-quality" pages into usable data, roughly a five-fold increase in the estimate) and because a model can safely re-read the same text a few times. So the wall got **pushed back** by cleverness. Hold that fact — it is the whole theme of this page's ending.
- The people building the models split on how much this matters. **Dario Amodei** (head of the AI lab Anthropic) named this worry directly:

> "one that's popular today, and I think could be a limit that we run into ... is we simply run out of data. There's only so much data on the internet, and there's issues with the quality of the data."
> *(Dario Amodei, Lex Fridman Podcast, 2024)*

He went on to say he would **bet against** this being the wall that stops progress — because, he argued, machine-made text and reasoning models will fill the gap. The doubters reply that no one has yet *proven* machine-made text can replace the real thing at the needed scale. That argument is not settled. **[Contested — whether the data wall truly stops scaling is a live disagreement, as of 2026-07.]**

### Why running out of text hits scale so hard

Recall the **Chinchilla rule** from the [scaling page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) *(short reminder: for the best result at a set compute budget, you must grow the amount of text along with the model's size — double the size, double the text)*. This rule is why the data wall is not a small problem. The steady line **needs** more text every time the model grows. So when the text runs out, you cannot simply keep turning the size dial — the two dials are chained together. Running out of fuel does not just slow the engine; it **unchains the whole scaling recipe.**

That is why three of the bets on the map are really answers to *this exact wall.* The [verdict](../40-the-verdict/01_which-bets-get-to-agi.md) called them the **data-wall answers** *(short reminder: the three bets that supply new training experience once human text runs out)*: [AP4 · reward](../20-the-approaches/04_ap4-rl-from-interaction.md) (learn from your own checkable successes, not from our text), [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md) (invent an endless stream of your own new challenges), and [AP10 · embodiment](../20-the-approaches/10_ap10-embodiment.md) (get fresh data from a body sensing and acting in the world). Seen this way, those are not rivals to scale — they are the **new fuel lines** that let scale keep running once the human-text tank runs dry.

**The lasting point:** the fuel is a **one-time supply**, measured and running low, and the whole scaling recipe is chained to it. Whether cleverness (machine-made text, learning from experience) refills the tank fast enough is one of the two big open questions on the map.

---

## Wall 2 — the compute wall: the rising price of the engine

Now the engine. This wall is not that we run *out* of computer power — you can always build more machines. It is that each step up has cost **far more** than the last, faster than chips get cheaper. So the wall here is made of **money.**

### How fast the compute has grown

The steadiest fact in modern AI is not about intelligence — it is about how much computer power a top model's training has eaten. The team that measured it (Sevilla and colleagues, 2022) found the growth splits into clear eras:

> "before 2010 training compute grew in line with Moore's law, doubling roughly every 20 months. Since the advent of Deep Learning in the early 2010s, the scaling of training compute has accelerated, doubling approximately every 6 months."
> *(Sevilla et al., "Compute Trends Across Three Eras of Machine Learning," 2022)*

Unpack it slowly. **"Moore's law"** is the decades-old pattern that computer chips get about **twice as powerful every two years** *(named after Gordon Moore, who noticed it in 1965)* — that is how fast the *hardware itself* improves. The finding above is startling because since about 2010, the compute poured into training top AI models has doubled **every six months** — roughly **four times faster** than the chips underneath are improving. **[Established — one of the most-checked trends in AI.]**

Think about what that gap means. If your hunger for compute doubles every 6 months but the chips only get twice as good every 24 months, then **most** of your extra compute is not coming from better chips. It is coming from **buying and running far more of them** — bigger and bigger farms of machines. And more machines means more money, and more electricity (which is Wall 3).

### The price of a single training run

So the compute wall shows up as a **price tag**, and the tag is climbing fast. A live check of the field (**as of 2026-07**):

- The most expensive *publicly known* training runs a few years ago were in the tens of millions of dollars — OpenAI's **GPT-4** is estimated at roughly **$40–100 million**, Google's **Gemini Ultra** around **$190 million.**
- Frontier training runs in **2026** are estimated at **$200–500 million** each, and the amortised cost *(the total hardware-and-energy cost of the final training run, spread out fairly)* has been rising about **2.4× per year** since 2016.
- On that curve, the first **billion-dollar** single training run is expected around **2027**, heading toward several billion after that.

**[Likely — cost estimates are uncertain and companies rarely confirm them; SOTA as of 2026-07.]** The direction is not in doubt even if the exact figures are: each generation of frontier model costs **several times more** than the one before.

### Is the money wall close, or far?

Here the honest picture has **two sides**, and a careful reader holds both.

**The wall is far (the optimist).** The writer Dwarkesh Patel laid out the room still left to grow. His argument, made durable:

> "We can afford a further 10,000x scaleup of GPT-4 (i.e. something GPT-6 level) before we touch even one percent of world GDP."
> *(Dwarkesh Patel, "Will scaling work?", 2023)*

*(GDP = a country's or the world's total yearly economic output — all the money made in a year. "1% of world GDP" is a genuinely huge sum, on the order of a trillion dollars.)* His point: today's spending is still a tiny slice of what humanity *could* spend, so if scale keeps paying off, there is a lot of headroom before cost alone stops it. Governments and companies are already announcing data-centre projects measured in **hundreds of billions of dollars** to chase exactly this.

**The wall is close (the pessimist).** But 1% of world GDP is not a soft limit you drift past — it is a genuine ceiling, and long before you reach it, two other things get in the way. First, spending several billion dollars on a *single* training run that *might* not work is a bet few organisations can make, so the number of players shrinks. Second — and this is the crucial link — **all that compute has to be plugged in somewhere.** Which is Wall 3.

**The lasting point:** compute for training has grown far faster than chips improve, so scale is bought mostly with **money and machines**, not free hardware progress. There is real headroom in dollars — but it runs straight into the electricity wall.

---

## Wall 3 — the energy wall: the power the machines run on

The third wall is the one turning most concrete right now, because you cannot argue with a power grid. Every chip in every training run and every answer draws electricity. When the machines number in the millions, the electricity becomes a national-scale problem.

### How to think about energy: numbers, not adjectives

Before the figures, borrow the right *method* — from the physicist David MacKay, who wrote the clearest book on energy, *"Sustainable Energy — without the hot air"* (2008). His whole approach was one rule:

> "To make this comparison, we need numbers, not adjectives."
> *(David MacKay, "Sustainable Energy — without the hot air," 2008)*

His point: energy arguments are full of vague words — "huge," "green," "tiny" — that let people believe whatever they want. The only way to see straight is to put **actual numbers** side by side and see if they **add up.** *(This is a durable habit, not a fast-moving fact: whenever someone says AI's energy use is "nothing to worry about" or "about to boil the planet," ask for the number, and compare it to something real.)* So let us do exactly that for AI.

### The numbers (as of 2026-07)

The clearest count comes from the **International Energy Agency (IEA)** *(the main world body that measures energy use)*:

- In **2024**, the world's data-centres used about **415 terawatt-hours** of electricity — roughly **1.5%** of all the electricity humanity uses. *(A **terawatt-hour**, TWh, is a unit of energy: one billion kilowatt-hours. 415 TWh is about as much electricity as a country the size of Sweden or Poland uses in a year.)*
- By **2030**, the IEA projects data-centre electricity use will **more than double, to about 945 TWh** — just under **3%** of world electricity. The AI part is the fastest-growing piece, rising about **30% a year.**
- To make it concrete: by 2030, the electricity used just for data-processing in the **United States alone** is projected to be **more than** the combined electricity used by American steel, cement, and chemical factories.

**[Likely — a leading projection, sensitive to how fast AI grows; SOTA as of 2026-07.]** The lasting fact is the *shape*: a demand that doubles in a few years is unusual for electricity, where most sectors grow slowly.

### Why this is now a hard, physical bottleneck

Electricity is not like money — you cannot conjure a gigawatt overnight. Power plants and grid lines take **years** to build. So AI's power hunger has run into the slow, physical world, and the companies' response shows how seriously they take it. A live check (**2026-07**):

- **Microsoft** signed a 20-year deal to **restart the Three Mile Island nuclear plant** in Pennsylvania (about **835 megawatts**, targeted for 2028) purely to power its data-centres. *(A **megawatt**, MW, is a million watts, a measure of power — the rate of using energy; **1,000 MW = 1 gigawatt, GW**, about the output of one large power station.)*
- **Meta** signed nuclear deals adding up to several gigawatts; **Amazon** is putting over **$20 billion** into a nuclear-powered data-centre campus and backing new small reactors; **Google** signed the first corporate deal for a fleet of **small modular reactors** *(smaller, factory-built nuclear reactors)*.

When the largest technology companies on earth start **buying nuclear power stations** to run their AI, the energy wall has stopped being a worry and become a line item. **[Established — the power deals are real and public.]**

### The ultimate floor — and why it is very far away

Is there a *physics* limit to computing energy, the way there is a speed of light? Yes — and it matters that it is **astronomically far below** where we are, because it tells us the energy wall is a *building* problem, not an *impossible* one.

The floor is the **Landauer limit** *(named after Rolf Landauer, who found it in 1961)*. It says: every time a computer **erases one bit** of information *(a bit = the smallest unit of information, a single yes/no)*, it **must** release at least a tiny fixed amount of heat — you cannot compute for free. The amount, at room temperature, is about **0.000000000000000000003 joules** per bit *(a joule is a small unit of energy — roughly the energy to lift an apple a metre; this is a millionth of a millionth of a millionth of that, and then a thousand times smaller again)*. The formula is **E ≥ kT ln2** *(k is a fixed constant of nature, T is the temperature, ln2 is a fixed small number — you do not need the algebra, only the idea: erasing information costs a fixed minimum of heat)*.

Here is the striking part: today's computers use about **a billion times more** energy per operation than this floor. **[Established physics; the "billion times" gap is the current engineering reality.]** That matters in two opposite ways, and both do:

- **The good news for scale:** we are nowhere near the physics limit. There is, in principle, room for computers to become far, far more energy-efficient. So energy is not a wall physics built; it is a wall of **power plants and grid lines** — a building-and-money problem.
- **The reminder from biology:** the human brain runs a full general intelligence on about **20 watts** *(a dim light-bulb's worth — a fact you met in [AP6](../20-the-approaches/06_ap6-brain-based.md) and [AP11](../20-the-approaches/11_ap11-whole-brain-emulation.md))*. A single AI data-centre doing far less general thinking draws **millions of watts.** The gap between 20 watts and a nuclear power station is the clearest sign that today's way of building intelligence is enormously **wasteful** compared to what is possible. That gap is exactly why the brain-based bets ([AP6](../20-the-approaches/06_ap6-brain-based.md)) and **neuromorphic chips** *(chips built to compute more like a brain, aiming for a fraction of the energy)* get attention: not because they are more capable today (they are not), but because they point at where the wasted billion-fold could be won back.

**The lasting point:** energy is the most concrete wall — real grid limits, arriving now, met by buying power stations. But it is a wall of **infrastructure**, not of physics: the true floor (Landauer) is a billion-fold below us, and the brain proves intelligence can run on a light-bulb's power. The wall is real *and* there is huge room to make computing more efficient.

---

## Do the walls actually bind? The honest counter-argument

*(To **bind** here means for a limit to actually take effect — to really stop you, not just exist in theory. A speed limit "binds" when you are pushing against it; if you are driving slowly, it does not.)*

Lay the three walls in a row — text running out around 2028, training runs heading past a billion dollars, electricity demand doubling by 2030 — and it is tempting to conclude "scale is about to stop." That would be too quick. There is a strong counter-argument, and an honest page has to give it full weight. It has two parts.

### Part 1 — the walls keep moving back (algorithmic efficiency)

The single most important fact against a hard wall is that **we keep learning to do the same job with less.** Epoch AI measured this for language models: the amount of computer power needed to reach a **fixed** level of skill has **halved about every 8 months** (with an honest range of 5 to 14 months). **[Likely — a measured trend over 2012–2023; SOTA as of 2026-07.]**

Read that against Moore's law (chips double every ~24 months). **Better methods** — smarter model designs, better training recipes — have been improving *faster* than the chips themselves. So every wall in this page is being pushed back from the other side: you need less text (better data use), less compute (better methods), and less energy (better chips and designs) to reach any given ability than you did a year ago. A wall that recedes as you walk toward it is a very different thing from a brick wall. This is the same pattern you saw with the data wall: the "run out by 2024" estimate became "run out by 2028" because people got cleverer. The walls are **soft**, not hard.

### Part 2 — but efficiency does not shrink the total (Jevons paradox)

There is a catch, and it is important, because it explains why the energy numbers are *exploding* even as chips get more efficient. It is an old idea called the **Jevons paradox** *(named after the economist William Jevons, who noticed in 1865 that when steam engines became more efficient with coal, Britain burned* more *coal, not less)*. The logic: when something gets cheaper to do, people do **far more** of it — enough that the total goes **up**, not down.

The same thing is happening with AI. Each AI answer keeps getting cheaper to compute — but we are asking for **so many more** answers (and letting models think for longer per answer) that total compute and total energy keep climbing steeply. **So efficiency does not save us from the walls; it changes their shape.** Cheaper-per-use plus far-more-use means the *total* bill — in chips, dollars, and watts — keeps rising even as each unit gets more efficient. The wall moves back, and we move toward it faster.

### The synthesis: economic and supply walls, not physics walls

Put both parts together and here is the honest verdict on the bounds:

**None of the three walls is a hard limit set by physics.** There is far more text-like signal to be found (from experience, from other senses), the money headroom is large, and the true energy floor is a billion-fold below us. What the walls *really* are is **economic and infrastructure limits**: you run out of **cheap** text, **affordable** chips, and **available** electricity long before you run out of what nature allows. And those limits are being pushed back steadily by cleverness (Part 1) while being pushed forward by exploding demand (Part 2).

So the real question — the one this whole page has been circling — is a **race**, not a wall:

> **Does the money-and-electricity ceiling arrive before scale reaches AGI, or does efficiency keep pushing the ceiling back faster than demand pushes into it?**

Nobody knows. But notice what this does to the map's central argument. The [scaling-suffices debate](../20-the-approaches/01_ap1-scale-and-foundation-models.md) asked *"is scale enough, in principle?"* The bounds add a second, colder question underneath it: *"even if scale would be enough in principle, can we afford — in tokens, chips, and watts — to run it far enough to find out?"* A bet can be right about intelligence and still lose to arithmetic.

---

## What the bounds mean for the map

Pull it together, and the three walls connect back to several pages you have already read. This is the payoff — the bounds are not a side-topic; they set the terms the whole map plays on.

- **They sit underneath the [verdict's](../40-the-verdict/01_which-bets-get-to-agi.md) two gauges.** The verdict said to watch the **novelty gap** and the **data wall.** This page is the deep version of the data-wall gauge — plus two more dials beside it (compute cost, energy). If these three keep receding, the mainstream stack keeps improving; if they bind, it stalls. The bounds are *how you actually read* the verdict's central "does scale keep buying gains?" question.
- **They explain why the [data-wall answers](../40-the-verdict/01_which-bets-get-to-agi.md) (AP4 / AP9 / AP10) are rising.** Those bets look like rivals to scale, but Wall 1 shows they are really where scale's *next* training experience comes from once human text is spent. The energy wall raises them further: experience and self-play can be far cheaper per unit of learning than reading the whole internet again.
- **They give the [brain-based bets](../20-the-approaches/06_ap6-brain-based.md) (AP6, and neuromorphic hardware) a second reason to matter.** Not "the brain is more capable" (it is not, today), but "the brain is *roughly a million times* more **energy-efficient**" (a light-bulb versus a power station). If the energy wall is the tightest of the three, the value of copying the brain's *efficiency* — not just its method — goes up. Wall 3 is the strongest argument for AP6 that has nothing to do with capability.
- **They reframe [AP2 · reasoning / test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md).** "Think longer at answer-time" *(short reminder: spend extra compute when answering a hard question, instead of only when training)* is partly a **response to the walls** — it wins more ability from a *fixed* trained model, buying capability with inference-time compute when training-time scaling gets too expensive or runs out of data. But by the Jevons paradox above, it is also a big new source of total compute and energy demand. The bounds are why AP2 exists *and* why it does not make the energy problem go away.

**The one line to keep:** the bounds are the physical, arithmetic floor under the whole "is scale enough?" argument. They do not decide *whether scale works* — they decide *whether we can afford to run it far enough to matter*, and they set the price every bet on the map has to pay.

---

## ⚠️ Honesty box

- **These are ceilings on *scale*, not on *intelligence*.** The walls press hardest on the "just make it bigger" bet ([AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md)). A cleverer, smaller approach that needs less data, compute, and energy would feel them far less. So "the walls are closing in" is an argument *for* the second-ingredient and efficiency bets as much as a warning about scale. **[Contested.]**
- **Every fast number here ages in months.** The 300-trillion-token stock, the ~2028 date, the $200–500M training runs, the 415→945 TWh energy path, the nuclear deals — all are dated snapshots (2024–2026). The lasting parts are the **three-wall shape** (fuel / engine-cost / power), the **numbers-not-adjectives** method, the **Landauer floor**, and the **recede-vs-demand race**. Treat the specific figures as this-year facts. **[Established core, dated specifics.]**
- **The data-wall date already moved once — that teaches two opposite lessons.** It slipping from "2024" to "2028" proves cleverness can push a wall back (a point for the optimists). It also proves the wall is *real enough that we keep having to push it* (a point for the pessimists). Do not read the slip as either "the wall is fake" or "the wall is here." **[Contested.]**
- **"Numbers, not adjectives" applies to this page too.** Both scary stories ("AI will boil the planet") and dismissive ones ("it's a rounding error") are usually told with adjectives. The honest read is arithmetic: ~1.5% of world electricity now, heading to ~3% by 2030 — large and fast-growing, not apocalyptic, not negligible. Hold the number, distrust the adjective. **[Established.]**
- **Efficiency is not a rescue — it reshapes the problem.** It is tempting to answer every wall with "but we keep getting more efficient." True, and yet the Jevons paradox means the *totals* keep rising anyway. Efficiency changes *where* the wall is, not *whether* there is one. **[Established.]**
- **The physics floor is far, but "far" is not "irrelevant."** The billion-fold gap to the Landauer limit says huge efficiency gains are *possible in principle*. It does **not** say they are easy, or that anyone knows how to claim them. A possible-in-physics saving you do not know how to build is not money in the bank. **[Established that the room exists; how much is reachable is open.]**

---

## How to use this (if you want to direct AI work, or judge a claim)

- **When someone says a model got better, ask which wall they spent against.** More data, more compute, more energy — or *better methods* that used less of all three? A gain bought with raw scale is running toward the walls; a gain bought with efficiency is pushing the walls back. That single question tells you whether the improvement is cheap to repeat or expensive to sustain.
- **Demand the number.** For any energy or cost claim about AI — reassuring or alarming — apply MacKay's rule: ask for the actual figure and compare it to something real (a country's electricity, a percent of GDP). Most confident claims in both directions dissolve when you make them numeric.
- **Read the walls as a race, not a verdict.** Do not say "scale has hit a wall" or "the walls don't matter." Say: *which is moving faster — the ceiling receding (efficiency) or demand pushing into it?* Watch the data-stock date, the cost-per-run curve, and data-centre TWh. Those three dials are the honest gauges of whether scale keeps paying.
- **Take the power grid as seriously as the algorithm.** In 2026 the binding limit on the biggest models is as likely to be **electricity and chips** as ideas. When you judge whether a lab can build the next frontier model, look at whether it has the **power** lined up, not just the plan. The nuclear deals are the tell.
- **Watch for the efficiency-and-Jevons pattern everywhere.** When a capability gets cheaper, expect total use — and total cost — to rise, not fall. Budget and plan for that, or you will be surprised by the electricity bill even as each chip gets better.
- **What you delegate vs what you keep:** hand the *engineering* to others and to AI — building the data-centres, designing the chips, running the training. **Keep for yourself** the judgement this page teaches: reading the three walls as a race, refusing both the scary and the dismissive adjective, and knowing that a bet can be right about intelligence and still lose to the arithmetic of tokens, dollars, and watts.

---

## Connections

- **Keep only three things:** ① Making a model bigger burns three limited resources, each near a ceiling — **data** (good human text runs out ~2028; ~300 trillion tokens, Epoch AI), **compute** (training compute has doubled every ~6 months for over a decade — 4× faster than chips improve — so scale is bought with money; runs heading past $1B by ~2027), and **energy** (AI data-centres at ~1.5% of world electricity in 2024, doubling toward ~3% by 2030 — companies are buying nuclear plants). ② **None of the three is a physics wall** (the true floor, the **Landauer limit**, is a *billion*-fold below us, and the brain runs general intelligence on ~20 watts). They are **economic and supply walls** — you run out of *cheap* text, *affordable* chips, and *available* power first — and they **recede** as we get cleverer (**algorithmic efficiency** halves the compute for a fixed skill every ~8 months) while **demand pushes into them faster** (the **Jevons paradox**). ③ So the bounds turn "is scale enough?" into a **race:** does the money-and-electricity ceiling arrive before scale reaches AGI, or does efficiency keep pushing it back? A bet can be right about intelligence and still lose to arithmetic.
- **Down the ladder (already read):** [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — owns the *idea* of the data wall (this page adds the *quantities*); [AP1 · scale](../20-the-approaches/01_ap1-scale-and-foundation-models.md) — the bet the walls press on; [The verdict](../40-the-verdict/01_which-bets-get-to-agi.md) — named the data wall as one of its two gauges (this page opens all three).
- **Its links across the map:** the **data-wall answers** [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) / [AP9](../20-the-approaches/09_ap9-open-endedness.md) / [AP10](../20-the-approaches/10_ap10-embodiment.md) — scale's new fuel lines past Wall 1; [AP6 · brain-based](../20-the-approaches/06_ap6-brain-based.md) — the ~20-watt existence proof that Wall 3 makes strategically important; [AP2 · reasoning](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — "think longer" as partly a response to the walls, and partly a new source of demand; [AP11 · whole-brain emulation](../20-the-approaches/11_ap11-whole-brain-emulation.md) — its compute/energy estimates are the same walls taken to the extreme.
- **How sure are we?** The compute-doubling history, the Landauer floor, the brain's ~20 watts, and the reality of the power deals — **[Established]**. The 300-trillion-token stock, the ~2028 date, the training-run costs, and the 945 TWh path — **[Likely, dated projections]**. Whether the walls truly *bind* before AGI — **[Contested, the open question]**.

## Check yourself *(try one, from memory)*

1. Name the **three walls** and, for each, say what limited resource it is a ceiling on. Which one is arriving first?
2. The data-wall date moved from "2024" to "2028." Give the two *opposite* lessons a careful reader draws from that single fact.
3. Training compute has doubled about every 6 months, but chips only get twice as good every ~24 months. Where does the extra compute come from, and why does that turn the compute wall into a **money** wall?
4. What is the **Landauer limit**, and why does the fact that we use a *billion times* more energy than it mean energy is a "building problem," not a "physics problem"? Use the brain's 20 watts in your answer.
5. Explain the **Jevons paradox** in one sentence, and say why it means "we keep getting more efficient" does **not** make the energy wall go away.
6. The [verdict](../40-the-verdict/01_which-bets-get-to-agi.md) asked "is scale the *source* or the *fuel*?" What second, colder question do the bounds add underneath it?

## Revision notes

*Newest first.*
- `rev 1 (2026-07-16)` — created as **The bounds**, the first page of the new reading group **③ Across the approaches** (sortkey 3001, reads after ② The approaches and before ④ The verdict). It is a **cross-cutting page, not a twelfth bet** — the physical/economic ceilings every scale-based bet must respect. It is the first of the two cross-cutting writes the [spine §4](../APPROACHES_TO_AGI.md) and the [verdict's](../40-the-verdict/01_which-bets-get-to-agi.md) closing footer named (the other = alignment / RSI). Structure: the three bounds in one minute → base reminder (leans on [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md), the [verdict](../40-the-verdict/01_which-bets-get-to-agi.md)) → **Wall 1 data** (the measured stock ~300T tokens, ~2028, Epoch AI — the *quantities* the scaling page's data-wall *idea* did not give; ties to the data-wall answers AP4/AP9/AP10) → **Wall 2 compute** (Sevilla's ~20mo→~6mo doubling, the cost curve toward $1B runs, the Dwarkesh "1% of GDP" headroom, Moore's-law gap) → **Wall 3 energy** (MacKay's "numbers, not adjectives" method; IEA 415→945 TWh; the gigawatt/nuclear deals; the **Landauer** floor a billion-fold below us; the brain's ~20 W) → **do the walls bind?** (algorithmic efficiency halving compute every ~8 months = the walls recede; **Jevons paradox** = demand rises anyway; synthesis: **economic/supply walls, not physics walls** → a *race*, not a wall) → what the bounds mean for the map (they sit under the verdict's two gauges; explain the data-wall answers; give AP6/neuromorphic a second reason; reframe AP2) → honesty box → director's use → connections → check-yourself. **Grounded** (grep-verified where in corpus): Sevilla et al. 2022 abstract (verbatim), MacKay 2008 "numbers, not adjectives" (verbatim), Amodei 2024 "run out of data" (verbatim), Dwarkesh 2023 "10,000x scaleup … one percent of world GDP" (verbatim). **Full live-SOTA pass (2026-07):** Epoch AI data-stock (~300T tokens, ~2028, 2026–2032 range; the estimate moved from 2024) + algorithmic-efficiency (halves ~every 8 months) + frontier training costs ($40–100M GPT-4, ~$190M Gemini Ultra, $200–500M 2026 runs, ~2.4×/yr, $1B by ~2027) + IEA energy (415 TWh/1.5% in 2024 → 945 TWh/~3% by 2030, AI ~30%/yr) + the nuclear/power deals (Microsoft–Three Mile Island 835 MW; Meta multi-GW; Amazon $20B+; Google SMRs) + the Landauer limit (E ≥ kT ln2 ≈ 2.9×10⁻²¹ J/bit, ~1e9× above floor) — each dated and source-graded, with the recede-vs-demand tension surfaced as the central open question. Built to the simplest-English + progressive-ladder standard ([HARD_RULES §6.5](../../INSTRUCTIONS/HARD_RULES.md)): every medium-or-hard term glossed (bound, token, FLOP, Moore's law, GDP, TWh, MW/GW, SMR, joule/bit, Jevons paradox, neuromorphic), one new step at a time, no prerequisite used before an earlier rung taught it; the data-wall *idea* is refreshed-and-linked to the scaling page (not re-taught), only its *quantities* are new here. **§7.0 recheck done:** re-read whole file in harsh-critic + confused-beginner hats. All four verbatim quotes grep-confirmed against corpus; every fast number dated and internally consistent (300T tokens / ~2028 / ~6-mo doubling / 415→945 TWh / Landauer ≈ 3×10⁻²¹ J-per-bit ≈ 10⁻²¹ order, checked against the "millionth³ then /1000" gloss; brain ~20 W vs data-centre ~million× vs Landauer ~billion× kept as distinct, consistent comparisons); §6.5a idiom/flourish sweep (removed "keep the lights on," "waved it away," "life-support," "Sit with," "cuts two ways" / "cuts both ways," "bite/bites," "sprint toward," "re-light"); glossed the key recurring term **bind** at its section (take effect as a real limit) plus every medium-or-hard term; the data-wall *idea* refreshed-and-linked to the scaling page (only its *quantities* are new here — no re-teach, DRY §4.2); every internal link verified to resolve to a live file. Reading-order/group placement verified (first ③ page, before the verdict which renumbers to ④). It is the **deep home for the three bounds — data stock, the compute trend and its cost, and the energy wall (with the Landauer floor).**

---
*This is the first of the two cross-cutting pages (reading group ③), the physical floor under the whole map. Its companion is the [alignment & self-improvement](02_alignment-control-and-self-improvement.md) page (the risk axis). It leans on [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md), and [The verdict](../40-the-verdict/01_which-bets-get-to-agi.md); the full [map is here](../APPROACHES_TO_AGI.md). The verdict asked whether scale is the source or the fuel; this page asks whether we can afford to run it far enough to find out.*
