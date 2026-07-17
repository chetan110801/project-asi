---
id: c-measure-of-intelligence
sortkey: 5001
title: AP8 · Deep dive — the formal theory of intelligence (Chollet's *Measure of Intelligence*)
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-scaling-laws, c-ap1-scale, c-ap8-program-synthesis]
provides: [skill-acquisition-efficiency-formula, generalization-difficulty, priors-experience-axis, generalization-spectrum, system-centric-vs-developer-aware, core-knowledge-four-systems, algorithmic-information-theory-basis, no-universal-intelligence-anthropocentric-scope]
resources: []
status: ready
reading_time: 32 min
rev: 1
created: 2026-07-16
updated: 2026-07-16
---

# AP8 · Deep dive — the formal theory of intelligence (Chollet's *Measure of Intelligence*)

*This is the first **deep dive**: an optional side-branch that goes **past** an approach card, one level deeper, toward the depth a researcher needs. The [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md) told you Chollet's one-line answer to "what is intelligence?" — **skill-acquisition efficiency**: how well you handle a problem you were never prepared for, from very little data. That one line is the tip of a whole machine. Underneath it is an actual **definition-as-a-formula** — the real content of Chollet's 2019 paper *"On the Measure of Intelligence."* This page opens that machine up: the exact quantity the formula measures, the four parts it is built from, how each part is *measured* (using the length of the shortest program), the **ladder of generalization** it lays out (from none, up to human-level), the **four innate "core knowledge" systems** it assumes, and the fight it picks with the field's other definition of intelligence. Everything the card already said — skill-vs-intelligence, fetching-vs-synthesis, the Caesar cipher, what ARC is, the two engines — is **not repeated here**; it is linked. This page adds only what is new: the theory beneath the slogan.*

> **You are here:** this is a **deep-dive module** — reading group **⑤**, the optional layer that sits *below* the main staircase. The main map (① how AI works → ② the eleven approaches → ③ across them → ④ the verdict) is the trunk; deep dives are branches you climb only when you want the full depth of one idea. This one branches off **[AP8 · program synthesis & ARC](../20-the-approaches/08_ap8-program-synthesis-arc.md)**. *Read the AP8 card first* — this page assumes it.
>
> **What the card already gave you (a one-line reminder each, then we move on — this page does not re-teach them):** **skill ≠ intelligence** (stored, fetchable competence is not the power to handle the truly new); **fetching vs synthesis** (pull a stored recipe vs build a new one on the spot); the **Caesar-cipher** fingerprint (works on the common case, breaks on the rare one → memory, not understanding); **ARC** (little grid puzzles built to resist memorising); and the **two engines** (deep-learning curve-fitting vs program search) and their merger. All of that lives on the [card](../20-the-approaches/08_ap8-program-synthesis-arc.md). **New here:** the *formula* those slogans are a summary of.
>
> **Where the facts come from:** Chollet's 2019 paper **"On the Measure of Intelligence"** (arXiv 1911.01547 — freely available; the durable primary source), read alongside the **Machine Learning Street Talk** deep-dive on that paper (in the corpus), which opens with a clip of Chollet stating the definition in his own spoken words. Quotes from the paper and the clip are exact. A fresh web check (**as of July 2026**) dates how the theory has held up — the efficiency idea, ARC-AGI-2's cost-scored leaderboard, and Chollet's new lab.

---

## In one minute

The [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md) said intelligence is *skill-acquisition efficiency*. That sounds nice, but a slogan is not a measurement. If you want to actually **test** a machine and get a number, you hit a hard wall right away, and the whole paper is built to climb it. Here is the wall, and the climb, as short as it goes.

**The wall: you can never measure "intelligence" directly — you can only ever measure *skill* (how well a system does a task). And skill is cheap: you can *buy* any amount of it two ways — pour in more built-in knowledge (**priors**), or pour in more practice data (**experience**). Both raise the score while telling you *nothing* about whether the system could handle something new. So a raw score is worthless as a measure of a mind.**

**The climb: Chollet's fix is to stop measuring the score and start measuring the *conversion rate* — how much brand-new problem-solving the system squeezed out of how little prior knowledge and how little practice. Write it as a fraction. On top: how far the system had to jump from what it was trained on to what it was tested on (the *generalization difficulty*). On the bottom: everything it was handed for free (its priors *plus* its experience). A big top over a small bottom = real intelligence. A big score bought with a huge bottom = just expensive skill. Do this across a whole *range* of tasks (a *scope*), not one, and you have a measure. That fraction — difficulty of the jump, divided by what you were given — is the formal theory of intelligence.**

