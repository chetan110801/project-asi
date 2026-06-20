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

## 6. Current state

- **System version:** 1.2 (see `INSTRUCTIONS/VERSION_HISTORY.md`).
- **The project has four parts:** **LEARN** (`LEARNING/` — a no-repeat dependency ladder of modules; start at `LEARNING/00_MAP.md`), **BUILD** (`BUILDS/` + `INSTRUCTIONS/BUILD_SYSTEM.md`), **GATHER** (`RESOURCES/`), **SYSTEM** (`INSTRUCTIONS/` + `REVIEWS/`).
- **North Star (confirmed):** all together — pure understanding + building toward AGI/ASI + eventual career/startup/research + an independent viewpoint.
- **Key mechanisms to respect:** DRY (one canonical explanation per concept — check `LEARNING/CONCEPT_REGISTRY.md` before explaining anything); dynamic insertion via numbering gaps; per-module `rev` + `## Revision notes` + `LEARNING/WHATS_NEW.md` so the learner re-reads nothing; judge the learner's ideas for feasibility (`INSTRUCTIONS/IDEA_EVALUATION_SYSTEM.md`).
- **Next candidates (v1.3):** produce foundational learning modules (0200–0600) and/or the first BUILD; and the standing goal — external, falsifying feedback (predictions resolving, contact with real sources).
