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
| Stanford CS336 — build an LLM | `r-cs336` | ② | ✂️ | **17 lecture transcripts** (2025) `courses/cs336-llm-from-scratch/` (session 4); CS336 main notes still ⬜ |
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
| AlphaFold — EBI guide + preprints | `r-alphafold-ebi` | ② | ✂️ | AlphaFold2 (Jumper 2021) **9 chunks** `biology/jumper-2021-alphafold2-nature/` (session 2) **+ EBI practical-guide course 9 chunks** `biology/ebi-alphafold-course/` (session 4, AF2/AF3/AlphaMissense, CC BY 4.0) |
| Preskill Ph229 / Quantum Country / Qiskit | `r-preskill-ph229`,`r-quantum-country` | ② | ✂️ | Quantum Country **19** + Watrous TQI **88** + Biamonte QML **5** `quantum/` (session 2; Preskill notes moved—pending) |
| GraphCast / GNoME / tokamak / AlphaGeometry | — | ② | ⬜ | lab blogs + arXiv |
| Shakarian — Metacognitive AI | `r-shakarian-metacog` | ① | ⬜ | owned |
| **Papers D10–D12** (post-transformer, robotics, AI-for-science) | — | ② | ⬜ | from PAPERS.md |

## Tier 4 — world & society
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Epoch AI — compute/data trend reports | — | ② | ✂️ | Sevilla compute-trends **8** `hardware-compute/` + Villalobos run-out-of-data **11** `economics-data/` (session 2; more Epoch pages pending) |
| Stanford HAI — AI Index (annual) | — | ② | ✂️ | **AI Index 2025 (full, 457 pp) 111 chunks** `economics-data/ai-index-2025/` (session 4) |
| Gov/lab safety frameworks | — | ② | ✂️ | session 5: NIST AI RMF 1.0 `9` + GenAI Profile `14`, OpenAI Preparedness v2 `6`, **Intl AI Safety Report 2025 (Bengio) `87`**, Anthropic RSP `1`, Bletchley `1` → `governance-safety/` |
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
| `ai-ml-foundations/` | Murphy — **Probabilistic ML: Advanced Topics** (book2, free PDF) | 📘 | 351 |
| `ai-ml-foundations/` | **Transformer/NN explainers** — Illustrated Transformer + GPT-2 (Alammar), Annotated Transformer (Harvard), Karpathy (RNNs, training recipe) | ✍️ | 13 |
| `papers/D1–D12/` | **115 landmark→SOTA papers** — every arXiv ID verified vs API, fetched + chunked (D1 word2vec/VAE/GAN/VGG/U-Net…, D2 BERT/T5/ViT, D3 CoT/emergence/GPT-4/DeepSeek-R1, D4 DPO/Constitutional/Debate, D5 TRPO/SAC/AlphaZero, D6 MoE/FlashAttn/LoRA/LLaMA, D7 all diffusion, D8 CLIP/Flamingo/Whisper, D9 RAG/ReAct/Toolformer/Voyager, D10 Mamba/S4/RWKV, D11 RT-1/2/SayCan/π0, D12 GraphCast/Codex/Med-PaLM/Petals) | 📄 | ~1,116 |

**Session-2 GRAND TOTAL: 163 new sources · ~3,812 verbatim chunks** (48 domain sources across 16 domain folders + 115 verified papers). **124 arXiv IDs verified vs API this session, 0 mismatches** (9 domain papers + 115 landmark papers). All legally-free; text git-ignored (.gitignore broadened to cover every corpus subfolder). Remaining ⬜ (no clean arXiv — fetch free copies later if a module needs them): Nature/Science-only AI-for-science papers (AlphaFold3, GNoME, AlphaTensor, AlphaGeometry, tokamak, GenCast, AlphaQubit, RFdiffusion, astronomy set — list in PAPERS.md), Preskill quantum notes (site moved), CS336/CS224n course sites, AI Index annual PDF, EBI AlphaFold course.

---

## Online mass-collection campaign — session 3 (2026-06-28): §③.R punch-list + transcripts + courses
Worked [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) §③.R. Same rules (HEAD-check live · skip owned · verify arXiv IDs vs API · legality absolute · text git-ignored · durability filter). New extractors this session: `epmcpdf.sh` (EuropePMC OA PDF via `getPdf?pmcid=`), `getblog.sh` (lab-blog HTML), `getts.sh` (HTML transcript), `ytchannel.sh`+`vtt2txt.pl` (YouTube auto-subs → de-duped text). `html2txt.pl` upgraded to normalize UTF-8 smart punctuation → ASCII (clean verbatim grep).

