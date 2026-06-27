---
id: c-language-models
sortkey: 1300
title: Language models (LLMs) — how they actually work
domains: [machine-learning, nlp, deep-learning, machine-intelligence]
level: core
prereqs: [c-neural-networks, c-entropy, c-reinforcement-learning]
provides: [next-token-prediction, llm, tokenization, transformer-attention, context-window, pretraining-finetuning, instruction-tuning, rlhf, in-context-learning, chain-of-thought-test-time-compute, hallucination, foundation-model]
resources: [r-slp3, r-cs336, r-handson-llm, r-karpathy-zth, r-cs224n]
status: ready
reading_time: 15 min
rev: 1
created: 2026-06-27
updated: 2026-06-27
---

# Language models (LLMs) — how they actually work
*The payoff of the chapter. After this rung you'll understand what an LLM really is (a next-word predictor trained on the internet), the one architecture that made it possible (the transformer, via **attention**), the three stages that turn a raw predictor into a helpful assistant (pretrain → fine-tune → RLHF), why capabilities seem to "emerge" with scale, and — crucially — what these systems fundamentally **cannot** do, so you can tell real capability from hype.*

## Why this rung matters
LLMs are the most general, most consequential AI ever built, and the substrate you'll most likely be *directing* as a founder. They pull together the entire ladder: prediction and compression ([0300](../00-foundations/0300_information-and-entropy.md)), self-supervised learning ([0600](../00-foundations/0600_what-it-means-to-learn.md)), neural nets ([1100](1100_neural-networks-deep-learning.md)), and RL/RLHF ([1200](1200_reinforcement-learning-and-agents.md)). Understand this rung and the magic resolves into machinery you can reason about, budget for, and steer — without losing the genuine astonishment that it works at all.

## The one trick: predict the next token
At its core, an LLM does something almost laughably simple:

> **Given some text, predict the next chunk of text.** Then add that chunk and predict again. That's it.

It's your phone's autocomplete, scaled up by a factor of millions. The "chunks" are **tokens** — sub-word pieces (e.g. *"playing"* → `play` + `ing`); models read and write in tokens, not letters or whole words, which is why they sometimes miscount letters. The model outputs a **probability** ([0500](../00-foundations/0500_probability-and-uncertainty.md)) over *every* possible next token, and one is sampled.

Why is "predict the next word" enough to produce essays, code, and arguments? Because of the deep link from [0300](../00-foundations/0300_information-and-entropy.md): **to predict well, you must compress — and to compress text well, you must in effect *understand* it.** To reliably guess the next word of a murder mystery, a maths proof, or a Python function, the model is forced to internalize grammar, facts, reasoning patterns, and a working model of the world. *Prediction is the training task; understanding (of some kind) is what it squeezes out.* This is exactly the **predictive brain** of [0700](../10-minds/0700_the-brain-working-model.md), and the **self-supervised** engine of [0600](../00-foundations/0600_what-it-means-to-learn.md): the text **labels itself** (the next word is the answer), so the whole internet becomes a self-grading teacher — no human labelling, so training data is effectively unlimited. **[Established]** that this is the training objective; *what* the resulting "understanding" amounts to is the live debate below.

## The engine: the transformer and attention
The architecture that made this work at scale is the **transformer** (2017, *Attention Is All You Need*). It's a deep neural net ([1100](1100_neural-networks-deep-learning.md)), and its key move is **attention**:

> For each token, **attention** lets it **look back at every other token and pull in the ones that matter** for predicting what comes next. In *"The trophy didn't fit in the suitcase because **it** was too big,"* attention is how the model links *"it"* to *"trophy."*

Mechanically, "which earlier tokens matter" is scored by **similarity between their vectors** — the **dot product** of [0350](../30-math-and-theory/0350_just-enough-linear-algebra.md), now doing real work (each token becomes an **embedding**; attention measures how aligned they are). Two things made the transformer win over the older step-by-step RNNs ([1100](1100_neural-networks-deep-learning.md)):
1. **It processes the whole sequence in parallel** → it maps perfectly onto GPUs ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)/[1400](../40-compute-and-physical/)) → it could be trained on far more data.
2. **It connects distant words directly**, capturing long-range structure RNNs lost.

