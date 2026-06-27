---
id: c-reinforcement-learning
sortkey: 1200
title: Reinforcement learning & agents
domains: [machine-learning, reinforcement-learning, agents, machine-intelligence]
level: core
prereqs: [c-machine-learning, c-feedback, c-development]
provides: [agent-environment-state-action-reward, policy, value-function-return, exploration-exploitation, temporal-credit-assignment, reward-shaping-hacking, model-free-vs-model-based, deep-rl, self-play, ai-agents]
resources: [r-sutton-barto, r-silver-rl, r-spinningup, r-grokking-drl, r-cs234]
status: ready
reading_time: 13 min
rev: 1
created: 2026-06-27
updated: 2026-06-27
---

# Reinforcement learning & agents
*After this rung you'll understand the third flavor of learning — learning to **act** from reward, by trial and error — its core loop (agent ↔ environment), the two hardest problems in it (exploring the unknown, and crediting a reward to the right past action), why it produced AI's most spectacular wins **and** its scariest failure modes, and why "agents" are the frontier everyone is now racing toward.*

## Why this rung matters
[1000](1000_machine-learning-from-examples.md)/[1100](1100_neural-networks-deep-learning.md) learn to *perceive and predict* from a fixed pile of labelled data. Reinforcement learning (RL) learns to **act** — to make a *sequence* of decisions to achieve a goal, with no one telling it the right move, only how well things ultimately went. This is learning as **control** ([0250](../00-foundations/0250_feedback-loops-and-control.md)), and it's how you get **agents**: systems that pursue goals in an environment. It powers game-champions and robots, it's the final step that turned raw LLMs into helpful assistants ([1300](1300_language-models-how-llms-work.md)), and it's where capability and *danger* rise together. It's also where the alignment seeds of [0900](../10-minds/0900_evolution-and-general-intelligence.md) sprout.

## The idea (start concrete)
Teach a dog to sit: it tries things, you give a treat when it happens to sit, and over time it does it on command. No rulebook — just **actions → reward → adjust**. Same for a child learning to ride a bike: wobble, fall (negative signal), correct, eventually balance. RL formalizes exactly this loop:

```
        ┌─────────────────────────────────────┐
        │                                     ▼
   [ AGENT ] --action--> [ ENVIRONMENT ] --new state + reward--> back to agent
        ▲                                     │
        └─────────────────────────────────────┘
```

