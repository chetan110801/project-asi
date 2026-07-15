---
id: c-ap8-program-synthesis
sortkey: 2008
title: AP8 · Program synthesis & abstraction (ARC) — the "scale is climbing the wrong ladder" bet
domains: [frontier, approaches-to-agi]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap2-reasoning]
provides: [skill-vs-intelligence, measure-of-intelligence, arc-agi, core-knowledge-priors, program-synthesis, discrete-program-search, deep-learning-plus-program-search, program-fetching-vs-synthesis, active-inference-test-time-training]
resources: []
status: ready
reading_time: 34 min
rev: 1
created: 2026-07-15
updated: 2026-07-15
---

# AP8 · Program synthesis & abstraction (ARC) — the "scale is climbing the wrong ladder" bet

*This is the fifth big idea we look at for how to build a machine that can think in a general way — and it is the sharpest attack on the first one. The "make it bigger" bet ([AP1](01_ap1-scale-and-foundation-models.md)) says: pour in more data and more computer power, and a real mind will appear. This bet says the opposite: **you are climbing the wrong ladder.** No matter how big you make a text machine, you are only ever growing its **stored skill** — the pile of things it has already seen — and stored skill is not the same thing as **intelligence.** Real intelligence, on this view, is the power to handle a problem you have **never seen before**, using very little experience. Its champion is François Chollet, who built a special test — **ARC** — designed to measure exactly that, and to be almost impossible to beat by memorising. This page explains it all from zero: the bet in one minute, the key split between skill and intelligence, what ARC is, the road Chollet proposes instead of scale (**program synthesis**), why serious people take it seriously — and the four places it is stuck.*