### R1 — AI-for-science papers (Nature/Science-only → free copies). **26 sources; 9 new arXiv IDs verified vs API, 0 mismatches.**
| Folder | Source | Free route | Type |
|---|---|---|---|
| `papers/D12-ai-for-science/` | NeuralGCM (2311.07222) · GenCast (2312.15796) · Genie world-models (2402.15391) · TabPFN (2207.01848) | arXiv ✓ | 📄×4 |
| `astronomy/` (new) | George-Huerta grav-waves (1701.00008) · Shallue-Vanderburg exoplanets (1712.05044) · Dieleman galaxy-morphology (1503.07077) · EHT PRIMO M87 (2304.06079) | arXiv ✓ | 📄×4 |
| `hardware-compute/` | AlphaChip predecessor — Chip Placement w/ Deep RL (2004.10746) | arXiv ✓ | 📄 |
| `biology/` | AlphaFold3 (Abramson 2024, EuropePMC PMC11168924 OA) · RoseTTAFold (Baek 2021, PMC7612213 OA) · ESMFold/ESM-2 (Lin 2023, bioRxiv) · Evo (Nguyen 2024, bioRxiv) · RFdiffusion (Watson 2023, bioRxiv) | EuropePMC/bioRxiv | 📄×5 |
| `neuroscience/` | Willett speech-neuroprosthesis (2023, PMC10468393 OA) · Tang semantic-decoding (2023, bioRxiv) · Takagi-Nishimoto image-reconstruction (2023, bioRxiv) | EuropePMC/bioRxiv | 📄×3 |
| `math-theory/` | AlphaTensor · AlphaDev · FunSearch · AlphaGeometry · AlphaProof-IMO2024 | DeepMind blog (Nature-only) | ✍️×5 |
| `materials/` `physics/` `quantum/` `biology/` | GNoME · tokamak plasma-control · AlphaQubit · AlphaMissense | DeepMind/Google blog | ✍️×4 |
> Skipped (paywalled, concept already covered): Coscientist (≈ ChemCrow, owned) · AlphaMissense paper (blog kept) · "Scientific Discovery in the Age of AI" review (not OA).

### R2 — debate/podcast/lecture transcripts (HARD_RULES §2 "gold") → `transcripts/`
| Source | Detail | Count |
|---|---|---|
| **Lex Fridman** (`lex-*`) | Hassabis, LeCun, Amodei, Jensen Huang, Yampolskiy, Altman, Srinivas — strong expert *disagreement* | 7 |
| **Dwarkesh Patel** (`dwarkesh-*`) — **ALL of it** (learner request) | full sitemap swept (172 posts); 135 transcripts/essays captured, 37 thin (paywalled/preview) skipped | 135 |
| **DeepMind YouTube** (`deepmind-youtube/`) — whole channel (learner request) | 365 videos → **212 transcripts** (151 no-speech promo clips auto-skipped), 7.9 MB. **Bonus:** the channel hosts full COURSES — David Silver's RL course (10 lectures), DeepMind×UCL RL Lecture Series (13), and the Deep Learning lecture series — all captured (overlaps R5). | ✅ **212 done** |
| **Two Minute Papers** (`two-minute-papers/`) — whole channel (learner request) | 1066 videos → **639 transcripts** (355 short/no-caption skipped), 4.9 MB | ✅ **639 done** |

### R3 — courses/notes → `courses/`
| Source | Chunks |
|---|---|
| Stanford **CS229** main notes (full PDF) | 30 |
| Stanford **CS224N** self-attention & transformers notes | 4 |
| **HuggingFace LLM course** ch.1 (transformer foundations) | 7 |
| **Karpathy nanoGPT** README | 1 |
> **University course playlists** (Stanford/MIT/DeepMind-UCL/NYU/Caltech, ~50 full courses) **scanned + catalogued** → [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md). **Collection deferred to next session** (learner: "we can do this in a new session").

