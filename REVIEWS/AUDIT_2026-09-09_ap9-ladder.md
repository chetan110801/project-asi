# AUDIT — the AP9 ramp's resource spine

**An independent check of the reading list the learner was about to spend months inside.**

`Date: 2026-09-09 · Audits: LEARNING/60-entry-ramps/01_ap9-open-endedness.md, Parts 2–4 and 6 (books · theses · the ~30-paper ladder · code)`
`Method: arXiv API verification of every ladder entry + a 22-query independent discovery sweep + targeted web checks · Outcome: drove rev 3 of the ramp`

> **Why this audit exists.** Rev 2 of the AP9 ramp rebuilt Part 5 (video) after the original was found to have been written entirely from the Videos section of one GitHub index — four items, and an assertion that no course existed "anywhere — I looked." A real sweep found ~130 videos and a 152-minute ICML tutorial. **Parts 2, 3 and 4 came from the same index on the same day and were never independently checked.** The ramp's own honesty box said so. This closes that.

---

## Headline

**The spine is sound. The edges are not, and the habit that produced them has not been fixed.**

**19 of the ~30 ladder entries verified exactly right** — title, authors, year and venue all correct, including every load-bearing paper in Rungs 1–3. The ladder is not junk and the learner can trust its shape.

Three findings matter more than the rest:

1. **Part 2 repeats the exact error rev 2 was written to fix.** It asserts that no textbook exists — *"this is genuinely true of the field, not a gap in searching"* — without searching the project's own corpus, which holds a **2025 CRC Press textbook with a section on novelty search and MAP-Elites in its index** (A5).
2. **The corpus contains recorded interviews with the authors of five papers on this ladder, and Part 5 lists none of them** — including no Jeff Clune interview at all, in a rung Clune co-authored half of (B13). For a learner whose stated blocker is reading papers cold, this was the most valuable thing already sitting on his disk.
3. **One of two ⭐-starred papers in the frontier rung is materially mis-described** — its description was inferred from a truncated title, and the real paper does something else (A1).

The ladder also **omits the paper that named the subfield**, a ***Nature* paper by the field's own founders**, and — most telling for a project about judging bets — **contains no technical critique of quality-diversity at all**.

**Thirteen verified additions** are listed in section B. All were found without using the index under audit.

---

## Method — stated plainly, so the next session can judge it

1. **Verification.** A script queried the arXiv API (`ti:` search, 3.2 s spacing, loose `all:` fallback) for all ~30 ladder entries and diffed the returned title / author list / v1 date / journal-ref / venue comment against what the ramp claims.
2. **Discovery.** A separate 22-query sweep of the arXiv API, sorted newest-first, across *open-endedness · open-ended AI · quality-diversity · novelty search · MAP-Elites · unsupervised environment design · automatic curricula · AI-generating algorithms · self-improving agents · autotelic · intrinsic motivation · surveys* — plus **seven queries aimed specifically at the AP9 × AP12 question** (section D).
3. **Targeted checks.** Web search for the items arXiv could not match — non-arXiv journal papers, venue claims, retitled preprints.
4. **Corpus grep** of `RESOURCES/corpus/` (6,174 transcript files).
5. **Deliberately not used: `awesome-open-ended`** — the index under audit. Everything in section B was found independently, then cross-checked.

---

## A. ERRORS — things the ramp currently states that are wrong

**A1. 🔴 A ⭐-starred paper is described as something it is not.**

The ramp's Rung 4 lists:

> ⭐ Earle et al., **In Search of the Ingredients of Open-Endedness** (2026) — *"Newest, and the most useful for finding a question of your own — it tries to isolate what actually makes a system open-ended rather than merely busy."*

The real paper is **"In Search of the Ingredients of Open-Endedness: **Replicating Picbreeder with Large Vision-Language Models**"** — Sam Earle, Kai Arulkumaran, Andrew Dai, Akarsh Kumar, Julian Togelius, Sebastian Risi; arXiv **2605.23908**, to appear at **GECCO 2026**.