> **You are here:** this is the **AP8** page — the eighth bet on the "approaches to AGI" map (see [APPROACHES_TO_AGI](../APPROACHES_TO_AGI.md)), and the fifth one written in full. AGI means *artificial general intelligence* — a machine that can think across many different problems, not just one. The short name for this idea is **program synthesis** (building a small program that solves a problem, by *searching* for it), and its measuring-stick is **ARC** — the *Abstraction and Reasoning Corpus*, a test of little puzzles built to resist memorising.
>
> **This page builds on four earlier rungs of the ladder**, all short and plain: [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — how today's AI works; [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the steady curve AP1 rides; [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) — the bet this one argues *against*; and [AP2 · the "think longer" bet](02_ap2-reasoning-and-test-time-compute.md) — which already mentioned ARC once. A one-line reminder of each is given where it is used, so you will not get lost. **AP8 is the deep home for one idea AP1 only touched: that skill is not intelligence.**
>
> **Where the facts come from:** the long 2024 conversation between Dwarkesh Patel and **François Chollet** (with Mike Knoop) — recorded the day they launched the $1 million ARC Prize, the fullest plain-spoken version of this bet on record. Quotes from it are exact. The durable root is Chollet's 2019 paper **"On the Measure of Intelligence."** Fresh check of the field, done on the web (**as of July 2026**): OpenAI's o3 result on ARC (Dec 2024), the launch of ARC-AGI-2 (2025) and ARC-AGI-3 (2026), and the 2025–26 ARC Prize competition results. Each fast-moving number is dated below.

---

## The bet in one minute

Here is the whole idea, as short as it goes.

**Today's biggest AI can pass hard exams, write code, and talk about almost anything. But show it a *simple* puzzle of a kind it has never seen, and it often fails — while a young child solves it at a glance. Chollet's claim is that this is not a small gap to be fixed by scale; it is the whole point. A big text machine is a giant *memory*: it stores an enormous number of patterns and, when you ask it something, it finds the closest stored pattern and reuses it. That is *skill* — being good at things you have practised. It is not *intelligence*, which is the power to face something genuinely new and work it out on the spot, from almost no examples. Growing the memory bigger makes it more skilful, not more intelligent. To get real intelligence, this bet says, you need a different engine: one that, for each new problem, *builds a small new program that solves it* — by searching for that program — instead of fetching a memorised one.**

Why believe skill and intelligence come apart? Because of one stubborn fact. Chollet built a test, ARC, out of little visual puzzles that a five-year-old finds easy but that need no special knowledge — only basic things like counting and "what is an object." He first released it in 2019. For years, as text machines grew a thousand-fold and beat every other test, ARC stayed nearly unbeaten by them. The puzzles are trivial for humans and hard for the machines — *precisely because* each one is new, and a memory cannot look up an answer it has never stored.

That is the bet. The rest of this page explains **why skill is not intelligence**, **what ARC is**, **the different engine Chollet proposes (program synthesis)**, **why it is a serious road**, and **why it might still be wrong.**

---

## First, a one-line reminder of the base

Three quick reminders from the rungs below, so this page stands on its own.

- From [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) and [AP1](01_ap1-scale-and-foundation-models.md): **today's main AI is a text machine trained to guess the next word** in billions of pages of human writing. Chollet describes what that produces in a sharp way — "a big interpolative memory" *(interpolative = filling in between things it has already seen; a memory that blends stored examples rather than reasoning from scratch)*. Hold that phrase; the whole card turns on it. *(New to you? Read those two rungs first; they are short.)*
- From [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): making the machine bigger makes its score climb in a steady, measured line — the **scaling laws.** AP1's bet is that this line leads to a mind. AP8 says the line leads only to more stored skill.
- From [AP2, the reasoning bet](02_ap2-reasoning-and-test-time-compute.md): we already saw ARC named once, when reasoning models spent extra computer power at answer-time to push their ARC score up. That was a passing mention; **this page is ARC's real home** — what it is, why it was built, and what it is trying to prove.

Now the one new idea this page adds. Every approach so far has argued about *how to train or run* a machine — copy text (AP1), think longer (AP2), learn from reward (AP4), model the world (AP5). AP8 steps back and asks a harder question: **what are we even measuring, and is it intelligence at all?** Its answer is that the whole field has quietly confused two different things — *skill* and *intelligence* — and that almost every famous benchmark measures the first while claiming to measure the second. To see why that matters, we start with the distinction itself.

---

## Part 1 — skill is not intelligence

This is the core of AP8's whole argument, so we go slowly.

Start with a benchmark almost everyone treats as a triumph. There is a grade-school-maths test called **GSM8K** — word problems a smart high-schooler could do. Today's models score about 95% on it. Surely, the story goes, a machine that does maths word problems is *reasoning*? Chollet says no — that is a **memorisation benchmark**. His reason cuts deep, and it rests on two different meanings of the word "reasoning":

> "There are two definitions you can use. One is, I have available a set of program templates … I'm going to identify the right template, which is in my memory, input the new values into the template, run the program, and get the solution … Here's another definition of reasoning. When you're faced with a puzzle and you don't already have a program in memory to solve it, it's the ability to synthesize on the fly a new program based on bits and pieces of existing programs that you have."
> *(François Chollet, Dwarkesh Podcast, 2024)*

("Program template" = a stored recipe for a *kind* of problem; you slot in the new numbers and run it. "Synthesize on the fly" = build a brand-new one, right now, that you did not already have.) Read the two side by side. The first is **fetching**: you recognise the problem type, pull the matching recipe from memory, and fill in the blanks. The second is **synthesis**: the problem is one you have *no* recipe for, and you must *make* a new recipe out of spare parts. Chollet's charge is that today's machines only ever do the first, and dress it up as the second:

> "It looks like reasoning but it's not really doing any sort of on-the-fly program synthesis. All it's doing is program fetching."
> *(Chollet, 2024)*

This "**fetching, not synthesis**" is the core accusation of the whole card. Everything else follows from it.

### The clearest example — the Caesar cipher

A *cipher* is a way of scrambling a message so only someone who knows the trick can read it. A **Caesar cipher** shifts every letter along the alphabet by a fixed number *n* — shift by 3 and A becomes D, B becomes E, and so on. It is a simple, exact rule that works for *any* shift. Chollet points out something revealing about how the machines handle it:

> "they can do it for a transposition length of like three or five, because those are very common numbers in examples provided on the internet. If you try to do it with an arbitrary number like nine, it's going to fail. It does not encode the generalized form of the algorithm, but only specific cases."
> *(Chollet, 2024)*

Sit with this. If the machine had truly *understood* the Caesar cipher — grasped the rule — the shift number would not matter at all; shifting by 9 is no harder than shifting by 3. But it works for 3 and 5 (which appear all over the internet) and breaks on 9 (which is rarer). **That is the sign of memory, not understanding.** It has stored the common cases as separate facts; it has not learned the one general rule that covers them all. A person who understands the cipher gets every *n* right, because they hold the *rule*, not a list of examples.

### What intelligence actually is, on this view

So if skill (stored, fetchable competence) is not intelligence, what is? Chollet's definition is precise, and it is worth learning by heart:

> "General intelligence is the ability to approach any problem, any skill, and very quickly master it using very little data … Generality is not specificity scaled up. It is the ability to apply your mind to anything at all, to arbitrary things."
> *(Chollet, 2024)*

("Specificity scaled up" = taking one narrow skill and just adding more and more narrow skills.) The key line is *"generality is not specificity scaled up."* Stacking a thousand memorised skills on top of each other never *becomes* generality, because there is an **infinite** space of possible problems, and any finite pile of skills covers **zero percent** of it. Generality is a different kind of thing: not a big collection of answers, but the **machine that makes a new answer when none of the old ones fit.** Chollet loves a line from the psychologist Jean Piaget that captures it: *"intelligence is what you use when you don't know what to do."* When you already know what to do, you are running memory. Intelligence only shows up in the face of the genuinely new.

And here is why this cannot be waved away as word-games. The reason a memory can never be enough is that **the world keeps changing**:

> "you can never pre-train on everything that you might see at test time because the world changes all the time … If our environment were static and predictable enough … evolution would have found the perfect behavioral program: a hard-coded, static behavioral program … But that's not what happened. Instead, we have general intelligence."
> *(Chollet, 2024)*

("Pre-train" = train ahead of time on stored data. "Static" = never changing.) This is a beautiful argument. Many insects run on **hard-coded programs** written into their genes — fixed responses that work because their world barely changes. Evolution gave *us* something different — general intelligence — precisely *because* our world does change, so no fixed set of stored responses could ever be enough. If a memory were sufficient, nature would have skipped the expensive brain and just written the answers into our genes. It didn't. That is the deepest evidence that intelligence is something *beyond* stored skill.

That is the distinction. Now — how do you *measure* it, so you can tell a memory apart from a mind?

---

## Part 2 — ARC: a test built to be memorisation-proof

Here is the move that makes AP8 concrete instead of philosophical. If almost every benchmark secretly rewards memory, then to measure *intelligence* you need a test that memory cannot beat. That test is **ARC**.

> "ARC is intended as a kind of IQ test for machine intelligence. What makes it different from most LLM benchmarks out there is that it's designed to be resistant to memorization … By contrast, ARC does not require a lot of knowledge at all. It's designed to only require what's known as core knowledge."
> *(Chollet, 2024)*

Two design choices make it work, and both matter.

**Choice 1 — every puzzle is new.** A single ARC puzzle looks like a child's IQ puzzle: you are shown a few example pairs — a small coloured grid "before" and the grid it should turn into "after" — and from those few examples you must work out the hidden rule, then apply it to a fresh grid. The catch is that **each puzzle uses a different rule, and the rule is not written anywhere on the internet.** So you cannot look it up. Whether you are a human or a machine, you have to face each puzzle from scratch and figure out its rule yourself. A memory has nothing to fetch.

**Choice 2 — it needs only "core knowledge," not learning.** ARC deliberately avoids school knowledge, trivia, or language. All it assumes is **core knowledge** — the handful of basic ideas every young child already has:

> "It's basic knowledge about things like elementary physics, objectness, counting, that sort of thing. It's the sort of knowledge that any four-year-old or five-year-old possesses."
> *(Chollet, 2024)*

("Objectness" = the sense that the world is made of separate objects — a thing you can point at, that stays one thing when it moves.) This is what makes the result so striking. The puzzles need almost no knowledge, so a machine's vast store of internet facts gives it *no advantage*. What is left is pure on-the-spot problem-solving — exactly the thing Chollet says is intelligence. And on exactly that, the biggest machines have long struggled while children breeze through: an average person scores about **85%**, and a smart human 90–95%, but for years the top text machines scored close to zero.

**Why "abstraction and reasoning."** The full name — the *Abstraction and Reasoning Corpus* — names the two skills it forces. *Abstraction* = seeing the general pattern behind the specific coloured squares ("the shape got copied and flipped"), not the squares themselves. *Reasoning* = using that pattern to produce the new answer. Both must happen fresh, per puzzle, from two or three examples. That is the "very little data" from Chollet's definition, made into a test.

Behind ARC sits Chollet's 2019 paper, *"On the Measure of Intelligence,"* which gave the field a new yardstick. As Mike Knoop put it, the paper argued that **"this efficiency of skill acquisition is the right definition"** of intelligence — not *how much* skill you have, but *how fast and cheaply you can pick up a new one.* ARC is that definition turned into a scoreboard: not "how many things can you already do?" but "how well do you handle something you were never prepared for?"

So ARC is the measuring-stick. But a good test that everyone fails is only half an idea. Chollet also proposes *how* to build a machine that could pass it — and that is a genuinely different engine.

---

## Part 3 — the road not taken: deep learning + program synthesis

This is AP8's constructive bet — its answer to "so what should we build instead?" It rests on contrasting two very different ways for a machine to learn. Take them one at a time.

**Engine A — deep learning (what today's AI is).** In the AI of AP1, the machine is, in Chollet's words, "a differentiable parametric curve" — a giant smooth mathematical shape with billions of adjustable knobs, bent to fit the data *(differentiable = smooth enough that you can nudge each knob a tiny bit and see the score improve; parametric = defined by those adjustable numbers)*. It is trained by **gradient descent** — a step-by-step downhill walk that keeps nudging the knobs to lower the error *(you met this idea as the "steady downhill" of training in the base rungs)*. Its strengths and weaknesses are exact opposites of Engine B:

> "Gradient descent is very compute efficient … but it is very data inefficient. In order to make it work, you need a dense sampling of the … data distribution. Then you're limited to only generalizing within that data distribution."
> *(Chollet, 2024)*

("Compute efficient" = cheap in computer power. "Data inefficient" = needs a *huge* pile of examples. "Generalizing within that data distribution" = it only handles things close to what it has already seen.) So: fast to run, but hungry for data, and trapped near its training examples — good at the familiar, weak on the new. This is why it wins every memorisation test and loses on ARC.

**Engine B — program synthesis (what Chollet proposes).** Here the machine does not bend a curve. It **builds a little program.** You give it a small box of basic operations — a *domain-specific language*, or **DSL** *(a tiny toolkit of allowed commands, like "rotate," "count," "recolour")* — and it **searches** for a way to snap those commands together into a program that turns each example's "before" into its "after." Its strengths and weaknesses are the mirror image:

> "the learning engine is combinatorial search. You're just trying a bunch of programs until you find one that actually meets your spec. This process is extremely data efficient. You can learn a generalizable program from just one example, two examples … The big limitation is that it's extremely compute inefficient because you're running into combinatorial explosion."
> *(Chollet, 2024)*

("Combinatorial search" = trying many combinations. "Combinatorial explosion" = the number of possible programs grows so fast — a program two steps longer has vastly more possibilities — that trying them all becomes impossible.) So: it can learn a true, general rule from **one or two examples** (exactly what ARC demands), but the searching gets impossibly expensive as programs get longer. **This is why program search, not scale, has led on ARC** — it is built for learning-from-almost-nothing.

Now the punchline. Look at the two lists: every weakness of one engine is a strength of the other. Deep learning is data-hungry but fast; program search is data-thrifty but slow. Chollet's proposal is therefore not "throw out deep learning" but **marry the two:**

> "You can sort of see here how deep learning and discrete program search have very complementary strengths, and limitations as well. Every limitation of deep learning has a corresponding strength in program synthesis and inversely. The path forward is going to be to merge the two."
> *(Chollet, 2024)*

How do you merge them? Program search's one great weakness is the explosion — too many possible programs to try. Deep learning's one great strength is **intuition** — instantly sensing which few options are worth looking at. So you let a deep-learning model be the **guide** that steers the search, cutting the explosion down to a handful of promising guesses:

> "You're actually going to ask another deep learning model for suggestions. It'll be like, 'here's the most likely next step. Here's where in the graph you should be going' … Discrete program search is going to be the key but you want to make it dramatically better, orders of magnitude more efficient, by leveraging deep learning."
> *(Chollet, 2024)*

Chollet ties this to the famous split between **System 1 and System 2** thinking *(System 1 = fast, automatic, gut-feel thinking; System 2 = slow, effortful, step-by-step thinking — a picture you met in [AP2](02_ap2-reasoning-and-test-time-compute.md))*. Deep learning is a perfect System 1 — a pattern-and-intuition machine. Program search is System 2 — deliberate, step-by-step working-out. Today, he says, "we have all the tools for System 1. We have almost nothing for System 2." The way forward is a **hybrid**: deep-learning intuition on the outside, guiding real program search on the inside. **That is AP8's actual construction bet — not "scale is bad," but "scale is only half a mind; the missing half is search."**

---

## Why this is a serious idea, not one man's hunch

Three legs hold it up.

### Leg 1 — ARC survived the scaling wave, for years

The strongest evidence is simply that **the test worked as designed.** Chollet released ARC in 2019, before the text-machine boom. Then the machines grew a thousand-fold and scored near the top on test after test — grade-school maths, professional exams, coding tests — the whole field's measuring sticks fell one by one. ARC did not. Mike Knoop, a successful tech founder, was so struck by this that he quit his executive job to work on it:

> "When I looked at the scores and the progress over the last four years, I was really shocked to see that we'd made very little objective progress towards it … If it's right that this is a really globally, singularly unique AGI eval … then more people should know about this thing."
> *(Mike Knoop, Dwarkesh Podcast, 2024)*

That a memory-resistant test *stayed* hard while every memory-friendly test fell is not proof of Chollet's whole theory, but it is exactly what his theory predicts — and it is a real, measured fact, not an opinion. **[Established — ARC's multi-year resistance to scaling is a documented result.]**

### Leg 2 — the approaches that work on ARC are program search, not scale

This is the concrete leg. When teams *do* score on ARC, the winning methods are not "a bigger text machine." They are the two things AP8 predicts: **program search** and **adapting the model to each puzzle on the spot.** Chollet, in 2024, described the state of the art as sitting at the two ends of one spectrum — pure discrete program search over a tiny toolbox at one end, and, at the other, a small model that does **test-time fine-tuning**:

> "What Jack Cole is actually doing is that for every test problem, it's on-the-fly fine-tuning a version of the LLM for that task. That's really what's unlocking performance. If you don't do that, you get like 1-2%, something completely negligible."
> *(Chollet, 2024)*

("Test-time fine-tuning" = instead of freezing the model and just asking it, you let it *learn a little from the specific puzzle in front of it* before answering.) Chollet calls this adding **active inference** — letting the model actually *adapt on the fly*, the very thing frozen text machines cannot do. He is blunt that this is program synthesis in disguise: fine-tuning on the task "is effectively a form of program synthesis … you are trying to assemble these building blocks into the right pattern that matches the task." So the methods that actually raise the ARC score are precisely the ones AP8 points to — search and on-the-spot adaptation — not raw scale. **[Established — the leading ARC methods are program-search and test-time-training based, confirmed again in the 2025–26 results below.]**

### Leg 3 — better data can't fix a worse architecture

The last leg answers the obvious rescue: "won't the machines just get there with more data?" Chollet's reply reaches for the clearest natural example — differences in intelligence between *people*:

> "There is extensive evidence that differences in intelligence are mostly genetic in nature. That means that if you take someone who is not very intelligent, there is no amount of training data you can expose that person to that would make them become Einstein. This points to the fact that you really need a better architecture. You need a better algorithm. More training data is not in fact all you need."
> *(Chollet, 2024)*

("Architecture" = the underlying design of the system; "algorithm" = the method it runs.) The logic transfers cleanly to machines: if, even in humans, *more experience* cannot turn an ordinary mind into a great one — if the difference is in the *design* — then the lesson for AI is that a better **design** matters more than a bigger **pile of data.** And this fits Chollet's long-held two-part position, which he has held for years and which has aged well: *"if you keep scaling up deep learning, it will keep paying off … [and] if you keep scaling up deep learning, this will not lead to AGI."* Scaling is genuinely useful — and, he bets, genuinely not the road to a general mind. **[Likely / contested — the human-intelligence-is-architectural claim is real but debated; its transfer to AI is a bet, not a proof.]**

---

## So what does AP8 say intelligence is?

Pulling the legs together, here is AP8's answer to *"what is intelligence?"*:

- **Intelligence is** *skill-acquisition efficiency* — how well and how cheaply you handle a problem you were **never prepared for**, using **very little data**. Not how much you already know; how fast you learn the genuinely new.
- **What it optimises** is solving **unseen** tasks from **one or two** examples — which is why its test (ARC) forbids memorising and its engine (program synthesis) can learn a rule from almost nothing.
- **Its claim about the missing piece:** what AP1 lacks is not size but a **second engine.** A text machine is a huge, powerful memory (System 1); a mind also needs the power to *build a new program on the spot* for a problem it has never met (System 2, via guided search). Add that, and you cross from skill to intelligence.

That is the bet. Now let us judge it.

---

## Judging the bet: where it is stuck

Be fair first. AP8 has arguably the sharpest single idea in the whole field — *skill is not intelligence* — and the only benchmark built honestly to catch the difference, plus a concrete, non-mystical proposal (guided program search) for crossing the gap. Hold that. Now the four places it is truly stuck.

### Stuck #1 — program search explodes, and nobody knows where the priors come from

AP8's own engine has a severe weakness, and Chollet names it himself: **combinatorial explosion.** Searching for a program works beautifully for tiny problems, but the number of possible programs grows so fast that, past a few steps, no computer could try them all. His fix is to have deep learning *guide* the search — but that only relocates the hard part. To guide a search well, the guide needs strong **priors** *(priors = built-in leanings about which answers are likely, before you look — a sense of what "usually" works)*. Where do those broad, human-like priors come from? Chollet does not have a full answer, and neither does anyone else. Humans seem to arrive with a small set of core priors and grow the rest; how to give a machine priors general enough to tame the search across *any* new problem is **unsolved.** So AP8 trades AP1's problem ("scale doesn't reach intelligence") for its own, equally hard problem ("search doesn't scale without priors we can't yet build"). **[Established as the central open problem of the program-synthesis route.]**

### Stuck #2 — a machine *did* beat the first ARC, and it looked a lot like scale

This is the sharpest turn in the story, and honesty demands it lead. In June 2024 Chollet said he was "pretty skeptical that we're going to see an LLM do 80% in a year." **About six months later he was proven wrong.** In December 2024, OpenAI's o3 model scored **75.7%** on the semi-private ARC-AGI-1 test at low compute and **87.5%** at high compute — passing the ~85% human average for the first time *(as of Dec 2024; "semi-private" = a held-back test set)*. By early 2026, frontier models reached roughly **98%** on ARC-AGI-1. The original ARC is, for practical purposes, beaten.

Now, *which side does this vindicate?* Both can claim it, and that is what makes it interesting.

- **Chollet's reading (search won):** o3 did not win by being a bigger frozen text machine. It won by spending enormous computer power *at answer-time*, exploring many chains of thought and checking them — which is precisely the [test-time compute](02_ap2-reasoning-and-test-time-compute.md) idea from AP2 *(spend computer power while answering, not just while training)*, and it behaves like the guided-search System 2 that AP8 called for. On this reading, the machines beat ARC by finally adding the *second engine*, exactly as AP8 said they must.
- **The scaling reading (brute force won):** o3's high-compute run cost on the order of **$3,500 per puzzle** — thousands of dollars to solve a task a child does for free in seconds. If "intelligence is *efficiency*," paying thousands of dollars per puzzle is closer to brute-forcing the answer than to thinking. And a big text model still sat underneath it all. On this reading, scale-plus-search forced its way through a test that was supposed to need real intelligence.

The honest verdict is that o3 **both** confirmed AP8 (you needed search, not just scale) **and** dented it (the search was hugely expensive, and rode on a giant scaled model). Chollet's own move was telling: rather than declare ARC broken, he **built a harder one.** **[Contested — o3's ARC-AGI-1 result is real and dated (Dec 2024); what it *means* is the live dispute.]**

