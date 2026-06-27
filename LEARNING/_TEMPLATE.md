---
id: c-REPLACE-ME                # stable handle, never changes (e.g. c-entropy)
sortkey: 0000                   # ladder position; pick a number BETWEEN neighbors
title: REPLACE — short, plain title
domains: [domain-one, domain-two]
level: foundational             # foundational | core | intermediate | advanced
prereqs: []                     # ids of modules to read first (e.g. [c-system])
provides: []                    # concepts this module is the HOME for
resources: []                   # ids from ../RESOURCES/INDEX.md  (+ corpus sources it's grounded in)
status: planned                 # planned | drafted | ready | needs-update
reading_time: ~ min
rev: 1                          # bump on every meaningful change
created: 2026-06-20
updated: 2026-06-20
---

<!-- ════════════════════════════════════════════════════════════════════════
 THE STANDARD (binding): INSTRUCTIONS/HARD_RULES.md. Structure modeled on the
 learner's "hy" file 36, FUSED with this project's truth-seeking + director
 sections. Priority when rules collide: miss-nothing-enduring → understand
 deeply → grounded & non-repeating → simple & glossed → concise (LAST).
 Two language axes, never in conflict: (1) 8-year-old SENTENCE SHAPES;
 (2) keep ALL real vocabulary, but GLOSS each term inline:
     term (general meaning; here: in-context meaning; register-if-idiom)
 EXHAUSTIVE on the conceptual axis; delegate only coding/execution grind.
 DURABILITY: teach the reason/objective (timeless); transient specifics
 (a particular dated algorithm) appear only as a brief illustration.
═════════════════════════════════════════════════════════════════════════ -->

# TITLE
*The **deck** — 1–3 sentences: what you'll understand after this rung, what it unlocks, and the stakes (why it matters). Gloss hard words even here. Replaces the old "Why this rung matters"; the body must **develop** the deck, never restate it.*

> **You are here:** rung [NNNN], [chapter name].
>
> **Grounded in:** [the corpus sources distilled here — book/paper/course titles + `r-ids`; this is what the claims are checked against].
>
> **Builds on:** [[prereq-rung]] — one line on the thread it continues / the question it now answers.

---

## The idea (start concrete)
<!-- Generic heading (multi-source). Use ### sub-heads that build a STAIRCASE — each climbs onto the one before. -->
*Open with a real example/analogy, then the general idea. **Heavy inline glossing** of every medium-to-advanced / technical term. Where a source **defines or states** something load-bearing, quote it **verbatim** with a `*(Source, year)*` line, then "read it plainly first" → the deeper principle → **what it rules out** → why it matters. **Self-containedness (HARD_RULES §4.2a):** when you USE a prerequisite concept, give a **one-line plain refresher of it right there, then link** — never a bare `[[link]]` that assumes recall (e.g. "the **dot product** — multiply two vectors position-by-position and add, a similarity score (see [[c-linear-algebra]])"). DRY still holds: the full home is elsewhere; this is a reminder, not a re-teach. The module must read on its own. Mark any transient specific as illustration of the enduring idea (durability filter).*

::: example
*A vivid case. Then: **why this example** — what it makes you see that a plain statement can't.*
:::

## Going deeper *(exhaustive on the concept; delegate the code)*
*Render the mechanism/argument/trade-offs/distinctions **in full** — miss nothing enduring. **Anticipate the reader's objection** ("but wait — what about…?") and resolve it. **Name the exact misconception** people have (often a `::: warn` box). Render math/mechanism for complete insight; leave actual coding/derivation to "you'd direct the AI to do X." If the topic is large, split into sub-rungs (numbering gaps) rather than bloating one file.*

## ⚠️ Honesty box *(where hype or contestation is common)*
*The real limits, failure modes, and live debates — at full force, both sides stated. Tag claims: **[Established] / [Likely] / [Contested] / [Speculative] / [Unknown]**. Flag fast-aging claims as dated snapshots.*

## How a director uses this
- *The decision-relevant takeaways — what to ask for, when, how to judge it.*
- **What you delegate:** *the execution/coding.*  **What you own:** *the data, objective, evaluation, judgment.*

## Connections
- **If you keep only three things:** *3 ultra-short hooks.*
- **Stands on:** [[prereq]] *(what it climbs from)*.
- **Where to go next:** **label** — one-line reason → [[next-rung]] *(the next step)*; **label** — reason → [[related]].
- **Contested?** *confidence tags on the load-bearing claims.*

## Proof-of-learning *(do one, from memory)*
*A question to answer · a tiny thing to build/direct · a checkable prediction.*

## Revision notes
*Newest first. One plain line per meaningful change, so the reader re-reads only what moved.*
- `rev 1 (2026-06-20)` — created.

---
*New concepts → add to [CONCEPT_REGISTRY](CONCEPT_REGISTRY.md). Announce in [WHATS_NEW](WHATS_NEW.md). Before ticking "ready", run the **final gate** ([`../INSTRUCTIONS/HARD_RULES.md`](../INSTRUCTIONS/HARD_RULES.md) §7): grounded · complete · non-repeating · glossed · simple · deep · honest. On later edits mark changed parts `*(updated revN)*`, bump `rev`, add a Revision note, update WHATS_NEW, commit.*
