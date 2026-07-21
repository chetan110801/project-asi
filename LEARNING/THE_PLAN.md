---
id: c-the-plan
sortkey: 0002
title: The plan — from reading about AGI to working on it
domains: [frontier, approaches-to-agi, method]
level: core
prereqs: [c-approaches-map]
provides: [efficiency-frontier-strategy, the-research-loop, open-questions-ledger, zero-budget-entry-points]
status: ready
rev: 1
created: 2026-07-21
updated: 2026-07-21
---

# The plan — from reading about AGI to working on it

*The map of the eleven bets is finished. This page is about what comes after reading. It argues one thing: the reason you cannot yet work on any of these problems is **not** that you lack money or knowledge — it is that nothing you have done so far has made contact with reality. It then lays out a way to fix that which costs nothing, starts this month, and does not go stale.*

> **You are here:** this is the project's *forward* page. The [map of the eleven approaches](APPROACHES_TO_AGI.md) says **what the bets are**; the [verdict](40-the-verdict/01_which-bets-get-to-agi.md) says **which look strongest**; this page says **what you do about it**. It is the only page in the project that is about your position rather than the field's.
>
> **Where the facts come from:** a live web check done on **2026-07-21** — the ARC Prize Foundation's 2025 results analysis and its ARC-AGI-3 launch material; the ARC-AGI-2 public and Kaggle leaderboards; Jolicoeur-Martineau 2025, *Less is More: Recursive Reasoning with Tiny Networks* (arXiv 2510.04871); EleutherAI's SOAR programme; Prime Intellect's open environment hub; current free-compute quotas on Kaggle and Colab. Figures are dated because they will move. The reasoning is built to survive the numbers changing; the numbers are not.

---

## In one minute

You have ~300,000 words that make you able to **judge** eleven bets on AGI. That is real and most people do not have it. But judgement built only from reading has a specific hole in it: you cannot tell a good idea of your own from a bad one, because nothing has ever pushed back.

The way to close that hole turns out to be cheap, and the reason is a genuine shift in the field that happened in the last six months. On the hardest open reasoning benchmark, **capability at any price has been mostly bought** — the top model now scores above the human panel, spending thousands of dollars a task. **Capability per dollar has not moved nearly as far.** The ARC Prize Foundation states the split directly: the accuracy gap is now bottlenecked by *engineering*, while the efficiency gap is still bottlenecked by *science and ideas*.

Ideas are the input you have. Money is the one you don't. So the plan is: **work the efficiency frontier, where being small is not a handicap and may be the point.** Three existence proofs say this is not wishful thinking — a **7-million-parameter** network beats reasoning models a thousand times its size on ARC-AGI-1; one prize-winning entry ran on a single gaming graphics card; and on the newest benchmark, **purpose-built agents beat the best frontier model by about 34×**.

The rest of this page is the machinery: what you actually have to work with, the repeating loop that turns a question into a result, and the order to do things in.

---

## Part 1 — the honest starting position

Take stock without flattery.

**What you have.** Thirty-five pages. The eleven approaches, each with a card and at least one deep dive. Two cross-cutting pages on limits and on alignment. A verdict that ranks the bets and then argues against its own ranking. The writing is grounded, dated, and disciplined — concepts are explained once and referenced after, not repeated. This is a real asset and it took months.

**What that buys you.** You can follow a frontier argument. You can read a paper's abstract and know which of the eleven bets it belongs to, what it is implicitly claiming, and which critique it has to answer. You can tell when someone is repackaging an old idea. That is genuinely more than most people who work adjacent to this field can do.

**What it does not buy you, and this is the whole problem.** Every page in the project says some version of *"this is not a how-to guide; it is a way to judge the idea."* That was the right scope for mapping. But it means the entire body of work is **judgement about other people's results**. You have never had an idea of your own turn out to be wrong in a way you could not argue with. And that specific experience — being corrected by reality rather than by an argument — is the thing that separates someone who can discuss research from someone who can do it.

There is a second, quieter problem. **Reading goes stale, and it goes stale faster than it feels like it does.** The audit run alongside this page found that the single most load-bearing empirical claim in the map — the one used to argue that machines still cannot handle genuine novelty — was six months out of date and now points the other way if you quote it carelessly. Nothing was done wrong; the field simply moved. Any plan built as "read these things, then you will be ready" has the same flaw built into it. So the plan below is not a reading list.

