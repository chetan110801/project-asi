# CONCEPT REGISTRY — one home per concept
**The no-redundancy enforcer.** Before explaining *anything*, check here. If a concept is listed, **link to its home — don't re-explain**. If it's not, explain it once in the right module, then add it here.

`Status: Living index · System Version: 3.0 · Last updated: 2026-07-16 (AP7 rung added to visible ladder — neurosymbolic / hybrid AI; AP3 added 2026-07-15)`

> Status legend: ✅ = home exists · 🔜 = home planned (queued in [`_QUEUE.md`](_QUEUE.md)/[CURRICULUM](CURRICULUM.md)); a 🔜 concept was *seeded* (briefly introduced, not fully explained) at the module noted, and its full pre-split explanation survives in that module's git history.

> Rule (from [`../INSTRUCTIONS/LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §5): every concept has exactly **one canonical module**, which lives in one **domain folder**. This table maps **concept → home module (`id` + folder) → one-line pointer**. It does *not* hold the explanation itself (that would be repetition) — it points to it. (Folders for planned modules: see [`00_MAP.md`](00_MAP.md).)

---

## ★ The visible ladder (v3.0) — link THESE from new pages

> These are the **only pages visible in the reader** — the new "approaches to AGI" learning ladder, in order. When a new page needs one of these ideas, give a one-line refresher and link its home here. **Everything in the big "legacy" table below now lives in `LEARNING/_legacy/` (hidden 2026-07-14) — kept as a record; do NOT link legacy files from visible pages.**

| Concept | Home (`id` → file) | One-line pointer |
|---|---|---|
| language model / guessing the next word | `c-next-word` → [next-word](10-how-ai-works-today/01_guessing-the-next-word.md) | Guesses the next word, giving odds to every word; writes by looping. |
| self-supervision (data teaches itself) | `c-next-word` → [next-word](10-how-ai-works-today/01_guessing-the-next-word.md) | The next word is its own answer key → the whole internet can teach it. |
| prediction ≈ compression | `c-next-word` → [next-word](10-how-ai-works-today/01_guessing-the-next-word.md) | No room to memorise → forced to keep patterns; some say that ≈ understanding. |
| autoregressive (guess, add, repeat) | `c-next-word` → [next-word](10-how-ai-works-today/01_guessing-the-next-word.md) | Writes one word at a time; its own words feed back in. |
| the "mistake-count" (loss) | `c-next-word` → [next-word](10-how-ai-works-today/01_guessing-the-next-word.md) intro; used in [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md) | How wrong the next-word guess is; training drives it down. |
| scaling laws (the steady line) | `c-scaling-laws` → [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md) | Bigger → mistakes fall in a steady, predictable line. |
| compute-optimal / Chinchilla | `c-scaling-laws` → [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md) | For a set budget, a *right shape* — grow size & text together (now running-cost aware). |
| the data wall | `c-scaling-laws` → [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md) | Good human text is finite — "we have but one internet." |
| emergent abilities + the "mirage" | `c-scaling-laws` → [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md) | Skills that seem to switch on at size — real, or a scoring trick? (open) |
| the "make it bigger" bet / scale hypothesis | `c-ap1-scale` → [AP1](20-the-approaches/01_ap1-scale-and-foundation-models.md) | One simple job + huge scale → skills appear on their own. |
| the Bitter Lesson (Sutton) | `c-ap1-scale` → [AP1](20-the-approaches/01_ap1-scale-and-foundation-models.md) | Methods that use more compute beat hand-built human knowledge. |
| foundation model | `c-ap1-scale` → [AP1](20-the-approaches/01_ap1-scale-and-foundation-models.md) | One big pretrained machine everything else is built on. |
| scaling-suffices debate | `c-ap1-scale` → [AP1](20-the-approaches/01_ap1-scale-and-foundation-models.md) | Is scale alone enough for AGI, or is a second idea needed? |
| the "think longer" bet / test-time compute | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Spend computer power *at answer-time*, not just training-time. |
| chain-of-thought (show the steps) | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Write in-between steps → more compute per hard problem → better answers. |
| fast vs slow thinking (in AI) | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Snap one-pass answer vs step-by-step working-out. |
| reasoning-via-RL / verifiable rewards | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Reward only correct checkable answers → good reasoning emerges (DeepSeek-R1). *(Deep RL home = [AP4](20-the-approaches/04_ap4-rl-from-interaction.md).)* |
| reinforcement learning (reward learning) — minimal taste | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) intro | Try → get a score → shift toward what scored well. *(One-line version only; full frame → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md).)* |
| self-play / AlphaZero (durable ancestor) | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Learn a skill from reward + search + self-tries, no human examples. *(Self-play **at scale** → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md).)* |
| reasoning-generalization debate | `c-ap2-reasoning` → [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) | Does learned reasoning transfer past checkable problems, or just sharpen the base model? (open) |
| reinforcement learning (the full frame) | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Agent in a world: state → action → reward → repeat; learn by trial and error, no human answers. *(The deep home; AP2 gave the taste.)* |
| reward · return · policy · value | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Reward = score to maximize; return = its long-run total; policy = the strategy; value = expected future return. |
| explore vs exploit · credit assignment | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Use-what-works vs try-new; and which past action earned a late, sparse reward. |
| the reward hypothesis | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Any goal = "maximize one scalar score, summed over time" (Sutton & Barto). |
| "reward is enough" (the bet) | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Intelligence + all its abilities emerge from maximizing reward in a rich world (Silver et al. 2021). |
| self-play at scale (DQN / Dota) | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Superhuman skill grown from zero on its own experience — Atari pixels, OpenAI Five. |
| reward specification / reward hacking | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | A maximizer chases the number, not your intent; Goodhart made live and dangerous. |
| sample-inefficiency (RL) | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | RL needs a fortune of tries — fine in a simulator, brutal in the slow real world. |
| era of experience / grounded rewards | `c-ap4-rl` → [AP4](20-the-approaches/04_ap4-rl-from-interaction.md) | Learn from your own life, not our text; reward from world signals — answers the data wall (Silver & Sutton 2025). |
| world model (predict consequences, then plan) | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | An inner copy of how the world changes: state + action → next state; plan by imagining outcomes and picking the best (LeCun). |
| JEPA / predict the abstract summary, not pixels | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | Joint Embedding Predictive Architecture — throw away unpredictable noise (the "windy leaves"), predict only what matters. |
| generative vs non-generative prediction | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | Draw every pixel of the future (failed 10 yrs) vs predict an abstract representation of it (JEPA's bet). |
| objective-driven AI / planning by optimization | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | Think/plan before you speak; model predictive control — imagine actions, predict, score, pick best (rockets since the '60s). |
| the sensory-bandwidth argument | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | A 4-year-old's eyes take in ~50× more than all internet text; most world-knowledge is watched, not read (LeCun). |
| autoregressive drift (exponential error) | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | Word-by-word output has a rising chance of wandering off the correct path — the longer it talks, the faster (LeCun). |
| hierarchical planning (open problem) | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | Plans built in layers (goal → sub-goals → muscle) — "nobody knows how to do this in AI" (LeCun). |
| the world-models race (SOTA snapshot) | `c-ap5-world-models` → [AP5](20-the-approaches/05_ap5-world-models-jepa.md) | 2025–26 surge: V-JEPA 2, DreamerV3 (Nature), AMI Labs ($1.03B), Genie 3, World Labs/Marble — dated, ages fast. |
| skill vs intelligence | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Stored, fetchable competence (skill) is *not* the power to handle the truly new (intelligence) — Chollet. *(AP1 only touched this line.)* |
| measure of intelligence / skill-acquisition efficiency | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Intelligence = how fast/cheaply you master a *novel* task from little data, not how much skill you already have (Chollet 2019). |
| ARC / ARC-AGI (the test) | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Little puzzles built to resist memorising — each novel, needs only a child's *core knowledge*. *(o3/test-time-compute number lives at [AP2](20-the-approaches/02_ap2-reasoning-and-test-time-compute.md).)* |
| core knowledge (priors) | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | The few basics every 4-year-old has: objectness, counting, elementary physics — all ARC assumes. |
| program fetching vs synthesis | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Pull a stored recipe (fetch) vs build a new one on the fly for a problem you have no recipe for (synthesis). |
| program synthesis / discrete program search | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Search a small toolbox (DSL) for a program that fits the examples; data-thrifty (learns from 1–2) but compute-heavy (combinatorial explosion). |
| deep learning + program search (the merger) | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Curve-fitting intuition (System 1) *guides* the program search (System 2) — cut the explosion; Chollet's proposed road. |
| active inference / test-time training | `c-ap8-program-synthesis` → [AP8](20-the-approaches/08_ap8-program-synthesis-arc.md) | Let the model learn a little from the specific task before answering — a form of program synthesis; what unlocks ARC scores. |
| the common cortical algorithm (Mountcastle) | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | The neocortex is *one* circuit copied ~150,000 times — vision, language, maths all run the same recipe; so AGI is one problem, not a thousand. |
| cortical column | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | The ~1mm repeated unit of the neocortex (~150,000 in a human) — Mountcastle's "unit of intelligence." |
| reference frames (grid/place cells) | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | Map-like coordinate frames the brain uses for space *and* (Hawkins' leap) for objects, the body, and abstract ideas; knowledge is stored *in* them. |
| the Thousand Brains Theory / cortical voting | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | Not one model of a thing but thousands of complementary models across columns, that *vote* to one perception (Hawkins). |
| the predictive brain | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | Each column predicts its next input with every movement; prediction tests and updates the model. *(Cousin of AP5's world model.)* |
| four attributes of an intelligent machine | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | Hawkins' AGI baseline: continuous learning · learning via movement · many models voting · reference frames. |
| neuromorphic computing | `c-ap6-brain-based` → [AP6](20-the-approaches/06_ap6-brain-based.md) | Brain-style chips (Intel Loihi, IBM NorthPole) — many small spiking units; far lower power on narrow tasks (dated snapshot). |
| the "agent" idea / cognitive architecture | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | A mind is a *system of parts* — wrap a reasoning model in memory + tools + planning + a loop; the old "design a mind's parts" idea (SOAR/ACT-R) with a working brain inside. |
| the agent loop / reason + act (ReAct) | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Think → act (use a tool) → see the result → think again; letting it *act* and check reality cuts hallucination. |
| tool use | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Let the model call outside things — search, a code-runner, a browser — to reach past its own head. |
| agent memory + reflection (Reflexion) | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Store what happened; write plain-word lessons from mistakes → learn from experience without retraining. |
| memory→reflection→planning architecture (Generative Agents) | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Store experiences → synthesize higher-level reflections → retrieve → plan. A cognitive architecture built from an LLM. |
| skill library / lifelong agent (Voyager) | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Save each new ability as reusable code; skills compound and dodge catastrophic forgetting. |
| multi-agent systems | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Many agents as a team / "AI firm" — exciting but unproven; still single-agent (2026, Karpathy). |
| the march of nines / compounding errors | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Small per-step errors multiply over a long job; each extra nine (90→99→99.9%) costs the same work (Karpathy). |
| scaffolding-vs-model debate | `c-ap3-agents` → [AP3](20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) | Is agent structure a real road to AGI, or a temporary *app layer* the next model absorbs? (open) |
| neurosymbolic / hybrid AI (the bet) | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Join a neural *learner* (flexible, learns from data) to a symbolic *reasoner* (exact rules) — keep both, so the whole learns *and* reasons reliably (Marcus, Lamb). |
| symbol / symbol-manipulation | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | A stand-in token handled by exact rules that hold in *every* case (like *x, y* in algebra); "operations over variables." |
| connectionism vs symbolic AI (GOFAI) | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Learn-by-tuning-connections (neural) vs hand-written rules & logic (old "Good Old-Fashioned AI") — the two camps AP7 rejoins (entangled since McCulloch–Pitts 1943). |
| systematicity / compositional generalization | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Grasp the parts + the rule for combining them → understand new combinations for free ("John loves Mary" → "Mary loves John"); Fodor & Pylyshyn 1988, still open in 2025. |
| robust AI + the four-step program | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Marcus's goal: dependable, systematic, *transfers* across contexts like an adult; built via hybrid → knowledge → reasoning → cognitive models. |
| the integration problem | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Smooth, differentiable learner vs jagged, discrete rules — no gradient flows through logic, so joining them without killing learning is unsolved (in general). |
| AlphaGeometry / neural guides symbolic | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Neural half *guesses* the useful construction; symbolic engine *proves* it — 25/30 Olympiad geometry ≈ gold medalist (2024, dated); the join realized. |
| de-facto neurosymbolic (LLM + tools) | `c-ap7-neurosymbolic` → [AP7](20-the-approaches/07_ap7-neurosymbolic-and-hybrid-ai.md) | Reliable 2026 systems call a calculator / code / theorem-prover / database — neural proposes, symbolic tool checks; winning, or too loose to be a distinct bet? (open) |

---

## Legacy homes (now in `LEARNING/_legacy/`, hidden — reference only, do not link)

| Concept | Canonical home (`id` → file) | Status | One-line pointer |
|---|---|---|---|
| intelligence (working definition) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Doing the *right thing* across many situations to reach goals. |
| generality (general vs narrow) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Many problem types vs one; the core of "G" in AGI. |
| "AGI is many forms" (flight analogy) | `c-intelligence` → [0100](00-foundations/0100_what-is-intelligence.md) | ✅ | Probably a family of forms, not one finish line. |
| system | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Parts + relationships that produce behavior. |
| emergence (general) | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | The whole does what no part can (e.g. intelligence). *(LLM "emergent abilities" now in the visible ladder → [scaling](10-how-ai-works-today/02_scaling-laws-and-emergence.md).)* |
| reductionism vs holism | `c-system` → [0200](00-foundations/0200_what-is-a-system.md) | ✅ | Zoom-in to fix parts; zoom-out to see behavior. |
| feedback loop | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Output looping back to change input. |
| negative / positive feedback | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Balancing → stability; reinforcing → runaway. |
| control (setpoint / error) | `c-feedback` → [0250](00-foundations/0250_feedback-loops-and-control.md) | ✅ | Goal → measure → correct → repeat. |
| entropy / information / bit | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Surprise, measured; the unit is the bit. |
| compression (≈ understanding) | `c-entropy` → [0300](00-foundations/0300_information-and-entropy.md) | ✅ | Predict well → remove entropy → compress. |
| vector / embedding | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | A point in a space of meaning; nearness = similarity. |
| matrix (as transformation) | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | An action that moves a whole space at once. |
| dot product / similarity | `c-linear-algebra` → [0350](30-math-and-theory/0350_just-enough-linear-algebra.md) | ✅ | Alignment of two vectors; the engine of retrieval/attention. |
| computation | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | What a machine can mechanically do. |
| universality / stored-program | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | One machine runs any program; a program is just data. |
| algorithm / complexity | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | A recipe; how its cost grows (cheap vs explosive). |
| uncomputability / hard limits | `c-computation` → [0400](00-foundations/0400_computation.md) | ✅ | Some problems no machine can ever solve. |
| probability / uncertainty | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Reasoning with what we don't fully know. |
| conditional probability | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | P(A given B) — odds after evidence. |
| Bayes' rule / base rate | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Update belief = prior × likelihood; mind the base rate. |
| expected value | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | Probability-weighted average; how to decide under risk. |
| distribution / fat tails | `c-probability` → [0500](00-foundations/0500_probability-and-uncertainty.md) | ✅ | The full spread; rare extremes can dominate. |
| learning (in a system) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Improving from experience by an error-reducing loop. |
| generalization vs overfitting | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Transfer to unseen cases vs memorizing the training set. |
| supervised / unsupervised / RL / self-supervised | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Four flavors = same loop, different feedback. |
| inductive bias / no free lunch | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | Can't learn without assumptions; none is best at everything. |
| objective function (Goodhart) | `c-learning` → [0600](00-foundations/0600_what-it-means-to-learn.md) | ✅ | The system gets what you measure, not what you meant. |
| neuron / synapse / plasticity | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Sum-and-fire units; learning = connections rewiring. |
| biological neural network | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Mind emerges from billions of wired neurons (inspired ANNs). |
| predictive brain | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | Brain predicts input, learns from prediction error. |
| brain efficiency / embodiment | `c-brain` → [0700](10-minds/0700_the-brain-working-model.md) | ✅ | ~20 watts; evolved to run a body — where AI still lags. |
| developmental bootstrapping | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | General intelligence grown from little data + interaction. |
| core-knowledge priors | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Built-in expectations (physics, agents, number) = inductive bias. |
| sample efficiency | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learning a lot from little — the human-vs-AI gap. |
| curiosity / intrinsic motivation | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learning driven from inside, no external reward. |
| active / causal learning | `c-development` → [0800](10-minds/0800_child-mind-bootstraps.md) | ✅ | Learn cause→effect by intervening, not just watching. |
| evolution (variation-selection-heredity) | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Design without a designer; the one recipe that made minds. |
| evolutionary optimization | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Gradient-free, population-based search (genetic algorithms). |
| inner/outer alignment (mesa-optimization) | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | An optimizer can produce an agent with divergent proxy goals. |
| cumulative culture | `c-evolution` → [0900](10-minds/0900_evolution-and-general-intelligence.md) | ✅ | Knowledge ratcheting across generations = the human superpower. |
| model / parameters (weights) | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | A function with tunable knobs; learning = setting the knobs. |
| training vs inference | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Tuning the knobs on data vs using the finished model. |
| features / feature engineering | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | The input numbers a model sees; hand-crafted then learned ([1100](20-machine-intelligence/1100_neural-networks-deep-learning.md)). |
| loss function | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | One number = how wrong; the objective ([0600](00-foundations/0600_what-it-means-to-learn.md)) made concrete. |
| gradient descent / learning rate | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Roll downhill on the error; the error-reducing loop on numbers. |
| train / validation / test split | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Tune knobs / tune choices / score once — honest held-out test. |
| bias–variance trade-off | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Underfit (too rigid) vs overfit (fits noise), operationalized. |
| hyperparameters | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Settings you choose (vs parameters the optimizer learns). |
| classical ML (trees/SVM/boosting) | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Non-deep methods; still win on tabular data. |
| data leakage | `c-machine-learning` → [1000](20-machine-intelligence/1000_machine-learning-from-examples.md) | ✅ | Answer-clue sneaks into features → fake-great scores. |
| artificial neuron / activation function | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Weighted sum + a non-linear bend; the unit of a net. |
| layers / depth / deep learning | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Stacked matrix-multiply+activation; "deep" = many layers. |
| representation / feature learning | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | The net invents its own features (edges→objects). The revolution. |
| backpropagation | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Push error backward to assign each weight its blame. |
| CNN / RNN / LSTM | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Architectures = baked-in inductive bias (vision / sequence). |
| embedding / latent space | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Learned internal vectors = meaning (uses [0350](30-math-and-theory/0350_just-enough-linear-algebra.md)). |
| universal approximation | `c-neural-networks` → [1100](20-machine-intelligence/1100_neural-networks-deep-learning.md) | ✅ | Can represent ~anything — but representable ≠ learnable. |
| agent / environment / state / action / reward / policy | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | The RL vocabulary; the control loop with a learned controller. |
| value function / return | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Long-run reward (foresight), not the next treat. |
| exploration vs exploitation | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Try new vs cash in what works; the bandit dilemma. |
| temporal credit assignment | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Which past action earned a delayed reward? |
| reward shaping / reward hacking | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Agent games the proxy reward (Goodhart/mesa, made live). |
| model-free vs model-based / world model | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Trial-and-error vs learn a world model and plan in it. |
| deep RL / self-play | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | RL + nets (DQN, AlphaZero); play copies of yourself. |
| AI agents (LLM agents) | `c-reinforcement-learning` → [1200](20-machine-intelligence/1200_reinforcement-learning-and-agents.md) | ✅ | Goal-directed act-loop; the 2025–26 LLM-agent frontier. |
| language model / next-token prediction / LLM | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md) | ✅ | A machine that assigns a probability to every possible next token; run in a loop, it writes. |
| autoregressive (causal) generation | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md) | ✅ | Predict, append, repeat — conditioning on its own outputs; one token at a time. |
| self-supervised pretraining (the idea) | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md) | ✅ | The next word is the label — the internet becomes a free teacher. *(Mechanics at scale → planned `1320`.)* |
| perplexity / LM cross-entropy loss | `c-language-models` → [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md) | ✅ | Punished by its surprise at the true next word; perplexity ≈ effective number of choices. |
| token / tokenization | planned `1305` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | Sub-word units the model reads/writes in. *(Seeded at [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md); rev-1 text in its git history.)* |
| transformer / attention | planned `1310` rewrite ([CURRICULUM](CURRICULUM.md) A3.4; un-wired demo exists) | 🔜 | Each token looks back at the relevant ones (dot-product similarity). |
| context window | planned `1355` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | The model's working memory; outside it is forgotten. |
| pretraining → fine-tuning → RLHF (three stages) | planned `1320`/`1330`/`1335` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | Raw predictor → instruction-follower → aligned assistant. |
| in-context learning / prompting | planned `1325`/`1328` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | Learn a task from prompt examples, no weight change. *(Seeded at [1300](20-machine-intelligence/1300_language-models-the-next-token-idea.md), GPT-3 section.)* |
| chain-of-thought / test-time compute | planned `1338` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | "Think step by step" / spend compute to reason = AI's slow mode. |
| hallucination (confabulation) | planned `1342` ([CURRICULUM](CURRICULUM.md) A3.4) | 🔜 | Fluent, confident, false — intrinsic to a plausibility predictor. |

---

## How to use this table
- **Writing a new module?** For each idea you mention, find its row. Listed → write *"(see [home])"*. Missing → this idea needs a home; either it belongs in the module you're writing (add the row, pointing here) or it needs its own module (insert one — [`LEARNING_ARCHITECTURE.md`](../INSTRUCTIONS/LEARNING_ARCHITECTURE.md) §8).
- **`id` is stable** even if the file is renumbered, so these pointers survive reordering.
- Rows are added the moment a concept gets its canonical explanation — never before (no empty promises), but planned homes may be pre-listed as ⬜ to reserve the slot.
