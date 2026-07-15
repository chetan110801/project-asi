---
id: c-scaling-laws
sortkey: 1002
title: Scaling laws & emergence — what "make it bigger" really buys
domains: [machine-intelligence, scaling]
level: core
prereqs: [c-next-word]
provides: [scaling-laws, compute-optimal-scaling, chinchilla, the-data-wall, emergent-abilities, emergence-mirage-debate]
resources: [r-cs336]
status: ready
reading_time: 18 min
rev: 2
created: 2026-07-14
updated: 2026-07-14
---

# Scaling laws & emergence — what "make it bigger" really buys
*This is the second rung of the ladder. On the first rung ([next-word](01_guessing-the-next-word.md)) you saw the one job: guess the next word. Now we ask the money question: **what happens when you make that machine bigger?** The answer is one of the most important facts in modern AI — the machine's mistakes fall in a **steady, predictable line** as you make it bigger. That single fact is what the whole "make it bigger" bet stands on. This page explains it in plain words: what exactly gets bigger, why the mistakes fall so neatly, how much of each thing you should buy, why this is now **running into a wall**, and the field's biggest fight — whether new skills that seem to "switch on" at large size are real, or just a trick of how we score the test.*

> **You are here:** rung 2 of the ladder. It builds on [guessing the next word](01_guessing-the-next-word.md). One-line reminder from that rung: **an AI language model is trained to guess the next word; when its guess is wrong, that is a "mistake," and the whole aim of training is to make fewer mistakes.** That "mistake-count" is the star of this page.
>
> **Where the facts come from:** Kaplan et al. 2020, *Scaling Laws for Neural Language Models*; Hoffmann et al. 2022, *Training Compute-Optimal Large Language Models* ("Chinchilla"); Wei et al. 2022, *Emergent Abilities of Large Language Models*; Schaeffer et al. 2023, *Are Emergent Abilities of Large Language Models a Mirage?*. Quotes are exact. Fresh web check (**July 2026**): the "data wall" (Ilya Sutskever, 2024) and the still-open emergence argument.

---

## Three things you can make bigger, and one number they move

Everything here is about a simple cause and effect. On one side, **three things you can pour in more of.** On the other, **one number that says how good the machine is.**

The three things you can make bigger (the field calls them the three ways to scale):

- **Size** — how many **adjustable numbers** are inside the machine. These inner numbers are the "knobs" that training sets; more of them means a bigger machine. (The proper name is **parameters**.) Counted in billions.
- **Data** — how much **text** you train on. (Counted in **tokens** — a token is a chunk of text, about a short word or a piece of a word.) More data means more to read. Counted in trillions of tokens.
- **Computer power** — how much **number-crunching** you spend on training. (The proper name is **compute**, measured in **FLOPs** — the count of tiny arithmetic steps, like single multiplications. It is just a way to measure "how much calculating," the way metres measure distance.) More of it means a longer, heavier training run.

The one number they move:

- **The mistake-count.** This is the score from rung [next-word](01_guessing-the-next-word.md): how often, and how badly, the machine guesses the next word wrong. Lower is better. (Its proper name is the **loss**.) Everything below is the story of what happens to this one number as you turn up the three things above.

---

## The big finding: a straight, steady line

Here is the discovery, in the exact words of the paper that found it. Read it once, then we unpack it:

> "The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude."
> *(Kaplan et al., "Scaling Laws for Neural Language Models," 2020)*

Two phrases to unpack, simply.

**"Scales as a power-law."** A **power law** here means a very steady rule: **every time you multiply the size (or data, or compute) by the same amount, the mistakes drop by the same fraction.** For example, make the machine 10 times bigger and the mistakes fall by a fixed slice. Make it 10 times bigger *again*, and they fall by the same-sized slice again. It is smooth and regular — no jumps, no luck.

There is a neat way to *see* this: if you draw the picture on a special chart where each step means "times 10" (instead of "plus 1") on both directions, the steady rule shows up as a **perfectly straight line**. That straight line is the most famous picture in modern AI.

**"Seven orders of magnitude."** An **order of magnitude** is just a factor of 10. Seven of them is ten million (10 × 10, seven times). So the straight line held true from tiny machines all the way up to machines **ten million times** larger. That is the shocking part. Not that bigger is better — everyone guessed that. The shock is that bigger is better **so regularly that you can draw it with a ruler and read the future off it.**

### Why this one line changed the whole field

