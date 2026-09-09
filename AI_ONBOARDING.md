# AI ONBOARDING — read this first
**For any AI tool (or person) picking up Project ASI later.** This page tells you what the project is, how it's organized, and how to read its full history end-to-end so you can continue the work without losing context.

---

## 1. What this project is (30 seconds)

A long-term, **self-improving** system for understanding **intelligence** — human, machine, and beyond — and what would *really* be required for **AGI** and **ASI**. The product is not a document; it is a *living system that builds and improves its own roadmap*. It may run for years.

The guiding rule everywhere: **simplify the language, never the ideas. Truth over comfort.**

---

## 2. The fastest path to full context (read in this order)

1. [`README.md`](README.md) — the map of the repo.
2. [`INSTRUCTIONS/MASTER_INSTRUCTION.md`](INSTRUCTIONS/MASTER_INSTRUCTION.md) — the constitution. Everything serves this.
3. [`INSTRUCTIONS/VERSION_HISTORY.md`](INSTRUCTIONS/VERSION_HISTORY.md) — the **human-readable evolution log**: what changed each version, *why*, and the trade-offs. This is the single best file for understanding "how did we get here."
4. [`REVIEWS/`](REVIEWS/) — the audits/self-critiques that *drove* each version change. Read these to understand the reasoning behind decisions, including mistakes that were caught.
5. The rest of [`INSTRUCTIONS/`](INSTRUCTIONS/) — the machinery (research method, learning method, domain discovery, milestones, quality control, etc.).

> **Two reading layers, on purpose:** `VERSION_HISTORY.md` + `REVIEWS/` give the *narrative* (prose, why). The **git log** gives the *exact diffs* (what, line-by-line). Use the narrative to understand intent; use git to see precise changes.

---

## 3. How to read the git history

Everything is tracked in git, end-to-end. Useful commands:

```bash
git log --oneline --stat        # every change, with files touched
git log --follow -p <file>      # full line-by-line history of one file
git log --oneline --reverse     # the project's story from the very beginning
```

**Commit message convention** (so history stays readable):
- `docs: …` — content/instruction changes (the usual case here)
- `feat: …` — a new system/document/capability
- `fix: …` — corrections (including correcting our own earlier mistakes)
- `chore: …` — scaffolding, config, housekeeping
- `audit: …` — a self-critique pass
- `vX.Y: …` — a version milestone (mirrors `VERSION_HISTORY.md`)

When you make a change, **commit it** with a message that says *what* and *why*, and — if it's significant — add a matching entry to `VERSION_HISTORY.md`. Keep the two in sync. That is how the next reader (maybe another AI) will understand you.

---

## 4. The non-negotiable working rules (inherited from the constitution)

1. **Truth over comfort** — real answers beat popular/flattering ones.
2. **Simple words, deep ideas** — easy language, expert thinking; define hard words on first use.
3. **Nothing is final** — every doc can be versioned and improved; preserve history, never silently overwrite.
4. **Show the reasoning** — claims travel with evidence, a confidence tag, and the strongest opposing view.
5. **Always ask "what are we missing?"** — assume every list is incomplete.
6. **Bias to action; show your work** — no long stretch of effort without a *showable artifact* (see `INSTRUCTIONS/MILESTONE_AND_SHOWCASE_SYSTEM.md`). Don't drift into admiring the machinery.

---

## 5. A known, important limitation (don't pretend otherwise)

This project mostly runs through a single AI assistant, which means the same mind often **writes and reviews** the same work — so it can rubber-stamp its own blind spots, hallucinate facts, or go stale past its knowledge cutoff. The system has internal checks for this (`INSTRUCTIONS/QUALITY_CONTROL_SYSTEM.md`), but they are **not a full fix**. If you are an AI continuing this work: **verify load-bearing facts against current external sources, and prefer predictions that can be tested against reality over internal consistency.** External, falsifying feedback is the project's top upgrade goal (v1.2).

---

## 6. Current state (updated 2026-09-09)

- **System version: 3.0 — the *investigation-first* re-root (2026-07-14).** The project used to be a broad *curriculum* about intelligence (v1.0–v2.6). It is now an **investigation into the approaches to AGI**. The old curriculum still exists, unmaintained, in `LEARNING/_legacy/`; do not treat it as the plan.
- **The spine is [`LEARNING/APPROACHES_TO_AGI.md`](LEARNING/APPROACHES_TO_AGI.md)** — eleven bets (AP1–AP11) on how general intelligence actually gets built. Each has a card on the map, a full page in `20-the-approaches/`, and one or two deep dives in `50-deep-dives/`. Plus two cross-cutting pages (`30-across-the-approaches/`) and a verdict (`40-the-verdict/`). **36 pages, ~310,000 words, all written.**
- **The forward page is [`LEARNING/THE_PLAN.md`](LEARNING/THE_PLAN.md)** (2026-07-21). It argues that the map is finished, that more reading has low marginal value, and that the binding constraint is **contact with reality** — so the next work is: Phase 0 repair the audit's findings → **Phase 1 build the open-questions ledger** (harvest every "Stuck #N" across all 35 pages into one ranked file) → Phase 2 reproduce a small published result → Phase 3 enter ARC-AGI-3. **Phase 1 has not been started.**
- **The binding rules are [`INSTRUCTIONS/HARD_RULES.md`](INSTRUCTIONS/HARD_RULES.md)**, not the older process documents. Two matter most: **§2.6 — do a live web SOTA check before writing anything** (the corpus goes stale, and an audit proved it did), and **zero repetition** — explain a concept in full at first occurrence, reference it thereafter. Check `LEARNING/CONCEPT_REGISTRY.md` before explaining anything.
- **The reader:** `py -3 build_site.py` compiles `LEARNING/**/*.md` into one self-contained offline `index.html`. Rebuild it after any content change. Verify reader changes in headless Chrome, not by eye.
- **Known outstanding work** (from [`REVIEWS/AUDIT_2026-07-21_v3.0.md`](REVIEWS/AUDIT_2026-07-21_v3.0.md), all still `QUEUED`): the eleven map cards are unscannable single-paragraph walls; two rival naming schemes (`P1–P7` in INSTRUCTIONS/RESOURCES vs `AP1–AP11` in LEARNING) both live; `WHATS_NEW.md` and `VERSION_HISTORY.md` have outgrown their purpose; the dead corpus-campaign planning files should be archived.
