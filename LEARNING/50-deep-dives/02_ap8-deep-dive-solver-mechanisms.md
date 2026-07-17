---
id: c-arc-solver-mechanisms
sortkey: 5002
title: AP8 · Deep dive — how ARC is actually solved (the solver mechanisms)
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-ap2-reasoning, c-ap8-program-synthesis, c-measure-of-intelligence]
provides: [neural-guided-program-search, dreamcoder-wake-sleep, library-learning-abstraction, induction-vs-transduction, test-time-training-recipe, augmentation-voting, refinement-loop, compression-at-test-time]
resources: []
status: ready
reading_time: 34 min
rev: 1
created: 2026-07-17
updated: 2026-07-17
---

# AP8 · Deep dive — how ARC is actually solved (the solver mechanisms)

*This is the second **deep dive** past the [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md). The [first deep dive](01_ap8-deep-dive-the-formal-theory-of-intelligence.md) opened up how Chollet **defines and measures** intelligence — the formula beneath the slogan. This one turns to the opposite question: not "what is intelligence?" but "**how do you actually build a machine that scores well on the test?**" The card gave the one-line answer — build a small new **program** for each puzzle by **searching** for it, and let a deep-learning model **guide** that search. But it left the guiding as a slogan. This page opens the real machinery: the four working tricks that actually top the ARC leaderboard today, each one a different way to beat the single enemy the card named — the **combinatorial explosion**. We will build them one at a time: a system that grows its own toolkit and learns to search it (**DreamCoder**), the two rival ways to answer a puzzle (**induction vs transduction**), the recipe that won the 2024 prize (**test-time training**), and the loop that defined 2025 (**propose → check → revise**). Everything the card and the first deep dive already said is referenced, not repeated.*