That is the engine under the card's slogan. The rest of this page names each part, shows how you'd measure it, and lays out the ladder of "how big a jump" that runs from a pocket calculator up to a human child.

---

## One line of base, then we build

Just one reminder from the card, because the whole page turns on it.

- From the [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md): Chollet's slogan is *"generality is not specificity scaled up"* — stacking more stored skills never *becomes* the power to face the genuinely new. Intelligence is **skill-acquisition efficiency**: handling an **unseen** task from **little data**. *(New to this? Read the card's Part 1 first — this page assumes it and will not re-explain it.)*

The card gave you that as a **slogan**. This page gives you the same idea as a **measurement** — which is a very different, and much harder, thing. A slogan you can nod at; a measurement you have to defend against every cheat. Watch how Chollet defends it.

---

## Part 1 — the wall: skill is all you can measure, and skill can be bought

Start with the honest, uncomfortable fact that the whole theory is a response to. When you test any system — a person, a chess program, a chatbot — the only thing your test can actually read off is **skill**: how well it did the task in front of it. You cannot open it up and read a dial marked "intelligence." As the MLST panel put it while working through the paper, *"the only thing we can really assess is how well you do at a particular task."* Skill is the only observable. Intelligence is not.

That would be fine if skill were a good stand-in for intelligence. It is not — because skill can be **bought**, cheaply, in two completely different ways that both fake it:

- **Buy it with priors.** *Priors* *(prior knowledge — everything built into the system before it sees any task; its head start)* can be cranked up until the task is trivial. Hand-code enough of the answer and a system "succeeds" while doing no thinking at all. A pocket calculator has huge built-in priors about arithmetic; it is not intelligent.
- **Buy it with experience.** *Experience* *(the practice data the system is trained on — every example it gets to learn from)* can be cranked up instead. Show a system enough examples and it can memorise its way to a high score on anything, again without any power to handle a case it has not seen. This is the card's *"interpolative memory"* charge, made general.

Chollet's word for this is that priors and experience let you **"buy" arbitrary levels of skill in a way that masks the system's own generalization power.** *(Generalization power = the ability to handle new cases, not just the trained ones.)* This is the key move of the whole paper, so say it slowly: **a high score can come from real intelligence, or from a big pile of priors, or from a big pile of experience — and from the outside they look identical.** A benchmark that just reports the score cannot tell them apart. That is why almost every famous benchmark, as the card argued, secretly rewards memory.

So the panel drew the picture as an **axis** *(a line with a trade-off along it)*: you can buy skill with lots of **priors**, or buy the very same skill with lots of **experience** — and neither of those is intelligence. Both ends of that line are cheats. Intelligence is not anywhere *on* the line; it is what is left over *after* you subtract out what the priors and the experience already gave you.

That "what is left over after you subtract the free stuff" is the seed of the formula. Chollet says it plainly in the clip that opens the corpus video:

> "I think intelligence is essentially the efficiency with which you turn experience into generalizable programs."
> *(François Chollet, spoken, Machine Learning Street Talk, 2020)*

("Generalizable programs" = little procedures that keep working on new cases, not just the ones you practised on — the same *synthesis* idea from the card.) Read it as a **rate**: *experience in → general skill out*, and intelligence is the **efficiency** of that conversion. A system that turns a *little* experience into a *lot* of transferable skill is intelligent. A system that needs a *mountain* of experience to get the same skill is not — it is just a good memory with a big enough shelf. Now we make "efficiency of that conversion" exact.

---

## Part 2 — the formula: intelligence as a conversion rate

Here is the paper's one-sentence definition, verbatim. Do not be scared by it; we take it apart word by word right after.

> "The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty."
> *(Chollet, "On the Measure of Intelligence," 2019)*

Four words in that sentence are doing all the work: **scope**, **generalization difficulty**, **priors**, **experience**. Take them one at a time.

- **Scope** — *the range of tasks you measure over, not a single task.* Intelligence is never about one job; a chess engine that is unbeatable at chess and helpless at everything else is skilled, not intelligent. So the measure averages a system's performance across a **whole set of tasks** — and, crucially, tasks the system was **not** built for one by one. (Which set of tasks? That choice is a fight of its own — see Part 6.)

- **Generalization difficulty** — *how big a jump the system had to make from what it was trained on to what it was tested on.* This is the **top** of the fraction, and it is the heart of the whole thing. If the test looks almost exactly like the training, the jump is tiny — difficulty near zero — and a high score means nothing. If the test is genuinely new, and the training only got you part-way there, the jump is large. The panel described the paper's picture like this: *"if you have a problem that's this hard, and your prior knowledge and all your experience today only get you this far, the difference is what you have to use intelligence for."* That **difference** — the gap the free stuff could *not* cover — is generalization difficulty. It is the part where thinking actually had to happen.

