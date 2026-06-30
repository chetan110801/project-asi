# 🛰️ Frontier R&D Corpus — companies × universities × organizations × every field
**Learner directive (2026-07-01, session 14):** *"Collect all the info — projects, research, publications, video/talk details, and any possible books — from all the top-tech **companies**, **universities**, and **organizations** across every domain of engineering, science, and adjacent fields (Neuralink explicitly included)."*

This is **Stream 3** of the corpus campaign, alongside Stream 1 (courses/transcripts) and Stream 2 (textbooks/papers — see [`_LIBRARY_CAMPAIGN_MATRIX.md`](_LIBRARY_CAMPAIGN_MATRIX.md)). It captures the **public output of the frontier institutions** so modules can be grounded in *what the leading labs are actually building*, not just textbook fundamentals. Text lands in **`corpus/frontier-rnd/<org-slug>/`** (git-ignored); only this tracking md is published.

`Status: Living plan · Created 2026-07-01 (session 14) · multi-session — breadth across all institutions × all fields`

---

## 0. Governing rules
1. **Legality absolute.** Only public / open / CC / public-domain / open-access / arXiv / gov material: research **blogs & RSS feeds**, **open-access papers** (arXiv, bioRxiv, JMIR, EuropePMC-OA), **company whitepapers/tech-reports** posted publicly, **gov tech reports** (NASA NTRS = public domain), **conference/keynote talk transcripts** (YouTube auto-subs). Paywalled / internal / login-gated → [`../REQUESTS.md`](../REQUESTS.md), never scrape.
2. **Validate-before-fetch.** HEAD/probe every URL live; confirm a feed carries real items (not a SPA HTML shell mis-served as `.xml`). Prefer **full-text RSS** (`content:encoded`) > sitemap-enumerated article pages > index snapshot.
3. **Durability filter.** Keep the *substance* — what a project is, the principle/result behind it, why it matters toward AGI/ASI and across science. A product-launch nav-blurb is kept only as a dated **project-catalog snapshot** (tag it). Marketing fluff with no technical content is skipped.
4. **Snapshot honesty.** Blog/feed content is time-stamped and moves fast → every folder's `_SOURCE.txt` records the URL + capture date; treat as a 2026 snapshot, re-sweep in future sessions.
5. **Anti-redundancy.** Don't re-pull what Stream 1/2 already hold (DeepMind/Two-Minute-Papers/Lex/Dwarkesh/Sutton YouTube; the PAPERS.md landmark arXiv set; the AlphaFold/GraphCast/etc. AI-for-science papers). This stream adds the *institution-indexed* layer on top.
6. **Git:** all `frontier-rnd/**` text git-ignored; tick this file every session.

## 0a. Method & toolkit (scratchpad, rebuild each session)
- **`rss2txt.pl` (BUILT session 14):** parse RSS 2.0 / Atom (stdin) → clean per-item records (`TITLE / DATE / CATEGORIES / LINK / body`); CDATA-aware; strip→decode→strip (handles `content:encoded` escaped-HTML); pulls full body when the feed carries it, else title+summary index.
- **`rndfeed.sh <url> <slug> "<src>" [rss|html]` (BUILT session 14):** curl → rss2txt (or html2txt for static index) → norm.pl → chunk.sh → `frontier-rnd/<slug>/`; THIN-guard (<1200 B skipped); 0-FFFD QC.
- **`getpdf.sh`** for whitepapers / open-access PDFs (Neuralink JMIR, NASA NTRS reports).
- **`ytchannel.sh`+`vtt2txt.pl`** for talk/keynote channels — **ONE channel at a time** (429 storms otherwise).
- **`chunk.sh` hardened (session 14):** now also hard-caps a chunk at 3× target on any line boundary (guards a body with no blank-line separators → no more single giant chunk).
- **SPA caveat:** most company blogs (DeepMind, Apple-ML articles, BAIR HTML, NVIDIA-research, Neuralink updates, Stanford-HAI) are JS-rendered → curl gets a shell. Routes that work: their **RSS feed**, their **sitemap** (URL list), their **PDFs**, or their **YouTube channel**. Don't waste cycles de-chroming a SPA article — switch route.

---

