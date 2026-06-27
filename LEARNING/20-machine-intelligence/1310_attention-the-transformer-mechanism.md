---
id: c-attention
sortkey: 1310
title: Attention — how a model decides what matters
domains: [machine-learning, deep-learning, nlp, machine-intelligence]
level: core
prereqs: [c-neural-networks, c-linear-algebra, c-language-models]
provides: [attention, query-key-value, self-attention, multi-head-attention, positional-encoding, quadratic-cost]
resources: [r-slp3, r-cs336, r-prince-udl, r-d2l]
status: drafted
reading_time: ~16 min
rev: 1
created: 2026-06-27
updated: 2026-06-27
---

<!-- ════════════════════════════════════════════════════════════════════════
 ⭐ STANDARD-DEMO (v2.4). This single file is a worked example of the new merged
 standard (INSTRUCTIONS/HARD_RULES.md + LEARNING/_TEMPLATE.md, modeled on hy
 file 36) — written to let the learner APPROVE THE FEEL. Two honesty flags:
 (1) GROUNDING PENDING — sources are named, but verbatim grounding against the
 RESOURCES/corpus/ is not yet done (corpus not built). (2) NOT YET WIRED — this
 is intentionally the ONLY file changed; CONCEPT_REGISTRY / 00_MAP / WHATS_NEW
 are NOT updated until the standard is approved and the module is grounded.
═════════════════════════════════════════════════════════════════════════ -->

# Attention — how a model decides what matters
*Every modern AI that reads or writes — every **LLM** (large language model; here: the next-word-predictors of [[c-language-models]]) — runs on one trick: for each word it is processing, it **looks back at all the other words and pulls in the few that matter**, ignoring the rest. That trick is **attention**. It is the reason a model can tell which earlier word a "**it**" refers to, hold a thread across a long page, and be trained on the whole internet at once. After this rung you'll know exactly what attention computes, why it beat the older designs, what it costs, and the misconceptions that fool even practitioners — enough to judge any "our model attends to…" claim without taking it on faith (believing it with no proof; informal).*

> **You are here:** rung 1310, machine intelligence — the heart of the transformer cluster.
>
> **Grounded in:** Vaswani et al., *Attention Is All You Need* (2017, the transformer); Jurafsky & Martin, *Speech and Language Processing* 3e (`r-slp3`, ch. on transformers); Stanford CS336 (`r-cs336`); Prince, *Understanding Deep Learning* (`r-prince-udl`). *(Grounding-pending: verbatim checks against the corpus.)*
>
> **Builds on:** [[c-neural-networks]] (a transformer is a deep net) and [[c-linear-algebra]] (the **dot product** = a similarity score). This rung opens up the one box [[c-language-models]] deliberately left closed: *how* a model "looks back."

---

## The idea (start concrete)

### The problem: which earlier word does *this* word depend on?
Take the sentence: *"The trophy didn't fit in the suitcase because **it** was too big."* What does *"it"* mean — the trophy or the suitcase? You know instantly: the **trophy** (because *big* is why it didn't fit). Change one word — *"…because it was too **small**"* — and now *"it"* flips to the **suitcase**. To understand *"it"*, a model must **look back** at the right earlier words and weigh them.

That is the entire job of attention:

> For each word it is processing, attention **builds a score for every other word** — *"how much should I let you influence me right now?"* — and then takes a **weighted blend** (a mix where each thing is counted in proportion to its score; here: an average that leans toward the high-scoring words) of those words. High score → strong influence. Near-zero score → ignored.

So *"it"* ends up mostly a blend of *"trophy"* — the model has, in effect, **routed** (sent along a chosen path; here: pulled information from the right place) the meaning of *trophy* into the slot for *it*. **[Established]**

::: example
**A meeting where everyone can hear everyone.** *The picture:* picture every word in the sentence sitting at one big round table. When it's *"it"*'s turn to update what it means, *"it"* doesn't ask its neighbours only — it can listen to **every** word at the table at once, and choose whom to trust. *Why this picture:* it captures the two things that make attention special — **every position can reach every other position directly** (no message has to pass hand-to-hand down the line), and **the listener picks whom to weight.** Hold this image; the older designs below could *not* do this.
:::

### The mechanism: query, key, value (the part worth slowing down for)
How does a word compute those scores? Through three roles every word plays at once — **query, key, value** (often "**Q, K, V**"). The cleanest analogy is **search** (looking something up; here: like a tiny search engine inside the sentence):

- **Query (Q)** — *what I'm looking for.* (The word *"it"* asks: *"which earlier noun am I standing in for?"*)
- **Key (K)** — *what I'm advertising about myself.* (The word *"trophy"* advertises: *"I'm a concrete object that could be referred to."*)
- **Value (V)** — *what I'll actually hand over* if you pick me. (The meaning of *trophy* that gets blended in.)

Each is just the word's **vector** ([[c-linear-algebra]]: a list of numbers that stands for the word's meaning) pushed through a small learned **transformation** (a fixed operation that re-mixes the numbers; here: a learned lens that turns the word into its "query" view, its "key" view, or its "value" view).