**Session-3 totals — ALL DONE:** **R1** 26 AI-for-science free copies · **R2** **993 transcripts (27 MB)** = Lex 7 + Dwarkesh 135 + DeepMind-YouTube **212** (incl. full David-Silver-RL / UCL-DL&RL courses) + Two-Minute-Papers **639** · **R3** 4 course sources (CS229/CS224N/HF-ch1/nanoGPT) + ~50 university playlists catalogued ([`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md), collection = next session). All text git-ignored. **Next session:** R5 university course playlists, then R4 anchors.

---

## Online mass-collection campaign — session 4 (2026-06-28): R5 university course playlists + R4 anchors
Worked [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md) (R5, spine-first then widen tier-1) + the R4 anchor punch-list. Rebuilt the YouTube tooling in scratchpad (`ytchannel.sh` + `vtt2txt.pl`, resumable; `html2txt.pl`/`chunk.sh`/`norm.pl`/`fetch_html.sh` for the web anchors — `html2txt.pl` now decodes UTF-8 before ASCII-normalizing smart punctuation). Same rules: HEAD-check live · skip owned · legality absolute · text git-ignored · durability filter (lectures = grounded intuition; ground hard facts to a primary source). Managed background queue, polite pacing, 429-backoff + recovery pass.

### R5 — UNIVERSITY COURSE LECTURE TRANSCRIPTS → `corpus/courses/` (**24 courses · 398 transcripts · 27 MB**)
| Group | Courses | Transcripts |
|---|---|---|
| **Stanford spine** | CS229 ML (22) `19` · CS230 DL `9` · CS231N CV `18` · CS224N NLP `23` · CS234 RL `16` · CS336 LLM-from-scratch `17` · CME295 Transformers&LLMs `9` | **111** |
| **DeepMind×UCL** (reused from session-3 channel pull; 0 re-downloads, re-foldered in lecture order) | Intro-to-RL-2015 (Silver) `10` · RL-2018 (Hasselt) `10` · DL-2021 `13` · DL-2020 `12` | **45** |
| **MIT OCW** | 6.7960 Deep Learning (F24) `24` · 9.13 The Human Brain `17` · 9.40 Neural Computation `20` | **61** |
| **Widen tier-1** | CS224R Deep-RL `19` · CS236 Deep-Generative-Models `18` · CS330 Meta-Learning `17` · CS329H ML-from-Human-Preferences `8` · CME296 Diffusion&Vision `8` · CS224W ML-Graphs `22` · NYU-DL-FL22 (LeCun) `8` · Caltech CS156 Learning-From-Data (Abu-Mostafa) `16` · MIT RES.9-003 Brains-Minds-Machines `60` · ECON295/CS323 AI-Awakening (Brynjolfsson) `5` | **181** |
> No-caption short clips auto-skipped (`.done` markers): CS224W 25, CS156 2. A 429-storm hit the two 47-video playlists; clearing markers + a slower re-run recovered the rate-limited videos (CS224W +3). Remaining long-tail playlists (CS221/CS224U/CS229M/CS109/EE364A/EE274/CS149/AA228V; MIT 18.065/18.S096/18.404J/6.006/8.04/7.91J/9.35/16.412J/RES.6-012/6.S897; NYU SP21/SP20/AI-SP24; +Berkeley/CMU/3B1B/fast.ai) catalogued in [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md).

### R4 — anchors (PDF + HTML, verbatim, ASCII-normalized) → various domains (**16 sources · 221 chunks**)
| Domain (folder) | Source | Type | Chunks |
|---|---|---|---|
| `economics-data/` | **Stanford HAI — AI Index Report 2025** (full, 457 pp PDF) | 📘 | 111 |
| `biology/` | **EMBL-EBI — AlphaFold: a practical guide** (online course, CC BY 4.0; 23 conceptual pages, AF2/AF3/AlphaMissense) | 📚 | 9 |
| `ai-ml-foundations/` | **Distill** — Why Momentum Really Works `6` · Visual Exploration of Gaussian Processes `3` · Attention & Augmented RNNs `3` · Gentle Intro to GNNs `5` | ✍️ | 17 |
| `governance-safety/` | **Distill** — Feature Visualization `3` · Building Blocks of Interpretability `4` | ✍️ | 7 |
| `complex-systems/` | **Distill** — Growing Neural Cellular Automata | ✍️ | 4 |
| `cognitive-science/` | **SEP** — The Turing Test `10` · The Chinese Room `12` | ✍️ | 22 |
| `governance-safety/` | **SEP** — Ethics of AI & Robotics | ✍️ | 13 |
| `information-computation/` | **SEP** — Semantic Conceptions of Information | ✍️ | 6 |
| `math-theory/` | **SEP** — Bayesian Epistemology `14` · Causal Models `9` | ✍️ | 23 |
| `complex-systems/` | **SEP** — Emergent Properties | ✍️ | 9 |

**Session-4 GRAND TOTAL: 40 new sources · 619 items** (24 courses / 398 transcripts + 16 anchors / 221 chunks). All legally-free (course-public YouTube auto-subs · Stanford-hosted PDF · EBI CC BY 4.0 · Distill CC-BY · SEP). All text git-ignored. **Next session:** widen to the remaining long-tail course playlists (managed queue) + finish R4 long tail (more authors/domains) — **or**, if the learner calls the corpus rich enough, the first grounded module rewrite (1300 LLMs).

---

## Online mass-collection campaign — session 5 (2026-06-28): FULL course long-tail + To-ADD channels + R4 long-tail anchors
Worked [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md) (all remaining catalogued long-tail) + the previously-unscanned "To-ADD" channels + the R4 governance/interpretability anchor gaps. Driver hardened mid-session (manual subs + `en`/`en-orig`/`en-en`; 429-on-retry leaves video unmarked for re-run). All catalogued + To-ADD playlist IDs validated live. Same rules: HEAD-check live · skip owned/overlaps · verify arXiv IDs vs API · legality absolute · text git-ignored · durability filter.

### R5b — COURSE LONG-TAIL + TO-ADD → `corpus/courses/` (**33 courses · 1,165 transcripts**; course corpus now **62 folders · 1,617 transcripts · 68 MB**)
| Group | Courses | Transcripts |
|---|---|---|
| **Stanford long-tail** | CS221 AI `20` · CS224U NLU `50` · CS229M ML-Theory `20` · CS109 Probability `29` · EE364A Convex-Opt `18` · EE274 Data-Compression `18` · CS149 Parallel-Computing `19` · AA228V Safety-Critical `17` | **191** |
| **NYU** | DL-SP21 (LeCun) `31` · AI-SP24 `9` · **DL-SP20 `0` (GAP — auto-only captions PO-token-gated; superseded by SP21)** | **40** |
| **MIT long-tail** | 9.35 Perception `23` · 18.065 Matrix-Methods `36` · 18.S096 Matrix-Calculus `17` · 18.404J Theory-of-Computation `25` · 6.006 Algorithms `32` · 6.S897 ML-Healthcare `25` · 7.91J Comp-Systems-Bio `22` · 16.412J Cognitive-Robotics `7` · 6.042J Math-for-CS `98` · 8.04 Quantum-I `97` · RES.6-012 Probability `98` | **480** |
| **To-ADD channels** (newly scanned) | Berkeley CS285 Deep-RL `99` · Berkeley CS182 DL `66` · CMU 11-785 Intro-DL `28` · CMU 11-711 Adv-NLP `23` · Stanford CS25 Transformers-United `50` · MIT 6.034 AI (Winston) `30` · MIT 18.06 LinAlg (Strang) `36` · 3B1B Essence-of-LinAlg `16` · 3B1B Neural-Networks `9` · fast.ai 2022 `8` · MIT 6.S191 Intro-DL `89` | **454** |
> Segment-style MIT playlists (6.042J/8.04/RES.6-012) are flat-list-capped at ~100 by this yt-dlp build — bulk captured. Skipped: CMU 11-785 S20 (overlap), Stanford CS324 (no lecture playlist).

### R4b — anchors (governance/safety frameworks + interpretability/RL/diffusion) → various (**11 sources · 139 chunks**)
| Domain (folder) | Source | Type | Chunks |
|---|---|---|---|
| `governance-safety/` | **International AI Safety Report 2025** (Bengio + 100 experts, arXiv 2501.17805 ✓) | 📘 | 87 |
| `governance-safety/` | **NIST AI RMF 1.0** (AI 100-1) `9` + **NIST GenAI Profile** (AI 600-1) `14` | 📘 | 23 |
| `governance-safety/` | **OpenAI Preparedness Framework v2** (2025) | 📄 | 6 |
| `governance-safety/` | **Anthropic Responsible Scaling Policy** (announce) `1` + **Bletchley Declaration** 2023 `1` | ✍️ | 2 |
| `governance-safety/` | **Distill** — Zoom-In: Circuits `5` + Multimodal Neurons `1` (CC BY) | ✍️ | 6 |
| `governance-safety/` | **Lil'Log** — Reward Hacking in RL (2024) | ✍️ | 4 |
| `ai-ml-foundations/` | **Lil'Log** — Policy Gradient Algorithms `6` + What are Diffusion Models? `5` | ✍️ | 11 |
> GraphCast (2212.12794) was already present from a prior session (no dup). All legally-free (NIST/gov public · arXiv · Anthropic/OpenAI public docs · Distill CC-BY · author blog).

**Session-5 GRAND TOTAL: 44 new sources · 1,304 items** (33 courses / 1,165 transcripts + 11 anchors / 139 chunks). The catalogued university long-tail + To-ADD channels are now **effectively complete**. All text git-ignored. **Next session:** optional residual channels (Harvard CS50-AI, 3B1B Calculus, NYU-SP20 if a JS-runtime/impersonation setup is added) — **or**, if the learner calls the corpus rich enough, the first **grounded module rewrite** (1300 LLMs).

---

## Online mass-collection campaign — session 6 (2026-06-29): ALL-DOMAIN × MANY-UNIVERSITIES course widening
Worked the session-6 prompt: widen course coverage past the AI/ML spine into **every under-served domain × many more universities**. Rebuilt the proven toolchain in scratchpad (`ytchannel.sh`+`vtt2txt.pl`+`runbatch.sh`, session-5 hardenings intact). Scanned candidate channels' `/playlists` live, **validated every playlist ID (count + first title) before queueing**, skipped dup editions + a generic Stanford mixed playlist that re-served the owned AA228V. Ran **3 managed queues, one at a time**, base sleep 2.6 s — no 429 storms. Same rules: HEAD/validate live · skip owned · legality absolute (course-public auto-subs / CC-licensed OCW) · text git-ignored · durability filter (full lectures + grounded-intuition channels).

### R5c — COURSE WIDENING → `corpus/courses/` (**31 courses · 1,050 transcripts**; course corpus now **93 folders · 2,667 transcripts · 99 MB**)
| Group | Courses | Transcripts |
|---|---|---|
| **Core university full-lectures (Q1)** | Harvard STAT110 Probability (Blitzstein) `35` · Berkeley CS188 AI `21` · UMich EECS498 Deep-Learning-for-CV (Johnson) `22` · CMU 10-708 PGM `29` · CMU 11-747 Neural-Nets-for-NLP `25` · MIT 6.041 Probabilistic-Systems (Tsitsiklis) `76` · MIT 6.832 Underactuated-Robotics (Tedrake) `23` · MIT 7.016 Biology `35` · MIT 9.14 Brain-Structure `35` · MIT 14.01 Microeconomics `26` · MIT 14.02 Macroeconomics `25` · MIT 2.003SC Engineering-Dynamics `38` · MIT 18.02 Multivariable-Calculus `35` · MIT 24.08J Philosophy-of-Brain-Science `5` | **430** |
| **Expert intuition channels + physics/quantum (Q2)** | 3B1B Essence-of-Calculus `11` · 3B1B Differential-Equations `8` · Brunton Control-Bootcamp `36` · Brunton Physics-Informed-ML `23` · Brunton Data-Driven-Dynamical-Systems `24` · Brunton DiffEq-&-Dynamical-Systems `49` · Brunton SVD `43` · Kirsanov Neuroscience `26` · Kirsanov AI-&-ML `9` · MIT 8.05 Quantum-II `24` · MIT 8.03 Vibrations-&-Waves `33` · MIT 8.06 Quantum-III `100` · MIT 8.01 Classical-Mechanics `95` | **481** |
| **Additional universities (Q3)** | Cornell CS4780 ML (Weinberger) `41` · Tübingen Deep-Learning (Geiger) `46` | **87** |
| **Efficient-ML domain + flagship AI intro (Q4)** | MIT 6.5940 TinyML & Efficient-DL (HAN Lab) `45` · Harvard CS50 Intro-to-AI-with-Python `7` | **52** |
> **New domains reached this session:** probability/statistics (Stat110, 6.041), quantum (8.05/8.06), physics (8.01/8.03), economics (14.01/14.02), biology (7.016), robotics/control (6.832, 2.003SC, Brunton control/dynamics), neuroscience (9.14, Kirsanov), cognitive-science (24.08J), applied-math/calculus (18.02, 3B1B, Brunton SVD/DiffEq), PGM (10-708), **efficient-ML/TinyML (6.5940)**. **+4 universities** (Harvard, UMich, Cornell, Tübingen) + 2 expert channels (Brunton, Kirsanov) + MIT HAN-Lab. Benign empties only (Berkeley CS188 NA/private placeholders; 8.06/8.01 flat-list-capped at ~100; scattered caption-less clips). Playlist-ID table: [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md) §session-6.

**Session-6 GRAND TOTAL: 31 new courses · 1,050 lecture transcripts.** `corpus/courses/` now holds **93 full lecture courses, 2,667 transcripts, 99 MB**. All legally-free (course-public YouTube auto-subs · MIT OCW CC BY-NC-SA · expert-channel public captions). All text git-ignored.

---

## Online mass-collection campaign — session 7 (2026-06-30): under-served-angle widening + campaign plan
Two parts. **(a)** Collected **6 courses · 108 transcripts** into genuinely **additive angles the corpus lacked** (not more AI/ML spine), all validated live before queueing. **(b)** Per the learner's 2026-06-30 directive, validated a named channel/playlist set and wrote a forward **[`_CAMPAIGN_PLAN.md`](_CAMPAIGN_PLAN.md)** for the next several sessions (Open-Yale + the 4 named playlists + `@mitocw`/`@stanfordonline`/`@stanford`/`@harvard` deep-scan + a **huge all-science free-textbook push** via OpenStax/LibreTexts/open monographs — "how each science pushes AGI"). Toolchain `ytchannel.sh` **hardened** (per-video `timeout 100` + `--socket-timeout 30`; a network hang had stalled the StatQuest run mid-way before the fix).

| Course (folder) | got | Domain / why additive |
|---|---|---|
| `mit-18337-scientific-machine-learning` | 25 | **NEW domain:** scientific ML / differentiable programming / physics-informed learning / neural ODEs / automatic differentiation |
| `oxford-information-theory` | 8 | rigorous entropy/coding (complements MacKay/Shannon) |
| `oxford-probability-measure-martingales` | 5 | measure-theoretic probability (deeper than applied-prob corpus) |
| `oxford-functional-analysis` | 3 | functional-analysis foundation of ML theory |
| `statquest-statistics-fundamentals` | 61 | stats-intuition channel (1 left: `_IgyaD7vOOA`, persistent transient 429) |
| `statquest-maximum-likelihood` | 6 | foundational MLE intuition |

**Session-7 GRAND TOTAL: 6 new courses · 108 lecture transcripts.** `corpus/courses/` now holds **99 full lecture courses, 2,775 transcripts, 102 MB**. All legally-free (Oxford/MIT/StatQuest/SciML course-public captions). All text git-ignored. **Next sessions:** execute [`_CAMPAIGN_PLAN.md`](_CAMPAIGN_PLAN.md) — session 8 = Open Yale Courses + the 4 named playlists; session 9 = OpenStax physical-science & math textbooks; etc.

---

**Totals (after gathering session 1, 2026-06-27):** 0 used · **373 sources chunked = 17,234 verbatim chunk files, 258 MB** · 8/8 spine arXiv IDs verified · whole owned library extracted.

**Totals (after gathering session 2, 2026-06-28):** **536 sources** (373 + 163 new) · **~21,046 verbatim chunk files** (17,234 + ~3,812 new) · **132 arXiv IDs verified vs API total (0 mismatches)** · corpus now spans 16 fresh online domain folders (neuroscience, cognitive-science, math-theory, information-computation, hardware-compute, energy, quantum, physics, robotics, biology, materials, complex-systems, blockchain-web3, economics-data, governance-safety, ai-ml-foundations) **+ the full PAPERS.md D1–D12 landmark set (125 paper folders)**. All text git-ignored. **Next:** more mass-collection can continue (Nature-only AI-for-science free copies, transcripts of debates/podcasts/YouTube per HARD_RULES §2 media rule, more authors per domain) **or** — once the learner calls the corpus rich enough — the first **grounded module rewrite** (1300 LLMs) as proof-of-standard before redoing 1000–1200. Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

**Totals (after gathering session 3, 2026-06-28):** **~1,559 sources** (536 + 26 AI-for-science free copies + 993 debate/podcast/YouTube transcripts + 4 R3 course-note sources) · **141 arXiv IDs verified vs API total** · two whole YouTube channels swept (DeepMind 212, Two-Minute-Papers 639) + Lex 7 + ALL Dwarkesh 135. All text git-ignored.

**Totals (after gathering session 4, 2026-06-28):** **~1,599 sources** (1,559 + 24 university courses [398 lecture transcripts] + 16 R4 anchors [221 chunks]) · `corpus/courses/` now holds **24 full lecture courses, 398 transcripts, 27 MB** (Stanford/MIT/DeepMind-UCL/NYU/Caltech spine + widen tier-1). All text git-ignored. **Next:** widen to the remaining long-tail course playlists ([`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md), managed queue) + R4 long tail — **or**, once the learner calls the corpus rich enough, the first **grounded module rewrite** (1300 LLMs). Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