- **Priors (P)** — *everything built in before any task: the system's innate head start.* The bottom of the fraction, part one.

- **Experience (E)** — *all the practice data the system consumed while learning the task.* The bottom of the fraction, part two.

Put them together and the definition is, in plain words, a **fraction averaged over the scope**:

::: key
For each task in the scope, take **how hard the jump was** (generalization difficulty) and divide it by **how much you were handed for free** (priors **+** experience). Average that over all the tasks. High = intelligent (big jumps from little given); low = not (small jumps, or big jumps only because you were given a fortune of priors or practice).
:::

Two subtleties make this sharper than it first looks.

**One: priors and experience are *added together* on the bottom — the formula does not care which one you used.** As the panel noticed reading the paper: *"in the measure of intelligence, the formula — it's prior *plus* experience; nowhere in the formula is the prior by itself or the experience by itself."* This has a striking consequence. It means the age-old **nature-versus-nurture** question *(is an ability built in, or learned? — "nature" = born with it, "nurture" = picked it up)* **does not matter to the measure at all.** A skill you were born with and a skill you drilled a million times both go on the bottom as "stuff you were given." Only the *left-over jump* counts. Intelligence is defined as exactly the part that is **neither** innate **nor** rehearsed.

**Two: this is why it is called *efficiency*.** A fraction of "output jump" over "input given" is a **conversion rate** — output per unit of input, exactly like *miles per gallon* for a car. Two cars can go the same distance; the efficient one did it on less fuel. Two systems can reach the same skill; the intelligent one did it on fewer priors and less experience. The score (distance travelled) is not the measure. The **efficiency** (distance per fuel) is. This is the exact meaning of the card's slogan "skill-acquisition efficiency" — now you can see it is a literal ratio, not a vague feeling.

So far this is a definition in words. But a fraction is only useful if you can put *numbers* on the top and bottom. How on earth do you measure "how big a jump" or "how much prior knowledge"? That is where the paper reaches for a surprising tool.

---

## Part 3 — how you measure the parts: the length of the shortest program

To turn the fraction into numbers, Chollet borrows an idea from a field called **Algorithmic Information Theory** *(a branch of computer science that measures how complex a thing is by the length of the shortest program that can produce it — "complexity = shortest description")*. The key quantity is **Kolmogorov complexity** *(the length, in bits, of the shortest possible program that outputs a given thing; a simple, regular thing has a short program, a random mess has a long one)*. You do not need the maths — you need the one intuition it gives, which is beautiful.

**The intuition: the "amount of understanding" in a solution is the length of the shortest program that expresses it.** A short program that solves a task has captured a *rule*; a giant program that just lists every case has captured only a *lookup table*. This is the same "prediction ≈ compression" idea you met at the base of the ladder — *(from [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md): squeezing something into a short form means you found its pattern; a memoriser needs a long form because it kept every case)* — now turned into a ruler.

With that ruler, Chollet can measure the parts of the fraction. The paper builds it around a clever reference point it calls the **optimal training-set solution**. The panel unpacked it well:

> "the shortest possible program that can solve the training set — and *only* the training set — to optimal precision … if I give you that, how much *more* do you need to know to solve the entire task?"
> *(MLST panel, plain-words version of the paper's construction, 2020)*

Sit with that, because it is the whole measurement in one move:

- Take the **shortest program that nails the training examples** — the best a pure memoriser could do. Call its length the "free" part: it is what the training data hands you outright.
- Now ask for the **shortest program that solves the *whole* task**, every unseen case included — the program that found the real *rule*.
- **Generalization difficulty is the gap between those two.** How much *extra* rule did you have to supply that the training data did not already contain?

Two quick examples make it concrete (and note — these are *new* illustrations, not the card's Caesar cipher):

- **Top-left-pixel task.** Suppose in the training images, every cat happens to have a blue top-left pixel and every dog a red one. The shortest training-set program is "read the corner pixel" — trivially short. But it tells you **nothing** about the real task of telling cats from dogs. The gap between the cheap training-program and the true task-program is **enormous** → generalization difficulty is high → a system that still solves the real task must be doing real work.
- **Sorting.** A few lines of code sort *any* list of numbers, forever. The shortest program that solves the whole task is about as short as the one that solves any training example — there is essentially **no gap**. Generalization difficulty is ~zero. Sorting is the paper's example of the bottom rung of the ladder (next section): a task with **no** generalization in it at all.

And **priors + experience** get measured the same way — as *description length*. A strong built-in prior (like "the world is made of objects") is a big chunk of program you were handed for free; a mountain of training examples is a big chunk of information you were fed. Both shrink the "work left to do," both go on the bottom of the fraction, both are counted in bits of program/description. It is one currency — **program length** — for the whole formula.

**The honest catch, stated now so it does not surprise you later:** Kolmogorov complexity is **not actually computable** — there is no program that can reliably find the shortest program for an arbitrary thing (this is a proven limit, a cousin of the uncomputable walls in the base rungs). So the formula is a **conceptual compass, not a working meter.** You cannot plug a real system in and get its exact IQ out. What you *can* do is build a test that **holds the bottom of the fraction fixed** — fix the priors, starve the experience — so that a high score can *only* have come from the top. That test is ARC. Which is the point of the ladder we build next.

---

## Part 4 — the ladder: the spectrum of generalization

If generalization difficulty is "how big the jump," then different systems live at different **heights of jump they can make**. Chollet lays these out as a **spectrum** — a ladder from no generalization at all up to the human kind. This is the single most useful picture in the paper, and the card never showed it. Here it is, bottom to top:

| Rung | Name | What it means | Who lives here |
|---|---|---|---|
| 0 | **Absence of generalization** | Zero uncertainty: every case is known in advance, the program is fixed. | A sorting algorithm; a calculator; classic hand-coded software. |
| 1 | **Local generalization** *(robustness)* | Handles new cases *inside* a known task — small wobbles it was trained to expect. | A good image classifier: new photo, same known category. |
| 2 | **Broad generalization** *(flexibility)* | Handles cases the *developer never specifically foresaw*, across a range within one broad domain. | Roughly where the best current AI is reaching for — and often missing. |
| 3 | **Extreme generalization** | Handling *"unknown unknowns"* — entirely new tasks across an unknown range of domains. | Humans. Only humans, so far. |

Two glosses, then the two most important lessons of the ladder.

*"Robustness"* = staying right under small, expected disturbances (noise, a shift, a new photo of a known thing). *"Flexibility"* = coping with genuinely unexpected situations, not just noisy versions of expected ones. *"Unknown unknowns"* = problems you did not even know were possible — you cannot have prepared for them, because you could not have imagined them.

**Lesson one — the whole field has been climbing this ladder one rung at a time, and moving the goalposts each time.** The panel caught the pattern sharply: ten years ago, getting a classifier to work on a new photo of a known object *was* the frontier of "generalization"; once that was routine it got renamed "narrow," and the frontier moved up a rung. This is not cheating — it is the ladder doing its job. Each rung that falls reveals the next. (It is the same "each ARC version falls, a harder one restores the gap" pattern the card flagged as Stuck #3 — now you can see it is *built into the theory*: the ladder was always meant to be climbed rung by rung.)

**Lesson two — there is a second, sneakier way to cut the ladder, and it is the one that matters for building an honest test.** Chollet splits generalization a second way, by *who* the new situation is new *to*:

- **System-centric generalization** — new to the **system**, but the *developer* knew it was coming. The classic example: the held-back **test set** in ordinary machine learning. The system has not seen those exact images, but the developer *chose* them, from the same distribution, knowing exactly what kind of thing they'd be. The developer's foresight quietly did most of the work.
- **Developer-aware generalization** — new to the system **and** to the developer. Nobody, not even the person who built the system, knew these exact tasks in advance.

This second cut is the real reason ARC is built the way the card described. Recall the card's design choice — *every puzzle is new, and the rule is not written anywhere.* Now you can see the deep reason: ARC's evaluation puzzles are kept in a **private set the developer never sees**, precisely to force **developer-aware** generalization. If the builder could see the test tasks, the builder's own foresight would leak into the system (as priors) and the score would be a lie. Hiding the tasks from *everyone* — the machine and its maker — is the only way to measure a jump that nobody pre-loaded the answer to. The card told you ARC hides its tasks; the theory tells you **why that is not a detail but the entire point.**

---

## Part 5 — the floor you're allowed to stand on: the four Core Knowledge systems

There is one more piece the formula needs, and it resolves an obvious objection. If intelligence is "jump from *little* given," and you must starve the priors, then — do you test the system with **zero** priors at all? No. A system with truly zero built-in knowledge could not even understand the question. A newborn is not a blank slate; it arrives already expecting a world of objects, and that head start is *not* what we call its intelligence.

So Chollet does not set priors to zero. He fixes them at a **specific, small, shared floor** — the priors a human is *born with* — and measures the jump *from there*. The card named this floor in one line (*"objectness, counting, elementary physics — the sort of knowledge any four-year-old possesses"*). The deep version is that this floor is not a vague list; it is taken straight from **developmental psychology** *(the science of how babies' minds grow)*, which finds that human infants come pre-equipped with exactly **four** systems of "core knowledge." ARC is built to require *these four and nothing else* — no language, no trivia, no schooling. Here they are:

| # | Core Knowledge system | What the baby already expects | How ARC uses it |
|---|---|---|---|
| 1 | **Objectness & elementary physics** | The world is made of **objects** that hold together (cohesion), don't vanish when hidden (persistence), and act on each other by touching (contact). | Grids are read as collections of distinct shapes that move, touch, and occlude. |
| 2 | **Agentness & goal-directedness** | Some things are **agents** that act *toward goals*, not just get pushed around. | A puzzle's "before → after" is read as a purposeful transformation, an intended end-state. |
| 3 | **Number & elementary arithmetic** | **Small numbers**: telling one from two from three, counting, comparing more/less. | Counting objects, repeating a shape *N* times, matching quantities. |
| 4 | **Elementary geometry & topology** | **Space**: lines, shapes, symmetry, rotation, translation, scaling, inside/outside (containment). | Reflecting a shape, rotating it, scaling it, testing what's enclosed. |

("Topology" = the study of shape-properties that survive stretching and bending, like "is this dot *inside* the loop?" — inside-ness, connectedness, holes.) These four are the paper's chosen **denominator floor**: every ARC solver is *allowed* exactly this much for free — the same start a human child gets — and its score then measures only how far it can jump *beyond* the floor. That is what makes ARC a fair race between a machine and a five-year-old: **both start from the same four priors.**

And here the nature/nurture point from Part 2 pays off. It does not matter whether a machine has these four systems *hand-coded in* or *learned* from somewhere — the formula sums priors and experience, so either way they sit on the bottom of the fraction as "given." What is being measured is always the same: the jump *from* this shared floor *to* a solved novel puzzle. That jump, and only that jump, is the intelligence.

---

## Part 6 — the fight it picks: no universal intelligence

The formal theory is not just a definition; it is a **rejection** of the field's other big definition, and seeing the fight makes both sharper. This is genuinely new to this page — the card never touched it.

The rival is the **Legg–Hutter definition of universal intelligence** (2007), which — because it is what most universities still teach — is the one to beat. Its idea: intelligence is an agent's **average success across *all possible* environments**, where each environment is weighted by its simplicity *(simpler worlds count for more)*. The weighting uses the same program-length ruler from Part 3: a simple environment has a short describing-program and gets a bigger weight. It is elegant, mathematical, and **universal** — it makes no reference to humans at all. A truly universal intelligence would be good at *every* conceivable world.

Chollet rejects it, on two grounds:

- **"Universal intelligence" is a mirage — the No Free Lunch theorem kills it.** There is a proven result in machine learning called **No Free Lunch** *(no single method can be better than random when averaged over literally all possible problems — a method that wins on some problem types must lose on others)*. So an intelligence that tried to be good across *all* environments equally could be **no better than brute-force search** — a nonsense target. To mean anything, intelligence must be measured over a **bounded, specific range** of tasks, not "everything." Universality, the very thing that makes Legg–Hutter elegant, is what makes it empty.
- **So pick the *human* range — be anthropocentric.** *(Anthropocentric = human-centred.)* If you must choose a bounded scope, choose the one scope we actually care about and can point to: the tasks **humans** find meaningful. Chollet is blunt that there is **no** universal intelligence to chase — intelligence is always *relative to a scope of tasks*, and the only scope worth targeting for a human-like AGI is the human one. The argument for it is disarmingly simple, as the discussion put it: human intelligence is *"the only intelligence we know,"* so it is the only non-arbitrary yardstick we have.

This is a real philosophical choice with a real cost, and the paper's own critics press it (we return to this in the honesty box). But you can now see the shape of the whole theory: **give up on measuring intelligence in the abstract, over all possible minds; instead measure a specific, human-anchored conversion rate — jump-per-given — over the tasks a human child could face.** ARC is that measurement made into 1,000 little coloured puzzles.

---

## Putting the machine back together

Before we judge it, hold the whole thing in one view — because the parts only shine when you see them click together:

1. You can only measure **skill**, and skill is **bought** with priors + experience (Part 1).
2. So measure the **conversion rate** instead: generalization difficulty (the jump) **÷** priors + experience (the free stuff), averaged over a scope (Part 2).
3. Measure each part in one currency — the **length of the shortest program** (Part 3).
4. Different systems make jumps of different height: the **spectrum** absent → local → broad → extreme, and the system-centric vs **developer-aware** cut that says *hide the test from the builder too* (Part 4).
5. Fix the bottom of the fraction at a fair, shared floor — the **four core-knowledge systems** a baby is born with (Part 5).
6. And measure it over the **human** scope, because "universal intelligence" is a mirage (Part 6).

ARC is what you get when you build a test that obeys all six rules at once. That is why the card could call ARC "the definition turned into a scoreboard" — now you have seen the definition it is a scoreboard *for*.

---

## Judging the formal theory: where it is stuck

The card judged the *bet* (does program synthesis reach AGI?). This page judges the *theory* (is the formula a good definition of intelligence?). They are different questions, and the theory has its own, distinct soft spots. Be fair first: this is the most **serious, operational** definition of intelligence anyone has put forward — it turned a word philosophers argue about forever into something you can (almost) measure, and it correctly predicted that a memory-resistant test would resist scaling for years. Hold that. Now the four cracks.

### Stuck #1 — the formula can't actually be computed

The theory's own ruler is broken as a ruler. **Kolmogorov complexity is uncomputable** (Part 3), so you can never find the true "shortest program," which means you can never put an exact number on generalization difficulty, on the priors, or on the final fraction. The formula is a **compass, not a meter** — it tells you which direction is "more intelligent," but not how far. Everything practical (ARC) is an *approximation* that works only by holding the denominator roughly fixed and hoping the estimate is close. A definition you cannot evaluate is a strange kind of measurement. **[Established — this is a mathematical fact, acknowledged in the paper.]**

### Stuck #2 — "less formal than it looks"

The panel's sharpest charge, from people who admire the paper: several of the key pieces are **crisper in the writing than in reality.** Two examples:

- **The spectrum's rungs are drawn around "what today's AI can't do yet."** One host's worry: the line between "local" and "broad" generalization keeps getting **redrawn** as models improve — so the ladder may be tracking *the machines' current blind spots* rather than a fixed, real structure of intelligence. (This is the theory-level version of the card's Stuck #3.)
- **"Developer-aware" runs away from you if you push it.** If a system's generalization must be judged against *everything* its developer knew, then — the panel pressed — you must also count what the *developer's* teachers knew, and their culture, and evolution, all the way back, until *"everything is as generalizable as everything else, because everything came from the Big Bang."* Where you *stop* that regress is a judgement call, not a formula. **[Contested — a real objection from sympathetic experts; the framework's edges are fuzzier than its equations suggest.]**

### Stuck #3 — the anthropocentric choice gives up universality (and maybe over-rates generalization)

Choosing the *human* scope (Part 6) buys meaning at the price of generality, and not everyone thinks the trade is worth it. One line of critique the panel raised: the paper simply **assumes generalization matters more than skill** — but *"the market tells us otherwise."* A narrow, super-skilled system (AlphaGo, a protein-folder) can be worth billions while generalizing to nothing; if raw usefulness is the goal, Chollet's yardstick measures the wrong thing. Chollet's reply is that he is measuring *intelligence*, not *usefulness*, and they are allowed to differ — but the objection is fair: the theory **decides in advance** that the human, generalizing kind of intelligence is the important kind, and that decision is a value judgement hidden inside what looks like a neutral measurement. **[Contested — a genuine disagreement about what the measure is *for*.]**

### Stuck #4 — even the theory's champions doubt it "gets you anywhere"

The most striking crack is one the paper's own admirers voice. On the very corpus video, the hosts — who clearly *love* the paper, and made feature-length videos on it — still say ARC may be a *"fun challenge"* that does not *"get us anywhere to AI."* Even if the formula is the right definition of intelligence, two gaps remain open: (a) a good **definition** of intelligence is not a **recipe** for building it — knowing what to measure doesn't tell you how to actually build a system that scores well; and (b) the human scope may be **impossible to write down** — one host's repeated point was that if he could formally describe all the human priors and tasks, he would *already* have solved AGI, so the scope the formula needs may be as hard as the thing it is trying to measure. **[Contested — the theory may be correct and still not be a path.]**

---

## ⚠️ Honesty box

- **A definition, not a device.** The single most important thing to keep straight: this is a *definition* of intelligence you can reason with, not an instrument you can read. Its central quantity is provably uncomputable (Stuck #1). When someone cites "the measure of intelligence," they mean the *conceptual* fraction — jump over given — not a number they calculated. **[Established.]**
- **The strong part is the diagnosis; the exact formalism is softer.** *Skill is bought with priors + experience; measure the conversion rate instead; hide the test from the builder* — these are sharp, durable, field-shaping ideas. The precise equation, the exact rung-boundaries, and the runaway "developer-aware" regress are **fuzzier than the paper's notation implies** (Stuck #2). Keep the diagnosis; hold the formalism loosely. **[Contested.]**
- **Anthropocentric is a choice with a cost.** Aiming at the *human* scope is defensible (it's the only intelligence we can point to) but it is a **choice**, and it quietly assumes generalization beats skill — which the market, and some serious critics, dispute (Stuck #3). Do not treat "human-scope generalization" as *obviously* the definition of intelligence; it is *a* definition, argued for. **[Contested.]**
- **Efficiency is the part that keeps being proven right (freshness).** The card's Stuck #2 was that o3 *beat* ARC-AGI-1 in Dec 2024 — but at roughly **$3,500 per puzzle**. Read through *this* page, that result does not dent the theory; it **confirms** it: the formula always said intelligence is *efficiency*, and paying thousands of dollars per task is the opposite of efficient. The field agreed — **ARC-AGI-2** (Chollet et al., 2025) rebuilt its leaderboard as a **2×2 of cost-per-task × score**, calling cost *"the most directly comparable efficiency axis across humans and AI"* (top private-set result ~**24% at $0.20/task**, *as of the ARC Prize 2025 results*). The measure's *efficiency* demand, which o3 seemed to break, is now **scored directly**. And Chollet has put money on the theory: in 2025 he and Mike Knoop founded **Ndea** (a YC-backed lab, ~**$43M** raised, *as of 2026-07*) to build the card's deep-learning-**plus**-program-synthesis architecture — the constructive bet, now funded. **[Established — dated snapshots; the numbers will age, the efficiency principle is the durable part.]**
- **What ages vs what lasts.** The ARC-AGI-2/-3 scores, the cost figures, Ndea's raise — all 2019–2026 snapshots that will move. The lasting parts are the **wall** (skill is all you can measure, and it's bought), the **fraction** (difficulty ÷ priors+experience), the **program-length ruler**, the **spectrum** (absent → local → broad → extreme; system-centric vs developer-aware), the **four core-knowledge systems**, and the **anthropocentric choice**. Learn those; the scores are illustration.

---

## How to use this (if you want to direct AI work)

- **Always ask for the denominator, not just the score.** The formula's single most useful habit: when you see a benchmark result, refuse to read the score alone. Ask *what was on the bottom of the fraction* — how many priors were hand-built in, and how much task-specific data was used? A 90% that cost a billion examples and a hand-tuned pipeline is worth **less**, as evidence of intelligence, than a 60% from almost nothing. Score-per-given, not score.
- **Separate "new to the system" from "new to the builder."** Before trusting any "it generalizes!" claim, ask which kind: is the test set something the developer *chose and foresaw* (system-centric — cheap), or something **nobody** saw coming (developer-aware — the real thing)? If you cannot confirm the test was hidden from the builder, assume foresight leaked in and discount the result.
- **Watch cost as the efficiency proxy.** Since exact efficiency is uncomputable, the usable stand-in is **cost per task** (compute, dollars, examples). A capability that only appears at thousands of dollars per problem is telling you about brute force, not intelligence — exactly the reframe ARC-AGI-2's cost-scored leaderboard institutionalised. Put price next to every score.
- **Name where a system sits on the spectrum.** "Robust" (local), "flexible" (broad), and "handles unknown unknowns" (extreme) are three genuinely different products, and vendors blur them. Forcing a claim onto the ladder — *which rung, exactly?* — cuts through more hype than any leaderboard.
- **What you delegate vs what you keep.** *Delegate:* building the ARC solver, estimating the description-lengths, running the evals. *Keep for yourself:* insisting on the denominator, telling system-centric from developer-aware, reading cost as efficiency, and remembering that this whole apparatus is a **compass** — it points, it does not measure, and a good definition of intelligence is still not a recipe for building one.

---

## Connections

- **Keep only three things:** ① **You can only measure skill, and skill is bought** — with priors (built-in) or experience (practice); both hide real ability. So intelligence is not the *score* but the **conversion rate**: how big a jump (generalization difficulty) you made from how little you were given (priors + experience), averaged over a scope of tasks. ② Every part is measured in one currency — **the length of the shortest program** (short = a rule, long = a lookup table) — which makes the formula a **compass, not a working meter** (it's uncomputable). ③ It lays out a **ladder** (absence → local/robust → broad/flexible → extreme/human) and insists the test be hidden from the **builder** too (developer-aware), starting everyone from the same **four core-knowledge priors** (objects, agents, number, geometry) over the **human** scope (there is no universal intelligence).
- **This deep-dive branches off:** [AP8 · program synthesis & ARC](../20-the-approaches/08_ap8-program-synthesis-arc.md) — read that card first; it owns *skill ≠ intelligence*, *fetching vs synthesis*, the *Caesar cipher*, *what ARC is*, and the *two engines*. This page is the formal theory **under** that card's one-line definition — the slogan turned into a measurement.
- **Down the ladder it leans on:** the *prediction ≈ compression* idea (short description = found the pattern) lives at [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md); the "scale buys skill, but is it intelligence?" fight is [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md); the reason "efficiency" keeps being the deciding number ties back to the [bounds](../30-across-the-approaches/01_the-bounds-data-compute-energy.md) (cost is the wall) and the [verdict](../40-the-verdict/01_which-bets-get-to-agi.md) (efficiency vs raw score).
- **Where it points next (later AP8 deep-dives):** having *defined* intelligence, the open question is how you **build** a system that scores well — the [**solver mechanisms**](02_ap8-deep-dive-solver-mechanisms.md) (library-learning / DreamCoder, test-time training, transduction vs induction — *now written*) and the [**research frontier**](03_ap8-deep-dive-the-research-frontier.md) (where broad priors come from; nets that propose programs; the efficiency race; the interactive ARC-AGI-3; program search that discovers new mathematics — *now written*). Those are the other deep-dive modules off this same [card](../20-the-approaches/08_ap8-program-synthesis-arc.md).
- **How sure are we?** The *diagnosis* (skill is bought; measure the conversion rate; hide the test from the builder) — **[Established / durable]**. The *exact formalism* (computable numbers, fixed rung-boundaries, a non-arbitrary human scope) — **[Contested, and partly uncomputable]**.

## Check yourself *(try one, from memory)*

1. In one sentence: why can a raw benchmark score *never* measure intelligence? (Use the word *bought*.)
2. Name the top and the bottom of Chollet's fraction. What does a *high* value mean, and what does a *high score with a huge bottom* mean?
3. Priors and experience are **added** on the bottom. What surprising thing does that say about the nature-vs-nurture question?
4. What is the "shortest program" ruler used for — and why does its uncomputability make the formula a *compass, not a meter*?
5. Put these in order and say what each means: *local*, *extreme*, *absence of*, *broad* generalization.
6. Why must an honest test (like ARC) be hidden from the **developer**, not just the system? (Use *developer-aware*.)
7. Name the four Core Knowledge systems, and say why ARC fixes the priors at exactly this floor rather than at zero.
8. Why does Chollet say there is **no universal intelligence** — and what does the No Free Lunch theorem have to do with it?

## Revision notes

*Newest first.*
- `rev 1 (2026-07-16)` — created as the **first deep-dive module** (reading group **⑤ Deep dives**), branching off the [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the card's *skill≠intelligence*, *fetching vs synthesis*, *Caesar cipher*, *ARC design*, and *two engines* are **referenced, never re-taught**; this page adds only the new formal layer: the *skill-is-bought* wall, the **conversion-rate fraction** (generalization difficulty ÷ priors + experience over a scope), the **program-length / Algorithmic-Information-Theory** measurement basis, the **generalization spectrum** (absence → local → broad → extreme; system-centric vs developer-aware), the **four Core Knowledge systems** (enumerated from developmental psychology — the card gave only a one-line version), and the **anthropocentric / no-universal-intelligence** fight with Legg–Hutter. Grounded in **Chollet, "On the Measure of Intelligence" (2019, arXiv 1911.01547)** — the informal definition quoted verbatim from the paper — plus the corpus **MLST** deep-dive on the paper (Chollet's spoken *"efficiency … into generalizable programs"* clip; the panel's unpacking of the formula, the priors-plus-experience denominator, the optimal-training-set-solution, and the sympathetic critiques used in the judge-it). Full live-SOTA pass (July 2026): the efficiency principle re-affirmed by **ARC-AGI-2**'s cost×score 2×2 leaderboard (Chollet et al. 2025; ~24% at $0.20/task) and by Chollet & Knoop's **Ndea** lab (YC W2026, ~$43M) — each dated. Four cracks: **uncomputable** (compass not meter) · **less formal than it looks** (moving rungs; the developer-aware regress) · **anthropocentric choice / generalization-over-skill value judgement** · **a definition is not a recipe** (the theory's own champions doubt it "gets us anywhere").

---
*This is the first deep dive — the formal theory beneath [AP8](../20-the-approaches/08_ap8-program-synthesis-arc.md)'s slogan. The next AP8 deep-dives go from *defining* intelligence to *building* it: [the solver mechanisms](02_ap8-deep-dive-solver-mechanisms.md), then [the research frontier](03_ap8-deep-dive-the-research-frontier.md). To see the whole map this branches off, return to the [spine](../APPROACHES_TO_AGI.md).*
