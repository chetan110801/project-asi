# Corpus Widening Campaign — optimal multi-session plan
**The forward plan for the next several gathering sessions.** Two parallel streams the learner set on 2026-06-30: **(1)** collect a named set of top-university YouTube channels/courses, and **(2)** pull a **huge breadth of free, rich textbooks across every domain of science** — selected for *how each domain pushes the progress of AGI/ASI*. Binding scope/durability/legality rules: [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §1–§2 · acquisition layer: [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) · method: [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) · status board: [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md).

`Status: Living plan · Created 2026-06-30 (session 7) · supersedes the ad-hoc "next session" notes in the handoff`

---

## 0. Governing rules (apply every session — do not relax)
1. **Durability filter (HARD_RULES §2):** collect the **timeless principle / the reason-and-objective behind a thing**, not transient specifics. For this campaign that means: for each science, gather the *foundations + the principles AI is now using or accelerating* — **how the field pushes AGI** — and skip pure humanities/history/literature that doesn't bear on building or directing intelligence.
2. **Anti-redundancy:** skip anything already in the corpus (`corpus/textbooks/_LIBRARY_INDEX.txt` for owned books; the course/coverage tables for transcripts). Don't re-take a saturated domain (AI/ML/DL/RL/NLP/CV lectures) just for an institution badge — that was the rule that (correctly) cut NPTEL-DL and dup editions in sessions 5–6.
3. **Legality absolute:** only **open-licensed / author-free / CC / public-domain / arXiv / gov / course-public** text. OpenStax & LibreTexts are CC-BY/CC-BY-SA → fine. Paywalled-not-owned → [`../REQUESTS.md`](../REQUESTS.md), never scrape.
4. **Validate before queueing:** HEAD-check each URL live; for playlists print `count + first title` before collecting. Verify arXiv IDs vs the API.
5. **Polite pacing:** YouTube in **managed queues, one playlist at a time**, base sleep ≥2.6 s, 429-on-retry leaves the video unmarked (resumable). Books: `pdftotext` + `chunk.sh`, no rate issue.
6. **Git:** all corpus **text stays git-ignored**; only the tracking markdown is committed. Tick [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) + the relevant worklist every session; refresh the handoff; commit; tell the learner to continue in a new session.
7. **Still gathering — do NOT write/reground modules** until the learner explicitly calls the corpus rich enough (memory `corpus-collection-continues`; HARD_RULES gate).

---

## 1. STREAM 1 — the named YouTube channels/courses (validated 2026-06-30)
The learner named these to collect "over the next few sessions." All probed live this session; the durable, non-redundant picks are tabled below with **validated playlist IDs**. Channels are large — collect the **science/foundations courses**, skip humanities-history-literature (durability filter) and anything already held.

### 1a. Open Yale Courses (`@YaleCourses`) — **richest new channel; full-lecture series.** Session-8 target.
Famous complete courses across the exact science spread the learner wants. Picks (all validated live, full-lecture):
| Course | Playlist ID | ~Lec | Domain → AGI relevance |
|---|---|---|---|
| Fundamentals of Physics I (Shankar) | `PLFE3074A4CB751B2B` | ~24 | physics substrate |
| Fundamentals of Physics II (Shankar) | `PLD07B2225BB40E582` | ~25 | E&M, QM intro |
| Freshman Organic Chemistry I (McBride) | `PL3F629F73640F831D` | ~37 | **chemistry (under-served)** |
| Freshman Organic Chemistry II (McBride) | `PLB572BA3ED0F700F1` | ~38 | chemistry / AI-for-chem |
| Frontiers/Controversies in Astrophysics (Bailyn) | `PLD1515420F4E601A4` | ~24 | astronomy / AI-for-astro |
| Evolution, Ecology & Behavior (Stearns) | `PL6299F3195349CCDA` | ~36 | evolution, selection, fitness |
| Atmosphere, Ocean & Environmental Change (Smith) | `PL902AF247F4163F61` | ~36 | **earth/climate (under-served)** |
| Game Theory (Polak) | `PL6EF60E1027E1A10B` | ~24 | multi-agent, mechanism design |
| Financial Markets (Shiller, 2011) | `PL8FB14A2200B87185` | ~24 | economics of tech/AI |
| Financial Theory (Geanakoplos) | `PLEDC55106E0BA18FC` | ~26 | economics, equilibrium |
| Introduction to Psychology (Bloom) | `PL6A08EB4EEFF3E91F` | ~20 | cognitive science |
| Philosophy & the Science of Human Nature (Gendler) | `PL3F6BC200B2930084` | ~25 | cog-sci / value |
| Introduction to Political Philosophy (Smith) | `PL8D95DEA9B7DFE825` | ~24 | governance / value-alignment |
| The Moral Foundations of Politics (Shapiro) | `PL2FD48CE33DFBEA7E` | ~24 | ethics → AI alignment |
| Death (Shelly Kagan) | `PLEA18FAF1AD9047B0` | ~26 | philosophy of mind/personhood |
| Frontiers of Biomedical Engineering (Saltzman) | `PL27E877E8206F196B` | ~24 | bioengineering |
| Global Problems of Population Growth (Wyman) | `PLE60A08636F41C128` | ~24 | biology/society |
| Yale QI — Quantum Error Correction | `PLh9mgdi4rNewrbMExcT-dzW-tH2mjkagq` | ~? | **quantum (QEC, additive)** |
> **Skip (not science / durability-fail):** Dante, Milton, Don Quixote, Hemingway, Roman Architecture, Old Testament/New Testament, Civil War, medieval/modern European history, Modern Poetry, Listening to Music, literature theory. (~40 of Yale's 81 playlists.)

### 1b. The 4 learner-named playlists (validated). Fold into session-8/10.
| Playlist | ID | Count | Pick? |
|---|---|---|---|
| Stanford — **Human Behavioral Biology** (Sapolsky) | `PLtdr2qSB8H94jFZJUwk99gPgK2Utv8RR1` | 22 | ✅ neuro/behavior — superb |
| Harvard — **Justice** (Sandel) | `PL72C62342291D5DAE` | 12 | ✅ ethics → governance |
| Harvard — **CS50x 2026 Lectures** | `PLhQjrBD2T380hlTqAU8HfvVepCcjCqTg6` | 13 | ◐ intro-CS (lower priority; CS50-AI already held) |
| Harvard — **CS50's Fundamentals of AI 2025** | `PLJPcEQXX4i60VGmCvt1TZsprC7IGdHMpn` | 9 | ✅ fresh 2025 AI intro |

### 1c. `@mitocw`, `@stanfordonline`, `@stanford`, `@harvard` — /courses + /playlists deep-scan. Session-9/10.
- **MIT OCW** (`@mitocw`): 354+ playlists scanned before; only a slice taken. **Next, mine the untaken durable courses in NEW domains:** chemistry (5.111/5.112 Principles of Chemical Science, 5.60 Thermodynamics & Kinetics), earth/climate (12.x), materials (3.091 Solid-State Chemistry, 3.012), astro/physics (8.02, 8.224 Exploring Black Holes), more bio (7.06 Cell Bio, 7.05 Biochem), genetics. Skip the saturated AI/ML/DL/math-we-have.
- **Stanford Online** (`@stanfordonline`) **/courses** tab: structured-course view — re-scan to catch any non-AI course missed (most AI/ML already held; look for stats/optimization/healthcare not yet taken).
- **`@stanford`** (flagship, distinct from stanfordonline) **/courses + /playlists**: scan live; pick durable science not already held.
- **`@harvard`** (flagship) **/courses + /playlists**: scan live; durable science/stat/ethics picks (e.g., Stat 110 already held via Blitzstein's own channel; look for new).
> Method for /courses + /playlists scan: `yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/@<chan>/playlists"` → grep for the target domains → validate each candidate (`count + first title`) → queue. Expect many dups with what's held; the durability+anti-redundancy filter does the cutting.

---

## 2. STREAM 2 — the all-science free-textbook push ("how each domain pushes AGI")
The big new directive: **gather a huge, rich set of free textbooks across every domain of science.** The corpus already holds the owned 12 GB library + the AI/ML free-textbook spine; this stream **systematically adds the open, CC-licensed science textbooks** not yet held, domain by domain, foundations → frontier, always asking *what timeless principles of this field a builder/director of AGI relies on, and where AI is now accelerating it.*

**Primary legally-free book sources (all open-license, bulk-downloadable):**
- ★ **OpenStax** (openstax.org) — CC-BY peer-reviewed PDFs, full catalog (physics, chem, bio, astronomy, calculus, statistics, psychology, economics, …). **Cleanest win.**
- ★ **LibreTexts** (libretexts.org) — vast CC library; fills domains OpenStax lacks (geosciences, oceanography, advanced chem).
- **Open Textbook Library** (open.umn.edu/opentextbooks) — curated open books across fields.
- **Author-free PDFs** (already used: MML, Boyd, ISL/ESL, MacKay, Murphy PML 1+2…) — extend per domain.
- **arXiv monographs / open lecture-note books** (Tong, introtcs, Watrous, Tedrake, LaValle — already held; extend).
- **Public-domain classics** (archive.org, Project Gutenberg) — the foundational primary texts (Darwin, Turing 1950, Shannon 1948 [held], etc.) for the *origin of the principle*.

> **Always:** check `corpus/textbooks/_LIBRARY_INDEX.txt` first (skip owned). `pdftotext -layout` → `chunk.sh` → `corpus/<domain>/<slug>/`. Tick coverage.

### Domain checklist (target free books; ✅=likely already held, ⬜=fetch)
| Domain | AGI-relevance hook | Target free books |
|---|---|---|
| **Physics** | energy/compute limits, world-models, simulation | OpenStax **University Physics Vol 1–3** ⬜; ✅Feynman (selections), Tong notes |
| **Chemistry** | AI-for-chemistry, reactions, drug/material discovery | OpenStax **Chemistry 2e** ⬜, **Atoms First** ⬜, **Organic Chemistry** ⬜; LibreTexts physical-chem ⬜ |
| **Biology** | brain blueprint, evolution, self-organization, AI-for-bio | ✅OpenStax Biology 2e; **Concepts of Biology** ⬜, **Microbiology** ⬜, **Anatomy & Physiology** ⬜; ✅Kandel neuro set |
| **Astronomy / cosmology** | scale, AI-for-astro, data-driven discovery | OpenStax **Astronomy 2e** ⬜ |
| **Earth / climate science** | AI weather/climate (GraphCast etc.), complex systems | LibreTexts **Geology / Oceanography / Atmospheric science** ⬜ |
| **Mathematics** | foundations of learning/optimization/inference | ✅MML, ISL, ESL, MacKay, Boyd; add OpenStax **Calculus 1–3** ⬜, **Statistics** ⬜; Hefferon **Linear Algebra** ⬜, OpenIntro **Statistics** ⬜ |
| **Statistics / probability** | the inference engine of ML | OpenIntro Stats ⬜; ✅Blitzstein, Murphy; StatQuest (collected this session) |
| **Computer science / theory** | the substrate (saturated — selective) | ✅introtcs, Arora-Barak, Goodfellow, d2l, …; add only gaps |
| **Materials science** | AI-for-materials (GNoME, MatterGen) | LibreTexts **Materials** ⬜; MIT 3.091 transcripts (Stream 1) |
| **Economics** | AI & work, mechanism design, growth | OpenStax **Principles of Economics 3e / Micro / Macro** ⬜; ✅Acemoglu, Brynjolfsson papers |
| **Cognitive science / psychology** | minds, learning, reasoning | OpenStax **Psychology 2e** ⬜; ✅probmods, SEP, Lake |
| **Neuroscience** | architecture of intelligence | ✅Kandel, Gerstner, CompCogNeuro; add Neuromatch notes ⬜ |
| **Complex systems** | emergence, networks, self-organization | ✅Newman; Santa Fe Complexity Explorer notes ⬜ |
| **Quantum** | quantum computing/error-correction, QML | ✅Watrous, Quantum Country; Yale QEC (Stream 1); Nielsen-Chuang → REQUESTS |
| **Engineering / control / robotics** | embodiment | ✅Tedrake, Lynch-Park, LaValle, Brunton, Siciliano |
| **AI-for-Science (the synthesis)** | the through-line of the whole campaign | survey/review monographs + ✅PAPERS.md D12 set |

---

## 3. The session sequence (optimal order)
Leverage × AGI-relevance, richest-new-source first, books interleaved so a science domain gets *lectures + textbook* together.

- **Session 7 (this one) ✅** — toolchain rebuilt; **6 additive courses collected** (18.337 Scientific-ML 25, Oxford Info-Theory 8 / Prob-Measure-Martingales 5 / Functional-Analysis 3, StatQuest Statistics-Fundamentals 62 + Maximum-Likelihood 6); this campaign plan written; new targets validated + catalogued.
- **Session 8 — Open Yale Courses (Stream 1a) + the 4 named playlists (1b).** Managed queues; the ~16 science picks + Sapolsky/Sandel/CS50-AI. *Biggest single new-coverage jump.*
- **Session 9 — Books wave 1 (Stream 2): OpenStax physical-sciences & math** — University Physics 1–3, Chemistry 2e + Atoms First + Organic, Astronomy 2e, Calculus 1–3, Statistics. Extract→chunk→`corpus/<domain>/`. Pairs with Yale physics/chem/astro from session 8.
- **Session 10 — `@mitocw` + `@stanford` + `@harvard` /courses-tab deep-scan (Stream 1c)** — mine untaken durable courses in chemistry/materials/earth/bio; collect. + CS50x if wanted.
- **Session 11 — Books wave 2 (Stream 2): OpenStax life/social-sciences + LibreTexts gap-fill** — Concepts of Bio, Microbiology, Anatomy, Psychology 2e, Principles of Economics/Micro/Macro; LibreTexts geosciences/oceanography/materials; OpenIntro Stats, Hefferon LinAlg.
- **Session 12 — Books wave 3 + frontier monographs** — per-domain open lecture-note books + AI-for-Science review monographs + public-domain primary classics (Darwin, Turing 1950, etc.); OCR the 3 image-only scans.
- **Session 13+ — residual widening + verification** — any remaining validated playlists; arXiv-ID verification sweep; then **pause for the learner's "rich enough" call** → first grounded module rewrite (1300 LLMs).

> Each session: validate-live → managed collect/extract → tick [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) → refresh handoff → commit tracking md. Take as many sessions as needed; depth + breadth beat speed.