**Totals (after gathering session 5, 2026-06-28):** **~1,643 sources** (1,599 + 33 new university courses [1,165 lecture transcripts] + 11 R4 governance/interp anchors [139 chunks]) · **142 arXiv IDs verified vs API total** (+ Intl-AI-Safety-Report 2501.17805; GraphCast 2212.12794 already held) · `corpus/courses/` now holds **62 full lecture courses, 1,617 transcripts, 68 MB** (full Stanford/MIT long-tail + Berkeley CS285/CS182 + CMU 11-785/11-711 + 3B1B + fast.ai + Stanford CS25 + NYU). The catalogued university long-tail + To-ADD channels are **effectively complete** (one gap: NYU SP20, auto-only captions env-blocked). `governance-safety/` filled with policy frameworks (NIST AI RMF + GenAI Profile, OpenAI Preparedness v2, **International AI Safety Report 2025**, Anthropic RSP, Bletchley) + Distill circuits/multimodal-neurons + Lil'Log reward-hacking. All text git-ignored. **Next:** optional residual channels — **or**, once the learner calls the corpus rich enough, the first **grounded module rewrite** (1300 LLMs). Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

**Totals (after gathering session 6, 2026-06-29):** **~1,674 sources** (1,643 + 31 new university/expert-channel courses [1,050 lecture transcripts]) · `corpus/courses/` now holds **93 full lecture courses, 2,667 transcripts, 99 MB** — widened past the AI/ML spine into the **under-served domains** (probability, quantum, physics, economics, biology, robotics/control, neuroscience, cognitive-science, applied-math/calculus, PGM, **efficient-ML/TinyML**) across **4 newly-represented universities** (Harvard STAT110 + CS50-AI, UMich EECS498, Cornell CS4780, Tübingen DL) + new Berkeley/CMU/MIT courses + 2 expert channels (Steve Brunton control/dynamics, Artem Kirsanov neuro) + MIT HAN-Lab efficient-ML. Every playlist ID validated live before queueing; no 429 storms; benign empties documented. All text git-ignored.

