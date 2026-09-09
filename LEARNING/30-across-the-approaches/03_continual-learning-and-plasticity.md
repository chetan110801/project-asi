---
id: c-continual-learning
sortkey: 3003
title: Continual learning — why the networks go dead, and which bets it blocks
domains: [frontier, approaches-to-agi, cross-cutting]
level: core
prereqs: [c-next-word, c-ap1-scale, c-ap4-rl]
provides: [catastrophic-forgetting, loss-of-plasticity, stability-plasticity-dilemma, continual-backprop, replay-regularization-architecture, frozen-weights-problem]
resources: []
status: ready
reading_time: 18 min
rev: 1
created: 2026-09-09
updated: 2026-09-09
---

# Continual learning — why the networks go dead, and which bets it blocks

*A thread running across the whole map, not a bet of its own. Every approach here assumes, somewhere, that a system can go on learning. Almost none of them check. This page is the check: what actually happens to a deep network asked to learn one thing after another for a long time, why the answer is worse and stranger than "it forgets", and which of the twelve bets that leaves standing.*

> **You are here:** the third page of **③ Across the approaches** — threads that cut across all the bets rather than competing with them. Its siblings: [the bounds — data, compute, energy](01_the-bounds-data-compute-energy.md) *(the physical ceilings)* and [alignment, control and self-improvement](02_alignment-control-and-self-improvement.md) *(the risk axis)*. This page is the third ceiling: **the learning one.** It is the technical obstacle underneath [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md), but it does not belong only to AP12, which is why it lives here.

> **Where the facts come from:** a live web pass on **2026-09-09**. Dohare, Hernandez-Garcia, Lan, Rahman, Mahmood & Sutton, *"Loss of plasticity in deep continual learning"*, **Nature** 632 (2024). Abbas et al., *"Loss of Plasticity in Continual Deep Reinforcement Learning"* (2023). The standard continual-learning survey literature on the replay / regularisation / architecture taxonomy, and the stability–plasticity dilemma as it comes from psychology. Plus 2026 survey work on continual learning in large language models. Figures are dated; the two failure modes are not going to change.

---

## In one minute

Ask a deep network to learn a long sequence of tasks — the way a life is lived rather than the way a dataset is served — and **two different things can go wrong, and they are opposites.**

- **Catastrophic forgetting:** it loses what it already knew. Everyone knows about this one. Most of the field works on it.
- **Loss of plasticity:** it loses the *ability to learn anything new*. Its capacity to absorb information wears out. Far fewer people work on this one, it was measured properly only recently, and it is the more alarming of the two — because a system that has forgotten can be retaught, and a system that has gone inert cannot.

You cannot simply fix both at once, because they are ends of one trade-off: **stability** keeps what you know, **plasticity** lets new things in, and turning either up turns the other down. That is the **stability–plasticity dilemma**, and it was named in psychology long before it was a deep-learning problem.

