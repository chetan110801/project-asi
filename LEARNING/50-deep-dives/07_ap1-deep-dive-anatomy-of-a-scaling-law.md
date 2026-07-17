---
id: c-scaling-law-anatomy
sortkey: 5007
title: AP1 · Deep dive — the anatomy of a scaling law: the actual equation you read the future off (and why nobody knows why it works)
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale]
provides: [scaling-law-parametric-form, irreducible-loss-entropy-floor, finite-size-penalty, finite-data-penalty, scaling-exponents-small, compute-identity-6nd, forward-backward-flop-count, compute-optimal-as-constrained-optimization, fit-and-extrapolate-methodology, gpt4-predictable-scaling, kaplan-chinchilla-measurement-bug, data-constrained-scaling-repeat-epochs, precision-scaling-effective-params, test-time-compute-new-axis, scaling-law-no-theory, loss-is-not-capability]
resources: [r-cs336]
status: ready
reading_time: 38 min
rev: 1
created: 2026-07-17
updated: 2026-07-17
---

# AP1 · Deep dive — the anatomy of a scaling law: the actual equation you read the future off (and why nobody knows why it works)

*This is a **deep dive** past the [AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md) and the [scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md). Both told you the headline: make a language model bigger and its mistakes fall in a **steady, straight, predictable line** — so "make it smarter" turns into "buy more computer power." That straight line is the whole reason people bet on scale. But both pages gave it to you as a **picture** — a line on a chart — and a **slogan** — "bigger is predictably better." Neither opened the machine. Under that line sits an actual **equation**: a short formula with three named pieces that says exactly how the mistakes fall, plus a second, simpler equation that turns a pile of money into a precise machine shape. This page writes both equations in plain words. Then it shows the thing the slogan hides: **how a lab actually reads the future off the line** (it really did predict a giant model's score before building it), the true story of the **two years the equation was measured wrong** and misled the whole field, the deepest uncomfortable fact — **we can use the law to three decimal places and cannot explain why it holds** — and where the law is being re-drawn in 2026 as its fuel runs out. Everything the card and the rung already said — the straight line, Chinchilla's balance rule, the data wall, emergence — is referenced, not repeated.*

> **You are here:** a **deep-dive module** — reading group **⑤**, the optional layer that branches off the main staircase. This one hangs off **[AP1 · scale & foundation models](../20-the-approaches/01_ap1-scale-and-foundation-models.md)**. *Read the AP1 card and the [scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) first* — this page assumes both and opens the equation they only drew as a line. It is the first deep dive off AP1, the approach every other one on the map argues against.
>
> **What you already have (a one-line reminder each, then we build — none of it is re-taught here):** from the **[scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md)** — the three things you scale (**size** = number of adjustable inner numbers, called **parameters**; **data** = amount of text, counted in **tokens**; **compute** = amount of number-crunching, counted in **FLOPs**); the **mistake-count** (called the **loss**) that all three push down; the **straight line** (loss falls as a **power law**, so a "times-ten" chart shows a ruler-straight line you can extend to predict a bigger machine); the **floor** the line falls toward but never crosses; **Chinchilla**'s balance rule (for a fixed budget, grow size and text together) and the **data wall** (good human text is finite — "we have but one internet"); and **emergence** (skills that seem to switch on at size — partly real, partly a scoring trick). From the **[AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md)** — the **bet** (one simple job + huge scale → real skills appear on their own), the **Bitter Lesson**, **foundation models**, and the four cracks in the bet. **New here:** the *equation* under the line — its three pieces, the compute identity that turns a budget into a shape, how the future is actually read off it, the bug that broke it for two years, and the 2026 frontier.
>
> **Where the facts come from:** written, checkable sources, each quote web- or corpus-verified as exact. The **equations** — Kaplan et al. (2020) for the compute identity and the first power-law fits; Hoffmann et al. (2022, "Chinchilla") for the three-piece loss formula; the GPT-4 technical report (2023) for the real "predict-before-building" story. The **2026 frontier** — the data-constrained law (Muennighoff et al., 2023), the precision law (Kumar et al., 2024), the test-time-compute turn (the o1 reasoning model, 2024), and the reconciliation of the Kaplan–Chinchilla disagreement (2024) — is checked on the web (**as of July 2026**) and dated where it moves. The durable framing traces to the corpus sources the card and rung already used (the CS336 course, the scaling papers), so those are *pointed at*, not re-quoted.

---

## In one minute

The card and the scaling rung both said the same true thing: **bigger → fewer mistakes, in a steady line you can predict.** Here is what neither opened. That line is not a mood or a trend — it is a specific **equation**, and there is a second equation next to it that quietly decides the shape of every large model ever built. Once you can read both, the whole "make it bigger" bet stops being a slogan and becomes a machine you can inspect — and criticise.

1. **The loss equation — a floor plus two penalties.** The mistake-count of a trained model is very well described by three added-up pieces: `loss = a floor you can never beat + a penalty for having a finite-size brain + a penalty for having read a finite amount of text`. Write it and you can *see* what scaling does: making the model bigger shrinks the second penalty; feeding it more text shrinks the third; neither can touch the first.

2. **The compute identity — `C ≈ 6ND`.** The total number-crunching a training run costs is, very simply, about **six times the number of parameters times the number of tokens**. This one line is why you cannot make the brain bigger *and* feed it more text for free: a fixed budget of compute is a fixed value of `6ND`, so more of one means less of the other. Put this next to the loss equation and "how big, trained on how much?" becomes a **math problem with one best answer** — which is exactly the problem Chinchilla solved.

3. **You really can read the future off it.** Train a *ladder* of small, cheap models, measure their loss, fit the equation's pieces, then **extend the line** to a giant model you have not built yet. This is not a metaphor: the makers of GPT-4 predicted its final score from small models using **one-thousandth** of the compute — before the big run finished.

4. **But the equation was measured wrong for two years, and it has no theory under it.** The first famous scaling law (2020) pointed the whole industry at models that were **too big and too little-read** — a subtle measurement mistake, not fixed until 2022. And to this day, we can *use* the equation with startling precision while having **no accepted explanation of why the loss should follow a power law at all.** A law you can't derive can bend anywhere without warning — which is the quiet danger under every chart that stretches the line out to "AGI."

The card showed you a line and asked "is scale enough?" This page shows you the equation under the line — and finds that the most reliable number in all of AI is also un-explained, points at the wrong target, gets crueller the further you push it, and has already fooled the smartest people in the field once.

---

## One line of base, then we build

Two reminders, because the whole page turns on them — and both are owned by earlier rungs, so here they are *pointed at*, not re-taught.

- The [scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) gave you the **line**: loss falls as a **power law**, which on a "times-ten" chart *(a chart where each step means ×10 on both directions, called a **log-log plot** — its home is the rung)* is a straight line you can extend into the future. That rung also gave you **Chinchilla**'s answer (balance size and text) and the **data wall**. This page never re-draws that line or re-states those answers. It opens the **formula** the line is a picture *of*, and shows the *mechanism* that makes Chinchilla's answer forced rather than lucky.
- The [AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md) judged the **bet** (is scale enough for a general mind? — its four cracks). This page is one level down: **is the engine under the bet — the scaling law itself — as solid as it looks?** So read every part as opening a machine: here is the line the field lives by → here is the equation inside it → here is where the equation is fragile. We are **not** re-judging the bet. We are testing whether the instrument the bet reads its future on is trustworthy — and only at the end asking what its flaws do to the bet.

One framing to carry the whole way. A scaling law is an **empirical law** *(empirical = found by measuring the world, not worked out from theory — like noticing "heavier things fall the same speed" before anyone knew why)*. That word is the key to this entire page. An empirical law is only ever as good as **two** things: the measurements you fit it on, and how far past those measurements you dare to stretch it. Both of those turn out to be shakier than the beautiful straight line lets on.

---

## Part 1 — the equation: a floor, plus two penalties

Start with the reveal that makes everything else readable. The "steady line" is a picture of one short equation. It was written most cleanly by the Chinchilla team (Hoffmann et al., 2022), who modelled a trained model's loss as a sum of **three pieces**. Here it is, in symbols first, then in plain words:

```
L(N, D)  =  E  +  A / N^α  +  B / D^β
```

Read the symbols slowly. **`L(N, D)`** is the loss *(the mistake-count — how badly the model guesses the next token; its home is the rung)* of a model that has **N** parameters *(N = the number of adjustable inner numbers — the "size"; home = the rung)* and has been trained on **D** tokens *(D = the amount of text, in chunks called tokens; home = the rung)*. The right side is what that loss will be: a fixed number **E**, plus a term that shrinks as **N** grows, plus a term that shrinks as **D** grows. The little raised letters **α** and **β** *(alpha and beta — two fixed **exponents**, i.e. the power a number is raised to; here, how fast each penalty shrinks)* control how fast each term falls. Now the three pieces, which are the real content — and the paper says exactly what each one *is*:

> "The first term captures the loss for an ideal generative process on the data distribution, and should correspond to the entropy of natural text. The second term captures the fact that a perfectly trained transformer with [N] parameters underperforms the ideal generative process. The final term captures the fact that the transformer is not trained to convergence, as we only make a finite number of optimisation steps, on a sample of the dataset distribution."
> *(Hoffmann et al., "Training Compute-Optimal Large Language Models," 2022)*

*(Two words from the quote, glossed: a **transformer** just means the standard kind of neural network today's language models are built as; the **data distribution** means the real text it is learning from.)* Unpack the three pieces one at a time, in the plainest terms.

- **`E` — the floor you can never beat.** This is a fixed number that no amount of scaling removes. It is the **entropy of natural text** *(entropy = the amount of genuine, built-in unpredictability in something; here, the fact that the exact next word in real writing is often a true coin-flip nobody and nothing could call for certain)*. Even a perfect machine that understood the world completely would still get some next-word guesses "wrong," because the writer could genuinely have gone either way. The rung called this **the floor**; the equation *names* it — it is the term `E`, and it sits there alone, untouched by `N` or `D`. **[Established]**

- **`A / N^α` — the price of a finite-size brain.** This term is the extra loss you pay for the model being a certain size rather than infinitely large. Because `N` is on the bottom of a fraction, **the bigger you make the model, the smaller this penalty gets** — you are paying down a debt by adding parameters. Make `N` huge and this term crawls toward zero. This is the "size" half of scaling, made exact. *(A is just a fixed number that sets the size of the penalty.)*

- **`B / D^β` — the price of finite reading.** The last term is the extra loss you pay for two limits: you trained on a limited amount of *text*, and for a limited *time* — the model was not *trained to convergence* *(trained to convergence = trained for so long that it stops improving)*, the way endless data trained forever would be. **More tokens `D` shrinks it.** This is the "data" half of scaling, made exact.

So the whole equation says something you can now *picture*: a trained model's mistakes are **an unbeatable floor, plus two debts** — one you pay down with size, one you pay down with data. Scaling is just paying down the two debts. And you can immediately see the bet's ceiling: **you can drive both debts toward zero, but you can never get below `E`.** The straight line the rung showed you is exactly this equation, drawn on a times-ten chart.

### The quiet bad news hiding in the exponents

Now look hard at α and β — the two little raised letters. Their **size** is the whole story of "diminishing returns," and it is easy to miss. In the Chinchilla fit, α ≈ 0.34 and β ≈ 0.28. In the earlier Kaplan fit they were even smaller (around 0.07–0.10). These are **small** numbers — and small exponents are cruel. Here is why, in one concrete step.

Because the penalty is `A / N^α`, halving that penalty does **not** take twice the size — it takes `2` raised to the power `1/α`. With α ≈ 0.34, that is `2` to the power of about `3` — roughly **eight times** the parameters to cut the size-penalty in half. And to halve it *again*, another eight times. The exponent being well below 1 means every equal *slice* of progress costs a **multiplying** amount of compute — 8×, then 8× again, then 8× again. The famous "smooth, predictable line" is smooth and predictable precisely because it is a power law — but the same power law, read honestly, says the road gets **exponentially more expensive** the further you walk it. Hold this; it becomes the engine's cruellest crack (Stuck #3). The equation that promises you can predict the gains is the same equation that guarantees they get ruinous.

---

## Part 2 — the compute identity: `C ≈ 6ND`, and why a budget forces a shape

Part 1 had two knobs, `N` and `D`, and no mention of money. But you cannot turn both knobs freely — every parameter and every token costs computer power, and computer power is the budget. The bridge between "size and data" and "money" is a second equation, even simpler than the first, and it is the most useful single line in this whole subject. It comes from Kaplan et al. (2020):

```
C  ≈  6 · N · D
```

In words: **the total compute `C` a training run costs is about six times the number of parameters times the number of tokens.** *(C = compute, the total number of tiny arithmetic steps, FLOPs; home = the rung.)* That is it. If you know how big the model is and how much text it reads, you know — up to a small constant — how much number-crunching the run will take.

### Where the "6" comes from (and why it is worth seeing)

The `6` is not magic; it is bookkeeping, and seeing it makes the identity stick. Training does two passes over the model for each token, and there is a neat rule of thumb for each:

- **The forward pass** *(forward pass = running the text through the model to make its guess)* costs about **2 FLOPs per parameter, per token.** Why 2? Because each parameter is used in one **multiply** and one **add** *(the two arithmetic steps in the core operation of a neural network — multiply an input by a weight, add it to a running total)* — that is two operations. Kaplan writes this as `C_forward ≈ 2N`.
- **The backward pass** *(backward pass = working out, for every parameter, which direction to nudge it to reduce the mistake — the actual "learning" step)* costs about **twice the forward pass**, so about `4N`.

Add them: `2N + 4N = 6N` FLOPs per parameter-token — that is, **about six operations per parameter for every token the model reads.** Multiply by the total tokens `D` and you get `C ≈ 6ND`. This is durable: the exact constant shifts a little with the model's **architecture** *(architecture = the model's design — how its parts are wired together)*, but "compute is roughly six times parameters times tokens" is a core fact every practitioner keeps in mind.

### Why this turns "how big?" into a solvable math problem

Here is the payoff, and it is the mechanism the rung's Chinchilla answer sits on top of without showing. Fix a compute budget — say, all the number-crunching you can afford. That fixes the value of `6ND`, which fixes the **product** `N × D`. So you are no longer free to pick `N` and `D` separately: **spend more on the brain (bigger `N`) and you must read less text (smaller `D`), and the reverse.** They trade off along a fixed budget line.

Now put that constraint together with Part 1's loss equation, and a real question appears with a real answer: *given that `N × D` is fixed, which split of the two makes the loss `L(N, D)` as low as it can go?* That is a **constrained optimisation** *(constrained optimisation = finding the best choice while a rule limits what you're allowed to pick — here, "lowest loss, but you must stay on the budget line")*. It has a single best answer — one particular ratio of size to data. **That answer is what "compute-optimal / Chinchilla" *is*** — the rung told you the answer (balance them; grow together); this page shows you it is not a rule of thumb but the **solution to an equation**: minimise `E + A/N^α + B/D^β` subject to `6ND = your budget`. The reason the field could suddenly *calculate* the right shape of a model, instead of guessing, is that both equations on this page were in hand at once. (And you can now see *why* the exponents α and β decide the balance: they set how steeply each penalty falls, so they set which knob is worth more per FLOP.)

