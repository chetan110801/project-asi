# Corpus Build — method & session handoff
**Read this first.** How to build the grounding substrate and write modules that are *distilled from real sources*, not from memory. This is the project-asi adaptation of the "hy" pipeline (`C:\Users\cheta\OneDrive\hy` — `_DOS_AND_DONTS.md` + the §11 gate), tuned to this project's **director-altitude** philosophy.

`Status: Living method · Created 2026-06-27 (v2.3) · Targets:` [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) `· Progress:` [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md)

---

## 0. The mission (why this phase exists)
The learner judged the 1000–1300 modules **"not sufficient"** — correctly. They were written from general knowledge: competent **summaries**, not **grounded distillations**. The "hy" system is the bar: every claim traceable to a verified source line, nothing important missed. To reach it, the sources must exist here as **readable, greppable text**. This phase builds that, then re-writes modules against it.

> **The one adaptation from "hy" (do not skip this):** "hy" is **exhaustive** ("miss nothing" from each philosopher). project-asi is **selective by design** — its standing philosophy is the *"rely-on-to-build" test*: include a topic **iff you'd need to understand it to build/direct AI** ([`../../INSTRUCTIONS/LEARNER_STRATEGY.md`](../../INSTRUCTIONS/) §3; memory `learning-content-philosophy`). So the merged standard is: **ground everything you say in real sources + miss nothing a *director* needs — but stay at director altitude; don't reproduce the textbook.** Grounding raises *trust and depth*, not word count for its own sake.

## 1. Session protocol (unchanged, reaffirmed)
- `.claude/settings.json`: autocompact OFF, token **countdown** on. Watch it; at ~15–20k left or a clean boundary, **STOP**, run the Handoff (§7), tell the learner to continue in a **new session**.
- Work in **many fresh sessions**. One session = a few sources gathered/extracted, or one module re-grounded. Don't cram.

## 2. Tooling available
- **Bash** (Git Bash). **`pdftotext`** is at `/mingw64/bin` (poppler) — the PDF→text tool (the Read tool's PDF *image* renderer is NOT installed). For EPUB: unzip + strip HTML, or `pandoc` if present.
- **WebSearch / WebFetch** are **deferred tools** — load them first: `ToolSearch "select:WebSearch,WebFetch"`. Use WebFetch to pull free HTML/PDF pages and the **arXiv API** (`export.arxiv.org/api/query?...`) to verify IDs.
- **arXiv**: programmatic access OK; be polite (a few req/sec). Prefer the abstract page `arxiv.org/abs/<id>`; grab PDF and, when useful, the LaTeX source (`arxiv.org/e-print/<id>`).

## 3. EXTRACT (stream ①) — the fast, legal win first
For each owned book in [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) §①:
```bash
# PDF → text (whole or page range). Poppler:
/mingw64/bin/pdftotext -layout "local_resources/RLbook2020.pdf" - > /tmp/rl.txt
# then chunk (see §5) into corpus/textbooks/sutton-barto/
```
- EPUB → unzip, concatenate the XHTML in spine order, strip tags. Keep chapter boundaries.
- **Only extract what a current/near-term module will cite** (the "rely-on-to-build" filter) — not all 250 books. A book jumps the queue when a module is about to need it.

## 4. FETCH (stream ②) — legally-free online only
- **Papers:** target list = [`../PAPERS.md`](../PAPERS.md). **Verify the arXiv ID via the API before downloading** (match title+authors+year; fix any mismatch in PAPERS.md). Save PDF (+ source if useful) → `corpus/papers/<Dn-area>/<id>_<slug>.txt` after extraction.
- **Free textbooks/courses:** URLs in [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) §A/§B/§D. PDF → `pdftotext`; HTML → WebFetch + de-chrome to text.
- **Never** fetch from pirate mirrors. Paywalled-and-not-owned → [`../REQUESTS.md`](../REQUESTS.md). Re-check for an author free copy first.

## 5. CHUNK & NAME (mirror "hy" so grounding-greps are easy)
- One folder per source. Split long text into ~5–15 KB chunks at natural boundaries (section/chapter):
  ```
  corpus/textbooks/sutton-barto/00_ch01_intro.txt, 01_ch02_bandits.txt, …
  corpus/papers/D2-transformers/1706.03762_attention.txt
  ```
- Keep text **verbatim** (fix only OCR breakage like "word- \n wrap"). Verbatim is the whole point — modules grep it to verify quotes.
- Tick the source in [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md): `not-started → fetched → extracted → chunked → used`.

## 6. The GROUNDED-SYNTHESIS standard (when re-writing modules)
When a module is (re)written against the corpus, it must pass this gate (adapted from "hy" §11, at director altitude):
- **(B) Coverage-that-matters:** every idea a *director* needs is present or cross-linked ([`../../LEARNING/CONCEPT_REGISTRY.md`](../../LEARNING/)). Not exhaustive — *sufficient for building/directing*. Diff against the source for anything load-bearing you dropped.
- **(F) Grounding:** every factual claim, number, and quote is **traceable to a corpus line**. Quotes are **verbatim** (grep them against `corpus/`). A paraphrased "quote" is a defect. Cite as the modules already do (author/year + `r-id`); keep raw arXiv IDs out of prose unless verified.
- **(C) No repetition / DRY:** one home per concept (registry); link, don't restate ([0200–1300] already do this).
- **Keep the project's voice:** concrete-example-first, define every hard word, confidence tags `[Established]/[Likely]/[Contested]/[Speculative]`, the **⚠️ honesty box**, and the **"How a director uses this / what you delegate vs own"** section. Simple sentences; depth via grounding, not jargon.
- **Freshness:** tag fast-moving 2026 claims as snapshots.
> Net effect vs. today's modules: same altitude and length-ish, but **every line now stands on a real source** and the contested/SOTA claims are checked — that is the "sufficiency" the learner wants.

## 7. Handoff (do before stopping — every session)
1. Tick [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) for every source touched; note any arXiv-ID fixes in PAPERS.md.
2. Update the project hand-off [`../library/_NEXT-SESSION-HANDOFF.md`](../library/) "Task D" line with where you stopped + the next source.
3. Commit the **tracking markdown** (corpus text stays git-ignored). Push if the learner wants the repo synced.
4. Tell the learner, one line, to continue in a new session.

---

## ▶ NEXT SESSION — START HERE
**Goal:** begin building the corpus, full breadth, spine-first ([`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) priority order). Concretely, first session of gathering:
1. `ToolSearch "select:WebSearch,WebFetch"` to load the web tools.
2. **Stream ① quick wins:** extract + chunk the **Tier-1 owned books** — `RLbook2020.pdf` (Sutton & Barto), `Bishop DL 2023`, `Huyen AI Engineering`, `Christian Alignment Problem` — into `corpus/textbooks/`. Tick coverage.
3. **Stream ② Tier-1 free:** fetch `d2l` (open PDF — easiest), `Prince UDL`, `Nielsen NNDL`, `SLP3`, `Spinning Up`; extract + chunk into `corpus/textbooks/` and `corpus/courses/`.
4. **Papers:** verify + fetch the **top ~10 spine papers** from PAPERS.md D1–D4 (Attention, GPT-3, Scaling-Laws, Chinchilla, InstructGPT/RLHF, DQN, PPO, AlphaGo, ResNet, AlexNet) into `corpus/papers/`.
5. Stop at the token boundary; run §7 Handoff.
**Then** (later sessions): widen to Tiers 2–4, and do the **first grounded module rewrite** as proof — suggest **1300 LLMs** re-grounded in the Attention paper + SLP3 + CS336 + InstructGPT, to show the standard before redoing 1000–1200.
