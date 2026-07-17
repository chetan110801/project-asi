---
id: c-ap5-world-models
sortkey: 2005
title: AP5 · World models / JEPA — the "learn how the world works, then plan" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap4-rl]
provides: [world-model, jepa, generative-vs-nongenerative-prediction, objective-driven-ai, planning-by-optimization, sensory-bandwidth-argument, autoregressive-drift, hierarchical-planning, world-models-race]
resources: []
status: ready
reading_time: 34 min
rev: 1
created: 2026-07-14
updated: 2026-07-14
---

# AP5 · World models / JEPA — the "learn how the world works, then plan" bet

*This is the fifth big idea for how to build a machine that can think in a general way. The four ideas before it all start from the same place: **human text.** They copy it (AP1), think harder over it (AP2), wrap it in a loop (AP3), or learn from reward (AP4). This one says something sharper: **text is the wrong food.** A machine that only reads words will never really understand the world, because most of what there is to know about the world is not written down anywhere — it is seen, touched, and lived. So this bet says: **stop feeding the machine our words. Let it watch the world (mostly video), build its own inner model of how the world works, and then use that model to plan** — to imagine "if I do this, what happens next?" before it acts. The idea has a champion, Yann LeCun, and a specific shape called **JEPA**. This page explains it from zero: the bet in one minute, what a "world model" really is, the clever trick at its heart, why serious people believe it — and the four places it is stuck.*