---

## Part 3 — reading the future off it: how a lab actually predicts a model before building it

The rung said the straight line lets you "read the future off it — predict how good a giant machine will be before you spend the money." True, and astonishing — but *how*, mechanically? A promise that vague is easy to distrust. Here is the actual procedure, and then the proof it works.

**The procedure — fit small, extend the line.**

1. **Train a ladder of small, cheap models.** Pick a handful of sizes `N` and data amounts `D`, all far smaller than your target — each one costs a tiny fraction of the real run. Train each and write down its final loss.
2. **Fit the equation.** You now have a set of `(N, D, loss)` points. Find the values of `E`, `A`, `B`, `α`, `β` that make Part 1's equation pass through those points best. *(This "find the numbers that best fit the data" step is a small, standard curve-fit — the AI's job, delegated; what matters to you is that it yields the five pieces of the law for **your** setup.)*
3. **Extend the line.** Plug your giant target's `N` and `D` into the now-fitted equation. Out comes a **prediction of the big model's loss** — computed before the expensive run exists.

**The proof it is real.** This is not a thought experiment. The GPT-4 team did exactly this and reported it plainly:

> "This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4."
> *(OpenAI, GPT-4 Technical Report, 2023)*

Sit with **one-thousandth.** They fit the law on models costing a thousandth as much, extended the line by a factor of a thousand in compute, and hit the target. And they stress the hardest part — the prediction was locked in *before* seeing how the big run turned out:

