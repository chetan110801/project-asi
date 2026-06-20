# PAPERS, BLOGS & EXPLAINERS — catalog
**Landmark → state-of-the-art research, plus the best blogs, explainers, and lab research hubs.** Nearly all are **free** (arXiv + lab sites). These feed the learning modules as *chunks* (per [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §12).

`Status: Living catalog · System Version: 1.4 · Last updated: 2026-06-20`

> **Honesty / QC note:** titles + authors + year are the stable handle; the arXiv IDs below are for the most-cited papers and should be **auto-verified before citing in a module** (avoids any wrong-number risk). Papers behind Nature/Science paywalls almost always have a **free lab/author copy** — noted where relevant. **You do not need to buy papers or blogs** — the buy-list ([`REQUESTS.md`](REQUESTS.md)) stays books.

---

## A. Where SOTA actually appears (track these, don't freeze a list)
The frontier moves monthly, so the durable move is to follow *living* sources rather than a static list:
- **arXiv** — [cs.LG](https://arxiv.org/list/cs.LG/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.AI](https://arxiv.org/list/cs.AI/recent) (where almost all ML papers land first, free).
- **Papers With Code** — [paperswithcode.com](https://paperswithcode.com/) (SOTA leaderboards + code).
- **Sebastian Raschka's LLM paper lists** — [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/) (excellent curated monthly SOTA roundups, e.g., "LLM Research Papers: The 2026 List").

## B. Lab / company research hubs (primary sources)
| Lab | Research hub |
|---|---|
| Google DeepMind | [deepmind.google/research](https://deepmind.google/research/) |
| OpenAI | [openai.com/research](https://openai.com/research) |
| Anthropic | [anthropic.com/research](https://www.anthropic.com/research) + [alignment.anthropic.com](https://alignment.anthropic.com/) + [transformer-circuits.pub](https://transformer-circuits.pub/) |
| Meta AI (FAIR) | [ai.meta.com/research](https://ai.meta.com/research/) |
| Google Research | [research.google](https://research.google/) |
| Microsoft Research | [microsoft.com/research](https://www.microsoft.com/en-us/research/) |
| Berkeley AI (BAIR) | [bair.berkeley.edu/blog](https://bair.berkeley.edu/blog/) |

## C. Famous blogs & explainers (validated, high-signal)
| Source | Why |
|---|---|
| [colah's blog](https://colah.github.io/) — Chris Olah | The clearest explainers ever (LSTMs, backprop, topology of NNs). |
| [Distill.pub](https://distill.pub/) | Interactive, peer-reviewed visual explanations (archived but gold). |
| [Lil'Log](https://lilianweng.github.io/) — Lilian Weng | Deep, current surveys (attention, RL, diffusion, agents). |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar | The famous visual intro to transformers (used at Stanford/MIT/Harvard). |
| [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP | The transformer paper, line-by-line in code. |
| [Karpathy's blog](https://karpathy.github.io/) + [karpathy.ai](https://karpathy.ai/) | "The Unreasonable Effectiveness of RNNs," plus build-from-scratch. |
| [Neel Nanda](https://www.neelnanda.io/) | Mechanistic interpretability, beginner → research. |
| [Gwern](https://gwern.net/) · [The Gradient](https://thegradient.pub/) · [Ruder](https://www.ruder.io/) | Long-form analysis; NLP. |

---

## D. Landmark papers by era (oldest → newest)

### D0 · Foundations (pre–deep-learning)
- **1943** McCulloch & Pitts — *A Logical Calculus of Ideas Immanent in Nervous Activity* (the artificial neuron).
- **1948** Shannon — *A Mathematical Theory of Communication* (information theory). → `r-shannon`
- **1950** Turing — *Computing Machinery and Intelligence* (the "imitation game").
- **1958** Rosenblatt — *The Perceptron*.
- **1986** Rumelhart, Hinton & Williams — *Learning representations by back-propagating errors* (backprop).
- **1997** Hochreiter & Schmidhuber — *Long Short-Term Memory* (LSTM).
- **1998** LeCun et al. — *Gradient-Based Learning Applied to Document Recognition* (LeNet/CNNs).

### D1 · The deep-learning breakthrough (2012–2016)
- **2012** Krizhevsky, Sutskever & Hinton — *ImageNet Classification with Deep CNNs* (AlexNet).
- **2013** Mikolov et al. — *Efficient Estimation of Word Representations* (word2vec) — arXiv:1301.3781.
- **2013** Kingma & Welling — *Auto-Encoding Variational Bayes* (VAE) — arXiv:1312.6114.
- **2014** Goodfellow et al. — *Generative Adversarial Networks* — arXiv:1406.2661.
- **2014** Sutskever, Vinyals & Le — *Sequence to Sequence Learning* — arXiv:1409.3215.
- **2014** Kingma & Ba — *Adam optimizer* — arXiv:1412.6980.
- **2015** Ioffe & Szegedy — *Batch Normalization* — arXiv:1502.03167.
- **2015** He et al. — *Deep Residual Learning* (ResNet) — arXiv:1512.03385.

### D2 · Attention & the transformer era (2017–2020)
- **2017** Vaswani et al. — *Attention Is All You Need* (the transformer) — arXiv:1706.03762.
- **2018** Devlin et al. — *BERT* — arXiv:1810.04805.
- **2018–20** Radford et al. / Brown et al. — *GPT-1/2/3*; GPT-3 *Language Models are Few-Shot Learners* — arXiv:2005.14165.
- **2020** Dosovitskiy et al. — *An Image is Worth 16×16 Words* (Vision Transformer) — arXiv:2010.11929.

### D3 · Scaling, emergence & reasoning (2020–)
- **2020** Kaplan et al. — *Scaling Laws for Neural Language Models* — arXiv:2001.08361.
- **2022** Hoffmann et al. — *Training Compute-Optimal LLMs* (Chinchilla) — arXiv:2203.15556.
- **2022** Wei et al. — *Emergent Abilities of LLMs* — arXiv:2206.07682.
- **2022** Wei et al. — *Chain-of-Thought Prompting* — arXiv:2201.11903.
- **2023** Schaeffer et al. — *Are Emergent Abilities a Mirage?* — arXiv:2304.15004 *(the rebuttal — read both).*
- **2025** DeepSeek-AI — *DeepSeek-R1: Incentivizing Reasoning via RL* — arXiv:2501.12948. *(opened the "reasoning model via RL" wave.)*
- **2025–26 SOTA** — frontier reasoning models (GPT-5-era, Gemini 2.5, etc.); track via section A rather than freezing here.

### D4 · Alignment, RLHF & safety
- **2022** Ouyang et al. — *Training LMs to follow instructions with human feedback* (InstructGPT/RLHF) — arXiv:2203.02155.
- **2022** Bai et al. (Anthropic) — *Constitutional AI* — arXiv:2212.08073.
- **interp** Olah et al. — *Zoom In: Circuits* (Distill); Anthropic — *Toy Models of Superposition*, *Tracing the Thoughts of an LLM* ([transformer-circuits.pub](https://transformer-circuits.pub/)).

### D5 · Reinforcement learning landmarks
- **2013/2015** Mnih et al. — *Playing Atari with Deep RL* (arXiv:1312.5602) → *Human-level control* (Nature 2015, free lab copy).
- **2016** Silver et al. — *Mastering the Game of Go* (AlphaGo, Nature; free copy via UCL/DeepMind).
- **2017** Silver et al. — *Mastering the game of Go without human knowledge* (AlphaGo Zero, Nature).
- **2017** Silver et al. — *Mastering Chess and Shogi by Self-Play* (AlphaZero) — arXiv:1712.01815.
- **2019/20** Schrittwieser et al. — *MuZero: Mastering games without knowing the rules*.

### D6 · Efficiency, adaptation & science
- **2021** Hu et al. — *LoRA: Low-Rank Adaptation* — arXiv:2106.09685.
- **2023** Touvron et al. — *LLaMA: Open and Efficient Foundation LMs* — arXiv:2302.13971.
- **2021** Jumper et al. — *Highly accurate protein structure prediction* (AlphaFold 2, Nature; free lab copy) — AI for science.

---

## E. Anything paywalled?
- **Nature/Science papers** (DQN, AlphaGo, AlphaFold): the journal page is paywalled, but **free author/lab copies exist** — I'll link those in the module; **no need to buy.**
- **Books** are the only real purchases → [`REQUESTS.md`](REQUESTS.md).
- If I ever hit a genuinely paywalled, no-preprint paper that we truly need, I'll add it to [`REQUESTS.md`](REQUESTS.md) with the reason.

*This catalog grows as the ladder advances; each paper is read and chunked into the relevant module, never dumped wholesale.*