---

## Part 2 — what changed: the gap moved, it did not close

This is the finding the rest of the plan rests on, so it is worth getting exactly right.

**ARC-AGI-2** is the benchmark built specifically to resist memorisation — puzzles designed so that having read the internet does not help. The project's map uses it as its strongest single piece of evidence that today's systems cannot handle real novelty.

As of **21 July 2026**, that benchmark has **two scores, and they are 3.5× apart**:

| Which leaderboard | What it allows | Best score now | What it means |
|---|---|---|---|
| **Frontier-API public board** | a run may cost up to **$10,000** | **85%** — GPT-5.5 *(GPT-5.4 Pro 83.3%, Gemini 3.1 Pro 77.1%)* | **above** the ~60% human test-panel average |
| **ARC Prize Kaggle track** | no internet, **~$50 per submission**, held-out private set | **24%** at **$0.20 per task** *(NVARC)* | not close to solved |

Read the two rows together and the conclusion is not "machines got general intelligence" and not "nothing changed." It is: **the difficulty moved from one axis to another.** If you are allowed to spend unlimited money, the puzzles fall. If you are held to a budget, they do not.

The ARC Prize Foundation's own summary of its 2025 competition puts it more sharply than I would dare to:

> "The accuracy gap is now primarily bottlenecked by **engineering**, while the efficiency gap remains bottlenecked by **science and ideas**."

Sit with what that sentence says about you. It says that the part of this problem that is now merely hard-but-known — the part solved by more engineers and more GPUs — is closed to you and always was. And it says that the part that is still genuinely open, still waiting on someone to have a better idea, is the part where **spending more money does not help by definition**, because spending more money is what disqualifies you.

That is the best news in this entire project for someone in your position, and it is not a motivational reframe. Three concrete results back it:

- **The Tiny Recursion Model.** Alexia Jolicoeur-Martineau (Samsung SAIL Montréal) published a network with **7 million parameters and 2 layers** that scores **45% on ARC-AGI-1 and 8% on ARC-AGI-2** — beating DeepSeek R1, o3-mini and Gemini 2.5 Pro with **under 0.01% of their parameters**. It does this not by being big but by **recursing on its own answer up to 16 times**, so that depth of thinking substitutes for size of model. *(arXiv 2510.04871.)* A 7-million-parameter model trains on free hardware.
- **CompressARC**, covered already in the [AP8 solver-mechanisms dive](50-deep-dives/02_ap8-deep-dive-solver-mechanisms.md), reached its result **on a single gaming graphics card**, with no pre-training and no search.
- **ARC-AGI-3**, launched 25 March 2026, drops an agent into a small world with *no instructions, no rules, no stated goals*. Humans solve 100%. The best frontier model — Gemini 3.1 Pro — scores **0.37%**. The best **purpose-built agent** scores about **12.6%**: roughly **34× better than the frontier model**, built by people rather than bought by a lab.

That last comparison is the one to keep. On the newest open problem in the field, the thing that wins is not the biggest model. It is somebody who thought carefully about the problem.

---

## Part 3 — the rule this gives you

From Part 2, a filter that decides what you work on. Before spending time on any problem, ask three questions:

1. **Is the bottleneck ideas or resources?** If the honest answer is "this needs more compute / more data / more engineers," it is not your problem, no matter how interesting. If the answer is "nobody knows how to do this efficiently," it might be.
2. **Is there a scoreboard you can actually reach?** An open benchmark, a public leaderboard, a reproducible baseline. Something that can tell you that you are wrong without asking anyone's permission. Contact with reality is the whole point; a problem with no scoreboard cannot give it to you.
3. **Can the smallest honest version of it run in under 30 GPU-hours?** That is your weekly free quota (Part 4). If the smallest version that would teach you something does not fit, either shrink it further or pick something else.

**What this rules in:** efficiency-constrained reasoning (AP8, AP2), small-model and test-time-adaptation work, agent design on interactive benchmarks (AP3 + AP8 + AP9 meeting at ARC-AGI-3), evaluation and measurement work — designing tests that catch what current tests miss — and reproduction of published results, which is undervalued and teaches more per hour than anything else on this list.