It is a **replication study**: re-running Picbreeder's human-in-the-loop divergent search with VLMs standing in for the humans. That is interesting and relevant — but it is not an attempt to "isolate what makes a system open-ended rather than merely busy." **The description was written from the title's first half, which is a colon away from saying what the paper does.** Severity is high because this is one of two starred items in the rung and it is sold as the best place to find a research question.
→ *Fix `SHIPPED`:* full title, correct description, and Picbreeder itself added to Rung 1 as the thing being replicated.

**A2. 🟡 The ladder mixes preprint years and venue years with no rule.**

`ADAS` is dated **2025** (arXiv v1 **2024-08-15**, ICLR 2025). `Prioritized Level Replay` is dated **2021** (arXiv v1 **2020-10-08**, ICML 2021). `Darwin Gödel Machine` is dated **"ICLR 2026"** (arXiv v1 **2025-05-29**). Each individual date is defensible; together they are not, because **Rung 4 is presented as a chronology** ("2022–2026", "the hinge", "everything after this is downstream") and an inconsistent sort silently misorders the field's history.
→ *Fix `SHIPPED`:* every entry now carries **arXiv v1 year + venue** where both exist, so the chronology is readable and the citation is complete.

**A3. 🟢 TerraLingua's author list is reordered in a way that implies the wrong leads.**

Ramp: *"Paolo, Meyerson, Miikkulainen et al."* Actual: **Giuseppe Paolo, Jamieson Warner, Hormoz Shahrzad, Babak Hodjat, Risto Miikkulainen, Elliot Meyerson** — Meyerson is **last** author, not second.
→ *Fix `SHIPPED`.*

**A4. 🟢 Two titles have drifted from what the ramp records.**

- *Automated Capability Discovery via Model Self-Exploration* → the arXiv title is now **"…via Foundation Model Self-Exploration"** (Cong Lu, Shengran Hu, Jeff Clune; **2502.07577**, ICLR 2025). The ramp's version matches the ICLR listing, so this is version drift rather than an error — but the arXiv id was missing, which is what makes it findable.
- *Safety is Essential for Responsible Open-Ended Systems* → **2502.04512** has been **retitled in a later version to "Safety Must Precede the Deployment of Open-Ended AI"** (Sheth, Wehner, Abdelnabi, Binkyte, Fritz). Searching the old title still works; the new one is what will be cited.
→ *Fix `SHIPPED`:* arXiv ids added throughout, both titles noted.

**A5. 🔴 Part 2 asserts a negative without checking the corpus — the *exact* error rev 2 was written to fix.**

Part 2 opens:

> **"Be clear-eyed: there is one real book, and it is not a textbook. This is genuinely true of the field, not a gap in searching.** Open-endedness as a named research programme is about ten years old; **nobody has written the textbook yet.**"

The project's own corpus contains **Hitoshi Iba, *Deep Swarm and Evolution for Generative Artificial Intelligence*, CRC Press, 1st ed. 2025** (University of Tokyo) — 40 chunks at `RESOURCES/corpus/textbooks/hitoshi-i-deep-swarm-and-evolution-for-generative-artif/`. It has:

- **§2.6, an entire section titled "Novelty search"**, citing Lehman & Stanley, deriving novelty against an archive of previously discovered individuals, and contrasting it with fitness-based selection;
- **MAP-Elites** in the index at p. 57;
- **"progressive minimal criteria novelty search"** as an index sub-entry at p. 55;
- coverage of coevolution, and citations into the ALife literature (e.g. Hintze & Schossau, *Sexual selection compared to novelty search*, ALIFE 2020).

**Being fair to the claim:** this is not a textbook *of open-endedness* — it is an evolutionary-computation and swarm-intelligence textbook that treats novelty search as one of its topics. The narrow reading of Part 2 survives. **The sentences actually on the page do not.** "There is one real book" and "nobody has written the textbook yet" are both false as written, and a learner would use them to stop looking.

