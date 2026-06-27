---
id: c-machine-learning
sortkey: 1000
title: Machine learning — learning from examples
domains: [machine-learning, machine-intelligence]
level: core
prereqs: [c-learning, c-probability, c-linear-algebra]
provides: [model, parameters-weights, training-vs-inference, features, loss-function, gradient-descent, train-val-test-split, bias-variance, hyperparameters, classical-ml, ml-pipeline]
resources: [r-cs229, r-isl, r-geron-homl, r-raschka-ml, r-d2l]
status: ready
reading_time: 12 min
rev: 1
created: 2026-06-27
updated: 2026-06-27
---

# Machine learning — learning from examples
*This opens the machine-intelligence chapter. After it you'll know what a "model" actually is, how one is trained by rolling downhill on its errors, the handful of moving parts in **every** ML system (data → features → model → loss → optimizer → evaluation), and why "AI" is far broader than the deep learning everyone talks about.*

## Why this rung matters
Everything ahead — neural nets ([1100](1100_neural-networks-deep-learning.md)), RL ([1200](1200_reinforcement-learning-and-agents.md)), LLMs ([1300](1300_language-models-how-llms-work.md)) — is a *special case* of what's on this rung. Machine learning (ML) is the concrete machinery that turns the **error-reducing loop** of [0600](../00-foundations/0600_what-it-means-to-learn.md) into running code. Get the vocabulary and the pipeline here, once, and the rest of the chapter stops being four mysteries and becomes variations on one machine.

## The idea (start concrete)
You want to predict a house's price. The old way: hire an expert to write rules — *"add $200/sq-ft, +$30k for a garage, −$50k near a highway…"* Brittle, and someone has to know the rules.

The ML way: collect **10,000 past sales** (size, bedrooms, location, … → the price it sold for), and let a program **find the rule itself** by adjusting numbers until its guesses match the real sales. That program-with-adjustable-numbers is a **model**.

> **Model** = a function with **tunable knobs** that maps an input to an output. The knobs are its **parameters** (also called **weights**). *Learning = finding the knob settings that make the model's outputs match reality.* That's the whole game.

A house-price model might be `price = w₁·(size) + w₂·(bedrooms) + w₃·(location-score) + b`. The `w`'s and `b` are the parameters. Untrained, they're random and the guesses are garbage. **Training** is the process of tuning them on data; **inference** is using the finished model to predict on a new house. (Recall [0400](../00-foundations/0400_computation.md): the trained model is *grown* software — its behavior lives in learned **data** (weights), not hand-written rules.)

## The five parts in every ML system
Strip any ML system — a spam filter, a face recognizer, ChatGPT — to the same skeleton:

1. **Data** — labelled examples (input → answer) for supervised learning ([0600](../00-foundations/0600_what-it-means-to-learn.md)). The fuel. Quality and quantity usually matter more than the algorithm.
2. **Features** — the *input numbers* the model actually sees. Raw data (a photo, a sentence, a customer record) must become numbers — a **vector** ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)). Choosing/engineering good features used to be the core craft of ML ("**feature engineering**"). *The deep-learning revolution was largely about making the model **learn its own features** instead — picked up at [1100](1100_neural-networks-deep-learning.md).*
3. **Model** — the function with the knobs (above). Its shape encodes an **inductive bias** ([0600](../00-foundations/0600_what-it-means-to-learn.md)): a straight-line model can only learn straight-line patterns.
4. **Loss function** — a single number measuring **how wrong** the model is on the data (e.g. average squared error between guessed and real prices). This is the **objective** of [0600](../00-foundations/0600_what-it-means-to-learn.md) made concrete — *and the thing you must guard*, because the model will optimize exactly this, not what you meant (Goodhart, [0600](../00-foundations/0600_what-it-means-to-learn.md)).
5. **Optimizer** — the procedure that adjusts the knobs to shrink the loss. Almost always: **gradient descent**.

## Gradient descent — the famous downhill walk (promised at 0600)
Picture the loss as a **landscape**: every possible setting of the knobs is a location, and the height is *how wrong* the model is there. You want the lowest valley. You can't see the whole map (too many knobs), but at your current spot you *can* feel **which way is downhill** — that direction is the **gradient**. So:

> **Gradient descent:** measure the error → compute the downhill direction (the gradient) → take a small step that way → repeat. Slowly roll toward less error.

That's it — the error-reducing loop of [0250](../00-foundations/0250_feedback-loops-and-control.md)/[0600](../00-foundations/0600_what-it-means-to-learn.md), run on numbers. The step size is the **learning rate** (too big → you overshoot and bounce; too small → you crawl). Training a neural net with billions of knobs is *the same idea at scale* — which is why "AI is mostly matrix multiplication on a GPU" ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)): computing gradients over huge weight-matrices, millions of times. **[Established]**

## The two failure modes, operationalized
[0600](../00-foundations/0600_what-it-means-to-learn.md) warned of **underfitting** (too simple) vs **overfitting** (memorizing noise). ML makes this measurable and gives it a name — the **bias–variance trade-off**:
- **High bias** = the model is too rigid to fit the real pattern (underfit).
- **High variance** = the model is so flexible it fits the *random quirks* of this particular dataset, and flails on new data (overfit).
You tune model complexity to balance them. And the **only honest referee** is the held-out test from [0600](../00-foundations/0600_what-it-means-to-learn.md), now operationalized as a **three-way split**:

> **Train** (tune the knobs) · **Validation** (tune your *choices* — see below) · **Test** (touch **once**, at the very end, to get an honest score). Score on the training data is meaningless; a model can ace what it has already seen.

This is also the difference between two kinds of knobs. **Parameters** are learned by the optimizer (the `w`'s). **Hyperparameters** are settings *you* choose — learning rate, model size, how long to train — and you pick them using the validation set, never the test set.

## The landscape beyond deep learning (don't skip this)
"AI" in the headlines means deep learning, but a huge share of ML in the real world is **classical** and often *better* for the job. The greatest hits, as a map (each is just a different model shape + inductive bias):
- **Linear / logistic regression** — straight-line and S-curve fits. Boring, fast, interpretable, shockingly hard to beat as a baseline.
- **Decision trees → random forests / gradient boosting** (e.g. XGBoost) — flowchart-of-questions models, combined in ensembles. **Still the top performers on *tabular* data** (spreadsheets — fraud, churn, credit, most business data). **[Established]**
- **k-nearest-neighbours** — "predict like the most similar past examples" (similarity = the dot product of [0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)).
- **Support-vector machines** — the max-margin separator that ruled ML before deep learning.
- **k-means / clustering** — the workhorse of **unsupervised** learning ([0600](../00-foundations/0600_what-it-means-to-learn.md)): find groups no one labelled.

The standing reference course is `r-cs229`; `r-isl` is the gentle classic; `r-geron-homl`/`r-raschka-ml` are the hands-on books.

## ⚠️ Honesty box: where ML quietly goes wrong
- **"AI = deep learning" is false.** Most deployed, money-making ML is classical, on tabular data. Reaching for a neural net first is a common rookie mistake. **[Established]**
- **Garbage in, garbage out.** The model inherits every bias, gap, and error in the data. *Most ML failures are data failures, not algorithm failures.* (Data as fuel → [1600](../50-world-and-society/).)
- **Data leakage** — the silent killer. If a clue to the answer sneaks into the features (e.g. a column that only exists *after* the outcome), the model looks brilliant in testing and collapses in production. A 99% score usually means a leak, not a miracle.
- **The metric isn't the goal.** 99% accuracy is worthless if 99% of emails aren't spam — predict "not spam" always and you score 99% while catching nothing. Choosing the *right* measure is a judgement call, not a default.

## How a director uses this
- **The leverage is in 1, 2, and 4 — not 3.** Data, features, and the loss/objective decide outcomes far more than which algorithm you pick. Spend your attention there. (This is the [0600](../00-foundations/0600_what-it-means-to-learn.md) thesis, now concrete: *pick the feedback and you've designed the learner.*)
- **Demand the held-out number, and ask how the split was made.** "It works" on training data is the oldest lie in ML. Insist on a test score on data the model never saw — and that no leakage contaminated it.
- **Right-size the method.** Tabular/small-data problem? Start with gradient boosting or plain regression — cheaper, faster, interpretable, often better. Save deep learning for perception and language ([1100](1100_neural-networks-deep-learning.md)).
- **What you delegate:** the model code, the gradient math, the hyperparameter search. **What you own:** the data and its integrity, the objective/loss, the evaluation design, and the judgement of whether a number is real or leaked.

## Connections
- **Stands on:** [0600 Learning](../00-foundations/0600_what-it-means-to-learn.md) (this is its concrete machinery), [0500 Probability](../00-foundations/0500_probability-and-uncertainty.md) (why small samples mislead → val/test), [0350 Linear algebra](../30-math-and-theory/0350_just-enough-linear-algebra.md) (data as vectors; training as matrix math), [0250 Feedback](../00-foundations/0250_feedback-loops-and-control.md) (gradient descent = the error-reducing loop).
- **Leads to:** neural nets, which *learn their own features* and scale gradient descent to billions of knobs ([1100](1100_neural-networks-deep-learning.md)); RL, which learns from reward instead of labels ([1200](1200_reinforcement-learning-and-agents.md)); scaling laws ([1700](../20-machine-intelligence/)); data-as-fuel ([1600](../50-world-and-society/)).
- **Contested?** Models/parameters/loss/gradient-descent/train-test-split, "classical ML wins on tabular" — **[Established]**. Nothing here is speculative; the debates begin once we add depth and scale.

## Proof-of-learning *(do one, from memory)*
1. Define **model**, **parameter**, and **loss function** in one sentence each, then explain how gradient descent uses all three.
2. Why is a 99% score on the **training** set close to meaningless? What's the fix, in three words?
3. A teammate's fraud model scores 99.9% in testing but fails in production. Name the two most likely culprits from this rung.
4. You have 5,000 rows of customer data in a spreadsheet and need to predict churn. What kind of model would you *start* with, and why not a deep neural net?

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-27)` — created. Opens the machine-intelligence chapter. *("Boosting wins on tabular" is current as of 2026; re-check as deep-tabular methods improve.)*

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md). Next rung: artificial neural networks ([1100](1100_neural-networks-deep-learning.md)) — where the model learns its own features.*