**Totals (after gathering session 7, 2026-06-30):** **~1,680 sources** (1,674 + 6 new courses [108 lecture transcripts]) · `corpus/courses/` now holds **99 full lecture courses, 2,775 transcripts, 102 MB** — session 7 added genuinely **additive angles** (MIT 18.337 **Scientific Machine Learning** = a new domain: differentiable programming / physics-informed learning / neural ODEs / AD; Oxford rigorous **Information Theory** + measure-theoretic **Probability/Measure/Martingales** + **Functional Analysis**; **StatQuest** Statistics-Fundamentals + Maximum-Likelihood stats intuition). Driver hardened (per-video timeout). A forward **[`_CAMPAIGN_PLAN.md`](_CAMPAIGN_PLAN.md)** now governs the next several sessions per the learner's 2026-06-30 directive: a named channel set (**Open Yale Courses** + Sapolsky/Sandel/CS50-AI + `@mitocw`/`@stanfordonline`/`@stanford`/`@harvard` deep-scan) **and a large all-science free-textbook push** (OpenStax/LibreTexts/open monographs — physics, chemistry, biology, astronomy, earth/climate, math, statistics, economics, psychology — selected for *how each science pushes AGI*). **Next:** session 8 = Open Yale Courses + the 4 named playlists. Still gathering — **do NOT write modules** until the learner calls the corpus rich enough. Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