**What this rules out, honestly:** pre-training anything (AP1), whole-brain emulation (AP11 — it needs a scanning lab), most robotics (AP10 — it needs a robot), and anything whose smallest interesting version still needs a cluster. These stay as things you *understand*, which is what the map is for. They do not become things you *do*.

> **This is a narrowing, and it should feel like one.** Eleven bets, and roughly four are open to you. That is not a failure of ambition; it is the difference between a plan and a wish. The four that are open are open *now*, for free, with public scoreboards.

---

## Part 4 — what you actually have to work with

Concrete inventory, checked 2026-07-21. All figures move; the categories do not.

**Free compute, in practice.**
- **Kaggle Notebooks** — **30 GPU-hours per week**, guaranteed, on T4 or P100 hardware (16–20 GB), 9-hour session cap. The quota is fixed and resets weekly; it does not fluctuate with demand. This is the most reliable free compute available and it is also where the ARC Prize competitions are hosted, which is not a coincidence.
- **Google Colab free tier** — roughly **22 hours per week** in practice on T4, but variable: 2026 introduced a compute-unit system, so heavy use throttles.
- **NAIRR** (US National AI Research Resource) — moving from pilot to permanent operations; aggregates donated compute including a $20M Azure commitment. Allocations are applied for with a proposal. Worth knowing exists; not a starting point.

Thirty GPU-hours a week is not a lot. It is also considerably more than the Tiny Recursion Model needed, and TRM beat models that cost tens of millions of dollars to train.

**Open competitions with real scoreboards.**
- **ARC Prize 2026** — over **$2M** total across three tracks, hosted on Kaggle. The ARC-AGI-3 track alone carries **$850K**: a $700K grand prize for 100%, $75K split among the top five, and — the part that matters for you — **$75K in milestone prizes for open-source submissions**, with deadlines at **30 June 2026** (passed) and **30 September 2026** (open). Entry is free. Rules: submissions through Kaggle only, no internet access during evaluation, and **all code and methods must be open-sourced to be eligible**.

  Be clear-eyed about this. You are not going to win $700K. The realistic value is that submitting is free, scored against a held-out set, publicly ranked, and forces you to produce working code that someone else can run. That is contact with reality on a deadline, which is worth more than the prize money is to you.

**Places that take people with no affiliation.**
- **EleutherAI's SOAR** (Summer of Open AI Research) — a five-week, fully online mentored research programme that **explicitly encourages applicants with no prior research experience**, and where participants can earn authorship credit on real outputs. This is the single most direct route from where you are to having done real research with real researchers.
- **Prime Intellect** — runs an open hub for **RL environments** with open-source libraries (Prime-RL, Verifiers) and a public leaderboard. Contributing a good environment requires design thinking, not a datacentre, and it is genuinely wanted.

**What you honestly cannot do, and should stop feeling bad about.** Train a frontier model. Run experiments that need a week on 256 GPUs. Access private evaluation sets. Get a result that requires proprietary data. None of these are close, and no amount of cleverness closes them.

---

## Part 5 — the loop

This is the part that makes the plan **dynamic and iterable** rather than a syllabus, and there is a specific reason it has to be a loop.

A syllabus written in January was materially wrong by July — the audit proved it on this project's own most important claim. Any plan of the form "learn these twelve things, then you will be ready" decays at the speed of the field, and the field is currently moving faster than the plan can be rewritten. A loop does not have that failure mode, because **re-grounding is a step inside it** rather than a maintenance chore outside it.

One turn of the loop. Aim for **one to two weeks**, and one visible artifact at the end.

**① Pick one question from the ledger.** Not a topic — a question, with a stated form of answer. The ledger is built in Phase 1 below.

**② Ground it, twice.** Once against the corpus you already have; once against the live web, because the corpus may be six months stale and you now know exactly what that costs. Write down what is already known, who established it, and when. If this step takes more than a day, the question was too big.

**③ Shrink it until it runs.** The hardest and most valuable step. Take the question and cut it down until the smallest version that could still surprise you fits in your weekly quota. "Does recursive depth substitute for parameter count?" does not fit. "Does TRM's accuracy degrade gracefully or fall off a cliff when I cut its recursion steps from 16 to 8 to 4?" fits, is unanswered in the paper, and takes an afternoon.

**④ Run it.** Write the code with AI assistance — that is what it is for, and the project's own standing position is that execution is assumed, not the achievement. The achievement is that the experiment was worth running.

