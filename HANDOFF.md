# HANDOFF — pick the work up here

**For the AI in a new Claude Code session.** Tracked in git on purpose, so it survives a machine. Last updated **2026-09-09**.

---

## 📋 PASTE THIS INTO THE NEW SESSION

> Read `HANDOFF.md` in this repo, top to bottom, then read `LEARNING/THE_PLAN.md` and `INSTRUCTIONS/HARD_RULES.md`. I'm the learner. Continue from the **"What's next"** section — tell me which option you'd pick and why, then start. Don't re-plan what's already decided.

That's all you need to paste. Everything below is for the AI to read.

---

## 1. What this project is

An investigation into **the approaches to AGI** — what would actually be required to build it — written as one readable book, plus a machine for producing that book. It has run since 2026-06-20, ~83+ commits.

- **The spine:** [`LEARNING/APPROACHES_TO_AGI.md`](LEARNING/APPROACHES_TO_AGI.md) — **twelve bets** on how general intelligence gets built. Each has a card, most have one or two deep dives.
- **The forward page:** [`LEARNING/THE_PLAN.md`](LEARNING/THE_PLAN.md) — argues the map is finished, more reading has low marginal value, and the binding constraint is **contact with reality**.
- **The binding rules:** [`INSTRUCTIONS/HARD_RULES.md`](INSTRUCTIONS/HARD_RULES.md). Two matter most: **§2.6 — do a live web check before writing anything** (the corpus is stale), and **zero repetition** — explain a concept in full at first occurrence, reference it after. Check `LEARNING/CONCEPT_REGISTRY.md` before explaining anything.
- **The reader:** `py -3 build_site.py` compiles `LEARNING/**/*.md` into one offline `index.html`. **41 pages across 7 groups.** Rebuild after any content change.
- Full orientation: [`AI_ONBOARDING.md`](AI_ONBOARDING.md). Repo map: [`README.md`](README.md).

---

## 2. Who the learner is *(matters for every decision)*

25 years old. One year as a data-science apprentice. Currently preparing for **data-science / ML-engineer interviews** — SQL, DSA, pandas/NumPy, classical ML, DL basics, NLP, LLM internals, AI engineering, MLOps.

**The plan he has stated:** land a DS/MLE role → get into an AI lab doing an approach he cares about → do original research → eventually **start his own lab**. The lab job is an intermediate step, not the destination.

