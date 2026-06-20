# LEARNING ARCHITECTURE
**How the actual learning files are structured, ordered, and grown.** This is the connective tissue that turns gathered resources into a single, non-repeating, ever-growing *ladder* of understanding you can climb — and insert into — without ever re-reading.

`Part of: PROJECT ASI — Living Instruction System`
`System Version: 1.3 (added in v1.2; domain folders + chunk pipeline in v1.3) · Status: Living document · Last updated: 2026-06-20`

> This doc defines the **shape** of learning content. It does **not** restate *how to learn* (see [`LEARNING_METHOD.md`](LEARNING_METHOD.md)), *how to turn a resource into a note* (see [`KNOWLEDGE_PROCESSING_SYSTEM.md`](KNOWLEDGE_PROCESSING_SYSTEM.md)), or *how to pick resources* (see [`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md)). It is the substrate those systems write *into*.

---

## 1. The problem this solves

You want to understand many domains but can't read everything. So I distil resources into **learning modules**: concise, simple-language, deep-context notes. But across a multi-year, multi-domain project, three things go wrong without a plan:
1. **Repetition** — the same idea re-explained in five places (wastes your time, drifts out of sync).
2. **Bad order** — advanced notes that assume things you haven't learned yet.
3. **Re-reading** — new material forces you back through old material to find where it fits.

This architecture fixes all three with **three hard rules**.

---

## 2. The three hard rules

### Rule 1 — DRY: one concept, one home (Single Source of Truth)
Every concept is explained **once**, in exactly one *canonical* module. Everywhere else that needs it **links** instead of re-explaining:
> *"Builds on **entropy** — see [0300 Information & Entropy](0300_information-and-entropy.md)."*

If a concept needs a *different angle* for a new domain, you don't re-teach it — you write a short **"in this context…"** note that points back to the canonical home and only adds what's new. (DRY = "Don't Repeat Yourself.")

### Rule 2 — The Ladder: foundational → advanced, always grounded
Modules form a **dependency ladder**. Each module names its **prerequisites** (earlier modules it stands on). You can always trace any advanced idea down to the axioms it rests on. Nothing assumes knowledge that hasn't been built yet.

### Rule 3 — Dynamic insertion: read only what's new
New material is **slotted between** existing modules using numbering gaps (next section), so a new idea that belongs "in the middle" becomes a new file *between* two you've already read — and you read **only that new file**. Existing files don't change (except a one-line pointer you don't need to re-read).

---

## 3. The numbering scheme (how gaps enable insertion)

Every module's filename starts with a **4-digit sort key** in **steps of 100**:

```
0100_what-is-intelligence.md
0200_what-is-a-system.md
0300_information-and-entropy.md
```

**To insert between two modules, pick a number between them:**
- Between `0200` and `0300` → `0250_feedback-loops.md`. You read only `0250`.
- Need another between `0200` and `0250`? → `0225`. Then `0210`, etc.
- Running out of room in a tight spot? widen digits: `0205` → `02055`. (Rare — steps of 100 leave lots of room on purpose.)

**Rules that keep links from breaking:**
- Sort keys are **integers only** (no decimals — they sort wrong as text).
- Every module also has a **stable `id`** in its frontmatter (e.g., `c-entropy`) that **never changes**, even if the file is someday renumbered. Cross-links and the Concept Registry use the `id` to stay findable.
- **Prefer inserting (new number) over reordering (renaming).** Gaps make reordering almost never necessary.

---

## 4. Anatomy of a learning module

**Frontmatter (the machine-readable header):**
```yaml
---
id: c-entropy                 # stable handle, never changes
sortkey: 0300                 # ladder position (gaps allow insertion)
title: Information & Entropy — the basics
domains: [information-theory, math]
level: foundational           # foundational | core | intermediate | advanced
prereqs: [c-probability-basics]   # ids you should read first
provides: [entropy, information, bit, surprise]  # concepts this is the HOME for
resources: [r-shannon-1948]   # ids from RESOURCES/INDEX.md
status: ready                 # planned | drafted | ready | needs-update
reading_time: 8 min
rev: 3                        # bumped every meaningful change (for "read only the change")
created: 2026-06-20
updated: 2026-06-20
---
```

**Body (kept lean, simple language, deep context):**
1. **Why this rung matters** (1–2 lines, and what it unlocks next).
2. **The idea** — built concretely-first, with an analogy; every hard word defined on first use.
3. **Depth as needed** — the deeper levels from [`LEARNING_METHOD.md`](LEARNING_METHOD.md) §2, only as far as leverage justifies.
4. **Connections** — links to prereqs and to where this gets used later (no re-explaining).
5. **One proof-of-learning** — a question, tiny build, or prediction (per [`LEARNING_METHOD.md`](LEARNING_METHOD.md) §6).
6. **Confidence tags** on any contested claim (per [`PRINCIPLES.md`](PRINCIPLES.md) §4).

---

## 5. The Concept Registry — the no-redundancy enforcer

[`../LEARNING/CONCEPT_REGISTRY.md`](../LEARNING/CONCEPT_REGISTRY.md) is a table: **concept → its canonical module (`id`) → one-line pointer**. 

**The rule:** before explaining *anything*, check the registry.
- Already there → **link to it**, don't re-explain.
- Not there → explain it once in the right module, then **add it to the registry**.

This single habit is what guarantees "no repetition anywhere across files."

---

## 6. The Map and the "What's New" feed

- [`../LEARNING/00_MAP.md`](../LEARNING/00_MAP.md) — the **ladder/table of contents**: the recommended reading order, foundational → advanced, grouped by area, with each module's status. Your "you are here."
- [`../LEARNING/WHATS_NEW.md`](../LEARNING/WHATS_NEW.md) — the **delta feed**. Every time a module is added or meaningfully updated, one line is appended: *what*, *where it was inserted*, *why*, and *"read this."* This is how you read **only** what's new since last time. (Git history is the exact backup record.)

---

## 7. Cross-referencing style (the "see there" rule)

When one module needs an idea owned by another, use a short, consistent pointer:
> *"(Recall **feedback loops** — [0250](0250_feedback-loops.md).)"*

Never copy the explanation. A reference is cheap; a duplicate is a future contradiction.

---

## 8. The lifecycle of adding a new concept (the dynamic procedure)

This is the exact answer to *"find a way to do it dynamically."* When new information or a new viewpoint appears:

```
1. NAME it. What concept is this? Check CONCEPT_REGISTRY.
2. DECIDE home.
   • Already has a canonical module? → add only the NEW angle there,
     or, if it's a distinct viewpoint, make a small new module and link.
   • New concept? → it needs its own module.
3. PLACE it on the ladder. Find its prerequisites and what builds on it.
   Pick a sort key BETWEEN the right neighbors (a numbering gap).
4. WRITE it lean (the module anatomy, §4), linking to prereqs — no repetition.
5. REGISTER it. Add to CONCEPT_REGISTRY. Add prereq links both ways.
6. ANNOUNCE it. One line in WHATS_NEW: "Added 0250 between 0200 and 0300 — read this."
7. COMMIT it (git), so the change is tracked end-to-end.
```

You then read **only** the new module. Nothing already read is invalidated.

---

## 9. Updating a module you've already read (read ONLY the change)

Inserting a *new* file is solved above. But what about when I later change *a few points or the structure inside a file you already read*? You should be able to read **only what changed**, not the whole module again. Here's the mechanism:

**Three things make a change readable on its own:**

1. **`rev:` counter + `updated:` date** in frontmatter. Every meaningful edit bumps `rev` (1 → 2 → 3…). At a glance you know a file moved.
2. **A `## Revision notes` section at the bottom of every module** — a tiny, plain-language log, newest first:
   > `rev 2 (2026-07-04) — Replaced the old claim that "scaling alone reaches AGI" with a more careful "scaling has limits X, Y." Why: new evidence (resource r-…). What to re-read: just the "Going deeper" section.`
   You read that one line, then re-read only the pointed-to section. Done.
3. **Inline change markers.** The changed sentence/section carries a small tag — `*(updated rev2)*` — so your eye jumps straight to it.

**And it's announced + versioned:**
- One line in [`../LEARNING/WHATS_NEW.md`](../LEARNING/WHATS_NEW.md): `[updated] 0500 rev2 — what changed in plain words — 👉 read the rev-note + that one section.`
- **Git is the exact, line-by-line backup.** `git log -p --follow <file>` shows every change ever made; `git diff` shows two versions side by side. The Revision notes are the *human-friendly* summary; git is the *precise* record. The two together mean nothing is ever lost and nothing must be re-read in full.

**The update procedure:**
```
1. EDIT the module (keep DRY — don't duplicate; adjust in place).
2. MARK the changed part inline: *(updated revN)*.
3. BUMP rev, set updated: date.
4. LOG it: add a plain-language line to ## Revision notes (what changed, why,
   what to re-read).
5. ANNOUNCE in WHATS_NEW (one line, with the rev).
6. COMMIT to git with a clear message (the exact diff lives here forever).
```

> **Rule of thumb:** if a change is big enough that the *meaning* shifts, it must leave a Revision note. Tiny fixes (typos, a clearer word) just bump nothing and ride along in git silently — they're not worth your re-reading time.

---

## 10. How this connects to the rest of the system

- **Resources** ([`RESOURCE_COLLECTION_SYSTEM.md`](RESOURCE_COLLECTION_SYSTEM.md) + `RESOURCES/`) feed modules (the `resources:` field).
- **Processing** ([`KNOWLEDGE_PROCESSING_SYSTEM.md`](KNOWLEDGE_PROCESSING_SYSTEM.md)) is *how* a module's content is produced; a module **is** an understanding-note given a home and a rung.
- **Milestones** ([`MILESTONE_AND_SHOWCASE_SYSTEM.md`](MILESTONE_AND_SHOWCASE_SYSTEM.md)) track climbing the ladder; reaching a level on a topic = a checkpoint with a showable artifact.
- **Building** ([`BUILD_SYSTEM.md`](BUILD_SYSTEM.md)) consumes modules as prerequisites — you build with what you've climbed to.

The ladder is the **spine**; everything else hangs off it.

---

## 11. Domain folders + the single book (how both are true at once) *(v1.3)*

You asked for two things that pull in opposite directions, and both are right:
- **Domain folders** — brain stuff under brain, AI under AI, quantum under quantum… (easy to browse, easy to cross-reference).
- **One continuous book** — a clear flow from file to file, foundational → advanced, that *reads* like a single authored work.

We get both by separating **where a file lives** from **the order you read it**:

| | **Domain folder** (where it lives) | **Sort-key + `00_MAP`** (the order you read) |
|---|---|---|
| Purpose | browse by topic; house each domain's resources; cross-reference | the single linear "book" reading flow |
| Example | `20-machine-intelligence/` holds all ML/DL/RL modules | the spine may send you through foundations → a little math → brains → ML |

**The folders** (under `LEARNING/`):
```
00-foundations/        intelligence, systems, information, computation, probability, learning
10-minds/              neuroscience, cognition, development, animal minds, language, evolution of mind
20-machine-intelligence/  ML, deep learning, neural nets, RL, agents, LLMs
30-math-and-theory/    linear algebra, probability/stats, information theory, learning theory, optimization
40-compute-and-physical/  CS, algorithms, hardware, chips, energy, thermodynamics of computation, quantum
50-world-and-society/  data economics, supply chains, geopolitics, governance, cultural evolution
60-frontier/           paths to AGI, scaling limits, alignment, ASI
```

**Key rule:** the **sort-key is global** (the book order), so a math module needed early gets a *low* sort-key even though it lives in `30-math-and-theory/`. Folder number ≠ reading order — `00_MAP` is the one true reading sequence, threading across folders. So it reads as one book; it's stored as tidy domains.

**Cross-domain references:** when an AI module needs a brain idea, it links to that idea's canonical home in `10-minds/` (per the DRY rule + `CONCEPT_REGISTRY`, which now records each concept's **domain home**). Explain once, in its home domain; reference everywhere else.

> **Depth vs. home:** a concept's canonical home is where it's *first* introduced on the spine (often the gentle version in `00-foundations/`). A later, more rigorous module (e.g., the *math* of entropy in `30-math-and-theory/`) does **not** re-introduce the concept — it links back and adds only the new depth.

---

## 12. The chunk pipeline (why content is NOT written book-by-book) *(v1.3)*

A learning module is **not** a summary of one resource. It's woven from the best **chunks** of *several* resources plus my own explanation — so it reads like one authored book, not a stack of book reports.

```
RESOURCE(S)                 e.g., MacKay (info theory), 3B1B (visual), a lecture (example)
   │  break into SEMANTIC CHUNKS (one self-contained idea each)
   ▼
CHUNKS  ──tag each──►  domain(s) + concept(s) + level (foundational…advanced)
   │  route each chunk to the canonical MODULE for its concept
   ▼
MODULE  =  best chunks from many sources, re-explained in simple language,
           placed at the right spine position, every source cited by `id`.
```

Consequences:
- A **domain-specific** resource feeds mostly one folder. A **cross-domain** resource gets its chunks **distributed** across several domain modules (its brain chunk → `10-minds/`, its AI chunk → `20-machine-intelligence/`), each linked.
- One module may draw on five resources; one resource may feed ten modules. **Never one-module-per-book.**
- Because each idea has exactly one home (DRY), a chunk that repeats an existing idea isn't re-written — it just *strengthens* the existing module or is dropped.

This is what makes the whole thing feel like **one enormous, continuous, incremental book** — even though it's built from many sources and grows dynamically.