Severity is high not because the fact matters most, but because **the mechanism is identical to the Part 5 failure this ramp already documented**: a confident negative, asserted without searching, in a section whose honesty box warns that this exact section was built from one index. Rev 2 fixed the instance; it did not fix the habit.
→ *Fix `SHIPPED`:* Iba added to Part 2, the claim narrowed to what is actually true, and Part 3's thesis advice re-pointed at a verified thesis (B6).

**A6. 🟢 The corpus `::: key` box understates the corpus by a wide margin.**

The box tells the learner to grep the corpus and cites *"six Stanley conversations."* An accurate sweep — `grep -rli`, no `-F` (see the process note below) — finds **58 files mentioning "open-endedness", 16 mentioning "novelty search", 15 mentioning "quality diversity", and 55 mentioning Kenneth Stanley.** Among them, recorded interviews with the **authors of five papers on this very ladder** (listed as B13).
→ *Fix `SHIPPED`.*

---

## B. MISSING — verified real, absent from the ramp

All arXiv ids below were confirmed against the API in this pass.

### 🔴 High — these change what the ladder is

**B1. The paper that named the subfield.**
**Pugh, Soros & Stanley (2016), *Quality Diversity: A New Frontier for Evolutionary Computation*** — *Frontiers in Robotics and AI* 3:40. Non-arXiv, open access. The ladder teaches quality-diversity as delta-concept #3 and walks through novelty search → local competition → MAP-Elites without ever citing **the paper that defined QD as a research programme**.

**B2. Go-Explore — a *Nature* paper by the field's own founders.**
**Ecoffet, Huizinga, Lehman, Stanley & Clune, *First return, then explore*** — arXiv **2004.12919**, **Nature 590, 580–586 (2021)**. The ladder cites Ecoffet's *safety* paper in Rung 5 but omits his major technical result — an archive-of-stepping-stones method that solved Montezuma's Revenge and Pitfall. It is the clearest demonstration in the whole literature that the archive idea transfers into hard RL, which is precisely the claim Part 10 makes when it says "take the archive."

**B3. There is no critique of quality-diversity anywhere in the ladder.**
**Batra, Tjanaka, Nikolaidis & Sukhatme (2024), *Quality Diversity for Robot Learning: Limitations and Future Directions*** — arXiv **2407.17515**, GECCO 2024. It argues that many QD results are illusory: tasks framed as "learn a diverse archive of policies" are often solvable by *one* goal-conditioned policy plus a classical planner, at O(1) space instead of O(archive). That is a direct attack on the value proposition of the field's most-used method. Rung 5 covers *safety*; Rungs 1–4 contain **no paper that argues the approach does not work**. For a project whose stated purpose is judging bets and knowing where each breaks, that is the most important single omission in the ladder.

### 🟡 Medium — real gaps in coverage

**B4. The QD reference layer.**
- **Chatzilygeroudis, Cully, Vassiliades & Mouret (2020), *Quality-Diversity Optimization: a novel branch of stochastic optimization*** — arXiv **2012.04322**. The survey.
- **Cully & Demiris (2017), *Quality and Diversity Optimization: A Unifying Modular Framework*** — arXiv **1708.09251**. The paper that shows novelty search, MAP-Elites and their variants are one algorithm with swappable parts — the single most useful thing to read before designing a QD experiment.

**B5. Cully, Clune, Tarapore & Mouret (2015), *Robots that can adapt like animals*** — arXiv **1407.3501**, **Nature 521, 503–507**. The damaged-robot result that made MAP-Elites famous. The ladder has the MAP-Elites *algorithm* paper and not the result that made anyone care.

**B6. The Samvelyan / UED line, including a verified thesis.**
- **Samvelyan et al. (2023), *MAESTRO: Open-Ended Environment Design for Multi-Agent RL*** — arXiv **2303.03376**, ICLR 2023.
- **Samvelyan et al. (2024), *Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts*** — arXiv **2402.16822**. QD pointed at LLM red-teaming; the clearest existing bridge from this approach to paid work.
- ⭐ **Samvelyan (2025), *Robust Agents in Open-Ended Worlds*** — arXiv **2512.08139**, **PhD thesis**. Part 3 of the ramp says *"I have not verified specific titles, so treat this as a search instruction"* and points at Cully's and Clune's groups. **Here is a verified, free, recent thesis in the UED lineage** — which is the half of Rung 2 the ramp has no thesis for.