### Stuck #3 — is ARC measuring intelligence, or just today's blind spot?

Here is the uncomfortable pattern. ARC-AGI-1 held for five years, then fell. In 2025 the team launched **ARC-AGI-2**, rebuilt to be harder (more steps, combining several ideas per puzzle) — and the scores dropped hard again: as of the ARC Prize's end-of-2025 results, the best *verified* frontier model (Anthropic's Opus 4.5) reached only about **37.6%**, and the best entry in the efficiency-capped competition track about **24%**, while humans still solve essentially all of it *(a typical person scores ~60%, and every task has been solved by at least two people; as of 2025–26)*. Then in 2026 came **ARC-AGI-3**, harder still, where frontier AI scores **under 1%** and humans score 100%.

This raises a real worry, and the critics press it. Each ARC version is beaten, then a new one restores the gap. Is ARC measuring some *stable, real* thing called intelligence — or is it just a moving marker that points at **whatever today's models happen to be bad at**, redrawn each time they catch up? If the test has to keep changing to stay unbeaten, maybe it is tracking the *machines' current weaknesses* rather than a fixed target. Chollet's reply is that each version is imperfect and the *definition* (efficiency on novelty) is what is stable, not any one puzzle set. But "we keep having to make a harder test" is a genuine soft spot in the claim that ARC pins down intelligence once and for all. **[Contested — a real, live objection; the versions-keep-falling pattern is documented.]**