> "This prediction was made shortly after the run started, without use of any partial results."
> *(GPT-4 Technical Report, 2023)*

That "without use of any partial results" is what makes it a genuine prediction and not hindsight. **This is the single most valuable thing a scaling law buys:** it converts a hundred-million-dollar gamble into a calculation you can check on small change first. It is also why the "just make it bigger" bet was ever *fundable* — investors are not betting on a hope, they are reading a fitted line. **[Established — this is standard practice at every frontier lab, as of 2026.]**

But notice the crack already opening, which we return to at the end: they predicted **loss** — the mistake-count. Whether that predicted loss would translate into GPT-4 being able to *pass a bar exam* is a **second, much looser** question the line does not answer. The report itself admits some capabilities "remain hard to predict." The future you can read off the line is the *loss*; the future you actually care about is the *capability*, and the two are not the same line.

---

## Part 4 — the two-year bug: when the equation itself was measured wrong

Here is the story that should permanently cure anyone of over-trusting a scaling law — and it is the mechanical heart of this page's critique. For about **two years**, the field's own scaling law told it to build the **wrong shape of model**, and almost everyone followed it.

The rung told you the *outcome*: the first famous law (Kaplan et al., 2020) led labs to make models **too big for the amount of text they read** ("undertrained"), and Chinchilla (2022) corrected it to "balance size and data." The rung owns that correction, so it is only pointed at here. What the rung did **not** open — and what matters for judging the engine — is *why the first law was wrong.* Because the answer is not "they had a dumb idea." Both teams did careful science. The law was wrong because of **subtle choices in how the small models were measured**, and that is far more unsettling.

