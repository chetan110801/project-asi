---
id: c-ap1-scale
sortkey: 2001
title: AP1 · Scale & foundation models — the "make it bigger" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws]
provides: [scale-hypothesis, the-bitter-lesson, foundation-model-paradigm, scaling-suffices-debate]
resources: [r-cs336]
status: ready
reading_time: 22 min
rev: 2
created: 2026-07-14
updated: 2026-07-14
---

# AP1 · Scale & foundation models — the "make it bigger" bet
*This is the first big idea for how to build a machine that can think in a general way. The idea is simple: **do not try to be clever — just make the machine bigger.** Give the machine one easy job (guess the next word), then feed it a huge amount of text and a huge amount of computer power. The bet is that real thinking will appear on its own, as a **side effect** — nobody has to build the thinking in by hand. This is the idea behind the AI tools you already use, and it is the idea every other approach argues against. This page explains it from zero: the bet in one minute, why it could work, the belief that backs it (the **Bitter Lesson**), and — the part that matters most — exactly where the bet is now stuck.*

> **You are here:** this is the **AP1** page — the first of the "approaches to AGI" (see the map, [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)). AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. This page is not a how-to guide. It is a way to **judge** the idea: to see why people believe it, and why they might be wrong.
>
> **This page builds on two earlier rungs of the ladder** (both short, both plain): [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — how today's AI actually works — and [scaling laws & emergence](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — what happens when you make it bigger. If you read those, this page will feel easy. A one-line reminder of each is given where it is used, so you will not get lost.
>
> **Where the facts come from:** Rich Sutton 2019, *The Bitter Lesson*; Bommasani et al. 2021, *On the Opportunities and Risks of Foundation Models*; Brown et al. 2020, the *GPT-3* paper; the scaling-law papers by Kaplan (2020) and Hoffmann (2022); François Chollet on the Dwarkesh Podcast, 2024; Schaeffer et al. 2023 on "emergence." Fresh check of the field, done on the web (**as of July 2026**): Ilya Sutskever's 2024 talk on running out of data, and the current "is scaling finished?" debate.

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**Take one simple job — guess the next word in a piece of text — and do it on a giant scale. The result is most of the way to a thinking machine.**

You do not teach the machine grammar. You do not teach it facts. You do not teach it how to reason. You just:

1. make the machine **big** (give it more inner parts),
2. feed it a **huge** amount of text (much of the internet), and
3. spend a **large** amount of computer power training it.

And then, the bet says, the ability to do real tasks shows up **by itself** — as a side effect of getting very good at guessing the next word.

Why believe this could work? Because there is a clear, measured pattern: the bigger you make the machine, the **fewer mistakes** it makes, in a smooth and steady way you can predict in advance. So "make it smarter" turns into "buy more computer power." That turns a hard research puzzle into a simple plan. The dream at the end of the road: keep making it bigger, and it keeps getting better — all the way to a general thinking machine.

That is the bet. The rest of this page explains **why it is a serious idea** and **why it might still be wrong.**

---

## First, a one-line reminder of the base

This bet stands on the idea from the first rung, [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md). In short: **today's AI is a machine trained to guess the next word in text.** To guess well, it is **forced** to pick up real math, facts, meanings, and patterns — all as a side effect of that one goal. (If that is new to you, read [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md) first; it is short.)

Hold that, and the whole AP1 bet fits in one line:

> **If guessing the internet well forces the machine to pack in how the world works, then guessing it *well enough* might force the machine to actually *understand* the world.**

The bet is that "well enough" can be reached just by making everything bigger.

---

## Why this is a serious idea, not a trick

It is easy to laugh at this bet ("it is just fancy autocomplete") and easy to over-hype it ("it will become a god"). Both miss the point. The idea rests on three solid legs.

### Leg 1 — the pattern is real and measured

This part is not an opinion. When you make a language model bigger, its number of mistakes falls in a **smooth, steady curve**. This holds true across a huge range — from tiny machines to machines millions of times larger. Because the curve is so steady, you can **predict** how good a giant machine will be *before* you spend the money to build it. (The full story of this curve is on the [scaling-laws page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md).)

Even better: the machine started doing things **nobody trained it to do**. The famous case is a machine called GPT-3. It was trained only to guess the next word. But once it was big enough, it could translate between languages and do simple math on its own — just because that was the most likely way to continue the text. **Nobody built those skills in.** They appeared from scale. This is the real, factual core of the bet. **[Established — this actually happened]**

### Leg 2 — the belief behind it: the Bitter Lesson

Leg 1 shows that scale *works*. This second leg is a belief about *why scale will keep winning*. It comes from Richard Sutton, a scientist who helped create a major part of AI called reinforcement learning (teaching a machine through reward and trial-and-error). In 2019 he wrote a short, famous essay. His main claim:

> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin."
> *(Rich Sutton, "The Bitter Lesson," 2019)*

In plain words: over 70 years, the methods that just **use more computer power** have beaten the methods where humans carefully build in their own knowledge — and beaten them by a lot. ("General methods that leverage computation" = simple methods that lean on raw computer power, not on human cleverness.)

Sutton says the same story repeats again and again. Here is his four-step pattern:

> "1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term ... but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning."
> *(Sutton, 2019)*

Read slowly: researchers build in their human knowledge; it helps for a while; then it **stops helping and even gets in the way** ("plateaus" = flattens out and stops improving; "inhibits" = blocks); and the big jump finally comes from the other path — **more computer power**, plus search and learning.

Why is it called *bitter*? Because it is a hard truth to swallow. The winning path is **not** the clever, human-insight path that researchers *wanted* to win. Sutton drives it home:

> "We have to learn the bitter lesson that building in how we think we think does not work in the long run."
> *(Sutton, 2019)*

He is warning us: do not try to hand-build your own idea of "how thinking works" into the machine. Instead, build a simple learner and give it lots of computer power. His proof is 70 years of history: in chess, in the game Go, in speech, and in vision, the "more computer power" method beat the "more human knowledge" method every single time. AP1 is the Bitter Lesson aimed at intelligence itself. **[Likely]** as a reading of history; **[Contested]** as a promise about the future (critics say this time we really do need a new idea, not just more power — that is the big argument below).

### Leg 3 — what it built: foundation models

Scaling this simple job made a brand-new kind of thing, and it got a name. The report that named it says:

> "models (e.g., BERT, DALL-E, GPT-3) trained on broad data (generally using self-supervision at scale) that can be adapted to a wide range of downstream tasks. We call these models **foundation models** ..."
> *(Bommasani et al., "On the Opportunities and Risks of Foundation Models," 2021)*

In plain words: a **foundation model** is one huge machine, trained once on a wide mix of data, that many smaller tools can then be built on top of. ("Adapted" = adjusted a little for a new job. "Downstream tasks" = the many later jobs built on top of it.) You do not train from scratch each time; you start from the big shared machine. That is the whole shape of AP1: build **one** giant general model, then stand everything else on it.

The same report warns about the risk hidden in this:

> "the defects of the foundation model are inherited by all the adapted models downstream."
> *(Bommasani et al., 2021)*

Simple version: if the big machine has a flaw or a bias, **everything** built on top of it gets that same flaw. One weak spot spreads everywhere. That is the cost of "build once, use everywhere." **[Established]**

### So, what does AP1 say "intelligence" is?

Every approach quietly answers the question *"what is intelligence?"* Here is AP1's answer, from the three legs above:

- **Intelligence is** a by-product of very good prediction. Predict the world well → you must have packed the world in → and (this bet says) packing the world in *is* most of what understanding means.
- **What it improves** is one thing: the number of mistakes in next-word guessing, pushed down by making everything bigger.
- **Its claim about the missing piece:** there is **no** special missing piece. The known gaps (real reasoning, common sense, and so on) will close slowly and steadily as the mistake-count keeps falling. In this view, scale is not *one* path to intelligence. It is *the* path.

That last claim is the strongest and most argued-over claim in all of AI. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP1 has the **best track record of any idea on this list.** It made every AI tool that became famous. Its main prediction (more scale → fewer mistakes, smoothly) is one of the most re-tested and confirmed results in the field. And it keeps surprising the people who doubt it. No rival has done anything close. Hold that in mind. Now, the four places it is truly stuck.

### Stuck #1 — running out of text (the "data wall")

The bet's engine needs to be fed more and more text. But there is a problem: **good human text is limited.** Books, articles, good web pages, code — it is a finite pile, and the biggest machines have now read a large part of all of it. People call this the **data wall**. The clearest warning came from Ilya Sutskever (a co-founder of the lab OpenAI) in a 2024 talk:

> "Pre-training as we know it will unquestionably end ... because we have but one internet."
> *(Ilya Sutskever, 2024; found on the web, July 2026)*

("Pre-training" = the first, main training stage, where the machine reads huge amounts of text. "Unquestionably" = for sure.) His point: you can only feed the machine the internet once. When you have used it up, this way of scaling has to stop. This hurts AP1 in a deep way: the pattern that the whole bet stands on **needs** ever more text, so running out of text does not just slow the bet down — it **breaks the engine**. The field is now trying other tricks instead (see the honesty box). But notice: those tricks are a move *away* from "just make it bigger." That the field had to move is itself a sign that pure scale is not enough. **[Likely]** the wall is close; the exact timing is argued.

### Stuck #2 — the "surprise new skills" may be partly fake

AP1's most exciting sales pitch is this: as you scale up, brand-new skills seem to **switch on suddenly**, out of nowhere. This is called **emergence**. It sounds like magic: who knows what the next, bigger machine will suddenly be able to do?

But a careful 2023 study showed that many of these "sudden" jumps are **not real jumps in the machine**. They are a trick of **how the test is scored**. (Full story on the [scaling-laws page](../10-how-ai-works-today/02_scaling-laws-and-emergence.md).) Short version: if a test only gives full marks for a perfect answer and zero for anything less, then the machine's slow, steady progress stays hidden as "zero" for a long time — and then jumps to a high score all at once. The **skill grew smoothly**; only the **score** jumped. Use a fairer test that gives part-marks, and the "sudden jump" turns into a smooth slope.

Why this hurts AP1: if the gains are actually **smooth and limited**, then "just keep scaling and magic will appear" promises more than the curve really gives. *As of July 2026:* this is still argued — a few sudden jumps do survive fairer tests — but the word "emergence" is used more loosely than the evidence supports. **[Contested]**

### Stuck #3 — copying is not the same as true understanding (the deepest doubt)

This is the objection that goes at the root of the bet. Its sharpest voice is François Chollet. He argues that a scaled-up machine is a huge **memory**, not a true mind:

> "The way LLMs work is that they're basically this big interpolative memory. The way you scale up their capabilities is by trying to cram as much knowledge and patterns as possible into them."
> *(François Chollet, Dwarkesh Podcast, 2024)*

("LLMs" = large language models, the big word-guessing machines. "Interpolative memory" = a memory that answers a new question by mixing together similar things it has already seen. "Cram" = stuff in.) His point: it works great **inside** what it has seen before, and struggles with anything truly new. Then he adds the key line:

> "you are not increasing the intelligence of the system one bit. You are increasing the skill of the system ... skill is not intelligence. That's the fundamental confusion that people run into."
> *(Chollet, Dwarkesh Podcast, 2024)*

Sit with **"skill is not intelligence."** In Chollet's view, real intelligence is the ability to handle a problem you have **never seen before**, using little experience. Scaling, he says, buys more and more **stored skill** and wider coverage — but does not improve the machine's power to handle the truly new. If he is right, the mistake-count can keep falling forever and still never turn into real, general intelligence, because scale is climbing the **wrong ladder**.

AP1's reply: if you have seen a large enough part of the world, then "mixing together similar things you have seen" starts to look the same as handling new things — and the doubter has to show one real task that scale can **never** reach. **[Contested — this is a live argument, not a settled win for either side].**

### The big question under all of these — is scale *enough*?

Every doubt above is really one question, the deepest split in the field: **is scale alone enough to reach AGI, or do we also need a second, new idea** — like real step-by-step reasoning (AP2), or a built-in model of the world (AP5), or a mix of learning and logic (AP7)? The scale-believers say the gaps will close on their own as the machine grows. The doubters say some gaps are a **different kind of problem** that no amount of "more of the same" will fix.

*As of July 2026, the field has, in practice, voted "not enough alone."* The newest progress is not coming from bigger base machines. It is coming from letting the machine **think longer at answer-time** (spending extra computer power to reason step by step — this is AP2's idea) and from extra polishing after the main training. That is not AP1 losing. It is AP1 **needing a partner**. The honest status: scale is **necessary and amazingly powerful**, and **probably not enough by itself** — but "probably not enough" is a 2026 read, and this bet has proven its doubters wrong before. **[Contested — the single most important open question in AI].**

---

## ⚠️ Honesty box

- **"It is just autocomplete" is not a real argument.** Yes, the machine guesses the next word — that is the true mechanism. But Leg 1 shows that guessing well **forces** the machine to build real structure inside. So the insult misses. Still, "builds real structure" is **not** the same as "understands like a person," and that gap is a real open question. Do not use the slogan to end the argument. **[Contested]**
- **A strong track record is a reason to respect the bet — not to trust it forever.** AP1 has beaten doubters many times. And every smooth curve bends down in the end. Both are true. "It surprised us before, so it will reach AGI" is a hope, not a proof. **[Contested]**
- **The curve measures mistakes, not wisdom.** Fewer word-guessing mistakes is measured and real. Whether that equals real understanding, truth, or general intelligence is a **separate** claim the curve does not prove. Keep the solid part and the hopeful part apart. **[Established → Contested]**
- **Ask whose money is behind the claim.** "Scale is all you need" is also a sales pitch — it justifies huge spending on computer power by the companies that sell it. That does not make it false. But treat big claims from people selling the hardware with the same care you would give any sales pitch. **[be careful]**
- **Numbers age fast.** "Ran out of data," "every lab now ships a reasoning machine," and any model name are all snapshots from 2020–2026. The lasting idea is the **shape of the bet** (one simple job + scale → skills appear) and the **Bitter Lesson's logic**. The numbers around them change every few months.

---

## How to use this (if you want to direct AI work)

- **Use AP1 as your baseline. Make every rival idea beat it.** Since it has the best track record, the right question about any new idea is always: *"what does this do that just adding more scale would not?"* If the idea cannot answer that, it is not ready.
- **Look for where the gains are today, not yesterday.** In 2026, making the base machine bigger is giving smaller and smaller returns (the data wall). The gains now come from **better data, extra polishing, and thinking longer at answer-time.** Point your bets there.
- **Doubt every "it can suddenly do X" headline.** Ask one question: *how was the test scored?* A harsh all-or-nothing test invents fake "sudden jumps." A fair part-marks test usually shows a smooth slope. This one question deflates most hype.
- **Keep "needed" and "enough" apart.** Scale is **needed** — you cannot compete without it. But scale is probably **not enough** on its own — it likely needs a partner idea. Betting only on "make it bigger" in 2026 is betting against where the field actually moved.
- **What you hand to others:** running the training, the math of the curves, the hardware. **What you keep for yourself:** the judgment about how far the curve really goes, whether "copying" can ever become "true understanding," and never mistaking a hardware sales pitch for a theory of the mind.

---

## Connections

- **Keep only three things:** ① AP1 = **one simple job (guess the next word) + huge scale → real skills appear on their own**, no cleverness built in; backed by a steady measured curve and the **Bitter Lesson**. ② It has the **best track record** of any approach *and* it is now **stuck** — running out of text, an over-sold "sudden new skills," and Chollet's charge that it grows **skill, not intelligence**. ③ The question under everything: **is scale *enough*, or do we need a second new idea?** — and in 2026 the field quietly bet "not enough alone."
- **Go deeper (still visible):** [scaling laws & emergence](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the numbers and curves behind Leg 1 and Stuck #2.
- **The ideas it argues with** (now written — read them): [AP2 · reasoning](02_ap2-reasoning-and-test-time-compute.md) (think longer), [AP5 · world models](05_ap5-world-models-jepa.md) (build a model of the world), [AP8 · program synthesis / ARC](08_ap8-program-synthesis-arc.md) (Chollet's own idea — handling truly new problems). See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** The measured curve and the track record — **[Established]**. The Bitter Lesson as history — **[Likely]**. "Scale alone reaches AGI" — **[Contested, the central question]**. "Copying can become true understanding" — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP1 bet in one plain sentence, using the words *guess*, *bigger*, and *side effect*.
2. Explain the Bitter Lesson using one of Sutton's examples (chess, Go, speech, or vision). Then say why it is called *bitter*.
3. Someone says: "New skills keep appearing as we scale, so AGI is just more computers." Give the two separate replies — one from the "scoring trick" idea, one from Chollet — and say what each one attacks.
4. What is the difference between "scale is **needed**" and "scale is **enough**"? Why does the 2026 move to "think longer at answer-time" hint at the answer?
5. Give the strongest reply you can to Chollet's line "skill is not intelligence."

## Revision notes

*Newest first.*
- `rev 2 (2026-07-14)` — rewritten to the new **simplest-English + progressive-ladder** standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)): short plain sentences, no idioms or fancy words, every term glossed. Placed as the **top of the AP1 ladder**: it now **builds on** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) and [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) with a short reminder-and-link (instead of re-teaching them), so the reader climbs a staircase and is never lost. Legacy links to now-hidden modules removed. Same structure and substance as rev 1; the language got simpler and the on-ramp moved to its own rung.
- `rev 1 (2026-07-14)` — created as the AP1 pilot cluster (proof-of-standard for the approach-module method). Grounded in Sutton, Bommasani, Chollet, GPT-3, and the scaling papers; live-web freshness pass for the data wall and the "is scale enough?" status.

---
*This is the first approach page. The ideas it argues with are on the [map](../APPROACHES_TO_AGI.md). To see the numbers behind the bet, read [scaling](../10-how-ai-works-today/02_scaling-laws-and-emergence.md).*