> **You are here:** a **deep-dive module** — reading group **⑤**, the optional layer below the main staircase. This one branches off **[AP8 · program synthesis & ARC](../20-the-approaches/08_ap8-program-synthesis-arc.md)** and sits next to its sibling, **[AP8 deep dive #1 · the formal theory of intelligence](01_ap8-deep-dive-the-formal-theory-of-intelligence.md)**. *Read the AP8 card first, and ideally deep dive #1* — this page assumes both.
>
> **What you already have (a one-line reminder each, then we move on — none of this is re-taught here):** from the **card** — the **two engines** (deep-learning *curve-fitting* is fast but data-hungry and stays near what it has seen; *program search* over a small toolkit, a **DSL**, can learn a rule from one example but suffers **combinatorial explosion** — the number of possible programs grows too fast to try them all); the **merger** (let deep-learning intuition *guide* the search); **System 1 / System 2** (fast gut-feel vs slow step-by-step); and **test-time fine-tuning** (Chollet's "active inference" — a frozen model gets ~1–2% on ARC, so you let it *adapt* to each puzzle). From **deep dive #1** — the **program-length ruler** (the "amount of understanding" in a solution ≈ the length of the shortest program that expresses it; short = a rule, long = a lookup table). **New here:** the actual algorithms those slogans stand for.
>
> **Where the facts come from:** two streams. The **voices** are corpus conversations from *Machine Learning Street Talk* — Kevin Ellis and Zenna Tavares on program synthesis, Alessandro Palmarini walking through DreamCoder, Ryan Greenblatt on the GPT-4o solver, Daniel Franzen and Jan Disselhoff (the 2024 winners), and Jeremy Berman (a 2025 top scorer). Because these are auto-transcribed, their words are given as **attributed paraphrase**, not quotation. The **hard facts** — the algorithms, the papers, the scores — are grounded in the primary papers and the ARC Prize reports, checked on the web (**as of July 2026**) and dated where they move.

---

## In one minute

The [card](../20-the-approaches/08_ap8-program-synthesis-arc.md) said: to handle a genuinely new puzzle, don't fetch a memorised answer — **build a small new program** that solves it, by **searching** for that program. And it named the catch: naive search **explodes**. A toolkit of even a dozen simple operations, snapped together into a program ten steps long, gives more possible programs than there are seconds in the age of the universe. You cannot try them all. So every real ARC solver is, underneath, **a clever way to avoid trying them all.** There are four such ways, and together they are what actually wins:

1. **Grow the toolkit and learn to search it (DreamCoder).** Instead of one fixed toolkit, the system *invents new tools* out of pieces it keeps reusing (so its programs get shorter), and it *trains a neural net* to sense which tool to reach for next (so it stops searching down dead ends). The two improvements feed each other, round after round.
2. **Pick how you answer: build the program, or guess the grid (induction vs transduction).** One family writes an actual program and runs it; the other skips the program and has a neural net *paint the answer grid directly*. Surprisingly, the two solve *different* puzzles — so the strongest systems run both and combine them.
3. **Let the model study for the exact puzzle in front of it (test-time training).** Don't freeze the model. For each new task, fine-tune it on that task's two or three examples — after manufacturing more examples by rotating, reflecting and recolouring them — then take a **vote** across all those views to pick the answer. This recipe won the 2024 prize.
4. **Propose, check, revise (the refinement loop).** Generate a candidate solution, *run it* against the examples to see where it fails, feed the failure back, and try again — an evolutionary search steered by a checker. This became the dominant shape in 2025.

Notice what is *not* on the list: "make the model bigger." Every trick here is about making the **search smarter**, not the network larger. That is the whole spirit of AP8, turned into working code.

---

## One line of base, then we build

Two reminders, because the whole page hangs on them.

- From the [card](../20-the-approaches/08_ap8-program-synthesis-arc.md): program search can learn a true rule from **one or two examples**, but it suffers **combinatorial explosion** — programs a few steps longer have vastly more possibilities, so brute-force search dies quickly. The card's fix was a slogan: *let deep learning guide the search.* **This page is what "guide" actually means, four different ways.**
- From [deep dive #1](01_ap8-deep-dive-the-formal-theory-of-intelligence.md): a solution's quality is measured by the **length of the shortest program** that expresses it — a short program found the *rule*, a long one is just a *lookup table*. Keep this ruler in your pocket; the last mechanism on the page is nothing but this ruler turned into a working solver.

Now the one new frame this page adds. The card treated "the search explodes" as a single wall. It is really **two** walls, and seeing them apart is the key that organises everything below. A search is a growing tree of possibilities. It gets too big in two independent ways:

- **It gets too deep.** The right program is long — many steps — so the tree you must grow is tall, and a tall tree is an enormous tree.
- **It gets too wide.** At each step there are many operations you *could* pick, most of them wrong, so the tree fans out fast at every level.

Every mechanism on this page attacks one wall or the other (or both): **make the program shorter** (cut the depth) or **guess the right step** (cut the width). Hold those two levers. Here is the first system that pulls both at once.

---

## Part 1 — DreamCoder: a machine that writes its own toolkit and learns to search it

Start with the purest realisation of the card's "let deep learning guide the search" — a system called **DreamCoder** (Kevin Ellis and colleagues, published 2021). It is not itself the top ARC scorer, but it is the clearest *mechanism*, and every idea later on the page is a descendant of it. The best plain-English walk-through in the corpus is by Alessandro Palmarini, a researcher who worked on DreamCoder-style solvers; the description below follows that walk-through, checked against the paper.

DreamCoder does **inductive program synthesis**: you hand it a set of little tasks, each given as a few input→output examples, and it searches for a program that produces each output from its input. *(Inductive = working out the general rule from particular examples — the opposite of being told the rule.)* On its own that is just the exploding search the card warned about. DreamCoder's whole contribution is two machines bolted onto the search that pull the two levers — depth and width — and, crucially, **improve each other over time.**

**Lever one — a growing library, to cut the depth.** A *library* here means the toolkit of building blocks the search is allowed to use *(start it with only the bare basics, like "add" and "the number 1")*. With a tiny toolkit, most useful programs are long: to build the number four you would write `1 + 1 + 1 + 1` — a deep stack of additions. DreamCoder watches the programs it manages to find and looks for **fragments that keep showing up** across many solutions. When it finds one, it **chunks** that fragment into a brand-new single tool and adds it to the library. If it notices that `1 + 1 + 1` keeps appearing, it makes a new block, "three" — so now four is just `three + 1`, a far shorter and shallower program, and the *next* search has less depth to climb. Palmarini calls this building a **tower of abstractions** — each new tool is made of older tools, and the tower grows taller as the system solves more. In the paper this chunking is done by a refactoring step (it uses a technique called *e-graph matching*) that finds the common sub-parts across many programs and factors them out. This is exactly the *program-length* idea from [deep dive #1](01_ap8-deep-dive-the-formal-theory-of-intelligence.md) used as an *engine*: a good new abstraction is one that lets the whole set of solutions be written **shorter**.

**Lever two — a neural search policy, to cut the width.** Even with a good toolkit, at each step the search faces many possible next blocks. So DreamCoder trains a neural network — a **search policy** — whose job is: *given the task, which block should I try next?* A well-trained policy points the search down the few promising branches and ignores the thousands of hopeless ones. This is the card's "deep learning guides the search," made concrete: the network is the **intuition** (System 1) steering the deliberate **search** (System 2).

Now the beautiful part — where the network's *training data* comes from. The policy needs examples of "this kind of task ⇒ this kind of program" to learn from, and at the start there are almost none. So DreamCoder **generates its own** by dreaming. This is the loop the system is named for, and it has three phases:

- **Wake.** Using the current library and the current policy, search for programs that solve the real tasks you were given. Keep the solutions you find.
- **Sleep, part one — abstraction.** Look across those solutions, chunk the repeated fragments into new library tools (lever one).
- **Sleep, part two — dreaming.** Here the system *makes up practice problems for itself.* It randomly assembles programs out of its current library, runs each one on some inputs to see what output it produces, and now it has a fresh (task ⇒ program) pair that **it invented, that never came from the real data.** These invented pairs are the "dreams" (in the paper, "fantasies"). It trains the search policy on a mix of these dreams and the real solutions — so the policy gets far more practice than the handful of real tasks could ever give it (lever two).

Then it repeats. And the two levers lift each other: a **better library** makes the dreams more realistic, which trains a **better policy**, which solves **more real tasks**, which reveals **better fragments to chunk** into the library — round and round, each turn climbing a little higher. The paper's word for this is **bootstrapping**: the system pulls itself up by teaching itself, starting from almost nothing.

Why this matters for AP8's big open problem. The card's Stuck #1 was: *program search needs strong priors to tame the explosion, and nobody knows where those priors come from.* DreamCoder is a partial, real answer — **the library is a set of priors the system grows for itself.** It does not have to be handed every useful abstraction; it discovers them by noticing what it keeps reusing. That is a genuinely new idea beyond "let deep learning guide search": *let the system also invent the vocabulary the search is conducted in.*

The honest limit, stated now. DreamCoder learned its towers in small, tidy worlds (drawing simple pictures, basic list operations) and started from a **hand-built** set of basic blocks chosen by researchers. ARC is messier and open-ended, and no one has yet grown a DreamCoder-style library rich enough to crack it on its own. *Where the base priors come from, and how to grow the library in an open world,* is still open — we return to it in the judge-it section, and it is the main thread of the next deep dive.

---

## Part 2 — two ways to answer: build the program, or guess the grid

DreamCoder always **builds a program.** But that is only one of two families of ARC solver, and the split between them is the single most clarifying idea in how ARC is attacked today. It comes sharpest from a 2024 study by Wen-Ding Li, Kevin Ellis and colleagues (*"Combining Induction and Transduction for Abstract Reasoning"*). The two families are called **induction** and **transduction**.

- **Induction — build the program.** The system outputs an actual **program** (say, a short piece of Python, or a sequence of DSL blocks) that is meant to turn each "before" grid into its "after." You then **run** the program on the examples to check it: if it reproduces every example's output, it has probably found the rule, and you run it on the real test input to get your answer. This is DreamCoder's family, and the card's whole "program synthesis" picture.
- **Transduction — guess the grid.** The system skips the program entirely. A neural net looks at the example pairs and the test input, and **emits the answer grid directly** — colouring in cell after cell, the same way a language model writes word after word *(you met next-token prediction in [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md); transduction is that, with grid cells instead of words)*. There is no program to inspect, no intermediate rule — just a learned leap from question to answer.

Put crudely: induction *shows its working*; transduction *blurts the answer.* Induction is the deliberate System 2; transduction is the intuitive System 1. And now the finding that makes the split worth a whole section. Li and Ellis trained **two neural nets on the same training tasks, with the same architecture** — one taught to induce (write the program), one taught to transduce (paint the grid). You might expect them to solve roughly the same puzzles. They did not. In the paper's own words:

> "Inductive and transductive models solve different kinds of test problems, despite having the same training problems and sharing the same neural architecture … Ensembling them approaches human-level performance on ARC."
> *(Li, Ellis et al., "Combining Induction and Transduction for Abstract Reasoning," 2024)*

The two approaches, given identical raw material, learned to be good at *different things*. Roughly: induction wins where the rule is a **precise, composed computation** ("reflect the shape, then recolour the copy, then count the corners") — the kind of exact multi-step recipe a program captures perfectly and a direct guess fumbles. Transduction wins where the pattern is **fuzzy and perceptual** ("make it look symmetric," "fill the obvious gap") — the kind of soft judgement that is hard to write as clean code but easy for a pattern-matcher to feel. Because their strengths barely overlap, the smart move is to run **both** and combine: try to find an induction program that fits the examples; if one does, trust it (you can *check* it by running it); if none does, fall back to the transduction guess. That ensemble is what climbs toward human level — and it is the card's System-1-plus-System-2 claim, now **measured**: you really do need both engines, because each reaches puzzles the other cannot.

One vivid instance of the induction family at scale. In mid-2024 Ryan Greenblatt got roughly **50%** on the public ARC-AGI-1 set using nothing exotic: have GPT-4o **write about a thousand different Python programs per puzzle**, run every one against the examples, throw away the ones that get any example wrong, and keep a program that fits — then run it on the test input *(as of mid-2024, on the public evaluation set)*. No fine-tuning, no special toolkit — just *generate many candidate programs and let the examples filter them.* It works because induction gives you a free, ruthless check: a program either reproduces the examples or it does not. That "you can run it and see" is induction's great advantage, and it comes back in Part 4.

---

## Part 3 — test-time training: let the model study for the exact exam

The card mentioned, in one line, that the leading ARC methods do **test-time fine-tuning** — Chollet's "active inference," without which a frozen model scores a negligible 1–2%. That was the headline. Here is the full recipe, the one that actually **won the ARC Prize 2024**, and *why each step is there.* It comes from Daniel Franzen, Jan Disselhoff and David Hartmann — a team who called themselves "the ARChitects" — and the corpus interview with Franzen and Disselhoff fills in the reasoning.

The starting problem is stark. A large language model, frozen and simply asked to solve ARC puzzles, is almost useless at them — the reasoning it learned from text does not transfer to these little grids. The ARChitects' fix has three moves.

**Move one — fine-tune the model to each specific task, at test time.** Instead of freezing the model, for **each puzzle** they run a short extra round of training on *that puzzle's own example pairs*, right before answering it. The model stops being a general text machine and briefly becomes a specialist in this one puzzle. This is the "active inference" the card named — but notice the difficulty it creates: an ARC task gives you only **two or three** example pairs, and you cannot train a neural network on three examples. Which forces move two.

**Move two — manufacture more training data by augmentation.** *(Augmentation = making extra training examples by changing an existing one in a way that does not change its answer.)* You take each example pair and produce many variants that obey the **same hidden rule**: rotate the whole grid ninety degrees, flip it left-to-right, swap the colour codes around, shift everything over by one. Each variant is, to the model, a fresh puzzle it has never seen — but it has the *same underlying transformation*, so learning to solve all the variants teaches the one rule from many angles. Out of three examples you can spin thousands; the ARChitects generated on the order of ten thousand augmented tasks across the public set. Augmentation is what makes test-time training possible at all: it is the water you add to three grains to get a meal.

**Move three — vote across perspectives to pick the answer.** After fine-tuning, the model, asked the puzzle, will still produce several *different* candidate answer grids. Which one do you submit? Here is the clever part, and it is why their paper is subtitled *"Solving the ARC Challenge Is a Matter of Perspective."* They do not trust the model's own confidence — a model tends to rate its own favourite answer highly whether or not it is right. Instead they test each candidate for **stability under augmentation**: take the puzzle, transform it many ways (they used sixteen views — rotations, reflections, recolourings), ask the fine-tuned model for the answer to each *transformed* puzzle, then undo the transformation on each answer and see which final grid the most views agree on. An answer that is *right for the right reason* survives being looked at sideways, upside-down and recoloured; a fluke does not. The answer that is most stable across perspectives wins the vote.

So the whole recipe is: **augment → fine-tune the model on each task → sample several answers → vote by picking the one most stable across transformed views.** With it, the ARChitects reached **53.5%** on the private ARC-AGI-1 test — the winning score of 2024, in a year when the state of the art on that test jumped from about **33% to 55.5%**, the largest single-year gain the prize had seen *(as of the ARC Prize 2024 results)*.

Step back and see what this is. The card called test-time fine-tuning "program synthesis in disguise," and now you can see why: fine-tuning bends the network's billions of knobs into the **specific procedure this one puzzle needs** — that bent network *is* the program, written in weights instead of code. Augmentation supplies the search with many views of the one rule; the vote is a checker that keeps only the answer that holds up. Depth and width, priors and checking — the same levers as DreamCoder, wearing very different clothes.

---

## Part 4 — the refinement loop: propose, check, revise

The 2024 recipe was largely **one shot**: adapt, answer, vote, done. The defining shift of **2025** — named as such in the ARC Prize 2025 report — was to make the solver **loop**: propose a candidate solution, *run it* against the examples, look at what it got wrong, feed that back in, and try again — and again — an **evolutionary search steered by a checker.** The report's phrase for the year's dominant shape is the *refinement loop* — a per-task cycle of optimisation guided by a feedback signal.

The clearest single example is Jeremy Berman's, which took the top public score on the harder **ARC-AGI-2** in 2025 (about **29.4%**, at roughly **$8 of compute per task** — *as of the ARC Prize 2025 public leaderboard*). Berman's twist is *what* gets evolved. Earlier solvers evolve **Python programs**; Berman evolves **descriptions in plain English.** The reasoning, from the corpus interview: natural language is **more expressive** than code — there are more ways to phrase an idea than to write it as a clean Python function, so an evolving search in language can *reach more of the space of possible rules*, and an LLM finds it easier to tweak a sentence than to debug a program. The search is steered the usual way: generate several candidate English descriptions, keep the promising ones, mutate and recombine them, repeat.

But language buys expressiveness at a price, and the price names the deep tension of the whole page. **You cannot run an English sentence on a grid.** A Python program checks itself — it either reproduces the examples or it does not (Part 2's free filter). A sentence does not; something else must judge whether the described rule actually works. So Berman's system had to include a separate **checker** to turn each description into a testable prediction and grade it — and the striking finding was that the *checker* mattered more than the *proposer*: a strong judge of candidate rules did more for the score than a clever generator of them. That is a general lesson about search. A search is only as good as its ability to tell a good candidate from a bad one; the guide that *scores* matters as much as the machine that *proposes*.

Notice that this is the same idea as everything before, one level up. DreamCoder's neural policy, induction's run-the-program filter, the ARChitects' augmentation vote, Berman's checker — all of them are the **guide** that tells the search which way to go. The card said "deep learning guides the search." Four sections in, "the guide" has turned out to be the load the whole enterprise carries: grow the vocabulary (Part 1), choose the representation (Part 2), adapt the model (Part 3), and above all **score the candidates well enough to climb** (Part 4).

---

## Putting the machine back together

Hold all four in one view — because each is a different pull on the same two levers (cut the depth, cut the width) the card's one wall really was:

1. **Grow the toolkit and learn to search it (DreamCoder).** Chunk reused fragments into new tools (shorter programs = less depth); train a neural policy on self-invented "dreams" (better guesses = less width); let the two bootstrap each other.
2. **Choose the representation (induction vs transduction).** Write-and-run a program, or paint the grid directly — and since the two solve *different* puzzles, ensemble them toward human level.
3. **Adapt the model to the task (test-time training).** Augment the two or three examples into thousands, fine-tune on them per puzzle, and vote for the answer that is stable across transformed views.
4. **Steer with a checker (the refinement loop).** Propose a solution, run/grade it, revise — evolve toward one that fits; and the *checker* is as important as the proposer.

Every ARC winner is some blend of these. Not one of them is "a bigger model." That is the point the card promised and this page delivered: **the progress on ARC has come from smarter search, not larger networks.**

---

## Judging the solvers: where they are stuck

The card judged the *bet* (does program synthesis reach AGI?). Deep dive #1 judged the *theory* (is the formula a good definition?). This page judges the *methods* (do these solvers show real intelligence, or just clever engineering?). Be fair first: these are genuine, ingenious inventions — a system that grows its own abstractions, a measured proof that two engines beat one, a recipe that turned a five-year-stuck test around in a single year. Hold that. Now the four cracks.

### Stuck #1 — almost every top solver now rides on a big pretrained model

Look back at what actually wins. Greenblatt samples programs from **GPT-4o**. The ARChitects fine-tune an **8-billion-parameter** language model. NVARC's 2025 winner test-time-trains a **4-billion-parameter** model on synthetic data. Berman evolves descriptions written by a **frontier LLM**. The "second engine" that AP8 said scale could never supply has, in practice, been **bolted onto a scaled model** — the search is wrapped around exactly the kind of network AP1 builds. This is the card's Stuck #2 (o3 beat ARC-AGI-1 with expensive test-time compute on a big model) seen from the solver side. So the live question sharpens: is "program synthesis" a **separate road** to intelligence, or a **technique you apply to a foundation model** — a passenger on the scaling road rather than a rival to it? **[Contested — the central tension, unresolved as of July 2026.]**

### Stuck #2 — test-time training might be fast memorising, not real synthesis

Test-time training fine-tunes the model on **rotations, reflections and recolourings of the very task being tested.** A sceptic's worry: is the system *understanding* the rule, or has it just been shown so many near-copies of the answer that it can now interpolate between them? That would be the card's "interpolative memory" charge — only sped up and aimed at one puzzle. The augmentation-vote defends against the crudest version (a pure memoriser would not survive being looked at sideways), but the line between "adapted to the task's structure" and "over-fitted to the task's surface" is genuinely blurry, and Chollet has been careful to ask which one is really happening. If the win is closer to memorisation, then test-time training raises the *score* on ARC without being the *intelligence* ARC was built to detect. **[Contested — a real, live doubt about what the method is doing.]**

### Stuck #3 — the base toolkit is still hand-built, so humans still supply the hardest priors

DreamCoder *grows* its library — but it grows it **on top of a starter set of basic blocks chosen by researchers.** The strong ARC program-search entries likewise search over a **hand-crafted DSL** (the best-known one was built by hand by a competitor, Michael Hodel). The system invents the *middle* of the tower; people still lay the *foundation.* And the foundation is where the card's Stuck #1 lives — the broad, human-like **priors** that decide what is even worth trying. So these mechanisms have *narrowed* the "where do priors come from?" problem (the system can grow abstractions) without *closing* it (someone still picks the primitives, and no one can yet grow them for an open world). That unfinished problem is the whole subject of the next deep dive. **[Established — the acknowledged open problem of the program-synthesis route.]**

### Stuck #4 — these tricks cracked the old test, and are far from cracking the new one

Every mechanism here was proven on **ARC-AGI-1**, which is now, for practical purposes, beaten. But on the harder **ARC-AGI-2**, the best 2025 Kaggle score was about **24%** (NVIDIA's NVARC, test-time training on synthetic data), with the returning ARChitects at ~16.5% and MindsAI at ~12.6% — while ordinary people solve roughly **60%** *(as of the ARC Prize 2025 results)*. On the newest, interactive **ARC-AGI-3**, frontier systems score **under 1%** and humans essentially 100% *(as of 2026)*. So the honest status is: the four tricks turned a hard test into a solved one, and then a new test opened a gap just as wide. Whether the *same* mechanisms scale to close it — or whether each new ARC needs a new trick — is exactly the card's "moving target" worry (its Stuck #3), now aimed at the methods. **[Contested — dated; the versions-keep-falling pattern is documented.]**

---

## ⚠️ Honesty box

- **The mechanisms are durable; the scores and rankings are snapshots.** *Grow-your-own-library, induction-vs-transduction, test-time training with an augmentation vote, the propose-check-revise loop, and the finding that induction and transduction solve different puzzles* — these are real, repeatable ideas worth keeping. The numbers around them (53.5%, 24%, 29.4%, and the names NVARC / ARChitects / MindsAI / Berman) are 2024–2026 snapshots that will move. Learn the mechanisms; treat the leaderboard as illustration. **[Established for the mechanisms; the rankings are dated.]**
- **Every method here is a way to prune search — not a new kind of mind.** It is worth being blunt: none of these is a fresh theory of intelligence. They are increasingly clever ways to *avoid trying every program* — better tools, better representations, better task-specific adaptation, better checkers. That is real progress, and it is also why the sceptic (Stuck #1) can say the whole enterprise is engineering wrapped around a scaled model. Keep the achievement and the doubt in the same hand. **[Contested.]**
- **A surprising outlier keeps everyone humble — CompressARC.** In late 2025 Isaac Liao and Albert Gu showed a solver with *no pretraining, no dataset, and no search* — a tiny (~76,000-parameter) network, randomly initialised, that for **each puzzle** simply trains itself by plain gradient descent to **compress that one puzzle** as tightly as possible, and reads the answer out of the compression. It solves about **20%** of the evaluation set, in ~20 minutes per puzzle on a single gaming graphics card *(Liao & Gu, "ARC-AGI Without Pretraining," Dec 2025)*. This is deep dive #1's **program-length ruler turned into a working solver** — "find the shortest description" done literally, with none of the machinery on this page. It suggests a fifth, very different mechanism, and it is a standing warning against assuming the four tricks here are the only road. **[Established the result; contested what it means.]**
- **"You can run it" is doing quiet, heavy work.** The methods that shine — induction, the refinement loop — all share one thing: a **free, exact checker**, because a program either reproduces the examples or it does not. Transduction and natural-language evolution give that up for expressiveness and have to *rebuild* a checker (Berman's lesson: the checker mattered most). Whenever you judge one of these systems, find the checker; a search with a weak judge is barely a search. **[Established.]**

---

## How to use this (if you want to direct AI work)

- **Ask which lever a "reasoning" win pulled.** When a lab reports a jump on ARC or a similar reasoning test, the useful question is not "how big was the model" but "**what made the search smarter?**" — a grown library, an induction/transduction ensemble, test-time adaptation, a better checker? A result with no answer to that question is probably a scaled model with a new prompt, not a new capability.
- **Always find the checker.** The single most predictive feature of these solvers is whether the system can **grade its own candidates cheaply and correctly** (run the program; test stability under augmentation; score the description). Strong checker → the search can climb. No real checker → the system is guessing, however fluent it sounds. Berman's finding — the judge matters more than the generator — generalises far beyond ARC.
- **Read cost per task as hard as score.** The mechanisms sit at wildly different prices: ~$8 per task (Berman), roughly $3,500 per task at o3's high-compute setting (from the card), ~20 minutes on a consumer GPU (CompressARC). Since deep dive #1 showed intelligence is *efficiency*, a high score bought with a huge search budget is telling you about brute force, not ability. Put the price next to every number.
- **Watch for test-time adaptation, and interrogate it.** If a system suddenly does far better on a task family after being allowed to fine-tune on task examples, you are seeing test-time training — powerful, and worth using. But ask Stuck #2's question: is it learning the *rule*, or memorising *near-copies*? The augmentation-stability vote is the current best defence; demand something like it before trusting the win.
- **What you delegate vs what you keep.** *Delegate:* building the DSL, running the fine-tune, wiring the augmentation and voting pipeline, coding the evolutionary loop. *Keep for yourself:* knowing whether a win came from **smarter search or a bigger model**, insisting on a **real checker**, reading **cost as efficiency**, and remembering that the deepest part — the **base priors** the search runs on — is still supplied by humans (Stuck #3), which is where the next deep dive goes.

---

## Connections

- **Keep only three things:** ① Every ARC solver is a way to **not** search every possible program, attacking two walls — a program tree that is too **deep** (fixed by growing a **library** of reusable tools, as in **DreamCoder**, which also trains a **neural policy** on self-invented "dreams" and lets the two bootstrap) and too **wide** (fixed by a **guide** that scores which step to try). ② There are **two answer styles** — **induction** (write a program and run it — checkable, exact) and **transduction** (paint the grid directly — fuzzy, perceptual) — and because they solve *different* puzzles, the best systems **ensemble** them. ③ The winning recipes adapt the model to each task: **test-time training** (augment the few examples → fine-tune per puzzle → **vote** for the answer stable across transformed views; won 2024) and the **refinement loop** (propose → **check** → revise; defined 2025) — and in all of them, the **checker** matters as much as the proposer.
- **This deep dive branches off:** [AP8 · program synthesis & ARC](../20-the-approaches/08_ap8-program-synthesis-arc.md) — the card owns the *two engines*, the *merger*, *System 1 / System 2*, and *active inference*; this page is the actual machinery those slogans stand for.
- **Its sibling deep dive:** [AP8 #1 · the formal theory of intelligence](01_ap8-deep-dive-the-formal-theory-of-intelligence.md) — its **program-length ruler** is the engine behind DreamCoder's library (a good abstraction shortens the code) and *is* the whole idea behind the CompressARC outlier (find the shortest description).
- **Down the ladder it leans on:** [guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md) — transduction is next-token prediction with grid cells instead of words; and [AP2 · test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — the "spend effort at answer-time" idea that test-time training and the refinement loop are both forms of.
- **Where it points next ([deep dive #3 · the research frontier](03_ap8-deep-dive-the-research-frontier.md)):** the crack this page could only *narrow* — **where the base priors come from**, how to grow a library in an **open** world, and building nets that *propose* whole programs — is the **research frontier**, along with the compute-**efficiency** race, the interactive **ARC-AGI-3**, and program search that discovers new results (**FunSearch / AlphaEvolve**, a bridge to [AP9 · open-endedness](../20-the-approaches/09_ap9-open-endedness.md)). That is [the next module](03_ap8-deep-dive-the-research-frontier.md) off this same [card](../20-the-approaches/08_ap8-program-synthesis-arc.md).
- **How sure are we?** The mechanisms and the induction≠transduction finding — **[Established]**. That any of them, or their combination, *scales* to close the gap on ARC-AGI-2/-3 and beyond — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. The card called the search "explosion" one wall. This page split it into two. Name both, and say which DreamCoder lever attacks each.
2. Explain DreamCoder's three phases — *wake*, *abstraction*, *dreaming* — in your own words. Where do the neural policy's training examples come from?
3. What is the difference between **induction** and **transduction**? Give one kind of puzzle each is better at, and say why running **both** beats running either.
4. Why does test-time training *need* augmentation? (Use the phrase "two or three examples.")
5. In the 2024 winning recipe, how is the final answer chosen — and why not just trust the model's most confident guess?
6. What did Jeremy Berman's system evolve instead of Python programs, what did that buy, and what did it cost? (Use the word *checker*.)
7. Stuck #1 and Stuck #3 are different doubts. State each in one sentence.
8. What makes **CompressARC** so surprising, and which idea from deep dive #1 does it turn into a working solver?

## Revision notes

*Newest first.*
- `rev 1 (2026-07-17)` — created as the **second AP8 deep-dive** (reading group **⑤ Deep dives**), branching off the [AP8 card](../20-the-approaches/08_ap8-program-synthesis-arc.md) and sitting beside [deep dive #1](01_ap8-deep-dive-the-formal-theory-of-intelligence.md). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the card's *two engines*, *merger*, *System 1/2*, and *active inference*, and deep dive #1's *program-length ruler*, are **referenced, never re-taught**; this page adds only the new machinery: the **depth/width** framing of the explosion, **DreamCoder**'s wake–abstraction–dreaming loop (library-learning + neural search policy + bootstrap), **induction vs transduction** (with the Li–Ellis measured finding that they solve different puzzles), the **test-time-training** recipe (augment → per-task fine-tune → augmentation-stability vote), the 2025 **refinement loop**, and the **CompressARC** outlier. Grounded in the primary papers and ARC Prize reports (**Ellis et al., DreamCoder, PLDI 2021**; **Li, Ellis et al., "Combining Induction and Transduction for Abstract Reasoning," arXiv 2411.02272, 2024** — abstract quoted verbatim; **the ARChitects, "Solving the ARC Challenge Is a Matter of Perspective," ARC Prize 2024 winner, 53.5%**; **Liao & Gu, "ARC-AGI Without Pretraining," 2025**), with corpus MLST conversations (Ellis & Tavares; Palmarini on DreamCoder; Greenblatt on GPT-4o; Franzen & Disselhoff; Berman) used as **attributed paraphrase** (auto-transcribed → not quoted). Full live-SOTA pass (July 2026): Greenblatt ~50% ARC-AGI-1 (mid-2024); ARC Prize 2024 SOTA 33%→55.5%; ARC Prize 2025 Kaggle top 24% (NVARC), ARChitects ~16.5%, MindsAI ~12.6%, the "refinement loop" as the year's theme; Berman 29.4% ARC-AGI-2-pub at ~$8/task; CompressARC 20% eval with no pretraining/dataset/search — each dated. Four cracks: **rides on a foundation model** · **test-time training may be fast memorising** · **base toolkit still hand-built** (→ deep dive #3) · **cracked v1, far from v2/v3**.

---
*This is the second AP8 deep dive — the machinery beneath the [card](../20-the-approaches/08_ap8-program-synthesis-arc.md)'s "guided program search." The [next one](03_ap8-deep-dive-the-research-frontier.md) goes to the open frontier: where the base priors come from, program search that discovers new results, and the efficiency race. To see the whole map this branches off, return to the [spine](../APPROACHES_TO_AGI.md).*