Why this belongs on a map of routes to AGI: **every frontier model in 2026 is trained once and then frozen.** After deployment the weights do not change. If continual learning is merely an engineering convenience, that is fine. If it is a requirement for intelligence, then the entire industry is building recordings of minds rather than minds — which is exactly [AP12's](../20-the-approaches/12_ap12-oak-experience-only-agents.md) claim.

---

## Part 1 — the two failures, precisely

The distinction is the single most useful thing on this page, so here it is stated as sharply as it can be.

| | **Catastrophic forgetting** | **Loss of plasticity** |
|---|---|---|
| What is lost | Useful information you already had | The ability to take in useful new information |
| Symptom | Old tasks degrade as you learn new ones | New tasks stop being learnable at all |
| Feels like | Amnesia | Rigidity — the network has set |
| How well known | Very. Decades of work. | Recently measured, much less studied |
| Which pole of the dilemma | Too much plasticity | Too much stability |

::: key
**Why the second is worse.** A network that has forgotten task 1 can be shown task 1 again and will relearn it. A network that has lost plasticity cannot learn task 1 *or* task 2,000 — nothing gets in. The first is a memory problem. The second is closer to death.
:::

**Why it happens** is not fully settled, and the honest answer is that several mechanisms are implicated rather than one. Units drift into regions where they stop responding — effectively dead. The distribution of weights loses the diversity it started with. The curvature of the loss surface changes in ways that make further progress hard. The common thread is that the *randomness the network was initialised with* — its raw material for learning — is spent, and nothing replenishes it.

---

## Part 2 — the measurement

Before 2024 this was mostly folklore. Sutton's group turned it into a number and put it in **Nature**.

**The setup:** take ImageNet, and instead of training on it once, repurpose it into a long sequence of separate tasks, presented one after another — thousands of them. Train a standard deep network straight through with ordinary backpropagation. Measure how well it learns *each new task as it arrives*, not how well it remembers old ones.

**The result:** accuracy on a newly presented task fell from roughly **89% early on to roughly 77% by the two-thousandth task.**

Read what that measures carefully, because it is easy to misread. It is not saying the network got 77% on the whole benchmark. It is saying that **the network's ability to learn a fresh task decayed by roughly twelve points over its lifetime** — the learning machinery itself wore out. And this is with standard, correct, unmodified deep learning: no bug, no misconfiguration, no adversarial setup.

The same effect has been shown separately in **continual deep reinforcement learning** (Abbas et al., 2023), which matters because RL is the setting where a long, unbroken stream of experience is the *normal* case rather than an artificial one.

---

## Part 3 — the fixes, and how far they get

Continual-learning research splits into three families. They were mostly built against forgetting; their record against plasticity loss is thinner.

| Family | The idea | Honest limits |
|---|---|---|
| **Replay** | Keep some old data and mix it back in. Consistently the strongest family against forgetting. | Needs to store or regenerate past data — which the strict experience-only position of [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md) rejects outright, and which does not scale to a lifetime. Does not directly restore plasticity. |
| **Regularisation** | Penalise moving weights that mattered for earlier tasks. | Buys stability by *reducing* plasticity — it can trade one failure for the other rather than solving either. |
| **Architecture** | Give new tasks new capacity — extra units, adapters, separate subnetworks. | Capacity grows with the number of tasks. A lifetime has no bound on tasks. |

**Continual backpropagation** — the fix proposed alongside the Nature result — attacks plasticity directly rather than forgetting, which is why it does not fit the three families cleanly. Two moves: give **every weight its own step-size**, tuned continuously rather than set globally; and **keep injecting fresh randomly-initialised units** to replace ones that have gone inert, so the supply of raw learning material is replenished instead of spent.

::: note
**The claim attached to it is strong.** Sutton's position is that loss of plasticity is *curable* — that this is a solvable algorithmic problem, not a law of deep networks. That is a real prediction and it will be tested. It has not been demonstrated at frontier scale, and treating "curable in principle" as "solved" is the mistake to avoid here.
:::

---

## Part 4 — which bets this blocks, and which it does not

The point of a cross-cutting page. Each bet is affected differently, and some barely at all.

| Bet | How much continual learning it needs | Reading |
|---|---|---|
| [**AP1 · Scale**](../20-the-approaches/01_ap1-scale-and-foundation-models.md) | 🟢 None, by design | Train once, freeze, ship. That is the paradigm, and it works commercially. AP12 says that is the problem; AP1 says it is the point. |
| [**AP2 · Reasoning**](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | 🟢 Low | Thinking longer happens in the forward pass; no weights change. Adaptation is per-query and thrown away. |
| [**AP3 · Agents**](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | 🟡 Medium — and it is being faked | Agents "remember" through context windows, retrieval and scratchpads, not weight updates. That works and it is not learning; it is note-taking. The 2026 long-task wall shows up right where the notes stop scaling. |
| [**AP4 · RL from interaction**](../20-the-approaches/04_ap4-rl-from-interaction.md) | 🔴 High | A long stream of experience is RL's native setting, and the plasticity result has been reproduced there. |
| [**AP5 · World models**](../20-the-approaches/05_ap5-world-models-jepa.md) | 🟡 Medium | A world model of a changing world has to be updated; in practice they are trained in batches like everything else. |
| [**AP6 · Brain-based**](../20-the-approaches/06_ap6-brain-based.md) | 🔴 High — and it is the pointed comparison | Brains do this continuously for eighty years on twenty watts. Whatever they do, it is not what backpropagation does. |
| [**AP7 · Neurosymbolic**](../20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | 🟢 Low on the symbolic side | Symbolic knowledge updates by editing a rule, which has no plasticity problem at all. This is a genuine and underrated advantage of the hybrid position. |
| [**AP8 · Program synthesis**](../20-the-approaches/08_ap8-program-synthesis-arc.md) | 🟡 Medium | Test-time training is adaptation, but short-lived and discarded. Growing a persistent library across tasks would hit this wall. |
| [**AP9 · Open-endedness**](../20-the-approaches/09_ap9-open-endedness.md) | 🔴 High, and mostly unexamined | An endlessly generating system requires endlessly learning solvers. Most work runs short enough not to notice. **This is an under-asked question in AP9 and a good place to look for one of your own.** |
| [**AP10 · Embodiment**](../20-the-approaches/10_ap10-embodiment.md) | 🔴 High | A robot that cannot adapt after deployment is a fixed appliance. |
| [**AP11 · Whole-brain emulation**](../20-the-approaches/11_ap11-whole-brain-emulation.md) | 🔴 Total, but inherited | If you copy a brain faithfully you copy whatever solves this. You do not solve it; you inherit the solution without understanding it. |
| [**AP12 · OaK**](../20-the-approaches/12_ap12-oak-experience-only-agents.md) | 🔴 It *is* the bet | Not a requirement of the approach — the approach exists because of it. |

::: key
**The pattern worth seeing.** The bets that need continual learning most are exactly the ones with the least to show — AP4's open-world claim, AP6, AP9, AP10, AP12. The bets that have delivered the visible results of the last five years — AP1, AP2 — need it least. That correlation is either a coincidence, or it is the reason the frozen-weights paradigm won: **it won partly by choosing the problems that do not require the unsolved thing.** Whether that is a clever avoidance or a permanent ceiling is the open question, and it is the same question [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md) closes on.
:::

---

## Part 5 — the frontier version of the problem

There is a live, well-funded version of this that does not mention plasticity at all: **how do you update a deployed language model?**

The 2026 survey framing splits it into three stages — **continual pre-training** (keep absorbing new world knowledge), **continual fine-tuning** (keep acquiring new skills), and **continual alignment** (keep the values current as norms shift). Each is an active area with real money behind it, and none is solved.

What the industry actually does instead, today, is route around the problem: **retrieval** (look it up rather than learn it), **long context** (put it in the prompt), and **periodic retraining** (a new model every few months). All three work. None is learning, and all three have the same tell — the model's weights are identical before and after it "learned" something.

::: warn
**The question to hold, without deciding it yet.** Is routing around the problem a permanent engineering answer, or a temporary one that stops working when tasks get long enough? [AP3's deep dive](../50-deep-dives/08_ap3-deep-dive-inside-the-agent-loop.md) found the 2026 long-task wall to be a **context-handling** gap rather than a reasoning gap. That is consistent with the workarounds holding — and it is also exactly what running out of note-taking room would look like from the inside. The evidence does not yet separate the two readings.
:::

---

## Open questions

1. **Is loss of plasticity curable at scale?** Continual backprop works in the published settings. Nobody has shown it at frontier scale, and the claim that it is generally curable is a prediction, not a result.
2. **Can you have stability and plasticity at once, or is the dilemma fundamental?** Every current method trades one for the other. Whether that trade is a limitation of our algorithms or a property of distributed representations is open.
3. **How would we even know a system was still learning?** There is no standard metric for "is this network still plastic" that is reported alongside accuracy. The field measures forgetting routinely and plasticity almost never.
4. **Do the workarounds have a ceiling?** Retrieval, long context and periodic retraining currently substitute for learning. If they scale indefinitely, AP12's critique is philosophical. If they do not, it is structural.
5. **Why do brains not have this problem?** Eighty years of continual learning on twenty watts, with no catastrophic forgetting and no observed plasticity collapse in the relevant sense. Whatever the mechanism is, it is not in our models — which is a live argument for [AP6](../20-the-approaches/06_ap6-brain-based.md).

---

## ⚠️ Honesty box

- **The 89%→77% figure is one experiment's shape, not a universal constant.** It is the headline from a specific ImageNet-derived continual setup. The *phenomenon* replicates broadly; that particular pair of numbers does not transfer to other settings and should not be quoted as if it did.
- **"Why plasticity is lost" is genuinely unsettled.** I gave several candidate mechanisms — dead units, weight-distribution collapse, curvature change — because the literature gives several. Anyone stating one confident cause is ahead of the evidence.
- **Part 4's ratings are my judgement.** No paper grades the twelve approaches for continual-learning dependence. The reasoning is given in each row so you can disagree with a specific one rather than the table.
- **I may be overweighting this thread** because it arrived through [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md), whose author has an obvious stake in it being central. The counter-position — that frozen weights plus retrieval is simply the right engineering answer, and continual learning is a solution looking for a problem — deserves more weight than a page written from this direction naturally gives it.
- **The LLM continual-learning literature moves monthly.** The three-stage framing in Part 5 is current as of 2026-09-09 and the specific methods under it will be stale quickly.

---

## Connections

- Its siblings on this shelf: [the bounds — data, compute, energy](01_the-bounds-data-compute-energy.md) · [alignment, control and self-improvement](02_alignment-control-and-self-improvement.md).
- The bet built on this obstacle: [AP12 · OaK](../20-the-approaches/12_ap12-oak-experience-only-agents.md), and its ramp: [how to start on it](../60-entry-ramps/02_ap12-oak-continual-learning.md).
- The bets most exposed to it: [AP4](../20-the-approaches/04_ap4-rl-from-interaction.md) · [AP6](../20-the-approaches/06_ap6-brain-based.md) · [AP9](../20-the-approaches/09_ap9-open-endedness.md) · [AP10](../20-the-approaches/10_ap10-embodiment.md).
- Where the workarounds were examined: [AP3 · inside the agent loop](../50-deep-dives/08_ap3-deep-dive-inside-the-agent-loop.md).

---

## Check yourself *(try one, from memory)*

1. State catastrophic forgetting and loss of plasticity in one line each, and say why the second is the more serious.
2. What is the stability–plasticity dilemma, and why does it mean you cannot simply fix both?
3. What did the Nature 2024 experiment actually measure — and what is the common misreading of the 89%→77% figure?
4. Name the three families of continual-learning method and one honest limit of each.
5. AP1 and AP2 have delivered the most visible results and need continual learning least. Give both readings of that correlation.

---

## Revision notes

- **rev 1 · 2026-09-09 · new.** Created alongside [AP12](../20-the-approaches/12_ap12-oak-experience-only-agents.md) when the learner surfaced Sutton and Javed's Oak Lab and a project-wide grep showed continual learning was absent from the map entirely — no page, no registry entry, no mention in any of the eleven cards. Placed as a cross-cutting page rather than inside AP12 because the obstacle is not AP12's property: it constrains AP4, AP6, AP9, AP10 and AP11, and the *absence* of a constraint is part of why AP1 and AP2 have gone as far as they have. Grounded in the Nature 2024 plasticity result, the 2023 continual-RL replication, the standard survey taxonomy, and 2026 survey work on continual learning in LLMs.