---

## Gathering session 8 (2026-06-30): Open Yale + 4 named playlists (transcripts) + a 52-book free-textbook wave (OpenStax + Engineering/CS + David Tong) + the all-discipline campaign matrix
Two parallel streams, plus a codified forward plan. The learner sharpened the vision mid-session: **the corpus must hold free, legal resources covering every domain & sub-domain of engineering, sciences, and adjacent fields — elementary -> undergrad -> graduate/PhD -> state-of-the-art research.** Codified as **[`_LIBRARY_CAMPAIGN_MATRIX.md`](_LIBRARY_CAMPAIGN_MATRIX.md)** (authoritative target board, Sessions 9-13 waves). Learner also directed: *complete in-progress tasks this session, let new sessions handle the new extractions.*

### (a) Transcripts — 22 courses / 528 transcripts -> `courses/` (now 121 folders, 3,303 transcripts, 127 MB)
All 22 playlists validated live first (count + first title); managed queue, 2.6 s pacing, **0 rate-limit stragglers**.
**Open Yale Courses (18 / 474):** Physics I (Shankar) `24` * Physics II (Shankar) `25` * Organic Chemistry I (McBride) `37` * Organic Chemistry II (McBride) `38` * Astrophysics (Bailyn) `29` * Evolution/Ecology/Behavior (Stearns) `36` * Atmosphere/Ocean/Climate (Smith) `36` * Game Theory (Polak) `24` * Financial Markets (Shiller) `23` * Financial Theory (Geanakoplos) `26` * Intro Psychology (Bloom) `19` (1 no-caption) * Philosophy & Science of Human Nature (Gendler) `26` * Political Philosophy (Smith) `24` * Moral Foundations of Politics (Shapiro) `25` * Death (Kagan) `26` * Frontiers of Biomedical Engineering (Saltzman) `25` * Global Problems of Population Growth (Wyman) `24` * Quantum Error Correction (Yale QI) `7`.
**4 named playlists (54):** Stanford Human Behavioral Biology (Sapolsky) `22` * Harvard Justice (Sandel) `12` * Harvard CS50x 2026 `13` * Harvard CS50 Fundamentals of AI 2025 `7` (2 appended dups removed: full CS50-AI-with-Python + a CS229 talk, both already held).