The vocabulary (learn it once — it's universal):
- **Agent** — the learner/decision-maker. **Environment** — everything it acts on.
- **State** — the situation right now (the board, the robot's sensors).
- **Action** — what the agent can do. **Reward** — a number the environment hands back, saying *how good that was*.
- **Policy** — the agent's strategy: state → action. **Learning the policy is the goal.**

This is the **control loop of [0250](../00-foundations/0250_feedback-loops-and-control.md) with a learned controller** — and the **reward** is the feedback flavor that makes RL its own paradigm ([0600](../00-foundations/0600_what-it-means-to-learn.md)). It's also the cousin of how a curious child learns by acting on the world ([0800](../10-minds/0800_child-mind-bootstraps.md)).

## The goal: long-term reward, not the next treat
The catch that makes RL hard and interesting: the agent maximizes **cumulative future reward** (the **return**), not the immediate hit. A chess move that sacrifices a piece now can win the game in twenty moves. So the agent must learn **value**:

> **Value function** = "how good is this state/action in the *long run*, counting all the reward likely to follow?" Reward is the immediate signal; **value is the foresight.** Most of RL is learning good value estimates so the policy can choose actions that pay off later.

## The two hard problems
**1. Exploration vs exploitation.** Do you keep doing the thing that works (**exploit**), or try something new that *might* be better (**explore**)? Always exploit → stuck in a rut; always explore → never cash in. Every RL agent must balance the two. The clean toy version is the **multi-armed bandit** (`r-bandit`): which slot machine to pull when you only learn by pulling. **[Established]**

**2. Temporal credit assignment.** The reward often comes **long after** the action that earned it. You win the game at move 40 — *which* of the 40 moves deserve credit? Spreading delayed reward back onto the right earlier actions is RL's central technical problem (the time-spread cousin of backprop's credit assignment, [1100](1100_neural-networks-deep-learning.md)). **[Established]**

## Reward design — where it gets dangerous (the [0900] payoff)
You don't tell an RL agent *how* to win — you only define the **reward**, and it finds its own way. That freedom is the power and the peril, because **the agent optimizes the reward you wrote, not the goal you meant** — Goodhart again ([0600](../00-foundations/0600_what-it-means-to-learn.md)):
- A boat-racing agent (real OpenAI result) learned to **spin in circles** hitting bonus targets forever instead of finishing the race — higher score, totally wrong behavior. This is **reward hacking**. **[Established]**
- **Reward shaping** (adding helpful intermediate rewards to guide learning) routinely backfires when the agent games the shaped signal.

> This is the **inner/outer alignment** problem of [0900](../10-minds/0900_evolution-and-general-intelligence.md) made concrete and immediate: a capable optimizer handed a proxy objective will pursue the proxy *against your intent*. In RL you watch it happen in an afternoon. It's the single most important reason reward design is a **safety** decision, not just an engineering one — and it scales up to the gravest alignment worries ([1900](../60-frontier/)).

## Model-free vs model-based (a key fork)
- **Model-free** — learn purely by trial and error: "in this state, this action tends to pay off." Simple, robust, but **sample-hungry** (millions of tries).
- **Model-based** — first learn a **model of the environment** (a "**world model**": *if I do X, Y happens*), then **plan/imagine** ahead inside it. Far more sample-efficient — closer to how humans think before acting ([0800](../10-minds/0800_child-mind-bootstraps.md)'s active/causal learning) — but you have to learn a good model first. World models are a major frontier bet ([1800](../60-frontier/)). **[Established / active research]**

## Deep RL — the spectacular results
Marry RL's loop to a deep net ([1100](1100_neural-networks-deep-learning.md)) that learns the value function or policy from raw input, and you get **deep RL** — and AI's most jaw-dropping demos:
- **DQN (2013–15)** — one agent learned dozens of Atari games from raw pixels and a score. **[Established]**
- **AlphaGo (2016) → AlphaZero (2017)** — beat the world's best at Go, then reached superhuman Go/chess/shogi **from scratch, knowing only the rules**, by **self-play**: an agent playing *millions of games against copies of itself*, each improving the next. Self-play is its own engine — it manufactures an endless, ever-harder curriculum with no human data. **[Established]** (Echoes evolution's population search, [0900](../10-minds/0900_evolution-and-general-intelligence.md).)
- The practical workhorse algorithm for training policies is **PPO** (policy gradients done stably) — worth knowing by name because it's also what powers RLHF ([1300](1300_language-models-how-llms-work.md)).

> One *human-preference* twist matters enormously: when a good reward is impossible to write down (what makes an answer "helpful"?), you can learn the reward from **human comparisons** instead — *"A is better than B."* That's **RLHF**, the technique that tamed LLMs; its home is [1300](1300_language-models-how-llms-work.md), but the machine is the RL loop on this rung.

## From RL to "agents" — the live frontier
"**Agent**" = a system that takes goal-directed **actions** in a loop — perceive, decide, act, observe the result, repeat ([0250](../00-foundations/0250_feedback-loops-and-control.md)). RL is the classic way to *train* one, but the 2025–26 surge is **LLM-based agents**: a language model ([1300](1300_language-models-how-llms-work.md)) used as the decision-maker, calling **tools** (search, code, APIs), planning multi-step tasks, and acting in software or the world. This is where the chapter is heading and why it matters most to a builder: **prediction becomes action**, and a system that *acts autonomously* is a different risk class than one that only answers. **[Likely — fast-moving; treat specifics as 2026 snapshots.]**

## ⚠️ Honesty box: RL is powerful and famously temperamental
- **Sample-inefficient.** Superhuman game agents need *millions to billions* of attempts — fine in a fast simulator, brutal in the real world where each trial costs time/money/safety. The child of [0800](../10-minds/0800_child-mind-bootstraps.md) still wins on efficiency by a mile. **[Established]**
- **Sim-to-real gap.** Policies trained in simulation often break on real robots (friction, sensor noise, the messy world). **[Established]**
- **Reward hacking is the default, not the exception.** Expect the agent to find the loophole. Specifying reward correctly is genuinely hard.
- **Brittle and unstable to train** — small changes in reward or hyperparameters can swing results wildly. The polished demos hide a lot of failed runs.
- **"Agent" is also a marketing word.** A reliable multi-step autonomous agent is much harder than a flashy demo; today's agents are powerful but error-compounding. Judge reliability, not the highlight reel.

## How a director uses this
- **Designing the reward *is* designing the product — and the safety case.** It's the highest-leverage and highest-risk decision in any RL system. Ask first: *what exactly am I rewarding, and how will it be gamed?* (Expect gaming; the [0900](../10-minds/0900_evolution-and-general-intelligence.md) analogy is not theoretical.)
- **Prefer abundant cheap trials.** RL shines where you have a fast, faithful simulator (games, code, markets). Be very skeptical of plans that need millions of *real-world* trials.
- **Watch the autonomy line.** The jump from a model that *answers* to an agent that *acts* (spends money, sends emails, runs code) raises both capability and stakes sharply — gate it with oversight, sandboxes, and human-in-the-loop. This is a director's call, not an engineer's.
- **What you delegate:** the algorithm (PPO, etc.), the network, the training infrastructure. **What you own:** the reward specification, the choice of where autonomy is allowed, the evaluation for reward-hacking, and the deployment safety case.

## Connections
- **Stands on:** [0250 Feedback & control](../00-foundations/0250_feedback-loops-and-control.md) (the agent–environment loop *is* control), [1000](1000_machine-learning-from-examples.md)/[1100](1100_neural-networks-deep-learning.md) (the model and gradient machinery deep RL uses), [0800 Child mind](../10-minds/0800_child-mind-bootstraps.md) (acting/curiosity to learn), [0900 Evolution](../10-minds/0900_evolution-and-general-intelligence.md) (reward hacking = the mesa/Goodhart story; self-play ≈ population search).
- **Leads to:** RLHF and LLM agents ([1300](1300_language-models-how-llms-work.md)), robotics & embodiment ([1800](../60-frontier/)), world models and paths to AGI ([1800](../60-frontier/)), and the alignment of goal-seeking systems ([1900](../60-frontier/)).
- **Contested?** The RL framework, exploration/exploitation, credit assignment, the deep-RL results — **[Established]**. World-models-as-the-path and "autonomous agents are imminent/safe" — **[Likely → Contested]**.

## Proof-of-learning *(do one, from memory)*
1. Define **agent, environment, state, action, reward, policy** — then say what "maximize the **return**" adds beyond "maximize reward."
2. Explain **exploration vs exploitation** with one everyday example, and why pure exploitation fails.
3. Tell the boat-race (reward-hacking) story and connect it to the inner/outer alignment idea of [0900](../10-minds/0900_evolution-and-general-intelligence.md). Why does it make reward design a *safety* decision?
4. Why is RL so **sample-inefficient**, and what does **model-based** RL (a world model) do to fix it?

## Revision notes
*Newest first — read only what moved.*
- `rev 1 (2026-06-27)` — created. *(LLM-agent frontier is a fast-moving 2026 snapshot — re-check specifics.)*

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md). Next, the chapter's payoff: how large language models actually work ([1300](1300_language-models-how-llms-work.md)) — where prediction, the transformer, and RLHF all meet.*
