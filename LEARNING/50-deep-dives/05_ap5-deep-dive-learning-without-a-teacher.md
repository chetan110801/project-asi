---
id: c-jepa-self-supervision
sortkey: 5005
title: AP5 · Deep dive — learning without a teacher: how a JEPA is really trained (and why it doesn't cheat)
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-ap5-world-models, c-rl-the-engine]
provides: [self-supervised-learning, pretext-task, representation-embedding, representation-collapse, contrastive-learning, vicreg-regularized-ssl, distillation-ema-target-stop-gradient, i-jepa, v-jepa, v-jepa-2-ac-action-conditioned-world-model, energy-based-models, objective-driven-ai-hjepa]
resources: []
status: ready
reading_time: 36 min
rev: 1
created: 2026-07-17
updated: 2026-07-17
---

# AP5 · Deep dive — learning without a teacher: how a JEPA is really trained (and why it doesn't cheat)

*This is a **deep dive** past the [AP5 card](../20-the-approaches/05_ap5-world-models-jepa.md). The card gave you the whole bet — stop feeding the machine our words, let it watch the world, build an inner model of how the world works, and plan against it — and it named the clever trick at the heart of it: **JEPA** — "don't predict the pixels, predict an abstract summary." That is the **what**. But it never opened the machine. And there is a hole right under that slogan that a sharp reader hits at once: if you reward the machine for making its own summaries easy to predict, **why doesn't it just cheat — output the exact same summary for everything, so prediction is always perfect and the summary means nothing?** That failure has a name — **collapse** — and beating it is the entire reason a JEPA is hard to build. This page is the machine the card only pointed at: where the training signal comes from when there is no teacher (self-supervised learning), the collapse trap the slogan hid, the three ways the field beats it, the real lineage of systems from a single image to a robot that plans, and the bigger blueprint the whole thing sits inside. Everything the card already said is referenced, not repeated.*

