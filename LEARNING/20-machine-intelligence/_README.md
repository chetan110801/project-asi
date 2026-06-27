# 20 · Machine intelligence
**How we actually build it.**

`Domain landing page · reading order lives in ../00_MAP.md`

**Scope:** machine learning · deep learning · neural networks · reinforcement learning · agents · large language models (LLMs).

**Key resources** (details in [`../../RESOURCES/INDEX.md`](../../RESOURCES/INDEX.md)): `r-cs229`, `r-d2l`, `r-nielsen-nndl`, `r-goodfellow-dl`, `r-karpathy-zth` (build-from-scratch), `r-sutton-barto` + `r-silver-rl` (RL), `r-cs224n` (LLMs/NLP), `r-mit-6034` (AI).

**Modules here:**
- ✅ [`1000_machine-learning-from-examples.md`](1000_machine-learning-from-examples.md) — model/parameters/loss/gradient-descent; train-val-test; bias–variance; classical ML still wins on tabular data
- ✅ [`1100_neural-networks-deep-learning.md`](1100_neural-networks-deep-learning.md) — artificial neuron, layers/depth, backprop, and the key idea: **the model learns its own features** (representation learning); CNN/RNN/transformer as inductive bias
- ✅ [`1200_reinforcement-learning-and-agents.md`](1200_reinforcement-learning-and-agents.md) — agent↔environment loop, value/return, explore-vs-exploit, reward hacking, deep RL & self-play, the LLM-**agent** frontier
- ✅ [`1300_language-models-how-llms-work.md`](1300_language-models-how-llms-work.md) — *(capstone of the core)* next-token prediction, the transformer & attention, pretrain→fine-tune→RLHF, emergence, reasoning/test-time compute, and what LLMs **can't** do (hallucination)
- ⬜ later on this shelf: 1700 scaling laws *(slotted when reached)*

> These stand on `30-math-and-theory/` (linear algebra) and the foundations spine (learning, probability, feedback) — the map puts that groundwork *before* them, and each module links **back** instead of re-explaining.