The amount of text the model can attend to at once is its **context window** (its working memory for this conversation). Everything outside it is forgotten — a key practical limit. **[Established]**

## From raw predictor to assistant: the three stages
A freshly pretrained model is *not* ChatGPT. It's a raw **next-token predictor** that will happily continue your text in any direction, helpful or not. Turning it into an assistant takes three stages — and knowing them is most of what a director needs:

1. **Pretraining** — the giant, expensive stage. Predict-the-next-token over a huge slice of the internet. Produces a **base model** (a.k.a. **foundation model**): vast knowledge and fluency, but no notion of "being helpful." This is where ~all the compute and data go ([1400](../40-compute-and-physical/)/[1600](../50-world-and-society/)). **[Established]**
2. **Supervised fine-tuning / instruction tuning** — show it many examples of *"instruction → good response."* Now it answers questions instead of just continuing text. Cheap relative to pretraining. **[Established]**
3. **RLHF (reinforcement learning from human feedback)** — the polish that aligned LLMs to people. Humans (or AIs) **compare** answers — *"A is better than B"* — that trains a **reward model**, and RL ([1200](1200_reinforcement-learning-and-agents.md), via PPO or simpler **DPO**) nudges the LLM toward preferred answers. This is what makes a model feel helpful, honest, and harmless rather than just plausible. **[Established]** — and note it's the [1200](1200_reinforcement-learning-and-agents.md) loop, inheriting all its **reward-hacking** risk (a model can learn to *sound* right / sycophantic rather than *be* right — Goodhart again, [0600](../00-foundations/0600_what-it-means-to-learn.md)/[0900](../10-minds/0900_evolution-and-general-intelligence.md)).

## Scale, emergence, and learning-at-inference
Two surprising behaviors define the LLM era:

- **Scaling & "emergence."** Make the model bigger, with more data and compute, and it gets predictably better at prediction — *and* new abilities (arithmetic, translation, reasoning) seem to appear rather suddenly past certain sizes. This is the engine of the whole field; the precise law (and how much to spend on size vs data) is **scaling laws**, its own rung ([1700](../20-machine-intelligence/)). Caveat worth holding: some argue "emergence" is partly a **measurement artifact** of sharp metrics, not a true phase change (Schaeffer et al., *Are Emergent Abilities a Mirage?*). **[Contested]** — know both sides.
- **In-context learning.** A pretrained LLM can learn a brand-new task *from examples in the prompt*, with **no weight changes at all** — show it three translations and it does the fourth. Learning at **inference** time, not training time. This is what makes **prompting** a real skill: you're programming the model with words. **[Established, still not fully understood]**

