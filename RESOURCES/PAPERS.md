# PAPERS, BLOGS & EXPLAINERS — catalog
**Landmark → state-of-the-art research, plus the best blogs, explainers, and lab research hubs.** Nearly all are **free** (arXiv + lab sites). These feed the learning modules as *chunks* (per [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §12).

`Status: Living catalog · System Version: 1.9 · Last updated: 2026-06-22`

> **Honesty / QC note:** titles + authors + year are the stable handle; the arXiv IDs below are for the most-cited papers and should be **auto-verified before citing in a module** (avoids any wrong-number risk). Papers behind Nature/Science paywalls almost always have a **free lab/author copy** — noted where relevant. **You do not need to buy papers or blogs** — the buy-list ([`REQUESTS.md`](REQUESTS.md)) stays books.
>
> **✅ Verification log (2026-06-27, corpus gathering session 1):** the **8 spine arXiv IDs** were checked against the live arXiv API (title + first author + year) and are **all correct** — `1512.03385` ResNet, `1706.03762` Attention, `2005.14165` GPT-3, `2001.08361` Kaplan-Scaling, `2203.15556` Chinchilla, `2203.02155` InstructGPT, `1312.5602` DQN, `1707.06347` PPO. These 10 spine papers (+ AlexNet NeurIPS, AlphaGo Nature, both fetched from free copies) are now in [`corpus/papers/`](corpus/). Remaining D1–D12 IDs still to verify on demand before a module cites them.

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
| [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — Rich Sutton | The single most *strategy-relevant* essay for a builder: general methods that scale with **compute + search** keep beating hand-built human cleverness. This is how to place your bets. |
| [Neel Nanda](https://www.neelnanda.io/) | Mechanistic interpretability, beginner → research. |
| [Gwern](https://gwern.net/) · [The Gradient](https://thegradient.pub/) · [Ruder](https://www.ruder.io/) | Long-form analysis; NLP. |

---

## D. Landmark papers by era & area (oldest → newest within each section)

### D0 · Foundations (pre–deep-learning)
- **1943** McCulloch & Pitts — *A Logical Calculus of Ideas Immanent in Nervous Activity* (the artificial neuron).
- **1948** Shannon — *A Mathematical Theory of Communication* (information theory). → `r-shannon`
- **1950** Turing — *Computing Machinery and Intelligence* (the "imitation game").
- **1958** Rosenblatt — *The Perceptron*.
- **1969** Minsky & Papert — *Perceptrons* (proved single-layer limits → triggered the first "AI winter"; *why depth matters*).
- **1980** Fukushima — *Neocognitron* (hierarchical, shift-invariant feature detectors — the convolution/hierarchy idea before CNNs).
- **1982** Hopfield — *Neural Networks and Physical Systems with Emergent Collective Computational Abilities* (Hopfield networks; **2024 Physics Nobel** to Hopfield & Hinton).
- **1986** Rumelhart, Hinton & Williams — *Learning representations by back-propagating errors* (backprop).
- **1989** Cybenko — *Approximation by Superpositions of a Sigmoidal Function* (the universal approximation theorem).
- **1995** Cortes & Vapnik — *Support-Vector Networks* (the max-margin idea; dominated ML before deep learning).
- **1997** Hochreiter & Schmidhuber — *Long Short-Term Memory* (LSTM).
- **1998** LeCun et al. — *Gradient-Based Learning Applied to Document Recognition* (LeNet/CNNs).
- **2006** Hinton, Osindero & Teh — *A Fast Learning Algorithm for Deep Belief Nets* (layer-wise pre-training — the result that reignited "deep" learning).

### D1 · The deep-learning breakthrough (2012–2016)
- **2012** Krizhevsky, Sutskever & Hinton — *ImageNet Classification with Deep CNNs* (AlexNet).
- **2013** Mikolov et al. — *Efficient Estimation of Word Representations* (word2vec) — arXiv:1301.3781.
- **2013** Kingma & Welling — *Auto-Encoding Variational Bayes* (VAE) — arXiv:1312.6114.
- **2014** Goodfellow et al. — *Generative Adversarial Networks* — arXiv:1406.2661.
- **2014** Sutskever, Vinyals & Le — *Sequence to Sequence Learning* — arXiv:1409.3215.
- **2014** Bahdanau, Cho & Bengio — *Neural Machine Translation by Jointly Learning to Align and Translate* (the **original attention mechanism** — the seed the transformer grew from) — arXiv:1409.0473.
- **2014** Kingma & Ba — *Adam optimizer* — arXiv:1412.6980.
- **2014** Simonyan & Zisserman — *Very Deep Convolutional Networks for Large-Scale Image Recognition* (VGG) — arXiv:1409.1556.
- **2014** Szegedy et al. — *Going Deeper with Convolutions* (GoogLeNet / Inception) — arXiv:1409.4842.
- **2014** Srivastava et al. — *Dropout: A Simple Way to Prevent Neural Networks from Overfitting* (JMLR).
- **2015** Ioffe & Szegedy — *Batch Normalization* — arXiv:1502.03167.
- **2015** Ronneberger et al. — *U-Net: Convolutional Networks for Biomedical Image Segmentation* — arXiv:1505.04597 *(its encoder–decoder later became the backbone of diffusion models).*
- **2015** He et al. — *Deep Residual Learning* (ResNet) — arXiv:1512.03385.

### D2 · Attention & the transformer era (2017–2020)
- **2017** Vaswani et al. — *Attention Is All You Need* (the transformer) — arXiv:1706.03762.
- **2018** Peters et al. — *Deep Contextualized Word Representations* (ELMo) — arXiv:1802.05365.
- **2018** Devlin et al. — *BERT: Pre-training of Deep Bidirectional Transformers* — arXiv:1810.04805.
- **2018–20** Radford et al. / Brown et al. — *GPT-1/2/3*; GPT-3 *Language Models are Few-Shot Learners* — arXiv:2005.14165.
- **2019** Raffel et al. — *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer* (T5) — arXiv:1910.10683.
- **2020** Dosovitskiy et al. — *An Image is Worth 16×16 Words* (Vision Transformer) — arXiv:2010.11929.

### D3 · Scaling, emergence & reasoning (2020–)
- **2020** Kaplan et al. — *Scaling Laws for Neural Language Models* — arXiv:2001.08361.
- **2022** Hoffmann et al. — *Training Compute-Optimal LLMs* (Chinchilla) — arXiv:2203.15556.
- **2022** Wei et al. — *Emergent Abilities of LLMs* — arXiv:2206.07682.
- **2022** Wei et al. — *Chain-of-Thought Prompting* — arXiv:2201.11903.
- **2023** Schaeffer et al. — *Are Emergent Abilities a Mirage?* — arXiv:2304.15004 *(the rebuttal — read both).*
- **2021** Bommasani et al. — *On the Opportunities and Risks of Foundation Models* (Stanford CRFM — named the category) — arXiv:2108.07258.
- **2022** Chowdhery et al. — *PaLM: Scaling Language Modeling with Pathways* — arXiv:2204.02311.
- **2022** Lewkowycz et al. — *Minerva: Solving Quantitative Reasoning Problems with LMs* — arXiv:2206.14858.
- **2022** Wang et al. — *Self-Consistency Improves Chain-of-Thought Reasoning* — arXiv:2203.11171.
- **2023** OpenAI — *GPT-4 Technical Report* — arXiv:2303.08774.
- **2023** Bubeck et al. (Microsoft) — *Sparks of Artificial General Intelligence: Early experiments with GPT-4* — arXiv:2303.12712.
- **2023** Yao et al. — *Tree of Thoughts: Deliberate Problem Solving with LLMs* — arXiv:2305.10601.
- **2021** Wei et al. — *Finetuned Language Models Are Zero-Shot Learners* (FLAN — **instruction tuning**: the idea that turned raw next-word predictors into instruction-followers) — arXiv:2109.01652.
- **2024** OpenAI — *Learning to Reason with LLMs* (o1 — scaling **test-time / inference compute**; the idea behind the reasoning-model era).
- **2025** DeepSeek-AI — *DeepSeek-R1: Incentivizing Reasoning via RL* — arXiv:2501.12948. *(opened the "reasoning model via RL" wave — the open recipe.)*
- **2025–26 SOTA** — frontier reasoning models (GPT-5-era, Gemini 2.5, etc.); track via section A rather than freezing here.

### D4 · Alignment, RLHF & safety
*First, the framing — understanding the **shape of the problem** matters more for a director than any single method:*
- **2016** Amodei et al. — *Concrete Problems in AI Safety* (the paper that set the practical safety agenda) — arXiv:1606.06565.
- **2018** Irving et al. (OpenAI) — *AI Safety via Debate* (scalable oversight: judging systems smarter than us) — arXiv:1805.00899.
- **2021** Hendrycks et al. — *Unsolved Problems in ML Safety* (the modern taxonomy: robustness, monitoring, alignment, systemic safety) — arXiv:2109.13916.

*Then the methods that produced today's assistants:*
- **2017** Christiano et al. — *Deep RL from Human Preferences* (the root of RLHF) — arXiv:1706.03741.
- **2020** Stiennon et al. — *Learning to Summarize from Human Feedback* — arXiv:2009.01325.
- **2022** Ouyang et al. — *Training LMs to follow instructions with human feedback* (InstructGPT/RLHF) — arXiv:2203.02155.
- **2022** Bai et al. (Anthropic) — *Constitutional AI: Harmlessness from AI Feedback* — arXiv:2212.08073.
- **2023** Rafailov et al. — *Direct Preference Optimization* (DPO — RLHF without a separate reward model or PPO) — arXiv:2305.18290.
- **2023** Burns et al. (OpenAI) — *Weak-to-Strong Generalization* (can a weak supervisor align a stronger model?) — arXiv:2312.09390.
- **2024** Hubinger et al. (Anthropic) — *Sleeper Agents: Training Deceptive LLMs that Persist through Safety Training* — arXiv:2401.05566.
- **2023** Lightman et al. (OpenAI) — *Let's Verify Step by Step* (process- vs outcome-reward — supervising *how* a model reasons, not just its answer) — arXiv:2305.20050.
- **interp** Olah et al. — *Zoom In: Circuits* (Distill); Anthropic — *Toy Models of Superposition* (2022), *Towards Monosemanticity* (2023) & *Scaling Monosemanticity* (2024, SAE features inside Claude 3 Sonnet), *Tracing the Thoughts of a Language Model* (2025) — all at [transformer-circuits.pub](https://transformer-circuits.pub/).

### D5 · Reinforcement learning landmarks
**Algorithms (the toolbox):**
- **2013/2015** Mnih et al. — *Playing Atari with Deep RL* (DQN, arXiv:1312.5602) → *Human-level control through deep RL* (Nature 2015, free lab copy).
- **2015** Schulman et al. — *Trust Region Policy Optimization* (TRPO) — arXiv:1502.05477.
- **2015** Lillicrap et al. — *Continuous Control with Deep RL* (DDPG) — arXiv:1509.02971.
- **2016** Mnih et al. — *Asynchronous Methods for Deep RL* (A3C) — arXiv:1602.01783.
- **2017** Schulman et al. — *Proximal Policy Optimization* (PPO — the workhorse; also drives RLHF) — arXiv:1707.06347.
- **2018** Haarnoja et al. — *Soft Actor-Critic* (SAC) — arXiv:1801.01290.

**Grand-challenge agents (what RL achieved):**
- **2016** Silver et al. — *Mastering the Game of Go* (AlphaGo, Nature; free copy via UCL/DeepMind).
- **2017** Silver et al. — *Mastering the game of Go without human knowledge* (AlphaGo Zero, Nature).
- **2017** Silver et al. — *Mastering Chess and Shogi by Self-Play* (AlphaZero) — arXiv:1712.01815.
- **2019/20** Schrittwieser et al. — *MuZero: Mastering games without knowing the rules* (Nature).
- **2019** Vinyals et al. — *Grandmaster level in StarCraft II* (AlphaStar, Nature).
- **2019** OpenAI et al. — *Dota 2 with Large Scale Deep RL* (OpenAI Five) — arXiv:1912.06680.
- **2022** Meta FAIR et al. — *Human-level play in Diplomacy by combining language models with strategic reasoning* (CICERO, Science).
- **2023** Hafner et al. — *Mastering Diverse Domains through World Models* (DreamerV3) — arXiv:2301.04104.

### D6 · Efficiency, systems & inference (making it trainable and servable)
**Sparsity / Mixture-of-Experts:**
- **2017** Shazeer et al. — *Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer* — arXiv:1701.06538.
- **2021** Fedus et al. — *Switch Transformers: Scaling to Trillion-Parameter Models* — arXiv:2101.03961.
- **2024** Jiang et al. (Mistral) — *Mixtral of Experts* (open sparse-MoE LLM) — arXiv:2401.04088.

**Attention & long context:**
- **2021** Su et al. — *RoFormer: Rotary Position Embedding* (RoPE — used by most modern LLMs) — arXiv:2104.09864.
- **2021** Press et al. — *Train Short, Test Long: Attention with Linear Biases* (ALiBi) — arXiv:2108.12409.
- **2022** Dao et al. — *FlashAttention: Fast, Memory-Efficient Exact Attention* (→ FlashAttention-2/-3) — arXiv:2205.14135.

**Training & inference systems:**
- **2019** Shoeybi et al. — *Megatron-LM: Training Multi-Billion-Parameter LMs with Model Parallelism* — arXiv:1909.08053.
- **2019** Rajbhandari et al. — *ZeRO: Memory Optimizations Toward Training Trillion-Parameter Models* — arXiv:1910.02054.
- **2023** Leviathan et al. — *Fast Inference from Transformers via Speculative Decoding* — arXiv:2211.17192.
- **2023** Kwon et al. — *Efficient Memory Management for LLM Serving with PagedAttention* (vLLM) — arXiv:2309.06180.

**Adaptation & quantization (do more with less):**
- **2021** Hu et al. — *LoRA: Low-Rank Adaptation of Large Language Models* — arXiv:2106.09685.
- **2022** Frantar et al. — *GPTQ: Accurate Post-Training Quantization for GPTs* — arXiv:2210.17323.
- **2023** Dettmers et al. — *QLoRA: Efficient Finetuning of Quantized LLMs* — arXiv:2305.14314.
- **2023** Touvron et al. — *LLaMA: Open and Efficient Foundation LMs* (the open-weights lineage → Llama 2/3) — arXiv:2302.13971.

### D7 · Diffusion & generative models (images, audio, video)
- **2015** Sohl-Dickstein et al. — *Deep Unsupervised Learning using Nonequilibrium Thermodynamics* (the diffusion idea) — arXiv:1503.03585.
- **2019** Song & Ermon — *Generative Modeling by Estimating Gradients of the Data Distribution* (score-based) — arXiv:1907.05600.
- **2020** Ho et al. — *Denoising Diffusion Probabilistic Models* (DDPM) — arXiv:2006.11239.
- **2020** Song et al. — *Score-Based Generative Modeling through SDEs* (unifying framework) — arXiv:2011.13456.
- **2021** Dhariwal & Nichol — *Diffusion Models Beat GANs on Image Synthesis* — arXiv:2105.05233.
- **2022** Ho & Salimans — *Classifier-Free Diffusion Guidance* — arXiv:2207.12598.
- **2022** Rombach et al. — *High-Resolution Image Synthesis with Latent Diffusion Models* (Stable Diffusion) — arXiv:2112.10752.
- **2022** Ramesh et al. — *Hierarchical Text-Conditional Image Generation with CLIP Latents* (DALL·E 2) — arXiv:2204.06125.
- **2022** Saharia et al. — *Photorealistic Text-to-Image Diffusion Models* (Imagen) — arXiv:2205.11487.
- **2021** Song et al. — *Denoising Diffusion Implicit Models* (DDIM — fast deterministic sampling) — arXiv:2010.02502.
- **2023** Song et al. — *Consistency Models* (few-step generation) — arXiv:2303.01469.
- **2023** Zhang et al. — *Adding Conditional Control to Text-to-Image Diffusion Models* (ControlNet — controllable generation) — arXiv:2302.05543.
- **2023** Peebles & Xie — *Scalable Diffusion Models with Transformers* (DiT — swap the U-Net for a transformer; the backbone behind Sora) — arXiv:2212.09748.
- **2024** OpenAI — *Video Generation Models as World Simulators* (Sora technical report) — text-to-video at scale.

### D8 · Multimodal & vision-language
- **2021** Radford et al. — *Learning Transferable Visual Models from Natural Language Supervision* (CLIP) — arXiv:2103.00020.
- **2022** Alayrac et al. (DeepMind) — *Flamingo: a Visual Language Model for Few-Shot Learning* — arXiv:2204.14198.
- **2022** Radford et al. — *Robust Speech Recognition via Large-Scale Weak Supervision* (Whisper) — arXiv:2212.04356.
- **2023** Li et al. — *BLIP-2: Bootstrapping Language-Image Pre-training* — arXiv:2301.12597.
- **2023** Liu et al. — *Visual Instruction Tuning* (LLaVA) — arXiv:2304.08485.
- **2023** Girdhar et al. (Meta) — *ImageBind: One Embedding Space to Bind Them All* — arXiv:2305.05665.

### D9 · Agents, tool use & retrieval (RAG)
**Retrieval-augmented LMs:**
- **2020** Karpukhin et al. (Meta) — *Dense Passage Retrieval for Open-Domain QA* (DPR — embedding-based retrieval, the engine under most RAG) — arXiv:2004.04906.
- **2020** Guu et al. — *REALM: Retrieval-Augmented Language Model Pre-Training* — arXiv:2002.08909.
- **2020** Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP* (RAG) — arXiv:2005.11401.
- **2021** Borgeaud et al. (DeepMind) — *Improving LMs by Retrieving from Trillions of Tokens* (RETRO) — arXiv:2112.04426.
- **2023** Asai et al. — *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection* — arXiv:2310.11511.

**Tool use & autonomous agents:**
- **2021** Nakano et al. (OpenAI) — *WebGPT: Browser-Assisted Question-Answering with Human Feedback* (the idea of an LM *using tools / the web*) — arXiv:2112.09332.
- **2021** Chen et al. — *Decision Transformer: RL via Sequence Modeling* — arXiv:2106.01345.
- **2022** Reed et al. (DeepMind) — *A Generalist Agent* (Gato) — arXiv:2205.06175.
- **2022** Yao et al. — *ReAct: Synergizing Reasoning and Acting in LMs* — arXiv:2210.03629.
- **2023** Schick et al. (Meta) — *Toolformer: LMs Can Teach Themselves to Use Tools* — arXiv:2302.04761.
- **2023** Shinn et al. — *Reflexion: Language Agents with Verbal Reinforcement Learning* — arXiv:2303.11366.
- **2023** Park et al. — *Generative Agents: Interactive Simulacra of Human Behavior* — arXiv:2304.03442.
- **2023** Wang et al. (NVIDIA) — *Voyager: An Open-Ended Embodied Agent with LLMs* — arXiv:2305.16291.

### D10 · Beyond the transformer (efficient sequence architectures)
- **2020** *Efficient-attention transformers* — Reformer, Longformer, BigBird, Performer (the **sub-quadratic attention** idea: make attention scale better than O(n²) in sequence length).
- **2021** Gu et al. — *Efficiently Modeling Long Sequences with Structured State Spaces* (S4 — the state-space-model line) — arXiv:2111.00396.
- **2023** Peng et al. — *RWKV: Reinventing RNNs for the Transformer Era* — arXiv:2305.13048.
- **2023** Sun et al. (Microsoft) — *Retentive Network: A Successor to Transformer for LLMs* (RetNet) — arXiv:2307.08621.
- **2023** Poli et al. — *Hyena Hierarchy: Towards Larger Convolutional Language Models* (long convolutions instead of attention) — arXiv:2302.10866.
- **2023** Gu & Dao — *Mamba: Linear-Time Sequence Modeling with Selective State Spaces* — arXiv:2312.00752.
- **2024** Lieber et al. (AI21) — *Jamba: A Hybrid Transformer-Mamba Language Model* (the practical hybrid mixing both) — arXiv:2403.19887.

### D11 · Robotics & embodied AI (intelligence that acts in the world)
- **2016** Levine et al. — *End-to-End Training of Deep Visuomotor Policies* (pixels → motor torques; the founding deep-robot-learning result) — arXiv:1504.00702.
- **2018** Ha & Schmidhuber — *World Models* (learning to act inside a learned simulator) — arXiv:1803.10122.
- **2019** OpenAI et al. — *Solving Rubik's Cube with a Robot Hand* (Dactyl — domain randomization for sim-to-real transfer) — arXiv:1910.07113.
- **2022** Brohan et al. (Google) — *RT-1: Robotics Transformer for Real-World Control at Scale* — arXiv:2212.06817.
- **2022** Ahn et al. (Google) — *Do As I Can, Not As I Say: Grounding Language in Robotic Affordances* (SayCan — pair an LLM's plan with a robot's learned skills) — arXiv:2204.01691.
- **2023** Driess et al. (Google) — *PaLM-E: An Embodied Multimodal Language Model* — arXiv:2303.03378.
- **2023** Chi et al. — *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion* — arXiv:2303.04137.
- **2023** Zhao et al. — *Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware* (ALOHA / ACT) — arXiv:2304.13705.
- **2023** Brohan et al. (Google DeepMind) — *RT-2: Vision-Language-Action Models* (web knowledge → robot control) — arXiv:2307.15818.
- **2023** Open X-Embodiment Collaboration — *Open X-Embodiment: Robotic Learning Datasets and RT-X* — arXiv:2310.08864.
- **2023** Ma et al. (NVIDIA) — *Eureka: Human-Level Reward Design via Coding LLMs* — arXiv:2310.12931.
- **2024** Kim et al. — *OpenVLA: An Open-Source Vision-Language-Action Model* — arXiv:2406.09246.
- **2024** Black et al. (Physical Intelligence) — *π0: A Vision-Language-Action Flow Model for General Robot Control* — arXiv:2410.24164.

### D12 · AI for science & the intersected frontier (where AI already changes the field)
*The clearest evidence of progress toward general capability: AI moving the frontier of other disciplines.*
- **2023** Wang et al. — *Scientific Discovery in the Age of Artificial Intelligence* (Nature — the umbrella review of AI-for-science).

**Biology, medicine & drug discovery:**
- **2021** Jumper et al. (DeepMind) — *Highly Accurate Protein Structure Prediction with AlphaFold* (AlphaFold 2, Nature; free lab copy) — **2024 Chemistry Nobel** (Hassabis & Jumper).
- **2021** Baek et al. (Baker lab) — *Accurate Prediction of Protein Structures and Interactions Using a Three-Track Network* (RoseTTAFold, Science) — the independent breakthrough (Baker shared the **2024 Chemistry Nobel**).
- **2022** Singhal et al. (Google) — *Large Language Models Encode Clinical Knowledge* (Med-PaLM) — arXiv:2212.13138.
- **2023** Lin et al. (Meta) — *Evolutionary-Scale Prediction of Atomic-Level Protein Structure with a Language Model* (ESM-2 / ESMFold, Science).
- **2023** Cheng et al. (DeepMind) — *Accurate Proteome-Wide Missense Variant Effect Prediction* (AlphaMissense, Science).
- **2024** Abramson et al. (DeepMind / Isomorphic) — *Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3* (Nature).
- **2024** Nguyen et al. (Arc Institute / Stanford) — *Sequence Modeling and Design from Molecular to Genome Scale with Evo* (a DNA foundation model, Science).

**Mathematics & algorithms:**
- **2022** Fawzi et al. (DeepMind) — *Discovering Faster Matrix Multiplication Algorithms with RL* (AlphaTensor, Nature).
- **2023** Mankowitz et al. (DeepMind) — *Faster Sorting Algorithms Discovered Using Deep RL* (AlphaDev, Nature).
- **2023** Romera-Paredes et al. (DeepMind) — *Mathematical Discoveries from Program Search with LLMs* (FunSearch, Nature).
- **2024** Trinh et al. (DeepMind) — *Solving Olympiad Geometry Without Human Demonstrations* (AlphaGeometry, Nature) → **AlphaProof & AlphaGeometry 2** reach IMO silver-medal level (2024).

**Code & software engineering:**
- **2021** Chen et al. (OpenAI) — *Evaluating Large Language Models Trained on Code* (Codex / the engine behind Copilot) — arXiv:2107.03374.
- **2022** Li et al. (DeepMind) — *Competition-Level Code Generation with AlphaCode* (Science) — arXiv:2203.07814.
- **2023/24** Jimenez et al. & Yang et al. — *SWE-bench* (arXiv:2310.06770) and *SWE-agent* (arXiv:2405.15793): can agents resolve real GitHub issues?

**Physics, materials, weather & climate:**
- **2022** Degrave et al. (DeepMind) — *Magnetic Control of Tokamak Plasmas Through Deep RL* (Nature) — AI for fusion.
- **2023** Merchant et al. (DeepMind) — *Scaling Deep Learning for Materials Discovery* (GNoME, Nature) — 2.2M new crystals.
- **2025** Zeni et al. (Microsoft) — *A Generative Model for Inorganic Materials Design* (MatterGen — design new materials to order, Nature).
- **2023** M. Bran et al. — *ChemCrow: Augmenting LLMs with Chemistry Tools* (LLM agents that plan and run chemistry) — arXiv:2304.05376.
- **2023** Lam et al. (DeepMind) — *Learning Skillful Medium-Range Global Weather Forecasting* (GraphCast, Science) — arXiv:2212.12794.
- **2024** Price et al. (DeepMind) — *Probabilistic Weather Forecasting with Machine Learning* (GenCast, Nature).
- **2024** Kochkov et al. (Google) — *Neural General Circulation Models for Weather and Climate* (NeuralGCM — hybrid physics + ML, Nature).

**Space, astronomy & the cosmos:**
- **2015** Dieleman et al. — *Rotation-Invariant Convolutional Neural Networks for Galaxy Morphology Prediction* (MNRAS).
- **2018** Shallue & Vanderburg — *Identifying Exoplanets with Deep Learning* (found Kepler-90i, making Kepler-90 an 8-planet system) — The Astronomical Journal.
- **2018** George & Huerta — *Deep Learning for Real-Time Gravitational-Wave Detection and Parameter Estimation* (Physics Letters B).
- **2023** Medeiros et al. (Event Horizon Telescope) — *The Image of the M87 Black Hole Reconstructed with PRIMO* (ML image reconstruction, ApJ Letters).
- *Also:* deep learning now powers Earth-observation/climate pipelines and the survey data of Rubin/LSST and Euclid.

**Quantum computing × AI (each accelerating the other):**
- **2017** Biamonte et al. — *Quantum Machine Learning* (Nature — the field-defining review).
- **2024** Bausch et al. (Google DeepMind × Google Quantum AI) — *Learning High-Accuracy Error Decoding for Quantum Processors* (AlphaQubit, Nature) — neural decoding below the surface-code error threshold.

**Neuroscience & brain–computer interfaces:**
- **2023** Takagi & Nishimoto — *High-Resolution Image Reconstruction with Latent Diffusion Models from Human Brain Activity* (CVPR).
- **2023** Tang et al. — *Semantic Reconstruction of Continuous Language from Non-Invasive Brain Recordings* (Nature Neuroscience) — decoding meaning from fMRI.
- **2023** Willett et al. — *A High-Performance Speech Neuroprosthesis* (Nature) — BCI speech decoding near conversational rate.

**Decentralized & web3 AI (a real but earlier-stage frontier):**
- **2022** Borzunov et al. — *Petals: Collaborative Inference and Fine-Tuning of Large Models* (serve 100B+ models across volunteer hardware) — arXiv:2209.01188.
- **2023** Douillard et al. (DeepMind) — *DiLoCo: Distributed Low-Communication Training of Language Models* (train across weakly-connected islands of compute) — arXiv:2311.08105.
- *Honest note:* the concrete wins so far are **decentralized training/inference** and **verifiable ML** (zkML — zero-knowledge proofs that an inference actually ran). Broader "crypto × AI" — tokenized compute markets (e.g. Bittensor), on-chain autonomous agents, agent-to-agent payments — is genuinely active but **earlier-stage and light on peer-reviewed landmarks**: tracked, not overclaimed.

**Emerging & fast-moving frontiers (track, don't freeze — per Section A):**
- **2021** Mirhoseini et al. (Google) — *A Graph Placement Methodology for Fast Chip Design* (Nature) → **AlphaChip** (2024) — AI designs the chips that run AI.
- **2023** Watson et al. — *De Novo Design of Protein Structure and Function with RFdiffusion* (Nature) — generative biology (design, not just prediction).
- **2023** Boiko et al. — *Autonomous Chemical Research with Large Language Models* (Coscientist, Nature) — "self-driving labs."
- **2024** Bruce et al. (DeepMind) — *Genie: Generative Interactive Environments* (playable world models from video) → Genie 2/3.
- **2025** Hollmann et al. — *Accurate Predictions on Small Data with a Tabular Foundation Model* (TabPFN, Nature) — foundation models reach tabular/scientific data.
- *Also moving monthly:* time-series foundation models (TimesFM, Chronos), computer-use / GUI agents, AI for energy-grid & fusion control, agentic-AI economies, and AI tutoring. These shift too fast to freeze — follow the living sources in **Section A**.

---

## E. Anything paywalled?
- **Nature/Science papers** (DQN, AlphaGo, AlphaFold): the journal page is paywalled, but **free author/lab copies exist** — I'll link those in the module; **no need to buy.**
- **Books** are the only real purchases → [`REQUESTS.md`](REQUESTS.md).
- If I ever hit a genuinely paywalled, no-preprint paper that we truly need, I'll add it to [`REQUESTS.md`](REQUESTS.md) with the reason.

*This catalog grows as the ladder advances; each paper is read and chunked into the relevant module, never dumped wholesale.*