Now the score. To find how well a query matches a key, attention uses the **dot product** ([[c-linear-algebra]]) — *"multiply the two vectors position-by-position and add it all up."* A big dot product means the two vectors **point the same way** (are aligned in meaning; here: the query and key are about the same thing), so the score is high. This is the engine room: **attention is similarity-by-dot-product, turned into a blend.** The famous one-line summary of the whole operation:

> "Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V"
> *(Vaswani et al., 2017 — grounding-pending)*

Don't let the symbols scare you — read it in plain words, left to right:
- **QKᵀ** — every query dotted with every key → a full grid of raw match-scores.
- **÷ √dₖ** — shrink the scores a touch so they don't blow up (get so large the next step jams; informal) when the vectors are long. (A housekeeping step; here: keeps the numbers in a sane range.)
- **softmax** (a function that turns a row of numbers into positive fractions that add up to 1; here: turns raw scores into percentages of attention) — so each word spends exactly **100% of its attention**, split across the others.
- **× V** — use those percentages to blend the **values**. Out comes the new, context-aware meaning of the word.

*What this rules out:* attention is **not** a fixed rule about grammar. Nobody told it *"a pronoun attends to the nearest noun."* The Q/K/V lenses are **learned** (set by training, [[c-machine-learning]]) — the model *discovers* whom to attend to from data. That's why the same machine works for code, music, and protein sequences, not just English.

### Self-attention vs cross-attention (one small but useful split)
- **Self-attention** — the words of *one* sequence attend to *each other* (the trophy example). This is what stacks up inside an LLM, layer after layer, each layer letting words re-blend with richer context.
- **Cross-attention** — words of one sequence attend to a *different* sequence (e.g. an answer attending to a question, or a translation attending to the original). Same machine, two sources. **[Established]**

### Multi-head attention: several kinds of "mattering" at once
One set of Q/K/V lenses can only track **one** kind of relationship at a time. But *"it"*-refers-to-*"trophy"* (who-is-what), *"big"*-modifies-the-reason (why), and subject-verb agreement are **different** relationships. So a transformer runs **several attention operations in parallel** — called **heads** (separate copies, each with its own learned lenses; here: separate "viewpoints" that attend for different reasons) — and stitches their outputs together. One head may learn to track grammar, another long-range topic, another nearby word-pairs. **Multi-head** = look at the sentence through several relationship-lenses at once. **[Established]** *(How cleanly each head maps to one human-nameable job is **[Contested]** — see the honesty box.)*

## Going deeper *(exhaustive on the concept; the code is delegated)*

### Why this beat the older design (the strategic payoff)
Before 2017, sequences were handled by **RNNs** (recurrent neural networks; here: nets that read one word at a time, passing a memory forward — [[c-neural-networks]]). Two fatal limits, both of which attention erased:
1. **Distance.** In an RNN, to connect word 1 to word 100, information must survive **99 hand-offs** — and it usually fades (the model "forgets" the start). Attention connects any two words in **one step**, no matter how far apart. *(This is the long-range link of [[c-neural-networks]], now made concrete.)*
2. **Speed.** An RNN must process words **in order** (word 2 needs word 1's result first), so it can't use a GPU's full parallel power. Attention scores **all pairs at once** — a giant matrix multiply ([[c-linear-algebra]]), exactly what GPUs devour ([[c-machine-learning]]: "AI is matrix multiplication"). *This parallelism is the real reason transformers could be trained on internet-scale data* — and therefore the quiet reason the whole LLM era happened. **[Established]**

> *Anticipate the objection:* "If attention is so much better, why did it take until 2017?" Because the *idea* of attention existed earlier (as a helper bolted onto RNNs). The 2017 leap was to **throw the RNN away entirely** — *"attention is all you need"* — and that only paid off once GPUs and data were big enough to feed the hungrier, more parallel design (the **Bitter Lesson** again, [[c-learning]]).

### The bill: attention is quadratic
Here's the catch every director must know. To score **every word against every other word**, attention does roughly **n × n** comparisons for a sequence of **n** words. Double the length → **four times** the work and memory. This is **quadratic cost** (cost that grows with the *square* of the size; here: O(n²) — [[c-computation]]'s complexity, made painful). **[Established]**

That single fact explains a huge amount of the field:
- why **context windows** ([[c-language-models]]) were small for years and cost money to grow;
- why a whole research industry exists to make attention **cheaper** (FlashAttention, sparse/linear attention, and post-transformer designs like Mamba) — the efficiency frontier;
- why "long context" is a selling point, not a freebie.

> *The durable lesson, not the transient fix:* don't memorize which 2024 trick shaved the cost — those change yearly. **Own the *why*: the n² wall is the structural tax you pay for letting everything see everything.** Any future architecture is, at heart, a different bet about how to dodge that tax without losing too much of the all-to-all reach.

