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
| MacKay — ITILA | `r-mackay-itila` | ② | ⬜ | free PDF |
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
| Tedrake — Underactuated Robotics | — | ② | ⬜ | free HTML (MIT) |
| Raieli — AI Agents w/ LLMs, RAG | `r-raieli-agents` | ① | ⬜ | owned |
| Kawahara — HW Technologies for AI | `r-kawahara-hw` | ① | ⬜ | owned (compute) |
| HF courses (LLM/NLP/RL/Agents) | `r-hf-courses` | ② | ⬜ | HTML |
| CS231n / CS224n / CS285 notes | `r-cs231n`,`r-cs224n`,`r-berkeley-cs285` | ② | ⬜ | notes/slides |
| **Papers D5–D9** (RL/agents, systems, diffusion, multimodal, RAG) | — | ② | ⬜ | from PAPERS.md |

## Tier 3 — AI-for-science & intersected frontiers
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Gerstner — Neuronal Dynamics | `r-neuronal-dynamics` | ② | ⬜ | free HTML (EPFL) |
| Hawkins — A Thousand Brains | `r-hawkins-1000brains` | ① | ⬜ | owned EPUB |
| AlphaFold — EBI guide + preprints | `r-alphafold-ebi` | ② | ⬜ | bio |
| Preskill Ph229 / Quantum Country / Qiskit | `r-preskill-ph229`,`r-quantum-country` | ② | ⬜ | quantum |
| GraphCast / GNoME / tokamak / AlphaGeometry | — | ② | ⬜ | lab blogs + arXiv |
| Shakarian — Metacognitive AI | `r-shakarian-metacog` | ① | ⬜ | owned |
| **Papers D10–D12** (post-transformer, robotics, AI-for-science) | — | ② | ⬜ | from PAPERS.md |

## Tier 4 — world & society
| Source | `r-id` | Stream | Stage | Notes |
|---|---|---|---|---|
| Epoch AI — compute/data trend reports | — | ② | ⬜ | scaling limits, data econ |
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

**Totals (after gathering session 1, 2026-06-27):** 0 used · **373 sources chunked = 17,234 verbatim chunk files, 258 MB** · 8/8 spine arXiv IDs verified · whole owned library extracted. Remaining ⬜ (fetch only if a module needs them — not in backup): Murphy PML, MacKay ITILA, CS336/CS231n/CS224n course sites, Tedrake robotics, Tier-3/4 web anchors (Epoch, AI Index, quantum notes). **Next:** the first **grounded module rewrite** (1300 LLMs) can now begin — proof-of-standard before redoing 1000–1200. Method ▶ [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).
