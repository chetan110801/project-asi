# ATLAS SLICE — AI / ML / DL / RL / LLMs / agents  (tier: ⬛ CORE — exhaustive)
**The grounding index for the machine-intelligence domain** — the map a writer greps *before* drafting any `1000–1399` (shelf `20-`) or `1360–1399` (shelf `25-`) module. Role & template: [`_ATLAS.md`](_ATLAS.md) §4; flow: [`../../INSTRUCTIONS/PRODUCTION_FLOW.md`](../../INSTRUCTIONS/PRODUCTION_FLOW.md) ② + ⑤.

`Part of: PROJECT ASI · Status: Living · Created: 2026-07-02 (session 22)`

> **⚠️ HOW TO SEARCH THIS DOMAIN:** the corpus text is **git-ignored**, so the IDE Grep tool skips it — use **Bash `grep -r`** with absolute paths under `RESOURCES/corpus/`. Chunks are `<src>_NNN.txt`; a paper's abstract is in its `_000` chunk; every folder has `_SOURCE.txt` (what it is) and most have `_manifest.txt`.

---

## §1. Concept spine
**The spine is NOT restated here (DRY).** It is the A3 + A4 sections of [`../../LEARNING/CURRICULUM.md`](../../LEARNING/CURRICULUM.md):
- **A3.1** ML foundations · keys 1000–1099 (19 rows)
- **A3.2** Deep learning · keys 1100–1199 (17 rows)
- **A3.3** RL & agents · keys 1200–1299 (17 rows)
- **A3.4** Language & sequence models · keys 1300–1359 (22 rows)
- **A4** Applied AI & agentic systems · keys 1360–1399 (11 rows, shelf `25-`)

Each Curriculum row already carries its one-line durable core + a short ground pointer. This slice expands those pointers into the **full grounding table** below.

## §2. Grounding table — concept cluster → corpus sources (all pools)
Levels: **E** elementary · **U** undergrad · **G** graduate · **R** research. Quality: ⭐ spine (lean on it) · ✓ solid · ~ supplementary.