### One thing attention can't do by itself: order
Attention treats its inputs as a **bag** (an unordered pile; here: a set with no first/second/third) — it scores word-pairs, but the math doesn't know *"trophy"* came before *"it"*. Yet word order obviously matters (*"dog bites man"* ≠ *"man bites dog"*). So transformers **add position information** into each word before attention runs — **positional encoding** (a signal stitched into each word's vector that says where it sits in the line; here: giving every word a sense of its place). Worth knowing because it's a real, separate ingredient, not part of attention itself. **[Established]**

## ⚠️ Honesty box — what "attention" does and doesn't mean
The word *attention* is borrowed from human psychology, and that borrowing **misleads** (leads you to a wrong belief; here: makes people over-read it). Calibrate:
- **Attention weights are not explanations.** A high weight from *"it"* to *"trophy"* is *correlated* with the model's decision, but reading the weights as *"this is why the model answered"* is **[Contested]** — papers show you can change the weights and get the same output, or get the same weights with different outputs. Treat attention maps as a **hint**, not a confession.
- **It is not human attention.** No spotlight of awareness, no focus in the felt sense. It's a weighted average chosen by dot-product similarity. The name is a metaphor (a word borrowed from one thing to describe another; here: a loose analogy, not a claim of consciousness). **[Established]**
- **Heads are messier than the tidy story.** "One head does grammar, one does coreference" is a useful *first* picture, but in real models heads overlap, share work, and many look uninterpretable; some can be pruned (cut away; here: removed) with little loss. The clean division is **[Likely-oversimplified]**.
- **Attention may not be essential.** Strong non-attention sequence models exist (e.g. **Mamba** / state-space models). Whether attention is *necessary* for top performance, or just *currently winning*, is **[Contested / open]** — a live bet on the post-transformer frontier ([[c-language-models]]).

## How a director uses this
- **Use it to read the cost structure of any LLM product.** "Longer context" and "bigger documents" run straight into the **n² wall** — they cost compute and latency. When a vendor promises huge context cheaply, ask *how* (sparse/linear attention? caching?) and what they traded away (usually some recall quality).
- **Don't trust attention maps as interpretability.** If a team shows you a pretty heat-map as "proof" the model reasons correctly, push back — weights are a hint, not an explanation. Demand behavioural evals ([[c-machine-learning]]: held-out tests), not visualizations.
- **Recognize the durable idea vs the churn.** The enduring concept (all-to-all, similarity-weighted routing, and its n² tax) is stable; the specific efficiency trick of the month is not. Invest your understanding in the former.
- **What you delegate:** implementing attention, the GPU kernels, picking the efficiency variant. **What you own:** the architectural bet (how much all-to-all reach you need vs the cost you'll pay), the context-length/latency/price trade-off, and refusing false interpretability claims.

## Connections
- **If you keep only three things:**
  - Attention = for each word, take a **similarity-weighted blend** of all other words (Q·K scores → softmax → blend the V's).
  - It beat RNNs by giving **one-step long-range reach** + **full parallelism** — which is *why* internet-scale training (and the LLM era) became possible.
  - It costs **n²** — the structural tax for all-to-all reach, and the reason "long context" is hard and most efficiency research exists.
- **Stands on:** [[c-linear-algebra]] (dot product = similarity), [[c-neural-networks]] (a transformer is a deep net; the long-range/parallel advantage), [[c-machine-learning]] (the Q/K/V lenses are *learned*).
- **Where to go next:** **How LLMs work** — attention is the engine; this is the whole vehicle (tokens → pretrain → RLHF) → [[c-language-models]] *(the parent rung)*; **Scaling laws** — why making this machine bigger keeps paying → (rung 1700, planned); **Post-transformer architectures** — the attempts to dodge the n² tax → (frontier).
- **Contested?** The mechanism, Q/K/V, multi-head, the RNN comparison, n² cost — **[Established]**. Attention-weights-as-explanations and head-interpretability — **[Contested / oversimplified]**. Attention-is-necessary — **[Contested / open]**.

## Proof-of-learning *(do one, from memory)*
1. In the *"…because it was too big/small"* example, explain — in terms of **query, key, value** — how the model makes *"it"* point to a different word when one adjective changes.
2. State the **two** advantages of attention over an RNN, and say which one is the real reason LLMs could be trained at internet scale.
3. What is the **n²** problem, and why does it mean "long context" is a cost decision, not a free feature? Name one *kind* of fix (without naming this year's specific trick).
4. A teammate shows an attention heat-map as proof the model "understands" a sentence. Give the one-sentence pushback from the honesty box.

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-27)` — created as the **v2.4 standard-demo** (file-36 structure + glossing + depth devices + confidence tags + director section). *Grounding against the corpus and wiring into registry/map are pending standard-approval.*

---
*⭐ This is a STANDARD-DEMO for approval — deliberately the only file changed. Once the standard is approved and the corpus exists, this gets (a) verbatim-grounded, (b) logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md) (moving "transformer/attention" home here from 1300), (c) announced in [WHATS_NEW](../WHATS_NEW.md), and (d) placed on [00_MAP](../00_MAP.md).*
