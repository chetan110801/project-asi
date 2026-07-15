---
id: c-next-word
sortkey: 1001
title: How today's AI works — guessing the next word
domains: [machine-intelligence]
level: core
prereqs: []
provides: [language-model, next-word-guessing, self-supervision, prediction-is-compression, autoregressive-generation]
resources: [r-slp3]
status: ready
reading_time: 16 min
rev: 1
created: 2026-07-14
updated: 2026-07-14
---

# How today's AI works — guessing the next word
*This is the first step of our ladder, and it starts from zero. Almost every AI tool you have used — chatbots, writing helpers, coding helpers — is built on **one simple job**: guess the next word. That is it. This page explains that job in plain words: what the machine really does, how it learns with no human helpers, why "just guessing words" quietly forces it to learn real facts and skills, and what it still cannot do. Once you hold this one idea, the rest of the ladder — how these machines are made bigger, and the big bets on how to reach real thinking — will make easy sense.*

> **You are here:** the **first content rung** of the new "approaches to AGI" ladder. Read it before the others. You need **no prior knowledge** — everything is built up here from the ground.
>
> **Where the facts come from:** *Speech and Language Processing* (3rd edition) by Dan Jurafsky and James Martin — a widely used, free textbook (draft of January 2026). Quotes below are its exact words.

---

## The one job: guess the next word

Start with a game. Finish this line in your head:

> *The sky at noon is a clear ___*

You probably thought *blue*. Maybe *sky-blue*. You almost certainly did **not** think *banana*. Without trying, you just did the whole job of an AI language model.

Notice what you really did. You did not pick **one** word. You quietly **ranked** many words by how well they fit. *Blue* felt very likely. *Grey* felt possible. *Banana* felt silly. That ranking — every word, with a strength — is the whole thing.

Here is the textbook's plain definition:

> "A language model is a machine learning model that predicts upcoming words."
> *(Jurafsky & Martin, SLP3, Ch. 3)*

Let us unpack the two new words, simply:

- A **language model** (people shorten it to **LM**) is a machine whose only job is to look at some text and say **what word is likely to come next**. That is its entire purpose.
- A **machine learning model** is a machine that is **not** given fixed rules by a person. Instead, it **learns a skill from examples** — it looks at lots of data and slowly adjusts itself to get better. (We will see exactly how below.)

One key point: the machine's answer is never a single word. It is a **score for every word at once** — for example *blue* 40 out of 100, *grey* 12 out of 100, *banana* almost 0. This list of "every possible next word, each with its chance" is called a **probability** (chance, from 0 to none, up to 1 for sure). Keep this in mind: **the machine deals in odds, not in one certain answer.** A lot of what AI does — and where it goes wrong — comes straight from this fact.

---

## How it learns: hide, guess, correct — with no human helpers

Now, how does a machine get good at this game? The method is beautifully simple, and it hides the real magic.

You take real text — a book, a web page, anything. You **cover** the next word. You let the machine **guess** it. Then you **show** the real word, and you nudge the machine a tiny bit so that next time it would give that real word a higher score. You do this **billions of times**, over huge amounts of text.

Here is why this is such a big deal. In most machine learning, a **person** must first mark the "right answer" on every example — a slow, costly job. But in this game, nobody has to mark anything. The right answer is already sitting there. As the textbook puts it:

> "we know the correct answer (it's the next word in the corpus!)"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