**⑤ Write what happened — especially if nothing did.** A short page: the question, the setup, the result, and what you now believe that you did not believe before. Negative results count and are usually more informative. This page is the artifact; it is also what makes the work showable.

**⑥ Update the ledger and the map.** Close the question, or split it into the two sharper questions it turned out to be. If the result touches one of the eleven approach pages, revise that page. **The map is now downstream of your own results, not only of other people's.** That is the transition this whole plan exists to make.

Then go back to ①.

> **Why the loop beats reading more, in one sentence:** reading gives you other people's conclusions, which is judgement; the loop gives you your own error rate, which is calibration — and calibration is the thing that lets you tell your good ideas from your bad ones without waiting for someone to publish the answer.

---

## Part 6 — the order to do it in

Four phases. The first two are repair and setup and should not take long. Phases 3 and 4 are the actual work and do not end.

| Phase | What | Why it is here | Rough size |
|---|---|---|---|
| **0 · Repair** | The `QUEUED` fixes from the [audit](../REVIEWS/AUDIT_2026-07-21_v3.0.md): fix the stale ARC-AGI-2 argument, break the eleven cards out of their single-paragraph form, retire the P1–P7 naming, archive the dead scaffolding | The front door is currently the hardest page to read, and the map's strongest claim currently points the wrong way. Both are cheap to fix and both mislead you every time you use them | 2–3 sessions |
| **1 · Build the ledger** | Harvest every "Stuck #N" and every Honesty-box admission across all 35 pages into one ranked file of open questions, each tagged by what it would take to attack it: **read / reproduce / experiment / needs-a-lab** | The single highest-leverage thing available, and it needs no new research — the questions are already written, just scattered across 300,000 words where nothing can be done with them. This file is what converts a library into an agenda | 1–2 sessions |
| **2 · First turn of the loop** | Pick the easiest `reproduce`-tagged question and run it end to end. Suggested first: **reproduce TRM at 7M parameters on ARC-AGI-1**, then vary one thing — recursion depth — and report the curve | Reproduction is the cheapest possible contact with reality. You find out immediately whether you can actually get a published result to run, which is a skill nobody tells you is separate from understanding the paper | 1–2 weeks |
| **3 · Enter something real** | The ARC-AGI-3 Kaggle track, aiming at the **30 September 2026** open-source milestone rather than the grand prize | A public, held-out, dated scoreboard. Free to enter. Forces working code. The 12.6%-vs-0.37% gap means a thoughtful agent is genuinely competitive here | ongoing |
| **4 · Loop** | Repeat Part 5. Every third or fourth turn, re-ground one approach page against the live web and revise it | Keeps the map alive and keeps you calibrated. This is the steady state | forever |

**The first concrete thing to do after reading this page** is Phase 1 — build the ledger. It takes one session, needs no new information, and every subsequent decision gets easier once it exists.

---

## Part 7 — the three ways this plan is wrong

Stated in advance, so reality can correct it rather than me defending it.

**Break #1 — the efficiency frontier might close the same way the accuracy frontier did.** The whole plan rests on efficiency being idea-bound rather than resource-bound. But that was also true of accuracy in 2024, and accuracy is now "bottlenecked by engineering." If a lab decides efficiency is the next target and points a hundred researchers at it, the window in Part 2 closes, and it could close within a year. *Early warning sign:* the Kaggle-track ARC-AGI-2 score jumping sharply — say past 50% — driven by a well-resourced team rather than an individual. *If it happens:* the response is to move to whatever is newly unsaturated, not to compete on the closed frontier. Benchmarks that resist saturation keep being built precisely because the old ones fall.

**Break #2 — reproduction may teach less than I claim.** I have asserted that reproducing TRM teaches more per hour than reading. It might instead teach mostly software debugging: environment versions, CUDA errors, and dataset formatting, with very little insight per hour. *Early warning sign:* two weeks in, everything you have learned is about tooling. *If it happens:* switch to the `experiment` tag — design a small original test — and treat reproduction as infrastructure rather than education.