### Stuck #4 — even a solved ARC might not be AGI (and Chollet agrees)

The last crack is one AP8 itself concedes. Suppose someone builds a system that solves ARC honestly — from core knowledge, not by memorising millions of ARC-like puzzles. Would that be AGI? Chollet says **no** — only a milestone on the way:

> "Let's say we end up with a solution that is not like trying to brute force the space of possible ARC tasks … I don't think it's necessarily going to be in and of itself AGI, but it's probably going to be a huge milestone on the way to AGI."
> *(Chollet, 2024)*

And there is a deeper doubt underneath. ARC's puzzles are tiny, tidy, coloured grids that need only core knowledge. Real-world novelty is vastly larger, messier, and full of the knowledge ARC deliberately strips out. A machine that solved these small grid puzzles might still fail at *open-world* novelty — the kind Chollet elsewhere calls handling "a fair amount of novelty in every hour of every day." So even a clean ARC win would leave the biggest question open: does grid-puzzle intelligence *transfer* to the genuine, unbounded novelty of the real world? **[Contested — ARC is a narrow, deliberately simplified probe; that solving it yields general intelligence is unproven.]**

### The big question under all of these

Every doubt above is one question: **is Chollet drawing a real, permanent line — skill on one side, intelligence on the other — or a temporary line that scale keeps stepping over?** AP8 says the line is real and deep: no amount of stored skill *becomes* the power to handle the truly new, so a second engine (guided program search) is required. The other side says the line keeps *moving* — o3 crossed ARC-AGI-1, each new version gets crossed in turn, and the "second engine" (test-time search) turned out to be something you bolt onto a big scaled model, not a rival to it. And note the twist that ties AP8 to its siblings: the thing that finally beat ARC-AGI-1 was **AP2's test-time compute running on top of an AP1 model** — so AP8's own predicted cure arrived *inside* the approaches it set out to refute. So the live 2026 question is whether program synthesis is **a separate road to AGI**, or — like the doubts that dog [AP2](02_ap2-reasoning-and-test-time-compute.md) and [AP4](04_ap4-rl-from-interaction.md) — **a crucial missing *part* that ends up bolted onto the scaled models of AP1.** *As of July 2026, this is genuinely open,* and it is one of the most clarifying arguments in the whole field. **[Contested — the key open question.]**