Think about what a straight, steady line lets you do. If you measure the mistakes for small and medium machines, you can **extend the line** and read off how good a giant machine will be — *before* you spend the millions of dollars to build it. The paper says exactly this:

> "These relationships allow us to determine the optimal allocation of a fixed compute budget."
> *(Kaplan et al., 2020)*

("Optimal allocation of a fixed compute budget" = the best way to spend a set amount of computer power.) This turned a gamble into a plan. Instead of *hoping* a bigger machine would be better, labs could **calculate** it: pick a budget, predict the result, build the machine. That is why the whole field started making things bigger and bigger. **[Established]** — this steady line is one of the most re-tested results in AI.

**What the line does NOT promise:** it does not promise **zero** mistakes. The line falls toward a **floor** it can never go below. Why is there a floor? Because language has real, built-in surprise — the exact next word is often a genuine coin-flip that no machine, however large, can get right every time. Making the machine bigger closes the gap **down to that floor**, but never past it. **[Established]**

---

## Chinchilla: the same money, spent smarter

The first finding said "make it bigger." But it did not clearly say **how to split your money** between the two costly things: more size, or more data? For about two years the field guessed wrong. A 2022 study caught the mistake:

> "we find that current large language models are significantly undertrained ... for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled."
> *(Hoffmann et al., "Training Compute-Optimal Large Language Models," 2022 — the "Chinchilla" paper)*

Unpack it. **"Undertrained"** means the giant machines of 2020–2021 were the wrong shape: **too many inner parts for the small amount of text they read** — big brains that had not read enough. The fix, called **compute-optimal** (getting the best score for a set amount of computer power): **grow the size and the amount of text together, hand in hand.** Double the size, double the text.

They proved it the expensive way. They built a machine called **Chinchilla** (70 billion parts) and set it against a bigger machine called Gopher (280 billion parts), using the **same computer power** — but Chinchilla read **4 times more text**. The smaller, better-read machine won:

> "Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B) ... on a large range of downstream evaluation tasks."
> *(Hoffmann et al., 2022)*

The lasting lesson (which outlives the exact numbers): **a bigger machine is not automatically a better machine.** For a set budget there is a **right shape**, and for two years the field was building the wrong shape — too big, too little-read.

**A newer twist (July 2026):** Chinchilla answers "cheapest to *train*." But a machine is trained **once** and then **run** billions of times to answer people — and a bigger machine is more expensive to run **every single time**. So today labs often do the opposite on purpose: they take a **smaller** machine and train it on **far more** text than Chinchilla says — paying more up front to get a machine that is **cheaper to run forever after**. So do not memorise the "double for double" ratio; hold the real idea: **balance training cost, running cost, and quality.** The exact ratio changes; the trade-off stays. **[Established]**

---

## The wall: there is only one internet

The steady line has a hidden catch, and it is now the biggest story in AI: **the line needs you to keep feeding it more text.** You cannot do that forever. This is the **data wall**.

The reason is simple. The Chinchilla rule says the amount of text must grow along with the size. But good human text — books, articles, good web pages, code — is a **limited pile**, and the biggest machines have already read a large part of all of it. The clearest warning came from Ilya Sutskever (a co-founder of the lab OpenAI) in a 2024 talk:

> "Pre-training as we know it will unquestionably end ... because we have but one internet."
> *(Ilya Sutskever, 2024; found on the web, July 2026)*

("Pre-training" = the first, main training stage, where the machine reads huge amounts of text. "Unquestionably" = for sure.) He called data **"the fossil fuel of AI"** — like oil, the internet is a **one-time supply** built up over decades of human writing. You can burn through it fast, but you cannot make more original human text on demand. **[Likely]** as a near-term limit — people argue about *when*, not about the fact that text is finite.

### What the field does now that the wall is here (July 2026)

Because there is not much new text left, the field's effort has moved **off "just read more text"** and onto other tricks — and this move is itself a sign that plain "make it bigger" is straining:

- **Make new text** — have machines **write** their own training text, then keep only the good parts. This helps, but it has a known danger called **model collapse** (train a machine too much on its own writing, and the rare, unusual bits fade away — like a photocopy of a photocopy getting worse). So labs keep a lot of real human text and add machine-made text mostly for things that can be **checked** (math, code).
- **Polish after training** — squeeze more out of a finished machine by extra shaping steps (teaching it to follow instructions, for example).
- **Think longer when answering** — instead of a bigger machine, spend extra computer power **at answer-time**, letting the machine work step by step. This is a whole separate bet, with its own future page `[AP2]`. Experts now expect this answer-time computer power to grow larger than the training computer power by 2030.
- **Better training methods** — smarter recipes are letting **smaller** machines catch up to bigger ones, showing that *how* you train is winning back ground from *how big*.

