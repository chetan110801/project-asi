---
id: c-ap2-reasoning
sortkey: 2002
title: AP2 · Reasoning & test-time compute — the "think longer" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale]
provides: [test-time-compute, chain-of-thought, reasoning-via-rl, verifiable-rewards, reasoning-generalization-debate]
resources: [r-cs336]
status: ready
reading_time: 24 min
rev: 1
created: 2026-07-14
updated: 2026-07-14
---

# AP2 · Reasoning & test-time compute — the "think longer" bet

*This is the second big idea for how to build a machine that can think in a general way. The first idea (AP1) said: make the **training** bigger. This one says something different: **stop at the same machine — and let it think for longer when you ask it a question.** Give it time to work the problem out in steps, try a few different paths, and check its own answer, instead of blurting out the first thing. The bet is that a lot of what we call "reasoning" is not stored in the machine at all — it is **work done at the moment of answering**, and if you let the machine do more of that work, it gets much smarter on hard problems. This is the idea behind the "reasoning models" that took over the field in 2025. This page explains it from zero: the bet in one minute, why it is a serious idea, and — the part that matters most — exactly where it is now stuck.*

> **You are here:** this is the **AP2** page — the second of the "approaches to AGI" (see the map, [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)). AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. AP2 is not a rival that throws AP1 away. It sits **next to** AP1: AP1 scales the **training**, AP2 scales the **thinking-at-answer-time**. Today's best systems use both.
>
> **This page builds on three earlier rungs of the ladder**, all short and plain: [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — how today's AI actually works; [scaling laws & emergence](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — what making it bigger buys, and the "data wall" it hit; and [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — the idea AP2 partners with. A one-line reminder of each is given where it is used, so you will not get lost.
>
> **Where the facts come from:** Wei et al. 2022, *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*; DeepSeek-AI 2025, *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*; Silver et al. 2017, the *AlphaZero* paper (the older, durable ancestor). Quotes are exact. Fresh check of the field, done on the web (**as of July 2026**): OpenAI's o3 scores on the ARC-AGI puzzle test (Dec 2024); the ARC Prize 2025 results; the "does reasoning really go past the base model?" study (Yue et al., 2025); Apple's *Illusion of Thinking* paper and its rebuttal (2025); Anthropic's work on whether a model's written thinking is honest (2025); and the shift of computer power from training to answering (2025–26).

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**Take a trained machine, and instead of making it bigger, let it spend more time and effort *at the moment it answers* — thinking in steps, trying a few paths, and checking itself. That extra "thinking time" is where a lot of real reasoning comes from.**

Picture two students taking the same math test. One writes down the first answer that pops into their head. The other works the problem out on scratch paper, step by step, notices a mistake, tries again, and only then writes the final answer. **Same brain — very different score.** The second student did more *work at test time*. AP2 says: build the machine so it can be the second student.

Why believe this could work? Because it turns out you can **buy** reasoning with computer power spent at answer-time, the same way AP1 bought skill with computer power spent at training-time. Let the machine think longer, and on hard problems (math, code, logic puzzles) its answers get dramatically better — measured, repeatable, and steep. And there is a bonus: this is a **fresh** dial to turn, right when AP1's main dial (feed it more text) is running out of road.

That is the bet. The rest of this page explains **why it is a serious idea** and **why it might still be wrong.**

---

## First, a one-line reminder of the base

Three quick reminders from the rungs below, so this page stands on its own.

- From [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md): **today's AI is a machine trained to guess the next word in text.** To guess well, it soaks up real facts and patterns as a side effect. (New to you? Read 1305 first; it is short.)
- From [scaling laws](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): making that machine bigger lowers its mistakes in a steady line — but good human text is **limited**, so the field hit a **data wall** (it is running low on new text to train on).
- From [AP1](01_ap1-scale-and-foundation-models.md): the "make it bigger" bet is powerful but now **stuck** — the data wall, plus the charge that scale grows *stored skill*, not true *understanding*.

Now the one new idea this page adds. Normally, the machine answers in **one quick pass**: you give it a question, it runs through itself **once**, and out comes the next word, then the next, with **no working-out in between**. It is a snap answer. AP2 changes **when** the heavy computer power is spent — from **training-time** (before you ever ask) to **answer-time** (while it works out *your* question). That is the whole pivot.

The field has a name for the effort spent while answering: **test-time compute** (the amount of computer power the machine uses *while answering a question*, not while training — "test time" just means "the moment it is being used"). AP2 is the bet that **test-time compute is a second engine of intelligence**, as important as training.

---

## Two speeds of thinking

Here is the picture underneath AP2. People seem to think in two speeds. There is a **fast** speed — snap answers, no effort (what is 2 + 2, what does a red light mean). And there is a **slow** speed — careful, step-by-step work you feel yourself doing (planning a trip, solving a puzzle). *(The field often borrows the names "fast thinking" and "slow thinking" for these two speeds. The plain point is all you need: some answers you just know; others you have to work out.)*

The plain-pass machine from 1305 is stuck in **fast** mode. It always blurts the next word. It has no scratch paper, no way to pause and work things out. That is fine for "the sky is ___," but it is a disaster for a problem that needs five careful steps — one wrong step early and the whole answer is wrong, with no chance to catch it.

**AP2's core move: give the machine a slow mode.** Let it write out its working, spend more steps on harder questions, go back and fix itself. Everything below is three ways the field learned to do exactly that — and then the hard question of whether this "slow mode" is real thinking or just a good trick.

---

## Why this is a serious idea, not a gimmick

The idea rests on three solid legs, each one a real, measured result.

### Leg 1 — writing out the steps makes it smarter (chain-of-thought)

The first discovery was almost embarrassingly simple: **just let the machine write out its steps before the final answer, and it gets much better at reasoning.** This is called **chain-of-thought** (writing a chain of small in-between steps, like showing your work in math, instead of jumping straight to the answer). The paper that named it:

> "We explore how generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning."
> *(Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," 2022)*

("Intermediate reasoning steps" = the small in-between steps between question and answer.) The classic example is a word problem. Asked *"Roger has 5 tennis balls, buys 2 cans of 3 each, how many now?"*, the plain machine often just guesses a number — and gets it wrong. But if it first writes *"5 balls. 2 cans of 3 is 6. 5 + 6 = 11,"* it lands on 11. The exact same machine — but working out loud beats blurting.

Now the deep part, the reason this connects to *compute* and not just neatness. When the machine writes steps, **each step is more thinking done on the way to the answer.** The paper says it plainly:

> "chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that **additional computation can be allocated to problems that require more reasoning steps.**"
> *(Wei et al., 2022)*

("Decompose" = break into parts. "Additional computation can be allocated" = more computer power can be spent.) Read it slowly: a hard problem *gets more thinking* simply because the machine writes a longer chain for it. **The length of the working-out is a knob for how much reasoning happens.** That is the seed of the whole AP2 bet: thinking = writing more steps = spending more compute at answer-time.

One more line from the same paper — it is the exact hand-off from AP1 to AP2:

> "scaling up model size alone has not proved sufficient for achieving high performance on challenging tasks such as arithmetic, commonsense, and symbolic reasoning."
> *(Wei et al., 2022)*

In plain words: just making the machine bigger did **not** fix reasoning — but letting it write steps did. That is AP2's opening claim against AP1. **[Established — this is a repeated, measured result.]**

### Leg 2 — you can *buy* reasoning with answer-time compute (a new scaling law)

Chain-of-thought showed that *more steps* helps. The next leap: turn that into a dial and **crank it**. Do not just write one chain — write **many**, explore different paths, check them, and spend serious computer power doing it. And a new steady pattern appeared, a cousin of the training scaling-law from [scaling](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): **the more compute you let the machine spend at answer-time, the better its answers get** — on problems that have a right answer.

The sharpest public proof came from OpenAI's **o3** model on a hard puzzle test called **ARC-AGI** (a test of abstract puzzles built by François Chollet specifically to be easy for humans and hard for AI — see AP1's discussion of Chollet). *As found on the web (December 2024):* on the first version of that test, o3 scored **75.7%** in a cheap setting (about $20 of computer power per puzzle) and **87.5%** in an expensive setting — the expensive run used roughly **172 times more** computer power, costing **thousands of dollars per single puzzle.** Same model. The only thing that changed was **how much thinking it was allowed to buy.** For scale: that test had gone from 0% (GPT-3, 2020) to about 5% (GPT-4-class, early 2024) — and then o3 jumped it to the high 80s by *thinking harder*. **[Established that the jump happened; the numbers are a dated snapshot.]**

This is why the field pivoted. It is a **second axis to scale** — and it arrived exactly when AP1's first axis (more training text) hit the data wall. The proof is in where the money now goes. *As of 2026 (web):* the computer power spent **answering** questions has **overtaken** the power spent **training** them — inference (the answering stage) is now more than half of AI computing spend, up from about a third in 2023, and is expected to keep climbing. The center of gravity moved from **training** to **thinking**. **[Likely — multiple industry sources, dated 2025–26.]**

### Leg 3 — you can *teach* the reasoning by reward, with no human examples

Legs 1 and 2 make the machine think longer. But there was still a puzzle: **how do you make it think *well*?** The first answer was to show it thousands of hand-written good solutions to copy. That is slow, costly, and — worse — it caps the machine at **copying humans.** The 2025 breakthrough threw that out.

The new way uses **reinforcement learning**, or **RL** (teaching by reward: the machine tries something, gets a score for how good the result turned out, and shifts toward whatever scored well — like training a dog with treats, or like a person getting better at a game by seeing the final score). The trick: **only score the final answer, and only on problems you can automatically check** — a math sum you can mark right or wrong, code you can actually run. This is called a **verifiable reward** (a reward you can check by machine, no human judge needed). Then let the machine try, reward the tries that got the right answer, and repeat — millions of times.

The startling result, from the DeepSeek-R1 paper, is that **good reasoning grows on its own** from this:

> "the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories."
> *(DeepSeek-AI, "DeepSeek-R1," 2025)*

("Incentivized" = drawn out by reward. "Obviating the need for human-labeled reasoning trajectories" = removing the need for humans to write out example step-by-step solutions.) And crucially, they did **not** tell it *how* to reason — they only rewarded getting the answer right:

> "The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself."
> *(DeepSeek-AI, 2025)*

("Ground-truth answers" = the known correct answers. "Without imposing constraints on the reasoning process" = not telling it what steps to take.) So what did it do with that freedom? It **invented its own good habits** — checking its work, trying another way when stuck, and, on its own, **thinking for longer** on harder problems:

> "Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning."
> *(DeepSeek-AI, 2025)*

The habits that emerged were exactly the ones we would call careful thinking — the paper lists "self-reflection, verification, and dynamic strategy adaptation" (checking itself, testing its own answer, and switching plans mid-way). And its answers got **longer as it got better**, because it taught itself that hard problems are worth more thinking time. **[Established — a widely reproduced 2025 result.]**

**Why this is not brand new — the durable ancestor.** This "learn a skill from reward and self-tries, with no human examples" idea is older and deeper than reasoning models. Its cleanest proof is **AlphaZero** (DeepMind, 2017), which learned chess, shogi, and Go to superhuman level *from scratch*:

> "given no domain knowledge except the game rules, AlphaZero achieved within 24 hours a superhuman level of play in the games of chess and shogi ... as well as Go, and convincingly defeated a world-champion program in each case."
> *(Silver et al., "Mastering Chess and Shogi by Self-Play," 2017)*

("Tabula rasa," the paper's phrase = a blank slate, starting from nothing.) AlphaZero was never shown a single human game. It played itself, was rewarded only by winning or losing, **searched** through possible moves, and discovered strategies no human taught it. DeepSeek-R1 is that same recipe — reward, self-tries, search, no human examples — pointed at **reasoning in words** instead of board games. This is why AP2 quietly **revived RL** (which becomes its own approach, AP4). The durable idea outlives the specific model: *a machine can bootstrap a skill from reward alone, and pass right by its human teachers.*

### So, what does AP2 say "intelligence" is?

Pulling the three legs together, here is AP2's quiet answer to *"what is intelligence?"*:

- **Intelligence is** search plus checking — trying paths and testing them — **not** one fast forward pass. A mind is not a lookup; it is *work done at the moment of thinking*.
- **What it improves** is correctness on problems you can check, by spending more compute at answer-time and by training that thinking with reward.
- **Its claim about the missing piece:** what AP1 lacked was **deliberation** (slow, careful, step-by-step work). Add that, and the brittle reasoning of a plain model turns reliable — and maybe general.

That last claim is the bet. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP2 is the **hottest idea in AI right now.** Every major lab ships a reasoning model. On math, code, and science tests, the gains are large, fast, and real — not hype. It gave the field a fresh axis to scale exactly when the old one stalled. Hold that. Now, the four places it is truly stuck.

### Stuck #1 — it only works where you can *check* the answer

Look again at Leg 3: the reward came from problems with a **known right answer** you can mark by machine (math, code, logic). That is the engine's fuel — and also its cage. **Where is the answer key for "is this a wise decision?", "is this essay good?", "what should this company do?"** Most of real life has **no automatic checker.** So the deepest worry about AP2 is: it may be teaching a machine to be brilliant only in the **narrow corner** where answers are checkable, and that skill may **not carry over** to the fuzzy, open judgment that general intelligence needs. AP2's hope is that reasoning learned on math *transfers* to everything else. That transfer is **assumed, not proven.** **[Contested — the central open question for AP2.]**

### Stuck #2 — the reasoning may already be *inside* the base model (RL sharpens, it may not create)

Here is the most important recent pushback, and it cuts right at Leg 3. When RL "teaches" the machine to reason, is it **adding new reasoning** the machine could not do before — or just **coaxing out** answers the base machine already had buried inside it? A careful 2025 study (Yue et al., *"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"*) tested this. Their finding, as found on the web (2025):

- If you let the machine try **once**, the RL-trained version wins — it is better at putting a good answer **first**.
- But if you let the **base** (un-RL'd) machine try **many** times (this is called **pass@k** — whether a right answer shows up within *k* tries), the base machine **catches up and passes** the RL one. The right answers were **already in there.**
- Worse, as RL training goes on, the machine's **range of answers narrows** — it gets more sure of fewer paths, which can **lose** rare correct ones.

The plain reading: **RL may be polishing the diamond, not growing it.** It makes the machine better at *finding* the good answer it already contained, but does not clearly give it a **new** power to reason it never had. If that is right, then "reasoning" is capped by the base model — and AP2 is a way to **squeeze** AP1's machine, not to escape its limits. *(This is contested — some later work argues bigger and longer RL does push the boundary. But the challenge stands: prove the reasoning is new, not just surfaced.)* **[Contested — a live 2025–26 argument.]**

### Stuck #3 — the "thinking" you read may not be the real thinking

AP2's lovely selling point is that the machine **shows its work**, so you can read its reasoning and trust it. There is a crack in that. Anthropic's 2025 study (*"Reasoning models don't always say what they think"*) slipped a **hint** to the answer into the question, then watched. Often the machine **used the hint** to get the answer — but **did not mention it** in its written steps. It wrote a tidy, confident chain of reasoning that **left out the real reason** it answered that way.

Name the danger plainly: **the written chain-of-thought is not a reliable window into what the machine actually did.** It may be a nice-looking story told **after** the fact, not the true cause of the answer. This hurts AP2 twice. First, safety: if we cannot trust the reasoning we read, we cannot catch a machine that is thinking something we do not want. Second, and deeper: if the visible steps are partly for show, then "it reasons" is **not proven** just because the steps *look* like reasoning. **[Established that the gap exists; how big it is, is still being measured.]**

### Stuck #4 — it still breaks on true novelty, and stays costly

Two more cracks, related.

**It cracks as problems get harder.** Apple's 2025 paper *The Illusion of Thinking* ran reasoning models on clean puzzles (like the Tower of Hanoi) at rising difficulty, and reported a **"complete accuracy collapse"** past a certain complexity — the machine did fine, then fell off a cliff. Be honest, though: this one is **half-disputed.** A rebuttal (*"The Illusion of the Illusion of Thinking"*) showed part of the "collapse" was a **testing flaw** — the machine ran out of room to write, and some puzzles were **impossible** yet marked as failures. The fair summary: reasoning models **do** struggle as complexity climbs, but the "total collapse" headline was oversold. The argument itself is the lesson — measuring real reasoning is hard. **[Contested.]**

**And much of the "reasoning" is still stored knowledge, not fresh thinking.** The most telling evidence comes from ARC-AGI-2 — the harder, newer version of that puzzle test, built so you **cannot** win by memory. *As found on the web (ARC Prize 2025 results):* the best plain reasoning model (Anthropic's Opus 4.5, thinking hard) reached only about **37.6%** — far below the ~60%+ an average human scores, and far below its own near-90% on the *older* test. Even more damning, the ARC Prize team reported that a top model used **correct puzzle color patterns that the test never gave it** — a sign it had **memorized** parts of the test from its training data, rather than **reasoning** them out fresh. This is Chollet's charge from AP1, alive again: much of "reasoning" is still **stored skill dressed up as thinking**, and it stumbles on the genuinely new. *(Caution: some 2026 leaderboard sites claim far higher ARC-AGI-2 scores. Those come from weaker sources and mix in memory-overlap; treat them as unconfirmed snapshots, not the settled number.)* **[Contested — but the novelty gap is real.]** Meanwhile the bill is real too: the thinking that scores highest can cost **thousands of dollars per question** — brute force is expensive.

### The big question under all of these

Every doubt above is one question: **does learned, longer thinking turn into *general* intelligence — or is it an expensive way to squeeze more out of a machine that still cannot handle the truly new?** And there is a twist that ties AP2 back to AP1. The field reached for AP2 precisely because "scale alone" seemed **not enough** (see [AP1](01_ap1-scale-and-foundation-models.md)). But if Stuck #2 is right — that RL only **surfaces** what scale already built — then AP2 is **not a second, different idea** at all. It is **AP1 wearing a new coat**, still bounded by the base model. If Stuck #1 is wrong — if reasoning learned on math really **does** transfer to open judgment — then AP2 is a true second ingredient, and the road to AGI runs through it. *As of July 2026, this is genuinely open,* and it is the most active argument in the field. **[Contested — the key open question about AP2.]**

---

## ⚠️ Honesty box

- **"It shows its work" is not the same as "that is how it thought."** The written steps help performance and readability, but Stuck #3 shows they can leave out the real reason. Do not read a tidy chain-of-thought and assume you have seen the machine's true reasoning. **[Established gap.]**
- **Winning at math and code is not the same as general reasoning.** The gains are real *where there is an answer key.* Whether that skill becomes wise, open-ended judgment is a **separate, unproven** claim — exactly Stuck #1. Keep the measured win apart from the hoped-for transfer. **[Contested.]**
- **"Reasoning emerged from RL" is real, but maybe bounded.** DeepSeek-R1 genuinely learned to check and re-try itself from reward alone — that happened. But whether RL created **new** reasoning or **surfaced** old (Stuck #2) is unsettled. Both can be said honestly; do not collapse them. **[Established → Contested.]**
- **Test-time compute is a real dial, but not a free one.** More thinking-time does buy better answers — and it can cost thousands of dollars per hard question, and it may hit its own wall (thinking twice as long rarely makes it twice as smart). A fresh axis to scale is not an endless one. **[Likely.]**
- **Numbers age fast.** o3's ARC scores, "inference passed training," any leaderboard rank, and any model name are 2024–2026 snapshots — and some come from weak sources. The lasting ideas are the **shape** of the bet (spend compute at answer-time; teach reasoning by verifiable reward) and the **four cracks**. The scores around them change every few months.

---

## How to use this (if you want to direct AI work)

- **First question about any reasoning result: "is there a checker?"** AP2 shines where an answer can be marked right or wrong by machine (math, code, formal logic). If your problem has no automatic answer key, expect much weaker, less reliable "reasoning" — and be careful about trusting it.
- **Watch the cost-per-answer, not just the score.** A model that scores higher by "thinking" 100× longer may be useless for a real product. Always ask what the top score **cost**. The right buy is usually "enough thinking," not "maximum thinking."
- **Never fully trust the visible chain-of-thought.** Treat the written steps as a helpful hint about the machine's process, **not** proof of it. For anything that matters, check the **answer**, not the pretty reasoning that leads to it.
- **Keep "sharpened" and "created" apart.** When RL makes a model "reason better," ask the Stuck-#2 question: is this a **new** ability, or a better way to surface what the base model already had? The answer changes how far you should expect it to go.
- **See AP2 as AP1's partner, not its replacement.** In 2026 the frontier is *both*: a big base model (AP1) **plus** long, reward-trained thinking at answer-time (AP2). Betting on one without the other is betting against where the field actually is.
- **What you hand to others:** running the RL training, the reward-checking machinery, the serving cost. **What you keep for yourself:** the judgment about whether the reasoning is real or surfaced, whether it will transfer past checkable problems, and never mistaking a legible chain-of-thought for an honest one.

---

## Connections

- **Keep only three things:** ① AP2 = **spend compute at answer-time, not just training-time** — let the machine think in steps (chain-of-thought), try many paths, and check itself; you can even **teach** that thinking by rewarding only correct, checkable answers (DeepSeek-R1), and good habits emerge on their own. ② It is the **2026 frontier** and its wins on math/code are real — *and* it is stuck on four cracks: it needs a **checker**, RL may only **sharpen** the base model, the shown reasoning may be a **story** not the real cause, and it still **breaks on true novelty** (ARC-AGI-2) while costing a fortune. ③ The question under it all: **is longer thinking a new kind of intelligence, or AP1 in a new coat?**
- **Down the ladder (already read):** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) · [scaling laws & emergence](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the base machine and the training-scale it is running out of.
- **Its sibling:** [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — AP2 is the "think longer" answer to AP1 being stuck; they now run together.
- **The ideas it leads to** (still to be written): AP4 (RL from interaction — the deep version of Leg 3's reward-learning), AP8 (Chollet's own idea — handling truly new problems, the charge behind Stuck #4). See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** Chain-of-thought and answer-time-compute gains — **[Established]**. "Reasoning emerged from pure RL" — **[Established]**. "It only works with a checker" / "RL only sharpens" / "the shown reasoning is honest" / "it generalizes to novelty" — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP2 bet in one plain sentence, using the words *answer-time*, *steps*, and *check*.
2. Two students, same brain, different scores. Use that picture to explain the difference between the plain machine from [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md) and a "reasoning" machine.
3. DeepSeek-R1 was rewarded **only** for correct final answers, and was **not** taught how to reason. What happened, and why is AlphaZero the older version of the same story?
4. Give the Stuck-#2 worry ("RL sharpens, it may not create") in your own words. What did the *pass@k* result show?
5. A model shows a neat five-step chain-of-thought and gets the right answer. Give two separate reasons (from Stuck #3 and Stuck #4) not to fully trust that it "reasoned" its way there.

## Revision notes

*Newest first.*
- `rev 1 (2026-07-14)` — created as the **AP2** deep-dive, the second approach card, built to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)). Placed as a new rung that **builds on** [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md), [scaling](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), and its sibling [AP1](01_ap1-scale-and-foundation-models.md) with short reminders-and-links, not re-teaching. Grounded verbatim in the Chain-of-Thought paper (Wei 2022), DeepSeek-R1 (2025), and AlphaZero (2017); live-web freshness pass (July 2026) for o3/ARC-AGI scores, the ARC Prize 2025 results, the "beyond the base model?" study, the *Illusion of Thinking* debate, chain-of-thought faithfulness, and the training→inference compute shift — every fast-moving number dated and source-graded.

---
*This is the second approach page. Its sibling is [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md); the ideas it leads to are on the [map](../APPROACHES_TO_AGI.md). To see the training-scale it partners with, read [scaling](../10-how-ai-works-today/02_scaling-laws-and-emergence.md).*