**B7. A rival formal definition of open-endedness.**
**Xu, Zhu & Van Roy (2026), *An Information-Theoretic Definition for Open-Ended Learning*** — arXiv **2606.08369**. Rung 3 presents Hughes et al. (2024) as *the* formal definition — "open-endedness relative to an observer." This is a competing formalisation from a serious source, published two years later. Open problem #1 in Part 7 says nobody can measure open-endedness; this is somebody trying.

### 🟢 Low — worth adding, not urgent

**B8.** **Kumar, Clune, Lehman & Stanley (2025), *Questioning Representational Optimism in Deep Learning: The Fractured Entangled Representation Hypothesis*** — arXiv **2505.11581**. All three founders plus Kumar, arguing that what evolved/open-ended search produces is *representationally* different from what SGD produces. Bears directly on Part 10's "what a synthesis takes."
**B9.** **Kumar, Lu, Kirsch, Tang, Stanley, Isola & Ha (2024), *Automating the Search for Artificial Life with Foundation Models*** (ASAL) — arXiv **2412.17799**.
**B10.** **Lu, Hu & Clune (2024), *Intelligent Go-Explore*** — arXiv **2405.15143**, ICLR 2025. Go-Explore with a foundation model choosing which states are interesting — the exact Rung-4 pattern, applied to B2.
**B11.** **Lim, Allard, Grillotti & Cully (2022), *Accelerated Quality-Diversity through Massive Parallelism*** — arXiv **2202.01258**. **The QDax paper.** Part 6 recommends QDax by name and cites pyribs' paper but not QDax's.
**B12.** **Iacob, Jovanović, Shen, Burkhardt, Kurmanji, Tastan et al. (2026), *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators*** — arXiv **2606.26294**. A direct successor to the DGM. **Note: not Clune's group** — a different team, which is itself the news.

### 🔴 High, and already owned — author interviews sitting in the corpus

**B13. The corpus holds recorded interviews with the authors of at least five ladder papers, and Part 5 lists none of them.**

This matters more than any single paper above, because the learner's stated blocker is that he cannot yet read frontier papers cold, and Part 5 ③ exists specifically to fix that with explainers. **An interview with the author is a better explainer than a third party's walkthrough**, and these are already local, already text, already searchable.

| In the corpus | The ladder paper it explains |
|---|---|
| `twiml-ai-podcast/8L4lDCCAsMQ_accelerating-intelligence-with-ai-generating-algorithms-with…` | **AI-GAs** — Rung 3, by Clune himself |
| `twiml-ai-podcast/5cuRo0bCmPY_is-artificial-superintelligence-imminent-with-tim-rockt-schel` | **Open-Endedness is Essential for ASI** — Rung 3 |
| `twiml-ai-podcast/C5EyZAYlW7E_automated-design-of-agentic-systems-with-shengran-hu-700` | **ADAS** — Rung 4, by its first author |
| `machine-learning-street-talk/1kwbp8hRRfs_can-ai-improve-itself-chris-lu-robert-lange-cong-lu` | **The AI Scientist** — Rung 4, three of its authors |
| `machine-learning-street-talk/EInEmGaMRLc_when-ai-discovers-the-next-transformer-robert-lange` | **Darwin Gödel Machine** — Rung 4 ⭐, a co-author |
| `twiml-ai-podcast/1igh4oas1Ls_genie-3-…-jack-parker-holder` | **ACCEL** — Rung 2, by its first author |

**And separately: `machine-learning-street-talk/mw5WIDGRLnA_don-t-invent-faster-horses-prof-jeff-clune`.** Part 5 ④ lists six Stanley conversations, one Lehman, one Rocktäschel, one Togelius and a POET episode — and **no Jeff Clune interview at all**, despite Clune being an author on roughly half of Rung 4.
→ *Fix `SHIPPED`:* new subsection in Part 5.

