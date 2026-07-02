# THE CURRICULUM — the full module blueprint
**The complete, deeply-nested inventory of every study-material file this project intends to write** — the entire AI domain decomposed into its sub-domains and sub-sub-domains, plus every other field the corpus holds, each placed on the ladder at its depth tier. This is the *map of what to produce*; it is not the modules themselves.

`Part of: PROJECT ASI · System Version: 2.6 (new in v2.6) · Status: Living / revisable · Last updated: 2026-07-02`

---

## What this file is (and what it is not)

Think of the project's planning docs as four views of the same work, each answering a different question:

| Doc | The question it answers | Granularity |
|---|---|---|
| [`00_MAP.md`](00_MAP.md) — **the Trunk** | *In what order do I read?* | ~24 top-level rungs (the friendly "one book" spine) |
| **`CURRICULUM.md` — this file** | *What is the full set of files we will ever write?* | **every planned leaf module, decomposed to the bottom** |
| [`_QUEUE.md`](_QUEUE.md) — **the Queue** | *What do I write next?* | the few highest-leverage items, re-sorted constantly |
| [`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) — **the Atlas** | *Which corpus sources ground each module?* | per-domain grounding tables, built just-in-time |

So: **`00_MAP` is the table of contents, this Curriculum is the exhaustive outline, the Queue is the work order, and the Atlas is the evidence index.** The Trunk's ~24 rungs are the *cluster headers* of this file — each one expands here into its full set of leaf modules. The Queue always pulls its next item from this blueprint.

> **Why this exists (the learner's ask, 2026-07-02).** Before rewriting the thin from-memory modules and producing the rest, we need one place that lays out — robustly, dynamically, in full breadth and depth — *the kind of study material we must generate to span the entire AI domain (every sub-domain, sub-sub-domain, and below) and all the other fields we hold.* This file is that plan.

### This is a plan, not pre-built scaffolding (the reconciliation)

The project warns against two opposite failures, and this file threads between them:

- **Over-scaffolding** — creating hundreds of empty files or pre-populating every Atlas slice up front ([`../INSTRUCTIONS/PRODUCTION_FLOW.md`](../INSTRUCTIONS/PRODUCTION_FLOW.md) ②). We do **not** do that. No file listed here exists until it reaches the front of the Queue; Atlas slices are still built one domain at a time, on demand; per-domain sub-folders in `70-sciences/`/`80-engineering/` are still created only when their first module lands.
- **No map** — writing modules ad-hoc with no sense of the whole, so coverage is lumpy and the numbering paints us into corners.

**Enumerating a plan is cheap and reversible; building files is not.** This blueprint is a *living outline* — a few kilobytes of titles, one-line scopes, tiers, and grounding pointers. It costs almost nothing, it makes sequencing optimal, and it is revised freely (add/split/merge/re-tier rows as writing teaches us more). That is fully consistent with "scaffold the *system*, populate the *content* on demand": **the map is part of the system; the territory is filled in just-in-time.**

---

## How to read the tables

Every row is one planned module (one `.md` file). Columns:

- **Key** — the proposed 4-digit **sort-key** (global reading order; steps leave gaps for insertion — [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §3). Keys inside a cluster are *proposed*; the exact integer is finalized when the file is written (5-digit fine-insertion is always available, e.g. `1305` → `13055`).
- **Module** — working title.
- **Durable core (the AI-proof angle)** — the *one-line reason the module exists* in terms of enduring understanding: why the idea exists, what it optimizes, what it rules out, its trade-off or live debate. **Never** "learn to implement X." This is the [`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) §2.5 content test applied at planning time.
- **Tier** — depth budget ([`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) §1): **⬛ Core** (exhaustive) · **◧ Bridge** (working depth) · **▫ Literacy** (compact map + "how it feeds AGI").
- **Ground** — the main corpus folders that ground it (shorthand; the Atlas slice holds the full table). `pD#` = `papers/D#`; `tb/` = `textbooks/`; `co/` = `courses/`; `tr/` = `transcripts/`; `fr/` = `frontier-rnd/`; a bare name = a discipline shelf.

**Status legend** (shown per section, not per row): **✅** ready to standard · **♻️** file exists but was written from memory and needs the grounded rewrite · **⬜** planned (no file yet).

> The AI domain (Parts A3–A4) is rendered to the **deepest** granularity because it is the mission's core and the corpus is richest there. Bridge domains get working-depth clusters; Literacy branches get a compact ladder + a "how it feeds AGI" capstone. Depth of the *plan* mirrors depth of the *modules*.

---
---

# PART A — THE TRUNK (the AGI/ASI spine · Core + Bridge · reads as one book)

Sort-keys `0100`–`2999`. This is the single continuous narrative: *intelligence → its foundations → minds → machine intelligence → applied AI → what powers & bounds it → the frontier → society.*

## A0 · Foundations — the shared vocabulary of intelligence
Shelf [`00-foundations/`](00-foundations/) (+ math on [`30-math-and-theory/`](30-math-and-theory/)). Tier: ⬛ Core (foundational). Status: all exist ♻️ (from-memory; reground where thin — lower urgency, less contested).

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 0100 | What is intelligence? | Intelligence as *doing the right thing across situations to reach goals*; general vs narrow; why "AGI" is a family of forms, not a finish line. | ⬛ | tb/ (Legg, Bennett), tr/ |
| 0150 | Problem-solving as search (classical AI) | The first idea of AI: intelligence as search over states with heuristics; what symbolic/GOFAI got right and where it hit a wall. | ▫ | tb/AIMA, co/ |
| 0200 | What is a system? | Parts + relationships → emergence; reductionism vs holism — the lens for every complex thing after this. | ⬛ | tb/, complex-systems |
| 0250 | Feedback loops & control | Output looping to change input; negative→stability, positive→runaway; setpoint/error — the root of learning and of RL. | ⬛ | tb/, electrical-engineering (Åström) |
| 0300 | Information & entropy | Surprise measured in bits; **predict-well ⇒ compress ⇒ understand** — *the* reason next-token prediction works. | ⬛ | information-computation (MacKay, Shannon) |
| 0400 | Computation | What a machine can mechanically do; universality, stored-program, complexity, and the hard limits (uncomputability). | ⬛ | information-computation (Aaronson), tb/ |
| 0500 | Probability & uncertainty | Reasoning under what we don't know; conditional probability, Bayes, expected value, fat tails — the grammar of learning. | ⬛ | tb/Blitzstein, co/STAT110 |
| 0600 | What it means to learn | Improving from experience via an error-reducing loop; generalization vs overfitting; the four paradigms; inductive bias & no-free-lunch; Goodhart. | ⬛ | tb/, pD1 |

## A1 · Minds — intelligence's only working example (blueprint + benchmark)
Shelf [`10-minds/`](10-minds/). Tier: ⬛ Core. Status: 0700/0800/0900 exist ♻️; the rest ⬜. *The brain is the existence proof and the yardstick; we study it for what it teaches about building and bounding machine minds — not as neuroscience for its own sake.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 0700 | The brain: a working model | Neuron→network→mind; the brain as a prediction machine at ~20 watts — the efficiency & embodiment gap AI still faces. | ⬛ | neuroscience (Kandel), tb/ |
| 0710 | Neurons & neural computation | How a real neuron computes and learns (spikes, plasticity) — what artificial neurons kept and what they threw away. | ⬛ | neuroscience (Neuronal Dynamics), co/MIT-9.x |
| 0720 | Brain architecture & the cortex | Hierarchy, columns, maps, modularity — the structural ideas that inspired (and diverge from) deep nets. | ⬛ | neuroscience, co/ |
| 0730 | Prediction, perception & the predictive brain | Perception as controlled inference; predictive coding / free-energy as a candidate master-principle. ⚠️ corpus skews here — render as a strong hypothesis, not settled. | ⬛ | neuroscience (Friston/Rao), pD15 |
| 0740 | Memory & learning in the brain | Working vs long-term memory, consolidation, replay — why biological learning is sample-efficient where AI is not. | ⬛ | neuroscience, cognitive-science |
| 0760 | Cognition: reasoning, concepts, System 1 / System 2 | Fast intuition vs slow deliberation; concepts, analogy, compositional thought — the target capabilities for AGI. | ⬛ | cognitive-science (Lake), tb/, SEP |
| 0770 | Language & the mind | What language is for and how minds acquire it — the human benchmark LLMs are measured against. | ⬛ | cognitive-science, tb/SLP3, neuroscience |
| 0780 | Consciousness & the hard question | The honest map of theories; why it's unsolved and why it matters (or may not) for building/aligning AI. | ⬛ | cognitive-science, SEP, tr/ |
| 0800 | How a child's mind bootstraps | General intelligence grown from little data + interaction; core-knowledge priors, curiosity, active/causal learning — the sample-efficiency lesson. | ⬛ | cognitive-science, tb/ |
| 0860 | Cognitive architectures | ACT-R/SOAR and the "unified theory of cognition" dream — what a whole-mind design has to solve that a model doesn't. | ▫ | cognitive-science, tb/ |
| 0900 | Evolution & general intelligence | Variation-selection-heredity as design without a designer; evolutionary optimization; **inner/outer alignment (mesa-optimization)**; cumulative culture as the human superpower. | ⬛ | biology, tb/, pD4 |

## A2 · AGI-math — the Core mathematical spine (interspersed, pulled early where needed)
Shelf [`30-math-and-theory/`](30-math-and-theory/). Tier: ⬛ Core for the AGI-math slice (the rest of math is a Literacy Branch, Part B3). Low keys because these feed the machine-intelligence core. Status: 0350 exists ♻️; rest ⬜. *Rendered for insight and judgment — never as derivations to reproduce (the AI does the algebra).* 

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 0350 | Just-enough linear algebra | Vectors as points in meaning-space; matrices as transformations; **dot-product = similarity** — the engine of embeddings, retrieval, attention. | ⬛ | math-theory (Strang), co/3B1B |
| 0360 | Linear algebra, deeper | Eigenvectors/SVD as "the natural axes of a transformation"; why they underlie PCA, compression, and spectral methods. | ⬛ | math-theory (Strang, Boyd) |
| 0520 | Probability for machine learning | Distributions, likelihood, MLE, the Bayesian view — how models turn data into beliefs. | ⬛ | tb/Murphy, math-theory |
| 0530 | Statistics & inference | Estimation, hypothesis testing, confidence, causation vs correlation — reading evidence without fooling yourself. | ⬛ | math-theory (Think-Stats), co/ |
| 0540 | Information theory (the math) | Entropy, KL-divergence, mutual information, the source-coding bound — the deeper form of 0300 that scores every model. | ⬛ | information-computation (MacKay) |
| 0550 | Optimization | Convexity, gradients, the Lagrangian, constrained optimization — *the* verb of machine learning (everything is minimizing a loss). | ⬛ | math-theory (Boyd), pD1 |
| 0560 | Learning theory | PAC learning, VC dimension, generalization bounds, the bias-variance decomposition — *why* learning from finite data can work at all, and its limits. | ⬛ | co/CS229M, tb/, math-theory |
| 0570 | Calculus & analysis for ML | Chain rule = backprop; gradients, Jacobians; just enough real analysis to trust the machinery. | ⬛ | math-theory, co/3B1B |

## A3 · Machine intelligence — THE AI DOMAIN, decomposed to the bottom
Shelf [`20-machine-intelligence/`](20-machine-intelligence/). Tier: ⬛ Core (exhaustive). *This is the deepest part of the whole curriculum — the AI domain broken into its four sub-domains (classical ML, deep learning, reinforcement learning, language/sequence models), each into its sub-sub-domains, each into leaf modules.* Status: **1300 ✅ (grounded rev 2, session 22 — the proof-of-standard)**; 1000/1100/1200/1310 exist ♻️ (rewrite); rest ⬜.

### A3.1 — Machine-learning foundations (the pre-deep-learning bedrock) · keys 1000–1099
*Why this survives the deep-learning era: these are the concepts that decide when NOT to reach for a neural net, how to evaluate anything, and what "learning from data" even means.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1000 | Machine learning from examples | Model = function with tunable knobs; loss, gradient descent, train/val/test, bias-variance — the loop under everything. | ⬛ | tb/Bishop-PRML, ISLR, co/CS229 |
| 1010 | Linear & logistic regression | The workhorses; why a strong linear baseline is the honest first move and often hard to beat. | ⬛ | ISLR, co/CS229, tb/ |
| 1015 | Regularization & sparsity | L1/L2 as encoding a preference for simpler models; the bias you *add on purpose* to generalize. | ⬛ | ISLR, ESL |
| 1020 | Decision trees | Learning by asking questions; interpretability vs instability — the unit that ensembles are built from. | ⬛ | ISLR, tb/ |
| 1025 | Ensembles: bagging, boosting, forests | Many weak models → one strong one; **why gradient-boosted trees still win on tabular data** over deep nets. | ⬛ | ISLR, ESL, tb/Huyen |
| 1030 | SVMs & the kernel trick | Max-margin as a principled objective; kernels as "compute in a huge space without visiting it" — a lasting idea. | ⬛ | ESL, co/CS229 |
| 1035 | k-NN & the curse of dimensionality | The simplest learner; why distance stops meaning anything in high dimensions — a constraint that shapes all ML. | ▫ | ISLR, tb/ |
| 1040 | Probabilistic classifiers (naïve Bayes) | Modelling P(data｜class); the "naïve" independence assumption and why a wrong model can still work. | ▫ | tb/Murphy, SLP3 |
| 1045 | Clustering & unsupervised structure | Finding groups with no labels (k-means, hierarchical, density); what "structure without supervision" buys. | ⬛ | ISLR, tb/ |
| 1050 | Dimensionality reduction | PCA and manifold learning; the idea that high-dim data lives on a low-dim surface — the seed of representation learning. | ⬛ | ISLR, tb/Murphy |
| 1055 | Probabilistic graphical models | Bayes nets & HMMs: reasoning with structured uncertainty; the pre-deep way to encode knowledge into a model. | ◧ | tb/Bishop-PRML, co/CMU-10-708 |
| 1060 | Latent variables & the EM algorithm | Learning the hidden causes behind data; mixture models — the logic reused in VAEs and clustering. | ◧ | tb/Bishop-PRML |
| 1065 | Gaussian processes & Bayesian non-parametrics | Models that say "I don't know" honestly (calibrated uncertainty); the trade-off vs deep nets. | ◧ | ai-ml-foundations/distill-gaussian-processes, tb/Murphy |
| 1070 | Optimization in practice (SGD → Adam) | Stochastic gradient descent, momentum, adaptive methods — why we can train billion-parameter models at all. | ⬛ | pD1/1412.6980_adam, survey-optimization-ml-bottou |
| 1075 | Evaluation & validation | Metrics, cross-validation, calibration, data leakage — the skill that separates real results from self-deception. | ⬛ | tb/Huyen, ISLR |
| 1080 | Generalization: bias, variance, overfitting | The central tension made concrete; regularization, capacity, and why more data usually beats a cleverer model. | ⬛ | ESL, co/CS229M |
| 1085 | The map of learning paradigms | Supervised / unsupervised / self-supervised / semi / active / transfer — same loop, different feedback signal. | ⬛ | pD13 (survey-transfer, -contrastive), tb/ |
| 1090 | Classical vs deep: when each wins | The honest decision rule — tabular & small-data vs perceptual & large-data; the AI-proof judgment, not a default. | ⬛ | tb/Huyen, tr/ |

### A3.2 — Deep learning (learning the representations themselves) · keys 1100–1199
*The pivot: instead of hand-designing features, let the model learn them. Every architecture below is a different **inductive bias** — a built-in assumption about the data's structure.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1100 | Neural networks & deep learning | Stacked simple units learn layered representations; depth = composition; the shift from feature-engineering to feature-learning. | ⬛ | tb/Goodfellow, Prince-UDL, co/ |
| 1110 | Backpropagation | Credit assignment as the chain rule run backward; *the* algorithm that makes deep learning trainable. | ⬛ | tb/Nielsen, Goodfellow |
| 1115 | Nonlinearity & activations | Why a stack of linear layers is still linear; what ReLU & friends buy and their failure modes. | ⬛ | tb/Goodfellow, d2l |
| 1120 | Training deep nets: the optimization reality | Vanishing/exploding gradients, learning-rate schedules, why deep nets were "untrainable" until they weren't. | ⬛ | tb/Goodfellow, co/CS231n |
| 1125 | Normalization (batch/layer) | Why normalizing activations stabilizes and speeds training — a trick that became load-bearing infrastructure. | ⬛ | pD1/1502.03167_batchnorm |
| 1130 | Regularization in deep nets | Dropout, weight decay, augmentation, early stopping — fighting overfitting when the model can memorize anything. | ⬛ | tb/Goodfellow |
| 1135 | Initialization & training dynamics | Why where you start matters; the loss landscape picture — intuition for why huge non-convex models train. | ◧ | tb/Prince-UDL, pD1 |
| 1140 | Representation learning & embeddings | The core payoff: learned vector spaces where geometry = meaning (word2vec and beyond). | ⬛ | pD1/1301.3781_word2vec, ai-ml-foundations |
| 1145 | Convolutional networks & vision | Convolution as the "translation-invariance" inductive bias; LeNet→AlexNet→ResNet as a lesson in depth + residuals. | ⬛ | pD1 (vgg,resnet,googlenet,unet,alexnet), co/CS231n |
| 1150 | Recurrent networks (RNN/LSTM/GRU) | Modelling sequences with memory; the vanishing-gradient wall that motivated gating — and later, attention. | ⬛ | pD1/1409.3215_seq2seq, ai-ml-foundations/distill-augmented-rnns |
| 1160 | Autoencoders & self-supervised pretraining | Learning by reconstruction; "the labels are in the data" — the idea that scales to LLMs. | ⬛ | tb/, pD13/survey-contrastive-self-supervised |
| 1165 | VAEs (variational autoencoders) | Generative modelling with a probabilistic latent space; the trade-off of blurry-but-principled generation. | ◧ | pD1/1312.6114_vae |
| 1170 | GANs (adversarial generation) | Generation as a two-player game; why they're powerful and unstable (mode collapse) — a durable idea beyond the specific model. | ◧ | pD1/1406.2661_gan |
| 1175 | Diffusion & score-based models | Generation as iterative denoising; **why it overtook GANs** for images/video; the modern generative workhorse. | ⬛ | pD7 (ddpm, score-sde, latent-diffusion), ai-ml-foundations/lilianweng-diffusion |
| 1180 | Graph neural networks | Learning on relational structure (the "irregular data" inductive bias); message-passing as the core idea. | ◧ | pD13/survey-graph-neural-networks, ai-ml-foundations/distill-gnn-intro |
| 1185 | Why does deep learning generalize? | Double descent, over-parameterization, the lottery ticket — the honest "we don't fully know" at the theory frontier. | ⬛ | co/, pD1, tr/ |
| 1190 | Scale & the bitter lesson | General methods + compute beat hand-crafted knowledge; the observation that reframed the whole field (→ 1700). | ⬛ | ai-ml-foundations/ml-blogs (Bitter-Lesson), tr/ |

### A3.3 — Reinforcement learning & agents (learning from consequences) · keys 1200–1299
*The other great paradigm: no labels, only rewards from acting. This is where "agency," goals, and the alignment failure modes first become concrete.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1200 | Reinforcement learning & agents | The agent-environment loop; explore vs exploit; reward as the signal — and reward-hacking as the first live alignment problem. | ⬛ | tb/Sutton-Barto, co/CS234, DeepMind-RL |
| 1205 | MDPs, return & discounting | The formal frame: states, actions, reward, the value of the future — the vocabulary all of RL is written in. | ⬛ | tb/Sutton-Barto |
| 1210 | Value functions & Bellman | "The value of now = reward + value of next"; dynamic programming as the recursive heart of RL. | ⬛ | tb/Sutton-Barto |
| 1215 | Model-free value methods | TD-learning, Q-learning, SARSA — learning to act well without a model of the world. | ⬛ | tb/Sutton-Barto |
| 1220 | Deep Q-networks | Neural nets as value approximators; the Atari moment that started deep RL — and its instability. | ⬛ | pD5/1312.5602_dqn-atari |
| 1225 | Policy-gradient methods | Optimizing the policy directly; REINFORCE — the family that scales to continuous, high-dim action. | ⬛ | pD5, ai-ml-foundations/lilianweng-policy-gradient |
| 1230 | Actor-critic & the stable workhorses (A3C, TRPO, PPO) | Combining value + policy; **why PPO became the default** (incl. for RLHF) — stability as the real objective. | ⬛ | pD5 (a3c, trpo, ppo) |
| 1235 | Continuous control (DDPG, SAC) | Acting in real-valued action spaces (robots); exploration via entropy — the bridge to robotics. | ◧ | pD5 (ddpg, soft-actor-critic) |
| 1240 | Model-based RL & world models | Learn a model of the world, then plan/dream inside it; sample-efficiency and the Dreamer line. | ⬛ | pD5/2301.04104_dreamerv3, pD11/1803.10122_world-models |
| 1245 | Exploration & intrinsic motivation | The hard-exploration problem; curiosity as a reward — links back to the child mind (0800). | ◧ | pD5, tr/ |
| 1250 | Reward design & reward hacking | Specification is the hard part; Goodhart at full strength — the seed of the alignment problem (→ 1910). | ⬛ | pD4, governance-safety |
| 1255 | Self-play & the AlphaGo lineage | Superhuman skill from playing yourself; AlphaGo→Zero→MuZero — search + learning + self-generated data. | ⬛ | pD5 (alphago, alphazero) |
| 1260 | Deep-RL grand challenges | Dota-Five, StarCraft, Rubik's-cube hand — what massive-scale RL achieved, and how brittle it stayed. | ◧ | pD5/1912.06680_openai-five, pD11/1910.07113 |
| 1265 | Offline RL | Learning from logged data without acting; distribution shift as the core difficulty — the practical RL. | ◧ | pD13/survey-offline-rl |
| 1270 | Multi-agent RL | Many learners at once: cooperation, competition, emergent conventions — and why it's hard to reason about. | ◧ | pD13/survey-multiagent-rl |
| 1275 | RL as sequence modelling | Decision Transformer: recast control as prediction — a unifying idea linking RL and LLMs. | ◧ | pD9/2106.01345_decision-transformer |
| 1280 | RL from human/AI feedback (the LLM connection) | How the RL loop became the alignment tool for language models (→ 1335); reward *models* instead of reward functions. | ⬛ | pD4 (deep-rl-from-hf, instructgpt) |

### A3.4 — Language & sequence models: NLP → the transformer → LLMs · keys 1300–1359
*The current frontier and the substrate the learner will most direct. The richest corpus we hold — rendered to the finest granularity.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1300 ✅ | [Language models: the next-token idea](20-machine-intelligence/1300_language-models-the-next-token-idea.md) *(grounded rev 2, session 22)* | An LM assigns probability over the next token; **predict-to-compress-to-understand**; self-supervision makes the whole internet a teacher. | ⬛ | tb/SLP3, pD2/gpt3, mackay-itila, tr/legg+karpathy |
| 1305 | Tokenization | Sub-word pieces (BPE) as the model's alphabet; why models miscount letters and stumble on rare words — a real design constraint. | ⬛ | tb/SLP3, co/CS336, hf-llm-course |
| 1308 | Classical & n-gram language models | The distributional hypothesis; what counting-based LMs got right and the sparsity wall neural LMs broke. | ▫ | tb/SLP3, pD13/survey-deep-learning-nlp |
| 1310 | Attention & the transformer | Attention as content-based soft retrieval (dot-product similarity); parallelism + long-range links — why it beat RNNs. | ⬛ | pD2/1706.03762_attention, tb/SLP3, co/CS25 |
| 1312 | Positional encoding | Attention is order-blind by default; how position is injected (RoPE/ALiBi) and why it caps/extends context. | ◧ | pD6 (rope-roformer, alibi) |
| 1315 | Embeddings & the geometry of meaning | Static→contextual embeddings; the vector space where analogy and similarity live — the model's semantic memory. | ⬛ | pD1/word2vec, pD2/elmo, tb/SLP3 |
| 1318 | Pretraining objectives: autoregressive vs masked vs seq2seq | GPT vs BERT vs T5 — three bets on *what to predict*; why decoder-only autoregression won for generation. | ⬛ | pD2 (bert, t5, gpt3) |
| 1320 | Pretraining at scale | The data pipeline, the objective, the compute bill; what "training a base/foundation model" actually means. | ⬛ | pD3/foundation-models, tb/Huyen |
| 1322 | Scaling laws & emergence (the LLM view) | Loss falls predictably with size/data/compute; abilities that *seem* to appear suddenly — with the "mirage" caveat (→ deep dive 1700/1710). | ⬛ | pD3 (kaplan, chinchilla, emergent-abilities, mirage) |
| 1325 | In-context learning & few-shot | Learning a task from examples in the prompt, no weight change — learning at inference; still not fully understood. | ⬛ | pD2/gpt3, pD13/survey-in-context-learning |
| 1328 | Prompting & context engineering | Programming the model with words; the durable principles (specify, decompose, ground) vs transient "prompt tricks." | ⬛ | pD13/survey-prompting-methods-nlp, fr/ |
| 1330 | Fine-tuning & instruction tuning | Adapting a base model to follow instructions (SFT/FLAN); cheap vs pretraining; when adaptation beats prompting. | ⬛ | pD3/flan, pD4/instructgpt |
| 1332 | Parameter-efficient fine-tuning | LoRA/QLoRA: adapt a giant model by moving few weights; the cost/quality trade-off that democratized tuning. | ◧ | pD6 (lora, qlora), survey-peft |
| 1335 | Preference learning & alignment tuning | RLHF, DPO, Constitutional AI/RLAIF — turning a raw predictor into a helpful, honest, harmless assistant; sycophancy risk. | ⬛ | pD4 (instructgpt, dpo, constitutional-ai), survey-rlhf |
| 1338 | Reasoning: chain-of-thought & test-time compute | Buying accuracy with thinking-time (CoT, self-consistency, o1/R1); the arrival of a "System 2" for models. | ⬛ | pD3 (chain-of-thought, self-consistency, deepseek-r1, tree-of-thoughts) |
| 1342 | Hallucination & calibration | A next-token predictor optimizes plausibility, not truth; **why confabulation is intrinsic**, not a patchable bug. | ⬛ | pD13 (survey-hallucination-llms, -nlg) |
| 1345 | Evaluating LLMs | Benchmarks, contamination, the "capability is jagged" problem, LLM-as-judge and its biases — how to not be fooled. | ⬛ | pD13/survey-evaluation-of-llms |
| 1348 | Multimodal models | Fusing vision/audio/language in one model (CLIP→Flamingo→LLaVA); a shared representation across senses. | ◧ | pD8 (clip, flamingo, llava, whisper) |
| 1350 | Mixture-of-experts & conditional computation | Route each token to a few sub-networks; **decouple parameter count from compute** — how frontier models scale cheaply. | ◧ | pD6 (moe-sparsely-gated, switch, mixtral), survey-moe |
| 1352 | Post-transformer architectures | State-space models (Mamba), RWKV, RetNet — the bet that attention's quadratic cost is beatable; is the transformer forever? | ◧ | pD10 (mamba, s4, rwkv, retnet), survey-state-space-models |
| 1355 | Context, memory & the "what an LLM is not" | Frozen weights, the finite context window, no post-training learning; the honest boundary of the object. | ⬛ | tb/SLP3, tr/, survey-of-llms |
| 1358 | Do LLMs understand? (the open debate) | Stochastic-parrot vs emergent-world-models; what interpretation of "understanding" is even at stake — genuinely unsettled. | ⬛ | tr/ (debates), pD14, sparks-of-agi |

## A4 · Applied AI & agentic systems — turning models into systems that work
Shelf [`25-applied-ai-and-agentic-systems/`](25-applied-ai-and-agentic-systems/). Tier: ⬛ Core (principles, **not** framework syntax — [`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) §2.5). Keys 1360–1399. Status: all ⬜. *The founder-director's core craft: the model is one component inside a reliable system.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1360 | From model to system | Why a great model ≠ a great product; the systems view — data, control flow, feedback, humans — around the model. | ⬛ | fr/ (anthropic-eng, chip-huyen), tb/Huyen-AIE |
| 1362 | Retrieval & grounding (RAG) | The durable answer to "the model doesn't know your world / hallucinates": retrieve real context, then generate. [RAG's home] | ⬛ | pD9 (rag, dense-passage-retrieval, retro, self-rag), survey-rag |
| 1365 | Agentic systems: the loop | Plan→act→observe→repeat; tools, memory, autonomy; **why long-horizon reliability degrades (errors compound)** and the patterns that fight it. | ⬛ | pD9 (react, toolformer, reflexion, voyager, generative-agents), fr/ |
| 1368 | Orchestration & multi-agent design | When to add agents vs a single call; roles, hand-offs, and the failure modes of agent swarms. | ⬛ | fr/ (langchain/langgraph/crewai/autogen docs — principles), survey-llm-agents |
| 1370 | Tool use & the model-context protocol | Giving models hands (APIs, code, search); the durable interface idea behind MCP — not the spec details. | ◧ | fr/ (mcp-docs, openai-agents-guide) |
| 1372 | Evaluating AI systems | Evals, LLM-as-judge, failure analysis, regression tests — **the skill that separates real builders from demo-makers.** | ⬛ | fr/ (anthropic-eng, methodology), pD13/survey-evaluation |
| 1375 | Reliability, guardrails & human-in-the-loop | Designing for a component that is wrong sometimes: fallbacks, verification, where a human must stay. | ⬛ | fr/ (openai practical-guide, twelve-factor-agents) |
| 1378 | AI product & system design patterns | The latency/cost/quality triangle; caching, routing, cascades; UX for probabilistic systems. | ⬛ | fr/, tb/ (designing-llm-apps, huyen-aie) |
| 1380 | The director's lever choice: prompt vs RAG vs fine-tune vs pretrain | Reach for the cheapest lever that solves it; the decision framework, not a default. | ⬛ | fr/, tb/Huyen-AIE |
| 1385 | AI-for-X archetypes | The reusable *shapes* of applying AI to a field (assistant, copilot, autonomous agent, discovery engine) — links the science/eng branches. | ⬛ | pD12 (codex, alphacode, med-palm, chemcrow, swe-agent), fr/ |
| 1390 | Spec-driven agentic engineering (the anti-"vibe-coding" discipline) | Treating agent-built software as an engineering discipline (specs, tests, review) rather than lucky prompting. | ⬛ | fr/ (spec-kit, twelve-factor-agents, latent-space) |

## A5 · Compute & infrastructure — what powers the models
Shelf [`40-compute-and-infrastructure/`](40-compute-and-infrastructure/). Tier: mostly ◧ Bridge; scaling laws ⬛ Core. Keys 1400–1799. Status: all ⬜.

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1400 | Compute & chips | GPUs/TPUs and why AI runs on them; the fabrication chokepoints (TSMC/ASML) that make compute geopolitical. | ◧ | hardware-compute (Sze), tr/chip-war, fr/ (NVIDIA) |
| 1410 | How AI accelerators work | Parallelism, memory bandwidth, the roofline — why *memory*, not FLOPs, is often the real limit. | ◧ | hardware-compute (Sze), co/MIT-6.5940 |
| 1420 | Distributed training | Data/model/pipeline parallelism, ZeRO, Megatron — how a model too big for any chip gets trained. | ◧ | pD6 (megatron, zero) |
| 1430 | Inference & serving | KV-cache, FlashAttention, speculative decoding, paged-attention (vLLM) — why serving cost, not training, dominates. | ◧ | pD6 (flashattention, speculative-decoding, vllm) |
| 1440 | Model compression | Quantization, distillation, pruning — running frontier capability on modest hardware; the quality trade-off. | ◧ | pD6 (gptq), pD13/survey-knowledge-distillation, survey-efficient-llms |
| 1450 | The AI systems stack | Compilers, kernels, frameworks — the layers a director should understand to reason about cost/speed (not to write). | ▫ | computer-systems, co/MIT-6.5940 |
| 1500 | Energy & the physical cost of thinking | The wattage of intelligence; data-center power/cooling as a real constraint on scaling. | ◧ | energy (MacKay), tr/ |
| 1600 | Data: the fuel | Where training data comes from, curation, data-centric AI — why data quality beats model cleverness. | ◧ | tb/Huyen, economics-data |
| 1620 | The data wall | Are we running out of high-quality text? Synthetic data and its risks (model collapse). | ◧ | economics-data (Villalobos), tr/ |
| 1630 | The data economy & rights | Who owns training data; the legal/economic fight that will shape what can be built. | ▫ | economics-data, governance-safety |
| 1700 | Scaling laws & their limits | The compute-optimal frontier (Kaplan→Chinchilla); how to spend a fixed budget on size vs data — the field's master curve. | ⬛ | pD3 (kaplan, chinchilla), hardware-compute/compute-trends |
| 1710 | Emergence & the mirage debate | Do new abilities truly "switch on," or is it a measurement artifact of sharp metrics? Both sides, honestly. | ⬛ | pD3 (emergent-abilities, emergent-abilities-mirage) |
| 1720 | The limits of scaling | Data, compute, energy, and money walls; what scaling reliably buys and what it plausibly cannot (→ 1800). | ⬛ | pD3, tr/ (debates) |

## A6 · Frontier & alignment — paths to AGI and the control problem
Shelf [`50-frontier-and-alignment/`](50-frontier-and-alignment/). Tier: ⬛ Core. Keys 1800–1999. Status: all ⬜. *Where 0900 mesa-alignment, 1250 reward-hacking, and 1335 RLHF all pay off.*

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 1800 | Paths to AGI, compared | The live approaches — scale-is-enough, neuro-inspired, world-models, hybrid neuro-symbolic, agentic/RL — and their bets. | ⬛ | pD16/survey-llms-for-agi, togelius-agi, tr/ (debates) |
| 1810 | What would count as AGI? | Competing definitions & benchmarks; why the goalposts move; the "sparks" claim and the pushback. | ⬛ | pD3/sparks-of-agi, tr/, SEP |
| 1820 | Recursive self-improvement & takeoff | The intelligence-explosion argument; fast vs slow takeoff; what would have to be true for each. | ⬛ | tr/ (Dwarkesh, debates), governance-safety |
| 1830 | World models & agency: the missing pieces | The case that prediction ≠ agency/grounding; what current systems still lack for general intelligence. | ⬛ | pD11/world-models, tr/ (LeCun), pD15 |
| 1840 | Superintelligence: scenarios | Honest, clearly-tagged speculation about ASI and its stakes — the far end of the mission. | ⬛ | tr/, governance-safety |
| 1900 | The alignment problem | Why *capable* ≠ *safe*; the core argument that objectives are hard to specify and optimizers exploit them. | ⬛ | pD14/survey-ai-alignment, christian-alignment, fr/anthropic |
| 1910 | Specification gaming & outer alignment | Reward hacking at scale (1250 grown up); Goodhart as an alignment-breaking force. | ⬛ | pD4, governance-safety/concrete-problems |
| 1920 | Mesa-optimization & inner alignment | A trained model can become an optimizer with its own proxy goal (0900 realized); the deception risk. | ⬛ | pD4, governance-safety, tr/AXRP |
| 1930 | RLHF and its limits as alignment | Sycophancy, reward-model hacking, the gap between "sounds aligned" and "is aligned." | ⬛ | pD4 (instructgpt, constitutional-ai), survey-rlhf |
| 1940 | Scalable oversight | Debate, amplification, weak-to-strong generalization — supervising systems smarter than us. | ⬛ | pD4 (debate, weak-to-strong, lets-verify) |
| 1950 | Interpretability & mechanistic interp | Opening the black box: features, circuits, superposition — can we read a model's cognition? | ⬛ | pD14 (mech-interp), governance-safety/transformer-circuits, ai-ml-foundations |
| 1960 | Deceptive alignment & sleeper agents | The scariest failure: a model that behaves until it doesn't; why standard training may not remove it. | ⬛ | pD4, governance-safety (sleeper-agents) |
| 1970 | Dangerous-capability evaluations | Red-teaming, capability elicitation, responsible scaling policies — measuring risk before deploying. | ◧ | governance-safety (RSP, preparedness, NIST), fr/ |
| 1980 | AI safety: the open-problems map | The consolidated landscape (concrete + unsolved problems) — where the field actually is. | ⬛ | pD4/unsolved-problems, governance-safety |

## A7 · World & society — the civilization view
Shelf [`60-world-and-society/`](60-world-and-society/). Tier: ◧ Bridge (complex-systems slice ◧). Keys 2000–2200. Status: all ⬜.

| Key | Module | Durable core | Tier | Ground |
|---|---|---|---|---|
| 2000 | The economics of AI | Automation, productivity, the labor question, comparative advantage — how AI reshapes who does what. | ◧ | economics-data (Acemoglu), AI-Index, tr/ |
| 2010 | Governance & policy | The frameworks (NIST AI RMF, EU AI Act, RSPs, Bletchley); what regulating a general technology can and can't do. | ◧ | governance-safety (NIST, Int'l-AI-Safety-Report) |
| 2020 | Geopolitics & the compute race | Chips, export controls, national AI strategy — why compute is the new strategic resource. | ◧ | tr/chip-war, governance-safety, fr/ |
| 2030 | Complex systems & society | Networks, cascades, tipping points, systemic risk — the lens for AI's second-order effects. | ◧ | complex-systems (Newman), tb/ |
| 2040 | AI & epistemics | Misinformation, synthetic media, trust and the shared-reality problem in an AI-saturated information ecosystem. | ◧ | governance-safety, tr/ |
| 2050 | Catastrophic & existential risk | The honest landscape of large-scale risks (misuse, accident, structural) — clearly tagged by evidence and dispute. | ◧ | governance-safety, tr/ (debates) |

---
---

# PART B — THE BRANCHES (the broad-knowledge library · Literacy/Bridge)

Each domain is a **local ladder** (not forced into the Trunk's reading order) ending in a **"how this field feeds AGI/ASI" capstone** that links back into the Trunk. Sort-keys `7000`–`8999` keep each shelf grouped. Tier is per-domain (mostly ▫ Literacy; robotics/quantum/computer-systems are ◧ Bridge). *Literacy = the enduring core of the field + its connection to the mission, not textbook reproduction.* Status: all ⬜. Per-domain sub-folders created when the first module lands.

## B1 · Sciences — [`70-sciences/`](70-sciences/)

**Physics** ▫ (keys 7000s) — grounds: physics (Tong, OpenStax, Feynman), co/ (Yale, MIT-8.0x)
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 7000 | Physics for a director — the map | The hierarchy of physical law and why "it's all physics underneath" matters for what's buildable. | physics |
| 7010 | Mechanics & the idea of a law | Conservation, symmetry, least-action — the template for "a law that predicts." | physics (Tong), co/Yale |
| 7020 | Thermodynamics & statistical mechanics | Entropy, the arrow of time, temperature-as-statistics — the deep bridge to information (0300/0540). | physics, information-computation |
| 7030 | Electromagnetism | Fields and Maxwell's unification; the physical substrate that computing rides on. | physics (Tong), electrical-engineering |
| 7040 | Quantum mechanics — the honest map | Superposition, measurement, entanglement; what's real vs pop-science — feeds compute (8700) & materials. | physics (Tong), quantum |
| 7050 | Relativity & cosmology — the map | Spacetime and the universe at large; the worldview, lightly. | physics, astronomy |
| 7060 | How physics pushes AGI | Simulation, ML-for-physics, physics-informed learning, fusion control — where AI accelerates physics. | pD12 (fusion), pD15, physics |

**Chemistry** ▫ (7100s) — grounds: chemistry (OpenStax, DeVoe, Jakubowski)
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 7100 | Chemistry — the map | Matter, bonds, reactions; why chemistry is a search over an astronomically large molecule space. | chemistry |
| 7110 | Bonding, reactions & energy | What drives reactions (thermodynamics + kinetics); the durable "why." | chemistry (DeVoe) |
| 7130 | Organic & biochemistry | The carbon molecules of life and industry — the target space for AI-designed molecules. | chemistry (Jakubowski) |
| 7140 | How AI transforms chemistry | Retrosynthesis, reaction/property prediction, autonomous labs (ChemCrow) — search made tractable. | pD12/chemcrow, materials |

**Biology** ▫ (7200s) — grounds: biology (OpenStax, Kellis), pD12/pD15
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 7200 | Biology — the map | Life as information + chemistry + evolution; why biology is the ultimate existence proof of self-organizing intelligence. | biology |
| 7210 | The cell & molecular biology | DNA→RNA→protein; the machinery — the "code" AI now reads and writes. | biology, chemistry |
| 7220 | Genetics & the genome | Heredity, variation, the genome as data; the substrate for computational biology. | biology (Nickle) |
| 7230 | Evolution & ecology | Selection, fitness landscapes, ecosystems — the algorithm of life (deepens 0900). | biology, complex-systems |
| 7250 | How AI transforms biology | AlphaFold, protein language models (ESM), genomic models (Evo), protein design (RFdiffusion) — biology's AI revolution. | pD12 (alphafold), pD15, biology |

**Materials** ▫ (7300s) · **Astronomy** ▫ (7400s) · **Earth & climate** ▫ (7500s)
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 7300 | Materials — structure→property→AI | How atomic structure sets properties; why materials discovery is a search problem AI now drives (GNoME, MatterGen). | materials (DoITPoMS), pD12 (gnome) |
| 7400 | Astronomy — the map + AI | The cosmos at scale; how AI mines surveys and finds exoplanets/transients (the data-deluge science). | astronomy, pD12 |
| 7500 | Earth, climate & AI weather | The climate system; ML weather/climate models (GraphCast, GenCast, NeuralGCM) beating classical NWP. | earth-climate, pD12 (graphcast, gencast) |

## B2 · Engineering — [`80-engineering/`](80-engineering/)

**Classical engineering** ▫ (compact map + AI link each): grounds = the matching discipline shelves.
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 8000 | Electrical engineering — the map | Circuits, signals, semiconductors; **the physical basis of all computing** — where AI meets silicon (→ 1400). | electrical-engineering |
| 8020 | Semiconductors & VLSI | How transistors become chips; Moore's law and its end — the constraint under the compute story. | electrical-engineering, hardware-compute |
| 8100 | Mechanical engineering — the map | Statics, dynamics, thermo, fluids; the physics of machines that move — feeds robotics (8600). | mechanical-engineering |
| 8200 | Civil engineering — the map | Structures & infrastructure; the physical build-out (data centers, grids) that AI scaling now demands. | civil-engineering |
| 8300 | Chemical engineering — the map | Process, reactions at scale, separations; where AI does process control & optimization. | chemical-engineering |
| 8400 | Aerospace engineering — the map | Flight & orbital mechanics; autonomy and control as the AI frontier here. | aerospace-engineering |
| 8500 | Biomedical engineering — the map | Instruments & the body-machine interface; AI in diagnosis, imaging, and BCIs (→ Neuralink). | biomedical-engineering, fr/neuralink |

**Robotics & embodiment** ◧ (8600s) — grounds: robotics (Lynch&Park, LaValle, Tedrake), pD11, pD16
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 8600 | The embodiment problem | Why the physical world is harder than the digital (Moravec's paradox); the sim-to-real gap. | robotics, pD11 |
| 8610 | Kinematics, dynamics & control | Making a body move on purpose; the classical control that learning augments, not replaces. | robotics (Lynch&Park, Åström) |
| 8620 | Perception & state estimation (SLAM) | Knowing where you are & what's around you; the durable estimation ideas under autonomy. | pD16/slam, robotics |
| 8630 | Motion planning | Finding a path through a world of constraints; search in configuration space (links 0150). | robotics (LaValle) |
| 8640 | Robot learning & foundation models | Learning control end-to-end; vision-language-action models (RT-2, OpenVLA, π0, diffusion policy) — the LLM playbook for bodies. | pD11 (rt2, openvla, pi0, diffusion-policy), pD16 |

**Quantum computing** ◧ (8700s) — grounds: quantum (Preskill, Watrous, Nielsen), pD16
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 8700 | Quantum computing — the model | Qubits, superposition, interference as a *new model of computation* — what changes vs a classical computer. | quantum (Nielsen) |
| 8710 | Quantum algorithms | Why some problems could be dramatically faster (Shor/Grover as ideas); and the many where quantum gives nothing. | quantum (Watrous) |
| 8720 | The reality: NISQ & error correction | Noise, decoherence, the enormous overhead of error correction — an honest "where it actually is." | quantum (Preskill), pD16 (qec, nisq) |
| 8730 | Quantum + AI | Quantum machine learning — the sober assessment of a hype-heavy intersection. | quantum, pD16 |

**Computer systems** ◧ (8800s) — grounds: computer-systems (OSTEP, Kleppmann, networks, crypto)
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 8800 | Operating systems & the machine | Processes, memory, the illusions the OS maintains — what "running" software really means. | computer-systems (OSTEP) |
| 8810 | Networks & the internet | Packets, protocols, layering; how the distributed substrate of AI services holds together. | computer-systems |
| 8820 | Data-intensive systems | Databases, storage, consistency (Kleppmann) — the durable principles of handling data at scale. | computer-systems (Kleppmann) |
| 8830 | Distributed systems | Consensus, replication, failure — why scale is hard and what guarantees are even possible. | computer-systems |
| 8840 | Cryptography & security | Trust without a trusted party; the primitives (and their limits) under digital security. | computer-systems (Boneh-Shoup) |

**Blockchain & decentralization** ▫ (8900s) — grounds: blockchain-web3
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 8900 | Decentralization — the durable idea | Trustless consensus (the one genuinely new idea); what it solves and its hard trade-offs (the trilemma). | blockchain-web3 |
| 8910 | Where blockchain meets AI | Compute markets, provenance/attestation of AI outputs, incentives — the honest, non-hype intersection. | blockchain-web3, tr/ |

## B3 · Rest-of-mathematics — [`30-math-and-theory/`](30-math-and-theory/) (Literacy slice)
▫ (keys 9000s) — the math beyond the AGI-math Core (A2), held for depth and for the branches that need it. Grounds: math-theory (Hefferon, Trench, Judson, Morris, Levin).
| Key | Module | Durable core | Ground |
|---|---|---|---|
| 9000 | Real analysis | The rigor under calculus — what "limit," "continuous," "converges" actually mean; why proofs matter. | math-theory (Trench) |
| 9010 | Abstract algebra | Groups/rings/fields — the study of structure itself; the language of symmetry (physics) and crypto. | math-theory (Judson) |
| 9020 | Topology | Shape & continuity without distance; the "rubber-sheet" view that appears in data (manifolds) and beyond. | math-theory (Morris) |
| 9030 | Number theory | Integers, primes, modular arithmetic — pure beauty that turns out to be the backbone of cryptography. | math-theory (Stein) |
| 9040 | Discrete math & combinatorics | Counting, graphs, logic — the mathematics of computation and algorithms. | math-theory (Levin) |
| 9050 | Differential equations & dynamical systems | How things change over time; the language of physics, control, and continuous-time models (neural ODEs). | math-theory, co/ |

---
---

## How this blueprint grows (the dynamic protocol)

This file is **living** ([`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) house-rule: nothing final). It changes by the same lifecycle as a module ([`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §8):

1. **A new topic appears** (from writing, from the corpus, from the learner) → add a row at the right sort-key; if it belongs between two existing rows, use a fine key (`1325`→`13255`).
2. **A row proves too big** → split it into a sub-cluster (a numbering gap opens the room). Too thin/duplicative → merge or drop.
3. **A tier is wrong** → re-tier the row and note why (the Atlas §1 is the tier's home; keep them in sync).
4. **A module gets written** → its status flips ♻️/⬜ → ✅ *in [`00_MAP.md`](00_MAP.md) and here*; the [`_QUEUE.md`](_QUEUE.md) row is closed; [`WHATS_NEW.md`](WHATS_NEW.md) gets a line.
5. **Write-pulls-gather** ([`../INSTRUCTIONS/PRODUCTION_FLOW.md`](../INSTRUCTIONS/PRODUCTION_FLOW.md) ⑥) may reveal a real corpus hole → a *surgical GET*, then the row's Ground column is updated.

**Estimated scope:** ~130 Trunk modules (A0–A7) + ~55 Branch modules (B1–B3) ≈ **185 planned files** (the AI domain, A3–A4, is ~65 of them). This is a multi-year plan, produced in leverage order — never all at once.

## Consistency (per [`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) §8)
- **Curriculum vs. `00_MAP`:** no contradiction — `00_MAP` is the ~24-rung reading spine; this file expands each rung into its leaf modules. `00_MAP` stays the friendly order; this is the full inventory. Both point to the same files.
- **Curriculum vs. just-in-time Atlas / anti-over-scaffolding:** resolved above — a *plan of titles* is not *built files or populated Atlas slices*. Files and Atlas slices remain just-in-time; only the map is drawn in full. This is the leverage rule applied to planning: cheap to enumerate, expensive to build, so enumerate freely and build on demand.
- **Curriculum vs. `_QUEUE`:** the Queue is the *order*; this is the *set*. The Queue always draws its next item from this blueprint and re-sorts; this file does not encode priority (leverage lives in the Queue).
- **Tiers vs. "cover every domain":** unchanged from [`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) Reconciliations — tiers set *how deep*, not *whether*; a Literacy branch still counts as covered only once it yields grounded modules.

---
*This blueprint is the map; the [`_QUEUE.md`](_QUEUE.md) is the next step on it; the [`../RESOURCES/corpus/_ATLAS.md`](../RESOURCES/corpus/_ATLAS.md) grounds each step; [`00_MAP.md`](00_MAP.md) is the reading order through the finished ones. Start where the Queue points — currently the AI core (A3.4 LLMs), the richest-grounded, highest-leverage slice.*
