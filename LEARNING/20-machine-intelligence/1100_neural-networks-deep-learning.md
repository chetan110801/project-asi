---
id: c-neural-networks
sortkey: 1100
title: Neural networks & deep learning
domains: [machine-learning, deep-learning, machine-intelligence]
level: core
prereqs: [c-machine-learning, c-brain, c-linear-algebra]
provides: [artificial-neuron, activation-function, layers-depth, backpropagation, deep-learning, representation-learning, cnn, rnn-lstm, embedding-latent-space, universal-approximation]
resources: [r-nielsen-nndl, r-goodfellow-dl, r-prince-udl, r-karpathy-zth, r-d2l]
status: ready
reading_time: 13 min
rev: 1
created: 2026-06-27
updated: 2026-06-27
---

# Neural networks & deep learning
*After this rung you'll understand what a neural network actually is (stacked simple units doing matrix math), the one trick that makes "deep" learning special — **the model learns its own features** — how training assigns blame across millions of knobs (backpropagation), and why this approach waited decades for GPUs and data before it conquered AI.*

## Why this rung matters
Neural nets are the engine under almost every headline AI: vision, speech, and the LLMs of [1300](1300_language-models-how-llms-work.md). They're not a new *kind* of learning — they're the [1000](1000_machine-learning-from-examples.md) machine (model + loss + gradient descent) with a particular, enormously flexible model shape. The payoff is one idea worth more than the rest combined: **representation learning** — instead of you hand-crafting features ([1000](1000_machine-learning-from-examples.md)), the network *discovers* them. That shift is most of the modern AI revolution.

## The idea (start concrete)
Take the classic task: read a handwritten digit (a 28×28 grid of pixels → "that's a 7"). Hand-writing rules for "7-ness" is hopeless. A neural net learns it.

The basic unit is the **artificial neuron**, a deliberate caricature of the brain's sum-and-fire cell ([0700](../10-minds/0700_the-brain-working-model.md) — we *don't* re-explain biology here):
- it takes several inputs (the pixels, or outputs of earlier units),
- multiplies each by a **weight** (a knob — [1000](1000_machine-learning-from-examples.md)) and **adds them up** (a weighted sum — exactly the **dot product** of [0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)),
- then passes the total through a simple **activation function** that bends it — most just "keep it if positive, else zero" (called ReLU).

That last bend is the secret ingredient. Without it, stacking neurons would collapse into one big straight-line model (no matter how many layers). The **non-linearity** is what lets the network represent curves, corners, and arbitrarily complex patterns. **[Established]**

## Layers, depth, and why "deep"
Wire these neurons in **layers**: inputs → a hidden layer → another hidden layer → … → output. Each layer is, mathematically, **multiply by a weight matrix, then apply the activation** — the "matrices = motion" of [0350](../30-math-and-theory/0350_just-enough-linear-algebra.md), stacked. "**Deep** learning" just means *many* such layers.

Why does depth matter? Because each layer builds on the previous one's outputs, the network learns a **hierarchy of features**:

> For images: layer 1 finds **edges** → layer 2 assembles edges into **shapes/textures** → layer 3 into **parts** (an eye, a wheel) → later layers into **objects** (a face, a car). Nobody programmed "edge" or "eye." The network **invented these features on its own** to minimize its loss.

This is **representation learning**, and it's the whole point. The [1000](1000_machine-learning-from-examples.md) craft of feature engineering — humans deciding what the model should look at — is replaced by the model **learning the right representation** end-to-end, straight from raw pixels or text. The internal numbers a layer produces are an **embedding** / a point in a **latent space** ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md): a vector *is* meaning; nearby = similar). The network's "understanding" lives in these learned representations. **[Established]**

## Backpropagation — assigning blame across a million knobs
A deep net has millions to billions of weights. Gradient descent ([1000](1000_machine-learning-from-examples.md)) still works, but how do you know which way is "downhill" for a knob buried five layers deep? Answer: **backpropagation** ("backprop").

The intuition: run an example forward, measure the error at the output, then **push that error backwards** through the layers, handing each weight its **share of the blame** — "you contributed *this much* to the mistake, so adjust *this much*." (Mechanically it's the chain rule from calculus applied layer by layer; you direct it, you don't derive it.) It's the **credit-assignment** problem solved efficiently — and it's the same loop as always: guess → measure error → assign blame → nudge every knob downhill → repeat ([0250](../00-foundations/0250_feedback-loops-and-control.md)/[0600](../00-foundations/0600_what-it-means-to-learn.md)). **[Established]** (1986 Rumelhart–Hinton–Williams; the algorithm that made deep nets trainable.)

## Why it waited 30 years (the strategic lesson)
The core ideas are old (1950s–80s). Deep learning only *exploded* around 2012 (AlexNet winning ImageNet) because three things finally arrived together:
1. **Compute** — GPUs turned out to be perfect for the dense matrix math ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)); what took weeks now took hours (→ chips, [1400](../40-compute-and-physical/)).
2. **Data** — the internet produced labelled datasets big enough to feed millions of knobs (→ [1600](../50-world-and-society/)).
3. A few **engineering tricks** (better activations, normalization, residual connections) that let very deep nets train without falling apart.

