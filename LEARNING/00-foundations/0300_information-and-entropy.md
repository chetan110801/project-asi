---
id: c-entropy
sortkey: 0300
title: Information & entropy (the gentle version)
domains: [information-theory, foundations, math]
level: foundational
prereqs: [c-system]
provides: [information, bit, entropy, surprise, compression]
resources: [r-mackay-itila, r-shannon]
status: ready
reading_time: 8 min
rev: 1
created: 2026-06-22
updated: 2026-06-22
---

# Information & entropy
*After this rung you'll have a precise, simple grip on what "information" actually **is**, what a **bit** measures, and why **entropy** (uncertainty) is the hidden quantity behind compression, learning, and — the deep claim — intelligence itself.*

## Why this rung matters
Everything an AI does is move and reshape **information**. The training signal that makes a language model learn is measured in this exact currency ("cross-entropy"). And there's a serious thesis that **understanding ≈ compression ≈ intelligence**. You can't judge any of that without the idea on this page. We do the *gentle* version here; the math returns later and links back (no repetition).

## The idea (start concrete)
Play "20 questions." I'm thinking of a number from 1 to 16. You ask: *"Is it 8 or higher?"* — yes. *"12 or higher?"* — no. *"10 or higher?"* — yes. *"Is it 11?"* — yes. Four yes/no answers and you nailed it.

Each good question **cut the possibilities in half**. That halving is the atom of information:

> A **bit** = one yes/no answer that **halves your uncertainty**. (16 options → 4 bits. 1,000 options → about 10 bits.)

So **information = how much your uncertainty drops** when you learn something. Before, 16 possibilities; after, one. The message carried the gap between them.

## Surprise: rare news carries more
Here's the twist that makes the idea powerful. Information is tied to **surprise**:

- "The sun rose this morning." You already knew it. ≈ **0 bits**. No surprise, no information.
- "It snowed in the Sahara today." Shocking, rare → **many bits**. Big surprise, lots of information.

> **Rare events carry more information than common ones.** The more surprising the message, the more it tells you.

This is why a predictable message can be sent in almost no space, and a surprising one can't be shortened.

## Entropy = average surprise = how unpredictable a source is
Now zoom from one message to a whole *source* (a coin, a language, a data stream):

> **Entropy** = the **average surprise** of a source = the average number of bits you need to describe each outcome = **how unpredictable it is.**

- A **fair coin**: every flip is a real 50/50 surprise → maximum entropy, **1 bit per flip**. You can't do better than one bit each.
- A **two-headed coin**: every flip is "heads," no surprise → entropy ≈ **0**. You don't even need to send it.
- **English text**: quite predictable (after "th" you can guess "e"), so its entropy per letter is *low* — which is exactly why text files shrink when you zip them.

**High entropy = unpredictable, random, incompressible. Low entropy = predictable, structured, compressible.**

## The bridge: compression ↔ prediction ↔ understanding
Two ideas that look separate are secretly the same:

- **Compression.** You can only shrink data by exploiting its *predictable* parts (zip replaces repeated patterns with short codes). The entropy is the hard floor — Shannon proved you **cannot** compress below it without losing information. **[Established]** (Shannon, 1948 — see resources / [`PAPERS.md`](../../RESOURCES/PAPERS.md).)
- **Prediction.** To predict well *is* to know where the surprise isn't. A model that predicts the next word well has found the structure in language — and could therefore compress it well.

Put them together and you get a striking claim that runs through modern AI:

> **To predict = to find structure = to remove entropy = to compress = (arguably) to understand.**

A large language model is trained to do exactly one thing: **predict the next piece of text**, i.e. lower its surprise about the data. Its training score, **cross-entropy loss**, literally measures *how surprised it still is* — lower is better (you'll meet it again at [1300](../20-machine-intelligence/)). Some researchers go further: **compression is intelligence** (you understand something to the exact degree you can compress it). A real cash prize, the Hutter Prize, is built on that bet. **[Likely → Contested]** — a powerful and influential framing, not a settled law.

## How a director uses this
- **Value data by its information, not its size.** A terabyte of near-duplicates carries few bits; a small, surprising, diverse dataset can carry many. *Bits, not bytes,* is what a learner actually feeds on.
- **Read "loss" correctly.** When you direct a training run, the number going down (cross-entropy / perplexity) is *average surprise falling* — the model is finding structure. Knowing what it means keeps you from chasing the wrong metric.
- **Use the compression lens to judge "understanding."** If a system can reproduce a domain from a tiny description, it has *modeled* it; if it needs to memorize everything, it hasn't. That instinct will serve you constantly (memorizing vs. generalizing returns at [0600](0600_what-it-means-to-learn.md)).
- **What you delegate:** the formulas (logs, exact bit counts) — the AI computes them. **What you own:** the instinct for where information *is*, and what "lowering entropy" buys you.

## Connections
- **Stands on:** [0200 What is a system?](0200_what-is-a-system.md). Uses an informal idea of *chance/surprise*; the rigorous probability behind it comes at [0500](0500_probability-and-uncertainty.md), and a deeper, math version of entropy can later live in [`30-math-and-theory/`](../30-math-and-theory/) and link back here.
- **Leads to:** learning ([0600](0600_what-it-means-to-learn.md)), language models & cross-entropy loss ([1300](../20-machine-intelligence/)), data as fuel ([1600](../50-world-and-society/)).
- **Contested?** Bits/entropy/compression limits — **[Established]**. "Compression = understanding = intelligence" — **[Likely → Contested]**.

## Proof-of-learning *(do one, from memory)*
1. Why does "the sun rose today" carry almost zero bits, while "it snowed in the Sahara" carries many?
2. A friend's text messages are 99% the word "lol." High or low entropy? Will they compress well?
3. In one sentence, connect **predicting the next word** to **lowering entropy** — and say why that's what training an LLM does.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-22)` — created.

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md).*