---

## ⚠️ Honesty box

- **The distinction is stronger than the cure.** *Skill is not intelligence*, and ARC's memory-resistance, are sharp and widely respected — they reframed how the field thinks about measuring progress. The proposed fix — deep-learning-guided program synthesis that scales — is far less proven; its own engine still explodes without priors nobody knows how to build (Stuck #1). Keep the strong critique apart from the unproven remedy. **[Contested.]**
- **Chollet made a bold, dated prediction and it missed — that counts.** He doubted an LLM would hit 80% on ARC-AGI-1 within a year; o3 did it in about six months (Stuck #2). His deeper claim ("that isn't *efficient*, general intelligence") may still hold, but the specific forecast was wrong, and an honest account says so. **[Established.]**
- **"We keep needing a harder test" cuts both ways.** That each ARC falls and a new one restores the gap can mean the machines still lack real fluid intelligence (Chollet's reading) *or* that ARC tracks a moving blind spot rather than a fixed target (the critics' reading). Do not treat either reading as settled (Stuck #3). **[Contested.]**
- **Solving ARC ≠ AGI — by Chollet's own admission.** ARC is a narrow, simplified probe of one crucial ability, not a full test of a mind (Stuck #4). A high ARC score would be a milestone, not a finish line; demand evidence that grid-puzzle skill *transfers* to open-world novelty. **[Likely.]**
- **Numbers and names age fast.** The o3 result, the ARC-AGI-2 and -3 scores, the 2025–26 competition winners — these are 2019–2026 snapshots. The lasting parts are the **distinction** (skill vs intelligence), the **definition** (intelligence = efficient skill-acquisition on novelty), the **test idea** (memory-resistant, core-knowledge-only), the **two engines** (curve-fitting vs program search) and their **merger**, and the **four cracks.** The scores around them will change.

---

## How to use this (if you want to direct AI work)

- **First question about any "reasoning" claim: is it fetching or synthesising?** When a model scores high on a benchmark, ask whether that task type appears all over its training data (then it may be *fetching* a stored recipe) or is genuinely novel to it (then it may be *synthesising*). The Caesar-cipher test is the model in miniature: does performance hold on the *rare* variant, or only the common one? If it breaks on the uncommon case, it was fetching from memory, not truly reasoning.
- **Separate "how skilful" from "how general."** A system can get more useful — wider coverage, higher scores — without getting one bit more able to handle the truly new. When someone sells "it's getting smarter," ask whether they mean *more stored skill* (usually true, and valuable) or *more power on unseen problems* (much rarer, and the thing that matters for AGI).
- **Watch efficiency, not just the score.** ARC's whole point is *cheap* skill-acquisition. A benchmark "solved" at thousands of dollars and a giant search per task tells you more about brute force than about intelligence. Always ask what a result *cost* — per task, in compute and money — before calling it a step toward a general mind.
- **For genuine novelty, look for the second engine.** If a problem truly needs handling the unseen from few examples, ask where the *search* is — the part that builds a new solution rather than retrieving one. A frozen model that only pattern-matches will do "local" generalisation; crossing to broad generalisation needs some form of on-the-spot construction (search, or test-time adaptation).
- **Treat ARC as a lens, not a scoreboard.** Its most useful gift is the *question* — "could this system handle a simple thing it has never seen?" — not the exact percentage. Use the question on any AI you are judging; it cuts through demos faster than any leaderboard.
- **What you hand to others:** running the training, building the DSL, tuning the search. **What you keep for yourself:** telling fetching from synthesis, refusing to confuse a high score with intelligence, watching the *cost* of a result, and knowing that the deepest part — priors general enough to tame the search — is still unsolved (Stuck #1).

---

## Connections

- **Keep only three things:** ① AP8 = **skill is not intelligence.** A big text machine is an *interpolative memory* that *fetches* stored recipes; real intelligence is *skill-acquisition efficiency* — building a **new** solution for a problem you have **never seen**, from **very little data**. ② Its test is **ARC** — little puzzles built to resist memorising (each one novel; needs only a child's *core knowledge*), and its proposed engine is **program synthesis guided by deep learning** — merge System 1 (fast curve-fitting intuition) with System 2 (slow, deliberate program search). ③ It is stuck on four cracks: **program search explodes without priors nobody can yet build**, **o3 beat ARC-AGI-1 (part search, part expensive scale)**, **each ARC version falls then a harder one restores the gap**, and **even a solved ARC would not be AGI** (Chollet agrees).
- **Down the ladder (already read):** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) · [scaling laws & the data wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md) — the interpolative memory AP8 says is only half a mind.
- **Its siblings:** [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md) is the one AP8 attacks head-on — AP8 is the **deep home** for the *"skill is not intelligence"* line AP1 only touched. And the twist: what beat ARC-AGI-1 was [AP2 · test-time compute](02_ap2-reasoning-and-test-time-compute.md) running on an AP1 model — so AP8's own cure showed up *inside* its rivals.
- **The ideas it leads to** (still to be written): AP7 (neurosymbolic — the general family of "fuse learning with explicit structure/search," of which AP8 is the ARC-focused case), AP9 (open-endedness — where do broad priors *come from*? maybe an endless generating process), and AP6 (brain-based — how the one working mind we have gets its priors). See the [map](../APPROACHES_TO_AGI.md).
- **How sure are we?** *Skill ≠ intelligence*, ARC's memory-resistance, and program search leading on ARC — **[Established / Likely]**. That guided program synthesis *scales* to general intelligence, that ARC pins intelligence down for good, that solving ARC yields AGI — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Say the AP8 bet in one plain sentence, using the words *skill*, *intelligence*, and *novel*.
2. Explain the difference between **program fetching** and **program synthesis** in your own words. Which one does Chollet say today's models do?
3. Use the **Caesar cipher** example: why does "works for shift 3 and 5, fails on shift 9" show *memory* rather than *understanding*?
4. What two design choices make **ARC** resistant to memorising? (Think: *novel* + *core knowledge*.)
5. Deep learning and program search have opposite strengths. Name one strength and one weakness of each, and say how Chollet wants to **merge** them.
6. In December 2024, o3 scored 87.5% on ARC-AGI-1. Give **both** readings — why it *confirms* AP8, and why it *dents* AP8. (Stuck #2.)

## Revision notes

*Newest first.*
- `rev 1 (2026-07-15)` — created as the **AP8** deep-dive, the fifth approach card written (badge = AP index; the `06`/`07` slots stay open for the still-unwritten AP6/AP7). Built to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)). Placed as a new rung that **builds on** [next-word](../10-how-ai-works-today/01_guessing-the-next-word.md), [scaling/data-wall](../10-how-ai-works-today/02_scaling-laws-and-emergence.md), [AP1](01_ap1-scale-and-foundation-models.md), and [AP2](02_ap2-reasoning-and-test-time-compute.md) with short reminders-and-links; it is the **deep home for the "skill is not intelligence" idea** AP1 only touched (no re-teach — AP1's Chollet mention and AP2's test-time-compute are referenced, not repeated; ARC's real home is here). Grounded verbatim in the Dwarkesh × Chollet 2024 conversation (fetching-vs-synthesis, the two definitions of reasoning, the Caesar-cipher fingerprint, the definition of generality, the static-world/insects argument, ARC's design and core knowledge, the deep-learning-vs-program-search contrast and their merger, System 1/System 2, test-time fine-tuning / active inference, the genetics-not-data argument, "scaling pays off but won't reach AGI," and Chollet's own "solving ARC ≠ AGI") + Knoop on *"On the Measure of Intelligence"* (skill-acquisition efficiency). Full live-web freshness pass (July 2026): o3's ARC-AGI-1 result (75.7% / 87.5%, ~$3.5k/task, Dec 2024) and the ~98% frontier by early 2026; ARC-AGI-2 (2025, best verified frontier ~37.6% Opus 4.5, efficiency-track ~24%, humans ~60%); ARC-AGI-3 (2026, frontier <1%, humans 100%); the 2025–26 competition confirming program-search + test-time-training as the winning methods — each dated and source-graded, with the o3 result surfaced as the central corpus-vs-current tension (Stuck #2).

---
*This is the fifth approach page written. Its chief rival is [AP1 · the "make it bigger" bet](01_ap1-scale-and-foundation-models.md); the twist is that [AP2 · test-time compute](02_ap2-reasoning-and-test-time-compute.md) is what beat its first test. The ideas it leads to are on the [map](../APPROACHES_TO_AGI.md). To see the interpolative memory it says is only half a mind, read [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md).*
