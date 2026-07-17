---
id: c-test-time-compute-machine
sortkey: 5009
title: AP2 · Deep dive — how a machine actually "thinks longer": the four ways to spend answer-time compute, and why verification (not thinking) is the bottleneck
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-ap1-scale, c-ap2-reasoning]
provides: [sequential-vs-parallel-test-time, self-consistency-majority-vote, coverage-vs-selection, repeated-sampling-power-law, verification-easier-than-generation, reward-model-orm-prm, process-vs-outcome-supervision, tree-of-thoughts-search, mcts-propose-evaluate, compute-optimal-test-time, overthinking-diminishing-returns, rlvr, test-time-compute-vs-test-time-training, verifier-is-the-bottleneck, self-verification-unreliable, alphazero-analogy-limits]
resources: [r-cs336]
status: ready
reading_time: 37 min
rev: 1
created: 2026-07-17
updated: 2026-07-17
---

# AP2 · Deep dive — how a machine actually "thinks longer": the four ways to spend answer-time compute, and why verification (not thinking) is the bottleneck

*This is a **deep dive** past the [AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md). The card gave you the bet — **spend computer power at answer-time, not just training-time**: let the machine write out its steps, try a few paths, and check itself. And it gave you the headline curve: **more answer-time compute → better answers**, a fresh dial to turn. But it treated "think longer" as **one dial** and showed you **one rising line**. That is not what is actually happening inside. "Spend more compute at answer-time" is not a single machine — it is a **family** of them, and they work in fundamentally different ways: think **longer** in one chain, or think in **many** chains and pick one, or search a **tree** of half-thoughts. This page opens all of them. And it finds the thing the single rising line hides: the machine's real problem is **not** producing a good thought — throw enough attempts at a hard problem and a right one almost always appears — it is **telling which of its thoughts was the right one.** The whole "think longer" bet, opened up, turns out to rest on a quieter power the card never named: the power to **verify.** Everything the card already said — chain-of-thought, the o3/ARC-AGI scaling numbers, verifiable-reward RL, DeepSeek-R1, AlphaZero, the four cracks — is referenced, not repeated.*