### (b) Free textbooks — 52 books across new + existing domains
**OpenStax (16, CC-BY; via the CMS-API URL resolver):** University Physics Vol 1/2/3 (`physics/`) * Chemistry 2e + Atoms First 2e + Organic Chemistry (`chemistry/` NEW) * Astronomy 2e (`astronomy/`) * Calculus Vol 1/2/3 + Introductory Statistics 2e (`math-theory/`) * Psychology 2e (`cognitive-science/`) * Principles of Economics 3e (`economics-data/`) * Concepts of Biology + Microbiology + Anatomy & Physiology (`biology/`). [Dropped high-school Statistics as redundant w/ Intro Stats 2e; skipped Biology 2e - already held.]
**Engineering / CS systems (14, all author-free/CC):** `computer-systems/` NEW - OSTEP (full OS book, 67 ch -> 159 chunks), Computer Networks: A Systems Approach (Peterson-Davie, 109), Distributed Systems (Kleppmann, Cambridge), Architecture of a Database System (Hellerstein), Database Design 2e (BCcampus), Think OS. `electrical-engineering/` NEW - DSP Guide (Steven W. Smith, 34 ch -> 157), Think DSP (Downey), Lessons in Electric Circuits Vol I-V (DC/AC/Semiconductors/Digital/Reference, 351 chunks). `robotics/` - Feedback Systems (Astrom & Murray, control, 124).
**David Tong Cambridge lecture notes (22 NEW, author-free; physics end-to-end):** classical-dynamics, dynamics-and-relativity, electromagnetism, quantum-mechanics, topics-in-quantum-mechanics, quantum-field-theory, kinetic-theory, statistical-field-theory, fluid-mechanics, general-relativity, cosmology, particle-physics, standard-model, gauge-theory, solid-state-physics, quantum-hall-effect, solitons, string-theory, supersymmetric-field-theory, supersymmetric-quantum-mechanics (-> `physics/`) + vector-calculus (`math-theory/`) + mathematical-biology (`biology/`). [statistical-physics already held -> skipped. 4 courses re-fetched with correct text-notes PDFs after the largest-bytes heuristic first grabbed image-only colour-handout files.]

### Method notes (carry forward)
- OpenStax URLs resolved via the CMS API `https://openstax.org/apps/cms/api/v2/pages/?type=books.Book&fields=high_resolution_pdf_url&slug=<slug>` -> direct CC-BY PDF. Reusable: `bookresolve.sh`.
- Tong site moved to **davidtong.org**; PDFs at `/pdfs/teaching/<course>/<file>.pdf`. **Pick the largest TEXT-yielding PDF, not largest bytes** (colour-handout PDFs are image-only -> ~0 text). `tong.sh` rebuilt.
- **LibreTexts is the source for the disciplines with no clean direct PDF (mechanical/civil/chemical/aerospace/materials).** Its deki API is token-gated and batch-PDF is async -> a future session must build a **per-page public-HTML walker** (`libretexts.sh`). Documented in the matrix.
- Owned-library check: ALL local books were extracted in session 1 (362 textbook folders + canonical spine `aima`/`bishop-dl`/`goodfellow-dl`/`prince-udl`/`esl`/`mml`/`boyd-cvx`/`sutton-barto`/`huyen-aie`/`slp3` + full Kandel set + all 18 Dummies). Only documented non-book clutter + 3 image-only scans (need OCR) remain out.

**Session-8 GRAND TOTAL: 22 new courses / 528 transcripts + 52 free textbooks.** New domain folders: `chemistry/`, `computer-systems/`, `electrical-engineering/`. All legally-free; all corpus text git-ignored.