> **You are here:** a **deep-dive module** — reading group **⑤**, the optional layer that branches off the main staircase. This one hangs off **[AP5 · world models / JEPA](../20-the-approaches/05_ap5-world-models-jepa.md)**. *Read the AP5 card first* — this page assumes it and opens the machine the card only named. It is the first deep dive off AP5.
>
> **What you already have (a one-line reminder each, then we build — none of it is re-taught here):** from the **[AP5 card](../20-the-approaches/05_ap5-world-models-jepa.md)** — the **bet** (learn from watching, not from text); the **world model** (predict: *state now + action → state after*, where **state** = everything that matters about the situation now); **planning by imagining** (try action-sequences in your head, predict where each ends, keep the best); and the **JEPA trick** — pass the input through an **encoder** *(a part that squeezes raw input into a short summary)* and predict an **abstract summary** *(a stripped-down code that keeps the meaning and drops exact detail)* instead of the raw pixels, so the machine wastes no effort guessing unpredictable noise (the card's "windy leaves"). From **[AP4 · the engine](04_ap4-deep-dive-the-engine.md)** — the *model-based* idea: **learn a model of the world and practise inside it, in imagination, for free** (its MuZero and DreamerV3). **New here:** how you actually *train* that encoder when nobody hands you labels — and why the obvious way quietly destroys itself.
>
> **Where the facts come from:** written, checkable sources, each quote grep- or web-verified as exact. The **method** papers — *I-JEPA* (Assran et al., 2023), *V-JEPA 2* (Meta, 2025), *VICReg* (Bardes, Ponce & LeCun, 2022) — and a survey of contrastive self-supervised learning in the project corpus. The durable framing (energy-based models, the full "objective-driven AI" blueprint) traces to LeCun's writing and course. The **fast-moving facts** — which systems exist, the scores, the newest results — are checked on the web (**as of July 2026**) and dated where they move.

---

## In one minute

The card said a JEPA "predicts an abstract summary, not the pixels." Fine — but that one line hides a whole machine and a hidden trap. Here is the machine, in four stacked steps.

1. **The teacher problem — learning with no labels (self-supervised learning).** Nobody labels a million hours of video by hand. So the machine makes its *own* homework: hide part of the data and try to fill in the hidden part from the rest. The "right answer" is just the part it hid — free, no human needed. This is **self-supervised learning**, and it is exactly how the text machine of [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md) already learns (hide the next word, guess it). A JEPA does the same — but it hides and predicts in the *summary* space, not the raw input.
2. **The trap the slogan hid — collapse.** Here is the catch the card never mentioned. If you train the machine to make its summaries *easy to predict*, it finds a horrible shortcut: make every summary **identical**. Then prediction is perfect and the summary is worthless — it says nothing about the input at all. This is **representational collapse**, and it is the single enemy that makes a JEPA hard. Predicting raw pixels was *safe* from this (you cannot fake a whole video frame); predicting summaries is *dangerous* — the freedom that made JEPA elegant is the same freedom that lets it cheat.
3. **The three ways to beat the cheat.** The whole field of this kind of learning is really three tricks to stop collapse: **push different things apart** (contrastive), **force the summaries to stay spread out and non-redundant** (regularized — VICReg), or **make the machine chase a slow-moving copy of itself** (distillation — the trick real JEPAs use). Each stops the "everything identical" shortcut in a different way.
4. **From one image to a robot that plans.** With collapse beaten, the same idea scales up a clear ladder: **I-JEPA** (fill in a masked patch of one image, 2023) → **V-JEPA** (do it across time in video, 2024) → **V-JEPA 2** (2025, over a million hours of video) → **V-JEPA 2-AC**, which adds *actions* and becomes a real world model a robot can **plan** inside — zero-shot, on hardware it never trained on.

And the payoff for the whole AP5 bet: the card promised "learn how the world works by watching, then plan." **V-JEPA 2-AC is that sentence turned into a working robot** — and it works entirely on the self-supervised, anti-collapse machine below. The card gave the promise; this page shows the engine that (partly) keeps it.

---

## One line of base, then we build

Two reminders from the card, because the whole page turns on them.

- The card's JEPA trick was: **predict an abstract summary, not the pixels.** It said *why* that is smart (you stop wasting effort on unpredictable noise). It never said *how you train an encoder to produce a good summary in the first place*, when there is no human telling it what a good summary is. **Parts 1–3 are that "how."**
- The card's world model was: **state + action → next state**, and you *plan* by imagining actions and predicting outcomes. The card showed this as an idea. It named one system, V-JEPA 2, in a single line. **Part 4 opens that system** — how the abstract summary machine actually becomes a thing a robot plans with.

Now the one new frame this page adds. The card asked *what a world model is and whether the bet is right.* This page is one level down: *how you learn one from raw watching, with no teacher.* So read every part as a piece of a machine — here is a job the card said must happen → here is the concrete mechanism → here is what it costs. We are **not** re-judging the bet (the card did that, with its four cracks). We are opening the learning engine the bet rides on, and only at the end asking whether the *engine's own* limits change the picture.

---

## Part 1 — the teacher problem: learning with no labels

Start with the question the card walked straight past. To learn from video, the machine needs to be *trained* — corrected, over and over, toward something. But trained toward *what*? Who says whether a summary is good or bad?

**First, the old way — and why it cannot work here.** The usual way machines learn is **supervised learning** *(supervised = a human supplies the right answer for each example, like a teacher marking homework)*. You show a picture, a human has written "cat," the machine guesses, you correct it toward "cat." This built most of early AI. But it has a hard limit that kills it for AP5: **someone must label every example by hand.** For a million hours of video, that is impossible — there is no army of people big enough to write down what is happening in every frame. If the machine can only learn from what humans label, it can never drink from the ocean of raw, unlabelled video the card's whole bet depends on. The teacher does not scale.

**The move that changes everything — let the data be its own teacher.** Here is the trick that unlocks learning from raw video, and it is beautiful in its simplicity: **hide part of the data, and train the machine to fill in the hidden part from the part it can still see.** No human is needed, because the "right answer" is the piece you hid — you already have it. Cover a patch of a photo and predict what was under it. Cut a video in half and predict how it continues. The data supplies its own questions *and* its own answers. This is **self-supervised learning** *(self-supervised = the supervision, the "right answer," comes from the data itself, not from a human; "self" = it teaches itself)*. The made-up task you invent for this — "predict the hidden patch," "predict the next second" — is called a **pretext task** *(pretext = a pretend job; the machine does not really care about filling in the patch — the patch-filling is an excuse that forces it to learn how the world looks and moves)*.

*(Why this matters so much:* it is the reason any of the card's bet is even possible. "Watch a million hours of video and learn how the world works" is only affordable because **no human has to label any of it.** Self-supervised learning is the key that opens the ocean of raw sensory data. Without it, AP5 is a nice idea with no fuel.)*

**You have already met this idea — it is how the text machine learns.** Recall from [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) that today's main AI is trained by hiding the next word and making the machine guess it, across billions of pages. *That is self-supervised learning* — the hidden word is the free label. So the text machine ([AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md)) and the JEPA world model (AP5) share the **exact same learning idea** — predict a hidden part from a visible part. They differ in one deep choice, and that choice is the whole story of this page: **what space they predict in.**

- The text machine predicts in the **raw input space** — it predicts the actual next *word*, one of a fixed list.
- A JEPA predicts in the **summary space** — it does *not* try to reproduce the hidden pixels; it predicts the *abstract summary* of the hidden part (the card's trick).

That one difference — predict the summary, not the raw thing — is what makes a JEPA powerful. It is also what opens the trapdoor the card never showed you. To see the trap, we have to look at exactly what "predict the summary" asks the machine to do.

---

## Part 2 — the cheat that ruins everything: collapse

Here is the landmine hidden under the card's clean slogan. Walk onto it slowly, because it is the single most important idea on this page.

Set up the JEPA task exactly as the card described. Take a video. Feed the "before" part through the encoder to get a summary — call it the **context summary**. Feed the "after" part through an encoder to get *its* summary — the **target summary**. Now train a small **predictor** *(a little network whose only job is to guess one summary from another)* to go from the context summary to the target summary. Push the machine to make that prediction as accurate as possible. Sounds right — that is "predict the abstract representation."

**Now watch the machine find the cheat.** The machine is not trying to understand the world. It is trying to make one number as small as possible: the gap between its prediction and the target summary. So it asks, coldly: *what is the easiest way to make that gap zero?* And there is a shortcut that beats every honest answer. **Make the encoder output the same summary for absolutely everything.** If every "after" is summarised as, say, the number 7, and every "before" is too, then the predictor's job is trivial — always guess 7 — and the prediction is *perfect, every time.* The gap is zero. The machine has "won."

And it has learned **nothing.** A summary that is 7 for a sunset, 7 for a car crash, and 7 for an empty room tells you *nothing* about the input. It is not a compressed meaning; it is a blank. The machine did not learn to see the world — it learned to **shut its eyes and say the same word forever.** This failure is called **representational collapse** *(collapse = the summaries fall in on themselves to a single constant point, carrying no information; "representation" = the summary/code the encoder produces)*. The VICReg paper (Bardes, Ponce & LeCun, 2022) states the trap in one flat line:

> "A trivial solution is obtained when the encoder outputs constant vectors."
> *(Bardes, Ponce & LeCun, VICReg, 2022)*

*("Trivial solution" = a useless answer that technically wins the game. "Constant vectors" = the same fixed summary for every input — the "always 7" above; a **vector** here is just the list of numbers that makes up one summary.)* Collapse is not a rare bug. It is the *most tempting* answer the machine can find, because it is the easiest. Left alone, a JEPA does not drift toward understanding — it **races toward the blank.**

### Why this is the deep reason JEPA is hard — and why predicting pixels was "safe"

Now the piece that ties it back to the card and makes everything click. The card said the *generative* way — predict every pixel of the next frame — failed because it wastes effort on unpredictable detail (the windy leaves). True. But there is a second thing the card did not say: **predicting raw pixels is at least safe from the cheat.** You cannot make the "everything is identical" shortcut work when you are forced to draw the *actual* next frame — a blank constant image would be an obviously terrible prediction of a real video, so the machine is *forced* to keep real information. The raw pixels are a demanding teacher that cannot be fooled.

The moment you switch to predicting a *summary* — the card's whole trick — you take away that safety. Now the machine controls *both* what it predicts *and* what the target is (both are summaries it produces). So it can quietly change the target into something trivial to predict — the blank. **The very freedom that makes JEPA elegant (throw away noise, keep only meaning) is the same freedom that lets it cheat (throw away *everything*, keep nothing).** That is the trapdoor under the slogan. So the real engineering question of a JEPA is not "how do I predict the summary?" — it is: **"how do I stop the encoder from collapsing to a blank, while still letting it throw away the noise it should throw away?"** Answer that, and you have a JEPA. That answer is Part 3.

---

## Part 3 — the three ways to beat the cheat

There are three families of tricks that stop collapse, and — this is worth holding — **almost every self-supervised system of the last decade is one of these three.** They all fight the same enemy (the blank) from different sides. Take them in order of how they think.

### Way 1 — contrastive: push different things apart

The first idea is the most direct. Collapse happens because the machine is only ever told "make matching things *close*" (the before-summary near the after-summary). If that is the only rule, "make everything close by making everything identical" wins. So **add the opposite rule: make *non*-matching things *far apart.*** Show the machine a matching pair (two views of the same thing) and also a pile of **negative examples** *(negatives = other, unrelated inputs — a different video, a different image)*, and train it to pull the matching pair together *while pushing the negatives away.* Now the blank is impossible: if every summary were identical, the negatives would be close too, and the "push apart" rule punishes that hard. The corpus survey states the core in one line:

> "The central idea in contrastive learning is to bring similar instances closer and push away dissimilar instances far from each other."
> *(survey of contrastive self-supervised learning, project corpus)*

*("Contrastive" = based on contrast — it learns by comparing what should be alike against what should be different. "Instances" = individual examples/inputs.)* This is called **contrastive learning**, and its famous systems (like SimCLR, 2020) work exactly this way. It works well. But it has a real cost: **you need a lot of negatives** to get good summaries, which means comparing **big batches** *(batch = a group of examples the machine processes together in one go)* of data all at once, which is heavy and awkward — and you have to be careful, because two of your "negatives" might actually be similar (two different photos of cats), and then you are wrongly teaching the machine to push cats apart. Contrastive learning beats collapse, but it pays in appetite and fuss.

### Way 2 — regularized: force the summaries to stay spread out

The second idea is cleverer and needs no negatives at all. Instead of *comparing* inputs, watch the summaries themselves and **forbid the blank directly with a rule.** Collapse means all the summaries pile up on one point. So add a rule that says: *across a batch of inputs, each number in the summary must keep some spread — it is not allowed to be the same for everyone.* If the spread is forced to stay above a floor, the summaries **cannot** all fall onto one point, so collapse is banned by construction. This is what **VICReg** does *(the name = its three rules: **V**ariance — keep the summaries spread out, the anti-collapse rule; **I**nvariance — still make matching pairs close, the ordinary predict-the-target job from Part 2; **C**ovariance — stop the numbers copying each other)*. Its own words for the fix:

> "explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually."
> *(Bardes, Ponce & LeCun, VICReg, 2022)*

*("Variance" = how spread out a set of numbers is; high variance = they differ a lot, zero variance = all identical. "Regularization term" = an extra rule added to the training goal to force good behaviour. "Embeddings" = the summaries again — another word for the encoder's output code. "Along each dimension individually" = for each separate number inside the summary.)* In plain words: **VICReg keeps each part of the summary from going flat.** It adds a second guard too — it decorrelates the numbers *(decorrelate = stop different parts of the summary from all copying each other, so the summary uses its whole capacity instead of repeating one fact many times)*. The beauty of this family is that it needs **no negatives, no big batches** — just a rule watching the summaries. The cost is that it is a more delicate balancing act: you are tuning the strength of a rule rather than relying on the data.

### Way 3 — distillation: chase a slow copy of yourself

The third idea is the strangest, and it is the one **real JEPAs actually use** — so slow down here. It sounds like it *should* collapse, and mysteriously does not.

Use **two** encoders, not one. Call them the **student** and the **teacher** *(these are just names for the two copies)*. The student sees the "before" and tries to predict the teacher's summary of the "after." Two rules make it work:

- **The teacher is a slow-moving copy of the student.** You do not train the teacher directly. Instead, after each step, you nudge the teacher's settings a tiny bit toward the student's — so the teacher is a smoothed, lagging average of the student over time. This is called an **EMA target** *(EMA = exponential moving average — a running average that leans on the recent past; "target" = the thing the student aims at)*.
- **Stop-gradient — the teacher never learns from the chase.** The correction signal that improves the student is **not** allowed to flow into the teacher. The teacher is frozen at each moment, a fixed target; only the student moves. This block is called **stop-gradient** *(gradient = the correction signal that adjusts a network; "stop" = it is cut off from the teacher)*.

Why does this dodge the blank? Because the student is always chasing a target that is **just behind it, not equal to it.** If the student tried to collapse to a constant, the teacher (its own recent past) would still be pointing somewhere slightly different, so there is always a real, moving target to predict — the "everything identical" shortcut never quite closes. Systems called **BYOL** (2020) and **DINO** (2021) showed this works surprisingly well with no negatives at all. And **this is the machine inside I-JEPA and V-JEPA**: a context (student) encoder, a slow **EMA** target (teacher) encoder, a predictor between them, a **stop-gradient** on the target — plus **masking** (hiding patches) as the pretext task. The web-checked summary of how V-JEPA beats the blank names exactly these parts: masking one branch, an EMA of the other branch, isolated by a stop-gradient *(as of 2025)*.

### The honest catch, saved for the judge-it

Hold one uncomfortable fact about Way 3, because it comes back at the end. Nobody fully agrees on *why* the slow-copy trick avoids collapse — it works in practice, and the theory of exactly what stops the blank is still argued over. The whole area is, as of 2026, a **collection of clever guards** — negatives, variance rules, slow copies, masking schemes — each of which *works*, rather than one clean, understood principle. Keep that; it is the machinery's deepest crack.

So: three ways to stop the machine from shutting its eyes. Contrastive pushes rivals apart; regularized forbids the blank with a rule; distillation chases a slow self. With one of these in place, the encoder is finally *forced* to keep real information — and now, at last, it can learn something worth scaling. That is Part 4.

---

## Part 4 — the lineage: from one image to a robot that plans

The card named one system, **V-JEPA 2**, in a single line and moved on. But V-JEPA 2 is the top of a clear ladder, and climbing the ladder is the best way to see the abstract machine turn into a thing that acts in the world. Four rungs.

**Rung 1 — I-JEPA (images, 2023).** The first clean JEPA. The pretext task: take one image, look at a small **context block** *(a visible patch)*, and predict the *summaries* of several hidden **target blocks** *(masked-out patches)* elsewhere in the same image — using the distillation machine of Part 3. The paper's own plain statement:

> "We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image."
> *(Assran, Duval, Misra, Bojanowski, Vincent, Rabbat, LeCun & Ballas, I-JEPA, 2023)*

*("Non-generative" = it does **not** draw the pixels — exactly the card's Stuck #4 line, now built into a real system. "Representations" = the summaries.)* The result that mattered: predicting *summaries* of masked patches, with no pixel-drawing and no hand-made tricks for flipping or cropping the image, gave **strong, useful image understanding** — first solid proof the card's "predict the summary, not the pixels" actually learns good features at scale.

**Rung 2 — V-JEPA (video, 2024).** The same idea, now across **time**: mask parts of a video and predict their summaries from the visible parts. This is the real target, because *time* is where a world model lives — "what happens next" is a question about time, not a still image.

**Rung 3 — V-JEPA 2 (2025) — scale.** The big one the card named. V-JEPA 2 was pre-trained on **over a million hours of internet video** with the JEPA machine above. The paper frames the whole ambition in one sentence:

> "This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world."
> *(V-JEPA 2, Meta, 2025)*

*("Internet-scale" = as much data as the whole internet holds. "Trajectories" = recorded paths of a robot's movements over time.)* On plain watching, it does well — for example **77.3%** on a standard motion-understanding test (Something-Something v2) and a state-of-the-art **39.7** on anticipating human actions (Epic-Kitchens-100), and, when joined to a language model, top scores on video question-answering *(all as of the June 2025 paper)*. But watching is not the point. The point is the fourth rung.

**Rung 4 — V-JEPA 2-AC — the world model that plans.** Here the passive watcher becomes an agent. The problem: a plain video model predicts "what happens next" on its own, but a world model needs to predict "what happens next **if I take this action**" — the card's *state + action → next state*. So Meta did a small, striking add-on. They took the big watched-from-video model and **post-trained** it *(trained a bit more, on top)* on **less than 62 hours of unlabelled robot video** to make it **action-conditioned** *(action-conditioned = its prediction now takes the robot's action as an input; "conditioned on" = "depends on")*. The paper's line:

> "post-training a latent action-conditioned world model, V-JEPA 2-AC, using less than 62 hours of unlabeled robot videos from the Droid dataset."
> *(V-JEPA 2, Meta, 2025)*

*("Latent" = happening in the summary space, not in pixels — "latent" means hidden/internal, the abstract code from Part 1; this is the key word.)* Read what that gives you. Now the machine can answer, *in its abstract summary space,* "if the arm moves like this, what is the next state?" — which is exactly a world model you can **plan** inside (the card's plan-by-imagining). And it did the thing the whole AP5 bet promised: deployed **zero-shot** *(with no training in that place)* on real **Franka robot arms** *(Franka = a common brand of robotic arm)* **in two different labs**, it could **pick up and place objects it was never trained on there** — guided only by a picture of the goal, **with no reward and no task-specific training** *(as of 2025)*.

Sit with why that is the card's bet made real. AP4's engine ([the engine deep dive](04_ap4-deep-dive-the-engine.md)) needed a *fortune* of real tries and a hand-made reward. V-JEPA 2-AC planned a real-world manipulation **from watching**, with **no reward at all**, in a place it had never seen — because it had a *model* of how things move and could imagine its way to the goal. This is "learn how the world works by watching, then plan" (the card) and "learn a model and plan inside it" (AP4's model-based branch) — the same sentence, now standing up as a robot. Note the deep contrast with the card's Stuck #4 rival: a *generative* video model would try to **draw** the future frames to plan; V-JEPA 2-AC plans in the **latent summary space** and never draws a pixel. That is the non-generative bet, working.

*(The honest size of it, saved for the judge-it:* this is **narrow** — table-top picking and placing, short horizons, modest success rates. It is a real demonstration of the principle, **not** a general worker. Hold the pride and the smallness together.)*

---

## Part 5 — the bigger blueprint: energy-based models and objective-driven AI

One last step up, kept short — a **bridge**, not a re-teach, because the card owns the planning story and its Stuck #3. The JEPA you have just built is not meant to be the whole mind. In LeCun's design it is **one module** inside a larger machine. It is worth seeing the frame, because it says where this whole road is trying to go.

**The frame is "energy-based."** Underneath all of Part 3 is one simple way of thinking: instead of a machine that *outputs an answer*, build a machine that *scores how well two things fit together* — it gives a **low score** when they are compatible (this "after" really could follow this "before") and a **high score** when they clash. This score is called an **energy** *(energy here = a made-up "badness" number; low energy = good fit, high energy = bad fit — borrowed from physics, where things settle into low-energy states)*. Training means shaping this score so that real pairs get low energy and wrong pairs get high energy — and **collapse (Part 2) is just the failure where the machine gives everything low energy**, which is why the whole page has really been about energy all along. This view is called an **energy-based model**, and it is LeCun's preferred language for the entire approach.

**The full blueprint — objective-driven AI.** In a 2022 position paper, *A Path Towards Autonomous Machine Intelligence*, LeCun sketched a whole architecture with the JEPA world model at its centre, wired to a handful of other parts: a **perception** module (turn raw senses into a state), the **world model** (the JEPA — predict next state from action), a **cost/objective** module (score how far a state is from the goal — the thing planning tries to make small), an **actor** (propose the action-sequences), and a **short-term memory.** Planning, in this design, is the card's loop — imagine action-sequences, run them through the world model, keep the one the cost module likes best — now drawn as a full standing system rather than an idea.

**And this is where the card's Stuck #3 gets its proposed answer.** The card said the deepest unsolved piece is **hierarchical planning** *(planning in layers — big steps made of smaller steps; the card owns this, so it is only referenced here)*. LeCun's proposed fix is to **stack JEPAs** — a **Hierarchical JEPA (H-JEPA)** — where a higher-level JEPA predicts in a coarser, more abstract summary (long, slow steps) and a lower one fills in the fine, fast detail. Whether that actually works is **open** — it is a *proposal*, not a result (the card's Stuck #3 stands). But it tells you the ambition: the anti-collapse summary machine of this page is meant to be **stacked into layers** until it can plan a trip, not just a grab. Consider that pointed at, and handed back to the card.

---

## Putting the machine together

Hold the whole engine in one view.

1. **The teacher problem (Part 1) — self-supervised learning.** No human can label an ocean of video, so the data teaches itself: **hide a part, predict it from the rest.** The same idea as the text machine's next-word game — but a JEPA predicts in the **summary space**, not the raw input.
2. **The trap (Part 2) — collapse.** Predicting a summary you also control invites a cheat: **make every summary identical** → perfect prediction, zero meaning ("a trivial solution … constant vectors"). Predicting raw pixels was safe from this; predicting summaries is not. Beating collapse *is* the JEPA problem.
3. **The three guards (Part 3).** **Contrastive** (push negatives apart — SimCLR), **regularized** (forbid the blank with a variance rule — VICReg, no negatives), and **distillation** (chase a slow **EMA** copy of yourself behind a **stop-gradient** — BYOL/DINO; the machine real JEPAs use, with masking).
4. **The lineage (Part 4).** **I-JEPA** (mask an image patch, predict its summary, 2023) → **V-JEPA** (video, 2024) → **V-JEPA 2** (>1M hours, 2025) → **V-JEPA 2-AC** (add actions on <62 hours of robot video → a **latent** world model that plans real robot pick-and-place, zero-shot, no reward). The AP5 bet, standing up.
5. **The blueprint (Part 5).** It is all **energy-based** (score fit; collapse = giving everything a low score), and the JEPA is one module in LeCun's **objective-driven AI**; the proposed answer to the card's Stuck #3 (hierarchical planning) is a **stack of JEPAs (H-JEPA)** — a proposal, still open.

---

## Judging the machinery: where the learning engine itself is stuck

The card judged the *bet* (four cracks: unproven at scale · language may already carry the world model · hierarchical planning unsolved · "world model" names two opposite things). This page judges the *learning engine* — a different, narrower question. The engine is real: self-supervised JEPAs learn genuinely useful things from raw video, and one of them planned a real robot. Be fair and hold that. But the machinery has its **own** cracks, separate from the bet's, and they sharpen what is and is not proven.

### Stuck #1 — collapse is beaten by recipe, not by understanding

Everything in Part 3 is, honestly, a **bag of guards** — negatives, variance rules, slow copies, stop-gradients, masking schemes — each of which *stops the blank in practice*, while the clean theory of *why* (especially for the slow-copy trick) is still argued over. A recent line of work makes the point sharply: as of **late 2025**, a method called **LeJEPA** was presented as the *first* JEPA to drop this pile of hand-tuned guards in favour of one principled rule — the whole selling point being that *until then*, **every published JEPA leaned on at least one heuristic** *(heuristic = a trick that works but is not derived from a clean principle)* to prevent collapse. That is the field admitting its own foundation is patchy. So a fair verdict: the JEPA learning engine **works but is not yet understood** — much of the craft is **keeping the training from falling apart** against a failure we cannot fully explain, the same story the [RL engine](04_ap4-deep-dive-the-engine.md) had with its deadly triad: a method that works only when handled just right, held together by patches. **[Established that the guards are heuristic; Contested whether a clean principle (LeJEPA-style) now settles it — too new, as of 2026-07.]**

### Stuck #2 — a non-collapsed summary is not the same as understanding

This is the most important doubt, and it cuts straight into the card's Stuck #1. Beating collapse guarantees the summaries carry *real information* — but "carries real information" is a low bar. It does **not** guarantee the summaries carry the **right, deep, plannable** understanding of the world the bet needs. And look at *what the systems are actually measured on*: the wins in Part 4 are **perception** wins — recognising motion, anticipating the next action, answering questions about a clip, short-horizon table-top grabbing. Those are real, but they are the *easy end* of "understanding the world." Nobody has yet shown a JEPA doing the *hard* end — long, multi-step reasoning and planning far into the future — which is the very thing the card promised and the [scale road](../20-the-approaches/01_ap1-scale-and-foundation-models.md) actually delivers. So the engine has climbed from "blank" to "good perceptual features"; the leap from there to "a world model rich enough to plan a life" is **exactly the card's unproven promise, now located precisely** — it lives in the gap between *good features* and *deep understanding*, and no anti-collapse trick closes that gap by itself. **[Contested — the central open question, inherited from the card's Stuck #1 and sharpened here.]**

### Stuck #3 — you don't get to choose what the summary throws away

The card sold the JEPA trick as "throw away the unpredictable noise (windy leaves), keep what matters." Here is the uncomfortable other edge of that blade: **the machine decides what is "noise," and it decides by predictability — not by importance.** But the world is full of things that are **hard to predict yet absolutely matter**: a child darting into the road, a rare fault in a machine, the one surprising event you most need to catch. Those are, by definition, *un*predictable — exactly the kind of thing the encoder is trained to treat as noise and discard. So the very rule that makes JEPA efficient ("drop what you can't predict") risks **dropping the rare, important surprise** along with the meaningless flicker. "Keep what is predictable" and "keep what matters" are **not the same set**, and a JEPA optimises for the first while the bet needs the second. This is a genuine, under-discussed crack in the trick itself, not just in its scale. **[Likely — a real structural tension in the objective; how much it bites in practice is open.]**

### Stuck #4 — how do you even *score* a latent world model?

The card's trick was to stop predicting pixels. That buys efficiency — and a measurement problem the card never mentioned. With a pixel-predictor you can at least *look* at its predicted frame and see if it is right. A JEPA predicts an **abstract summary** on purpose, so **there is nothing to look at** — no picture to compare against reality. How, then, do you tell a good world model from a bad one? In practice the field falls back to **downstream tasks** *(downstream = further along — judge the model by how well something built on top of it performs, e.g. a robot's success rate)*. But that score mixes the world model's quality with the quality of everything *else* in the pipeline — the planner, the controller, the goal. You can rarely say "the *model* is good"; you can only say "the *whole stack* worked here." So the field is partly **working without a clear way to measure** the very thing it most wants to improve. That both slows progress and makes bold "our world model understands physics" claims hard to check — the card's warning about hype, now given its mechanical root. **[Established as a real difficulty; the best way to evaluate latent world models is an open research question, as of 2026-07.]**

### The big question under all four

The card asked: *is a model of the physical world the missing key to intelligence, or a hard road to something text is quietly already reaching?* The engine answers a narrower, mechanical version: **is "learn to represent the world without collapsing" the seed of understanding — or a very good perception front-end that still lacks the reasoning and planning it was supposed to unlock?** Everything on this page points, honestly, at the second, *for now.* Self-supervised JEPAs are a real and important way to learn useful structure from raw sensory data with no teacher — arguably the only known way to drink the ocean of video the bet depends on. That is a genuine achievement and a necessary one. But "no teacher, no collapse, good features, one real robot grab" is a long way from "a mind that plans." **As of July 2026, the learning engine has convincingly solved the *entry* problem (how to learn from unlabelled reality at all) — and the fact that the solved part is *perception* while the unsolved part is *deep understanding and long-horizon planning* is exactly where the whole AP5 bet still hangs.** The engine works; it has carried the bet to the door, not through it. **[Contested — the key open question, now sharpened: the door is the leap from good self-supervised features to a plannable world model.]**

---

## ⚠️ Honesty box

- **Self-supervised learning is the durable core; the systems are snapshots.** *Learning with no labels by hiding-and-predicting, collapse and the three guards against it, predicting in a summary space* — these are load-bearing ideas that will still be central in a decade. The specific systems (**I-JEPA, V-JEPA 2, VICReg, BYOL, DINO, LeJEPA**) and their scores are 2020–2026 snapshots that will move. Learn the mechanisms; treat the systems as illustration. **[Established for the mechanisms; the specifics are dated.]**
- **Collapse is the one idea to keep.** Of everything here, "a machine trained to make its own summaries predictable will cheat by making them all identical, and beating that cheat *is* the whole problem" is the single most durable and clarifying point. If you keep one thing, keep collapse. **[Established.]**
- **The guards against collapse work but are not fully understood.** Especially the slow-copy (distillation) trick that real JEPAs use — it works, and nobody fully agrees why (Stuck #1). Do not read "V-JEPA avoids collapse" as "the field has a clean theory of representation learning." It has a set of reliable tricks. **[Established / Contested.]**
- **V-JEPA 2-AC is a real robot, and a narrow one.** It planned genuine, zero-shot, no-reward manipulation from watching — a true proof of the card's principle. It is also table-top picking and placing at modest success rates, not a general worker (Stuck #2). Hold the achievement and its smallness together; the gap between them is the whole open bet. **[Likely / dated.]**
- **"It learns from raw video with no labels" is true and easy to over-read.** Self-supervision genuinely opens the ocean of sensory data — a necessary key. But learning *good perceptual features* with no teacher is not the same as learning a *world model deep enough to plan a life* (Stuck #2), and "keep what's predictable" quietly is not "keep what matters" (Stuck #3). The engine solved the entry problem; it did not thereby solve the bet. **[Contested.]**

---

## How to use this (if you want to direct AI work)

- **When someone says "self-supervised," ask what the pretext task is and what space it predicts in.** (Parts 1–2.) *Predict the hidden part from the visible part* is the shape; the live question is **raw space or summary space?** Raw-space (pixels, words) is safe from collapse but wasteful on noise; summary-space (JEPA) is efficient but must actively fight collapse. The choice decides the system's whole character.
- **On any joint-embedding / JEPA system, the first question is: how does it stop collapse?** (Part 3.) There are only three real answers — negatives (contrastive), a spread-out rule (VICReg-style), or a slow self-copy with stop-gradient (distillation). If a team cannot tell you which guard they use, they do not yet understand their own training, and unstable or suspiciously-easy results should be your first worry.
- **Separate "beat collapse" from "understand the world."** (Stuck #2.) A model that scores well on recognition and anticipation has proven it did *not* collapse and learned useful features — it has **not** proven it has a plannable world model. Demand evidence at the hard end (long-horizon prediction, real planning), not the easy end (perception), before believing the big claim.
- **Ask what the model was allowed to throw away — and whether the thing you care about is in it.** (Stuck #3.) A JEPA discards the unpredictable. If your task hinges on rare, surprising, safety-critical events (the child in the road, the rare fault), a "predict the summary" model may have been *trained to ignore exactly those.* Check that the abstraction kept what your problem needs, not just what was easy to predict.
- **Distrust any evaluation of a latent world model that is not end-to-end.** (Stuck #4.) Because there are no pixels to check, "our world model is good" almost always really means "our whole stack did well on this task." Ask what *else* is in the pipeline before crediting the model, and treat naked "it understands physics" claims as unproven.
- **What you delegate vs what you keep.** *Delegate:* building the encoders, the masking, the predictor, the training loop, the anti-collapse guard. *Keep for yourself:* choosing raw-space vs summary-space (the character call), checking that collapse is genuinely handled, judging whether "good features" has been oversold as "understanding," and asking whether the model's learned abstraction kept the rare things your problem cannot afford to lose.

---

## Connections

- **Keep only three things:** ① A JEPA learns with **no teacher** — **self-supervised learning**: hide part of the data, predict it from the rest (the same idea as the [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md) machine, but predicting in the **summary space**, not raw pixels). ② That freedom opens a trapdoor — **collapse**: the machine cheats by making every summary identical ("a trivial solution … constant vectors"), so prediction is perfect and meaning is zero; **beating collapse is the entire JEPA problem**, and there are three guards — **contrastive** (push negatives apart), **regularized** (VICReg's spread-out rule), **distillation** (chase a slow **EMA** self behind a **stop-gradient** — what real JEPAs use). ③ With collapse beaten, the ladder **I-JEPA → V-JEPA → V-JEPA 2 → V-JEPA 2-AC** turns the summary machine into a **latent world model that plans a real robot, zero-shot, with no reward** — the card's bet standing up — but it wins *perception*, not yet *deep planning*, so the bet still hangs on the gap between good features and real understanding.
- **This deep dive branches off:** [AP5 · world models / JEPA](../20-the-approaches/05_ap5-world-models-jepa.md) — the card owns the *bet, the world-model definition, planning-by-imagining, the JEPA slogan, the windy-leaves, the animals/babies evidence, the world-models race,* and the *four cracks in the bet* (including hierarchical planning, Stuck #3, and generative-vs-non-generative, Stuck #4); this page opens the *learning engine* underneath the slogan (self-supervision + collapse + the guards + the real systems) and judges the *engine's own* limits.
- **Down the ladder it leans on:** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — the text machine's training *is* self-supervised learning (hide the next word), the same idea in a different space; and [AP4 · the engine](04_ap4-deep-dive-the-engine.md) — its *model-based* branch (learn a world, plan inside it — MuZero, DreamerV3) is what V-JEPA 2-AC makes real in a **learned latent space**, at last with no reward.
- **Where it points:** [AP1 · scale](../20-the-approaches/01_ap1-scale-and-foundation-models.md) is the rival the engine is measured against (it delivers the deep reasoning JEPAs have not yet shown — Stuck #2); [AP6 · brain-based](../20-the-approaches/06_ap6-brain-based.md) is the natural next stop (the brain is also cast as a constant prediction machine); and the card's [hierarchical-planning](../20-the-approaches/05_ap5-world-models-jepa.md) crack is where the energy-based **H-JEPA** blueprint of Part 5 is aimed.
- **How sure are we?** That self-supervised JEPAs learn useful features from raw video with no labels, that collapse is real and the three guards work in practice, and that V-JEPA 2-AC planned a real zero-shot robot grab — **[Established / Likely]**. That the guards rest on a clean principle, that beating collapse yields a *plannable* world model, and that "predict the summary" keeps what actually matters — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. What is **self-supervised learning**, in the "hide a part, predict it" phrase? Why is it the *only* affordable way to learn from a million hours of video — and how is it the same idea as how the text machine learns?
2. Explain **collapse** in your own words. Why is "make every summary identical" a *winning* move for the machine, and why does it destroy all the meaning?
3. Why was predicting **raw pixels** *safe* from collapse, while predicting an **abstract summary** (the card's trick) is *dangerous*? What does that tell you about where JEPA's difficulty really comes from?
4. Name the **three ways to beat collapse** and give the one-line idea of each (contrastive · regularized/VICReg · distillation). Which one do real JEPAs use, and what are its two moving parts (**EMA target**, **stop-gradient**)?
5. Walk the ladder **I-JEPA → V-JEPA → V-JEPA 2 → V-JEPA 2-AC**. What does the final "-AC" step add, and why does that turn a passive video-watcher into a **world model you can plan with**?
6. Why is V-JEPA 2-AC's real-robot result the AP5 card's bet (and AP4's model-based branch) *made real* — and what does "**latent**" (not pixels) have to do with it?
7. The big one (Stuck #2): beating collapse proves the summaries carry *real information*. Why is that still not the same as having the **deep, plannable understanding** the bet needs — and which of the card's cracks does this sharpen?
8. Stuck #3: why can "throw away the unpredictable noise" also throw away the thing you most need to keep? Give the road/child example.

## Revision notes

*Newest first.*
- `rev 1 (2026-07-17)` — created as the **first AP5 deep-dive** (reading group **⑤ Deep dives**, sortkey 5005), branching off the [AP5 card](../20-the-approaches/05_ap5-world-models-jepa.md). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the card's *bet / world-model definition / planning-by-imagining / the JEPA "predict-the-summary-not-pixels" slogan / windy-leaves / animals-and-babies / world-models race / the four bet-cracks* are **referenced, never re-taught**; [AP4 · the engine](04_ap4-deep-dive-the-engine.md)'s *model-based RL / MuZero / DreamerV3 / plan-inside-a-model* is **pointed at, not retold** (V-JEPA 2-AC is framed as that branch realised in a learned latent space); the card's *hierarchical planning* (Stuck #3) and *generative-vs-non-generative* (Stuck #4) are referenced to the card. This page adds only the new **learning-engine** layer the card skipped: **self-supervised learning** (hide-and-predict; the same shape as next-word, but predicting in summary space — Part 1); **representational collapse** (the "constant vectors" cheat, and why summary-prediction invites it while pixel-prediction is safe — Part 2); the **three anti-collapse families** (contrastive/negatives · VICReg/variance-regularized · distillation with **EMA target** + **stop-gradient** — Part 3); the **I-JEPA → V-JEPA → V-JEPA 2 → V-JEPA 2-AC** lineage ending in a zero-shot, no-reward, **latent action-conditioned** world model planning a real robot (Part 4); and the **energy-based / objective-driven-AI (H-JEPA)** blueprint as a bridge back to the card's Stuck #3 (Part 5). Grounded in written, quotable sources — the **I-JEPA** paper (Assran et al., 2023 — "non-generative … from a single context block, predict the representations of various target blocks"), the **V-JEPA 2** paper (Meta, 2025 — the "understanding, predicting, and planning" ambition and the "<62 hours … latent action-conditioned world model, V-JEPA 2-AC" line), **VICReg** (Bardes, Ponce & LeCun, 2022 — "A trivial solution is obtained when the encoder outputs constant vectors" + the variance-regularization fix), and a corpus survey of contrastive SSL ("bring similar instances closer and push away dissimilar instances") — plus a full live-SOTA pass (**July 2026**), each fast fact dated: V-JEPA 2 / V-JEPA 2-AC (June 2025, >1M hours internet video, <62 hours Droid robot video, zero-shot Franka pick-and-place, 77.3 SSv2 / 39.7 R@5 Epic-Kitchens / 84.0 PerceptionTest / 76.9 TempCompass); the anti-collapse taxonomy (SimCLR/BYOL/DINO/VICReg); and **LeJEPA** (late 2025 — the first JEPA claimed to drop the heuristic anti-collapse guards, used as the Stuck #1 evidence that every prior JEPA leaned on a heuristic). Four **engine** cracks (distinct from the card's bet-cracks): collapse is beaten by **recipe not understanding** · a non-collapsed summary is **not deep understanding** (sharpens the card's Stuck #1 — perception wins, not planning) · you **don't choose what the abstraction discards** (predictable ≠ important — the rare-but-critical event) · **latent world models are hard to even score** (no pixels to check) — under the big question: *the engine solved the entry problem (learning from unlabelled reality), but the solved part is perception while the unsolved part is deep understanding and long-horizon planning.*

---
*This is the first AP5 deep dive — the **learning engine** beneath the "predict the abstract summary" slogan. Its self-supervision leans on [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md); its planning payoff realises [AP4 · the engine](04_ap4-deep-dive-the-engine.md)'s model-based branch; and its blueprint points back at the [AP5 card](../20-the-approaches/05_ap5-world-models-jepa.md)'s hierarchical-planning crack. To pick the next approach to go deep on, return to the [spine](../APPROACHES_TO_AGI.md).*