**What he wants from the map:** understand *all* the approaches deeply enough to take the best idea from each and combine them — explicitly **not** to pick one and follow it. (DeepMind's own founding is the precedent. The amendment on record: a synthesis is only real if you know where each piece *breaks*, and you learn that by hitting the break — so breadth across all twelve, depth in one for calibration.)

**Where his interest actually points:** systems with **less human intervention — where the agent sets its own goals.** That is **AP9 (open-endedness)** and **AP12 (OaK)**, with AP8's ARC-AGI-3 and AP4's intrinsic-motivation frontier as the ring around them. Conveniently, that cluster is also the cheapest to enter.

**Two constraints he has been explicit about:**
1. **Don't write him prerequisite curricula.** He has learned and forgotten maths/ML/DL several times and will revise them for interviews anyway. Anything lookup-able should be looked up. The one prerequisite that *is* named: **reinforcement learning — Sutton & Barto Ch. 1–6 and 13** (free), because his interview prep omits it and five bets need it.
2. **He cannot yet read frontier papers cold** and intends to use the AI to do it. Established working rule: *he does pass one himself* (5 min — title, abstract, intro, conclusion, figures, decide if it deserves more), *then hands it over.* Handing a paper over cold trains nothing.

Style: simple language, real depth, self-critique rewarded, hype punished. He pushes back well — take it seriously when he does.

---

## 3. What happened on 2026-09-09 (this session)

Six commits, all pushed. `git log 5b84d6f..HEAD` for the detail.

| | What |
|---|---|
| `ea66ebe` | **Reader nav made invisible** (his request) — the top-left menu/home/back are `opacity:0` at rest, on hover and on touch, but still laid out and hit-testable (44px on phones). Only keyboard focus reveals them. Verified in headless Chrome at 390×844, 768×1024, 1440×900. Also repaired the front door: `START_HERE.md` had a dead link since the July pivot, `README.md`'s tree described pre-pivot folders, `AI_ONBOARDING.md` still said "version 1.2". |
| `a080b7c` `adc200d` `eb910b1` | **New group ⑥ · Entry ramps** — the resource-and-route pages he asked for. [`00_the-shared-core.md`](LEARNING/60-entry-ramps/00_the-shared-core.md) (cut to 2.6k words after he said prerequisites are handled: the three piles — internalise / reference / delegate — the rule *delegate execution, never judgement*, a 20-concept judgement floor, permission to forget, the once rule). Then [`01_ap9-open-endedness.md`](LEARNING/60-entry-ramps/01_ap9-open-endedness.md), the first full ramp. |
| `4674797` | **AP12 added — a twelfth bet the map had missed.** He sent the Sutton/Javed Sequoia podcast; a grep for "OaK" and "Alberta Plan" returned zero hits. New card [`12_ap12-oak-experience-only-agents.md`](LEARNING/20-the-approaches/12_ap12-oak-experience-only-agents.md), new cross-cutting page [`03_continual-learning-and-plasticity.md`](LEARNING/30-across-the-approaches/03_continual-learning-and-plasticity.md), new ramp [`02_ap12-oak-continual-learning.md`](LEARNING/60-entry-ramps/02_ap12-oak-continual-learning.md). Map, heat axis, cross-cutting list and CONCEPT_REGISTRY updated. |
| `593f3a2` | **AP9 ramp Part 5 rebuilt after he challenged it** — see §5, the process lesson. |

---

## 4. The ramp template *(now established — follow it)*

Each approach ramp, in `LEARNING/60-entry-ramps/`:

① what this bet uniquely claims *(brief — the card already says it)* → ② the **🧠 delta**: the 3–6 concepts beyond the shared core you must actually hold → ③ **books** *(and say plainly when none exist)* → ④ **theses** *(in young fields, dissertations ARE the textbook)* → ⑤ the **paper ladder** in rungs, each paper tagged 🟢 read yourself / 🟡 method with me / 🔴 hand to me first → ⑥ **video**, organised by kind → ⑦ **code** → ⑧ **open problems** → ⑨ **your first experiment** *(must fit 30 GPU-hours)* → ⑩ **where to publish with no affiliation** → ⑪ **the best idea in this bet** — what a synthesis would take, and what it would leave.

⑪ is what makes twelve ramps compose into one argument instead of twelve reading lists. Don't drop it.

---

## 5. Process lessons learned this session *(apply these)*

- **🔴 Do not build a resource section from one curated index.** The AP9 ramp's first video section came entirely from `awesome-open-ended`'s Videos list — four items — and asserted no course existed anywhere. A real sweep found ~130 videos and a 152-minute ICML tutorial. **A curated index tells you what its maintainer curated; its gaps are invisible from inside it.** Verify independently.
- **🔴 Grep this project's own corpus first.** `RESOURCES/corpus/transcripts/` holds **5,654** transcript files — including six Kenneth Stanley conversations the AP9 ramp initially failed to cite, in a section about videos, on a card that was *grounded in them* in July.
- **`yt-dlp` is installed** at `C:\Users\cheta\AppData\Local\Programs\Python\Python314\Scripts\yt-dlp` and is the right tool for surveying video — `ytsearchN:query` with `--flat-playlist --print`. Run long sweeps in the background.
- **The freshness rule needs widening.** AP12 was missed because §2.6's pass checks *benchmark numbers* and not *named research programmes*. A Turing Award winner's architecture slipped through for a year. **Consider amending HARD_RULES §2.6 — this has not been done yet.**
- **Verify reader changes in headless Chrome**, not by eye. Chrome is at `C:\Program Files\Google\Chrome\Application\chrome.exe`; `--headless=new --screenshot` and a DOM-probe harness both work.
- **Python is `C:\Users\cheta\AppData\Local\Programs\Python\Python314\python.exe`** — bare `python` hits the Microsoft Store stub and fails.
- **Bash heredocs break** on long markdown with mixed quoting. Write the content to a scratchpad file, then have a short Python one-liner splice it in.
- **Don't infer pronouns.** Use they/them for anyone whose pronouns aren't stated.

---

## 6. What's next — pick one and say why

**Option A — audit the AP9 ramp's paper ladder independently.** *(This is what was on the table when the session ended, and the learner was told it was worth doing.)* Parts 2, 3 and 4 of the AP9 ramp — books, theses, the ~30-paper ladder — lean on the same `awesome-open-ended` index that turned out to be four items deep on video. The load-bearing items were verified; the rest were not. Before he spends months on that ladder, run the same kind of independent sweep: arXiv, Semantic Scholar, the QD community hub, recent surveys. Expect to find missing papers and at least one wrong attribution. **Cheapest way to protect months of his time.**

**Option B — the AP8 ramp.** Program synthesis / ARC. It is where his cluster meets a live public scoreboard (ARC-AGI-3: humans 100%, best frontier model 0.51%, prizes on Kaggle). Was the original next-in-queue before AP12 jumped ahead.

**Option C — ground the AP9 × AP12 research question.** The most interesting thing this session produced, written into the AP12 ramp's Part 7: *open-ended runs are known to stall and nobody knows why; networks are known to silently lose plasticity over long task sequences; nobody appears to have checked whether the second explains the first.* It is cheap to test, sits exactly where his two interests meet, and is publishable either way. **Flagged as unverified against the literature — one search pass is not a review.** Grounding it properly is one session and would be his first turn of THE_PLAN's actual loop rather than more library.

**Recommendation on record:** A then C, unless he says otherwise. A is insurance on work already shipped; C is the first real move from reading to doing.

**After that, the ramp queue:** AP8 → AP4 → AP5 → AP3 → AP2 → AP1 → AP6 → AP7 → AP10 → AP11, then the approaches outside the map (spatial intelligence / World Labs, continual learning already covered by AP12, mechanistic interpretability, AI-for-math and formal reasoning, alternative architectures, multi-agent, neuroevolution), then a **synthesis capstone** — what the best of each is, and which combinations are actually coherent.

---

## 7. Known outstanding items

- **From the [2026-07-21 audit](REVIEWS/AUDIT_2026-07-21_v3.0.md), all still `QUEUED`:** the twelve map cards are unscannable single-paragraph walls (finding C1, highest priority in the content queue); two rival naming schemes live side by side (`P1–P7` in `INSTRUCTIONS/`+`RESOURCES/LANDSCAPE.md` vs `AP1–AP12` in `LEARNING/`); `WHATS_NEW.md` and `INSTRUCTIONS/VERSION_HISTORY.md` have outgrown their purpose; the dead corpus-campaign planning files should be archived.
- **`HARD_RULES §2.6` has not been amended** despite the AP12 miss proving it needs to be.
- **`RESOURCES/library/_NEXT-SESSION-HANDOFF.md`** (315 KB) is the old handoff — pre-v3.0, gitignored, local-only. Superseded by this file. Read it only for archaeology.
- **Session transcripts are deleted after 30 days** by Claude Code's default cleanup (`cleanupPeriodDays` is unset). Everything before ~2026-08-10 is gone. Offered to raise it; not yet done.

---

## 8. Mechanics

```bash
# rebuild the reader after any LEARNING/ change
py -3 build_site.py

# checks that must pass
grep -c 'wikilink missing' index.html   # must be 0
grep -c 'sortkey:' index.html           # must be 0 (frontmatter leak)
```

Commit style: `feat(scope): …` / `fix(scope): …`, message says *what and why*. End with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Push to `origin main` — the learner has authorised pushes of his own work.

**Adding a new page:** frontmatter (`id`, `sortkey`, `title`, `domains`, `level`, `prereqs`, `provides`, `status`, `rev`, `created`, `updated`) → "You are here" box → "Where the facts come from" *(dated)* → "In one minute" → body → **Honesty box** *(mandatory — state what you did not verify)* → Connections → Check yourself → Revision notes. Callouts are `::: key` / `::: note` / `::: warn` / `::: vocab`, closed with `:::`. A new folder needs a row in `GROUP_ORDER` in `build_site.py`.