## Adding the "slow" mode: reasoning & test-time compute
Base LLMs are brilliant at the **fast, intuitive** thinking of [0700](../10-minds/0700_the-brain-working-model.md) and historically weak at **slow, deliberate** reasoning. Two linked ideas closed much of the gap:
- **Chain-of-thought** — prompt (or train) the model to *"think step by step,"* writing its reasoning out before answering. Working through it in tokens dramatically improves maths/logic. **[Established]**
- **Test-time / inference compute** — let the model *spend more computation thinking* before it answers (explore options, check itself). The **reasoning-model** era (OpenAI's o1 and successors, 2024→) is built on this: buy capability with thinking-time, not just bigger weights. It's the [0700](../10-minds/0700_the-brain-working-model.md) two-speed picture, finally giving AI a "System 2." **[Likely — recent, fast-moving; treat as a 2026 snapshot.]**

## ⚠️ Honesty box: what an LLM is *not*
This is the most over-hyped object in tech — calibrate hard:
- **It has no ground truth, so it hallucinates.** A next-token predictor optimizes for *plausible*, not *true*. It will state false things — fake citations, invented facts — **fluently and confidently**, because confidence and correctness are unrelated in its training. This is **confabulation**, and it's intrinsic, not a bug to be fully patched. Tools like **RAG** (retrieve real documents, then answer) and giving it search/tools ([1200](1200_reinforcement-learning-and-agents.md) agents) *reduce* it; they don't eliminate it. **[Established]**
- **It doesn't learn after training.** The weights are frozen; it has no memory beyond the **context window**. "It remembered" usually means text was fed back in, not that the model changed. **[Established]**
- **It's not a database or a calculator.** Knowledge is smeared across billions of weights, lossily. For exact facts/maths, pair it with real tools.
- **"Does it actually understand?"** The honest answer is *we don't fully know.* One camp: it's a **"stochastic parrot,"** stitching patterns with no comprehension. Another: to predict that well it must have learned genuine **world models** and abstractions; interpretability work finds real structured concepts inside ([1900](../60-frontier/)). **[Contested — genuinely open.]** Don't let anyone (hype or dismissal) tell you it's settled.
- **Jagged capability.** It can write a working program and then fail a child's riddle. Competence is **uneven and unpredictable** — never assume that brilliance on task A implies competence on task B. **[Established]**

## How a director uses this
- **You direct an LLM at four levers, in rising cost:** the **prompt / context** (cheap, immediate — in-context learning), **tools & retrieval** (RAG/agents — ground it, extend it), **fine-tuning / RLHF** (shape its behavior and values), and **pretraining** (almost never your job — you rent it). Reach for the cheapest lever that solves the problem.
- **Treat hallucination as a design constraint, not a defect to wait out.** Architect around it: retrieval, tool use, citations, human review for anything that matters. Owning this risk is your job, not the model's.
- **Buy "thinking time" when accuracy matters.** Reasoning/test-time-compute trades latency and cost for correctness — a real knob you control per query.
- **Evaluation is everything, because capability is jagged and confidence lies.** The team that wins builds trustworthy **evals** for *its* task on held-out cases ([1000](1000_machine-learning-from-examples.md)) — not vibes from a few impressive chats.
- **What you delegate:** the architecture, the training, the serving. **What you own:** the data and objective, the post-training behavior/values, the eval, the hallucination-mitigation design, and the choice of how much autonomy/tool-access to grant.

## Connections
- **Stands on:** [0300 Information & entropy](../00-foundations/0300_information-and-entropy.md) (predict ⇒ compress ⇒ understand — *the* reason next-token works), [0600 Learning](../00-foundations/0600_what-it-means-to-learn.md) (self-supervised), [1100 Neural nets](1100_neural-networks-deep-learning.md) (the transformer is a deep net; embeddings), [0350 Linear algebra](../30-math-and-theory/0350_just-enough-linear-algebra.md) (attention = dot-product similarity), [1200 RL](1200_reinforcement-learning-and-agents.md) (RLHF), [0700 Brain](../10-minds/0700_the-brain-working-model.md) (prediction machine; fast/slow → reasoning).
- **Leads to:** scaling laws ([1700](../20-machine-intelligence/)), the compute & data that train them ([1400](../40-compute-and-physical/)/[1600](../50-world-and-society/)), paths to AGI and whether scaling LLMs suffices ([1800](../60-frontier/)), and alignment/interpretability of the systems we now deploy at scale ([1900](../60-frontier/)).
- **Contested?** Next-token training, the transformer/attention, the three training stages, hallucination, in-context learning — **[Established]**. "Emergence" as a real phase change, reasoning-model framing — **[Likely → Contested]**. Whether LLMs *understand* / have world models — **[Contested, open]**.

## Proof-of-learning *(do one, from memory)*
1. Explain why "**just** predicting the next token" can yield reasoning and knowledge — using the compression idea of [0300](../00-foundations/0300_information-and-entropy.md).
2. In one sentence each: what does **attention** do, and what two advantages let the transformer beat RNNs?
3. Name the **three stages** that turn a base model into an assistant, and say which one inherits reward-hacking risk and why.
4. A model gives you a confident, well-formatted citation that turns out not to exist. Name the phenomenon, explain *why it's intrinsic* to a next-token predictor, and give two ways a director designs around it.
5. State the strongest version of *both* sides of "does an LLM understand?" — and why the question isn't settled.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-27)` — created. Capstone of the machine-intelligence core (1000–1300). *(Reasoning/test-time-compute and "frontier" specifics are 2026 snapshots — re-check; the understanding-debate is deliberately left open.)*

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md). This closes the machine-intelligence **core** (1000→1300). The ladder now turns to what powers it all — compute & chips ([1400](../40-compute-and-physical/)), data ([1600](../50-world-and-society/)), and scaling laws ([1700](../20-machine-intelligence/)) — then the frontier: paths to AGI ([1800](../60-frontier/)) and alignment ([1900](../60-frontier/)).*
