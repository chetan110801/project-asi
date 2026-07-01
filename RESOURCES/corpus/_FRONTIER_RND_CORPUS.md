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
| **Microsoft Research** | AI, all-science | ✅ B + V | blog feed ✅ + **YouTube `microsoft-research-youtube` 43** ✅ (diffusion theory, quantum sim, materials inverse-design, FHE, AI-reasoning, BCIs, health-AI) |
| **OpenAI** | AI | ✅ B | `openai.com/blog/rss.xml` ✅ (real RSS — supersedes sitemap-only) |
| **Anthropic** | AI safety | 🟡 (article prose partial) | research index reachable; ⬜ enumerate + fetch articles (rss.xml is SPA) |
| **IBM Research** | AI, quantum | 🟡 | blog RSS still SPA; **IBM Quantum/Qiskit Medium feed ✅** (`ibm-quantum-qiskit`); ⬜ IBM Research YouTube |
| **AI2 (Allen Inst. for AI)** | AI | ✅ B | `medium.com/feed/ai2-blog` ✅ (404 FIXED via Medium) |
| xAI · Cohere · Mistral · Stability · EleutherAI | AI | ⬜ | next sessions |

### ⭐ Agentic-Engineering & AI-lab official docs (session 17 — the "build & direct AI" / anti-vibe-coding corpus)
| Institution / project | Field | Status | Source captured |
|---|---|---|---|
| **Anthropic / Claude docs** | LLM API + agent SDK | ✅✅ | `anthropic-docs` 1734 (`docs.anthropic.com/llms-full.txt` 86.8 MB) + `anthropic-engineering` 11 (21 SSR /engineering/ articles: building-effective-agents, context-engineering, harnesses, evals, MCP) |
| **OpenAI docs + Agents SDK + guide** | LLM API + agents | ✅ | `openai-docs` 268 · `openai-agents-sdk-docs` 2 · `openai-agents-guide` 3 (Practical Guide PDF) |
| **xAI · Mistral · Gemini docs** | LLM APIs | ✅ | `xai-docs` 87 · `mistral-docs` 59 · `gemini-docs` 1 |
| **LangChain / LangGraph / LangSmith** | agent orchestration | ✅✅ | `langchain-docs` 415 (unified) · `langsmith-docs` 21 |
| **CrewAI · AutoGen · Semantic Kernel · MS Agent Framework** | multi-agent frameworks | ✅✅ | `crewai-docs` 126 · `autogen-docs` 43 (CC-BY) · `semantic-kernel-docs` 131 (MIT) · `microsoft-agent-framework-docs` 81 (MIT, ADRs) |
| **Google ADK · Pydantic-AI · Haystack · Agno · Letta · LlamaIndex · Mastra · smolagents · Strands · Cloudflare Agents** | agent frameworks | ✅ | ADK 159 · pydantic-ai 151 · haystack 120 · agno 334 · letta 55 · llamaindex 7 · mastra 2 · smolagents 20 · strands 124 · cloudflare-agents 131 |
| **MCP (Model Context Protocol)** | agent tool/context standard | ✅✅ | `mcp-docs` 137 (`modelcontextprotocol.io/llms-full.txt`) |
| **DSPy · Instructor · LiteLLM · Langfuse · Ragas** | prompt-opt / structured-output / gateway / observability / eval | ✅ | dspy 1 · instructor 1 · litellm 39 · langfuse 1 · ragas 2 |
| **Methodology: 12-Factor Agents · Spec-Kit (SDD) · Latent Space · Simon Willison · Chip Huyen** | agentic-eng discipline (vs vibe-coding) | ✅ | `twelve-factor-agents` 6 · `spec-kit-sdd` 23 · `latent-space-blog` 24 · `simon-willison-blog` 5 · `chip-huyen-blog` 17 · n8n 39 · dify 3 |

### Brain–Computer Interface — companies (⭐ learner-named)
| **Neuralink** | BCI / neurotech | ✅ P + R + V | JMIR 2019 whitepaper ✅ + PRIME brochure ✅ + **YouTube `neuralink-youtube` 14** ✅ (Summer-2025 / July-2024 update talks — the SPA updates recovered via YouTube) |
| Synchron · Blackrock Neurotech · Precision Neuro · Kernel | BCI | ⬜ | open papers / press; next sessions |