("**Corpus**" just means a large pile of text — the machine's reading material.) The next word **is** the answer key. So the machine can teach itself from **any** text, with no humans in the loop:

> "We call such a model self-supervised because we don't have to add any special gold labels to the data; the natural sequence of words is its own supervision!"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

Two new terms, glossed:

- **Self-supervised** = the data teaches itself; the machine makes its own practice questions and answers out of plain text. ("Supervision" here means the "right answers" a learner is trained against.)
- **Gold labels** = the trusted "right answers" that a human normally has to write in by hand. This game needs none.

Why does this matter so much? Because it removes the one thing that used to limit AI: the cost of human labelling. Suddenly the **whole internet** becomes free practice material — a teacher that never gets tired and never sends a bill. **This is the single reason this kind of AI could grow so large.** [Established]

---

## The surprise: guessing words forces the machine to learn real things

Here is the idea that turns a party trick into something serious. *Guessing the next word sounds shallow — surely it only teaches grammar?* No. Look at what some blanks actually **demand**:

| Fill the blank | What the machine must have learned |
|---|---|
| "The square root of 9 is ___" → *3* | a bit of **math** |
| "The capital of France is ___" → *Paris* | a **fact about the world** |
| "The opposite of *hot* is ___" → *cold* | what words **mean** |
| "She poured the water and it started to ___" → *flow / spill* | how the **world behaves** |

There is no way to guess these well by knowing grammar alone. To score well, the machine is **forced** to pick up math, facts, meanings, and a sense of how things work — all as a side effect of one goal: guess the next word better. One simple job quietly pulls in a huge amount of real knowledge. **[Established]**

*Anticipate the doubt:* "But maybe it just memorised these exact lines?" Good question — and the next section answers it.

---

## Why it can't just be memorising: packing the world in

When a machine reads a truly gigantic amount of text but only has a limited amount of inner storage, something important happens: **it does not have room to store the text.** It is forced to keep the **patterns** instead of the exact words — the rule of grammar once, the idea of addition once, the shape behind a million examples instead of the million examples.

This is the same thing your phone does when it shrinks a photo file: it keeps what matters and throws away the rest. That is called **compression** (making something smaller by keeping the pattern and dropping the exact details). And here is the deep link that makes people excited:

> **To guess the next word really well, you have to find the patterns in the text. Finding the patterns is the same as compressing it. And some people argue that compressing the world well is close to *understanding* it.**

You do not need to fully believe that last step yet — whether "compressing well" equals "understanding" is a real open argument we will return to. But the first part is solid: because there is no room to memorise, the machine is **forced** to learn general patterns, not exact copies. That is why it can handle sentences it has never seen. **[Established that it must compress; Contested whether that equals understanding]**

---

## How it writes whole answers: guess, add, repeat

So far the machine only **scores** the next word. How does that become a full paragraph? By the simplest loop you can imagine:

1. Guess the next word and pick one.
2. Add it to the end of the text.
3. Now guess the **next** next word — using everything so far, including the word it just wrote.
4. Repeat.

That is all. The stream of text you see a chatbot type is exactly this loop running fast. This "guess one word, add it, guess again" style has a name: **autoregressive** (a long word that just means "each new piece is guessed from the pieces before it"). Two things to remember, because they explain a lot of AI behaviour:

- **It writes one word at a time.** There is no hidden step where it plans the whole answer first. Each step is just one more guess.
- **Its own words become part of its input.** If it takes a wrong turn early, that wrong word steers everything after it. Small early mistakes can grow. (This will matter a lot later, when we look at AI that acts over many steps.)

---

## What it is NOT (clear these away now)

Three wrong pictures to drop, because each causes confusion later:

- **It is not a rulebook.** No person wrote grammar rules into it. Any "grammar" it has, it soaked up from examples.
- **It is not a giant lookup table.** It does not store your sentence and find a saved reply. It **works out** a fresh set of odds for text it has never seen. (This is what "compression" above buys.)
- **It is not sure of anything.** Its natural output is odds, never one certain answer. Every bit of its creativity — and every one of its confident mistakes — flows from that.

---

## ⚠️ Honesty box

- **Its goal is "what is likely," not "what is true."** The machine is trained to guess the **most likely** next word in human text. Human text is full of mistakes, opinions, and lies. So a machine that copies it perfectly would also copy its untruths. Sounding right and being right are **not** the same thing. **[Established]**
- **Its teacher is the raw text — so its quality is the text's quality.** Nobody hand-checked the training text. Whatever bias or error is in the text can pass into the machine. There is no built-in filter for truth. **[Established]**
- **"It just predicts words" is true — but it is not the whole story.** Yes, the mechanism is next-word guessing. But we saw that good guessing **forces** real knowledge and pattern-finding. So the mechanism being simple does not make the result shallow. How deep it really goes is a live argument — held open, on purpose. **[Contested]**

---

## How to use this (if you want to direct AI work)

- **When an AI surprises you — good or bad — ask its real question:** *"what words would most likely come next in text like this?"* That one question explains its fluent nonsense (likely ≠ true), its habit of copying your style (your text is part of its input), and its cleverness (it found the pattern).
- **The training text is a decision, not a detail.** Since the text is the teacher, whoever picks and cleans the text decides what the machine knows and believes. If you ever guide AI work, own that choice.
- **Do not trust it like a database.** It keeps the gist and drops exact details, so it can get names, quotes, and numbers wrong while sounding sure. Check facts.

---

## Connections

- **Keep only three things:** ① a language model **guesses the next word**, giving odds to every word, then writes by guessing one word at a time. ② It learns with **no human helpers** — the next word is its own answer key — which is why the whole internet could teach it. ③ Guessing well **forces** it to pack in real patterns and knowledge; it is not memorising, and it is not sure of anything.
- **Next on the ladder:** what happens when you make this machine **bigger** — the steady pattern that powers today's AI → [scaling laws & emergence](02_scaling-laws-and-emergence.md). Then the first big bet on reaching real thinking → [AP1 · the "make it bigger" bet](../20-the-approaches/01_ap1-scale-and-foundation-models.md).
- **How sure are we?** The definition, self-supervision, and "guessing forces knowledge" — **[Established]**. "Guessing well = real understanding" — **[Contested, open]** (we return to it).

## Check yourself *(try one, from memory)*

1. A friend says "an AI just predicts the next word, so it can't really know anything." Use the fill-in-the-blank examples to show what is wrong with that — and then say honestly which part of the doubt still stands.
2. Explain why training this machine needed **no** human markers, and what that means for who the machine's real "teacher" is.
3. Why can't a machine that reads far more text than it can store be just memorising? What must it do instead?

## Revision notes

*Newest first.*
- `rev 1 (2026-07-14)` — created as the **bottom rung of the new simple ladder** (HARD_RULES §6.5): the shared "guess the next word" basics that the scaling page and every approach page build on. Plain English, zero prior knowledge; grounded in SLP3 (quotes exact). Replaces the on-ramp that earlier sat inside the AP1 page, so that idea now lives once, here.

---
*The base of the ladder. Next step up → [scaling laws & emergence](02_scaling-laws-and-emergence.md).*
