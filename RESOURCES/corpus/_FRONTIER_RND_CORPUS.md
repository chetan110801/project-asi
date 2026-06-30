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
| **Google DeepMind** | AI, AI-for-science | 🟡 B-snapshot · 🔁 V (214) · 🔁 P | blog index snapshot; YouTube + papers already held |
| **Google Quantum AI** | quantum | 🟡 B-snapshot | `quantumai.google` project catalog (Willow/Quantum Echoes); ⬜ papers |
| **Meta AI / FAIR** | AI | 🟡 B | Meta Engineering feed ✅; ⬜ ai.meta.com/research publications |
| **NVIDIA** | AI HW, deep learning | ✅ B | developer blog (deep-learning) RSS ✅; ⬜ research.nvidia.com (SPA→arXiv) |
| **Amazon Science** | AI, robotics | ✅ B | `amazon.science/index.rss` ✅ |
| **Apple ML Research** | AI on-device | 🟡 B (RSS thin) | `machinelearning.apple.com/rss.xml` ✅(1); ⬜ sitemap article pages |
| **Hugging Face** | open ML | ✅ B | `huggingface.co/blog/feed.xml` ✅ |
| **Microsoft Research** | AI, all-science | ⬜ | feed 403/000 to curl → try sitemap / MSR YouTube |
| **OpenAI** | AI | ⬜ B (sitemap held) | research sitemap enumerated (SPA articles); ⬜ route via papers |
| **Anthropic** | AI safety | 🟡 (article prose partial) | research index reachable; ⬜ enumerate + fetch articles |
| **IBM Research** | AI, quantum | ⬜ | RSS 404 → find feed / IBM Research YouTube |
| **AI2 (Allen Inst. for AI)** | AI | ⬜ | blog feed 404 → find correct URL |
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
| **Stanford HAI / SAIL** | AI | ⬜ | rss.xml is a Next.js SPA → use sitemap |
| **IEEE Spectrum** (prof. body) | engineering, all | ✅ B | `spectrum.ieee.org/feeds/feed.rss` ✅ |
| CMU SCS/RI · Oxford · ETH · Toronto Vector · Stanford-medicine | many | ⬜ | next sessions (find full-text feeds) |

### Research organizations / national labs / gov
| **NASA** | aerospace, space, AI | ⬜ R (API probed ✅) | NTRS public-domain reports — search-API works; ⬜ fetch report PDFs per topic |
| Allen Institute (Brain Science) · Broad Institute · EMBL-EBI · CERN · DOE labs (ORNL/LLNL/Argonne/NREL/Fermilab) · DARPA · NIH/NCBI · ESA · Santa Fe Institute | many | ⬜ | next sessions |

### Other frontier sectors (next sessions)
- **Quantum HW:** IBM Quantum · IonQ · Quantinuum · PsiQuantum · Rigetti — papers/blogs.
- **Semiconductors/compute:** TSMC · Intel · AMD · ARM · Cerebras · Groq · Tenstorrent — tech blogs/whitepapers.
- **Fusion/energy:** Commonwealth Fusion · Helion · TAE · ITER · NREL.
- **Biotech/AI-for-bio:** Isomorphic Labs · Recursion · insitro · Ginkgo · Arc Institute.
- **Space:** SpaceX · Blue Origin · JPL (NASA) · ESA.

---

## 2. Session waves
- **Session 14 ✅ (first wave) — 27 sources / 342 chunks → `frontier-rnd/` (all 0 FFFD).** Built `rss2txt.pl` + `rndfeed.sh`; hardened `chunk.sh` (3× hard-cap). **AI labs:** Google Research, Amazon Science, NVIDIA, Apple ML, Hugging Face, Meta Engineering, Berkeley BAIR (full-text), MIT CSAIL. **MIT News all-field full-text feeds (12):** AI, CSAIL, physics, biology, chemistry, neuroscience, energy, quantum-computing, materials-science, genetics, mathematics, climate. **Engineering:** IEEE Spectrum. **BCI ⭐:** Neuralink JMIR whitepaper + PRIME brochure. **Robotics/quantum snapshots:** Boston Dynamics, Waymo, Google Quantum AI, DeepMind (catalog snapshots). [Stanford-HAI dropped — SPA, no feed.]
- **Session 15+ — continue:** (a) **YouTube talk channels** one-at-a-time — Boston Dynamics, MIT, Stanford, IBM Research, NVIDIA, Microsoft Research, Neuralink, company keynote channels. (b) **More org feeds** — find working feeds/sitemaps for MSR, IBM, AI2, Anthropic (enumerate articles), OpenAI, Stanford HAI, CMU, national labs, Allen Institute, CERN, EMBL-EBI. (c) **NASA NTRS** — fetch public-domain report PDFs per field. (d) **Quantum/semiconductor/fusion/biotech/space** sectors (table above). (e) re-sweep session-14 feeds (they advance). Always: validate-live → `rndfeed.sh`/`getpdf.sh`/`ytchannel.sh` → 0-FFFD QC → tick this file.

> Each session: validate-live → managed collect → 0-FFFD QC → tick this file + [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) → refresh handoff → commit tracking md. **Multi-session; breadth across all institutions × all fields is the goal.**