> **You are here:** this is the **AP5** page — the fifth of the "approaches to AGI" (see the map, [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)). AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. The short name for this idea is **world models** — a machine that learns an inner model of how the world works and plans against it. Its most specific form is **JEPA** — *Joint Embedding Predictive Architecture* — LeCun's particular design (the long name is unpacked slowly below; do not worry about it yet).
>
> **This page builds on four earlier rungs of the ladder**, all short and plain: [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — how today's AI works; [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — why the field is running low on human text; [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — the bet this one argues *against*; and [AP4 · RL from interaction](04_ap4-rl-from-interaction.md) — which ended by pointing straight here. A one-line reminder of each is given where it is used, so you will not get lost. **AP5 is the deep home for the idea of a *world model*** — the thing AP4 said would ease its biggest problem.
>
> **Where the facts come from:** the long 2024 conversation between Lex Fridman and **Yann LeCun** (Meta's chief AI scientist at the time; one of the three "godfathers of deep learning") — the fullest plain-spoken version of this bet on record. Quotes from it are exact. The durable older root is **David Ha & Jürgen Schmidhuber, *"World Models"* (2018)**. Fresh check of the field, done on the web (**as of July 2026**): Meta's V-JEPA 2 (2025); LeCun leaving Meta to start a world-model company (AMI Labs, 2026); Google DeepMind's Genie 3; Fei-Fei Li's World Labs and Marble; and DreamerV3's 2025 *Nature* result. Each fast-moving fact is dated below.

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**A machine that only ever reads text is like a person who has read every book about swimming but has never been in water. It can *say* all the right words, but it does not really know how the world behaves. The fix, this bet says, is to let the machine *watch the world* — mostly video — and build an inner "world model": a private, working copy of how things move, fall, bump, and change. Once it has that model, it can do the thing text machines cannot — *plan*. It can imagine "if I take this action, here is what happens next," try that out in its head across many possible actions, and pick the one that reaches its goal. Intelligence, on this view, is not fluent talk. It is having a good enough model of the world to plan inside.**

Why believe a *model of the world* is the missing piece? Because every animal has one and no animal needs language for it. A house cat has never read a word, yet it understands the physical world — gravity, distance, what will fall if it pushes it — far better than the best text machine. It plans complex jumps and predicts the results of its actions. That understanding did not come from words. It came from *watching and doing.* AP5's bet is that this — not more text — is the road to a real mind.

That is the bet. The rest of this page explains **what a world model is**, **the clever trick (JEPA) that makes it work**, **why serious people back it**, and **why it might still be wrong.**

---

## First, a one-line reminder of the base

Three quick reminders from the rungs below, so this page stands on its own.

- From [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) and [AP1](01_ap1-scale-and-foundation-models.md): **today's main AI is a text machine.** It is trained to guess the next word in billions of pages of human writing, and it writes by looping that guess — pick a word, add it, guess again. Its whole world is *our words.* *(New to you? Read those two first; they are short.)*
- From [the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): there is only so much good human text, and the field is **running out of it** — the "data wall." So the plan "just feed it more of our writing" is hitting a hard limit.
- From [AP4, the ending](04_ap4-rl-from-interaction.md): reward-learning works, but it needs a *huge* number of real tries to learn anything — the **sample-inefficiency** problem *(needing a fortune of attempts to learn a little)*. AP4 ended by saying there might be a way around this: if the machine had **a model of the world, it could do its trying *inside the model* — in imagination — instead of paying for real attempts.** That model is exactly what this page is about.

Now the one new idea this page adds. AP1, AP2, and AP4 all still argue about *what to do with text and reward.* AP5 steps back and attacks the food itself: **words are a thin, late, second-hand description of a world the machine has never seen.** Fix that — give the machine the world directly, through the senses — and let it build a model good enough to plan with. To see why this is a serious idea and not just a slogan, we have to understand three things in order: **why text is not enough, what a "world model" actually is, and the trick that makes learning one possible.**

---

## Part 1 — why a text-only machine is not enough

LeCun's starting complaint is blunt: a text machine is missing the basic equipment of a mind. He lists what it lacks:

> "the capacity to understand the world, understand the physical world, the ability to remember and retrieve things, persistent memory, the ability to reason, and the ability to plan. Those are four essential characteristics of intelligent systems or entities, humans, animals. LLMs can do none of those or they can only do them in a very primitive way …"
> *(Yann LeCun, in conversation with Lex Fridman, 2024)*

("LLMs" = large language models, the text machines of [AP1](01_ap1-scale-and-foundation-models.md). "Persistent memory" = memory that lasts and can be looked up later.) Two of those four — **understand the physical world** and **plan** — are the heart of AP5. Why does he think text can never give them? Two reasons, and both are worth going slowly.

### Reason 1 — text is a tiny trickle of information next to the senses

This is the argument that surprises people most. It sounds like text machines are trained on an *enormous* amount of data — the whole internet. And they are. But compare it to what a small child takes in. LeCun does the arithmetic:

> "through sensory input, we see a lot more information than we do through language, and … most of what we learn and most of our knowledge is through our observation and interaction with the real world, not through language. Everything that we learn in the first few years of life, and certainly everything that animals learn has nothing to do with language."
> *(LeCun, 2024)*

("Sensory input" = what comes in through the eyes, ears, skin — the senses.) The numbers behind it: all the text on the internet is about twenty trillion bytes *(a byte = one small unit of computer data; twenty trillion = 2 followed by 13 zeros)* — so much that it would take a person **170,000 years** to read it at eight hours a day. Yet the eyes of a **four-year-old** have already sent the brain roughly **a thousand trillion bytes** *(a 1 followed by 15 zeros — about fifty times more than all that text)*, in just four years. **A four-year-old has already "seen" about fifty times more of the world than the biggest text machine has ever read.** And the child got the *real* world — moving, three-dimensional, with cause and effect — not a written description of it. This is the **sensory-bandwidth argument** *("bandwidth" = how much information flows through per second; the senses have a far bigger pipe than language)*: the richest source of knowledge about the world is not text at all — it is watching the world go by.

*(Why this example matters:* it turns the usual story on its head. We assume the internet is a giant pile of knowledge and a child knows almost nothing. On raw information about *how the physical world works*, it is the other way round.)

### Reason 2 — writing word-by-word drifts off course, and the drift grows fast

There is a second, deeper problem, buried in *how* a text machine produces its answer. Recall from [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) that it works one word at a time: it picks a word, adds it to what it has written, and feeds the whole thing back in to pick the next word. This is called **autoregressive** generation *(auto = self; regressive = feeding back — it keeps feeding its own output back into itself)*. LeCun's worry is what happens to errors along the way:

> "every time you produce a token, the probability that you stay within the set of correct answer decreases and it decreases exponentially."
> *(LeCun, 2024)*

("Token" = a word or word-piece, the unit the machine writes in. "Exponentially" = not steadily, but faster and faster — like doubling, so it runs away quickly.) Read it slowly. Each word the machine adds has some small chance of being a wrong turn — a word that nudges the answer off the path of sensible answers. And once it is off the path, the next word is chosen *based on that mistake*, so the machine drifts further. LeCun's claim is that the chance of staying on the correct path does not fall gently — it falls **exponentially** with the length of the answer. **The longer the machine talks, the faster it tends to wander into nonsense.** *(This is why long, multi-step answers from a text machine so often start well and slowly go wrong.)*

The two reasons point the same way. Reason 1 says the machine never got the world; Reason 2 says the way it speaks has no plan holding it on course. What is missing in both is the same thing: **an inner model of the world, and a plan made against it, *before* the words come out.** So — what is that?

---

## Part 2 — what a "world model" actually is

Here is the central idea of AP5. Take it one small piece at a time.

**A world model is an inner copy of how the world behaves.** Not a copy of how the world *looks* right now — a copy of how it *changes.* LeCun defines it in two parts:

> "building world models means observing the world and understanding why the world is evolving the way it is, and then the extra component of a world model is something that can predict how the world is going to evolve as a consequence of an action you might take."
> *(LeCun, 2024)*

("Evolving" = changing over time.) So a world model does two jobs: it **watches** the world and works out the rules of how it changes, and — the key part — it can **predict the next state of the world if you take an action.** In the plainest form:

> **Here is the state of the world now. Here is an action I might take. What is the state of the world *after*?**

That is the whole engine. *(A quick word: **state** = "everything that matters about the situation right now" — the same word AP4 used for the RL loop. You met it in [AP4](04_ap4-rl-from-interaction.md); here it means the same thing, the current situation the model works from.)* You have this engine in your own head. Open your hand holding a cup, and you *know* it will fall — you did not have to drop it to find out. Push a heavy table and you know it will barely move. That knowing-in-advance is a world model at work.

### Why a world model is the thing that lets you *plan*

Once a machine can predict "action → next state," something new becomes possible that a text machine simply cannot do: **planning.** Here is how planning falls out of a world model:

> "if you have this world model, we can imagine a sequence of actions, predict what the outcome of the sequence of action is going to be, measure to what extent the final state satisfies a particular objective … and then plan a sequence of actions that will minimize this objective, at runtime."
> *(LeCun, 2024)*

("Objective" = the goal, written as something to measure — for example, "distance to where I want the cup to be." "At runtime" = at the moment of acting, not during training.) In plainer words, planning is a loop the machine runs *in its own head*:

1. **Imagine** a possible sequence of actions.
2. Use the world model to **predict** where that sequence ends up.
3. **Score** how close that end-state is to the goal.
4. Try other sequences, and **keep the one that scores best.**
5. *Then* act.

This is old and proven engineering. It has a name — **model predictive control** — and it is exactly how engineers have steered rockets since the 1960s: predict where a sequence of commands takes the rocket, and pick the commands that land it where you want. *(The durable point:* "plan by imagining outcomes and picking the best" is not new or mysterious — the new part is *learning* the world model from raw video instead of hand-writing the physics.) Notice how this answers Part 1's second problem: a planning machine **thinks first and speaks second.** LeCun calls this the blueprint of future systems — machines that "think about their answer, plan their answer by optimization before turning it into text."

So the target is clear: learn a world model from watching, then plan against it. But there is a catch that stopped this idea for years — and beating it is the real heart of AP5.

---

## Part 3 — the trick: don't predict the pixels (this is JEPA)

Here is the wall the field hit. If a world model must predict "what happens next" from video, the obvious way is to make it predict the **next video frame** — every dot of colour on the screen. This is called a **generative** approach *(generative = it generates, or produces, the full detailed output — every pixel)*. People tried it for a decade. It failed. LeCun is direct about it:

> "you take a video, show a system, a piece of video, and then ask you to predict the reminder of the video, basically predict what's going to happen. … You're not going to be able to do this with generative models."
> *(LeCun, 2024)*

*("reminder" is the transcript's spelling of *remainder* — the rest of the video.)* Why does predicting every pixel fail? Because **most of the fine detail of the world is not predictable, and does not matter.** Think of a video of a tree on a windy day. The exact position of every leaf, flickering in the wind, is essentially random. A machine forced to predict every pixel wastes almost all its effort trying to guess the unguessable — the precise wiggle of each leaf — and learns nothing useful. LeCun's fix is the core insight of AP5:

> "In a JEPA, you're not trying to predict all the pixels, you're only trying to predict an abstract representation of the inputs."
> *(LeCun, 2024)*

("Abstract representation" = a stripped-down summary that keeps the *meaning* and drops the exact detail — like "the leaves are rustling" instead of the position of every leaf. "Abstract" here = pulled up to a higher, simpler level.) The machine first passes the video through an **encoder** *(a part that squeezes the raw input down into that summary)*, and predicts the *summary*, not the pixels. LeCun's own words on what the encoder is *for*:

> "what you want is your encoder to basically eliminate all those details … learn an abstract representation of the world where what can be modeled and predicted is preserved and the rest is viewed as noise and eliminated by the encoder."
> *(LeCun, 2024)*

("Noise" = meaningless, unpredictable junk — here, the exact flicker of each leaf.) **That is JEPA in one line: throw away the unpredictable noise, keep only what can be predicted, and predict *that*.** The long name now makes sense — *Joint Embedding Predictive Architecture*: it makes two summaries (*joint embedding* = two matched compressed views, of the "before" and the "after"), and a *predictor* learns to go from one to the other.

*(Why this is deep, not a mere shortcut:* it means the machine is forced to learn the world at the *right level of abstraction* — the level of objects and events, not pixels. That is what a mind does. You do not model your kitchen as a swarm of atoms; you model it as cups, tables, and "if I let go, it falls." JEPA is a bet that a machine must do the same to understand anything.)

The word **non-generative** is worth keeping, because it is the whole fight (Part 4, crack #4). A generative world model *draws you the next frame*; a JEPA world model *understands the next situation without drawing it.* LeCun bets the second is the road to a mind and the first is a costly detour.

> **▶ Go deeper — a deep dive past this card.** This card *names* the JEPA trick — "predict an abstract summary, not the pixels" — but never shows **how you train an encoder to produce a good summary with no teacher, or why that very trick invites a hidden cheat.** That machine is opened in **[AP5 · Deep dive #1: learning without a teacher](../50-deep-dives/05_ap5-deep-dive-learning-without-a-teacher.md):** where the training signal comes from when nobody labels the video (**self-supervised learning** — hide a part, predict it from the rest); the trapdoor under the slogan (**collapse** — the machine cheats by making *every* summary identical, so prediction is perfect and the meaning is zero); the **three ways the field beats collapse** (push rivals apart · a spread-out rule · the slow-self-copy trick real JEPAs use); the real lineage **I-JEPA → V-JEPA → V-JEPA 2 → V-JEPA 2-AC** — ending in a **latent** world model that plans a real robot, zero-shot, with **no reward** (this card's bet standing up); and the bigger **energy-based / objective-driven-AI** blueprint where the JEPA is just one module (and where the **hierarchical planning** of Stuck #3 gets its proposed answer, **H-JEPA**). Optional — read it when you want the machinery beneath "predict the summary."

---

## Why this is a serious idea, not one man's hunch

Three legs hold it up.

### Leg 1 — every animal is living proof

The strongest everyday evidence is that **minds without language already work this way.** A cat, a dog, a one-year-old baby — none has language, yet each understands the physical world and plans in it:

> "we're not going to get to the level of even the intelligence or level of understanding of the world of a cat or a dog, which doesn't have language. They don't have language and they understand the world much better than any LLM. They can plan really complex actions and imagine the result of a bunch of actions."
> *(LeCun, 2024)*

Read what that claims: the ability to *imagine the result of an action* — the world model — came first in the history of life, long before words. Babies learn gravity, that objects still exist when hidden, and the difference between a living thing and a dead one, mostly by **watching**, in the first months, before they can act on the world at all. If the deepest layer of intelligence was built by watching and never needed language, then a machine that only reads may be missing the real foundation. **[Established as an observation about animals and babies; that it *proves* the machine route works is the open bet.]**

### Leg 2 — small world models already work

This is not only philosophy; working systems exist. Three landmarks, each grounded.

**Learning inside a dream (Ha & Schmidhuber, 2018).** The durable root of the idea. These researchers first trained a small **world model** of a simple game, and then did something striking: they trained the game-playing agent **entirely inside the model's imagination** — inside a dream — and the skill still worked when the agent was moved back to the real game. Their own words: they trained

> "our agent entirely inside of its own hallucinated dream generated by its world model"
> *(David Ha & Jürgen Schmidhuber, "World Models," 2018)*

("Hallucinated" here = made-up by the model, not real — the agent practised in a world its own model invented.) This is exactly AP4's escape route made real: **practise in imagination, for free, instead of paying for real tries.** It is the clearest early proof that a learned world model is good enough to plan and learn inside.

**Diamonds in Minecraft, from scratch (DreamerV3, published in *Nature*, 2025).** A direct descendant. DreamerV3 learns a world model of its surroundings and "imagines" future outcomes to improve — and, using one single setup across 150-plus different tasks, it became **the first system to find diamonds in the game Minecraft from scratch, with no human examples** *(as of the 2025 Nature paper)*. Finding diamonds is a long, many-step goal that had resisted machines for years. It matters here because it is a **world model plus planning** doing what raw reward-learning (AP4) struggled to do — the two approaches working together. **[Established — a peer-reviewed, reproduced result.]**

**Robots that plan from watching video (V-JEPA 2, Meta, June 2025).** LeCun's own line, made real. V-JEPA 2 is a world model trained mostly on **over a million hours of ordinary internet video**, plus a tiny amount — about 62 hours — of real robot data. From that, it can do **zero-shot robot planning** *("zero-shot" = handling a new object or task it was never specifically trained on)* — it plans how to move things it has never seen, by predicting outcomes in its learned abstract space *(as of 2025)*. It is the first sizeable, public JEPA world model doing the exact job the bet promises: watch cheap video, learn how the world moves, then plan. **[Likely / dated — a real 2025 result; whether it scales to general competence is unproven.]**

### Leg 3 — the field just poured in (the "world-models race")

For years this was a contrarian view — LeCun arguing against the whole text-machine mainstream. That changed fast. As of **July 2026**, "world models" is one of the hottest areas in AI, with real money and top names behind it:

- **LeCun left Meta** in **November 2025**, after 12 years as its chief AI scientist, and started a company, **AMI Labs** (*Advanced Machine Intelligence*), to build world models full-time. In **March 2026** it raised **about $1.03 billion** in its first funding round — reported as the largest of its kind ever for a European company — with backers including NVIDIA, Jeff Bezos's fund, and Eric Schmidt. Betting a billion dollars against the text-machine mainstream is a strong signal of how seriously this bet is now taken.
- **Google DeepMind's Genie 3** (announced **August 2025**) generates a full, explorable 3-D world you can walk around inside, in real time, from a text prompt.
- **Fei-Fei Li** — the researcher who built the dataset that started the modern AI boom — launched **World Labs** and its product **Marble** (late 2025), calling the goal *"spatial intelligence."* It raised about **$1 billion** in **February 2026**.

**[Likely / dated — the surge is real; whether it delivers AGI is exactly the open question.]** *(Caution: this heat also brings hype. Some 2026 press claims — for example that reasoning has been "found inside" a given world model — trace to weak sources. Treat those as* open*, not fact. The named results above are the grounded ones.)*

---

## So what does AP5 say intelligence is?

Pulling the legs together, here is AP5's answer to *"what is intelligence?"*:

- **Intelligence is** having **a model of the world good enough to plan with** — not fluent talk, but the ability to imagine "if I do this, what happens?" and choose well.
- **What it learns from** is mostly **sensory experience** — watching the world (video), the way animals and babies do — not human text.
- **Its claim about the missing piece:** what AP1 and AP2 lack is a **grounded model of reality.** They know our *words about* the world; they do not have the world itself. Give a machine the world through the senses, let it learn how the world changes, and let it **plan** against that model — and the understanding text can never supply will finally be there.

That is the bet. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP5 has the deepest diagnosis of what is wrong with today's AI, it matches how real minds (animals, babies) actually formed, it has early working systems, and it has just become one of the field's hottest bets. Hold that. Now the four places it is truly stuck.

### Stuck #1 — it is still largely unproven at real scale

This is the honest heart of it. The generative version of world-from-video **failed for ten years.** The JEPA version is **young** — the first sizeable one (V-JEPA 2) is from 2025. Nobody has yet shown that a JEPA-style world model, scaled up, produces the things that matter most: real reasoning, and the high, language-level abstraction that AP1's text machines *do* have. **The whole bet rests on a promise — "predict abstract representations, not pixels, and understanding will come" — that has been demonstrated only in small and narrow settings.** Text machines went from small demos to astonishing scale in a few years; whether world models make the same jump is unknown. Until they do, AP5 is a very well-argued *hope*, not a proven road. **[Contested — the central open question about AP5.]**

### Stuck #2 — maybe language already contains the world model

This is the strongest push-back, and it is the whole [scaling-suffices debate](01_ap1-scale-and-foundation-models.md) *(the field's central argument: does scale alone get to AGI, or is a second idea needed? — its home is AP1)* pointed straight at AP5. The counter-claim: **a huge pile of text may quietly contain the world model already.** People write about gravity, about cups breaking, about cause and effect — endlessly, between the lines. Feed a machine enough of that, the argument goes, and to predict the words well it is *forced* to build an internal model of the world those words describe. On this view LeCun's "text is too thin" is wrong: text is a compressed shadow of the world, and a big enough machine can reconstruct the world from the shadow. Which side is right is not settled — and it is the exact dividing line between AP1 and AP5. LeCun bets you cannot get a world model from words; the scaling camp bets you already are. **[Contested — the key disagreement in the whole field, still open as of 2026-07.]**

### Stuck #3 — nobody knows how to do hierarchical planning

Even granting the world model, the *planning* part has an unsolved core. Real plans are **hierarchical** *(built in layers — big steps made of smaller steps made of smaller steps)*. To go from New York to Paris you do not plan every muscle twitch; you plan "get to the airport → fly → …" and only fill in the fine movements as you go. Learning to plan across those layers is an open problem, and LeCun says so plainly:

> "nobody really knows how to do this in AI. Nobody knows how to train a system to learn the appropriate multiple levels of representation so that hierarchical planning works."
> *(LeCun, 2024)*

("Levels of representation" = the layers, from the big abstract goal down to the tiny concrete action.) So even the champion admits a key piece is missing. A world model tells you *what happens next*; turning that into long, layered, real-world plans is not yet solved. **[Established as an open problem, on the approach's own account.]**

### Stuck #4 — "world models" now means two opposite things

Here is a trap in the 2026 excitement. The phrase "world model" has become a banner that two *opposite* bets march under — and mixing them up hides the real disagreement.

- **The generative kind** — Genie 3, Marble, and video-generators — *draw you the world*: they produce the actual pixels of a navigable scene. They are dazzling, and useful for games and film.
- **The non-generative kind** — LeCun's JEPA — refuses to draw pixels on purpose, and predicts only the abstract summary.

The catch: **LeCun argues the generative kind is exactly the wrong path** — the same pixel-predicting detour he says failed for a decade (Part 3). So a headline that "world models are winning" can point at systems built on the very approach he bets against. When you read "world model," you have to ask *which kind* — the pretty pixel-generator, or the abstract non-generative predictor. They share a name and disagree about almost everything. **This is where hype is most likely to mislead:** the word is hot, but the two things it names pull in opposite directions, and only one of them is AP5's actual bet. **[Contested / a definition trap — surfaced 2026-07.]**

### The big question under all of these

Every doubt above is one question: **is a model of the physical world the missing key to intelligence, or a hard road to something text is quietly already reaching?** AP5 says the key is grounding — build the world model from the senses, plan against it, and the mind follows. The critics say: maybe (Stuck #2) words already carry the world; maybe (Stuck #1) the JEPA promise never scales; maybe (Stuck #3) planning stays unsolved even with a good model. And note the twist that ties AP5 to its siblings: its best recent win (DreamerV3, Leg 2) is a world model *joined to reward-learning* ([AP4](04_ap4-rl-from-interaction.md)), and its rival's best answer (Stuck #2) is *more scale* ([AP1](01_ap1-scale-and-foundation-models.md)). So the live 2026 question is whether AP5 is **a replacement for the text-machine road, or a missing *part* that will end up bolted onto it.** *As of July 2026, this is genuinely open* — and, with a billion dollars now riding on it, one of the most watched bets in the field. **[Contested — the key open question.]**

---

## ⚠️ Honesty box

- **The diagnosis is stronger than the cure.** AP5's critique of text machines — too little sensory grounding, drifting word-by-word output, no world model — is sharp and widely respected. The proposed fix — JEPA world models that scale to general intelligence — is still mostly **unproven** (Stuck #1). Keep the strong critique apart from the unproven remedy. **[Contested.]**
- **"Animals do it without language" is an argument, not a result.** It is true and important that minds formed by watching, before words. It does **not** prove a *machine* built this way will reach human-level intelligence, or that words are useless. LeCun himself says language on top of a world model would be "a winner." **[Likely.]**
- **Watch the word "world model" — it hides a fight.** The generative pixel-drawing kind and LeCun's non-generative JEPA kind share a name and disagree about the core (Stuck #4). A claim that "world models work" may be about the approach LeCun bets *against.* Always ask *which kind.* **[Contested.]**
- **The billion-dollar bet is a signal, not a verdict.** Serious money and names (AMI Labs, World Labs) now back this. Funding shows the idea is taken seriously; it does **not** show it is right. The text-machine camp is also funded in the tens of billions. **[Likely.]**
- **Numbers and names age fast.** V-JEPA 2, DreamerV3, Genie 3, Marble, the AMI Labs raise — these are 2018–2026 snapshots. The lasting parts are the **critique** (text is thin; output drifts; no world model), the **idea** (learn a world model from the senses and plan against it), the **trick** (JEPA: predict the abstract summary, not the pixels), and the **four cracks.** The examples around them will change.

---

## How to use this (if you want to direct AI work)

- **First question about any "world model" claim: which kind — generative or non-generative?** (Stuck #4.) A system that draws the next frame and a system that predicts an abstract summary are opposite bets under one name. Pin this down before anything else; most confusion lives here.
- **Ask what the model is trained to predict — pixels, or an abstract representation?** If it is trying to predict every detail of the future, expect it to waste its effort on unpredictable noise (the windy leaves) and to struggle. Predicting the *right level of abstraction* is what matters most.
- **Separate "understands the world" from "talks about the world."** A text machine can describe gravity flawlessly and still have no model that *predicts* a falling cup. When a task needs prediction and planning in the physical world (robots, driving, control), a world model is the relevant idea; fluent text is not evidence of one.
- **For anything needing planning, ask where the world model is.** Planning = imagine actions → predict outcomes → pick the best. Without a model that predicts outcomes, "planning" is just the text machine guessing. If a project claims to plan, find the model it plans against.
- **Treat AP5 as a bet on grounding, and hold it to scale.** Its promise — abstraction and understanding from sensory prediction — is beautiful and, so far, shown mostly small (Stuck #1). Demand evidence that it *scales*, the way you would demand transfer evidence from AP4. Do not confuse a compelling argument with a proven result.
- **What you hand to others:** building the encoder, training on video, running the planner. **What you keep for yourself:** judging whether a system truly has a world model or is only talking, spotting when "world model" quietly switches between the two opposite kinds, and knowing that the deepest part — hierarchical planning — is still unsolved (Stuck #3).

---

## Connections

- **Keep only three things:** ① AP5 = **text is the wrong food; learn how the world works by watching it, then plan.** The machine builds a *world model* (predict: state + action → next state), and plans by imagining action-sequences, predicting outcomes, and picking the best — the thing text machines cannot do. ② Its trick is **JEPA: do not predict the pixels, predict an abstract summary** — throw away unpredictable noise, keep only what matters (the "windy leaves"). Its evidence is that **animals and babies build world models with no language at all**, plus early working systems (Ha & Schmidhuber's "dream," DreamerV3's Minecraft diamonds, V-JEPA 2's robot planning). ③ It is stuck on four cracks: **unproven at scale**, **maybe language already contains the world model** (the AP1 fight), **hierarchical planning is unsolved**, and **"world model" now names two opposite bets.**
- **▶ Go deeper (deep dive):** [#1 · learning without a teacher](../50-deep-dives/05_ap5-deep-dive-learning-without-a-teacher.md) — the learning engine beneath this card's "predict the abstract summary": **self-supervised learning** (learn from raw video with no labels — hide a part, predict it), the **collapse** trapdoor that the JEPA slogan hides (the machine cheats by making every summary identical), the **three guards** against it (contrastive · VICReg · the slow-self-copy trick, with an **EMA target** + **stop-gradient**, that real JEPAs use), the lineage **I-JEPA → V-JEPA → V-JEPA 2 → V-JEPA 2-AC** ending in a real robot that plans zero-shot with **no reward**, and the **energy-based / objective-driven-AI (H-JEPA)** blueprint aimed at Stuck #3. The optional layer past this card.
- **Down the ladder (already read):** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) · [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the text machine, and the wall AP5 says text was always going to hit.
- **Its siblings:** [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) is the one AP5 argues *against* (their clash is the [scaling-suffices debate](01_ap1-scale-and-foundation-models.md), and it is Stuck #2); [AP4 · RL from interaction](04_ap4-rl-from-interaction.md) is AP5's partner — a world model is AP4's escape from needing a fortune of real tries (you plan and practise inside the model), and their joining is DreamerV3.
- **The ideas it leads to** (now written — read them): [AP6 · brain-based](06_ap6-brain-based.md) (the brain is *also* said to be a constant prediction machine, a biological world model), [AP3 · agents](03_ap3-agents-and-cognitive-architectures.md) (a world model is the "planning" part of a full agent), and [AP10 · embodiment](10_ap10-embodiment.md) (a body is how a machine would gather — by *acting*, not just watching — the grounded sensory experience AP5 needs; its action-side partner). See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** The critique of text machines and the animal/baby evidence — **[Established / Likely]**. That JEPA world models *scale* to general intelligence, that grounding beats scale, that planning gets solved — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP5 bet in one plain sentence, using the words *world model*, *watch*, and *plan*.
2. What is a **world model**? Give the "state + action → next state" idea in your own words, and one everyday example (the cup, the table…).
3. Explain the **sensory-bandwidth argument**: why does LeCun say a four-year-old has "seen" more of the world than the biggest text machine has read?
4. What is the **JEPA trick**, and why is predicting *every pixel* of the next video frame a bad idea? (Use the windy-leaves picture.)
5. Give the Stuck-#2 push-back in your own words: how could *language alone* already contain a world model?
6. "World model" names two opposite bets in 2026 — what are they, and which one is AP5's? (Stuck #4.)

## Revision notes

*Newest first.*
- `rev 1 (2026-07-14)` — created as the **AP5** deep-dive, the fourth approach card written (badge = AP index; the `03` slot stays open for the still-unwritten AP3). Built to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)). Placed as a new rung that **builds on** [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md), [scaling/data-wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), [AP1](01_ap1-scale-and-foundation-models.md), and [AP4](04_ap4-rl-from-interaction.md) with short reminders-and-links; it is the **deep home for the world-model idea** AP4 pointed at (no re-teach — AP4's RL frame and sample-inefficiency are referenced, not repeated; the scaling-suffices debate is referenced to AP1). Grounded verbatim in the Lex Fridman × Yann LeCun 2024 conversation (the four missing pieces, the sensory-bandwidth argument, the autoregressive-drift argument, the world-model definition, the planning/MPC picture, the JEPA "don't predict pixels" trick, the "windy leaves," the cat/animal argument, generative video's ten-year failure, and hierarchical planning still unsolved) and in Ha & Schmidhuber's *"World Models"* (2018, the "dream" quote). Full live-web freshness pass (July 2026): V-JEPA 2 (June 2025), DreamerV3 in *Nature* (2025), LeCun leaving Meta for AMI Labs (Nov 2025) and its ~$1.03B raise (Mar 2026), Genie 3 (Aug 2025), and World Labs / Marble (late 2025 → Feb 2026) — each dated and source-graded, with a caution flag on weak hype claims and the generative-vs-non-generative "world model" definition trap surfaced as Stuck #4.

---
*This is the fourth approach page written. Its rival is [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) and its partner is [AP4 · RL from interaction](04_ap4-rl-from-interaction.md); the ideas it leads to are on the [map](../APPROACHES_TO_AGI.md). To see the text-machine road it routes around, read [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md).*
