# Corpus Build — method & session handoff
**Read this first.** How to build the grounding substrate and write modules that are *distilled from real sources*, not from memory. This is the project-asi adaptation of the "hy" pipeline (`C:\Users\cheta\OneDrive\hy` — `_DOS_AND_DONTS.md` + the §11 gate). The binding rules are [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md); the depth standard is in §0 below.

`Status: Living method · Created 2026-06-27 (v2.3) · Targets:` [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md) `· Progress:` [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md)

---

## 0. The mission (why this phase exists)
The learner judged the 1000–1300 modules **"not sufficient"** — correctly. They were written from general knowledge: competent **summaries**, not **grounded distillations**. The "hy" system is the bar: every claim traceable to a verified source line, nothing important missed. To reach it, the sources must exist here as **readable, greppable text**. This phase builds that, then re-writes modules against it.

> **How "hy"-exhaustive applies here (learner confirmed 2026-06-27 — do not skip):** the learner wants the **full, exhaustive hy treatment, even at the cost of length.** The selectivity from the *"rely-on-to-build" test* ([`../../INSTRUCTIONS/LEARNER_STRATEGY.md`](../../INSTRUCTIONS/) §2–§3, §7b; memory `learning-content-philosophy`) governs the **two axes differently** — it does NOT mean "stay shallow":
> - **Conceptual / understanding axis → EXHAUSTIVE.** Render **every** idea, mechanism, argument, distinction, result, example, trade-off, failure mode, and live debate the sources hold on the topic. This is hy's "miss nothing," applied to the understanding a director relies on. (§3: *cut implementation depth, never conceptual depth* — so this axis is never cut and, as of v2.3, never collapsed.)
> - **Implementation / execution axis → delegated.** Not a coding tutorial; don't reproduce every proof step. Render math/mechanism for **complete insight**, leave the code/rote derivation to "direct the AI."
> - **So big topics SPLIT into several grounded sub-rungs** (numbering gaps) — e.g. "LLMs" → a cluster — each at full hy depth, rather than one thin file. Coverage + depth beat brevity (brevity last).

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
- **Video/YouTube + podcasts (transcripts, v2.4):** fetch the **transcript/captions** (e.g. a `youtube-transcript`/`yt-dlp --write-auto-sub` style pull, or the platform transcript) → `corpus/courses/<source>/`. Store text only; note speaker + date. Use these for intuition/the "why" and **ground factual claims to a primary source** (HARD_RULES §1.3, §2). Transcripts are for local note-writing only (stay git-ignored).
- **Never** fetch from pirate mirrors. Paywalled-and-not-owned → [`../REQUESTS.md`](../REQUESTS.md). Re-check for an author free copy first.

## 5. CHUNK & NAME (mirror "hy" so grounding-greps are easy)
- One folder per source. Split long text into ~5–15 KB chunks at natural boundaries (section/chapter):
  ```
  corpus/textbooks/sutton-barto/00_ch01_intro.txt, 01_ch02_bandits.txt, …
  corpus/papers/D2-transformers/1706.03762_attention.txt
  ```
- Keep text **verbatim** (fix only OCR breakage like "word- \n wrap"). Verbatim is the whole point — modules grep it to verify quotes.
- Tick the source in [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md): `not-started → fetched → extracted → chunked → used`.

## 6. The GROUNDED-SYNTHESIS standard (when re-writing modules) — EXHAUSTIVE
When a module is (re)written against the corpus, it must pass this gate (full "hy" §11 depth on the conceptual axis — see §0):
- **(B) EXHAUSTIVE coverage:** list the source(s)' major beats on the topic — **every idea, mechanism, argument, distinction, key result, example, trade-off, failure mode, and live debate** — and tick each as *present in the module* or *handed to its home* via `[[cross-link]]` ([`../../LEARNING/CONCEPT_REGISTRY.md`](../../LEARNING/)). **Diff against the source before ticking; miss nothing** that bears on understanding-to-direct. (The only thing you may leave out is pure execution/coding drill — §0.)
- **(F) Grounding:** every factual claim, number, and quote is **traceable to a corpus line**. Quotes are **verbatim** (grep them against `corpus/`). A paraphrased "quote" is a defect. Cite as the modules do (author/year + `r-id`); keep raw arXiv IDs out of prose unless verified.
- **(C) No repetition / DRY:** each idea once, in its home; different *angles* of it are good; cross-link what another rung owns (registry). With long modules this matters more, not less.
- **(D) Depth devices (hy's five), on every important idea:** plain read → deeper principle → *what it rules out* → why it matters; per example, *why this example*; **anticipate the objection** and resolve it; **name the exact misconception**; show each idea click onto the one before.
- **Structure for length:** if a topic is large, **split into several grounded sub-rungs** (numbering gaps) rather than one bloated file; use `###` sub-heads, `::: ` boxes, and lists so a long rung still reads easily.
- **Keep the project's voice:** concrete-example-first, confidence tags `[Established]/[Likely]/[Contested]/[Speculative]`, the **⚠️ honesty box**, and the **"How a director uses this / what you delegate vs own"** section. **Simple sentences (8-year-old bar); depth via grounding, not jargon.**
- **Glossing (ADOPTED v2.4):** every medium-to-advanced word / phrase / collocation / idiom / technical term is **glossed inline — general + in-context meaning, in very simple words, in brackets.** Zero bare hard items. Full rules: [`../../INSTRUCTIONS/HARD_RULES.md`](../../INSTRUCTIONS/HARD_RULES.md) §6–§7.
- **Freshness:** tag fast-moving 2026 claims as snapshots.
> Net effect vs. today's modules: **much fuller and longer** (~hy scale), big topics split into clusters, **every line stands on a verified source**, and every important idea/argument/caveat the sources hold is rendered — *only* the coding/execution grind is still delegated. That is the "sufficiency" the learner asked for.

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