> This is the **Bitter Lesson** of [0600](../00-foundations/0600_what-it-means-to-learn.md) in the flesh: a general method that *learns its own features* + scale beat decades of hand-crafted computer-vision cleverness, almost overnight. **[Likely → Contested]** as a law, but it is the pattern the whole field now bets on.

## Architectures = inductive bias (a quick map)
The *shape* of the network bakes in an assumption about the data ([0600](../00-foundations/0600_what-it-means-to-learn.md), inductive bias). The greatest hits:
- **Convolutional nets (CNNs)** — bake in "nearby pixels relate, and a pattern is the same wherever it appears." The workhorse of **vision** for a decade. **[Established]**
- **Recurrent nets (RNNs / LSTMs)** — process sequences step-by-step with a memory. Once the default for text/speech; now **largely superseded** by the transformer (next paragraph). **[Established]**
- **Transformers** — the architecture behind modern LLMs. It replaced recurrence with **attention** (let every element look directly at every other). It's important enough that its mechanism gets its **own home at [1300](1300_language-models-how-llms-work.md)** — here just note it *is* a neural net, and it won because it parallelizes on GPUs and scales. **[Established]**

A theory note worth holding lightly: **universal approximation** says a big enough network can *represent* essentially any function. **[Established]** — but that only promises a setting of the knobs *exists*, not that gradient descent can *find* it from finite data. Representability ≠ learnability; don't let the theorem oversell what nets can actually learn.

## ⚠️ Honesty box: the price of the power
- **They're black boxes.** A trained net is millions of numbers with no human-readable logic. *Why* it decided something is often genuinely unknown — the motivation for **interpretability** research ([1900](../60-frontier/)). **[Established]**
- **Data-hungry.** They need far more examples than a human (or a child — [0800](../10-minds/0800_child-mind-bootstraps.md)). Sample-inefficiency is a real, unsolved gap.
- **Brittle / fooled.** Tiny, deliberate perturbations invisible to you (**adversarial examples**) can flip a confident answer. Confidence ≠ correctness.
- **Not the brain.** Reuse the whole [0700](../10-minds/0700_the-brain-working-model.md) honesty box: ~megawatts vs ~20 watts, no continual learning (catastrophic forgetting), and the artificial neuron is a cartoon. "Neural" is an inspiration, not a copy. **[Established]**

## How a director uses this
- **Reach for deep learning when the input is raw and unstructured** — images, audio, text — where the value is in *learning the representation*. For tidy tabular data, classical ML still wins ([1000](1000_machine-learning-from-examples.md)). Match the tool to the data.
- **The architecture is a bet about your data's structure.** Choosing CNN vs transformer vs something else is choosing an inductive bias. It's a design decision with real consequences, not a default.
- **Budget for the three enablers.** Deep learning is a compute + data + talent purchase. If you can't feed it data or pay for the GPUs, its advantage evaporates.
- **Treat the black box as a risk to manage,** not a detail to ignore — demand evaluation on held-out and adversarial cases, and watch for interpretability tooling as it matures.
- **What you delegate:** the architecture code, backprop, the training run. **What you own:** the data, the choice of architecture-as-bias, the eval, and honest accounting of brittleness and opacity.

## Connections
- **Stands on:** [1000 Machine learning](1000_machine-learning-from-examples.md) (model + loss + gradient descent — nets are a model shape), [0700 The brain](../10-minds/0700_the-brain-working-model.md) (the neuron it abstracts, and the gaps it inherits), [0350 Linear algebra](../30-math-and-theory/0350_just-enough-linear-algebra.md) (layers = matrix multiply; embeddings = vectors).
- **Leads to:** the **transformer** and LLMs ([1300](1300_language-models-how-llms-work.md)), deep **reinforcement** learning ([1200](1200_reinforcement-learning-and-agents.md)), why scale keeps paying ([1700](../20-machine-intelligence/)), the compute it demands ([1400](../40-compute-and-physical/)), and interpretability/alignment ([1900](../60-frontier/)).
- **Contested?** Neurons/layers/backprop/representation-learning/CNN/RNN — **[Established]**. "Scale + depth is the path" — **[Likely → Contested]**. Universal approximation is proven but routinely over-claimed (representability ≠ learnability).

## Proof-of-learning *(do one, from memory)*
1. What does a single artificial neuron compute, and why is the **activation function** essential (what breaks without it)?
2. Explain **representation learning** with the digit/edges→objects example — and say what job it eliminates from the [1000](1000_machine-learning-from-examples.md) pipeline.
3. In one sentence each: what problem does **backpropagation** solve, and why did deep learning take off around 2012 and not 1990?
4. Name two failure modes from the honesty box and how you'd test for each before shipping.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-27)` — created. *(Architecture landscape current as of 2026 — transformers dominant, RNNs superseded; re-check as post-transformer work matures, [1300](1300_language-models-how-llms-work.md).)*

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md). Next: learning from **reward** instead of labels — reinforcement learning & agents ([1200](1200_reinforcement-learning-and-agents.md)).*