---

## C. CONFIRMED CORRECT — what the audit did *not* find fault with

Verified exactly as claimed, against the arXiv record: **Mouret & Clune 2015** (1504.04909) · **POET** (1901.01753) · **Enhanced POET** (2003.08536) · **PAIRED / Dennis et al.** (2012.02096) · **Prioritized Level Replay** (2010.03934) · **ACCEL** (2203.01302) · **Open-Ended Learning Leads to Generally Capable Agents** (2107.12808) · **AI-GAs** (1905.10985) · **Hughes et al. 2024** (2406.04268) · **Knightian Blindspot** (2501.13075) · **ELM** (2206.08896) · **OMNI** (2306.01711) · **OMNI-EPIC** (2405.15568) · **Voyager** (2305.16291) · **Eureka** (2310.12931) · **The AI Scientist** (2408.06292) and **v2** (2504.08066) · **Foundation Model Self-Play** (2507.06466, RLC 2025) · **Ecoffet, Clune & Lehman 2020** (2006.07495).

**The Darwin Gödel Machine's "ICLR 2026" claim is correct** — arXiv 2505.22954, poster at ICLR 2026. Worth stating because it was the venue claim most likely to be wrong.

Non-arXiv Rung 1 entries (*Abandoning Objectives*, *Virtual Creatures*, *Chromaria*, *Minimal Criterion Coevolution*, *The Last Grand Challenge*) returned no arXiv match, which is expected — they are journal, GECCO and O'Reilly items. **Their attributions were not independently re-verified in this pass** (see section E).

---

## D. The AP9 × AP12 question — the verdict the AP12 ramp asked for

The AP12 ramp's Part 7 ② proposes, with an explicit caveat that one search pass is not a review:

> *Does an open-ended system's solver lose plasticity, and if so, is that what makes open-ended runs stall?* … "Nobody appears to have checked whether the second explains the first."

**Verdict: the question survives, but two of its premises need correcting, and the neighbourhood is now occupied.**

**D1. Somebody has connected these two literatures — in the opposite direction.**
**Lillo & Cheney (2026), *Beyond Single-Model Optimization: Preserving Plasticity in Continual Reinforcement Learning*** — arXiv **2604.15414** (v1 April 2026, revised June 2026). They introduce **TeLAPA**, which takes the QD idea — behaviourally diverse archives instead of one retained policy — and uses it to **fix** loss of plasticity in continual RL. From the abstract: retaining a single successful policy "may no longer provide a reliable starting point for rapid adaptation after interference, reflecting a form of **loss of plasticity** that single-policy preservation cannot address."

So the claim "nobody has connected these" is **no longer true**. The direction, though, is **AP9 → AP12**: use archives to cure plasticity loss. The proposed question runs **AP12 → AP9**: does the *solver inside* an open-ended system lose plasticity, and does that explain stalling. **That direction is still open.**

**D2. "They stall and nobody knows why" is overstated.**
Enhanced POET's own paper names two stagnation modes explicitly — domains stop increasing in complexity, or solutions get stuck sub-optimally and fail to solve solvable challenges. The field has *named* the failure; what it lacks is a *mechanism*. That is a better and more defensible framing of the gap, and it makes the question sharper rather than weaker.

**D3. The competitor is identifiable, and is in this project's own corpus.**
Nick Cheney's group is the obvious team to run the reverse direction next. `RESOURCES/corpus/courses/mit-res9003-brains-minds-machines/_qTVDxXBK5A_nick-cheney-capturing-neural-plasticity-in-deep-networks.txt` — a Cheney talk on exactly this — has been sitting in the corpus the whole time.

**Net: this is what the honesty box predicted would happen, and it is a good outcome.** The question is not dead; it is one direction narrower, has a named baseline (TeLAPA), a named competitor, and a defensible framing. Grounding it properly is now a smaller job than it was this morning.

