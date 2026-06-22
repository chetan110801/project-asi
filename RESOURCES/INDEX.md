# RESOURCE LIBRARY — index (by domain)
**Curated, *validated* entry-point resources** — university open-courseware and canonical open textbooks, not random explainers. Each carries a stable `id` used by learning modules. We curate the *best* per domain, not "everything" (the giant-unread-library trap is in [`../INSTRUCTIONS/RESOURCE_COLLECTION_SYSTEM.md`](../INSTRUCTIONS/RESOURCE_COLLECTION_SYSTEM.md) §1).

`Status: Living catalog · System Version: 1.7 · Last updated: 2026-06-22`

> 📄 **Research papers, blogs & explainers** (landmark → SOTA, lab hubs like DeepMind/OpenAI/Anthropic) have their own catalog: [`PAPERS.md`](PAPERS.md).
> 🗺️ **The AGI/ASI landscape** (who's pursuing it, and via which bets — labs, startups, research paths): [`LANDSCAPE.md`](LANDSCAPE.md).
>
> **Validation:** I checked these against their official sources rather than taking them at face value (per the learner's instruction). Legend:
> ✅ = official source web-verified, free/open · 🎥 = validated free lecture series · 🟢? = known-canonical, **link to be re-verified** · 📘 = canonical book, **need to obtain** (paywalled → [`REQUESTS.md`](REQUESTS.md)) · 📕 = **local copy held** in [`library/`](library/) (curated & content-verified 2026-06-22 — see [`library/CURATION_VERDICTS.md`](library/CURATION_VERDICTS.md)).
> Where videos are restricted to enrolled students, the slides/notes are usually still public — noted per item.

---

## 30 · Math & theory (the language everything is written in)
| id | Resource | Source | Access |
|---|---|---|---|
| `r-3b1b` | Essence of Linear Algebra / Calculus / Neural Nets — 3Blue1Brown | [3blue1brown.com](https://www.3blue1brown.com/) | 🎥 ✅ free |
| `r-mit-1806` | 18.06 Linear Algebra — Gilbert Strang | [MIT OCW](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | ✅ free (video+notes) |
| `r-mml` | Mathematics for Machine Learning — Deisenroth, Faisal, Ong | [mml-book.github.io](https://mml-book.github.io/) | ✅ free PDF · 📕 local |
| `r-mackay-itila` | Information Theory, Inference & Learning Algorithms — MacKay | [inference.org.uk](https://www.inference.org.uk/itila/) | ✅ free to read |
| `r-boyd-cvx` | Convex Optimization — Boyd & Vandenberghe | [stanford.edu/~boyd](https://web.stanford.edu/~boyd/cvxbook/) | 🟢? free PDF · 📕 local |
| `r-strang-calc` | Calculus — Gilbert Strang | (Wellesley-Cambridge) | 📕 local copy |
| `r-essential-math-ai` | Essential Math for AI — Hala Nelson | (O'Reilly) | 📕 local copy |
| `r-esl` | The Elements of Statistical Learning (2e) — Hastie, Tibshirani, Friedman | [hastie su](https://hastie.su.domains/ElemStatLearn/) | ✅ free PDF · 📕 local |
| `r-isl` | An Introduction to Statistical Learning (ISLP, Python ed.) — James et al. | [statlearning.com](https://www.statlearning.com/) | ✅ free PDF · 📕 local |
| `r-bertsekas-prob` | Introduction to Probability — Bertsekas & Tsitsiklis | (MIT / Athena Scientific) | 📕 local copy |

## 20 · Machine intelligence (ML, deep learning, RL, LLMs)
| id | Resource | Source | Access |
|---|---|---|---|
| `r-cs229` | CS229 Machine Learning — Stanford (Ng et al.) | [cs229.stanford.edu](https://cs229.stanford.edu/) | 🟢? notes public |
| `r-d2l` | Dive into Deep Learning — Zhang et al. (interactive, code) | [d2l.ai](https://d2l.ai/) | ✅ free |
| `r-nielsen-nndl` | Neural Networks and Deep Learning — Nielsen | [neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com/) | ✅ free |
| `r-goodfellow-dl` | Deep Learning — Goodfellow, Bengio, Courville | [deeplearningbook.org](https://www.deeplearningbook.org/) | ✅ free (read) · 📕 local |
| `r-bishop-dl` | Deep Learning: Foundations & Concepts — Bishop & Bishop (2023) | (Springer) | 📕 local copy |
| `r-prince-udl` | Understanding Deep Learning — Prince (2024) | [udlbook.com](https://udlbook.com/) | ✅ free PDF · 📕 local |
| `r-bishop-prml` | Pattern Recognition & Machine Learning — Bishop (2006) | (Springer, now free) | 📕 local copy |
| `r-geron-homl` | Hands-On Machine Learning (3e) — Géron | (O'Reilly) | 📕 local copy |
| `r-raschka-ml` | ML with PyTorch & Scikit-Learn — Raschka | (Packt) | 📕 local copy |
| `r-huyen-dmls` | Designing Machine Learning Systems — Huyen | (O'Reilly) | 📕 local copy |
| `r-huyen-aie` | AI Engineering: Building Apps with Foundation Models — Huyen (2025) | (O'Reilly) | 📕 local copy |
| `r-handson-llm` | Hands-On Large Language Models — Alammar & Grootendorst | (O'Reilly) | 📕 local copy |
| `r-nlp-transformers` | NLP with Transformers — Tunstall, von Werra, Wolf | (O'Reilly) | 📕 local copy |
| `r-ng-mly` | Machine Learning Yearning — Andrew Ng | [mlyearning.org](https://www.mlyearning.org/) | 🟢? free · 📕 local |
| `r-grokking-drl` | Grokking Deep Reinforcement Learning — Morales | (Manning) | 📕 local copy |
| `r-bandit` | Bandit Algorithms — Lattimore & Szepesvári | [tor-lattimore.com](https://tor-lattimore.com/downloads/book/book.pdf) | ✅ free PDF · 📕 local |
| `r-raieli-agents` | Building AI Agents with LLMs, RAG & Knowledge Graphs — Raieli (2025) | (Packt) | 📕 local copy |
| `r-karpathy-zth` | Neural Networks: Zero to Hero (build GPT from scratch) — Karpathy | [karpathy.ai/zero-to-hero](https://karpathy.ai/zero-to-hero.html) | 🎥 ✅ free |
| `r-fastai` | Practical Deep Learning for Coders — fast.ai | [course.fast.ai](https://course.fast.ai/) | 🎥 🟢? free |
| `r-cs231n` | CS231n Vision/CNNs — Stanford | [cs231n.stanford.edu](https://cs231n.stanford.edu/) | 🟢? notes public |
| `r-cs224n` | CS224n NLP with Deep Learning — Stanford (Manning) | [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/) | ✅ slides/notes public |
| `r-sutton-barto` | Reinforcement Learning: An Introduction (2nd ed) — Sutton & Barto | [incompleteideas.net](http://incompleteideas.net/book/the-book-2nd.html) | 🟢? free draft · 📕 local |
| `r-silver-rl` | RL Course — David Silver (DeepMind × UCL) | [davidsilver.uk/teaching](https://www.davidsilver.uk/teaching/) | 🎥 ✅ free (CC-BY-NC) |
| `r-cs234` | CS234 Reinforcement Learning — Stanford | [web.stanford.edu/class/cs234](https://web.stanford.edu/class/cs234/) | 🟢? notes public |
| `r-berkeley-cs285` | CS285 Deep RL — Berkeley (Levine) | [rail.eecs.berkeley.edu/deeprlcourse](https://rail.eecs.berkeley.edu/deeprlcourse/) | 🎥 🟢? free |
| `r-mit-6034` | 6.034 Artificial Intelligence — MIT | [MIT OCW](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) | ✅ free |
| `r-aima` | AI: A Modern Approach (4th ed, 2022) — Russell & Norvig | [aima.cs.berkeley.edu](https://aima.cs.berkeley.edu/) | 📘 book (resources free) · 📕 local |
| `r-pml-murphy` | Probabilistic Machine Learning — Murphy | [probml.github.io](https://probml.github.io/pml-book/) | 🟢? free PDFs |

## 10 · Minds & brains (natural intelligence)
| id | Resource | Source | Access |
|---|---|---|---|
| `r-neuronal-dynamics` | Neuronal Dynamics — Gerstner et al. (EPFL) | [neuronaldynamics.epfl.ch](https://neuronaldynamics.epfl.ch/online/index.html) | ✅ free + video |
| `r-kandel` | Principles of Neural Science (6e, 2021) — Kandel et al. | (McGraw-Hill) | 📘 → 📕 local copy obtained |
| `r-henrich` | The Secret of Our Success (cultural evolution) — Henrich | (Princeton UP) | 📘 need to obtain |
| `r-hawkins-1000brains` | A Thousand Brains: A New Theory of Intelligence — Hawkins | (Basic Books) | 📕 local copy |
| `r-bennett-bhi` | A Brief History of Intelligence — Bennett | (Mariner) | 📕 local copy |
| `r-harari-sapiens` | Sapiens: A Brief History of Humankind (collective intelligence) — Harari | (Harper) | 📕 local copy |

## 40 · Compute & physical (hardware, energy, quantum)
| id | Resource | Source | Access |
|---|---|---|---|
| `r-quantum-country` | Quantum Country — Matuschak & Nielsen | [quantum.country](https://quantum.country/) | ✅ free |
| `r-preskill-ph229` | Quantum Computation notes — Preskill (Caltech) | [theory.caltech.edu](http://theory.caltech.edu/~preskill/ph229/) | 🟢? free notes |
| `r-nielsen-chuang` | Quantum Computation & Quantum Information — Nielsen & Chuang | (Cambridge) | 📘 canonical, obtain |
| `r-feynman` | The Feynman Lectures on Physics | [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) | 🟢? free |
| `r-chipwar` | Chip War (semiconductors/geopolitics) — Miller | (Scribner) | 📘 need to obtain |
| `r-kawahara-hw` | Hardware Technologies for AI: AI Chips, Ising Machines, In-Memory — Kawahara (2026) | (CRC) | 📕 local copy |
| `r-mainzer-neuro` | AI of Neuromorphic Systems (digital→quantum→brain-oriented) — Mainzer (2024) | (World Scientific) | 📕 local copy |
| `r-siciliano-robotics` | Foundations of Robotics — Siciliano, Villani, Oriolo, De Luca (2025) | (Springer) | 📕 local copy |

## 60 · Frontier (paths to AGI, alignment, ASI)
| id | Resource | Source | Access |
|---|---|---|---|
| `r-aisf` | AI Safety / Alignment Fundamentals curriculum — BlueDot | [aisafetyfundamentals.com](https://aisafetyfundamentals.com/) | ✅ free curriculum |
| `r-rob-miles` | AI Safety explainers — Rob Miles (validated communicator) | YouTube: "Rob Miles AI Safety" | 🎥 🟢? free |
| `r-russell-hc` | Human Compatible — Stuart Russell | (Viking) | 📘 need to obtain |
| `r-bostrom-superint` | Superintelligence — Bostrom | (Oxford UP) | 📘 need to obtain |
| `r-legg-hutter` | A Collection of Definitions of Intelligence — Legg & Hutter (2007) | arXiv | 🟢? free |
| `r-christian-alignment` | The Alignment Problem — Brian Christian | (Norton) | 📕 local copy |
| `r-tegmark-life3` | Life 3.0 — Max Tegmark | (Knopf) | 📕 local copy |
| `r-togelius-agi` | Artificial General Intelligence — Togelius (2024) | (MIT Press) | 📕 local copy |
| `r-martinez-systems` | AI: A Systems Approach from Architecture to Deployment — Martinez (2024) | (MIT Press / Lincoln Lab) | 📕 local copy |
| `r-shakarian-metacog` | Metacognitive AI (neurosymbolic, self-assessment) — Shakarian & Wei (2025) | (Cambridge) | 📕 local copy |
| `r-tsironis-complex` | AI & Complex Dynamical Systems — Tsironis (2025) | (Springer) | 📕 local copy |

---

## How an entry becomes understanding
A resource here is **broken into semantic chunks**, each chunk tagged to a domain/concept, and the chunks are **woven into the learning modules** (often several resources feed one module — *not* one module per book). Pipeline: [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §12.

*This list is curated and will grow as the ladder reaches new areas — added on demand, never hoarded.*
