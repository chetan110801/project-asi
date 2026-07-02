# 20 · Machine intelligence
**How we actually build it.**

`Domain landing page · reading order lives in ../00_MAP.md`

**Scope:** machine learning · deep learning · neural networks · reinforcement learning · agents (the *concept*) · large language models (LLMs). *(The **applied** layer — building agentic systems, RAG, evaluation, AI product design — lives on its own shelf, [`../25-applied-ai-and-agentic-systems/`](../25-applied-ai-and-agentic-systems/); this shelf is the foundations those applications stand on.)*

**Key resources** (details in [`../../RESOURCES/INDEX.md`](../../RESOURCES/INDEX.md)): `r-cs229`, `r-d2l`, `r-nielsen-nndl`, `r-goodfellow-dl`, `r-karpathy-zth` (build-from-scratch), `r-sutton-barto` + `r-silver-rl` (RL), `r-cs224n` (LLMs/NLP), `r-mit-6034` (AI).

**Modules here:**
- ✅ [`1000_machine-learning-from-examples.md`](1000_machine-learning-from-examples.md) — model/parameters/loss/gradient-descent; train-val-test; bias–variance; classical ML still wins on tabular data
- ✅ [`1100_neural-networks-deep-learning.md`](1100_neural-networks-deep-learning.md) — artificial neuron, layers/depth, backprop, and the key idea: **the model learns its own features** (representation learning); CNN/RNN/transformer as inductive bias
- ✅ [`1200_reinforcement-learning-and-agents.md`](1200_reinforcement-learning-and-agents.md) — agent↔environment loop, value/return, explore-vs-exploit, reward hacking, deep RL & self-play, the LLM-**agent** frontier
- ✅ [`1300_language-models-the-next-token-idea.md`](1300_language-models-the-next-token-idea.md) — *(opens the LLM cluster 1300–1358; the first module grounded to the v2.5 standard)* what a language model is, self-supervision (the internet as teacher), the loss & perplexity, autoregressive generation, and predict ⇒ compress ⇒ (maybe) understand. *Its rev-1 whole-story coverage (transformer, training stages, hallucination, the understanding debate) is being split into cluster rungs 1305–1358 per [`../CURRICULUM.md`](../CURRICULUM.md) A3.4.*
- ⬜ later on this shelf: 1700 scaling laws *(slotted when reached)*

> These stand on `30-math-and-theory/` (linear algebra) and the foundations spine (learning, probability, feedback) — the map puts that groundwork *before* them, and each module links **back** instead of re-explaining.