---

## E. What I did *not* check — so the next session knows the edges

- **I did not read the papers.** This audit verifies that entries **exist, are correctly attributed, and say what the ramp says they say at abstract level**. The 🟢/🟡/🔴 difficulty tags are still estimates.
- **The five non-arXiv Rung 1 entries were not re-verified** against their journal records. They are the oldest and most-cited items in the ladder and the least likely to be wrong, which is why they were deprioritised — not because they were checked.
- **The books in Part 2 were not re-verified** (prices, editions, the `gameaibook.org` free copy).
- **Discovery was arXiv-first.** Semantic Scholar was rate-limited (HTTP 429) throughout and its citation graph was never queried. A citation-graph sweep around POET and Hughes 2024 would likely surface more than this pass did, and is the obvious next increment.
- **"There is no technical critique of QD in the ladder" is a claim about the ladder, not the field.** B3 is one such critique; there are probably others.

---

## Process lesson — the trap that put a false claim into the first draft of this very report

**This audit made the mistake it was auditing, and the draft went to disk before it was caught.** An earlier version of A5 read: *"a term sweep of the whole corpus returns zero files for MAP-Elites, quality diversity and novelty search — the corpus holds this field's philosophy and not its mechanics."* Every word of that was wrong, and it was wrong in the confident direction.

**Cause 1 — `grep -F` is silently broken in this environment.** Combining `-F` with `-l`/`-i`/`-r` returns **zero matches on files that definitely contain the string**:

```bash
grep -li  'open-endedness' "$file"   # → 1  (correct)
grep -lFi 'open-endedness' "$file"   # → 0  (silently wrong)
```

**Cause 2 — the `Grep` tool (ripgrep) respects `.gitignore`**, and `RESOURCES/corpus/` is gitignored by design (HARD_RULES §3.2). Ripgrep reports **"No files found"** for the entire corpus. Reaching for it as the "more reliable" fallback reproduced the same zero.

Two independent tools returned nothing, which is the most persuasive possible form of a wrong answer. **For corpus searches: `grep -rli`, never `-F`, never the `Grep` tool.**

**The transferable rule, and it is the same one the ramp already learned once:** a search that returns nothing is not evidence of absence until the search itself has been tested against a positive control. The check that caught this took one command — grep a file known to contain the term. Both of this session's false negatives, and Part 5's original failure, would have been caught by it.

---

## Scorecard

| | |
|---|---|
| Ladder entries verified | **~30** |
| Verified correct | **19 exactly right**, including every Rung 1–3 load-bearing paper |
| Errors found | **6** — 2 high (A1, A5), 1 medium (A2), 3 low (A3, A4, A6) |
| Missing items found | **13 verified additions** (B1–B13), 4 of them high-severity |
| Biggest single finding | **Part 2 asserts "no textbook exists" without checking the corpus, which holds one** (A5) — the same failure mode rev 2 was written to fix |
| Most immediately useful | **Author interviews for five ladder papers, already in the corpus** (B13) |
| Research question | **Survives, re-framed** — one direction narrower, with a named baseline and competitor (D) |
| Verdict on the ladder | **Trustworthy in shape, incomplete at the edges, and two confident negatives were unchecked** |

**Was the audit worth running?** Yes, and for a reason different from the one predicted. The prediction was *"expect to find missing papers and at least one wrong attribution"* — that came true, mildly: one wrong description, four small attribution defects, thirteen omissions, and a spine that held up well.

The finding that justifies the session is the one nobody predicted: **the ramp's problem is not its sources, it is a habit of asserting negatives.** "No course exists anywhere" (rev 1, wrong). "Nobody has written the textbook yet" (rev 2, wrong). Both were confident, both were unchecked, both were disprovable from material already on the learner's own disk. Fixing the two instances is the small half of the job; **the standing rule now added to the ramp — never assert an absence without a positive-control search — is the large half.**

And this report reproduced the same error in its own first draft before catching it, which is the strongest available evidence that the rule is needed rather than obvious.