### Robotics / autonomy — companies
| **Boston Dynamics** | legged/humanoid robotics | ✅ B + V | blog catalog snapshot ✅ + **YouTube `boston-dynamics-youtube` 36** ✅ (humanoid tech-talks/webinars + Inside-the-Lab Atlas + RL behaviour) |
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
| **NASA** (NTRS) | aerospace, space, AI, materials | ✅✅ R | **19 public-domain report PDFs** (6 session-14 + **13 session-16**): + ML-aircraft-engine-design · composite-virtual-testing · electric-propulsion-AEPS · CFD-survey · astrobiology+AI · ECLSS · quantum-sensing · autonomous-ops · nuclear-propulsion · optical-comms · Mars-rover-autonomy · ISRU · airspace-autonomy. (search-API → resolve real `downloads/<file>.pdf`) |
| **LBNL** (Berkeley Lab, DOE) | physics/energy/bio | ✅ B | `newscenter.lbl.gov/feed/` ✅ |
| **EMBL** (mol. biology) | biology/genomics | ✅ B | `embl.org/news/feed/` ✅ |
| **Fermilab** (DOE) | particle physics | ✅ B | `news.fnal.gov/feed/` ✅ |
| **DARPA** | defense R&D, all | ✅ B | `darpa.mil/rss/news.xml` ✅ (404 FIXED) |
| **NIST** | metrology/standards/QIS | ✅ B | `nist.gov/news-events/news/rss.xml` ✅ |
| **Sandia National Labs** (DOE) | energy/HW/security | ✅ B | `newsreleases.sandia.gov/feed/` ✅ |
| **NASA** (JPL + main) | space/aero/Earth | ✅ B | `jpl.nasa.gov/feeds/news/` + `nasa.gov/feed/` ✅ (NTRS PDFs also held) |
| **ESA** | space | ✅ B | `esa.int/rssfeed/Our_Activities/Space_News` ✅ |
| **Broad Institute** | genomics/biomedicine | ✅ B | `broadinstitute.org/rss.xml` ✅ |
| **Argonne** (DOE) | computing/materials/physics | ✅ B | `anl.gov/rss.xml` ✅ (`argonne-news`) |
| **ORNL** (DOE) | materials/computing/neutron/nuclear | ✅ B | `ornl.gov/rss.xml` ✅ (`ornl-news`) |
| **SLAC** (DOE/Stanford) | particle physics/X-ray/cryo-EM | ✅ B | `www6.slac.stanford.edu/rss.xml` ✅ (`slac-news`) |
| **Jefferson Lab** (DOE) | nuclear physics/accelerator | ✅ B | `jlab.org/rss.xml` ✅ (`jefferson-lab-news`) |
| **HHMI Janelia** | neuro/imaging/bio-eng | ✅ B | `janelia.org/rss.xml` ✅ (`janelia-hhmi-news`) |
| **Cold Spring Harbor** | genomics/neuro/cancer | ✅ B | `cshl.edu/feed/` ✅ (`cold-spring-harbor-news`) |
| **Intel** | semiconductors/AI accel | ✅ B | `newsroom.intel.com/feed` ✅ (`intel-newsroom`) |
| **Together AI** | open ML / systems | ✅ B | `together.ai/blog/rss.xml` ✅ (`together-ai-blog`) |
| Allen Institute (Brain) · EMBL-EBI · CERN · LLNL/NREL/PNNL/BNL/LANL · NIH/NCBI · Santa Fe Inst. | many | ⬜ | still SPA/404 to curl (session-16 confirmed) → route via sitemap or YouTube |

### Other frontier sectors (next sessions)
- **Quantum HW:** **IBM Quantum/Qiskit ✅** (`ibm-quantum-qiskit`) · IonQ · Quantinuum · PsiQuantum · Rigetti (all SPA — route via arXiv/YouTube).
- **Semiconductors/compute:** **ARM ✅** (`arm-newsroom`) · TSMC · Intel · AMD · Cerebras · Groq · Tenstorrent (SPA — route via newsroom RSS where they exist).
- **Fusion/energy:** Commonwealth Fusion · Helion · TAE · ITER (`whatsnew/rss` = THIN index) · NREL (feed empty).
- **Biotech/AI-for-bio:** Isomorphic Labs · Recursion · insitro · Ginkgo · Arc Institute.
- **Space:** SpaceX · Blue Origin · JPL (NASA) · ESA.

---

