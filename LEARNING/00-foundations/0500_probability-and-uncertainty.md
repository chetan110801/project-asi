---
id: c-probability
sortkey: 0500
title: Probability & uncertainty (the basics)
domains: [math, probability, statistics, foundations]
level: foundational
prereqs: [c-entropy]
provides: [probability, conditional-probability, bayes-rule, expected-value, distribution, base-rate]
resources: [r-stat110, r-bertsekas-prob, r-mackay-itila]
status: ready
reading_time: 9 min
rev: 1
created: 2026-06-22
updated: 2026-06-22
---

# Probability & uncertainty
*After this rung you'll think in probabilities the way good founders and good AI systems do: holding degrees of belief, updating them on evidence (**Bayes**), and making decisions by **expected value**. This is the second core mathematical language of AI, alongside linear algebra ([0350](../30-math-and-theory/0350_just-enough-linear-algebra.md)).*

## Why this rung matters
The world is uncertain, so **intelligence is the skill of acting well *without* certainty.** Modern AI is probabilistic to the core: a language model picks the next word *by probability*; a classifier says "70% cat"; a self-driving car reasons over what *might* be behind the truck. And as a founder you bet under uncertainty every day. The tools here — especially **Bayes' rule** and **expected value** — are reasoning equipment you'll use constantly, by hand or by directing the AI.

## The idea (start concrete)
**Probability** is a number from **0** (impossible) to **1** (certain) saying how strongly we expect something. 0.5 = a coin flip; 0.9 = "very likely"; 0.01 = "rare."

There are two honest ways to read that number, and you'll use both:
- **Frequency:** "in the long run, it happens this fraction of the time" (a fair die shows 6 about 1/6 of rolls).
- **Belief (Bayesian):** "this is how confident I am," even for one-off events with no "long run" ("70% chance this startup ships by Q3"). Most real founder and AI reasoning is this kind. **[Established]** as a framework; *which interpretation is "right"* is an old, mostly harmless **[Contested]** debate — use whichever fits.

Two combining moves cover most everyday cases:
- **AND (independent events): multiply.** Two fair coins both heads → ½ × ½ = ¼.
- **OR (mutually exclusive): add.** Rolling a 1 *or* a 2 → 1/6 + 1/6 = 1/3.

## Conditional probability: updating on evidence
The workhorse is **conditional probability**, written **P(A | B)** — "the probability of A *given that* we know B." Learning B changes the odds of A. *"Chance of rain"* is one number; *"chance of rain given the sky is black"* is a very different one. **Almost all useful reasoning is conditional** — you're never starting from zero; you always know *something*.

## Bayes' rule — the crown jewel
Bayes' rule is the precise recipe for *updating a belief when new evidence arrives*. In plain words:

> **new belief ∝ (how much you believed it before) × (how well it explains the evidence)**
> *(posterior ∝ prior × likelihood)*

Why it's the most important idea here: it forces you to weigh evidence against the **base rate** — how common the thing was to begin with — and people (and hyped AI claims) constantly forget the base rate.

**The medical-test trap (burn this in).** A disease affects **1 in 1,000** people. A test is **99% accurate**. You test positive. Your chance of actually having it is **not 99%** — it's about **9%**. Why: out of 1,000 people, ~1 truly has it (and tests positive), but ~10 healthy people *also* test positive (the 1% error on 999 people). So ~1 in ~11 positives is real → ~9%. The rare base rate swamps the test's accuracy.

> **The lesson a director never forgets:** a strong signal applied to a rare thing still yields mostly false alarms. Always ask *"how common was this to begin with?"* before believing the evidence. This single instinct will save you from countless bad bets and overblown claims.

Bayes is also, quietly, what learning *is*: start with a prior, see data, update. Many AI methods are Bayesian updating wearing an engineering coat (forward link: [0600](0600_what-it-means-to-learn.md)).

## Expected value — how to decide
To choose under uncertainty, weigh each outcome by its probability and sum:

> **Expected value (EV) = Σ (probability of an outcome × its value).**

A bet: 10% chance to win $100, else nothing → EV = 0.10 × $100 = **$10**. If it costs less than $10 to play, it's a good bet *on average*; more, and it isn't. Founders live here: most single bets fail, but a **positive-EV portfolio** of them wins over time. EV turns vague "it might work" into a number you can compare. *(Caveat: EV assumes you can survive the bad outcomes to reach the average — never bet the company on a positive-EV gamble that can wipe you out. Tails matter — next.)*

## Distributions and tails (the shape of uncertainty)
A single probability is thin; reality comes as a **distribution** — the full spread of possible outcomes and how likely each is. Two shapes to carry:
- **The bell curve (normal):** outcomes cluster near an average, extremes rare — heights, measurement noise.
- **Long / fat tails:** rare events are *far* more common and *far* bigger than a bell curve suggests — market crashes, pandemics, viral hits, and arguably **transformative AI outcomes**. Here the *average* is misleading and the **tail dominates** — most of the impact (good or bad) comes from the few extreme events.

A director's reflex: ask *"what does the distribution look like, and what lives in the tail?"* In a fat-tailed world you manage for the extremes, not the average — which is exactly why AI risk and AI upside are both argued from the tails. **[Established]** that tails dominate some domains; *whether AGI outcomes are fat-tailed* is **[Contested → Speculative]** but taken seriously.

A last guardrail: **small samples lie.** A few data points can show any pattern by luck; confidence should scale with how much (and how representative) the data is. This is the seed of overfitting and of why scale matters in learning ([0600](0600_what-it-means-to-learn.md), [1700](../20-machine-intelligence/)).

## How a director uses this
- **Speak in probabilities, not certainties.** "I'm ~70% this works" is more honest and more useful than "this'll work" — and it lets you update gracefully.
- **Run Bayes in your head.** New evidence? Weigh it against the base rate before you move. Demand base rates for any impressive-sounding number.
- **Decide by EV, survive by tails.** Pick positive-EV bets; size them so a bad tail can't kill you.
- **What you delegate:** the calculations, the statistics code, the formal proofs (the AI is excellent at these). **What you own:** framing problems probabilistically, sniffing out base-rate errors, and judging risk by the tail.

## Connections
- **Stands on:** [0300 Information & entropy](0300_information-and-entropy.md) (surprise *is* low probability; entropy is built on probability). Pairs with [0350 linear algebra](../30-math-and-theory/0350_just-enough-linear-algebra.md) as AI's two math languages.
- **Leads to:** learning ([0600](0600_what-it-means-to-learn.md)), machine learning ([1000](../20-machine-intelligence/)), LLMs choosing tokens by probability ([1300](../20-machine-intelligence/)), and decision-making under uncertainty throughout the frontier chapters. A rigorous statistics module can later live in [`30-math-and-theory/`](../30-math-and-theory/) and link back here.
- **Contested?** The probability framework and Bayes — **[Established]**. Frequentist-vs-Bayesian interpretation — **[Contested]** (harmless). Whether AGI outcomes are fat-tailed — **[Speculative]**.

## Proof-of-learning *(do one, from memory)*
1. The 99%-accurate test, 1-in-1,000 disease, you test positive — roughly what's your real chance of being sick, and *why* isn't it 99%?
2. A bet: 5% chance to win $1,000, costs $40 to play. What's the EV — and would you take it once? A thousand times? What changes?
3. In one sentence, why does "manage for the tail, not the average" matter in a fat-tailed world?

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-22)` — created.

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md).*
