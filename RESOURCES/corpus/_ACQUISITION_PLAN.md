# Corpus Acquisition Plan — full breadth
**The target list for building the grounding substrate.** What to gather, from where, in what order — across **every crucial science/technology field that can drastically affect humanity and advance society (prioritizing AGI/ASI).** Binding scope, durability filter, and media rules: [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §1–§2. Legality + git treatment: [`README.md`](README.md).

`Status: Living plan · Created 2026-06-27 (v2.3); scope+media broadened v2.4 · Execute per` [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) `· Track in` [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md)

> **SCOPE (v2.4):** not AI alone — **all crucial domains, studied independently (foundations → advanced), then merged.** A living queue (full map: [`../../INSTRUCTIONS/DOMAIN_DISCOVERY_SYSTEM.md`](../../INSTRUCTIONS/DOMAIN_DISCOVERY_SYSTEM.md)): brain & neuroscience · cognitive science · AI/ML/DL/RL/LLMs/agents · robotics · math & theory · information & computation · hardware/chips/compute · energy · **quantum computing** · biology/biotech · materials · physics · complex systems · **blockchain/web3/decentralization** · economics & data · governance/safety/alignment. The AI spine (Tiers 1–2 below) is acquired **first** for leverage; the rest follow in the same sweep.
>
> **DURABILITY FILTER (v2.4):** collect the **timeless, grounded principles — the reason/objective behind things — not the transient specifics** (we don't memorize the 2012-vs-2020 algorithm; we learn *why* it exists so we could build the next). Fast-aging facts only when decision-relevant, tagged as snapshots. (HARD_RULES §2.)
>
> **ALL MEDIA (v2.4):** textbooks · books · research papers/publications · courses/lectures · survey & review papers · serious blogs/essays · recorded **debates & interviews** (gold — expert disagreement) · **podcasts** · **video/YouTube (transcripts)**. Use videos/podcasts/blogs for intuition & the "why"; **ground factual claims to primary/durable sources.** Extraction of transcripts: [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md).

> **Two streams, run both:**
> - **① EXTRACT-LOCAL** — the learner **already owns** ~250 books in (git-ignored) [`../../local_resources/`](../../) (4.9 GB). Converting the relevant ones to chunked text is the **fastest, fully-legal win** (their own copies, used locally to write notes). *Do this first — no download, no copyright question.*
> - **② FETCH-FREE** — download the **legally-free online full text** not already local: arXiv papers + author-published textbooks + open course notes. URLs below.
>
> **DRY:** this plan is the *acquisition layer* over the existing catalogs. The **paper target list is** [`../PAPERS.md`](../PAPERS.md) (~145 landmark→SOTA papers, 13 areas D0–D12) — **don't re-list it here**; fetch from there. The **resource IDs** (`r-…`) map to [`../INDEX.md`](../INDEX.md). This file adds the **how/where/priority** and the broad-field sources the catalogs point at.

---

## Priority order (depth on the spine first within the full-breadth sweep)
The learner chose **full breadth**, but acquire in this order so grounded modules can start ASAP and the sweep still finishes wide:
1. **Tier 1 — core spine** (needed for the next modules 1400–1900): ML/DL, neural nets, RL, LLMs, scaling, compute/data, alignment.
2. **Tier 2 — applied & embodied**: robotics/embodied AI, agents/RAG, efficiency/systems, multimodal, diffusion.
3. **Tier 3 — AI-for-science & intersected frontiers**: biology/medicine, math, materials, weather/fusion, space/astro, neuro/BCI, quantum, decentralized/web3, world models.
4. **Tier 4 — world & society**: scaling-limits/data-economics, governance/geopolitics, safety institutions, the annual index reports.

---

## ① EXTRACT-LOCAL — books the learner already has (do first)
Convert these from [`../../local_resources/`](../../) to chunked `.txt` (method in [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) §Extract). High-value, already-owned, spine-relevant:

| Local file (in `local_resources/`) | Maps to | Tier |
|---|---|---|
| `RLbook2020.pdf` — Sutton & Barto, *RL: An Introduction* 2e | `r-sutton-barto` | 1 (RL) |
| `Bishop C. Deep Learning. Foundations and Concepts 2023` | `r-bishop-dl` | 1 (DL) |
| `Stuart Russell … AIMA (3rd ed).pdf` / `AI - A Modern Approach 3rd` | `r-aima` | 1 (AI breadth) |
| `Huyen C. AI Engineering … Foundation Models 2025` | `r-huyen-aie` | 1 (LLM apps) |
| `A Thousand Brains … Jeff Hawkins EPUB` | `r-hawkins-1000brains` | 3 (neuro) |
| `The Alignment Problem … Brian Christian EPUB` | `r-christian-alignment` | 1 (alignment) |
| `Life 3.0 … Max Tegmark EPUB` | `r-tegmark-life3` | 4 (society) |
| `Sapiens … Harari EPUB` | `r-harari-sapiens` | 3 (evolution/culture) |
| `Siciliano B. Foundations of Robotics 2025` | `r-siciliano-robotics` | 2 (robotics) |
| `Kawahara T. Hardware Technologies for AI 2026` | `r-kawahara-hw` | 2 (compute) |
| `Togelius J. Artificial General Intelligence 2024` | `r-togelius-agi` | 4 (paths to AGI) |
| `Shakarian P. … Metacognitive AI 2025` | `r-shakarian-metacog` | 3 (frontier) |
| `Raieli S. Building AI Agents with LLMs, RAG… 2025` | `r-raieli-agents` | 2 (agents) |
| `Mainzer K. … Neuromorphic Systems 2024` | `r-mainzer-neuro` | 3 (neuro/HW) |
| `Kandel … Principles of Neural Science (10 books)` | `r-kandel` | 3 (neuro) |
| *(scan the rest of `_local-books-manifest.txt`; extract any the modules will cite)* | — | — |

> The full owned-book list is [`../library/_local-books-manifest.txt`](../library/) (git-ignored). Extract **on demand** — a book a soon-to-be-written module will cite jumps the queue.

---

## ② FETCH-FREE — legally-free online full text

### A. Free textbooks (author-published) — Tier 1–2
| Book | `r-id` | URL | Format / fetch note |
|---|---|---|---|
| Goodfellow, Bengio, Courville — *Deep Learning* | `r-goodfellow-dl` | deeplearningbook.org | HTML per chapter (read-free; not a single download) |
| Zhang et al. — *Dive into Deep Learning* | `r-d2l` | d2l.ai (PDF: d2l.ai/d2l-en.pdf) | **Open-licensed** PDF + HTML — easy, high-value |
| Nielsen — *Neural Networks & Deep Learning* | `r-nielsen-nndl` | neuralnetworksanddeeplearning.com | HTML chapters |
| Prince — *Understanding Deep Learning* | `r-prince-udl` | udlbook.github.io/udlbook | Free PDF (GitHub) |
| Murphy — *Probabilistic ML* (Intro + Advanced) | `r-pml-murphy` | probml.github.io/pml-book | Free PDFs (GitHub) |
| Jurafsky & Martin — *Speech & Language Processing* (SLP3) | `r-slp3` | web.stanford.edu/~jurafsky/slp3 | Free per-chapter + full PDF (Jan-2026 draft) |
| MacKay — *Information Theory, Inference & Learning* | `r-mackay-itila` | inference.org.uk/itila/book.html | Free PDF |
| Boyd & Vandenberghe — *Convex Optimization* | `r-boyd-cvx` | web.stanford.edu/~boyd/cvxbook | Free PDF |
| Deisenroth et al. — *Mathematics for ML* | `r-mml` | mml-book.github.io | Free PDF |
| James et al. — *Intro to Statistical Learning* | `r-isl` | statlearning.com | Free PDF |
| Hastie et al. — *Elements of Statistical Learning* | `r-esl` | hastie.su.domains/ElemStatLearn | Free PDF |
| Blitzstein & Hwang — *Intro to Probability* | `r-stat110` | probabilitybook.net | Free PDF + Stat110 site |
| Gerstner et al. — *Neuronal Dynamics* | `r-neuronal-dynamics` | neuronaldynamics.epfl.ch | Free HTML (EPFL) |

### B. Open courses / notes / transcripts — Tier 1–2
| Course | `r-id` | URL | Note |
|---|---|---|---|
| OpenAI **Spinning Up in Deep RL** | `r-spinningup` | spinningup.openai.com | HTML + code; canonical RL intro |
| Stanford **CS231n** (vision) notes | `r-cs231n` | cs231n.github.io | HTML notes |
| Stanford **CS224n** (NLP) | `r-cs224n` | web.stanford.edu/class/cs224n | Slides/notes |
| Stanford **CS336** (build an LLM) | `r-cs336` | stanford-cs336.github.io | Lectures/assignments |
| Berkeley **CS285** (deep RL, Levine) | `r-berkeley-cs285` | rail.eecs.berkeley.edu/deeprlcourse | Slides + lectures |
| **CS234** (RL, Stanford) | `r-cs234` | web.stanford.edu/class/cs234 | Slides |
| Karpathy **Zero to Hero** | `r-karpathy-zth` | karpathy.ai / YouTube + nanoGPT repo | Transcripts + code |
| **Hugging Face** courses (LLM/NLP/RL/Agents) | `r-hf-courses` | huggingface.co/learn | HTML |
| **AI Safety Fundamentals** (alignment + governance) | `r-aisf` | aisafetyfundamentals.com | Free curriculum + readings |
| **ARENA** (mech-interp / alignment, code) | `r-arena` | arena.education (arena-ch*…github.io) | Notebooks |
| **Sutton — The Bitter Lesson** (essay) | — | incompleteideas.net/IncIdeas/BitterLesson.html | 1 page; already cited in modules |

### C. Papers — Tier 1–4 (the whole breadth)
**Fetch from [`../PAPERS.md`](../PAPERS.md)** — it already maps the landmark→SOTA set across D0–D12 (core ML, attention/transformers, scaling/emergence/reasoning, alignment/RLHF, RL+agents, efficiency/systems, diffusion, multimodal, agents/RAG, post-transformer, robotics/embodied, and the AI-for-science + intersected-frontier section). Acquisition rules:
- **VERIFY each arXiv ID against the arXiv API first** (titles+authors+year are the reliable handle; IDs in PAPERS.md are best-effort from memory — this is the standing caveat). Fix mismatches in PAPERS.md as you go.
- Pull the **PDF + (where present) the LaTeX/HTML source** from `arxiv.org/abs/<id>`; arXiv allows programmatic bulk access (API + `export.arxiv.org`). Rate-limit politely.
- For **Nature/Science** landmark results (AlphaGo, AlphaFold, GraphCast, tokamak control, GNoME, AlphaTensor/Geometry): grab the **free arXiv/lab preprint or the lab blog**, not the paywalled version.

### D. Broad-field free anchors (Tier 3–4) — sources the catalogs point at
| Field | Free anchor(s) | Fetch note |
|---|---|---|
| Robotics / embodied | **Underactuated Robotics** (Tedrake, MIT) underactuated.mit.edu; RT-1/RT-2/RT-X, Open-X (arXiv) | free HTML book + arXiv |
| Biology / medicine | **AlphaFold** EBI guide (`r-alphafold-ebi`); ESM/ESMFold, AlphaFold2/3 preprints | EMBL-EBI free course + arXiv |
| Math | AlphaGeometry, AlphaTensor, FunSearch (lab blogs + arXiv) | preprints |
| Materials | **GNoME** (DeepMind blog + arXiv), Open Catalyst | preprints |
| Weather / climate | **GraphCast**, FourCastNet, Pangu-Weather | arXiv |
| Fusion | DeepMind **tokamak magnetic control** (Nature 2022 + arXiv) | preprint |
| Neuro / BCI | `r-neuronal-dynamics` (above); predictive-coding reviews; `r-hawkins-1000brains` (local) | free book + papers |
| Quantum computing | **Preskill Ph229** notes (theory.caltech.edu/~preskill/ph229); **Quantum Country** (quantum.country); **Qiskit textbook** | free notes/HTML |
| Decentralized / web3 AI | survey papers on decentralized training / federated learning (arXiv) | preprints |
| Scaling limits / data econ | **Epoch AI** reports (epoch.ai) — compute & data trends; "Will we run out of data?" (Villalobos et al., arXiv) | free reports + arXiv |
| Governance / society | **Stanford HAI AI Index** (annual, free PDF); lab **Responsible Scaling / Preparedness** frameworks; OECD/GPAI | free PDFs |
| Superintelligence / paths | `r-bostrom-superint`, `r-russell-hc` (route to BUY/own); `r-togelius-agi` (local) | books |

---

## BUY-list — paid, not to be pirated (route to REQUESTS.md)
Good but paywalled and **not** the learner's already-owned copies → add/confirm in [`../REQUESTS.md`](../REQUESTS.md), don't scrape:
- Bishop — *Pattern Recognition & ML* (PRML) `r-bishop-prml` *(note: free PDF was released by author — verify; if free, move to FETCH-FREE)*
- Nielsen & Chuang — *Quantum Computation & Quantum Information* `r-nielsen-chuang` *(check author free copy; else buy)*
- Bostrom — *Superintelligence* `r-bostrom-superint`; Russell — *Human Compatible* `r-russell-hc`
- Any Tier-3/4 field book with no free edition and not already in `local_resources/`.

> Before buying anything, **re-check for an official free copy** (many authors post final PDFs); only truly-paywalled, needed sources go on the BUY-list.

---

## Definition of done (this acquisition)
- Every **Tier-1** source is **extracted + chunked** in `corpus/` and ticked in [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md).
- Tiers 2–4 are **at least fetched** (PDF/HTML saved) with the highest-value items chunked.
- PAPERS.md arXiv IDs are **verified** (mismatches fixed) at least for everything a written/near-term module cites.
- The first **grounded module rewrite** (proof-of-standard) can begin — see [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) §Next.