## 2. Session waves
- **Session 17 ✅ (⭐ AI-lab official docs + END-TO-END AGENTIC-ENGINEERING corpus) — learner redirected mid-session** to *"current official SOTA docs + all info from LangChain/LangGraph/LangSmith/AutoGen/etc. + all available in-depth on end-to-end agentic engineering — the dynamic Agentic-Engineering system-design discipline replacing 'vibe-coding' trending online."* Delivered as a large clean docs wave: **38 NEW folders · 4,386 verbatim chunks · ALL 0 FFFD · 0 oversized** (`frontier-rnd/` now **118 folders / 163 MB**, was 80). **(A) AI-lab official docs (5):** Anthropic `anthropic-docs` **1734** (⭐ 86.8 MB `docs.anthropic.com/llms-full.txt`) · OpenAI `openai-docs` 268 · xAI `xai-docs` 87 · Mistral `mistral-docs` 59 · Gemini `gemini-docs` 1. **(B) LLM/agent-framework docs (16, llms.txt/llms-full.txt):** LangChain (unified w/ LangGraph+LangSmith) `langchain-docs` 415 · LangSmith 21 · CrewAI 126 · Haystack 120 · Pydantic-AI 151 · Google-ADK 159 · Letta 55 · LlamaIndex 7 · LiteLLM 39 · Agno 334 · MCP 137 · DSPy 1 · OpenAI-Agents-SDK 2 · Mastra 2 · Instructor 1 · Weaviate 3. **(C) Microsoft agent frameworks (3, official GitHub docs repos → raw .md/.ipynb):** Semantic-Kernel `semantic-kernel-docs` 131 (MIT) · MS-Agent-Framework `microsoft-agent-framework-docs` 81 (MIT; ADR design-decisions) · AutoGen `autogen-docs` 43 (CC-BY-4.0; notebooks via `ipynb2txt.py`). **(D) Agentic-engineering METHODOLOGY canon (anti-vibe-coding, 7):** OpenAI "Practical Guide to Building Agents" `openai-agents-guide` 3 · Anthropic Engineering blog `anthropic-engineering` 11 (21 SSR /engineering/ articles de-chromed — building-effective-agents, context-engineering, writing-tools-for-agents, harnesses, evals, multi-agent-research, Claude-Code-best-practices — NOT in product docs) · 12-Factor-Agents `twelve-factor-agents` 6 · GitHub Spec-Kit / Spec-Driven-Development `spec-kit-sdd` 23 (MIT) · Latent-Space `latent-space-blog` 24 · Simon-Willison `simon-willison-blog` 5 · Chip-Huyen `chip-huyen-blog` 17. **(E) Agentic infra / observability / eval + platforms (7):** AWS Strands `strands-agents-docs` 124 · Cloudflare Agents `cloudflare-agents-docs` 131 · HF smolagents 20 · n8n 39 · Dify 3 · Langfuse 1 · Ragas 2. **(F) RAG / vector-DB retrieval+memory infra (5):** Chroma `chroma-docs` 57 · Qdrant `qdrant-docs` 147 · Pinecone `pinecone-docs` 3 · Milvus `milvus-docs` 3 · HF AI-Agents-Course `hf-agents-course` 1. *(Grand session total: **43 folders / 4,597 chunks**; `frontier-rnd/` now **123 folders**. Google "Agents"/"Agents Companion" whitepapers = Kaggle-gated SPA → `REQUESTS.md`.)* **TOOLS BUILT (scratchpad):** `gettext.sh` (llms.txt fetcher) · `ghfetch.sh` (GitHub raw md/ipynb → fetch-all-then-concat-in-ONE-redirect = lock-safe → chunk) · `ipynb2txt.py` · `htmlpages.sh` (SSR page set → de-chrome → chunk). **GOTCHAS:** (1) Windows append-lock recurs on rapid `>>` → Phase-1 fetch-all, Phase-2 single-redirect concat. (2) minified `llms.txt` (LangSmith) → fold long lines (`perl -pe 's/(.{800,}?) /$1\n/g'`) before chunking. (3) AutoGen/Semantic-Kernel have no llms.txt → official GitHub docs repos. (4) Anthropic engineering blog is SSR & separate from `docs.anthropic.com` → enumerate sitemap `/engineering/`. (5) Google "Agents" whitepaper Kaggle-gated → REQUESTS. **⏭ STILL OPEN (from session-16 defer):** NVIDIA/IBM-Research YouTube · Y Combinator (YouTube+YC-Library+Paul-Graham) · full Lex + podcast wave.
- **Session 16 ✅ (YouTube talk-channels + NASA-NTRS-per-field + bonus org feeds) — did the two session-15 DEFERRED items first, then bonus feeds.** All 0 FFFD; YouTube pulled **one channel at a time** (no 429 storms; a couple of long-talk 100 s socket timeouts self-recovered on the 60 s retry). **(a) YouTube talk channels → NEW `frontier-rnd/<org>-youtube/` folders:** **Neuralink** `neuralink-youtube` **14** (⭐ learner-named — Summer-2025 update 1379 lines, July-2024 update 1413, Overview Fall-2025 635; filter ≥140 s) · **Boston Dynamics** `boston-dynamics-youtube` **36** (3 humanoid tech-talks/webinars: Why-Humanoids-Future-of-Manufacturing 1351 lines, Humanoid-Mission-in-Manufacturing 1075, Form-&-Function-of-Enterprise-Humanoid 895; + Inside-the-Lab Atlas series, RL-behaviour Air-Spot/Stepping-Up; filter ≥240 s, music-only demos skipped as no-caption) · **Microsoft Research** `microsoft-research-youtube` **43** (recent 20–90 min focused research talks: generative-diffusion theory, flow-matching/RL policies, quantum simulation/wavefunction-flows, materials inverse-design, molecular generative models, FHE/CKKS/CROSS, AI-reasoning, multi-agent geospatial, BCIs, healthcare-AI). **(b) NASA NTRS — 13 NEW public-domain report PDFs / 35 chunks** (search-API → resolve real `downloads/<file>.pdf` link, many have descriptive filenames not `<id>.pdf`): ML-aircraft-engine-design · composite-virtual-testing · electric-propulsion-AEPS `6` · CFD-progress-survey · **astrobiology+AI (Scharf 2026)** · ECLSS-overview · **quantum-sensing (2025)** `5` · autonomous-operations · nuclear-propulsion-101 · optical-comms (GEO-relay; swapped an image-scan for the digital-native copy) · Mars-rover-autonomy · ISRU-living-off-the-land · resilient-airspace-autonomy. (`nasa-ntrs-*` now 19 folders.) **(c) BONUS org feeds — 8 NEW / 26 chunks** (probed for real RSS/Atom, not SPA shells): **Argonne** `argonne-news` `2` · **ORNL** `ornl-news` `6` · **SLAC** `slac-news` `7` · **Jefferson Lab** `jefferson-lab-news` `4` · **Intel newsroom** `intel-newsroom` `1` (semiconductor) · **HHMI Janelia** `janelia-hhmi-news` `1` · **Cold Spring Harbor** `cold-spring-harbor-news` `2` · **Together AI** `together-ai-blog` `3`. **`frontier-rnd/` now 80 folders** (was 56). **⏭ DEFERRED to next session (learner added mid-session):** (1) **NVIDIA Developer + IBM Research** YouTube channels (one-at-a-time). (2) **Scrape the top AI-lab official sites + docs** (OpenAI/Anthropic/DeepMind/Meta/Mistral/xAI…) — TESTED PATHS: Anthropic **`docs.anthropic.com/llms-full.txt` = 86.8 MB whole-docs markdown** (+ `docs.claude.com` mirror; 202 KB `llms.txt` index) · xAI `docs.x.ai/llms.txt` = 1.23 MB · OpenAI `developers.openai.com/llms.txt` = 90 KB (index → follow) · Gemini `ai.google.dev/gemini-api/docs/llms.txt` = 27 KB · Mistral `docs.mistral.ai/llms.txt` = 14 KB · Cohere stub only. Live sitemaps: `openai.com/sitemap.xml` (3 KB, index→sub-sitemaps), `anthropic.com/sitemap.xml` (63 KB), `deepmind.google/sitemap.xml` (81 KB), `x.ai/sitemap.xml` (16 KB); Meta/Mistral root sitemap 404 → find sub-path. (3) **Y Combinator** — YouTube channel/playlists (Startup School, How-to-Start-a-Startup, founder talks) + YC Library essays + Paul Graham essays. (4) **Rich AI/eng/science podcasts** — full **Lex Fridman** channel curated to AI/sci/eng guests (7 specific eps already held) + MLST (down-payment 50 eps started this session → `transcripts/machine-learning-street-talk/`) + No-Priors / Latent-Space / Cognitive-Revolution / 80k-Hours / TWIML / Mindscape / Huberman / Robot-Brains / AXRP / a16z.
- **Session 15 ✅ (org-feed wave) — 21 feeds / 295 chunks → `frontier-rnd/` (all 0 FFFD; `frontier-rnd/` now 56 folders).** Re-probed every SPA-miss + new candidates with the research UA; collected the confirmed RSS/Atom feeds via `rndfeed.sh` (curl, sequential). **AI labs (5):** Microsoft Research (`microsoft-research-blog` — the 403/000 miss is FIXED with UA, 7), OpenAI (`openai-blog`, 26 — real RSS, supersedes the sitemap-only note), Google DeepMind (`deepmind-blog-rss`, 3 — real full RSS, supersedes the `deepmind-blog-index` snapshot), EleutherAI (`eleuther-ai-blog`, 2), **AI2 / Allen Institute for AI** (`ai2-allen-ai-blog` via Medium feed, 4 — the 404 is FIXED). **Semiconductor/quantum/fusion:** ARM newsroom (4), IBM Quantum/Qiskit (Medium, 7); ITER `whatsnew/rss` = index-only THIN, skipped. **Biotech/space:** Broad Institute (6), ESA Space News (1), NASA JPL (3), NASA main (5). **National labs/gov:** Fermilab (2), DARPA (1 — the feed 404 is FIXED: `darpa.mil/rss/news.xml`), NIST (2), Sandia (5). **Universities/institutes:** Stanford (1), CMU (20), UC Berkeley (1), Caltech (Atom, 5), **Vector Institute** (189 — full-text feed, 270 unique articles verified no-dup); Princeton-Engineering = empty-parse, skipped. **Science press:** Quanta Magazine (1, summary feed — like IEEE Spectrum, a frontier-science publication). **Still SPA/no-feed (route via YouTube/sitemap/PDF next):** IBM Research blog, Anthropic, Cohere, ORNL, LLNL, Argonne, CERN, Allen Institute (brain), EMBL-EBI, IonQ, Quantinuum, Rigetti, Cerebras, Groq, PsiQuantum, Ginkgo, Arc Institute, Blue Origin, PNNL, SLAC, BNL, ETH-Zürich, Oxford, Mila, NREL (empty). **⚠️ carry-forward gotcha:** a few WordPress/Medium feeds leak em-dash mojibake (`â` for `—`) — FFFD=0, prose & grep intact; `norm.pl` ASCII-folds smart quotes but not this double-encoded `â€"` sequence — add a fold rule next session if worth it. **DEFERRED to next session (learner paused to shut down mid-wave):** NASA NTRS report PDFs (more fields) + the YouTube talk-channel pulls (Boston Dynamics / IBM Research / MSR / NVIDIA / Neuralink — one-at-a-time).
- **Session 14 ✅ (first wave) — 35 sources / 364 chunks → `frontier-rnd/` (all 0 FFFD).** Built `rss2txt.pl` + `rndfeed.sh`; hardened `chunk.sh` (3× hard-cap). **AI labs:** Google Research, Amazon Science, NVIDIA, Apple ML, Hugging Face, Meta Engineering, Berkeley BAIR (full-text), MIT CSAIL. **MIT News all-field full-text feeds (12):** AI, CSAIL, physics, biology, chemistry, neuroscience, energy, quantum-computing, materials-science, genetics, mathematics, climate. **Engineering:** IEEE Spectrum. **BCI ⭐:** Neuralink JMIR whitepaper + PRIME brochure. **Robotics/quantum snapshots:** Boston Dynamics, Waymo, Google Quantum AI, DeepMind (catalog snapshots). **Orgs/gov:** NASA NTRS (6 public-domain report PDFs across fields), LBNL (Berkeley Lab), EMBL. [Stanford-HAI/Allen-Institute dropped — SPA/404, no feed.]
- **Session 16+ — continue (Session-15 feed wave done above):** (a) **YouTube talk channels** one-at-a-time — Boston Dynamics, MIT, Stanford, IBM Research, NVIDIA, Microsoft Research, Neuralink, company keynote channels. (b) **More org feeds** — find working feeds/sitemaps for MSR, IBM, AI2, Anthropic (enumerate articles), OpenAI, Stanford HAI, CMU, national labs, Allen Institute, CERN, EMBL-EBI. (c) **NASA NTRS** — fetch public-domain report PDFs per field. (d) **Quantum/semiconductor/fusion/biotech/space** sectors (table above). (e) re-sweep session-14 feeds (they advance). Always: validate-live → `rndfeed.sh`/`getpdf.sh`/`ytchannel.sh` → 0-FFFD QC → tick this file.

> Each session: validate-live → managed collect → 0-FFFD QC → tick this file + [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) → refresh handoff → commit tracking md. **Multi-session; breadth across all institutions × all fields is the goal.**