Two causes, in order of size (established by careful 2024 replications that reconciled the two laws):

- **Counting the wrong parameters (the bigger cause).** Kaplan measured model size as **non-embedding parameters** *(the parameters in the model's main body, leaving out the big "embedding" table that turns tokens into numbers at the very entrance)*. For small models, that left-out table is a **large slice** of the total, so Kaplan's small models were effectively mis-measured relative to big ones — which tilted the fitted line toward "size matters more than it really does." Count **total** parameters and compute, and much of the disagreement dissolves.
- **A learning-rate schedule that didn't match the run (the second cause).** Training turns a "learning rate" *(learning rate = how big a step the model takes each time it adjusts itself)* down to nearly zero by the end of a run, on a planned schedule. Kaplan used one fixed schedule set for a long run, then also read off **shorter** runs part-way along that same schedule — so those shorter, data-lighter runs were stopped while their learning rate was still "wrong for their length," making them look **worse than they truly were.** That made *reading more data* look less valuable than it is, again tilting the answer toward "spend on size." Chinchilla matched the schedule to each run's length, and *more data* suddenly paid off properly.

Read what happened here. Two respectable, careful measurement choices — *which parameters you count*, and *how you set a training knob on the small runs* — moved the fitted optimum by a factor of roughly **three in model size**, and the entire industry built oversized, under-fed models (GPT-3 among them) for two years as a result. Nobody was being foolish. **The law was simply an empirical fit, and a fit inherits every quiet bias in the runs you fit it on.** The straight line looked exactly as clean and convincing in 2020 as it does today. It was still pointing the wrong way. **[Established — the discrepancy and its causes were pinned down by replications in 2024.]**

That is the lesson to carry into the judgement: **a scaling law is not a law of nature you have discovered. It is a summary of the experiments you happened to run, and it can be confidently, cleanly, expensively wrong.**

---

## Part 5 — the frontier: the law bends, so the field re-draws it (2023–2026)

The classic law assumed a comfortable world: **endless fresh text**, each token seen once, and numbers stored at full precision. By 2026 all three assumptions have cracked, and the interesting research is the field **re-fitting the law** for the world as it actually is. Three extensions matter, and each is a genuinely new mechanism the rung does not cover — so each is built here.

### Extension 1 — data-constrained scaling: what to do when the text runs out

The rung told you the **data wall** exists (good human text is finite). It did **not** tell you what happens *mechanically* when you hit it. The cleanest answer comes from a study of training on **repeated** data — reading the same text more than once (each full pass is an **epoch** *(epoch = one complete pass through the whole training dataset)*). The finding is precise and surprisingly hopeful, then sobering:

> "we find that with constrained data for a fixed compute budget, training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data. However, with more repetition, the value of adding compute eventually decays to zero."
> *(Muennighoff et al., "Scaling Data-Constrained Language Models," 2023)*

Unpack it. For the **first ~4 passes**, re-reading the same text works **almost as well as brand-new text** — a real reprieve when new text is scarce. But keep repeating and the benefit **decays to zero**: the model has wrung everything it can from that text, and extra compute buys nothing. So the data wall is not a cliff — it is a **ramp down**: repetition extends the runway a few times over, then flattens. This *quantifies* the rung's data wall, and it is why "just re-read the internet a few more times" is a real but strictly limited move. **[Established, as of 2026.]**

### Extension 2 — precision scaling: a fourth knob, measured in bits

There is a knob the classic law never counted: **precision** *(precision = how many bits are used to store each number in the model — more bits = finer, more exact numbers; fewer bits = coarser, cheaper ones)*. Storing every parameter in fewer bits makes the model cheaper to train and run — but too few bits and the numbers get too coarse to hold what was learned. A 2024 study turned this into its own scaling law with a striking core idea:

> "We propose that training in lower precision reduces the model's 'effective parameter count,'"
> *(Kumar et al., "Scaling Laws for Precision," 2024)*

In plain words: **using coarser numbers is a bit like having a smaller model** — a model with a billion low-precision parameters may behave like one with fewer full-precision ones. So precision folds *into* Part 1's `N` term rather than being separate. And the study found a genuinely counter-intuitive twist that bites right on the data wall:

> "For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful."
> *(Kumar et al., 2024)*

Read that carefully: if you plan to later **compress** the finished model to run it cheaply *(post-training quantization = squashing a trained model down to fewer bits after the fact)*, then a model trained on **more** data can end up **worse** after squashing — so past some point, extra training data actively hurts. This is the opposite of every earlier lesson, and it shows the "law" is not one fixed line but a **surface that shifts** as you add real-world knobs. **[Established for the studied setups; the exact thresholds are 2024–2026 snapshots and move.]**

### Extension 3 — the new axis: scaling compute *at answer-time*

The biggest re-drawing of all: when scaling the **training** knobs started paying diminishing returns, the field found a **whole new axis** to scale — the compute spent **thinking at answer-time.** Instead of a bigger model, let a fixed model **work for longer** on a hard question, taking many steps before answering. The 2024 reasoning model o1 reported that this is *its own* scaling law, on a different axis:

> "The performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)."
> *(OpenAI, "Learning to Reason with LLMs," 2024)*

Two axes, not one. **Train-time compute** is everything on this page so far — pour it into `N` and `D` up front, once. **Test-time compute** *(also called inference-time compute — the number-crunching spent each time the model answers, not during training)* is new: pour it in *at the moment of answering*, and let the model spend it thinking step by step. Accuracy rises smoothly as you give it more thinking — a second predictable curve. *The reasoning **mechanism** behind this (chain-of-thought, reasoning-via-reward) is [AP2 · reasoning & test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)'s home — pointed at, not opened here.* What belongs on **this** page is only the **scaling-law shape** of it: the field did not find that scaling was over; it found a **new knob to turn**, with its own curve — and a new trade-off, because test-time compute is paid **every single time the model answers**, forever, while training compute is paid once. As of 2026, this shift is the field's main answer to the plateau in the old knobs: *the age of pouring everything into one giant pre-training run is giving way to a mix of a strong base model and a lot of answer-time thinking.* **[Established that the axis exists and scales; how far it goes is a live 2026 question.]**

---

## Putting the machine together

Hold the whole engine in one view.

1. **The loss equation (Part 1) — floor + two penalties.** `L(N, D) = E + A/N^α + B/D^β`: an unbeatable floor `E` (the entropy of natural text), plus a size-penalty `A/N^α` you pay down with parameters, plus a data-penalty `B/D^β` you pay down with tokens. The exponents α, β are **small**, so every equal slice of progress costs a **multiplying** amount of compute.
2. **The compute identity (Part 2) — `C ≈ 6ND`.** Compute ≈ six times parameters times tokens (2 for the forward pass + 4 for the backward pass, per parameter per token). A fixed budget fixes `N × D`, so size and data **trade off** — and minimising the loss along that budget line is the **constrained-optimisation** whose answer *is* Chinchilla's balance rule.
3. **Reading the future (Part 3) — fit small, extend the line.** Train a ladder of cheap models, fit the five pieces, extend to the giant target. Real: GPT-4's loss was predicted from models using **1/1,000th** the compute, locked in before the run finished. But what's predicted is **loss**, not capability.
4. **The two-year bug (Part 4) — the fit can be wrong.** The 2020 law mis-measured the small runs (counting non-embedding parameters; an unmatched learning-rate schedule), pointing the whole field at oversized, under-fed models until 2022. An empirical law inherits every quiet bias in its runs.
5. **The 2026 frontier (Part 5) — the law is being re-drawn.** Repeated data buys ~4 free epochs then decays (the mechanical data wall); precision is a fourth knob (fewer bits ≈ fewer effective parameters, and more data can *hurt* after compression); and a **new axis** — test-time compute — scales on its own curve, paid at every answer.

---

## Judging the machinery: where the scaling law itself is stuck

The [AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md) judged the **bet** (four cracks: running out of text · "surprise skills" may be partly fake · copying isn't understanding · is scale *enough*). This page judges the **instrument** — a narrower, sharper question: *set the bet aside; is the scaling law, as a measuring tool, as trustworthy as the clean straight line makes it look?* Be fair first: it is the **most re-tested, most reliable quantitative fact in all of AI**, it genuinely predicts giant models from small ones, and it turned a gamble into a calculation. Nothing here erases that. But the instrument has its **own** four cracks, and each sharpens a crack the card only stated.

### Stuck #1 — the law is measured, not derived: there is no theory under it

This is the deepest and most surprising crack. We can *fit* the equation to many decimal places and *use* it to steer billion-dollar runs — and we have **no accepted explanation of why the loss should follow a power law at all.** It is a curve we found by looking, not one we worked out from how learning must behave. There are candidate theories — that language modelling is really fitting a surface on a **low-dimensional data manifold** *(the idea that real text, though it looks huge, actually lives on a much simpler hidden shape, and the scaling exponent is roughly one divided by that shape's dimension)*, or that skills come in discrete **"quanta"** learned in order of how often they're needed *(the quantization model — a power law in how often each skill is used produces the power law in loss)* — but none is settled. A 2026 review of the theory work put the state of things plainly:

> "I only listed two hypotheses here, but there are more studies on explaining the shape of power-law scaling through spectral tails of data, kernel eigenvalues, natural-language statistics, or phase transitions in training dynamics."
> *(Lilian Weng, "Scaling Laws, Carefully," June 2026)*

Many candidate explanations, no winner. Why this bites: **a law you cannot derive gives you no warning about where it will bend.** A theory would tell you "the line stays straight until *here*, then breaks." An empirical fit tells you only "it has been straight so far." So every chart that stretches the line out to AGI is trusting a curve **nobody can explain** to keep behaving in a range **nobody has visited.** That is not a calculation. It is a hope, with a straight line drawn under it to make it look certain. This is the mechanical face of the card's "is scale enough?" — you are extrapolating an instrument you do not understand. **[Established that there is no consensus theory, as of 2026; which candidate is right is Contested, open.]**

### Stuck #2 — the law predicts loss, and loss is not capability

The clean, reliable, predictable quantity is the **loss** — the next-token mistake-count. But nobody wants low loss for its own sake; they want a model that can **reason, code, plan, tell the truth.** And the map from loss to those capabilities is **loose, jumpy, and task-by-task** — which is exactly why "emergence" *looks* like magic (the rung owns emergence and the scoring-trick debate — pointed at, not re-argued). So the most trustworthy thing on this page predicts the **wrong target.** You can bank the loss curve with confidence and *still* not know what the finished model will be able to *do* — the GPT-4 team said as much when they admitted some capabilities "remain hard to predict." The instrument is precise about a number that is only **loosely** tied to what you actually care about. This sharpens the card's Stuck #2 and #3 into one mechanical point: **predictability lives on the loss axis; capability lives on a different, blurrier axis; and the bet quietly assumes the two are the same line.** **[Established that loss is what's predictable and capability is not tightly tied to it; how loose the tie is, is Contested.]**

### Stuck #3 — the exponents are cruel: diminishing returns are built into the law

Return to the small exponents from Part 1 (α ≈ 0.34, β ≈ 0.28). They are not a detail — they are a **structural verdict.** Because they sit well below 1, every further equal drop in a penalty costs a **multiplying** amount of compute: roughly 8× the size to halve the size-penalty, then 8× again, then 8× again. So "keep scaling" is not walking a flat road — it is climbing a slope that **gets steeper at a fixed rate forever.** The very same power law that makes progress *predictable* also makes it *predictably ruinous*: to keep the loss falling in equal steps, the money must rise in multiplying leaps. Stack this on the data wall (Part 5) and the physical ceilings the [physical-bounds cross-cutting page](../30-across-the-approaches/01_the-bounds-data-compute-energy.md) treats in full (compute, energy, cost — pointed at, its home), and you get the real reason the field is hunting new axes: **the old axis still works, it just costs exponentially more per unit of progress, and the world has finite chips, text, and electricity to feed it.** The instrument that promised cheap prediction quietly encodes expensive progress. **[Established — this is a direct reading of the fitted exponents.]**

### Stuck #4 — the instrument was wrong once, quietly, for two years

Part 4 is not just history; it is a standing warning about the instrument's **epistemic fragility** *(epistemic = about how we know things; here, how easily our confident knowledge can be quietly mistaken)*. The lesson generalises past the specific 2020 mistake: the exponents you extrapolate are **downstream of experimental choices** — which parameters you count, how you set the learning-rate schedule on the small runs, what data you fit on, how you score. A small, reasonable-looking choice moved the compute-optimal point by ~3× and misdirected the whole field, and **the wrong line looked exactly as clean as the right one.** So "we can predict the future" carries an unstated clause: *provided we measured the present correctly* — and we have a worked example proving we can fail that clause without noticing for years. Every current extrapolation to AGI rests on today's fits being free of a bias we can't yet see. History says: do not bet the clean line is bias-free just because it is clean. **[Established — the 2020→2022 correction is the existence proof.]**

### The big question under all four

The card asked: *is scale enough to reach a general mind?* The instrument answers a sharper, mechanical version: **can you trust the line far enough to bet the future on it?** And the honest answer from all four cracks is: *the line is superb inside the range you fit it, and a leap of faith the moment you leave it.* It is the best **interpolator** in AI *(interpolator = something that fills in answers **between** points you have actually measured)* — ask it about a model between the ones you measured and it is almost never wrong. But every use that matters — "will a model 1,000× bigger be generally intelligent?" — is an **extrapolation** *(extrapolation = stretching a pattern **beyond** the range you measured, into territory nobody has visited)* far past the measured range, of a curve with **no theory** (Stuck #1), predicting the **wrong target** (Stuck #2), on a road that gets **exponentially costlier** (Stuck #3), fitted by a process that has **misled the field before** (Stuck #4). None of that makes the law fake — it makes it an **instrument with a clearly marked safe range**, being read confidently far outside it. **As of July 2026, the scaling law is the most reliable fact in AI and the least safe thing to extrapolate — and the whole "make it bigger" bet is a bet that you can read this particular instrument past the last mark on its dial.** The engine works beautifully; the question is whether "works where we've measured" is the same as "works where we want to go." **[Contested — the key open question, now located precisely: it lives in the gap between interpolating a fitted law and extrapolating an un-derived one.]**

---

## ⚠️ Honesty box

- **The equation is the durable core; the coefficients are snapshots.** The *shape* — `loss = floor + size-penalty + data-penalty`, and `compute ≈ 6 × params × tokens` — is a core idea that will still be central in a decade. The specific **coefficients** — the fixed fitted numbers in the equation (E ≈ 1.69, A, B, α ≈ 0.34, β ≈ 0.28, the "6", the Chinchilla ratio) — are 2020–2022 fits for particular models and data, and they move with architecture, data, and precision. Learn the two equations; treat every coefficient as dated. **[Established for the shape; the numbers are snapshots.]**
- **"You can predict the future" is true and narrow.** The line predicts **loss**, by **interpolation**, inside the range you measured — and it is genuinely excellent at that (GPT-4 from 1/1,000th the compute). It does **not** reliably predict **capabilities**, and it is **not** a measurement once you extend it far past your data — there it is a bet. Keep "interpolate loss" (solid) and "extrapolate to AGI" (hope) firmly apart. **[Established → Contested along that line.]**
- **A clean line is not a correct line.** The 2020 law was as smooth and convincing as any chart in AI, and it was pointing the wrong way for two years. Smoothness measures how well the curve fits the runs you did; it says nothing about whether those runs were biased. Always ask *how the small models were measured* before trusting a scaling extrapolation. **[Established — the Kaplan→Chinchilla correction is the proof.]**
- **No theory is the quiet problem.** We steer the most expensive projects in technology by a curve we cannot derive from first principles. That is not a reason to dismiss it — it works — but it *is* a reason to distrust any confident claim about where the line goes next. "It's been straight so far" is the whole of the evidence, and power laws in nature do eventually bend. **[Established that there's no consensus theory; Contested where it bends.]**
- **The knobs are multiplying, and there are only so many.** Small exponents mean each step costs many times more; the data wall, compute limits, and energy limits (the [physical-bounds page](../30-across-the-approaches/01_the-bounds-data-compute-energy.md)) are real ceilings. "Just keep scaling" is running into arithmetic, not just into doubt. The 2026 move to test-time compute and better data is the field voting with its budget. **[Established.]**
- **Numbers and model names age fast.** Kaplan (2020), Chinchilla (2022), GPT-4's 1/1,000th, the 4-epoch repeat rule, the precision law, o1's two axes — all dated snapshots in a fast corner. The lasting parts are the **two equations**, the **fit-and-extrapolate** method, the **measured-not-derived** warning, and the **loss-is-not-capability** gap. **[Established core, dated specifics.]**

---

## How to use this (if you want to direct AI work)

- **Learn the two equations by heart; they are your X-ray.** `loss = E + A/N^α + B/D^β` and `C ≈ 6ND`. With them you can sanity-check almost any scaling claim with a quick rough calculation: what's the budget, what's the size-data split, is it near the compute-optimal point, how much loss is even reachable above the floor. A team that can't write these two lines does not yet understand its own training run.
- **Always separate "interpolate" from "extrapolate."** A prediction *inside* the measured range (a model between sizes you've trained) is trustworthy engineering. A prediction *far past* it (this line reaches AGI) is a bet on an un-derived curve. Ask which one is being sold to you — the same chart is used for both, and only one of them is safe.
- **Interrogate how the small models were measured.** (Stuck #4.) Before you believe any fitted scaling law, ask the unglamorous questions: which parameters were counted, was the learning-rate schedule matched to each run, what data was it fit on, how was the score computed? A subtle answer to any of these can move the optimum by 3× — it did for the whole field once.
- **Ask what the law is predicting — loss or capability.** (Stuck #2.) "The scaling law says the next model will be much better" almost always means *lower loss*, which is only loosely tied to *what it can do*. Demand the capability evidence separately; do not let a confident loss curve stand in for a capability you actually need.
- **Treat "scale" as a portfolio of knobs, not one dial.** (Part 5.) In 2026 the returns are shifting from raw pre-training size to **data quality, repeated-data budgets, precision, and test-time compute.** Point your bets where the marginal FLOP still buys the most, and expect that place to keep moving off "bigger base model."
- **What you delegate vs what you keep.** *Delegate:* running the training, the curve-fitting, the hardware, the exact coefficient estimates. *Keep for yourself:* the judgement of how far the line can be trusted, the discipline of separating interpolation from extrapolation, the habit of auditing how a law was measured, and the refusal to mistake a low predicted loss for a capability the model has actually shown.

---

## Connections

- **Keep only three things:** ① The "steady line" is one equation — **`loss = E + A/N^α + B/D^β`** — a floor you can't beat (the entropy of text), plus a **size-penalty** you pay down with parameters and a **data-penalty** you pay down with tokens; the exponents are **small**, so equal progress costs multiplying compute. ② A second equation, **`compute ≈ 6 × parameters × tokens`**, turns a budget into a fixed `N × D`, so size and data **trade off**, and finding the lowest-loss split on that budget line **is** Chinchilla's balance rule (a solved math problem, not a guess). You **fit** these on cheap small models and **extend the line** to predict a giant one — real: GPT-4's loss was called from 1/1,000th the compute. ③ But the instrument is only safe **inside** the measured range: it was **mis-measured for two years** (Kaplan→Chinchilla), it predicts **loss not capability**, it has **no theory** under it, and its cruel exponents make progress **exponentially costlier** — so extrapolating it to AGI is a leap of faith, not a calculation.
- **This deep dive branches off:** [AP1 · scale & foundation models](../20-the-approaches/01_ap1-scale-and-foundation-models.md) — the card owns the *bet, the Bitter Lesson, foundation models, the "surprise skills" debate, Chollet's "skill is not intelligence," the data wall as a bet-crack,* and the *four cracks in the bet*; and the [scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — which owns the *straight line / power law, the log-log plot, the floor, Chinchilla's balance answer, the data wall, and emergence + the mirage debate*. This page opens the *equations* under that line (the three-piece loss formula + the `6ND` compute identity), the *fit-and-extrapolate method*, the *measurement bug*, and the *2026 re-fits*, and judges the *instrument's own* trustworthiness.
- **Where it points:** [AP2 · reasoning & test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — owns the *mechanism* of the new answer-time axis this page only shows the scaling-shape of; the [physical-limits cross-cutting page](../30-across-the-approaches/01_the-bounds-data-compute-energy.md) — owns the *compute, data, and energy ceilings* that the cruel exponents (Stuck #3) run into; and the [alignment & self-improvement page](../30-across-the-approaches/02_alignment-control-and-self-improvement.md) — where "we can't predict what capabilities a bigger model will have" (Stuck #2) becomes a safety problem, not just an engineering one.
- **How sure are we?** That the loss follows the three-piece equation, that `C ≈ 6ND`, that labs fit-and-extrapolate it, and that the 2020 law was mis-measured and corrected in 2022 — **[Established]**. That there is *no consensus theory* of why the power law holds — **[Established, as of 2026]**. Which candidate theory is right, how loosely loss ties to capability, and how far the line can be safely extrapolated — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Write the **loss equation** `L(N, D) = E + A/N^α + B/D^β` and say, in plain words, what each of the three pieces is. Which piece can scaling **never** remove, and why?
2. Why are the **small exponents** α, β "cruel"? Roughly how much must you multiply the size by to **halve** the size-penalty when α ≈ 0.34 — and what does that say about the cost of "just keep scaling"?
3. State the **compute identity** and explain where the **"6"** comes from (forward vs backward pass). Why does a **fixed budget** force a trade-off between size and data, and how does that turn "how big?" into a **solved** problem?
4. Describe how a lab **reads the future off the line** in three steps. What did the GPT-4 team predict, from how little compute, and why does "without use of any partial results" matter?
5. The 2020 scaling law pointed the field at the **wrong shape of model** for two years. Give the **two measurement causes**, and state the general lesson about trusting any empirical fit.
6. Name the three **2026 re-fits** of the law (repeated data, precision, test-time compute) and say, in one line each, what new thing each one adds.
7. The big one: the law is "the most reliable fact in AI and the least safe thing to extrapolate." Name the **four engine cracks** and explain why each makes *stretching the line to AGI* a bet rather than a calculation.

## Revision notes

*Newest first.*
- `rev 1 (2026-07-17)` — created as the **first AP1 deep-dive** (reading group **⑤ Deep dives**, sortkey 5007), branching off the [AP1 card](../20-the-approaches/01_ap1-scale-and-foundation-models.md) and the [scaling-laws rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md); the seventh module in group ⑤ (after the AP8 trilogy + AP4 #1 + AP5 #1 + AP9 #1). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the rung's *straight line / power law / log-log plot / the floor / Chinchilla's balance answer / the data wall / emergence + mirage* and the card's *bet / Bitter Lesson / foundation models / "skill is not intelligence" / the four bet-cracks* are **referenced, never re-taught**; [AP2](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)'s *test-time-compute mechanism* is **pointed at, not opened** (only the scaling-law *shape* of the new axis is built here); the [physical-limits page](../30-across-the-approaches/01_the-bounds-data-compute-energy.md)'s *compute/data/energy ceilings* are pointed at for Stuck #3. This page adds only the new **mechanism/instrument** layer the card and rung skipped: the **three-piece loss equation** `E + A/N^α + B/D^β` (irreducible entropy floor + finite-size penalty + finite-data penalty; the cruelty of small exponents — Part 1); the **compute identity** `C ≈ 6ND` (2N forward + 4N backward per parameter-token; the fixed budget as a constrained optimisation whose solution *is* compute-optimal training — Part 2); the **fit-and-extrapolate methodology** (a ladder of small models → fit the five pieces → extend the line; GPT-4 predicted from 1/1,000th the compute — Part 3); the **Kaplan→Chinchilla measurement bug** (non-embedding-parameter counting + an unmatched learning-rate schedule → a ~3× wrong optimum for two years — Part 4); and the **2026 frontier** (data-constrained/repeat-epoch scaling; precision scaling / effective-parameter-count; the test-time-compute new axis — Part 5). Grounded in **written, quotable** sources, each verified as an exact contiguous string: **Chinchilla** (Hoffmann et al., 2022 — the three-term "first term…entropy of natural text…" risk-decomposition passage; coefficients E ≈ 1.69, A ≈ 406.4, B ≈ 410.7, α ≈ 0.34, β ≈ 0.28), **Kaplan** (2020 — the `C ≈ 6N` per-token and `C_forward ≈ 2N` compute mechanics, rendered as mechanism), the **GPT-4 Technical Report** (2023 — "predict…no more than 1/1,000th the compute" + "without use of any partial results"), **Muennighoff et al.** (2023 — "up to 4 epochs of repeated data yields negligible changes to loss…the value of adding compute eventually decays to zero"), **Kumar et al.** (2024 — "training in lower precision reduces the model's 'effective parameter count'" + post-quantization data-harm line), the **o1 blog** (OpenAI 2024 — the two-axes train-time/test-time line), and **Lilian Weng** (June 2026 — the "no consensus theory" line). Full live-SOTA pass (**July 2026**), each fast fact dated: the Kaplan–Chinchilla reconciliation (2024, non-embedding-parameter counting as the primary cause + learning-rate schedule); the pretraining-plateau / test-time-compute shift; the candidate theories (data-manifold-dimension; the quantization/quanta model) with no winner. Four **engine** cracks (distinct from the card's bet-cracks): **measured, not derived — no theory** (sharpens "is scale enough?") · **the law predicts loss, and loss ≠ capability** (mechanical face of the emergence + skill-vs-intelligence cracks) · **the exponents are cruel — diminishing returns are structural** (the arithmetic under the data/compute wall) · **the instrument was mis-measured once, for two years** (epistemic fragility) — under the big question: *the scaling law is the most reliable fact in AI and the least safe thing to extrapolate; the bet is that you can read this instrument past the last mark on its dial.*

---
*This is the first AP1 deep dive — the **equation** beneath the "make it bigger" line. Its `6ND` budget is the same compute the [AP9 · open-ended engine](06_ap9-deep-dive-the-open-ended-engine.md)'s foundation-model operator spends; its "new axis" hands to [AP2 · reasoning](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md); and its cruel exponents run into the [physical limits](../30-across-the-approaches/01_the-bounds-data-compute-energy.md). To pick the next approach to go deep on, return to the [spine](../APPROACHES_TO_AGI.md).*