| Concept cluster (keys) | `papers/` | `textbooks/` | `courses/` | `ai-ml-foundations/` + shelves | `transcripts/` + `frontier-rnd/` |
|---|---|---|---|---|---|
| **ML foundations (1000–1090)** | D13 `survey-optimization-ml-bottou`, `survey-transfer-learning`, `survey-contrastive-self-supervised` (R) | ⭐`bishop-prml` (G) · ⭐`esl` (G) · `islr2` (U) · `mml` (U) · `murphy-probabilistic-ml-intro-book1`+`-advanced-book2` (G, in ai-ml-foundations) · `hands-on-ml-3rd-edition` (U, code-heavy — durability-filter it) | ⭐`cs229-lectures`+`cs229-main-notes` (G) · `cs229m-ml-theory` (G) · `caltech-cs156-learning-from-data` (U) · `cornell-cs4780-machine-learning` (U) · `cmu-10-708-pgm` (G) | `distill-gaussian-processes`, `distill-momentum` (U✓) · `math-theory/` (ISLR/OpenIntro ladder) | `tr/` interviews for the classical-vs-deep judgment |
| **Deep learning (1100–1190)** | ⭐D1 (alexnet→resnet, seq2seq, adam, batchnorm, vae, gan, word2vec) (R) · D7 diffusion (R) · D13 `survey-graph-neural-networks`, `survey-diffusion-models-vision` | ⭐`goodfellow-dl` (G) · ⭐`prince-udl` (G, modern) · `bishop-dl` (G) · `d2l` (U, code-heavy) · `nielsen-nndl` (E–U, best intuition) | ⭐`cs231n` (U, +`cs231n-notes` in ai-ml-foundations) · `mit-6-7960-deep-learning` · `nyu-deep-learning-*` (LeCun) · `tubingen-deep-learning-geiger` · `cmu-11-785-intro-deep-learning` · `berkeley-cs182` · `umich-eecs498` · `deepmind-dl-2020/2021` · `mit-6-s191` | ⭐`ml-blogs-and-essays` (Bitter-Lesson + colah + Lil'Log) · `transformer-and-nn-explainers` (Alammar/Karpathy) · `distill-*`, `lilianweng-diffusion-models` | `tr/` Karpathy/Hinton-adjacent interviews (generalization debate) |
| **RL & agents (1200–1280)** | ⭐D5 (dqn, trpo, ppo, ddpg, a3c, sac, alphazero, alphago, openai-five, dreamerv3) (R) · D4 (deep-rl-from-human-preferences, instructgpt) · D9 `2106.01345_decision-transformer` · D13 `survey-offline-rl`, `survey-multiagent-rl` | ⭐`sutton-barto` (U–G, THE spine) · `spinning-up` (U, practical) | ⭐`deepmind-rl-2015-silver` (U–G) · `deepmind-rl-2018-hasselt` · `cs234-rl` · `berkeley-cs285-deep-rl` (G) · `cs224r-deep-rl` | `lilianweng-policy-gradient` (✓) · `robotics/` (Tedrake underactuated, for control ties) | `tr/` DeepMind-channel David-Silver lectures + Sutton talks (`richard-sutton-talks`) |
| **LM: the next-token idea (1300)** | ⭐D2 `2005.14165_gpt3` (R) | ⭐`slp3` Ch3 `_013`–`_016` + Ch7 `_047`–`_053` (U) | ⭐`cs336-llm-from-scratch` lec 1 (G) · `cme295-transformers-llms` · `hf-llm-course-ch1` (E) | `information-computation/mackay-itila` `_010`,`_045` (predict⇒compress) (G) | `tr/cognitive-revolution-podcast_004` (Shane Legg, compression test) · `tr/dwarkesh-andrej-karpathy` (15T-tokens compression) |
| **Tokenization (1305)** | — | ⭐`slp3` Ch2 (`_013` head has BPE history) (U) | `cs336` lec 2 · `hf-llm-course-ch1` · `karpathy-nanogpt` (README) | — | `fr/` lab docs (context-window pricing = token economics) |
| **n-gram / classical LM (1308)** | D13 `survey-deep-learning-nlp` | ⭐`slp3` Ch3 `_013`–`_016` (U) | `cs224n-nlp` early lectures | `mackay-itila` `_022` (letter/word predictability) | — |
| **Attention & transformer (1310, 1312, 1315, 1318)** | ⭐D2 (`1706.03762_attention`, `1409.0473_bahdanau-attention`, bert, t5, elmo, gpt3, vit) · D6 (`rope-roformer`, `alibi`) · D1 `word2vec` | ⭐`slp3` Ch8–9 (U) · `prince-udl` (G) | ⭐`cs336` lec 3 · `stanford-cs25-transformers-united` · `cs224n-self-attention-transformers` · `cme295` | ⭐`transformer-and-nn-explainers` (Illustrated Transformer/GPT-2, Annotated Transformer) | `tr/` architect interviews (NVIDIA/IBM channels) |
| **Pretraining at scale (1320, 1322)** | ⭐D3 (kaplan, chinchilla, palm, foundation-models, emergent-abilities, mirage, gpt4-report) (R) | `slp3` Ch7 `_053` · `huyen-aie` | `cs336` (data/systems lectures) | `hardware-compute/`, `economics-data/` (compute+data trends) | `fr/` lab blogs · `tr/dwarkesh-*` lab-CEO eps |
| **In-context & prompting (1325, 1328)** | ⭐D2 `gpt3` · D13 `survey-in-context-learning`, `survey-prompting-methods-nlp` | `slp3` Ch7 (prompting) | `cs336` · `cme295` | — | ⭐`fr/anthropic-docs` + `fr/openai-docs` (prompt/context engineering, principles only — §2.5 filter) |
| **Tuning & alignment-tuning (1330, 1332, 1335)** | ⭐D4 (instructgpt-rlhf, dpo, constitutional-ai, learning-to-summarize) · D3 `flan` · D6 (lora, qlora) · D13 `survey-parameter-efficient-finetuning`, D14 `survey-rlhf` | `slp3` Ch10 · `huyen-aie` | `cs336` · `cs329h-human-feedback` (if held; else CS234) | `governance-safety/` (RLHF critiques) | `tr/axrp-podcast`, `80000-hours-podcast` (alignment-tuning limits debates) |
| **Reasoning & test-time compute (1338)** | ⭐D3 (chain-of-thought, self-consistency, tree-of-thoughts, `2501.12948_deepseek-r1`) · D13 `survey-reasoning-foundation-models` | — | `cs336` (late lectures) | — | `tr/` 2024–26 interviews (o1/R1 era) — tag as snapshots |
| **Hallucination & eval (1342, 1345)** | ⭐D13 (`survey-hallucination-llms`, `-nlg`, `survey-evaluation-of-llms`, `survey-of-llms`) | `huyen-aie` (eval chapters) | `cme295` | — | ⭐`fr/anthropic-engineering` (eval methodology) · `tr/` (jagged-capability debates) |
| **Multimodal / MoE / post-transformer (1348, 1350, 1352)** | ⭐D8 (clip, flamingo, llava, whisper) · D6 (moe-sparsely-gated, switch, mixtral) · D10 (s4, mamba, rwkv, retnet, hyena, jamba) · D13 (`survey-multimodal-llms`, `survey-moe-in-llms`, `survey-state-space-models`) | — | `cs25` guest lectures | — | `tr/` architecture-bet interviews |
| **LLM limits & the understanding debate (1355, 1358)** | D3 `sparks-of-agi` + `emergent-abilities-mirage` · D14 (mech-interp reviews) · D16 `survey-llms-for-agi` | `slp3` Ch7 | — | `cognitive-science/` (Lake; SEP entries) | ⭐`tr/` debates: MLST, Dwarkesh (LeCun-vs-scaling eps), `lex-*` AI guests — the richest debate pool we hold |
| **Applied AI & agentic systems (1360–1399, shelf 25)** | ⭐D9 (rag, dpr, retro, self-rag, react, toolformer, reflexion, voyager, generative-agents, webgpt, gato) · D13 `survey-rag-for-llms`, `survey-llm-agents` | `huyen-aie` · `designing-ml-systems` · `designing-llm-apps` | `hf-llm-course-ch1` | — | ⭐`fr/`: `anthropic-docs`+`anthropic-engineering` · `openai-agents-guide` · `twelve-factor-agents` · `spec-kit` · `mcp-docs` · 26 framework docs (langchain/crewai/autogen/… — **principles only**, HARD_RULES §2.5) · `latent-space-*` |

## §3. Best sources — the 6 to lean on (this domain's spine)
1. **`textbooks/slp3`** (Jurafsky & Martin, Jan-2026 draft, 229 chunks) — the LM/NLP backbone; Ch2 tokens · Ch3 n-grams/perplexity · Ch7 LLMs/pretraining · Ch8–9 transformer · Ch10 post-training.
2. **`textbooks/sutton-barto`** — the RL backbone, start-to-end.
3. **`textbooks/goodfellow-dl` + `textbooks/prince-udl`** — DL theory backbone (Prince = the modern one).
4. **`papers/D1–D14`** — the primary record; every arXiv ID API-verified. Quote the abstract (`_000`) for what a work claims.
5. **`courses/cs336-llm-from-scratch`** (Stanford 2025, 17 lectures) — how the whole LLM pipeline actually fits together, current.
6. **`frontier-rnd/anthropic-docs` + `anthropic-engineering` + `openai-agents-guide` + `twelve-factor-agents`** — the applied/agentic layer (SOTA practice; filter to principles).

## §4. Debates & tensions to render (high value — both sides live in the corpus)
- **Does prediction ⇒ understanding?** stochastic-parrot vs world-models — `tr/` MLST + Dwarkesh + `pD3/sparks-of-agi` vs `pD3/emergent-abilities-mirage`; home: 1358.
- **Is emergence real or a metric artifact?** `pD3/2206.07682` vs `pD3/2304.15004`; home: 1322/1710.
- **Scaling vs new ideas** (LeCun/Sutton/Karpathy positions all in `tr/`); home: 1190/1700/1800.
- **Is the transformer forever?** D10 SSM line vs attention; home: 1352.
- **RLHF: alignment tool or capability polish?** D4 + `tr/axrp`; home: 1335/1910.
- **Agents: reliability vs autonomy** (compounding errors) — `fr/` methodology docs vs demo hype; home: 1365/1375.

## §5. Known thin spots / write-pulls-gather candidates
- **Learning-theory formalism** (PAC, VC) — only `cs229m` + scattered ESL; fine for insight-level, surgical-GET a monograph if 1080 needs rigor.
- **Older classic interviews** (Karpathy/Sutskever/Bengio Lex eps) have no website transcripts — YouTube-caption pull if a debate quote is needed.
- **Berkeley LLM-Agents MOOC** noted as optional residual (handoff §5b) — only if shelf-25 modules hit a wall; current `fr/` docs are already the richest pool.
- `textbooks/` noise folders (`ml`, `la-a-z`, `c1-w1-4`, course fragments) — **do not ground against these**; always prefer the named ⭐/✓ sources above.
