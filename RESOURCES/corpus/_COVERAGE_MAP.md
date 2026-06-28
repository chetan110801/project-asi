# Corpus Coverage Map — the status board
**What's gathered, what's pending.** One row per target source. Update every session ([`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) §7). Targets & URLs: [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md).

`Status: Living board · Created 2026-06-27 (v2.3)`

> **Stages:** ⬜ not-started → 📥 fetched (file saved) → 📄 extracted (→ text) → ✂️ chunked (in `corpus/`) → ✅ used (a module grounded on it).
> **Stream:** ① = extract from owned `local_resources/` · ② = fetch legally-free online.

---

## Tier 1 — core spine (do first)
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Sutton & Barto — RL: An Introduction 2e | `r-sutton-barto` | ① | ✂️ | 143 chunks (556 pp) `textbooks/sutton-barto/` |
| Bishop — Deep Learning 2023 | `r-bishop-dl` | ① | ✂️ | 159 chunks (656 pp) `textbooks/bishop-dl/` |
| Russell & Norvig — AIMA 3e | `r-aima` | ① | ⬜ | owned; extract on demand (49 MB) |
| Huyen — AI Engineering 2025 | `r-huyen-aie` | ① | ✂️ | 85 chunks (1096 pp) `textbooks/huyen-aie/` |
| Christian — The Alignment Problem | `r-christian-alignment` | ① | ✂️ | 20 chunks (EPUB, 29 docs) `textbooks/christian-alignment/` |
| Dive into Deep Learning (d2l) | `r-d2l` | ② | ✂️ | 225 chunks (1151 pp) `textbooks/d2l/` |
| Prince — Understanding Deep Learning | `r-prince-udl` | ① | ✂️ | 129 chunks — **found OWNED in backup** (UnderstandingDeepLearning_11_21_24_C.pdf); the web-fetch deferral is resolved `textbooks/prince-udl/` |
| Nielsen — Neural Networks & DL | `r-nielsen-nndl` | ② | ✂️ | 45 chunks (index+ch1–6, HTML) `textbooks/nielsen-nndl/` (eqns are images — rely on Bishop/d2l for math) |
| Goodfellow — Deep Learning | `r-goodfellow-dl` | ① | ✂️ | 155 chunks — **found OWNED in backup** (Deep Learning Book 2018) `textbooks/goodfellow-dl/` |
| Murphy — Probabilistic ML (1+2) | `r-pml-murphy` | ② | ⬜ | free PDFs — not in backup; fetch if a module needs it |
| Jurafsky & Martin — SLP3 | `r-slp3` | ② | ✂️ | 227 chunks (626 pp, Jan-2026 draft) `textbooks/slp3/` |
| OpenAI — Spinning Up (RL) | `r-spinningup` | ② | ✂️ | 6 chunks (intro + rl_intro 1/2/3) `courses/spinningup/` |
| Stanford CS336 — build an LLM | `r-cs336` | ② | ⬜ | lectures |
| MacKay — ITILA | `r-mackay-itila` | ② | ✂️ | **201 chunks** (11.6 MB free PDF) `information-computation/mackay-itila/` (session 2) |
| **Spine papers (D1–D5): 10** | — | ② | ✂️ | **all 8 arXiv IDs verified vs API 2026-06-27 (all correct)** → see papers table below |

### Spine papers — fetched + chunked this session (`corpus/papers/`)
| Paper | arXiv / source | Area folder | Chunks |
|---|---|---|---|
| Krizhevsky et al. — AlexNet (2012) | NeurIPS (no arXiv) | `D1-deep-learning/alexnet` | 3 |
| He et al. — ResNet (2015) | 1512.03385 ✓ | `D1-deep-learning/1512.03385_resnet` | 10 |
| Vaswani et al. — Attention Is All You Need (2017) | 1706.03762 ✓ | `D2-transformers/1706.03762_attention` | 5 |
| Brown et al. — GPT-3 (2020) | 2005.14165 ✓ | `D2-transformers/2005.14165_gpt3` | 24 |
| Kaplan et al. — Scaling Laws (2020) | 2001.08361 ✓ | `D3-scaling/2001.08361_kaplan-scaling-laws` | 10 |
| Hoffmann et al. — Chinchilla (2022) | 2203.15556 ✓ | `D3-scaling/2203.15556_chinchilla` | 11 |
| Ouyang et al. — InstructGPT/RLHF (2022) | 2203.02155 ✓ | `D4-alignment/2203.02155_instructgpt-rlhf` | 18 |
| Mnih et al. — DQN / Atari (2013) | 1312.5602 ✓ | `D5-rl/1312.5602_dqn-atari` | 4 |
| Schulman et al. — PPO (2017) | 1707.06347 ✓ | `D5-rl/1707.06347_ppo` | 4 |
| Silver et al. — AlphaGo (2016) | Nature (free DeepMind copy) | `D5-rl/alphago` | 10 |

## Tier 2 — applied & embodied
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Siciliano — Foundations of Robotics 2025 | `r-siciliano-robotics` | ① | ⬜ | owned |
| Tedrake — Underactuated Robotics | — | ② | ✂️ | **51 chunks** (20 chapters) `robotics/tedrake-underactuated-robotics/` (session 2) |
| Lynch & Park — Modern Robotics | — | ② | ✂️ | **94 chunks** (free PDF) `robotics/lynch-park-modern-robotics/` (session 2) |
| LaValle — Planning Algorithms | — | ② | ✂️ | **233 chunks** (free PDF) `robotics/lavalle-planning-algorithms/` (session 2) |
| Raieli — AI Agents w/ LLMs, RAG | `r-raieli-agents` | ① | ⬜ | owned |
| Kawahara — HW Technologies for AI | `r-kawahara-hw` | ① | ⬜ | owned (compute) |
| HF courses (LLM/NLP/RL/Agents) | `r-hf-courses` | ② | ⬜ | HTML |
| CS231n / CS224n / CS285 notes | `r-cs231n`,`r-cs224n`,`r-berkeley-cs285` | ② | ⬜ | notes/slides |
| **Papers D5–D9** (RL/agents, systems, diffusion, multimodal, RAG) | — | ② | ⬜ | from PAPERS.md |

## Tier 3 — AI-for-science & intersected frontiers
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Gerstner — Neuronal Dynamics | `r-neuronal-dynamics` | ② | ✂️ | **104 chunks** (133 pages, EPFL HTML) `neuroscience/gerstner-neuronal-dynamics/` (session 2) |
| Hawkins — A Thousand Brains | `r-hawkins-1000brains` | ① | ⬜ | owned EPUB |
| AlphaFold — EBI guide + preprints | `r-alphafold-ebi` | ② | ✂️ | AlphaFold2 (Jumper 2021) **9 chunks** `biology/jumper-2021-alphafold2-nature/` (session 2; EBI course pending) |
| Preskill Ph229 / Quantum Country / Qiskit | `r-preskill-ph229`,`r-quantum-country` | ② | ✂️ | Quantum Country **19** + Watrous TQI **88** + Biamonte QML **5** `quantum/` (session 2; Preskill notes moved—pending) |
| GraphCast / GNoME / tokamak / AlphaGeometry | — | ② | ⬜ | lab blogs + arXiv |
| Shakarian — Metacognitive AI | `r-shakarian-metacog` | ① | ⬜ | owned |
| **Papers D10–D12** (post-transformer, robotics, AI-for-science) | — | ② | ⬜ | from PAPERS.md |

## Tier 4 — world & society
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Epoch AI — compute/data trend reports | — | ② | ✂️ | Sevilla compute-trends **8** `hardware-compute/` + Villalobos run-out-of-data **11** `economics-data/` (session 2; more Epoch pages pending) |
| Stanford HAI — AI Index (annual) | — | ② | ⬜ | free PDF |
| Lab Responsible-Scaling / Preparedness frameworks | — | ② | ⬜ | free |
| Togelius — AGI 2024 | `r-togelius-agi` | ① | ⬜ | owned (paths) |
| Tegmark — Life 3.0 | `r-tegmark-life3` | ① | ⬜ | owned |
| Bostrom — Superintelligence / Russell — Human Compatible | `r-bostrom-superint`,`r-russell-hc` | — | ⬜ | BUY/own — REQUESTS.md |

---

---

## Full owned-library extraction — the whole backup (2026-06-27, session 1)
The learner directed: **pull in *all* offline resources from the full backup** (`Downloads/Learning_Resources/New folder (2)`, 12 GB / 3,507 files). Done — every real **document** (book/paper/course-notes PDF + EPUB) is now extracted to verbatim, greppable, ~14 KB chunks.

| Result | Count |
|---|---|
| **Sources extracted** (book/paper/notes) | **373** (362 textbook-folders + 10 spine papers + 1 course) |
| **Verbatim chunk files** | **17,234** |
| **Corpus size on disk** | **258 MB** (git-ignored) |
| Catalog of every extracted source | `textbooks/_LIBRARY_INDEX.txt` (title · pages · chunks · slug) |

**What was deliberately NOT pulled in** (so the greppable understanding-substrate stays clean):
- **Code repos** — 1,235 `.py` + 192 `.ipynb` (coding is delegated per [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §5.2; they stay safe in the backup). *Reverse on request.*
- **130 junk/admin files** excluded by path — macOS resource forks, Python cheat-sheet image bundles, Python official-docs API ref, GCP-cert logistics decks.
- **26 dedup'd** (already extracted under cleaner spine slugs).
- **3 image-only scans, no text layer → need OCR later:** `Everything You Need To Know About AI 2023`, `Kandel — Nobel Lecture (2000)`, `TIME Special Edition — AI 2025`. *(Logged; optional OCR pass.)*

> The corpus now spans far beyond the AI spine: neuroscience (full **Kandel** set incl. *Principles of Neural Science 6e*), math (ESL, Deisenroth MML, Boyd convex-opt, Bertsekas probability, Strang calculus), DL/ML (Goodfellow, Bishop PRML+DL, Prince UDL, d2l, Géron, Raschka), LLMs/agents (Huyen, Raieli, hands-on-LLMs), robotics (Siciliano), compute (Kawahara), AGI/society (Togelius, Tegmark, Bostrom-adjacent), evolution/culture (Sapiens, Bennett), + ~300 broader AI-domain volumes and course-note sets. Processing order is still governed by leverage × AGI/ASI-relevance ([`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §1.4) — **collected ≠ processed**; a domain counts as "covered" only once it has produced grounded modules.

---

## Online mass-collection campaign — session 2 (2026-06-28), all-domain web sweep
Per the learner override (keep mass-collecting online across all domains × many authors × all media, *before* writing modules). Worked [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) §③ top-to-bottom: HEAD-checked each URL live, skipped what the owned backup already holds, verified every arXiv ID vs the API. All legally-free (author-hosted / open-licensed / arXiv / gov / course-public). Text git-ignored; one folder per source under `corpus/<domain>/<slug>/` with `_SOURCE.txt`.

| Domain (folder) | Source | Type | Chunks |
|---|---|---|---|
| `neuroscience/` | Gerstner et al. — **Neuronal Dynamics** (EPFL, 133 pp) | 📘 | 104 |
| `neuroscience/` | O'Reilly et al. — **Computational Cognitive Neuroscience** ed5 (open PDF) | 📘 | 43 |
| `neuroscience/` | Huang & Rao — **Predictive Coding** review 2011 (author-hosted) | 📄 | 6 |
| `neuroscience/` | Friston — FEP "rough guide" / "Free-energy & the brain" / "Predictive coding under FEP" (UCL author-hosted) | 📄×3 | 21 |
| `cognitive-science/` | Goodman, Tenenbaum et al. — **Probabilistic Models of Cognition** (probmods, 16 ch) | 📘 | 35 |
| `cognitive-science/` | **Stanford Encyclopedia of Philosophy** — 9 entries (computational-mind, mental-representation, connectionism, …) | ✍️ | 81 |
| `cognitive-science/` | Lake, Ullman, Tenenbaum, Gershman — **Machines That Learn & Think Like People** (1604.00289 ✓) | 📄 | 15 |
| `math-theory/` | Boaz Barak — **Introduction to Theoretical CS** (introtcs, free PDF) | 📘 | 119 |
| `math-theory/` | Arora & Barak — **Computational Complexity** (Princeton free draft) | 📘 | 96 |
| `math-theory/` | James et al. — **Intro to Statistical Learning** (ISLR2, free PDF) | 📘 | 112 |
| `information-computation/` | MacKay — **Information Theory, Inference & Learning** (free PDF) | 📘 | 201 |
| `information-computation/` | Shannon 1948 — **A Mathematical Theory of Communication** | 📄 | 15 |
| `information-computation/` | Aaronson — **Quantum Computing Since Democritus** (21 lectures) | 📝 | 44 |
| `hardware-compute/` | Sze et al. — **Efficient Processing of DNNs** survey (1703.09039 ✓) | 📄 | 20 |
| `hardware-compute/` | Sevilla et al. (Epoch) — **Compute Trends Across Three Eras** (2202.05924 ✓) | 📄 | 8 |
| `energy/` | MacKay — **Sustainable Energy Without the Hot Air** (full book) | 📘 | 98 |
| `energy/` | **Our World in Data** — Energy (4 articles) | ✍️ | 4 |
| `quantum/` | Watrous — **Theory of Quantum Information** (free PDF) | 📘 | 88 |
| `quantum/` | Nielsen & Matuschak — **Quantum Country** (QCVC + search + teleportation) | 📝 | 19 |
| `quantum/` | Biamonte et al. — **Quantum Machine Learning** (1611.09347 ✓) | 📄 | 5 |
| `physics/` | David Tong — **Statistical Physics** lecture notes | 📝 | 30 |
| `physics/` | **Feynman Lectures** — 8 selected conceptual chapters (atoms, energy, thermo, symmetry, least action) | 📘 | 22 |
| `robotics/` | Lynch & Park — **Modern Robotics** (free PDF) | 📘 | 94 |
| `robotics/` | LaValle — **Planning Algorithms** (free PDF) | 📘 | 233 |
| `robotics/` | Tedrake — **Underactuated Robotics** (MIT, 20 ch) | 📘 | 51 |
| `biology/` | **OpenStax Biology 2e** (full text) | 📘 | 318 |
| `biology/` | Jumper et al. — **AlphaFold2** (Nature 2021, EuropePMC OA) | 📄 | 9 |
| `materials/` | Zeni et al. — **MatterGen** (2312.03687 ✓) | 📄 | 12 |
| `materials/` | Chanussot et al. — **Open Catalyst 2020** (2010.09990 ✓) | 📄 | 10 |
| `complex-systems/` | Newman — **Structure & Function of Complex Networks** (cond-mat/0303516 ✓) | 📄 | 29 |
| `complex-systems/` | Clauset, Shalizi, Newman — **Power-law Distributions in Empirical Data** (0706.1062 ✓) | 📄 | 11 |
| `economics-data/` | Villalobos et al. (Epoch) — **Will We Run Out of Data?** (2211.04325 ✓) | 📄 | 11 |

**Checkpoint subtotal (committed a8757bb): 34 sources · 1,964 chunks · 13 domains.**

### Session-2 continued — remaining §③ domains + the PAPERS.md sweep
| Domain (folder) | Source | Type | Chunks |
|---|---|---|---|
| `blockchain-web3/` | Antonopoulos — **Mastering Bitcoin** (open-licensed, ch01–14 asciidoc) | 📘 | 61 |
| `blockchain-web3/` | Nakamoto — **Bitcoin whitepaper** | 📄 | 2 |
| `blockchain-web3/` | **Ethereum whitepaper** + Vitalik essays (PoS, sharding) | 📄✍️ | 9 |
| `economics-data/` | Acemoglu — **The Simple Macroeconomics of AI** (MIT free) | 📄 | 10 |
| `economics-data/` | **Our World in Data** — AI overview | ✍️ | 2 |
| `governance-safety/` | Amodei et al. — **Concrete Problems in AI Safety** (1606.06565 ✓) | 📄 | 9 |
| `governance-safety/` | Hubinger et al. — **Sleeper Agents** (2401.05566 ✓) | 📄 | 22 |
| `governance-safety/` | Anthropic **transformer-circuits** — Toy Models / Framework / Monosemanticity | 📄 | 33 |
| `governance-safety/` | **80,000 Hours** AI problem profile + aisafety.info | ✍️ | 6 |
| `ai-ml-foundations/` | Murphy — **Probabilistic ML: An Introduction** (book1, free PDF) | 📘 | 180 |
| `ai-ml-foundations/` | **ML blogs/essays** — Bitter Lesson + colah×3 + Lil'Log×3 | ✍️ | 13 |
| `ai-ml-foundations/` | Stanford **CS231n** notes (10 conceptual pages) | 📝 | 21 |
| `papers/D1–D12/` | **115 landmark→SOTA papers** — every arXiv ID verified vs API, fetched + chunked (D1 word2vec/VAE/GAN/VGG/U-Net…, D2 BERT/T5/ViT, D3 CoT/emergence/GPT-4/DeepSeek-R1, D4 DPO/Constitutional/Debate, D5 TRPO/SAC/AlphaZero, D6 MoE/FlashAttn/LoRA/LLaMA, D7 all diffusion, D8 CLIP/Flamingo/Whisper, D9 RAG/ReAct/Toolformer/Voyager, D10 Mamba/S4/RWKV, D11 RT-1/2/SayCan/π0, D12 GraphCast/Codex/Med-PaLM/Petals) | 📄 | ~1,116 |

**Session-2 GRAND TOTAL: 161 new sources · ~3,448 verbatim chunks** (46 domain sources across 16 domain folders + 115 verified papers). **124 arXiv IDs verified vs API this session, 0 mismatches** (9 domain papers + 115 landmark papers). All legally-free; text git-ignored (.gitignore broadened to cover every corpus subfolder). Remaining ⬜ (no clean arXiv — fetch free copies later if a module needs them): Nature/Science-only AI-for-science papers (AlphaFold3, GNoME, AlphaTensor, AlphaGeometry, tokamak, GenCast, AlphaQubit, RFdiffusion, astronomy set — list in PAPERS.md), Preskill quantum notes (site moved), CS336/CS224n course sites, AI Index annual PDF, EBI AlphaFold course.

---

**Totals (after gathering session 1, 2026-06-27):** 0 used · **373 sources chunked = 17,234 verbatim chunk files, 258 MB** · 8/8 spine arXiv IDs verified · whole owned library extracted.

**Totals (after gathering session 2, 2026-06-28):** **534 sources** (373 + 161 new) · **~20,680 verbatim chunk files** (17,234 + ~3,448 new) · **132 arXiv IDs verified vs API total (0 mismatches)** · corpus now spans 16 fresh online domain folders (neuroscience, cognitive-science, math-theory, information-computation, hardware-compute, energy, quantum, physics, robotics, biology, materials, complex-systems, blockchain-web3, economics-data, governance-safety, ai-ml-foundations) **+ the full PAPERS.md D1–D12 landmark set (125 paper folders)**. All text git-ignored. **Next:** more mass-collection can continue (Nature-only AI-for-science free copies, transcripts of debates/podcasts/YouTube per HARD_RULES §2 media rule, more authors per domain) **or** — once the learner calls the corpus rich enough — the first **grounded module rewrite** (1300 LLMs) as proof-of-standard before redoing 1000–1200. Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).
