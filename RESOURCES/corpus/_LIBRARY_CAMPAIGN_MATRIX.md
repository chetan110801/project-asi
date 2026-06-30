# 📚 Science & Engineering Library Campaign — the full elementary→research matrix
**Learner directive (2026-06-30):** the corpus must hold **free, legal resources covering every domain & sub-domain of engineering, the sciences, and adjacent relevant fields — from elementary through undergraduate, graduate/PhD, up to state-of-the-art research level.** "Collect as many books as needed per discipline; cover each sub-domain end-to-end." This file is the **authoritative target matrix + status board** for that push. Companion to [`_CAMPAIGN_PLAN.md`](_CAMPAIGN_PLAN.md) (Stream 2, now expanded here).

`Status: Living plan · Created 2026-06-30 (session 8) · a multi-session campaign — depth + breadth beat speed`

---

## 0. Governing rules (unchanged from HARD_RULES §1–§2 + campaign plan §0)
1. **Legality absolute.** Only open-licensed / CC / public-domain / author-free / arXiv / gov / course-public text. **OpenStax & LibreTexts = CC-BY/CC-BY-SA → fine.** Paywalled-not-owned → [`../REQUESTS.md`](../REQUESTS.md), never scrape pirated copies (this is why commercial "Dummies" titles beyond the 18 owned can't be web-fetched).
2. **Anti-redundancy.** Skip what's already held (`corpus/textbooks/_LIBRARY_INDEX.txt` for the 362 owned books; the per-domain folders). Newest edition wins; don't re-take a saturated tier.
3. **Durability filter (relaxed for breadth).** Still collect the *timeless principle / reason-and-objective*, but the learner has explicitly widened scope: **breadth + depth across all of science/engineering is now wanted**, each field framed by *how it pushes / is accelerated by AI → AGI*. Execution-only coding tutorials still delegated.
4. **Validate-before-fetch.** HEAD/probe each URL live; for multi-file books enumerate first. Verify arXiv IDs vs API.
5. **Git:** all corpus text stays git-ignored; only tracking md committed. Tick this file + [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) every session.
6. **Still gathering — do NOT write/reground modules** until the learner calls the corpus rich enough.

## 0a. The 4 levels (every discipline should span all four)
| Tier | Level | Primary free sources |
|---|---|---|
| **L1** | Elementary / intro | OpenStax (CC-BY), LibreTexts intro shelves, CK-12 |
| **L2** | Undergraduate | OpenStax upper-div, author free books (Hefferon, Boyd, MacKay…), university lecture-note PDFs, **owned 362-book library** |
| **L3** | Graduate / PhD | University grad lecture notes (Tong, MIT-OCW/Stanford PDFs), advanced author monographs, **owned grad texts** |
| **L4** | State-of-the-art / research | **arXiv** monographs & surveys, review articles, the [`../PAPERS.md`](../PAPERS.md) D0–D12 landmark set (142 arXiv IDs verified), lab tech-reports, the 1,672-source course/transcript corpus |

## 0b. Proven fetch toolkit (scratchpad, rebuild each session)
`getpdf.sh` (curl→pdftotext -layout→norm→chunk) · `fetchmulti.sh` (multi-PDF book→concat→chunk) · `chunk.sh` · `bookresolve.sh` (OpenStax CMS API → real PDF URL) · `tong.sh` (davidtong.org pattern: page→largest non-problem-sheet PDF) · `probe_*.sh` (HEAD validate) · `arxiv.sh`/`paperbatch.sh` (verify+fetch). **`libretexts.sh` (BUILT Session 11):** recursive public-HTML descendant-walker — deki API confirmed token-gated (403) & batch-PDF async, so it crawls the root → child links (one path-level deeper, descendants only) → `MAXDEPTH=3`; content filter drops everything through the `fillinmathshade` MathJax-preamble anchor and stops at `<footer>`; pass roots with a colon as `%3A`. **`pbwalk.sh` (BUILT Session 11):** Pressbooks walker — enumerate `/wp-json/pressbooks/v2/toc`, de-chrome, cut at the `License` footer, `--max-time` hardened.

---

## 1. THE MATRIX — disciplines × sub-domains × level, with status
Legend: ✅ held (some level) · 🔄 in progress this session · ⬜ to fetch. "Held" notes the strongest existing items.

### Mathematics  — `math-theory/`
Sub-domains: arithmetic/pre-algebra · algebra · precalculus · **calculus (single+multi)** · **linear algebra** · **differential equations (ODE/PDE)** · **real & complex analysis** · **abstract algebra** · **topology** · **number theory** · **discrete math/combinatorics** · **probability** · **statistics** · **numerical methods** · **optimization** · **mathematical logic/set theory** · **graph theory** · **measure theory** · **functional analysis** · **differential geometry** · **category theory**.
- ✅ Held: MML, ISL/ESL, Boyd (convex opt), MacKay, Tong vector-calculus, OpenStax Calculus 1–3, Intro Stats 2e, Oxford measure/functional-analysis (courses), 18.02/18.06/18.404J/18.065 (courses), 3B1B. **+ Session 9:** Hefferon LA ✅, VMLS (Boyd-Vandenberghe applied LA) ✅, Trench Real Analysis ✅, Judson Abstract Algebra ✅, Levin Discrete Math ✅, Morris Topology ✅, OpenStax Prealgebra/Elem-Algebra/Interm-Algebra/College-Algebra/Precalculus 2e ✅ (L1 ladder).
- ⬜ Remaining L1–L3: **Strang Calculus (MIT)**. **+ Session 12:** **Stein — Elementary Number Theory** ✅ (number-theory sub-domain filled). L4 ✅ session 12: optimization-for-ML (Bottou), GNN, time-series-DL, causal-ML surveys → `papers/D13/D15/`. **[Session-9 wave DONE: linear algebra, real analysis, abstract algebra, topology, discrete math, applied LA, + L1 algebra→precalc ladder all collected.]**

### Statistics & Probability — `math-theory/`
Sub-domains: descriptive · probability theory · inference · regression · Bayesian · experimental design · stochastic processes · time series · causal inference · ML-stats.
- ✅ Held: Blitzstein (STAT110 course), Murphy PML, Intro Stats 2e, StatQuest, Oxford prob-measure. **+ Session 9:** OpenIntro Statistics 4e ✅, Downey Think Stats 2e ✅ + Think Bayes ✅, Hernán-Robins "What If" causal inference ✅, Hyndman FPP3 forecasting/time-series ✅ (HTML-walked).
- ⬜ Remaining: "Seeing Theory" (interactive — low priority), Hansen "Econometrics" (→ economics-data, session 10+). **[Session-9 wave DONE: descriptive→probability→inference→Bayesian→causal→time-series all collected.]**

### Physics — `physics/`
Sub-domains: classical mechanics · E&M · thermodynamics · statistical mechanics · **quantum mechanics** · **QFT** · optics · waves/vibrations · relativity (special+general) · **cosmology** · particle/nuclear · condensed-matter/solid-state · fluid dynamics · plasma · biophysics · computational physics.
- 🔄 **Tong full set (this session):** classical-dynamics, dynamics-and-relativity, electromagnetism, QM, topics-in-QM, QFT, stat-physics, kinetic-theory, stat-field-theory, fluids, GR, cosmology, particle, standard-model, gauge-theory, solid-state, quantum-hall, solitons, string, SUSY×2. ✅ Held: OpenStax University Physics 1–3, MIT 8.01/8.03/8.04/8.05/8.06 (courses), Yale Physics I/II 🔄, Feynman selections.
- ⬜ L1: OpenStax College Physics 2e (algebra-based). L4: arXiv hep/cond-mat/astro-ph reviews.

### Chemistry — `chemistry/`
Sub-domains: general · **organic** · inorganic · **physical chemistry** · analytical · biochemistry · quantum chemistry · materials chem · computational chem (AI-for-chem).
- ✅ Held: OpenStax Chemistry 2e, Atoms First 2e, Organic Chemistry; Yale Organic Chem I/II 🔄. **+ Session 11:** **DeVoe — Thermodynamics and Chemistry** (chemical thermodynamics, direct PDF, CC BY) ✅ — fills the **Physical-Chemistry** gap.
- ✅ **+ Session 12:** **Harvey — Analytical Chemistry 2.1** (analytical) · **Introduction to Inorganic Chemistry** (Wikibook, inorganic) · **Jakubowski & Flatt — Fundamentals of Biochemistry** (biochemistry, `655` chunks) — all LibreTexts. **+ MIT 5.111 Principles of Chemical Science** + **5.60 Thermodynamics & Kinetics** + **3.091 Solid-State Chemistry** (courses). L4: ML-for-chemistry survey (1904.10370) → `papers/D15/`.
- ⬜ Remaining: "Quantum Chemistry" notes. **[Session-11: Physical-Chemistry gap filled. Session-12: analytical + inorganic + biochemistry filled.]**

### Biology — `biology/`
Sub-domains: cell · molecular · **genetics/genomics** · **evolution** · ecology · microbiology · anatomy · physiology · botany · zoology · developmental · immunology · **systems/computational biology** · biotech · **neuroscience(→own)**.
- ✅ Held: OpenStax Biology 2e, Concepts of Biology, Microbiology, Anatomy & Physiology (this session); Tong mathematical-biology 🔄; MIT 7.016/7.91J (courses); Yale Evolution/Population-Growth/Biomed-Eng 🔄; AlphaFold papers.
- ✅ **+ Session 12:** **Nickle & Barrette-Ng — Online Open Genetics** (LibreTexts) + **MIT 7.05 General Biochemistry** (course). L4: DL-&-neuroscience (1606.03813), DL-in-healthcare (2310.00727) → `papers/D15/`.
- ⬜ Remaining: LibreTexts **immunology** + developmental; **Computational Biology (MIT 6.047 notes)** — both → session 13. **[Session-12: genetics filled.]**

### Earth, Climate & Environmental science — `earth-climate/` (NEW)
Sub-domains: geology · oceanography · atmospheric science/meteorology · climatology · hydrology · environmental science · geophysics · AI-weather (GraphCast/GenCast).
- ✅ Held: Yale Atmosphere/Ocean/Climate 🔄; GraphCast/GenCast/NeuralGCM papers. **+ Session 11 (folder seeded):** **Johnson et al. — An Introduction to Geology** (minerals, igneous/sedimentary/metamorphic, plate tectonics, earthquakes, geologic time) ✅ · **Webb — Introduction to Oceanography** (currents, waves, tides, salinity/thermocline, marine life) ✅. Both Geosciences LibreTexts.
- ✅ **+ Session 12:** **Stull — Practical Meteorology** (UBC, full ~940-pp, `390` chunks) · **Brune — Fundamentals of Atmospheric Science** (Penn State, LibreTexts) · **Schmittner — Introduction to Climate Science** (Oregon State, LibreTexts) — fills meteorology + atmospheric-science + climatology. L4: ML-climate-models review (2311.09413) → `papers/D15/`; GraphCast/GenCast/NeuralGCM already held.
- ⬜ Remaining: Hydrology, Environmental science (lower priority); USGS/NOAA open texts. **[Session-11: geology + oceanography. Session-12: meteorology + atmospheric-science + climatology filled.]**

### Astronomy & Cosmology — `astronomy/`
Sub-domains: observational · planetary · stellar · galactic · cosmology · astrophysics · astrobiology · AI-for-astro.
- ✅ Held: OpenStax Astronomy 2e (this session); Yale Astrophysics 🔄; Tong cosmology 🔄; astronomy AI papers.
- ⬜ "Astrophysics" open notes; arXiv astro-ph reviews.

### Computer Science — `computer-systems/` · `information-computation/` · `ai-ml-foundations/`
Sub-domains: **algorithms & data structures** · **theory of computation/complexity** · **operating systems** · **networking** · **databases** · **distributed systems** · **computer architecture** · **compilers/PL** · **security/cryptography** · **HCI** · **graphics** · **software engineering** · **AI/ML(→own)**.
- ✅ Held: OSTEP, Computer Networks (Systems Approach), Distributed Systems (Kleppmann), DB Architecture (Hellerstein), Database Design, Think OS. Prior: introtcs, Arora-Barak, Goodfellow/d2l/many ML, CS courses. **+ Session 10:** Erickson **Algorithms** ✅, Boneh-Shoup **Applied Cryptography** ✅, Nystrom **Crafting Interpreters** (compilers/PL) ✅, Pierce **Software Foundations** Vol 1+2 (formal verification/PL theory) ✅, Pharr **Physically Based Rendering** 4e (graphics) ✅.
- ⬜ Remaining: Computer Architecture ("Dive into Systems" / Patterson→REQUESTS), Security ("Computer Security" open), Software-engineering open texts. **[Session-10 wave DONE: algorithms, cryptography, compilers/PL, formal verification, graphics all collected.]**

### Artificial Intelligence & Machine Learning — `ai-ml-foundations/` · `papers/` · `courses/`
Sub-domains: classical ML · deep learning · RL · NLP/LLMs · CV · generative · graph ML · representation · optimization for ML · probabilistic ML · MLsys · efficient-ML · interpretability · alignment/safety · agents · multimodal · AI-for-science.
- ✅ **Deeply held** (this is the corpus spine): owned spine books + ~90 courses + PAPERS.md D1–D12 (142 arXiv IDs) + governance set. **+ Session 12 L4 review layer (`papers/D13–D16/`):** comprehensive surveys for LLMs/agents/reasoning/RAG/multimodal/MoE/SSM/ICL/eval/distillation/continual/optimization/GNN/SSL/federated/ViT/efficient-LLM/diffusion (D13) + mech-interp/RLHF/alignment (D14) + ML-for-each-science (D15) + quantum/robotics/AGI frontier (D16). **Saturated — selective top-ups only;** a 2nd L4 batch (NLP/CV/speech/meta-learning/transfer/uncertainty/OOD/neuro-symbolic/NAS/offline-RL/multiagent-RL/hallucination) queued for session 13.

### Electrical & Electronics Engineering — `electrical-engineering/`
Sub-domains: **circuits (DC/AC)** · **electronics/semiconductors** · **digital logic** · **signals & systems** · **DSP** · **control systems** · communications · electromagnetics · power systems · microelectronics/VLSI · embedded systems · **computer/AI hardware (→`hardware-compute/`)**.
- ✅ Held: Lessons in Electric Circuits Vol I–V (DC/AC/Semiconductors/Digital/Reference), DSP Guide (Smith), Think DSP; prior Sze (efficient DNN HW), Kawahara HW. **+ Session 10:** Ellingson **Electromagnetics Vol 1 + Vol 2** (Virginia Tech, CC BY-SA) ✅.
- ✅ **+ Session 12:** **Baraniuk et al. — Signals and Systems** (LibreTexts/Connexions, CC BY) — fills the **signals-&-systems** sub-domain (Oppenheim stays paywalled→REQUESTS) + **MIT 6.002 Circuits and Electronics** (course). L4: DSP/efficient-LLM hardware already via Sze.
- ⬜ Remaining: Communications, Power systems, VLSI (Harris&Weste→REQUESTS), Embedded → session 13. **[Session-10: electromagnetics. Session-12: signals-&-systems + circuits filled.]**

### Control & Robotics — `robotics/`
Sub-domains: classical/modern control · feedback · state-space · optimal/robust · nonlinear · **robot kinematics/dynamics** · motion planning · estimation/SLAM · manipulation · legged/aerial · embodied AI.
- ✅ Held: Feedback Systems (Åström-Murray, this session), Tedrake Underactuated, Lynch-Park, LaValle, Siciliano, Brunton control set (courses), MIT 6.832/2.003SC/16.412J.
- ⬜ "Modern Robotics" (Lynch-Park ✅), "Underactuated"✅, estimation ("Probabilistic Robotics"→REQUESTS), SLAM notes.

### Mechanical Engineering — `mechanical-engineering/` (NEW)
Sub-domains: statics · dynamics · mechanics of materials/solids · thermodynamics · fluid mechanics · heat transfer · machine design · vibrations · manufacturing · MEMS · CFD.
- ✅ Held: Lienhard **A Heat Transfer Textbook** (Session 10). **+ Session 11:** **Mechanics Map** (Moore — statics+dynamics+1-DOF vibrations) ✅ · **Engineering Statics: Open & Interactive** (Baker & Haynes) ✅ · **Mechanics of Materials** (Roylance, MIT — solids/strength) ✅ · **Basics of Fluid Mechanics** (Bar-Meir/Potto, direct PDF) ✅. (Thermodynamics → DeVoe, filed under `chemistry/`.)
- ⬜ Remaining: dedicated **machine design** & **manufacturing/CFD** texts (lower priority — Mechanics Map covers dynamics; Roylance covers solids). **[Session-11 wave DONE: statics, dynamics, mechanics-of-materials, fluid-mechanics all collected; heat-transfer already held.]**

### Civil & Structural Engineering — `civil-engineering/` (NEW — seeded Session 11)
Sub-domains: structural analysis · mechanics of materials · geotechnical · transportation · hydraulics/water-resources · construction · surveying · environmental/civil.
- ✅ **+ Session 11:** **Udoeyo — Structural Analysis** (Temple Univ, LibreTexts) ✅ — loads, determinacy/stability, beams/frames/trusses, arches & cables, deflections, force/displacement methods, influence lines. (Mechanics-of-materials also via Roylance in `mechanical-engineering/`.)
- ✅ **+ Session 12:** **Fundamentals of Foundation Engineering and their Applications 2e** (LibreTexts) — fills **geotechnical / foundation** engineering.
- ⬜ Remaining: transportation; hydraulics/water-resources → session 13. **[Session-11: structural analysis. Session-12: geotechnical/foundation filled.]**

### Chemical Engineering — `chemical-engineering/` (NEW — seeded Session 11)
Sub-domains: material/energy balances · transport phenomena · thermodynamics · reaction engineering · separations/distillation · process control · process design.
- ✅ **+ Session 11:** **Verret, Qiao & Barghout — Foundations of Chemical and Biological Engineering I** (material/energy balances, PFDs, process safety) ✅ · **Woolf et al. — Chemical Process Dynamics and Controls** (Laplace, transfer functions, PID, feedback/feedforward, stability — process control) ✅. Both LibreTexts.
- ⬜ Remaining: transport phenomena, reaction engineering, separations/distillation, process design. **[Session-11: ChemE intro + process control collected; `chemical-engineering/` folder seeded.]**

### Aerospace Engineering — `aerospace-engineering/` (NEW — seeded Session 11)
Sub-domains: aerodynamics · propulsion · flight dynamics · orbital mechanics/astrodynamics · aerospace structures · GNC · spacecraft.
- ✅ **+ Session 11:** **Marchman — Aerodynamics and Aircraft Performance 3e** (VT/LibreTexts: airfoils, lift/drag, level/climb/turn flight, range & endurance, V-n, constraint analysis) ✅ · **Leishman — Introduction to Aerospace Flight Vehicles** (Embry-Riddle Pressbooks, **~1,100-pp comprehensive**: aero, propulsion, structures, stability & control, flight & space flight, design — `1248` chunks) ✅.
- ⬜ Remaining: "Orbital Mechanics & Astrodynamics" open, MIT 16.x OCW notes, dedicated propulsion. **[Session-11: aerodynamics + aircraft performance + a full flight-vehicles text collected; `aerospace-engineering/` folder seeded. Leishman's slow server needed the hardened `pbwalk.sh` (`--max-time`).]**

### Materials Science — `materials/`
Sub-domains: structure/crystallography · thermo of materials · mechanical behavior · electronic materials · polymers · nanomaterials · **AI-for-materials (GNoME/MatterGen)**.
- ✅ Held: MatterGen, Open Catalyst papers. **+ Session 11:** **DoITPoMS (Cambridge) — TLP Library I** (crystallography, Miller indices, dislocations, diffusion, stress/strain, mechanical behaviour) ✅ · **TLP Library II** (phase diagrams & solidification, semiconductors, polymers, ferroelectrics, optical/electronic materials) ✅. Both LibreTexts. (Mechanical behaviour of materials also via Roylance.)
- ⬜ MIT 3.091 notes (scattered HTML — low priority, redundant with TLP + Tong solid-state); dedicated nanomaterials. **[Session-11: crystallography→phase-diagrams→electronic/polymer materials collected via the two TLP libraries.]**

### Biomedical / Bioengineering — `biomedical-engineering/` (NEW)
Sub-domains: biomechanics · biomaterials · biomedical imaging · biosignals · tissue eng · medical devices · computational medicine · AI-in-healthcare.
- ✅ Held: Yale Frontiers of Biomedical Engineering 🔄; MIT 6.S897 ML-for-Healthcare (course); owned AI-healthcare volumes.
- ⬜ LibreTexts/open biomechanics, medical imaging notes.

### Neuroscience — `neuroscience/`
Sub-domains: cellular/molecular · systems · cognitive · computational · behavioral · clinical · neural coding · plasticity.
- ✅ **Deeply held:** full Kandel set (12 vols), Gerstner Neuronal Dynamics, CompCogNeuro, predictive-coding; MIT 9.13/9.14/9.40, Kirsanov; Sapolsky Behavioral-Biology 🔄.
- ⬜ Neuromatch Academy notes; Dayan-Abbott "Theoretical Neuroscience" (→REQUESTS or open notes).

### Cognitive Science & Psychology — `cognitive-science/`
Sub-domains: perception · attention · memory · language · reasoning/decision · development · social · clinical · computational cognition.
- ✅ Held: OpenStax Psychology 2e (this session), probmods, SEP, Lake; MIT 24.08J; Yale Psychology/Phil-of-Human-Nature 🔄.
- ⬜ "Cognitive Psychology" open, OpenStax adjacent.

### Economics & Social science — `economics-data/`
Sub-domains: micro · macro · econometrics · game theory · behavioral · development · finance · mechanism design · economics-of-AI.
- ✅ Held: OpenStax Principles of Economics 3e (this session); Yale Game-Theory/Financial-Markets/Financial-Theory 🔄; Acemoglu, MIT 14.01/14.02.
- ⬜ OpenStax Micro/Macro (if additive), "Econometrics" open (Hansen free PDF), "Finance" open.

### Quantum information & computing — `quantum/`
Sub-domains: quantum mechanics(→physics) · qubits/gates · algorithms · error correction · quantum hardware · QML · quantum complexity.
- ✅ Held: Watrous, Quantum Country, QML; Yale QEC 🔄; MIT 8.05/8.06. **+ Session 10:** **Preskill** Ph219/CS219 lecture notes (Caltech, free) ✅ — chs 1-7,10 + topological QC.
- ⬜ Remaining: "Quantum Computing" open notes (Nielsen-Chuang→REQUESTS). **[Session-10 wave DONE: Preskill notes collected.]**

### Information theory & Complex systems — `information-computation/` · `complex-systems/`
- ✅ Held: MacKay ITILA, Shannon, Aaronson; Newman Networks; Oxford Info-Theory.
- ⬜ Cover's "Elements of Info Theory"→REQUESTS; Santa Fe Complexity Explorer notes; "Networks" extras.

### Other relevant fields
- **Philosophy of mind / epistemology / ethics / political philosophy** — `cognitive-science/` `governance-safety/`: ✅ SEP entries, Yale Political-Phil/Moral-Foundations/Death 🔄, Sandel Justice 🔄. ⬜ open ethics/phil-of-mind texts.
- **Linguistics** — ⬜ "The Language Instinct"→REQUESTS; open linguistics texts; (NLP/SLP3 ✅).
- **Governance / AI-safety / policy** — ✅ deeply held (International AI Safety Report, NIST, RSP, etc.).

---

## 2. Session waves (this campaign)
- **Session 8 (this) ✅🔄:** Yale 18 + 4 named playlists (transcripts) · OpenStax 16 (phys/chem/astro/math/bio/psych/econ) · Eng/CS 14 (OSTEP, DSP-Guide, Electric-Circuits I–V, Networks, Distributed, DB, Feedback-Systems) · **Tong physics full set (23)** 🔄. New domain folders: chemistry, computer-systems, electrical-engineering.
- **Session 9 ✅ DONE (2026-06-30) — Math + Stats end-to-end (author-PDF wave):** Hefferon, Judson, Trench, OpenIntro, VMLS, Topology-Without-Tears, Levin Discrete-Math, Downey Think-Stats/Bayes, Hyndman FPP3, Hernán "What If" + OpenStax L1 ladder (Prealgebra→Precalculus). **16 books / 1,603 clean chunks → `math-theory/`.** Built the general HTML walker (`htmlwalk.sh`+`html2txt.pl`) for FPP3; fixed `norm.pl` (CESU-8 surrogate + NFKC math-letter/ligature folding). [Judson via legal mirror — official host DNS-down.]
- **Session 10 ✅ DONE (2026-06-30) — CS depth + EE/ECE/MechE/quantum depth:** Erickson Algorithms, Boneh-Shoup crypto, Crafting Interpreters (compilers/PL), Software Foundations Vol 1+2 (formal verification), PBR 4e (graphics); Ellingson Electromagnetics Vol 1+2; Preskill quantum notes; Lienhard heat-transfer (→ NEW `mechanical-engineering/`). **9 books / 1,045 clean chunks** (0 FFFD). Built `fetchmulti.sh` (multi-PDF book → concat → chunk); proved `htmlwalk.sh` on 3 site shapes. [Carry-forward: JS-rendered index → enumerate page list via WebFetch; VTechWorks DSpace download = `vtechworks.lib.vt.edu/bitstreams/<uuid>/download`.]
- **Session 11 ✅ DONE (2026-06-30) — the LibreTexts/Pressbooks walkers + the 5 engineering shelves:** built **`libretexts.sh`** (recursive public-HTML descendant-walker; deki API confirmed token-gated → crawl; `fillinmathshade`→`<footer>` content filter; MAXDEPTH=3; `%3A` root handling) **and `pbwalk.sh`** (Pressbooks `/wp-json/.../toc` enumerator + `License`-cut filter + `--max-time` hardening). Collected **14 free books / 1,981 verbatim chunks, all 0 FFFD**: Mechanical (Mechanics Map, Baker Statics, Roylance Mechanics-of-Materials, Bar-Meir Fluid Mechanics), Chemistry (DeVoe Thermo — physical-chem gap), Civil (Udoeyo Structural Analysis), Chemical (Verret Foundations, Woolf Process-Dynamics-&-Controls), Aerospace (Marchman Aerodynamics, Leishman Flight-Vehicles `1248`), Materials (DoITPoMS TLP Library I + II), Earth (Intro-to-Geology, Webb Oceanography). **4 new domain folders:** `civil-engineering/`, `chemical-engineering/`, `aerospace-engineering/`, `earth-climate/`. All five "no-clean-PDF" engineering shelves now seeded end-to-end.
- **Session 12 ✅ DONE (2026-06-30/07-01) — L4 survey/monograph wave + textbook gap-fill + MIT-OCW gap courses + channel re-sweeps.** **(A)** 38 arXiv surveys/monographs / 712 chunks → `papers/D13–D16/` (every ID API-searched then re-verified vs API, 0 mismatches; built `arxiv_search.sh`; PAPERS.md §D13–D16). **(B)** 10 free books / 1,508 chunks filling the residual ⬜: Stein number-theory · Stull/Brune/Schmittner meteorology+atmospheric+climatology · Harvey analytical + inorganic + Jakubowski biochemistry · Nickle genetics · Baraniuk signals-&-systems · Foundation-Engineering geotech. **(C)** 9 MIT-OCW gap courses / 372 transcripts (3.091 solid-state, 6.002 circuits, 6.004 computation-structures, 6.046J algorithms, 18.085 computational-science, 22.01 nuclear-eng, 7.05 biochem, 5.111 gen-chem, 5.60 thermo). **(D)** learner-requested channel re-sweep: Dwarkesh full YouTube channel (`dwarkesh-youtube/` NEW, 198 — captures the website-gated episodes) + newest episode (Grant Sanderson #2) · Two-Minute-Papers +71 · DeepMind +2 (`@GoogleDeepMind`) · **Richard Sutton talks** (`richard-sutton-talks/` NEW, 76). **Learner directive: push everything to exhaustion across courses + books + L4 papers (multi-session).** OCR of the 3 image-only scans still pending (no tesseract).
  - ⬜ **Still residual (→ session 13):** aerospace orbital-mechanics/astrodynamics · civil hydraulics · chem analytical-deepen · **biology immunology + computational-biology (MIT 6.047)** · EE communications/power/VLSI/embedded · MIT 3.091 already taken (course). Plus a 2nd L4 arXiv batch (NLP/CV/speech/meta-learning/transfer/uncertainty/OOD/neuro-symbolic/NAS/offline-RL/multiagent-RL/hallucination — discovery list ready).
- **Session 13+ — continue exhaustion (residual books + 2nd L4 arXiv batch + more gap courses) + verification → pause for the learner's "rich enough" call → first grounded module rewrite (1300 LLMs).**

> Each session: validate-live → managed collect/extract → tick this file + [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) → refresh handoff → commit tracking md. **Take as many sessions as needed — exhaustive breadth+depth is the goal.**