**Totals (after gathering session 8, 2026-06-30):** **~1,754 sources** (1,680 + 22 courses + 52 books) - `corpus/courses/` now 121 lecture courses / 3,303 transcripts / 127 MB; **physics now covered end-to-end** (OpenStax intro -> full Tong graduate set); new chemistry/computer-systems/electrical-engineering domains seeded. Forward plan now governed by **[`_LIBRARY_CAMPAIGN_MATRIX.md`](_LIBRARY_CAMPAIGN_MATRIX.md)** - the elementary->research, all-disciplines push (Sessions 9-13). Still gathering - **do NOT write modules** until the learner calls the corpus rich enough. Method > [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

---

## Gathering session 9 (2026-06-30): Math + Statistics end-to-end (author-PDF wave) -> `math-theory/`
Executed [`_LIBRARY_CAMPAIGN_MATRIX.md`](_LIBRARY_CAMPAIGN_MATRIX.md) §2 **Session-9 wave**: the free author/open-license textbook ladder that fills the *non-AI* core mathematics & statistics sub-domains (linear algebra, real analysis, abstract algebra, discrete math, topology, applied LA, probability/Bayes, classical+causal statistics, time-series forecasting) **and** the L1 elementary->precalculus algebra rungs (OpenStax). Every URL validated live (HEAD/range probe) before fetch. **16 books / 1,603 verbatim chunks added — all 0 FFFD, 0 ligatures.**

### (a) Core author/open PDFs (10 books, 804 chunks)
- **Hefferon — Linear Algebra** (4th ed, GNU-FDL) `91` — https://hefferon.net/linearalgebra/ (book.pdf on the UVM mirror)
- **Boyd & Vandenberghe — VMLS / Intro to Applied Linear Algebra** (free) `85` — https://web.stanford.edu/~boyd/vmls/
- **Trench — Introduction to Real Analysis** (CC-BY-NC-SA, Trinity) `102` — ramanujan.math.trinity.edu (HTTP; the HTTPS host has a TLS fault)
- **Levin — Discrete Mathematics: An Open Introduction** (4th ed, CC-BY-SA) `87` — https://discrete.openmathbooks.org/
- **Judson — Abstract Algebra: Theory and Applications** (GNU-FDL) `60` — **legal CC mirror** math.colostate.edu (official `abstract.ups.edu` was NXDOMAIN all session; content timeless; next session may re-fetch newest ed if DNS recovers)
- **Morris — Topology Without Tears** (author-free) `93` — https://www.topologywithouttears.net/
- **Downey — Think Stats** (2nd ed, CC-BY-NC) `30` + **Think Bayes** (CC-BY-NC) `24` — Green Tea Press
- **Diez/Cetinkaya-Rundel/Barr — OpenIntro Statistics** (4th ed, CC-BY-SA, screen-reader single-column) `111` — https://www.openintro.org/book/os/
- **Hernan & Robins — Causal Inference: What If** (21 Nov 2025 draft, authors-free) `121` — https://miguelhernan.org/whatifbook

### (b) OpenStax L1 algebra ladder (5 books, 748 chunks; CC-BY, via CMS-API resolver)
Prealgebra 2e `124` -> Elementary Algebra 2e `147` -> Intermediate Algebra 2e `146` -> College Algebra 2e `147` -> Precalculus 2e `184`. Completes the **arithmetic -> precalculus** rungs feeding the already-held Calculus 1-3.

### (c) HTML-only book — Hyndman & Athanasopoulos FPP3 (51 chunks)
**Forecasting: Principles and Practice** (3rd ed) is a bookdown site with no PDF. Built a **general HTML walker** (`htmlwalk.sh` + `html2txt.pl`): pulled all **143 pages in reading order** (from the summary nav `data-path`), extracted `<section class="normal">` content, concatenated -> chunked. Adds the time-series/forecasting sub-domain (ETS, ARIMA, dynamic regression, hierarchical forecasting). https://otexts.com/fpp3/

### Method notes (carry forward — toolchain improved this session)
- **`norm.pl` had a real extraction bug, now fixed (critical for any math PDF).** pdftotext `-enc UTF-8` emits plane-1 **Mathematical-Alphanumeric** letters (italic/bold variables) as **CESU-8 surrogate pairs** (lead byte `ED`), which strict UTF-8 decode turns into U+FFFD — Levin alone had 33,836. Fix: norm.pl now (1) reconstructs `ED A0-AF / ED B0-BF` surrogate pairs into the real codepoint, then (2) **NFKC-folds** so math-italic `𝑥`->`x` AND **fi/fl/ff ligatures** -> ASCII (the ligatures silently broke grep for words like "definition"/"coefficient" in 6 books until re-run). Rebuild norm.pl with these two steps every session.
- `getpdf.sh` uses `pdftotext -layout -enc UTF-8`; verifies `%PDF` magic + min-text-bytes (rejects image-only).
- OpenStax CMS-API resolver unchanged (`bookresolve.sh`). Trench: prefer **HTTP** (HTTPS TLS-faulty). Judson: official host DNS-dead this session -> used legal academic mirror.

**Session-9 GRAND TOTAL: 16 free math/stats books / 1,603 verbatim chunks -> `math-theory/`** (all clean). Mathematics now spans **arithmetic -> precalc -> calculus -> linear algebra -> real analysis -> abstract algebra -> topology -> discrete math**; Statistics spans **descriptive -> probability -> inference -> Bayesian -> causal -> time-series forecasting**. All legally-free; all corpus text git-ignored.

**Totals (after gathering session 9, 2026-06-30):** **~1,770 sources** (1,754 + 16 books) · `corpus/math-theory/` substantially deepened (now ~30 book/paper folders covering the non-AI math+stats core end-to-end). New reusable tools: `htmlwalk.sh` + `html2txt.pl` (general bookdown/GitBook walker — also the basis for the §11 LibreTexts walker) and the **fixed `norm.pl`**. Still gathering — **do NOT write modules** until the learner calls the corpus rich enough. Next ▶ matrix §2 **Session 10 = CS depth + EE/ECE depth** (Crafting Interpreters, Boneh-Shoup crypto, Erickson Algorithms, Software Foundations, PBR; Ellingson Electromagnetics, Preskill quantum notes, Lienhard heat-transfer). Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).