**Break #3 — this may be too narrow too early.** Part 3 cuts eleven approaches down to about four. If the interesting question turns out to live in AP5 or AP6, the filter will have steered you away from it for reasons that are about your budget rather than about the problem. *Early warning sign:* the ledger's best questions cluster in approaches the filter excluded. *If it happens:* the honest move is to keep understanding those approaches through the map and accept that you will contribute to them later, through people who have the resources, rather than pretending the filter was wrong.

---

## ⚠️ Honesty box

- **Nothing here has been tested.** This plan was written on 2026-07-21 and no turn of the loop has been run. The reasoning is sound as far as I can check it; the practice is unproven. Treat Phase 2 partly as a test of this page.
- **The 85% ARC-AGI-2 figure is second-hand.** It comes from leaderboard aggregators that agree with each other and with ARC Prize's documented $10,000 display cap, but it was not read off `arcprize.org` directly. Verify it before quoting it in an argument. The two-track *structure* is well-sourced; the exact top number is the soft part.
- **"You will not win $700K" is a judgement, not a fact.** It is the right expectation to hold, but the milestone prizes are genuinely winnable by a good open-source submission and are the reason Phase 3 targets September rather than the grand prize.
- **The 30-GPU-hour filter is a rule of thumb, not a law.** Some worthwhile things need 100 hours across several weeks. The rule exists to stop you starting work you cannot finish, not to forbid patience.
- **This page will go stale too.** Every number in Part 4 is dated. The competition deadlines pass. The free quotas change. If you are reading this more than six months after 2026-07-21, re-ground Part 4 before acting on it — which is exactly what step ② of the loop is for.

---

## How to use this

- **If you have one session:** do Phase 1. Build the ledger. Nothing else unlocks as much.
- **If you have one week:** Phase 1, then step ② of the loop on the single question that looks most attackable. Stop before running anything. Just find out what is actually known.
- **If you are deciding whether to read another deep dive:** don't, unless it is the one that a live question in the ledger sends you to. Sixteen deep dives is enough to judge the field. The marginal seventeenth is worth much less than the first experiment.
- **If you want to direct AI work:** the loop is the transferable part. Question → ground → shrink → run → write → update is how research is actually managed, at any scale. Practising it on 30 GPU-hours is practising the same skill you would use on 30,000.

---

## Connections

- The bets this plan filters: [the map of the eleven approaches](APPROACHES_TO_AGI.md), and the ranking it argues with, [the verdict](40-the-verdict/01_which-bets-get-to-agi.md).
- Where the efficiency-frontier argument was first made in this project, and in more depth on ARC specifically: [AP8 · deep dive — the research frontier](50-deep-dives/03_ap8-deep-dive-the-research-frontier.md), Part 3.
- The small-model results Part 2 rests on: [AP8 · deep dive — solver mechanisms](50-deep-dives/02_ap8-deep-dive-solver-mechanisms.md).
- The approach an ARC-AGI-3 agent actually reaches into: [AP3 · agents](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md), [AP4 · RL from interaction](20-the-approaches/04_ap4-rl-from-interaction.md), [AP9 · open-endedness](20-the-approaches/09_ap9-open-endedness.md).
- What this plan was written in response to: [the 2026-07-21 audit](../REVIEWS/AUDIT_2026-07-21_v3.0.md).

---

## Check yourself *(try one, from memory)*

1. ARC-AGI-2 has two current scores that differ by about 3.5×. What separates them, and why does the difference matter more than either number?
2. Why is "the efficiency gap is bottlenecked by science and ideas" specifically good news for someone with no compute budget — and what would have to happen for it to stop being true?
3. State the three questions from Part 3 that decide whether a problem is worth your time. Which of the eleven approaches do they rule out, and why is ruling them out not the same as ignoring them?
4. Why is this written as a loop rather than a reading list? Give the concrete evidence from this project that a reading list would have failed.

---

## Revision notes

- **rev 1 · 2026-07-21 · new.** Written in response to the [2026-07-21 audit](../REVIEWS/AUDIT_2026-07-21_v3.0.md) finding E1: the project could teach you to judge the eleven bets but not to work on one, and the only material that pointed at doing was buried in Part 3 of the sixteenth deep dive. Promotes that argument to a first-class page, generalises it past AP8, and grounds it in a live web check of the ARC-AGI-2 two-track split, ARC-AGI-3's frontier-vs-purpose-built-agent gap, the Tiny Recursion Model, current free-compute quotas, and the ARC Prize 2026 milestone deadlines.