The plain summary: **the steady line is not cancelled — it is running low on fuel.** So gains now come from *quality and cleverness*, not raw size. Whether you call that "scaling is dead" or "scaling moved to new places" is exactly the argument on the [AP1 page](../20-the-approaches/01_ap1-scale-and-foundation-models.md). **[Contested]** as a headline; **[Established]** that good human text is running short.

---

## Emergence: skills that seem to switch on

Now the most argued idea on this page. The steady falling line is the **predictable** face of scale. But there is a stranger face. Some skills seem to be **missing** in smaller machines and then **present** in bigger ones — as if a switch flipped. The paper that named this:

> "We consider an ability to be emergent if it is not present in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted simply by extrapolating the performance of smaller models."
> *(Wei et al., "Emergent Abilities of Large Language Models," 2022)*

In plain words: an **emergent** skill is one you do **not** see in small machines, that suddenly appears in big ones — so you could not have guessed it was coming by watching the small ones. ("Extrapolating" = extending the pattern from smaller machines.) The examples included doing multi-step math, and answering in languages the machine barely saw.

Why did this shake people? Because it broke the comfort of the steady line. If new skills can appear **with no warning** at some unknown size, then you cannot fully know what your next, bigger machine will be able to do — including things you did **not** want it to do. That is a real safety worry. **[Established as a thing that happens]** — that test scores can jump sharply is not in doubt. What the jump **means** is very much in doubt.

### The pushback: it may be a trick of the scoring

Here is the twist that makes this a real fight. A 2023 study argued that the "sudden switch" is often **not a real change in the machine** — it is caused by **how we score the test**:

> "emergent abilities appear due [to] the researcher's choice of metric rather than due to fundamental changes in model behavior with scale ... alleged emergent abilities evaporate with different metrics or with better statistics."
> *(Schaeffer, Miranda & Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", 2023)*

("Metric" = the way you score the test. "Evaporate" = disappear.) How can the score jump when the machine changed smoothly? Here is the trick, step by step — go slowly:

1. Many tests use **all-or-nothing** scoring. Example: a multi-step math sum counts **only** if **every** digit is right. Get 4 of 5 digits right and you score **zero**.
2. Under the surface, the machine's real skill — its chance of getting the whole thing right — is climbing **smoothly** as it grows, just like the steady line says.
3. But the all-or-nothing score **hides** that smooth climb, showing "zero" for a long time, until the machine crosses the point where it *usually* gets the whole sum right. Only then does the score leap from near-0 to high.
4. So the **score** jumped, but the **skill** rose smoothly the whole time. Switch to a **fairer, part-marks** score (count how many digits are right) and the "sudden jump" turns into a smooth slope.

Name the mistake clearly: **a jump in the scoreboard was mistaken for a jump in the machine.** The machine changed smoothly; the **ruler** was the jumpy part.

### Where the fight stands (July 2026)

Do not tidy this into a winner — being honest is the point. The argument is **still open.** The scoring-trick idea is now widely accepted for **many** cases: a lot of "sudden skill" charts do smooth out under fairer scoring. **But** later work finds that a few sharp jumps **survive** even with fair scoring, and suggests these are real, sudden shifts that happen **during training** (like water turning to ice at 0°C — a sudden change of state at a threshold). The fair summary: **"emergence" was over-sold as magic, but it was not entirely made up.** So treat any single "skill X appeared at size Y" claim with care until you know **how the test was scored.** **[Contested — open question]**

---

## ⚠️ Honesty box

Scaling attracts two opposite exaggerations — "the line goes up forever, so AGI is just more computers" and "the line is a trick, so none of it is real." Both are wrong.

- **The line is real, but it measures mistakes, not wisdom.** Fewer word-guessing mistakes is measured and solid, and it keeps falling as you scale. But "fewer mistakes" is not the same as "understands the world." Whether one becomes the other is a separate, open question — not settled by this line. **[Established → Contested]**
- **Extending the line is a bet, not a measurement.** A straight line *so far* does not promise it stays straight. The line already bends toward its floor, and the data wall takes away the fuel it assumed. Reading "AGI" off a stretched-out line is a hope, not a proof. **[Contested]**
- **"Best shape" keeps changing.** Chinchilla's neat rule was right for its question (cheapest to train) and already changed for a different question (cheapest to run). Any exact ratio you memorise will be out of date in a year; keep the trade-off, not the number. **[Established]**
- **"Emergent" is a word doing too much work.** Some jumps are scoring tricks; some may be real sudden shifts; the word "emergent" quietly adds a feeling of *magic* that the evidence does not fully support. Keep the fact (scores can jump) apart from the story (a new skill switched on). **[Contested]**
- **Numbers age fast.** "Ran out of data," "answer-time computer power grows past training by 2030," and any size figures are snapshots from 2020–2026. The lasting parts are the **steady-line shape** and the **limit of human text**; the numbers around them change quickly.

---

## How to use this (if you want to direct AI work)

- **Ask which of the three things moved.** When someone says a machine got better, ask: more size, more (or cleaner) text, more training power, or more *answer-time* thinking? The answer tells you whether the gain will keep coming or was a one-off. It is the closest thing to an X-ray of AI progress.
- **Treat the data wall as a strategy fact.** If plain scaling is running low on text, the edge moves to **better data, machine-made data, polishing, and answer-time thinking** — that is where the returns are in 2026. Chasing "just make it bigger" is chasing a fuel that is running out.
- **Never trust an "it suddenly can do X" headline on its own.** Ask: *how was the test scored?* All-or-nothing scoring invents fake cliffs; part-marks scoring often shows a smooth slope. That one question deflates most hype.
- **Keep training cost and running cost apart.** The cheapest machine to **build** is rarely the cheapest to **run**. For a real product you usually want a smaller, over-trained machine.

---

## Connections

- **Keep only three things:** ① make a language model bigger and its mistakes fall in a **steady, straight line** you can predict far in advance; ② for a set budget there is a **right shape** (grow size and text together) — but human text is **limited**, so the line is now hitting a **data wall**; ③ skills that seem to "**switch on**" at large size are partly **real** and partly a **scoring trick** — the fight is not settled, so always ask how the test was scored.
- **Down the ladder (already read):** [guessing the next word](01_guessing-the-next-word.md) — the "mistake-count" and why guessing forces real knowledge.
- **Up the ladder (next):** [AP1 · the "make it bigger" bet](../20-the-approaches/01_ap1-scale-and-foundation-models.md) — this steady line is the whole reason people believe that bet.
- **How sure are we?** The steady line and the limit of good text — **[Established]**. "Scaling alone reaches AGI" — **[Contested → AP1]**. "Sudden skills are real vs. a scoring trick" — **[Contested, open]**. Exact best-shape ratios — **[out of date, now depends on running cost too]**.

## Check yourself *(try one, from memory)*

1. A friend says "they doubled the machine's size and the mistakes barely fell — scaling must be broken." Give two innocent reasons (use the words *steady line* and *floor*) before deciding anything is broken.
2. Explain why Chinchilla — a *smaller* machine — beat a bigger one on the same computer power. Then explain why, even so, a company might train an *even smaller* machine on *even more* text.
3. Say what the data wall is in one sentence, and name two things the field does once it hits the wall.
4. A test shows a machine jump from 2% to 60% between two sizes. Give the "scoring trick" reason this jump might be fake — and then say honestly what part of the worry still stands.

## Revision notes

*Newest first.*
- `rev 2 (2026-07-14)` — rewritten to the **simplest-English + progressive-ladder** standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)): short plain sentences, no fancy words, every term glossed. Now placed as **rung 2 of the ladder**, building on [next-word](01_guessing-the-next-word.md) with a short reminder-and-link (the "mistake-count" idea is owned there, not re-taught here). Same facts and quotes as rev 1; only the language and the ladder-wiring changed.
- `rev 1 (2026-07-14)` — created as the mechanism page the AP1 bet pulls in. Grounded in the scaling papers (Kaplan, Chinchilla, Wei, Schaeffer); quotes exact; live-web freshness pass for the data wall and the open emergence argument.

---
*Rung 2 of the ladder. Down → [guessing the next word](01_guessing-the-next-word.md). Up → [AP1 · the "make it bigger" bet](../20-the-approaches/01_ap1-scale-and-foundation-models.md).*
