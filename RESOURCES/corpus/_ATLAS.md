# THE ATLAS — grounding index + depth/breadth audit of the corpus
**The bridge between the source-organized corpus and the concept-organized modules.** Definition & role: [`../../INSTRUCTIONS/PRODUCTION_FLOW.md`](../../INSTRUCTIONS/PRODUCTION_FLOW.md) ② (not restated here). In short: for each domain it maps **every corpus source that touches it, across all folders**, tagged by level + quality — so grounding a module stops being needle-in-a-haystack — and it records **which depth tier** each domain is written to.

`Part of: PROJECT ASI · System Version: 2.5 · Status: Living · Last updated: 2026-07-02`
`Scale indexed: ~54,000 text files · ~900 MB · 31 corpus folders (survey: session 20).`

> **Two organizing schemes coexist in the corpus** (this is *why* the Atlas is needed): **source-type pools** — `textbooks/` (362 mixed all-domain sources + course fragments), `courses/` (134), `transcripts/` (192), `papers/` (16 D-groups ≈ 130 papers), `frontier-rnd/` (127) — and **discipline shelves** — `physics/`, `biology/`, … (26 folders). No domain lives in one place; the Atlas re-unifies them per domain.

---

## §1. Depth-tier assignments (approved by the learner, session 20 — 3-tier scheme)
Tiers set **how deep**, not **whether** (a Literacy domain is still "covered" once it yields modules). Rule: [`../../INSTRUCTIONS/PRODUCTION_FLOW.md`](../../INSTRUCTIONS/PRODUCTION_FLOW.md) ①; policy basis: [`../../INSTRUCTIONS/LEARNER_STRATEGY.md`](../../INSTRUCTIONS/LEARNER_STRATEGY.md) §2–§3 × [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §1.4.

| Tier | Depth | Domains |
|---|---|---|
| **CORE** — exhaustive (full hy standard) | every idea/mechanism/argument/trade-off/debate rendered | **AI/ML/DL/RL/LLMs/agents** · **applied AI & agentic systems** (shelf `25`; principles not frameworks) · **alignment & interpretability** · **scaling laws** · **AGI-math** (linear algebra, probability, optimization, information theory, learning theory) · **minds** (neuroscience, cognition — as blueprint + benchmark for intelligence) |
| **BRIDGE** — working depth (decide, don't build) | enough to reason and choose well; not every mechanism | **hardware/chips/compute** · **energy** · **data economics** · **robotics/embodiment** · **quantum computing** · **complex systems** · **governance/geopolitics** · **computer-systems** (OS/networks/DB/distributed — directing AI infra) |
| **LITERACY** — compact map + "how it pushes AGI" | enduring core + the connection to the mission; not textbook reproduction | **physics** · **chemistry** · **biology** · **materials** · **astronomy** · **earth/climate** · classical engineering (**electrical / mechanical / civil / chemical / aerospace / biomedical**) · **rest of math** (analysis, topology, abstract algebra, number theory) · **blockchain/web3** |

*Note:* a few domains split by concept — e.g. within `governance-safety/`, alignment+interpretability is **Core** while policy/governance is **Bridge**; within `information-computation/`, information theory is **Core (AGI-math)** while broader complexity theory is **Bridge**; within math, the AGI-math slice is **Core** and the rest is **Literacy**. The Atlas slice for each records the split.

---

## §2. Depth & breadth audit (the "check each" deliverable)
Honest read from the session-20 survey. **Readiness = does the corpus support this domain's *tier* depth?** (A thin corpus is fine for a Literacy domain and a problem only for a Core one.)

| Domain | Tier | Corpus depth (level span) | Breadth (sub-domains) | Ready for its tier? |
|---|---|---|---|---|
| AI / ML / DL / RL / LLMs / agents | Core | elementary → research (ai-ml-foundations + papers D1–D13 + 60+ courses + textbooks + transcripts) | excellent | ✅ deep + broad |
| Applied AI & agentic systems (shelf 25) | Core | practitioner → SOTA (frontier-rnd: 26 agent-framework docs + anti-vibe-coding methodology + OpenAI/Anthropic agent guides + papers D9-agents-rag) | good | ✅ (richest applied corpus we hold) |
| AGI-math (linalg/prob/opt/info-theory/learning-theory) | Core | elementary → grad (math-theory ladder + Boyd + ISLR + MacKay + Murphy) | excellent | ✅ |
| Alignment & interpretability | Core | undergrad → research (governance-safety + papers D14 + Distill circuits + AXRP/80k transcripts) | good | ✅ |
| Scaling laws | Core | research (papers D3 ×14 + compute-trends + data-limits + transcripts) | focused, sufficient | ✅ |
| Minds — neuroscience | Core | undergrad → research (Kandel 6e in textbooks + Neuronal Dynamics + MIT 9.x courses) | good, but **skewed to predictive-coding/FEP** | ⚠️ ready; watch the skew |
| Minds — cognitive science | Core | intro → research (psychology-2e + probmods + Lake + SEP) | thin-ish (6 shelf sources) | ⚠️ adequate; lean |
| Hardware / chips / compute | Bridge | undergrad → research (papers D6 + Sze + compute-trends + NVIDIA/IBM frontier-rnd) | thin shelf (3) but reinforced | ⚠️ adequate for Bridge |
| Energy | Bridge | intro (MacKay SEWTHA + OWID) | thin (2) | ⚠️ minimal but ok for Bridge |
| Data economics | Bridge | undergrad (Villalobos data-limits + Acemoglu + AI-Index + OWID) | ok | ✅ |
| Robotics / embodiment | Bridge | graduate (Lynch & Park, LaValle, Tedrake, Åström-Murray) | small but gold | ✅ |
| Quantum computing | Bridge | undergrad → grad (Preskill, Watrous, Nielsen Quantum Country, QML) | good | ✅ |
| Complex systems | Bridge | undergrad → research (Newman networks, power-laws, emergence) | thin (4) | ⚠️ adequate for Bridge |
| Governance / geopolitics | Bridge | policy-grade (Int'l AI Safety Report, NIST, RSP, Bletchley, SEP-ethics) | good | ✅ |
| Computer-systems (OS/net/DB/distributed) | Bridge | undergrad → grad (OSTEP, Kleppmann, networks, DB, crypto, PL) | good (12) | ✅ |
| Physics | Literacy | intro → **graduate-heavy** (full Tong set) + OpenStax intro + Feynman | broad; skews advanced | ✅ (more than enough for Literacy) |
| Chemistry | Literacy | intro → undergrad (gen/organic/analytical/physical/biochem) | moderate (7) | ✅ |
| Biology | Literacy | intro → research (textbooks + AI-for-bio papers: AlphaFold/ESM/Evo) | good (17) | ✅ |
| Materials | Literacy | undergrad + AI-for-materials (DoITPoMS + MatterGen/GNoME) | thin (5) | ✅ ok for Literacy |
| Astronomy | Literacy | intro (OpenStax) + **mostly AI-for-astro papers** | thin on general astro | ⚠️ ok for Literacy |
| Earth / climate | Literacy | intro → undergrad (geology, meteorology, climate, oceanography) | ok (5) | ✅ |
| Electrical engineering | Literacy | undergrad (circuits, EM, DSP, power, embedded, signals) | good (12) | ✅ |
| Mechanical engineering | Literacy | undergrad (statics, materials, fluids, heat) | ok (5) | ✅ |
| Civil engineering | Literacy | undergrad (structures, transport, geotech, hydraulics) | ok (4) | ✅ |
| Chemical engineering | Literacy | undergrad (separations, process control, foundations) | thin (3) | ✅ ok for Literacy |
| Aerospace engineering | Literacy | undergrad (aerodynamics, flight vehicles, orbital) | ok (4) | ✅ |
| Biomedical engineering | Literacy | intro (biosystems eng) | very thin (1) | ⚠️ minimal |
| Rest of math (analysis/topology/algebra/number-theory) | Literacy | undergrad → grad | good | ✅ |
| Blockchain / web3 | Literacy | intro → primary (Bitcoin/Ethereum whitepapers, Vitalik) | thin (3) | ✅ ok for Literacy |

**Bottom line of the audit:** the corpus is deep+broad exactly where the mission needs it (all Core domains ✅) and appropriately thin where it doesn't (thin domains are all Literacy/Bridge, where thin is fine). **No gathering is blocking production.** The only "watch" items are the neuroscience predictive-coding skew and the lean cognitive-science shelf — both Core, both adequate, both patchable via *write-pulls-gather* if a module hits a wall.

---

## §3. The source pools (cross-cutting — feed every tier)
These five folders are **not domains**; they are where sources of each *type* landed. Every Atlas slice pulls from them:
- **`textbooks/`** (362) — owned-book extractions, **all domains mixed + variable quality** (gold: Kandel, Strang, SLP3, Huyen, Hawkins; noise: `c1-w1-4`, `la-a-z`, `ml`). The slice must name the *specific* good folders per domain.
- **`courses/`** (134) — university lecture transcripts across domains.
- **`transcripts/`** (192) — podcasts / YouTube / interviews (debates = high-value).
- **`papers/`** (16 D-groups) — landmark → SOTA, `D1`…`D16`, arXiv-ID-verified.
- **`frontier-rnd/`** (127) — company/lab R&D + AI-lab docs + 26 agent frameworks + org talk channels.

---

## §4. How the Atlas grows (just-in-time)
A per-domain slice is built **when that domain reaches the front of [`../../LEARNING/_QUEUE.md`](../../LEARNING/_QUEUE.md)** — never all 31 upfront. Each slice is a root-level file **`_ATLAS_<domain>.md`** (root-level so it publishes; sub-folder `.md` is git-ignored).

**Slice template (what each `_ATLAS_<domain>.md` contains):**
```
# ATLAS SLICE — <domain>  (tier: Core|Bridge|Literacy)
## Concept spine for this domain   (the sub-rungs to write, in dependency order)
## Grounding table                 (concept → source folders across ALL pools → level → quality)
## Best sources (the spine)        (the 3–6 authoritative sources to lean on)
## Debates/tensions to render      (where experts disagree — high value)
## Known thin spots / write-pulls-gather candidates
```

## §5. Slice index
| Slice | Domain | Status |
|---|---|---|
| [`_ATLAS_ai.md`](_ATLAS_ai.md) | AI / ML / DL / RL / LLMs / agents (Core) | ✅ built (session 22, 2026-07-02) — feeds the A3/A4 modules |

*(rows added as slices are built)*
