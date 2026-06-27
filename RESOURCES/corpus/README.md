# RESOURCES/corpus — the grounding substrate

**What this is:** the actual **source text** (landmark papers, free textbooks, open course notes) extracted to `.txt` and chunked, so learning modules can be **distilled from and verified against real sources** — not written from memory. This is the project-asi equivalent of the `_corpus/` folders in the "hy" knowledge system: the thing that makes a module *grounded* instead of a competent summary.

> **Why it exists:** modules written from general knowledge read thin. The fix (the standard we're adopting) is the "hy" pipeline — **miss nothing → understand deeply → no repetition → simple & beautiful → concise (last)**, with **every claim traceable to a verified source line.** That requires the sources to be present as readable, greppable text. That's this folder.

## Layout
```
corpus/
├── _ACQUISITION_PLAN.md   ← the GET-list (free full-text, with URLs) + BUY-list, full breadth, prioritized
├── _CORPUS_BUILD.md       ← HOW: the download/extract/chunk method + the grounded-synthesis standard + the session handoff
├── _COVERAGE_MAP.md       ← status board: every target source → not-started / fetched / extracted / chunked / used
├── papers/                ← arXiv landmark papers as text, by PAPERS.md area (D1…D12)   [git-ignored]
├── textbooks/             ← free full-text books, chunked, one folder per book           [git-ignored]
└── courses/               ← open course notes / lecture transcripts                       [git-ignored]
```

## Git treatment (important)
- **Tracked & published:** the three `_*.md` files at this root (plan, method, coverage) — so the structure and progress are visible on GitHub.
- **Git-ignored (local only):** everything under `papers/`, `textbooks/`, `courses/`. The extracted text is a **working substrate** (redistribution/copyright varies by source, and it gets large), kept local like `local_resources/`. The **published product is the grounded modules in `LEARNING/`**, not the raw sources — exactly as "hy" publishes its `Synthesis/`, not its `_corpus/`.

## Hard rule — legality
Only **legally-free full text** goes here: arXiv papers, and textbooks/courses the authors publish free (Goodfellow, d2l, Sutton & Barto, Nielsen, Prince, Murphy, Jurafsky & Martin, MacKay, Boyd, Spinning Up, Stanford notes, …). **No pirated/paid books.** Anything good-but-paywalled is routed to [`../REQUESTS.md`](../REQUESTS.md) or read from the user's own [`../library/`](../library/) — never scraped from a pirate mirror.

*Start with [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md). The target lists live in [`_ACQUISITION_PLAN.md`](_ACQUISITION_PLAN.md); progress in [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md).*