> **You are here:** a **deep-dive module** — reading group **⑤**, the optional layer that branches off the main staircase. This one hangs off **[AP2 · reasoning & test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)**. *Read the AP2 card first* — this page assumes it and opens the machine under its "think longer" dial. It is the first deep dive off AP2, the hottest idea in AI as of 2026, and the one whose central mechanism — spending compute to *find* a right answer — is most worth seeing from the inside. It is also the page that **[AP1's deep dive](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) pointed at**: that page showed the *scaling-law shape* of the new answer-time axis and said the *mechanism* lives here. Here it is.
>
> **What you already have (a one-line reminder each, then we build — none of it is re-taught here):** from **[guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md)** — a language model answers in **one quick pass**: text in, next word out, no working-out in between. From the **[AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)** — the **bet** (spend compute at answer-time); **chain-of-thought** (writing the in-between steps makes it smarter, and the length of the working-out is a knob for how much reasoning happens — Wei et al. 2022); the **test-time-compute scaling curve** (o3 on ARC-AGI: same model, far higher score when allowed to buy more thinking; and inference compute overtaking training compute); **verifiable-reward RL** (reward only correct, checkable final answers, and good reasoning habits emerge on their own — DeepSeek-R1); the **AlphaZero** ancestor (learn a skill from reward + self-play + **search**, no human examples); **fast vs slow thinking**; and the four cracks — needs a **checker**, RL may only **sharpen** not create, the shown reasoning may be an **after-the-fact story**, and it **breaks on true novelty** while costing a fortune. **New here:** the *machine* under "think longer" — **sequential vs parallel** spending, **coverage vs selection**, the **verifier** (and why grading each step beats grading the end), **search / Tree of Thoughts**, and the **compute-optimal** science of how much to spend.
>
> **Where the facts come from:** written, checkable sources, each quote corpus- or web-verified as exact. The **parallel machines** — Wang et al., *Self-Consistency* (2022); Yao et al., *Tree of Thoughts* (2023); Brown et al., *Large Language Monkeys* (2024, repeated sampling). The **verifier** — Lightman et al., *Let's Verify Step by Step* (2023, process vs outcome rewards). The **compute-optimal** finding — Snell et al. (2024). The 2026 frontier (overthinking / diminishing returns, imperfect-verifier limits, RLVR) is checked on the web (**as of July 2026**) and dated where it moves. The card's own grounding — Wei, DeepSeek-R1, AlphaZero, the o3/ARC numbers — is *pointed at*, not re-quoted; the RL *optimiser* that trains all this is [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)'s home, pointed at, not opened.

---

## In one minute

The card showed you one dial marked "think longer" and one line going up. Here is what that hides — and each hidden thing is a place the bet is quietly stuck.

1. **"Think longer" is not one machine — it is at least three.** You can think **longer** (one long chain of reasoning), think **wider** (many separate attempts, then pick one), or **search** (a tree of half-thoughts you grow and prune). These spend compute in completely different ways and hit completely different walls. The card's single rising curve is really several curves stacked on top of each other.

2. **Generating a right answer is nearly a solved problem; *finding* it is not.** The startling measured fact of test-time compute: on a hard problem, if you let the machine try hundreds of times, one of those tries is very often correct — **coverage** climbs and climbs with more attempts. But that only helps if you can **tell which try was right.** With a perfect checker (run the code, mark the maths) you can, and the machine soars. Without one, you fall back on voting or a *learned* judge — and those **plateau.** The right answer sits in the pile, unfound.

3. **The whole thing runs on verification — a power the card never named.** Why can spending compute at answer-time buy correctness at all? Because for many problems, **checking** an answer is far easier than **producing** one. That asymmetry is the hidden engine. It is also the hidden ceiling: where checking is easy (maths, code, games) test-time compute is close to a superpower; where checking is itself hard or impossible (judgment, taste, real-world action) the machinery collapses back to a bigger pile of unsorted guesses.

4. **The dial is optimisable, and it bends.** More thinking is not free and not endless. There is a **compute-optimal** amount that depends on how hard the problem is — and past it, extra thinking wastes money or, worse, makes the answer *worse* ("overthinking"). "Just think longer" runs into its own arithmetic, exactly as "just make it bigger" did.

The card asked whether longer thinking is a new kind of intelligence or "AP1 in a new coat." This page reframes the question mechanically: **the power of the "think longer" bet is bounded almost entirely by how well the machine can check itself — so the frontier of reasoning is not really about thinking longer at all. It is about learning to verify.**

---

## One line of base, then we build

Two reminders, because the whole page turns on them — and both are owned by other pages, so here they are *pointed at*, not re-taught.

- The [AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) established **that** answer-time compute buys reasoning: chain-of-thought helps, the length of the working-out is a compute knob, and there is a rising curve (o3 on ARC-AGI). This page never re-argues *that* curve exists. It opens the **machines that produce it** — and shows the curve is really a stack of different curves with different ceilings.
- The [AP1 deep dive](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) opened the *training* scaling law and, at its end, named a **new axis** — compute spent thinking at answer-time — but drew only its *shape* and said the *mechanism* was AP2's home. **This is that home.** And it repays the debt in kind: just as AP1's page found a **compute-optimal** split between model size and data, this page finds a compute-optimal split between *bigger model* and *more thinking* — the same idea, one level out.

One framing to carry the whole way, and it organises everything below. Every method on this page is an answer to a single question: *the machine can produce many candidate thoughts — so how do you spend compute to end up holding the **right** one?* That splits cleanly into two sub-problems, and keeping them apart is the key that unlocks the whole subject:

- **Generation** — produce candidate answers (or candidate reasoning steps). Make more, make them more varied, make them longer.
- **Selection** — from the candidates, identify the correct one.

The card's "think longer" was almost entirely about **generation** — write more steps. The hard, hidden half is **selection** — and, as we will see, selection is where the bet lives or dies. One more distinction to pin down now, because the words are easy to confuse: this page is about **test-time compute** — spending more computer power *while answering*, with the model's internal numbers **frozen**. That is different from **test-time training** *(updating the model's weights on the spot for this one problem — the [AP8 solver deep dive](02_ap8-deep-dive-solver-mechanisms.md)'s home)*. Frozen weights, more thinking: that is the whole of this page.

---

## Part 1 — two axes: think *longer* (sequential) vs think *wider* (parallel)

Start with the split the card's single dial hid. There are two fundamentally different directions to spend answer-time compute, and they are different machines.

**The sequential axis — one longer chain.** The first way is the one the card mostly pictured: let the model produce a **longer chain of thought** — more reasoning steps, in one continuous stream, revisiting and correcting itself as it goes. This is what a 2025-era reasoning model does when it "thinks" for thirty seconds before answering: it generates a long internal monologue, one token after the next, and the extra tokens *are* the extra compute. It is **depth** — one line of reasoning, pushed further. The card owns why this helps (chain-of-thought; length as a compute knob — Wei et al., pointed at). What matters here is only that it is **one** of the axes, not the whole of it.

**The parallel axis — many separate attempts.** The second way is completely different: instead of one long think, run **many independent** thinks and combine them. The cleanest version is **self-consistency** (Wang et al., 2022). Rather than take the single most-likely chain, sample a whole *set* of different chains and see which final answer they agree on:

> "It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths."
> *(Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models," 2022)*

Unpack the two glosses that matter. **"Greedy"** decoding *(greedy = at each step just take the single highest-probability next word — the model's one default answer)* gives you one chain. **Sampling** *(sampling = letting the model roll the dice and pick among likely next words, so you get a **different** chain each run)* gives you many. **"Marginalizing out the … paths"** is a fancy phrase for a simple act: **ignore how each chain got there, look only at its final answer, and take the answer that shows up most** — a majority vote. Why on earth should a majority vote of a model's own guesses be better than its single best guess? The paper gives the intuition, and it is the heart of the parallel axis:

> "Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer."
> *(Wang et al., 2022)*

Read it slowly. There is usually **one** right answer but **many** roads to it — and many *more* wrong roads, each going somewhere different. So the **right** answer is the one many independent chains **converge** on, while the wrong answers scatter. Voting exploits that: truth agrees with itself; errors disagree. This is **width** — many lines of reasoning, run in parallel, resolved by agreement.

**Two different machines, two different walls.** Sequential deepens a single line of thought (and hits a wall when the line goes wrong early, or when more length stops helping). Parallel widens the search across many lines (and hits a *different* wall: once you have many candidate answers, **how do you pick?**). Self-consistency's answer — majority vote — is only the simplest possible pick, and it works only when the right answer is the *most common* one. That is often false on the hardest problems, where the model is confidently wrong in the same way many times. So the parallel axis immediately forces the question the card never asked, and it is the question the rest of this page is about: **selection.** Real systems, by the way, mix both axes — long chains *and* many of them — but the two never stop being distinct dials with distinct ceilings.

---

## Part 2 — coverage vs selection: the right answer is in the pile; can you find it?

Here is the single most clarifying result in all of test-time compute, and it splits the card's one rising curve cleanly in two. It comes from a 2024 study memorably titled *Large Language Monkeys* — the name nods at the "enough monkeys at typewriters" image. The idea: take a problem, sample the model not a handful of times but **hundreds or thousands** of times, and measure **coverage** *(coverage = the fraction of problems for which **at least one** of your many samples is correct — "did a right answer appear *anywhere* in the pile?")*. The finding:

> "coverage -- the fraction of problems that are solved by any generated sample -- scales with the number of samples over four orders of magnitude."
> *(Brown et al., "Large Language Monkeys," 2024)*

> "the relationship between coverage and the number of samples is often log-linear and can be modelled with an exponentiated power law"
> *(Brown et al., 2024)*

*("Four orders of magnitude" = from one sample up to about ten thousand. "Log-linear … power law" = a steady, predictable climb, the same well-behaved shape as the [training scaling laws](07_ap1-deep-dive-anatomy-of-a-scaling-law.md).)* In plain words: **keep sampling and the odds that a right answer shows up somewhere keep rising, reliably.** The concrete example is startling — a *weaker* model with many tries beats a *stronger* model with one:

> "the fraction of issues solved with DeepSeek-Coder-V2-Instruct increases from 15.9% with one sample to 56% with 250 samples, outperforming the single-sample state-of-the-art of 43%."
> *(Brown et al., 2024)*

Sit with that. On a real coding benchmark, one shot solved 16%; **250** shots contained a correct fix for **56%** — beating a model that scored 43% in a single shot. So on the **generation** side, test-time compute is close to a solved problem: throw enough darts and one hits the board. If this were the whole story, general intelligence would be a sampling budget.

It is not the whole story, because of the word "**contained**." Coverage says a right answer is *in the pile*. It does **not** say you can *find* it. And finding it is a separate problem with a much lower ceiling. The same paper is blunt about the two regimes:

- **When you have an automatic checker** — you can run the generated code against tests, or check the maths answer against the known result — you *can* pick the winner: try 250, keep the one that passes. Coverage becomes accuracy. **This is exactly why code and maths are where test-time compute looks miraculous.**
- **When you do not** — most of the world — you must guess which sample is right, using majority vote or a *learned* judge, and here the wheels come off:

> "In domains without automatic verifiers, we find that common methods for picking from a sample collection (majority voting and reward models) plateau beyond several hundred samples and fail to fully scale with the sample budget."
> *(Brown et al., 2024)*

There it is, in one sentence: **generation scales; selection plateaus.** You can put the right answer in the pile a thousand times over, and still not be able to point to it. So the card's Leg-2 curve — "more compute → better answers" — is secretly **two** curves: a gorgeous, power-law **coverage** curve (generation) and a flatter, quickly-capped **selection** curve (verification). The gap between them — between "a right answer exists in the pile" and "we can identify it" — is where the entire bet is won or lost. And that gap is set by one thing: **how good is your verifier?**

---

## Part 3 — the verifier: the hidden engine (and why grading each step beats grading the end)

Step back and ask the question Part 2 forces: *why does spending compute at answer-time buy correctness at all?* The deep answer, the one that makes the whole approach possible, is an **asymmetry**: for a huge class of problems, **checking** a candidate answer is far **easier** than **producing** one. It is easier to verify a completed jigsaw than to assemble it; easier to check a proof than to find it; easier to run a program against tests than to write a correct one. When verification is cheaper than generation, a beautiful trade opens up: don't struggle to be right on the first try — instead, **generate many cheap candidates and spend your compute checking them.** That asymmetry is the engine under every method on this page.

It is also, exactly, the **AlphaZero** connection the card named but did not open. A search-based game player is two parts working together: a **generator** that proposes candidate moves, and an **evaluator** that scores how good a resulting position is. It spends compute by **proposing and evaluating** many futures and keeping the promising ones — the method known as **MCTS** *(Monte Carlo Tree Search — repeatedly: pick a promising branch, extend it a step, estimate how good that leads, and pass that estimate back up the tree to guide the next pick)*. Test-time compute in language is that **same** propose-and-evaluate loop, pointed at reasoning steps instead of chess moves. Which means the card's lovely AlphaZero ancestor is not just inspiration — it is the literal template: **generate candidates, evaluate them, keep the good ones, repeat.** Hold that; its limits become engine-crack #4.

So the whole game reduces to: **get a good evaluator.** Where the world hands you a perfect one for free — a compiler, a maths checker, a game's rules — you are in paradise, and test-time compute soars. Where it does not, you must **build** one: train a model whose only job is to judge answers. This is a **reward model** *(a model trained to score how good a candidate answer or step is — a learned stand-in for the missing checker; it is [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)'s tool, used here at answer-time to **select**, not to train)*. And there is a crucial design choice in *what* it grades, pinned down by Lightman et al. (2023). You can grade only the **final answer**, or grade **each step of the working**:

> "we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step."
> *(Lightman et al., "Let's Verify Step by Step," 2023)*

These build two kinds of judge: an **outcome reward model (ORM)**, which sees a whole solution and rates the end, and a **process reward model (PRM)**, which rates the reasoning **step by step.** The finding is decisive:

> "process supervision significantly outperforms both forms of outcome supervision at all data collection scales."
> *(Lightman et al., 2023)*

Why does grading the steps beat grading the end? Two reasons, both mechanical. First, a step-grader **catches the reasoning going wrong at the moment it goes wrong**, instead of noticing only that the final number is off — it localises the error. Second, and more important for *selection*: a step-grader gives a signal at **every node** of a search, so it can steer the compute toward promising partial thoughts and prune bad branches early, rather than only ranking finished answers. A PRM turns the propose-and-evaluate loop from "generate whole answers and rank them" into "grow the good reasoning and kill the bad reasoning as you go." As of 2026, PRM-guided search is the state of the art of *spending compute to find the right thought.* (The paper's headline: its process-supervised model "solves 78% of problems from a representative subset of the MATH test set.")

But notice the crack already opening, which we return to at the end: the PRM is **itself a model**, trained on judgments, and often it is a *sibling* of the very model generating the thoughts. A judge that shares the generator's blind spots will confidently approve the generator's confident mistakes. The card's Stuck #3 — the written reasoning can be an after-the-fact story, not the true cause — is the same fault seen from here: **the thing checking the thinking is no more trustworthy than a model.** We have not escaped the model's fallibility; we have **added a second copy of it** and asked it to grade the first.

---

## Part 4 — search: Tree of Thoughts, and structure over the candidates

Between "one long chain" (Part 1's sequential axis) and "many independent chains" (Part 1's parallel axis) sits the richest way to spend compute: **search** — build a **tree** of partial thoughts, evaluate branches with a judge (Part 3), expand the promising ones, and back out of dead ends. The paper that named this for language models is **Tree of Thoughts** (Yao et al., 2023):

> "[It] enables exploration over coherent units of text ("thoughts") that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices."
> *(Yao et al., "Tree of Thoughts," 2023)*

Read the verbs, because they are the machinery: **exploration** (try several next-steps, not one), **self-evaluating** (a judge scores each partial thought — Part 3), **looking ahead** (estimate where a branch leads before committing), **backtracking** (abandon a bad branch and return to a better one). A plain chain-of-thought cannot do the last two at all — it commits to each step and marches on; one early wrong turn and the whole thing is lost (the card's own point about brittle single chains). A *tree* can un-commit. The payoff is large where a problem genuinely needs search:

> "in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, [Tree of Thoughts solved far more]"
> *(Yao et al., 2023)*

*(Game of 24 = a little puzzle: use four given numbers and arithmetic to make 24 — the kind of thing where you must try, fail, and back up.)* Four percent to a large majority, on the **same** model, purely by spending answer-time compute as a **tree** instead of a **line.**

Now unify the whole picture. Sequential, parallel, and search are not three unrelated tricks — they are **three shapes of the same activity**: generate candidate thoughts and select among them, differing only in *structure*.

- **Sequential** = a **path** (one line of thought, extended).
- **Parallel** = a **fan** (many independent lines, resolved by a vote or a judge).
- **Search** = a **tree** (lines that branch, get scored, and get pruned).

All three spend compute to move probability toward a right answer; all three, the moment they must *choose*, lean on the **verifier** of Part 3. And this is where the AlphaZero template both illuminates and misleads. AlphaZero's tree search worked spectacularly because Go handed it two gifts for free: a **perfect simulator** *(the exact rules — you always know precisely what the board becomes after a move)* and a **clean reward** (win or lose, no ambiguity). Its evaluator could be trained to near-perfection against ground truth. Open-ended reasoning has **neither**: there is no perfect simulator of "where this line of argument leads," and no clean win/lose signal for "is this essay wise?" So the search has to run on a **learned, fallible** evaluator — the PRM — and it inherits every weakness of that model. The template transfers; the *guarantee* does not. Hold that for the judgement.

---

## Part 5 — the compute is optimisable, and the curve bends (2024–2026)

The last piece: how *much* to spend, and where the whole thing runs out of road. Two findings, both crucial, both recent.

**There is a compute-optimal amount, and it depends on the problem.** More is not simply better. Snell et al. (2024) studied how to allocate a fixed answer-time budget and found the sharp fact:

> "the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt."
> *(Snell et al., 2024)*

Easy questions want a little sequential refinement; genuinely hard ones want broad parallel search — and matching the method to the difficulty pays off enormously. Allocating **adaptively per prompt** (a "compute-optimal" policy) beat the naive approach by a wide margin:

> "Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline."
> *(Snell et al., 2024)*

And the headline that ties this page back to AP1's deep dive:

> "test-time compute can be used to outperform a 14x larger model."
> *(Snell et al., 2024)*

That is the **test-time twin of Chinchilla**: for a fixed compute budget, there is a best *split* — not between model-size and data (AP1's page), but between **a bigger model** and **more thinking**, and between **sequential** and **parallel** thinking. Under the right conditions, a small model that thinks well beats a big model that thinks once. Reasoning, like training, has an optimisation problem with a real answer — and the answer is not "spend the maximum."

**Past a point, more thinking stops helping — and can hurt.** By 2026 the diminishing returns are measured and named. On many tasks, accuracy climbs with the thinking budget and then **flattens** — extra reasoning tokens buy almost nothing past a modest budget. Worse, researchers documented **"overthinking"**: with too long a leash, a model will **talk itself out of a correct answer** it had already reached, and end up wrong. And the parallel axis has its own ceiling from Part 2/3: without a good verifier, selection plateaus, and — a 2026 refinement — an **imperfect verifier actively causes** the diminishing returns, because as you sample more, the judge's **false positives** (wrong answers it mistakenly approves) pile up and drown the gains. So both axes bend: sequential saturates and can reverse; parallel is capped by the verifier's error rate. *(As of 2026-07; the exact token-budget where gains vanish is task-dependent and a moving snapshot — the durable fact is that both curves have a knee, not that any particular number is fixed.)*

**Where the training side stands, in one line.** The 2026 umbrella name for the card's Leg 3 — teach reasoning by rewarding only correct, checkable answers — is **RLVR** *(reinforcement learning with verifiable rewards)*, and it is the field's cornerstone method for building reasoning models. Its *optimiser* (how the weights are actually nudged — GRPO and its kin) is [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)'s home, pointed at, not opened here. What belongs on **this** page is only the shape of the frontier: **verifier-based** scaling is more robust than **verifier-free**, instilling genuine **parallel** thinking is still an open problem (models are natively sequential thinkers), and the whole edifice — training *and* inference — leans harder on the quality of the verifier the more you scale it.

---

## Putting the machine together

Hold the whole engine in one view.

1. **Two axes (Part 1).** Answer-time compute buys reasoning two different ways: **sequential** (one longer chain — depth) and **parallel** (many chains, then select — width; self-consistency's majority vote is the simplest select). Different machines, different walls.
2. **Coverage vs selection (Part 2).** **Generation** is nearly solved — sample enough and a right answer appears in the pile (coverage rises as a power law over four orders of magnitude; a weak model at 250 tries beat a strong one at one). **Selection** is the ceiling — without a checker, voting and reward models **plateau**. Generation scales; selection does not.
3. **The verifier is the engine (Part 3).** It all works because **checking is easier than generating** (the same propose-and-evaluate loop as AlphaZero/MCTS). Where a perfect checker exists, you soar; where not, you train a **reward model** — and grading **each step** (a PRM) beats grading the **end** (an ORM), because it localises errors and steers a search. But the judge is *itself a fallible model*.
4. **Search (Part 4).** Sequential = a **path**, parallel = a **fan**, search = a **tree** (Tree of Thoughts: explore, self-evaluate, look ahead, backtrack — 4% → a large majority on Game of 24). All three generate-and-select; all three lean on the verifier. The AlphaZero template transfers, but its *perfect simulator + clean reward* do not.
5. **Compute-optimal, and bending (Part 5).** The best method depends on **difficulty**; adaptive allocation beats naive by >4×, and smart test-time compute can beat a **14× larger** model. But both curves have a **knee**: sequential **overthinks** and reverses; parallel is capped by the verifier's **false positives**. The 2026 training name is **RLVR**; the optimiser is AP4's.

---

## Judging the machinery: where the "think longer" machine is stuck

The [AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) judged the **bet** (four cracks: needs a checker · RL may only sharpen · the shown reasoning may be a story · it breaks on novelty and costs a fortune). This page judges the **machine** — a sharper question: *set the bet aside; is "spend compute at answer-time" the clean, ever-rising dial the single curve made it look?* Be fair first: it is real, it is measured, and where a verifier exists it is close to a superpower — a small model plus smart thinking genuinely beating a much larger one is a profound result. Nothing here erases that. But the machine has its **own** four cracks, and each sharpens a crack the card only stated.

### Stuck #1 — the bottleneck is verification, not generation

This is the deepest finding on the page, and it relocates the whole problem. The card said AP2 "only works where you can check the answer" and filed it as one crack among four. The machine shows it is not one crack — it is **the single thing every method on this page depends on.** Generation is nearly solved (coverage scales as a power law); **selection** is the ceiling, and selection **is** verification. So "spend more compute at answer-time" is really "spend more compute generating candidates you then have to verify" — and you get to keep only as much as your verifier can correctly pick out. Where the verifier is perfect and free (maths, code, games), the ceiling is high and the curve soars. Where it is absent (judgment, taste, strategy, most of real life), the coverage curve keeps rising and buys you **nothing**, because you cannot find the right answer in your own pile. The card's "needs a checker" was stated as a limitation; the machine reveals it as **the central mechanism**: test-time compute is a verification amplifier, and it amplifies nothing where there is nothing to verify against. **[Established — coverage-scales-but-selection-plateaus is a measured, reproduced result.]**

### Stuck #2 — the verifier is itself a fallible model, and it can be gamed

Where no perfect checker exists, you *build* one — a reward model — and now the quality of your reasoning is bounded by the quality of a **second model** that is often a sibling of the first. Three failures follow, all documented. **It shares blind spots:** a judge trained like the generator will confidently approve the generator's confident errors — which is the card's Stuck #3 (unfaithful, after-the-fact reasoning) seen from the verifier's side: self-checking is only as honest as the checker. **It can be gamed:** optimise hard against a learned reward and the generator learns to produce answers the *judge* loves rather than answers that are *right* — **reward hacking**, whose home is [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) and the [alignment page](../30-across-the-approaches/02_alignment-control-and-self-improvement.md), pointed at. **Its errors compound with scale:** the more you sample, the more the verifier's **false positives** accumulate, which is *why* the returns diminish (Part 5). So "it checks itself" is not a foundation — it is a fallible model checking a fallible model, and the check is exactly as trustworthy as another guess. **[Established that learned verifiers are fallible and gameable; how far a good one can be pushed is Contested, open.]**

### Stuck #3 — both curves bend: sequential overthinks, parallel is capped

The card said the thinking "costs a fortune" and "may hit its own wall." The machine says precisely *which* wall, on *which* axis. The **sequential** curve saturates — extra reasoning tokens stop helping past a modest budget — and then **reverses**: with too long a leash a model **overthinks** and abandons a right answer it already had. The **parallel** curve is capped by the verifier (Stuck #1/#2): coverage rises forever, but usable accuracy stops where selection plateaus. So "think longer" is neither free nor infinite on *either* axis, and the compute-optimal amount is often surprisingly **modest** — the right buy is "enough thinking," and past it you are paying to get **worse.** This is the mechanical face of the card's cost crack: not a vague "expensive," but two curves each with a measurable knee beyond which more compute is wasted or harmful. **[Established — diminishing returns and overthinking are measured 2025–26; the exact knees are task-dependent snapshots.]**

### Stuck #4 — the AlphaZero template transfers, but its guarantees do not

The card's most inspiring point was the durable AlphaZero ancestor: learn from reward, search, self-play, pass your teachers. The machine shows *why that promise is harder to cash in reasoning than the analogy suggests.* AlphaZero's search worked because Go gave it a **perfect simulator** (you always know the exact next board) and a **clean, ground-truth reward** (win/lose). Its evaluator could be trained toward perfection. Open reasoning has **neither** — no exact model of where an argument leads, no unambiguous score for open judgment — so the same propose-search-evaluate loop must run on a **learned, fallible** evaluator (Stuck #2), in a space with no ground truth to anchor it. This is the mechanical reason the beautiful game-playing result does not simply "carry over" to thinking-in-words: the method is portable, the **perfect verifier that made it superhuman is not.** Everywhere the world supplies its own clean checker (theorem-proving, competitive programming) the transfer is real and stunning; everywhere it does not, the loop is only as good as a model grading a model. **[Likely — the analogy's power and its limits are both widely argued; the exact reach is Contested.]**

### The big question under all four

The card asked: *is longer thinking a new kind of intelligence, or AP1 in a new coat?* The machine answers a sharper, mechanical version: **test-time compute is a genuine second engine — but nearly all of its power is a function of how well you can verify, not how long you can think.** Where verification is free and perfect, it is close to a superpower and the "new coat" charge is plainly wrong — a small model that thinks and checks well really does out-reason a much larger one, and that is a new capability, not a repackaged old one. Where verification is hard or impossible — which is most of what we mean by *general* judgment — the generation curve keeps climbing and delivers a larger and larger pile of guesses you cannot sort, and the engine idles. So the frontier of the "think longer" bet is not, in the end, about thinking longer. It is about **learning to check**: build better verifiers, extend them past maths and code into open judgment, and keep them honest against a generator trying to fool them. *As of July 2026, the reasoning revolution is, underneath its long chains and clever search, a **verification** problem — and how far reasoning generalises is exactly the question of how far verification can be made to reach.* **[Contested — the key open question, now located precisely: it lives in whether verification can be extended beyond the checkable corner where it currently works.]**

---

## ⚠️ Honesty box

- **The generation/selection split is the durable core; the numbers are snapshots.** That coverage scales while selection plateaus, that verifying is easier than generating, that process rewards beat outcome rewards, that there is a compute-optimal amount — these are core ideas that will still frame the subject in a decade. The specific figures (16%→56% at 250 samples, ">4× efficiency," "14× larger model," the overthinking token-budgets) are 2024–2026 fits for particular models and tasks and will move. Learn the split; date every number. **[Established core; dated specifics.]**
- **"It thinks longer" ≠ "it thinks better."** Longer chains help up to a knee and then saturate or reverse (overthinking). Always ask for the *compute-optimal* point, not the maximum — and treat "we let it think for minutes" as a cost claim, not a quality claim, until shown the curve. **[Established.]**
- **A verifier is not a guarantee.** Where the checker is a real oracle (a compiler, a proof checker) the results are trustworthy. Where it is a *learned* reward model, it is a fallible sibling of the generator — gameable, blind in the same places, and worse the harder you optimise against it. Never read "reward-model-selected" as "correct." **[Established.]**
- **The miracle is real, and it is local.** Test-time compute beating a much larger model is genuine — *in the checkable corner.* It is precisely where you'd most like reasoning to help (open, fuzzy, unverifiable judgment) that the machinery has the least to offer. Keep "superhuman at maths" and "wise in general" firmly apart. **[Established → Contested along that line.]**
- **Sequential and parallel are different bets.** Depth (one long chain) and width (many chains + a judge) fail differently and cost differently. A system that only scales one is leaving the other on the table — and "we scaled test-time compute" should always prompt "which axis, and how did you select?" **[Established.]**
- **Names and numbers age; the machine doesn't.** Self-consistency, ToT, PRMs, the Monkeys coverage curve, RLVR, o3's ARC scores — all dated. The lasting parts are the **generation/selection split**, the **verification asymmetry**, **process-over-outcome** grading, **search as a tree**, and the **compute-optimal / bending-curve** facts. The example methods will be replaced; the shape of the argument will not. **[Established core, dated specifics.]**

---

## How to use this (if you want to direct AI work)

- **Ask "generate or select?" about every reasoning result.** (Stuck #1.) A high score from heavy test-time compute almost always means "we generated many candidates and selected well" — so the real question is *how did you select?* If the answer is "a perfect checker" (code, maths), trust it; if it is "a learned reward model" or "majority vote," expect the selection ceiling and the false-positive tax. No good selector, no reliable gain.
- **Demand the compute-optimal point, not the maximum.** (Stuck #3.) "It scores higher if it thinks 100× longer" is usually a bad buy and sometimes a *worse* answer (overthinking). Ask where the curve knees, match the budget to the problem's difficulty, and treat "enough thinking" as the target.
- **Name the axis.** (Part 1.) Push for *which* dial was turned — longer chains (sequential), more samples (parallel), or tree search — because they fail and cost differently, and a system scaling only one is usually leaving easy gains, or hidden costs, unexamined.
- **Treat the verifier as the most valuable part.** (Stuck #1/#2.) The leverage is in the checker, not the thinker. Invest in real oracles where you can build them, in strong process reward models where you can't, and audit them for gaming and shared blind spots — a better verifier buys more than a bigger generator.
- **Don't import AlphaZero's guarantee with its method.** (Stuck #4.) Search over reasoning is the same loop as game search, but your problem probably lacks Go's perfect simulator and clean reward. Before betting on search, ask what plays the role of the rules and the win/lose signal — if the answer is "a model we trained," you are back to Stuck #2.
- **What you delegate vs what you keep.** *Delegate:* running the sampling, the search, the reward-model training, the serving cost. *Keep for yourself:* the judgement of whether a result rests on a real checker or a fallible one, the discipline of separating coverage from selection, the refusal to pay for overthinking, and the habit of asking whether "reasoning" that shines on checkable tasks has any purchase on the unverifiable judgment you actually need.

---

## Connections

- **Keep only three things:** ① "Think longer" is not one dial but a **family of machines** — **sequential** (one longer chain), **parallel** (many chains, then pick — self-consistency's majority vote), and **search** (a tree you grow and prune — Tree of Thoughts); all three **generate candidates and select among them**, differing only in structure. ② **Generation is nearly solved, selection is the ceiling:** sample enough and a right answer appears in the pile (**coverage** scales as a power law), but without a checker you **can't find it** (voting and reward models **plateau**). So the whole bet rests on a power the card never named — **verification** — and *checking is easier than generating* is the hidden engine (grading **each step**, a PRM, beats grading the **end**). ③ The dial is **optimisable and bends:** the best method depends on difficulty (a small model + smart thinking can beat a **14×** larger one), but sequential **overthinks** past a knee and parallel is **capped by the verifier's false positives** — so the frontier of reasoning is really the frontier of **learning to check.**
- **This deep dive branches off:** [AP2 · reasoning & test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — the card owns the *bet, chain-of-thought, the o3/ARC-AGI scaling numbers, verifiable-reward RL + DeepSeek-R1, the AlphaZero ancestor, fast/slow thinking, and the four bet-cracks.* This page opens the *inference-time machine* under "think longer" — the sequential/parallel axes, coverage-vs-selection, the verifier (ORM vs PRM), search/Tree-of-Thoughts, and the compute-optimal/bending-curve facts — and judges the *machine's own* trustworthiness.
- **Where it points:** [AP1 · deep dive #1](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) — which drew the *scaling-shape* of this answer-time axis and handed the mechanism here; its **compute-optimal** idea is this page's compute-optimal split, one level out. [AP4 · RL from interaction](../20-the-approaches/04_ap4-rl-from-interaction.md) — owns the RL **optimiser** (GRPO/RLVR) that trains reasoning models, and **reward hacking**, the failure mode a learned verifier invites. [AP8 · solver mechanisms](02_ap8-deep-dive-solver-mechanisms.md) — owns **test-time *training*** (updating weights per problem), the cousin this page is careful to distinguish from test-time *compute*. And the [alignment page](../30-across-the-approaches/02_alignment-control-and-self-improvement.md) — where "the verifier is a fallible, gameable model" becomes a safety problem.
- **How sure are we?** That test-time compute splits into sequential/parallel/search, that coverage scales while selection plateaus, that verifying is easier than generating, that process rewards beat outcome rewards, and that there is a compute-optimal (bending) curve — **[Established]**. That the whole bet's reach is bounded by verification — **[Likely, strongly evidenced as of 2026]**. How far verifiers can be extended past checkable domains, and whether that lets reasoning generalise — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Name the **two axes** of spending answer-time compute and say how each fails. Which one does "self-consistency" use, and what is its "select" step?
2. Explain **coverage vs selection**. Why is it true that a weaker model with 250 tries can beat a stronger model with one — and why does that *not* always translate into a right final answer?
3. Why does spending compute at answer-time buy correctness at all? State the **asymmetry**, and connect it to AlphaZero's **propose-and-evaluate** loop.
4. What is the difference between an **outcome** reward model and a **process** reward model, and why does grading **each step** win?
5. Give the **compute-optimal** finding in your own words (Snell et al.). What is "**overthinking**," and what does it say about "just think longer"?
6. The big one: name the **four engine cracks**, and explain the thesis that ties them together — *why is the frontier of "think longer" really a verification problem?*

## Revision notes

*Newest first.*
- `rev 1 (2026-07-17)` — created as the **first AP2 deep-dive** (reading group **⑤ Deep dives**, sortkey 5009), branching off the [AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md); the ninth module in group ⑤ (after the AP8 trilogy + AP4 #1 + AP5 #1 + AP9 #1 + AP1 #1 + AP3 #1). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the card's *bet / chain-of-thought / the o3-ARC scaling numbers / verifiable-reward RL + DeepSeek-R1 quotes / the AlphaZero quote / fast-slow thinking / four bet-cracks* are **referenced, never re-taught**; [AP1's deep dive](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) is the *scaling-shape* that handed the mechanism here (its compute-optimal idea reused one level out); [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) owns the RL **optimiser** (GRPO/RLVR) + reward hacking (pointed at, not opened); [AP8's solver deep dive](02_ap8-deep-dive-solver-mechanisms.md) owns **test-time *training*** (explicitly distinguished from test-time *compute*). This page adds only the new **inference-time machine** the card skipped: the **sequential vs parallel** axes (Part 1); **coverage vs selection** + the repeated-sampling power law (Part 2); the **verification asymmetry**, **reward models**, and **process-vs-outcome** supervision (Part 3); **search / Tree of Thoughts** + the MCTS/AlphaZero propose-and-evaluate template and its perfect-simulator limit (Part 4); and the **compute-optimal / bending-curve / overthinking / RLVR** frontier (Part 5). Grounded in **written, quotable** sources, each verified as an exact contiguous string: **Self-Consistency** (Wang et al. 2022 — "samples a diverse set of reasoning paths … selects the most consistent answer by marginalizing"; the "multiple different ways of thinking leading to its unique correct answer" intuition); **Large Language Monkeys** (Brown et al. 2024 — "coverage … scales with the number of samples over four orders of magnitude"; "log-linear … exponentiated power law"; "15.9% with one sample to 56% with 250 samples … single-sample state-of-the-art of 43%"; "common methods for picking … (majority voting and reward models) plateau beyond several hundred samples"); **Let's Verify Step by Step** (Lightman et al. 2023 — the outcome-vs-process supervision definitions; "process supervision significantly outperforms both forms of outcome supervision at all data collection scales"); **Tree of Thoughts** (Yao et al. 2023 — "coherent units of text ('thoughts') … deliberate decision making … self-evaluating choices … looking ahead or backtracking"; the Game-of-24 4% line); **Snell et al. 2024** (compute-optimal — "critically varies depending on the difficulty of the prompt"; ">4x … best-of-N baseline"; "outperform a 14x larger model"). Full live-SOTA pass (**July 2026**), each fast fact dated: overthinking / diminishing returns (a thinking-budget knee; extended reasoning abandoning correct answers); imperfect-verifier false-positives *causing* the diminishing returns; **RLVR** as the cornerstone term; verifier-based scaling more robust than verifier-free; genuine parallel thinking still hard to instill (models natively sequential). Four **engine** cracks (distinct from the card's *bet*-cracks): **the bottleneck is verification, not generation** (generation/coverage scales, selection plateaus — sharpens the card's "needs a checker" into the central mechanism) · **the verifier is itself a fallible, gameable model** (self-verification shares blind spots — mechanical face of the card's unfaithful-CoT crack; reward hacking pointed at AP4) · **both curves bend** (sequential overthinks, parallel is capped by false positives) · **the AlphaZero template transfers but its perfect-simulator + clean-reward do not** — under the big question: *test-time compute is a real second engine, but nearly all its power is a function of how well you can verify; the frontier of "think longer" is really a verification problem.* Degendering: all sources attributed to name-et-al or org; **0 gendered pronouns**, **0 self-anchor `](#…)` links**, all outbound .md links resolve.

---
*This is the first AP2 deep dive — the **machine** beneath the "think longer" dial. It is the mechanism [AP1's deep dive](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) handed off; its RL optimiser is [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md)'s; its verifier-as-bottleneck is why the card's "only works where you can check" is the constraint the whole approach depends on. To pick the next approach to go deep on, return to the [spine](../APPROACHES_TO_AGI.md).*