## 1. THE MATRIX — institutions × field × output, with status
Legend: ✅ collected (session 14) · 🟡 partial / index-only / snapshot · ⬜ to fetch · 🔁 held via Stream 1/2 (don't duplicate). Output types: **B**=blog/feed, **P**=papers/whitepaper, **V**=video/talk channel, **R**=gov/tech report.

### AI / ML labs — companies
| Institution | Field | Status | Source captured / target |
|---|---|---|---|
| **Google Research** | AI, all-science | 🟡 B (index RSS) | `research.google/blog/rss/` — index only (SPA articles); ⬜ deepen via arXiv |
| **Google DeepMind** | AI, AI-for-science | ✅ B · 🔁 V (214) · 🔁 P | `deepmind.google/blog/rss.xml` ✅ (`deepmind-blog-rss`, supersedes index snapshot); YouTube + papers held |
| **Google Quantum AI** | quantum | 🟡 B-snapshot | `quantumai.google` project catalog (Willow/Quantum Echoes); ⬜ papers |
| **Meta AI / FAIR** | AI | 🟡 B | Meta Engineering feed ✅; ⬜ ai.meta.com/research publications |
| **NVIDIA** | AI HW, deep learning | ✅ B | developer blog (deep-learning) RSS ✅; ⬜ research.nvidia.com (SPA→arXiv) |
| **Amazon Science** | AI, robotics | ✅ B | `amazon.science/index.rss` ✅ |
| **Apple ML Research** | AI on-device | 🟡 B (RSS thin) | `machinelearning.apple.com/rss.xml` ✅(1); ⬜ sitemap article pages |
| **Hugging Face** | open ML | ✅ B | `huggingface.co/blog/feed.xml` ✅ |
| **Microsoft Research** | AI, all-science | ✅ B | `microsoft.com/en-us/research/feed/` ✅ (403/000 FIXED with research UA) |
| **OpenAI** | AI | ✅ B | `openai.com/blog/rss.xml` ✅ (real RSS — supersedes sitemap-only) |
| **Anthropic** | AI safety | 🟡 (article prose partial) | research index reachable; ⬜ enumerate + fetch articles (rss.xml is SPA) |
| **IBM Research** | AI, quantum | 🟡 | blog RSS still SPA; **IBM Quantum/Qiskit Medium feed ✅** (`ibm-quantum-qiskit`); ⬜ IBM Research YouTube |
| **AI2 (Allen Inst. for AI)** | AI | ✅ B | `medium.com/feed/ai2-blog` ✅ (404 FIXED via Medium) |
| xAI · Cohere · Mistral · Stability · EleutherAI | AI | ⬜ | next sessions |

### Brain–Computer Interface — companies (⭐ learner-named)
| **Neuralink** | BCI / neurotech | ✅ P + R | JMIR 2019 whitepaper (1000-channel BMI platform) ✅ + PRIME Study brochure (N1 implant / R1 robot) ✅; ⬜ technology/updates are SPA → route via YouTube |
| Synchron · Blackrock Neurotech · Precision Neuro · Kernel | BCI | ⬜ | open papers / press; next sessions |

### Robotics / autonomy — companies
| **Boston Dynamics** | legged/humanoid robotics | 🟡 B-snapshot | blog catalog (Atlas) snapshot ✅; ⬜ YouTube channel (rich) |
| **Waymo** | autonomous driving | ✅ B | `waymo.com/blog` ✅; ⬜ waymo.com/research papers |
| Tesla AI · Figure · 1X · Agility · NVIDIA Isaac | robotics/embodied | ⬜ | AI-Day transcripts (YouTube), papers |

### Universities — labs & news (full-text feeds = gold)
| **MIT News** (per-field full-text feeds) | **all fields** | ✅✅ | physics·biology·chemistry·neuroscience·energy·quantum-computing·materials-science·genetics·mathematics·climate·**AI**·**CSAIL** — 12 feeds ✅ |
| **MIT CSAIL** (site) | AI/CS | ✅ B | `csail.mit.edu/rss.xml` ✅ |
| **Berkeley BAIR** | AI | ✅ B (full-text) | `bair.berkeley.edu/blog/feed.xml` ✅ |
| **Stanford HAI / SAIL** | AI | 🟡 | HAI rss.xml is a Next.js SPA → use sitemap; **main Stanford news ✅** (`stanford-news`) |
| **IEEE Spectrum** (prof. body) | engineering, all | ✅ B | `spectrum.ieee.org/feeds/feed.rss` ✅ |
| **CMU** | AI/CS/eng, all | ✅ B | `cmu.edu/news/rss/news.xml` ✅ (`cmu-news`, 20) |
| **UC Berkeley** | all-science | ✅ B | `news.berkeley.edu/feed/` ✅ (+ BAIR already held) |
| **Caltech** | all-science | ✅ B | `caltech.edu/about/news/rss` ✅ (Atom) |
| **Toronto / Vector Institute** | AI | ✅ B | `vectorinstitute.ai/feed/` ✅ (full-text, 270 articles) |
| **Quanta Magazine** (science press) | math/physics/CS/bio frontier | ✅ B | `api.quantamagazine.org/feed/` ✅ (summary feed) |
| Oxford · ETH · Toronto Vector · Stanford-medicine · Princeton-Eng | many | 🟡/⬜ | Vector ✅; Oxford/ETH rss = SPA; Princeton-Eng empty-parse — next sessions |

### Research organizations / national labs / gov
| **NASA** (NTRS) | aerospace, space, AI, materials | ✅ R | 6 public-domain report PDFs across fields: RL spacecraft attitude control · hybrid-rocket propulsion · additive-mfg propulsion components · hypersonic aerodynamics · space-radiation human health · Earth-science deep learning. (search-API → `/api/citations/<id>/downloads/<file>.pdf`) |
| **LBNL** (Berkeley Lab, DOE) | physics/energy/bio | ✅ B | `newscenter.lbl.gov/feed/` ✅ |
| **EMBL** (mol. biology) | biology/genomics | ✅ B | `embl.org/news/feed/` ✅ |
| **Fermilab** (DOE) | particle physics | ✅ B | `news.fnal.gov/feed/` ✅ |
| **DARPA** | defense R&D, all | ✅ B | `darpa.mil/rss/news.xml` ✅ (404 FIXED) |
| **NIST** | metrology/standards/QIS | ✅ B | `nist.gov/news-events/news/rss.xml` ✅ |
| **Sandia National Labs** (DOE) | energy/HW/security | ✅ B | `newsreleases.sandia.gov/feed/` ✅ |
| **NASA** (JPL + main) | space/aero/Earth | ✅ B | `jpl.nasa.gov/feeds/news/` + `nasa.gov/feed/` ✅ (NTRS PDFs also held) |
| **ESA** | space | ✅ B | `esa.int/rssfeed/Our_Activities/Space_News` ✅ |
| **Broad Institute** | genomics/biomedicine | ✅ B | `broadinstitute.org/rss.xml` ✅ |
| Allen Institute (Brain) · EMBL-EBI · CERN · ORNL/LLNL/Argonne/NREL/PNNL/SLAC/BNL · NIH/NCBI · Santa Fe Inst. | many | ⬜ | next sessions — all SPA/404 to curl: route via sitemap or their YouTube |

### Other frontier sectors (next sessions)
- **Quantum HW:** **IBM Quantum/Qiskit ✅** (`ibm-quantum-qiskit`) · IonQ · Quantinuum · PsiQuantum · Rigetti (all SPA — route via arXiv/YouTube).
- **Semiconductors/compute:** **ARM ✅** (`arm-newsroom`) · TSMC · Intel · AMD · Cerebras · Groq · Tenstorrent (SPA — route via newsroom RSS where they exist).
- **Fusion/energy:** Commonwealth Fusion · Helion · TAE · ITER (`whatsnew/rss` = THIN index) · NREL (feed empty).
- **Biotech/AI-for-bio:** Isomorphic Labs · Recursion · insitro · Ginkgo · Arc Institute.
- **Space:** SpaceX · Blue Origin · JPL (NASA) · ESA.

---

## 2. Session waves
- **Session 15 ✅ (org-feed wave) — 21 feeds / 295 chunks → `frontier-rnd/` (all 0 FFFD; `frontier-rnd/` now 56 folders).** Re-probed every SPA-miss + new candidates with the research UA; collected the confirmed RSS/Atom feeds via `rndfeed.sh` (curl, sequential). **AI labs (5):** Microsoft Research (`microsoft-research-blog` — the 403/000 miss is FIXED with UA, 7), OpenAI (`openai-blog`, 26 — real RSS, supersedes the sitemap-only note), Google DeepMind (`deepmind-blog-rss`, 3 — real full RSS, supersedes the `deepmind-blog-index` snapshot), EleutherAI (`eleuther-ai-blog`, 2), **AI2 / Allen Institute for AI** (`ai2-allen-ai-blog` via Medium feed, 4 — the 404 is FIXED). **Semiconductor/quantum/fusion:** ARM newsroom (4), IBM Quantum/Qiskit (Medium, 7); ITER `whatsnew/rss` = index-only THIN, skipped. **Biotech/space:** Broad Institute (6), ESA Space News (1), NASA JPL (3), NASA main (5). **National labs/gov:** Fermilab (2), DARPA (1 — the feed 404 is FIXED: `darpa.mil/rss/news.xml`), NIST (2), Sandia (5). **Universities/institutes:** Stanford (1), CMU (20), UC Berkeley (1), Caltech (Atom, 5), **Vector Institute** (189 — full-text feed, 270 unique articles verified no-dup); Princeton-Engineering = empty-parse, skipped. **Science press:** Quanta Magazine (1, summary feed — like IEEE Spectrum, a frontier-science publication). **Still SPA/no-feed (route via YouTube/sitemap/PDF next):** IBM Research blog, Anthropic, Cohere, ORNL, LLNL, Argonne, CERN, Allen Institute (brain), EMBL-EBI, IonQ, Quantinuum, Rigetti, Cerebras, Groq, PsiQuantum, Ginkgo, Arc Institute, Blue Origin, PNNL, SLAC, BNL, ETH-Zürich, Oxford, Mila, NREL (empty). **⚠️ carry-forward gotcha:** a few WordPress/Medium feeds leak em-dash mojibake (`â` for `—`) — FFFD=0, prose & grep intact; `norm.pl` ASCII-folds smart quotes but not this double-encoded `â€"` sequence — add a fold rule next session if worth it. **DEFERRED to next session (learner paused to shut down mid-wave):** NASA NTRS report PDFs (more fields) + the YouTube talk-channel pulls (Boston Dynamics / IBM Research / MSR / NVIDIA / Neuralink — one-at-a-time).
- **Session 14 ✅ (first wave) — 35 sources / 364 chunks → `frontier-rnd/` (all 0 FFFD).** Built `rss2txt.pl` + `rndfeed.sh`; hardened `chunk.sh` (3× hard-cap). **AI labs:** Google Research, Amazon Science, NVIDIA, Apple ML, Hugging Face, Meta Engineering, Berkeley BAIR (full-text), MIT CSAIL. **MIT News all-field full-text feeds (12):** AI, CSAIL, physics, biology, chemistry, neuroscience, energy, quantum-computing, materials-science, genetics, mathematics, climate. **Engineering:** IEEE Spectrum. **BCI ⭐:** Neuralink JMIR whitepaper + PRIME brochure. **Robotics/quantum snapshots:** Boston Dynamics, Waymo, Google Quantum AI, DeepMind (catalog snapshots). **Orgs/gov:** NASA NTRS (6 public-domain report PDFs across fields), LBNL (Berkeley Lab), EMBL. [Stanford-HAI/Allen-Institute dropped — SPA/404, no feed.]
- **Session 16+ — continue (Session-15 feed wave done above):** (a) **YouTube talk channels** one-at-a-time — Boston Dynamics, MIT, Stanford, IBM Research, NVIDIA, Microsoft Research, Neuralink, company keynote channels. (b) **More org feeds** — find working feeds/sitemaps for MSR, IBM, AI2, Anthropic (enumerate articles), OpenAI, Stanford HAI, CMU, national labs, Allen Institute, CERN, EMBL-EBI. (c) **NASA NTRS** — fetch public-domain report PDFs per field. (d) **Quantum/semiconductor/fusion/biotech/space** sectors (table above). (e) re-sweep session-14 feeds (they advance). Always: validate-live → `rndfeed.sh`/`getpdf.sh`/`ytchannel.sh` → 0-FFFD QC → tick this file.

> Each session: validate-live → managed collect → 0-FFFD QC → tick this file + [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) → refresh handoff → commit tracking md. **Multi-session; breadth across all institutions × all fields is the goal.**
