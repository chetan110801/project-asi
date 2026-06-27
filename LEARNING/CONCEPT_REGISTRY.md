# CONCEPT REGISTRY — one home per concept
**The no-redundancy enforcer.** Before explaining *anything*, check here. If a concept is listed, **link to its home — don't re-explain**. If it's not, explain it once in the right module, then add it here.

`Status: Living index · System Version: 2.2 · Last updated: 2026-06-27`

> Rule (from [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §5): every concept has exactly **one canonical module**, which lives in one **domain folder**. This table maps **concept → home module (`id` + folder) → one-line pointer**. It does *not* hold the explanation itself (that would be repetition) — it points to it. (Folders for planned modules: see [`00_MAP.md`](00_MAP.md).)

---

| Concept | Canonical home (`id` → file) | Status | One-line pointer |
|---|---|---|---|
| intelligence (working definition) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Doing the *right thing* across many situations to reach goals. |
| generality (general vs narrow) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Many problem types vs one; the core of "G" in AGI. |
| "AGI is many forms" (flight analogy) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Probably a family of forms, not one finish line. |
| system | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Parts + relationships that produce behavior. |
| emergence | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | The whole does what no part can (e.g. intelligence). |
| reductionism vs holism | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Zoom-in to fix parts; zoom-out to see behavior. |
| feedback loop | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Output looping back to change input. |
| negative / positive feedback | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Balancing → stability; reinforcing → runaway. |
| control (setpoint / error) | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Goal → measure → correct → repeat. |
| entropy / information / bit | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Surprise, measured; the unit is the bit. |
| compression (≈ understanding) | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Predict well → remove entropy → compress. |
| vector / embedding | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | A point in a space of meaning; nearness = similarity. |
| matrix (as transformation) | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | An action that moves a whole space at once. |
| dot product / similarity | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | Alignment of two vectors; the engine of retrieval/attention. |
| computation | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | What a machine can mechanically do. |
| universality / stored-program | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | One machine runs any program; a program is just data. |
| algorithm / complexity | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | A recipe; how its cost grows (cheap vs explosive). |
| uncomputability / hard limits | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | Some problems no machine can ever solve. |
| probability / uncertainty | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Reasoning with what we don't fully know. |
| conditional probability | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | P(A given B) — odds after evidence. |
| Bayes' rule / base rate | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Update belief = prior × likelihood; mind the base rate. |
| expected value | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Probability-weighted average; how to decide under risk. |
| distribution / fat tails | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | The full spread; rare extremes can dominate. |
| learning (in a system) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Improving from experience by an error-reducing loop. |
| generalization vs overfitting | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Transfer to unseen cases vs memorizing the training set. |
| supervised / unsupervised / RL / self-supervised | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Four flavors = same loop, different feedback. |
| inductive bias / no free lunch | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Can't learn without assumptions; none is best at everything. |
| objective function (Goodhart) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | The system gets what you measure, not what you meant. |
| neuron / synapse / plasticity | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Sum-and-fire units; learning = connections rewiring. |
| biological neural network | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Mind emerges from billions of wired neurons (inspired ANNs). |
| predictive brain | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Brain predicts input, learns from prediction error. |
| brain efficiency / embodiment | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | ~20 watts; evolved to run a body — where AI still lags. |
| developmental bootstrapping | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | General intelligence grown from little data + interaction. |
| core-knowledge priors | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Built-in expectations (physics, agents, number) = inductive bias. |
| sample efficiency | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learning a lot from little — the human-vs-AI gap. |
| curiosity / intrinsic motivation | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learning driven from inside, no external reward. |
| active / causal learning | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learn cause→effect by intervening, not just watching. |
| evolution (variation-selection-heredity) | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Design without a designer; the one recipe that made minds. |
| evolutionary optimization | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Gradient-free, population-based search (genetic algorithms). |
| inner/outer alignment (mesa-optimization) | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | An optimizer can produce an agent with divergent proxy goals. |
| cumulative culture | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Knowledge ratcheting across generations = the human superpower. |
| model / parameters (weights) | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | A function with tunable knobs; learning = setting the knobs. |
| training vs inference | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Tuning the knobs on data vs using the finished model. |
| features / feature engineering | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | The input numbers a model sees; hand-crafted then learned ([1100](20-machine-intelligence/1100_neural-networks-deep-learning.md)). |
| loss function | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | One number = how wrong; the objective ([0600](00-foundations/0600_what-it-means-to-learn.md)) made concrete. |
| gradient descent / learning rate | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Roll downhill on the error; the error-reducing loop on numbers. |
| train / validation / test split | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Tune knobs / tune choices / score once — honest held-out test. |
| bias–variance trade-off | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Underfit (too rigid) vs overfit (fits noise), operationalized. |
| hyperparameters | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Settings you choose (vs parameters the optimizer learns). |
| classical ML (trees/SVM/boosting) | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Non-deep methods; still win on tabular data. |
| data leakage | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Answer-clue sneaks into features → fake-great scores. |
| artificial neuron / activation function | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Weighted sum + a non-linear bend; the unit of a net. |
| layers / depth / deep learning | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Stacked matrix-multiply+activation; "deep" = many layers. |
| representation / feature learning | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | The net invents its own features (edges→objects). The revolution. |
| backpropagation | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Push error backward to assign each weight its blame. |
| CNN / RNN / LSTM | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Architectures = baked-in inductive bias (vision / sequence). |
| embedding / latent space | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Learned internal vectors = meaning (uses [0350](30-math-and-theory/0350_just-enough-linear-algebra.md)). |
| universal approximation | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Can represent ~anything — but representable ≠ learnable. |
| agent / environment / state / action / reward / policy | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | The RL vocabulary; the control loop with a learned controller. |
| value function / return | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Long-run reward (foresight), not the next treat. |
| exploration vs exploitation | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Try new vs cash in what works; the bandit dilemma. |
| temporal credit assignment | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Which past action earned a delayed reward? |
| reward shaping / reward hacking | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Agent games the proxy reward (Goodhart/mesa, made live). |
| model-free vs model-based / world model | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Trial-and-error vs learn a world model and plan in it. |
| deep RL / self-play | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | RL + nets (DQN, AlphaZero); play copies of yourself. |
| AI agents (LLM agents) | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Goal-directed act-loop; the 2025–26 LLM-agent frontier. |
| next-token prediction / LLM | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Predict the next chunk of text; the whole LLM trick. |
| token / tokenization | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Sub-word units the model reads/writes in. |
| transformer / attention | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Each token looks back at the relevant ones (dot-product similarity). |
| context window | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | The model's working memory; outside it is forgotten. |
| pretraining → fine-tuning → RLHF | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Three stages: raw predictor → instruction-follower → aligned assistant. |
| foundation / base model | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | The big pretrained predictor everything is built on. |
| in-context learning / prompting | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Learn a task from prompt examples, no weight change. |
| chain-of-thought / test-time compute | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | "Think step by step" / spend compute to reason = AI's slow mode. |
| hallucination (confabulation) | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-how-llms-work.md) | ✅ | Fluent, confident, false — intrinsic to a plausibility predictor. |

---

## How to use this table
- **Writing a new module?** For each idea you mention, find its row. Listed → write *"(see [home])"*. Missing → this idea needs a home; either it belongs in the module you're writing (add the row, pointing here) or it needs its own module (insert one — [`LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §8).
- **`id` is stable** even if the file is renumbered, so these pointers survive reordering.
- Rows are added the moment a concept gets its canonical explanation — never before (no empty promises), but planned homes may be pre-listed as ⬜ to reserve the slot.
