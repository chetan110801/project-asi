---
id: c-agent-loop-context
sortkey: 5008
title: AP3 · Deep dive — inside the agent loop: what actually runs each turn, and why "context" (not reasoning) is the real bottleneck
domains: [frontier, approaches-to-agi, deep-dive]
level: core
prereqs: [c-next-word, c-ap2-reasoning, c-ap3-agents]
provides: [agent-control-loop, stateless-model-harness-split, tool-calling-structured-output, model-context-protocol-mcp, context-window-as-substrate, context-engineering, context-rot-lost-in-middle, attention-budget-quadratic, memory-as-context-management, plan-as-context, subagents-context-isolation, multi-agent-token-cost, context-handling-gap-not-reasoning-gap, harness-permanent-external-scaffolding, tool-calling-march-of-nines, lossy-memory-retrieval]
resources: []
status: ready
reading_time: 37 min
rev: 1
created: 2026-07-17
updated: 2026-07-17
---

# AP3 · Deep dive — inside the agent loop: what actually runs each turn, and why "context" (not reasoning) is the real bottleneck

*This is a **deep dive** past the [AP3 card](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md). The card gave you the bet — a mind is a **system**, not one model — and named the four pieces you bolt around a model to make an **agent**: an act-loop with tools (ReAct), a memory that reflects (Reflexion, Generative Agents), a planner, and a growing skill library (Voyager). It gave those pieces as **ideas** — as a diagram of parts. What it never did was open the machine and show you **what actually happens on each turn**: who runs the loop (it is **not** the model), how a model literally "uses a tool" (it does not run anything — it writes a wish that other code grants), and the single, finite thing that every one of the four pieces is really fighting over. This page opens all three. And it lands on the fact the field itself reached in 2026: the reason agents are brilliant for four minutes and hopeless for four hours is **not** that their reasoning runs out — it is that their **context** does. Everything the card already said — the four pieces, the march of nines, the scaffolding-vs-model debate — is referenced, not repeated.*

> **You are here:** a **deep-dive module** — reading group **⑤**, the optional layer that branches off the main staircase. This one hangs off **[AP3 · agents & cognitive architectures](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md)**. *Read the AP3 card first* — this page assumes it and opens the machine under the four "pieces" the card described. It is the first deep dive off AP3, the least speculative bet on the whole map (it is *how working AI is already built*) and, for that same reason, the one whose machinery is most worth seeing from the inside.
>
> **What you already have (a one-line reminder each, then we build — none of it is re-taught here):** from **[guessing the next word](../10-how-ai-works-today/01_guessing-the-next-word.md)** — today's main AI is a **text machine**: words in, words out, one step, then it forgets. From the **[AP3 card](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md)** — the **bet** (a mind is a system of parts, the model is one part); the **four pieces** an agent adds (act-loop/tools · memory/reflection · planning · skill-library), each grounded in a real published system (ReAct, Reflexion, Generative Agents, Voyager); and the four cracks — **the march of nines** (per-step errors compound, so long jobs fall apart), **scaffolding-vs-model** (is the wrapper a real road, or just an app layer the next model absorbs?), **can't out-think its model**, and **multi-agent teams don't yet beat one good agent**. From the **[AP2 card](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)** — the **reasoning model** that spends extra thinking at answer-time is the brain sitting *inside* the agent. **New here:** the *mechanism* the card skipped — the **loop as a program the harness runs** (not the model), the **tool call as structured text**, the **context window** as the agent's entire momentary world, **context engineering** as the real discipline, and the 2026 verdict that the bottleneck is context, not reasoning.
>
> **Where the facts come from:** written, checkable sources, each quote web- or corpus-verified as exact. The **loop and the stateless model** — the *12-Factor Agents* guide (a widely-cited practitioner guide) and Anthropic's *Building Effective Agents* (Dec 2024). **How a tool call works** — the *12-Factor Agents* guide (tools = structured outputs) and OpenAI's *A Practical Guide to Building Agents*. **The tool protocol** — the Model Context Protocol (MCP) documentation. **The context window as a finite resource** — Anthropic's *Effective context engineering for AI agents* (2025) and Liu et al., *Lost in the Middle* (2023). **Sub-agents** — Anthropic's write-up of its multi-agent research system (2025). The fast-moving numbers (MCP adoption, the long-horizon benchmark gap) are checked on the web (**as of July 2026**) and dated where they move. The card's own grounding — ReAct, Reflexion, Generative Agents, Voyager, Karpathy, METR — is *pointed at*, not re-quoted.

---

## In one minute

The card handed you a tidy picture: a reasoning model in the middle, four helpful parts bolted around it. Here is what that picture hides — and each hidden thing is a place the whole approach is quietly stuck.

1. **The model does not run the loop.** A language model is a **stateless** function *(stateless = it keeps no memory between calls; feed it the same input twice and you get the same output, with no trace that the first call ever happened)*. It answers once and forgets. So the agent's *continuity* — the thing that holds a goal for an hour — cannot live in the model. It lives in an outside program, the **harness**, that calls the model again and again and keeps all the state itself. The "mind" of an agent is mostly **outside** the brain.

2. **A model never "uses a tool." It writes a wish.** When an agent "runs a search" or "executes code," the model itself does nothing to the world. It emits a piece of **structured text** — a tool's name plus its arguments — and a *separate* piece of ordinary code reads that text, does the real action, and pastes the result back in. The model can only ask; another program does the acting. Which means a tool call is just more text the model **predicted**, and can be malformed, mis-aimed, or made up like any other text.

3. **The agent's entire world, at every instant, is one finite page of text — the context window.** Everything the model "knows" on a given turn is exactly the tokens fed into that one call: its instructions, its tool list, the running transcript, the latest result. Nothing else exists to it. That page has a hard size limit, and — the crucial part — the model gets *worse* at using it as it fills up. So all four of the card's "pieces" (tools, memory, planning, skills) turn out to be **four ways of fighting over one scarce page.** The real craft of building an agent has a name now: **context engineering.**

4. **The 2026 bottleneck is context, not reasoning.** Short tasks are nearly solved; long ones are not — and when the field looked closely at *why* a strong agent falls apart over hours, the answer was not that it runs out of intelligence. It runs out of **clean context**: the page fills with its own noise, the plan scrolls off the top, an early mistake poisons everything after it. The march of nines the card described is, underneath, mostly a **context** problem.

The card asked whether a mind is *assembled* or *grown*. This page shows you the assembly line — and finds that the part doing the real work is not the model, and not even "the architecture" in the abstract, but the humble, human-written machinery that decides **what goes on the page each turn.**

---

## One line of base, then we build

Two reminders, because the whole page turns on them — and both are owned by earlier rungs, so here they are *pointed at*, not re-taught.

- The [next-word rung](../10-how-ai-works-today/01_guessing-the-next-word.md) gave you the **text machine**: it takes some text and produces the next chunk of text, one shot, then it is done — it has no standing memory of its own. This page takes that fact deadly seriously: *a model is one function call, and one function call cannot be an agent.* Everything an agent is over time has to be built **around** that single, forgetful step.
- The [AP3 card](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) judged the **bet** (is wrapping a model in an architecture a real road to a general mind? — its four cracks). This page is one level down: **is the wrapper, seen up close, as clean and solid as the word "architecture" makes it sound?** So read every part as opening a machine: here is the loop the card drew as an arrow → here is the code that actually runs it → here is the one resource it all competes for → here is where that machine cracks. We are **not** re-judging the bet. We are inspecting the assembly the bet is made of, and only at the end asking what its flaws do to the bet.

One framing to carry the whole way. The card called the outside structure **scaffolding** and asked whether the models will absorb it. To judge that fairly you have to know what the scaffolding actually *is*. It is three things, and this page is built around them in order: **a loop** (Part 1), **a way to call tools** (Part 2), and **a way to manage a finite page of text** (Parts 3–4). Keep asking, as we go: *which of these could a bigger model ever swallow, and which must always live outside it?* That question turns out to have a sharp, mechanical answer.

---

## Part 1 — the loop is not the model: a stateless brain and the harness that runs it

Start with the reveal that reorganises everything. The card said an agent is "a reasoning model placed inside a loop" — the model *thinks, acts, sees what happened, thinks again.* That sentence quietly implies the model is *doing* the looping. It is not. The model cannot loop, because it cannot remember that a previous turn happened. The *12-Factor Agents* guide states the base fact plainly: language models are "stateless functions" that "turn inputs into outputs" — and nothing about them persists from one call to the next.

*(LLM = **large language model**, the text machine from the base rung. "Stateless" is glossed above: no memory between calls.)* A stateless function is like a pocket calculator: press `2 + 2`, get `4`; it does not know or care what you typed a moment ago. Each time you call a language model, it is a **fresh** calculator that has never seen you before. So where does the agent's memory, its sense of "I am halfway through a job," actually live? In a **separate ordinary program** that wraps the model — call it the **harness** *(the harness = the plain, non-AI code around the model that runs the loop: it holds the running record, decides when to call the model, executes the model's requested actions, and stops when the job is done; also called the orchestrator or the control loop)*. The harness remembers. The model just answers, one call at a time.

Here is the loop the harness runs, exactly as the guide writes it — three steps, then repeat:

> "1. LLM determines the next step in the workflow, outputting structured json ("tool calling")
> 2. Deterministic code executes the tool call
> 3. The result is appended to the context window
> 4. Repeat until the next step is determined to be "done""
> *(12-Factor Agents guide, 2025)*

Read it slowly, because this four-line loop is the whole engine of every agent on the card. *(Two glosses: **structured json** = text written in a strict, machine-readable format — more on this in Part 2; **deterministic code** = ordinary programming that does exactly the same thing every time, the opposite of the model's guessing.)*

1. The harness shows the model everything so far (the **context window** — Part 3) and asks: *what's the next step?* The model replies with either "I'm done, here's the answer" or "call this tool with these inputs."
2. If it asked for a tool, the **harness** — not the model — runs that tool for real.
3. The harness takes the result and **writes it into the record**, so the next call to the model can see it.
4. It loops back to step 1, and keeps going until the model says "done."

Notice who does what. The model contributes exactly one thing per turn: a single decision, then it forgets. The **harness** contributes everything else — the memory, the actual doing, the record-keeping, the stopping. This is why Anthropic, in *Building Effective Agents*, defines an agent not as a special model but as a **pattern of use**:

> "Agents ... are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."
> *(Anthropic, "Building Effective Agents," 2024)*

And, stripped to its bones:

> "They are typically just LLMs using tools based on environmental feedback in a loop."
> *(Anthropic, 2024)*

The word "just" is doing honest work there. An agent is *just* a model, called in a loop, with its tool-results fed back in. That is the entire trick. (Anthropic draws a useful line next to it: a **workflow** is when "LLMs and tools are orchestrated through predefined code paths" — a fixed recipe — whereas an *agent* lets the model choose the path as it goes. Both are loops the harness runs; the agent just hands the steering to the model.)

So the first correction to the card's picture is large: **the agent is the loop, and the loop is the harness, and the harness is not the model.** The model is a brilliant, amnesiac consultant you can phone once per question. Everything that makes it feel like a *worker with a goal* — the card's whole promise — is built by the plain code around it. Hold that; it becomes the sharpest thing this page can say about the scaffolding debate (engine-crack #2).

---

## Part 2 — how a model actually "uses a tool": a wish written in structured text

The card's Piece 1 was the act-loop: "an agent lets that text be an *action* — a command it can actually run." True as a picture, but it skips the mechanism entirely, and the mechanism is where the cracks hide. A model cannot run a command. It cannot touch a file, open a web page, or execute code. All it can ever do is **produce text.** So how does "produce text" become "search Wikipedia"?

The answer is the plainest idea in the whole field, and the *12-Factor Agents* guide puts it as a slogan: **tools are just structured outputs.** The model does not *do* the search. It **writes a request for one**, in a strict format the harness is waiting for. Concretely: instead of replying in loose prose, the model emits something shaped like

```
{ "tool": "web_search", "arguments": { "query": "population of France" } }
```

— a tool's **name** plus its **arguments**, written as **JSON** *(JSON = a simple, rigid text format for writing down structured data as labelled fields, so that a program can read it back exactly; it is the lingua franca of machines talking to machines)*. That block of text is the "wish." Then step 2 of the loop takes over: the **harness** reads the wish, calls the *real* `web_search` function with `"population of France"`, gets the answer, and pastes it back into the record for the next turn. The model asked; the harness acted. This split has a name in industry — **function calling** or **tool use** — and models are specially trained to produce these blocks reliably. OpenAI's guide lists it as one of an agent's three core parts:

> "Tools External functions or APIs the agent can use to take action"
> *(OpenAI, "A Practical Guide to Building Agents," 2025)*

*(**API** = an application programming interface: a defined doorway one program exposes so other programs can call it — here, the real functions the harness runs on the model's behalf.)*

### How the model knows what tools exist: the schema

For the model to write a valid wish, it has to be *told*, inside its context, what tools are available and what each one expects. Every tool comes with a **schema** *(schema = a precise description of a tool: its name, what it does, and the exact shape of arguments it takes — like the labelled slots on a form the model must fill in correctly)*. The model reads these descriptions and produces arguments that fit. The Model Context Protocol documentation states the mechanism cleanly:

> "Tools enable AI models to perform actions. Each tool defines a specific operation with typed inputs and outputs. The model requests tool execution based on context."
> *(Model Context Protocol documentation, 2026)*

> "Tools are schema-defined interfaces that LLMs can invoke."
> *(Model Context Protocol documentation, 2026)*

Read "the model **requests** tool execution" and "interfaces that LLMs can **invoke**" carefully: the model *requests* and *invokes*, it does not *execute*. The doing is always someone else's code.

### The 2026 standard plug: MCP

There is a practical problem lurking. Every tool — a database, a calendar, a code-runner, a company's internal system — used to need its own custom wiring into every agent, a quadratic mess of glue code. In late 2024 a standard emerged to kill that: the **Model Context Protocol (MCP)** *(a protocol = an agreed common language two programs use to talk, so anything that speaks it can plug into anything else that speaks it)*. Its own documentation gives the memorable analogy:

> "Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems."
> *(Model Context Protocol documentation)*

The idea: a tool or data source is wrapped once as an **MCP server** *(a small program that exposes some tools in the standard protocol)*, and any agent that speaks MCP — the **client** — can use it, no custom glue. By July 2026 this has become the field's default plumbing: MCP is reported to have crossed roughly **97 million monthly downloads of its software kits** with **over 10,000 public servers**, and is adopted across Anthropic, OpenAI, Google, Microsoft, and Amazon *(as of 2026-07; the exact figures come from secondary trackers and should be read as dated, rough snapshots — the durable fact is that the industry standardised on one tool-protocol, not any single number)*. It is now common to hear the *next* step discussed — **agent-to-agent** protocols, where one agent exposes *itself* to another as if it were a tool. Hold that idea; it is the mechanical seed of "multi-agent" (Part 5).

### Why this mechanism matters for judging the bet

Two consequences fall straight out of "a tool call is just predicted text," and both bite later.

- **A tool call can be wrong the way any sentence can be wrong.** The model can invent a tool that does not exist, fill an argument with a plausible-but-false value, or mangle the JSON so the harness cannot parse it. Nothing about "using a tool" is grounded or guaranteed — it is a guess, formatted as a form. (This becomes engine-crack #3: the plumbing has its *own* march of nines.)
- **The model's power is exactly the set of tools the harness offers it.** An agent is not "generally able to act"; it can do precisely the operations someone wired up, and no others. The intelligence may be general; the *reach* is a hand-built list. That is a permanent piece of scaffolding — a superhuman mind still cannot open a web page it was never given a tool for.

So Piece 1 of the card, opened up, is: **the model writes structured wishes; deterministic code grants them; a schema tells the model what it may wish for; and a standard protocol (MCP) is the plug.** Now we can see the thing all of this is written *onto* — and the thing it all competes for.

---

## Part 3 — the context window is the whole world (and it is finite)

Here is the deepest idea on the page, and the card does not touch it. Ask: on any single turn, what does the model actually *know*? Not "what has the agent seen over the last hour" — the model is stateless, remember; it knows nothing of the last hour. It knows **exactly and only the text placed in front of it for this one call.** That text has a name: the **context window** *(the context window = the single block of text handed to the model on one call — its entire momentary universe; also just called "the context." Everything the model can use to decide its next step must be inside it, and nothing outside it exists to the model at all)*.

What is on that page each turn? Four things, stacked together: the **instructions** (who the agent is, how to behave), the **tool list** (the schemas from Part 2), the **running transcript** (every thought, tool call, and result so far), and the **latest observation** (what just came back). The model reads all of it and emits its one next step. Then the harness adds to the page and calls again. *(One reminder from the [scaling rung](../10-how-ai-works-today/02_scaling-laws-and-emergence.md): text is measured in **tokens** — chunks of roughly a word; that rung owns the term. The context window has a **token limit** — a hard ceiling on how much text fits.)*

This single fact reorganises everything the card called a "piece." Memory, plan, skills, tool-results — for the model to *use* any of them, they must be **on the page.** There is no other channel. The agent does not "have" a memory the way you have yours; it has whatever text the harness chose to put in the window this turn. So the entire craft of building a good agent collapses to one question: **what do you put on the finite page each turn?** That craft has, in 2026, a settled name. Anthropic defines it:

> "**Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference..."
> *(Anthropic, "Effective context engineering for AI agents," 2025)*

*(**inference** = the act of running the model to get an output, as opposed to training it. "Curating" = choosing carefully what to include and what to leave out.)* And the aim of that craft is not "give the model everything" — it is the opposite:

> "good context engineering means finding the _smallest_ _possible_ set of high-signal tokens that maximize the likelihood of some desired outcome."
> *(Anthropic, 2025)*

Why *smallest*? Because the page is not just size-limited — it actively **degrades** as it fills. This is the part that surprises people, and it is the mechanical heart of the whole page.

### Why a fuller page is a worse page

You might think: context windows are huge now (millions of tokens), so why not just pile everything in? Because a model's ability to *use* what is on the page falls as the page grows. Two written findings pin this down.

First, the classic one. Liu et al. (2023) tested how models use long inputs and found a striking, now-famous pattern:

> "performance is often highest when relevant information occurs at the beginning or end of the input context"
> ... "significantly degrades when models must access relevant information in the middle of long contexts"
> *(Liu et al., "Lost in the Middle," 2023)*

A crucial fact buried in the middle of a long page is often *missed* — the model attends best to the ends. Anthropic's context-engineering guide names the general effect and, importantly, says *why* it happens:

> "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases."
> *(Anthropic, 2025 — describing "context rot")*

The mechanism is baked into how these models are built. A transformer *(the standard design of today's language models — the [AP1 deep dive](07_ap1-deep-dive-anatomy-of-a-scaling-law.md) names it too)* works by letting **every token look at every other token** to decide what matters — a mechanism called **attention** *(attention = the step where the model weighs how much each piece of the text should influence each other piece)*. Anthropic spells out the cost:

> "every token to attend to every other token across the entire context. This results in n² pairwise relationships for n tokens."
> *(Anthropic, 2025)*

Read `n²` (n-squared) plainly: if you **double** the amount of text, you roughly **quadruple** the number of token-to-token relationships the model must juggle — its finite "attention budget," in Anthropic's phrase, spread ever thinner over ever more pairs. So the guide's blunt conclusion:

> "Context, therefore, must be treated as a finite resource with diminishing marginal returns."
> *(Anthropic, 2025)*

*(**Diminishing marginal returns** = each extra token you add buys less than the one before, and eventually makes things worse.)* This is why a long context is not a bigger desk — it is a more *crowded* one. The 12-Factor guide reaches the same rule from the practitioner side:

> "Even as models support longer and longer context windows, you'll ALWAYS get better results with a small, focused prompt and context."
> *(12-Factor Agents guide, 2025)*

### The march of nines, seen from underneath

Now put this next to the card's Stuck #1, the **march of nines** (per-step errors compound over a long loop — the card owns that arithmetic; it is only pointed at here). This page adds the *substrate* under it. When an agent grinds through a hundred-step job, its context window is filling the entire time — with every thought, every tool result, every dead end. And a filling window is a degrading window. So the loop does not just fail because a fresh 95%-reliable step occasionally misfires; it fails because the *page it reasons on* gets longer, noisier, and harder to use with every turn. The 12-Factor guide describes the visible symptom exactly:

> "get lost when the context window gets too long - they spin out trying the same broken approach over and over again"
> *(12-Factor Agents guide, 2025)*

That "spin out — same broken approach over and over" is a context failure, not only a reasoning failure: an early mistake sits in the transcript, poisons the page, and every later turn keeps reading it and repeating it. So the card's compounding-error problem has a mechanical parent: **the agent's own history, piling up in a finite and degrading window.** Fix the context and much of the "unreliability" was never a reasoning problem at all. Hold that — it is exactly what the 2026 evidence will say out loud (Part 5).

---

## Part 4 — memory and planning, mechanically: everything is context management

Armed with Part 3, the card's other pieces stop being separate organs and reveal themselves as **operations on the one finite page.** Take them in turn.

### Memory = what you can put back on the page

The card gave memory as "a place outside the model where the agent writes down what it has seen and done, and from which it can read back later," and gave **reflection** (Reflexion) as writing lessons in plain words into an "episodic memory buffer." All true — and mechanically, all of it reduces to a single move: **memory is any trick for choosing what to put back in the window**, because the window is the only thing the model can read. There are two such tricks, and every agent uses them.

- **Compaction** *(compaction = boiling the running transcript down to a shorter summary so it still fits on the page)*. As the transcript grows toward the token limit, the harness replaces the old, verbose history with a condensed version — "here is what happened and what we learned so far," in far fewer tokens. The 12-Factor guide lists this as its own principle, "compact errors into the context window": even failures get summarised down rather than left to clog the page in full.
- **Retrieval** *(retrieval = storing information *outside* the window in a searchable store, and pulling back only the few pieces relevant to the current step)*. The full record lives in external storage; each turn, the harness fetches just the relevant slice and pastes it in. This is the same idea as **RAG** *(retrieval-augmented generation: before answering, search a document store for relevant passages and place them in the context — a standard way to give a model knowledge it was not trained on)*, usually powered by **embeddings** *(embeddings = turning each piece of text into a list of numbers that captures its meaning, so "find the relevant memory" becomes "find the stored numbers closest to the current ones"; the [AP5 deep dive](05_ap5-deep-dive-learning-without-a-teacher.md) uses embeddings too)*.

Here is the trade-off the card's clean "just add a memory" hid: **every token of recalled memory is a token you cannot spend on the task.** Memory is not free storage bolted onto the side — it is a **claim on the finite page**, competing with the instructions, the tools, and the live work for the same scarce room. "Give the agent a good memory" really means "spend the window wisely," and spending it on the past is spending it away from the present. There is no memory that does not cost context.

### Planning = a to-do list living on the page

The card's Piece 3 was planning — break a big goal into steps. Mechanically, in today's agents, a plan is **just tokens in the window**: a written to-do list the model produces, re-reads, and updates each turn. The card noted the modern way is that the reasoning model plans *inside its own chain of thought* — and now you can see what that means concretely: the plan is text the model writes into the context and then keeps consulting. Which raises an immediate, mechanical failure mode the card could only gesture at: on a long job, as the window fills and gets compacted, **the plan can scroll off the top or get summarised away** — and an agent that has lost its plan drifts, re-does finished work, or wanders. "Losing the thread" on a long task is often literal: the thread fell out of the window. Keeping the plan alive is a *context* job — re-inserting the goal and the to-do list every turn so the stateless model is reminded, from scratch, what it is doing and why.

### The unification

So here is Part 4's payoff. The card drew four pieces as four boxes around the model. Opened up, they are **not four things** — they are four kinds of **writing to, and reading from, one finite page**, all choreographed by the harness:

- **tools** put *the world's answers* on the page (Part 2),
- **memory** puts *the relevant past* on the page (compaction + retrieval),
- **planning** keeps *the goal and next steps* on the page,
- and **skills** (the card's Voyager library) are stored-away procedures the harness pulls *back onto* the page when needed.

The "architecture" the card celebrated is, underneath, a single discipline doing four jobs: **deciding what text the stateless model sees each turn.** That is context engineering, and it is the real substance of building an agent.

---

## Part 5 — the 2026 frontier: buy more pages, standardise the plug, and the honest long-horizon gap

The classic loop assumed one agent, one growing page. By 2026 the frontier is a set of moves that all trace back to the same scarcity — *the page is finite and degrades* — plus the field's own blunt diagnosis of where agents actually break.

### Sub-agents: the mechanical meaning of "multi-agent"

The card's Stuck #4 treated multi-agent systems as a grand, unproven dream — a "society" or "AI company." Mechanically, the version that *does* work in 2026 is far humbler and is really a **context** trick: when a sub-task would flood the main agent's window with detail, spin up a **sub-agent** with its own fresh, clean page, let it do the messy work, and have it hand back only a short summary. Anthropic's write-up of its multi-agent research system says exactly this:

> "Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent."
> *(Anthropic, "How we built our multi-agent research system," 2025)*

> "Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations."
> *(Anthropic, 2025)*

*(**Separation of concerns** = each part handles its own job on its own page, without its details tangling into the others'.)* Read what "multi-agent" turns out to *be*: not a civilisation of minds, but a way to get **more clean pages** — each sub-agent burns through the detail of one sub-question on its own window, then returns only the distilled tokens that matter, keeping the lead agent's page uncluttered. It is the agent-to-agent idea from Part 2 (one agent exposed to another as a tool) used as a **context-isolation** device. But it is not free, and the same write-up is honest about the cost:

> "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."
> *(Anthropic, 2025)*

So "add more agents" trades **money for clean context.** That is a real, useful trade — and a strict limit on the "society of agents" dream: every extra page you buy is paid for, forever, in tokens. (This is the mechanical reason the card's Stuck #4 stands: multi-agent *works* as context isolation, but "a team that genuinely out-thinks one good agent" is a different, unproven claim.)

### Persistent memory and the standard plug

Two more frontier moves, briefly, both already-introduced ideas pushed further. **Persistent memory** takes retrieval (Part 4) across *sessions*: the agent writes durable notes to an external store — a file, a memory of past projects — and reads them back on a later run, so it is not reborn blank each time. And **MCP** (Part 2) keeps spreading as the universal plug, which matters here because a shared protocol is what makes both tool-use and sub-agent-as-tool composable at scale. The plumbing is consolidating.

### The honest number: where agents actually break

Now the finding that ties this whole page together. Through 2026, the field split its benchmarks by **how long a task takes a human**, and the two halves are diverging hard. Short-horizon tests are **saturating** *(saturating = scores climbing so close to 100% that the test can no longer tell strong models apart)* — one widely-watched software-engineering benchmark, SWE-bench Verified, is reported to have gone from roughly **13.8% (March 2024) to about 82% (late 2025)** — while long-horizon tasks are **not** saturating: frontier agents score near **100% on tasks that take a human under about four minutes, and under 10% on tasks that take over four hours** *(as of 2026-07; the exact percentages come from secondary trackers and are dated, rough snapshots — the durable fact is the widening split between short and long horizons, which the card's METR "task time horizon" also measures; that number is the card's, pointed at here)*. The card owns *that* the horizon is climbing. What this page adds is the field's explanation of the gap's **cause**, and it is the thesis of everything above: the dominant diagnosis in 2026 is that this is a **context-handling gap, not a reasoning gap** — the model is smart enough for the four-hour task; what fails is holding a coherent, un-degraded page across the hundreds of turns the task takes. The bottleneck is not the brain. It is the page. **[The short/long-horizon split and the context-as-bottleneck framing are Established as of 2026; the exact percentages are Contested, dated snapshots.]**

---

## Putting the machine together

Hold the whole engine in one view.

1. **The loop is not the model (Part 1).** The model is a **stateless** function — it answers once and forgets. A separate program, the **harness**, runs the loop: show the page → get one step → execute it → append the result → repeat until done. The agent's continuity lives in the harness, not the brain.
2. **A tool call is structured text (Part 2).** The model never acts; it emits a tool's name + arguments as JSON — a *wish* — and deterministic code grants it. A **schema** tells the model what it may wish for; **MCP** is the 2026 standard plug. So every action is a *predicted* thing, and can be wrong like any prediction.
3. **The context window is the whole world (Part 3).** On each turn the model knows only the finite page fed to it. That page is size-limited *and* degrades as it fills (context rot; lost-in-the-middle; `n²` attention spread thin). The craft of choosing what goes on it is **context engineering**: the *smallest* set of high-signal tokens.
4. **Every piece is context management (Part 4).** Memory (compaction + retrieval), planning (a to-do list on the page), tools, and skills are all just **writing to and reading from the one page** — and each competes for the same scarce room. Memory isn't free storage; it's rent on the window.
5. **The frontier buys more pages (Part 5).** Sub-agents are **context isolation** (clean pages at 4×–15× the token cost), persistent memory extends retrieval across sessions, MCP standardises the plug — and the honest 2026 data says the long-task wall is a **context-handling gap, not a reasoning gap.**

---

## Judging the machinery: where the agent loop itself is stuck

The [AP3 card](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) judged the **bet** (four cracks: the march of nines · scaffolding-vs-model · can't out-think its model · multi-agent unproven). This page judges the **machine** — a sharper, mechanical question: *set the bet aside; is the loop, seen from the inside, as clean and solid as "wrap a model in an architecture" makes it sound?* Be fair first: this machine genuinely works, it is how every capable AI system today is built, and its pieces provably add abilities (the card's Legs 1–2 stand). Nothing here erases that. But the machine has its **own** four cracks, and each one sharpens a crack the card only stated.

### Stuck #1 — the finite window is a hard ceiling, and everything competes for it

The card's march of nines is per-step error multiplying. This page finds the **resource** underneath it: there is exactly one finite page, it degrades as it fills, and *every* part of the agent — instructions, tools, memory, plan, live work — competes for the same room. You cannot "just add memory" or "just add more tools," because each addition is rent on the one scarce, degrading window. So an agent doing a long job is in a losing race with its own transcript: the further it gets, the fuller and noisier its page, the worse its next step — until it spins out. This is not a bug to be patched; it is the **shape** of the machine. Bigger context windows do not remove it (they push the ceiling out while `n²` and context rot push back), which is why the discipline is *shrinking* what's on the page, not growing it. The card's compounding-error problem has a name at the bottom: **a finite, degrading working memory that everything must share.** **[Established — context rot and the finite-window trade-off are documented; how far bigger windows help is Contested.]**

### Stuck #2 — the harness *is* the scaffolding, and something must always live outside a stateless call

This is the sharpest thing the mechanism says, and it lands directly on the card's central doubt (is the scaffolding a real road, or an app layer the model absorbs?). Now we can answer *precisely which parts can be absorbed and which cannot.* A single call to the model is **stateless** — it cannot remember the last turn, cannot run its own next turn, cannot execute its own tool wish, cannot manage its own page over time. Those jobs **must** live in code *outside* the model, because they are jobs a stateless function structurally cannot do to itself: *someone* has to hold the record, run the loop, execute the wishes, and curate the window. So the card's fear — "the model will absorb all the scaffolding" — has a hard floor: **the loop, the tool-execution, and the context management can never be swallowed into a single forward pass**, no matter how smart that pass gets. What the models *have* absorbed is the *cleverness inside* the scaffolding — the planner, router, and critic parts the card mentioned, which a strong reasoning model now does in its own chain of thought. So the true division is now visible: the **thin, permanent harness** (loop + tool-execution + window management) survives every model; the **thick, clever middleware** (hand-built decomposition, routing, self-checking) is exactly what gets eaten. AP3 is a *real* road for the permanent part and an *app layer* for the rest — and the machine tells you which is which. **[Established that the harness must be external; Contested where exactly the line falls, and it moves toward "thinner" each year.]**

### Stuck #3 — tool-calling has its own march of nines

The card's compounding-error arithmetic was about the *task*. Part 2 shows the same arithmetic bites the *plumbing*. Every tool call is predicted text, so every tool call can be malformed (unparseable JSON), mis-aimed (right tool, wrong argument), or hallucinated (a tool that does not exist). Chain twenty tool calls and the reliability of the *machinery* multiplies down exactly as the reliability of the *reasoning* does — a second march of nines, underneath the first, in the wiring rather than the thinking. Worse, a tool result the model misreads becomes poisoned context (Stuck #1) that misleads every later turn. So "give the agent tools" does not just add power; it adds a whole new surface of failure that also has to be pushed to many nines before the agent is trustworthy. The card counted the reasoning's nines; the machine reveals the plumbing has its own. **[Established — tool-call errors and malformed outputs are a documented, active reliability problem.]**

### Stuck #4 — the agent doesn't remember; it re-reads a lossy summary

The card's "memory" sounds like recall — the agent *knows* what it did. Part 4 shows it is nothing of the sort. The model is stateless; it "remembers" only by having the harness paste a **compacted summary** or a **retrieved slice** back onto the page. Both are **lossy** *(lossy = compression that throws information away to save room, keeping only what it judges important)*: summarisation drops detail, retrieval fetches only what it scored as relevant — and the one fact you will need next is exactly the one you did not know to keep. So "give it a memory" quietly means "give it a lossy, self-chosen compression of its past," and the agent can be confidently wrong because the crucial detail was summarised away three turns ago and no longer exists on the page. This is a failure mode with **no clean fix**: keep everything and the window degrades (Stuck #1); compress and you lose the thing you needed. The card's tidy "memory piece" hides a permanent trade between *forgetting* and *drowning*. **[Established — the compression/retrieval trade-off is inherent; the best operating point is an open engineering question.]**

### The big question under all four

The card asked: *is a mind something you assemble out of parts, or something you grow in the middle?* The machine answers a sharper, mechanical version: **given that the model is stateless and its whole world is a finite, degrading page, how good can a mind built this way ever get?** And the honest answer from all four cracks is: *a mind built this way is only ever as coherent as the harness that curates its page* — and that harness is human-built, finite, and lossy. The intelligence may be superhuman; the *continuity* is a plain program deciding what text to show an amnesiac each turn. That is why the 2026 wall is a **context-handling gap, not a reasoning gap**: we already have the brains for the four-hour task; what we do not yet have is a way to hold a clean, coherent working memory across the hundreds of turns it takes. So the deepest verdict on AP3's machine is neither "the architecture is the road" nor "the model absorbs it all," but something more precise: **the architecture reduces, almost entirely, to the management of one scarce resource — context — and until that is solved, agents will keep being brilliant sprinters and unreliable marathoners.** As of July 2026, the frontier of "agents" is, underneath its diagram of parts, the frontier of *context.* **[Contested — the key open question, now located precisely: it lives in whether context management can be pushed to the reliability long tasks demand.]**

---

## ⚠️ Honesty box

- **The mechanism is durable; the tools and numbers are snapshots.** The *shape* — a stateless model, a harness running a loop, tool calls as structured text, a finite context window everything competes for — is a core idea that will still be central in a decade. The specifics — MCP's download counts, the SWE-bench percentages, the "4 minutes / 4 hours" split, today's context-window sizes — are 2024–2026 snapshots and move fast. Learn the machine; date every number. **[Established shape; dated specifics.]**
- **"Context, not reasoning" is a 2026 framing, not an eternal law.** The claim that the long-horizon wall is a context-handling gap is the dominant diagnosis *right now* and it is well-supported — but it is a diagnosis, and a genuinely better reasoning model or a new memory design could shift where the wall sits. Hold it as the current best explanation, strongly evidenced, not as proof that reasoning is "solved." **[Likely, as of 2026.]**
- **Bigger context windows are not the fix, and can mislead.** Million-token windows are real, but `n²` attention cost and context rot mean a fuller page is often a *worse* page. "It has a huge context window" is not the same as "it uses a huge context well" — treat the two as different claims, and prefer evidence of the second. **[Established.]**
- **Multi-agent is context isolation, not (yet) a society.** Sub-agents genuinely help by giving clean pages — at 4×–15× the token cost. That is a real, bounded win. It is *not* evidence for the grand "AI company" claim (the card's Stuck #4), which remains unproven. Keep "clean-context trick" and "team that out-thinks one agent" firmly apart. **[Established for the first; Contested for the second.]**
- **The harness can never fully vanish.** Because a single model call is stateless, the loop, the tool-execution, and the window management must always live outside it. Any pitch that "the next model won't need scaffolding" is half-right (the clever middleware shrinks) and half-wrong (the thin harness is permanent). Bet on the thin harness; expect the thick middleware to be absorbed. **[Established.]**
- **Names and numbers age; the machine doesn't.** MCP, the specific guides quoted, the 2026 benchmarks — all dated. The lasting parts are the **stateless-model / harness split**, **tool-calls-as-structured-text**, the **finite-window** truth, **context engineering**, and the **four cracks**. The example plumbing will be replaced; the shape of the argument will not. **[Established core, dated specifics.]**

---

## How to use this (if you want to direct AI work)

- **When someone shows you an agent, ask what's on the page.** Past the demo, the real questions are mechanical: what is in its context each turn, how does it compact the history, what does it retrieve and how does it decide, how does it keep the plan from scrolling away? An agent's true capability is set by its **context discipline**, not its model alone. A team that cannot describe its context strategy does not yet control its agent.
- **Read "big context window" and "uses context well" as different claims.** (Stuck #1.) The first is a spec sheet; the second is the whole game. Ask for evidence that the agent stays coherent as the page fills — long-task reliability, not headline window size.
- **Separate the thin harness from the thick middleware.** (Stuck #2.) Before building an elaborate planner/router/critic graph, ask which parts the next model will simply do in its own chain of thought (the thick middleware — expect it to be absorbed) and which must live outside a stateless call forever (the loop, tool-execution, context management — build these to last). Spend your engineering on the permanent thin layer.
- **Count the plumbing's nines, not just the reasoning's.** (Stuck #3.) Tool calls fail as text fails. Demand numbers on malformed/mis-aimed calls and on recovery, and design the harness to validate, retry, and quarantine bad tool results before they poison the page.
- **Treat memory as a lossy compression, and design what it keeps.** (Stuck #4.) "Add memory" is not a feature you switch on; it is a standing choice about *what to throw away.* Decide deliberately what must survive compaction and what may be retrieved on demand — and assume the agent will sometimes be confidently wrong because the needed detail was summarised away.
- **What you delegate vs what you keep.** *Delegate:* writing the tool wrappers, standing up MCP servers, wiring the retrieval store, tuning the compaction. *Keep for yourself:* the judgement of what belongs on the page each turn, the refusal to mistake window size for competence, the discipline of separating permanent harness from throwaway middleware, and the habit of asking whether a failure is really the *model* (see the card's Stuck #3) or — far more often — the **context.**

---

## Connections

- **Keep only three things:** ① An agent is **not a model** — it is a **stateless model** called in a loop by a **harness** (plain code) that holds all the state; the model contributes one decision per turn and forgets. ② A "tool" is a **wish written in structured text** (name + arguments as JSON) that *deterministic code* grants — so every action is a *prediction* that can be wrong; **MCP** is the 2026 standard plug. ③ The agent's entire world each turn is a **finite context window** that *degrades as it fills* — so memory, planning, tools, and skills are all just **operations on one scarce page**, the craft of choosing what to show is **context engineering**, and the 2026 long-task wall is a **context-handling gap, not a reasoning gap.**
- **This deep dive branches off:** [AP3 · agents & cognitive architectures](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md) — the card owns the *bet, the four pieces as ideas (ReAct, Reflexion, Generative Agents, Voyager), the cognitive-architecture history, the march-of-nines arithmetic, the scaffolding-vs-model debate, the METR task-horizon, and the four bet-cracks*. This page opens the *machine* under the pieces — the **stateless-model/harness loop**, the **tool-call-as-structured-text** mechanism, **MCP**, the **finite context window**, **context engineering**, and the memory/planning-as-context-management unification — and judges the *machine's own* trustworthiness.
- **Where it points:** [AP2 · reasoning & test-time compute](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md) — the **brain** inside the loop, whose in-chain planning is what absorbs the card's "thick middleware" (Stuck #2); [AP1 · scale & foundation models](../20-the-approaches/01_ap1-scale-and-foundation-models.md), whose [Bitter Lesson](../20-the-approaches/01_ap1-scale-and-foundation-models.md) is the force *doing* that absorbing; [AP4 · RL from interaction](../20-the-approaches/04_ap4-rl-from-interaction.md) — the reward-driven way to *train* the loop rather than script it; and the [alignment & self-improvement page](../30-across-the-approaches/02_alignment-control-and-self-improvement.md), where "a stateless mind whose continuity is a human-built harness" becomes a control question (what the harness lets the agent do, and remember, is where oversight lives).
- **How sure are we?** That the model is stateless and the harness runs the loop, that tool calls are structured outputs executed by deterministic code, that MCP is the de-facto tool protocol, and that the context window is finite and degrades as it fills — **[Established]**. That the 2026 long-horizon wall is primarily a *context-handling* gap rather than a reasoning gap — **[Likely, strongly evidenced as of 2026]**. The exact benchmark numbers, and how far better context management can push long-task reliability — **[Contested, open]**.

## Check yourself *(try one, from memory)*

1. Explain why a language model, on its own, **cannot** be an agent — using the word **stateless**. What runs the loop instead, and what does it hold?
2. Write the **three-step loop** in your own words. On each turn, what is the *one* thing the model produces, and who actually executes the action?
3. A model "uses a tool." Describe what *literally* happens (the **wish** and who grants it). Why does this mean a tool call can be wrong the way any sentence can be wrong?
4. What is the **context window**, and why is a *fuller* window often a *worse* window? Use the words **attention**, **`n²`**, and **context rot**.
5. Why is **memory** better described as "rent on the page" than as "free storage"? Name the two tricks (**compaction**, **retrieval**) and the loss each one risks.
6. The card's **march of nines** is per-step error compounding. Give the **context** substrate underneath it (why does a long-running agent "spin out"?).
7. The big one: name the **four engine cracks** of the agent loop, and explain why "the long-horizon wall is a *context-handling* gap, not a *reasoning* gap" is the thesis that ties them together.

## Revision notes

*Newest first.*
- `rev 1 (2026-07-17)` — created as the **first AP3 deep-dive** (reading group **⑤ Deep dives**, sortkey 5008), branching off the [AP3 card](../20-the-approaches/03_ap3-agents-and-cognitive-architectures.md); the eighth module in group ⑤ (after the AP8 trilogy + AP4 #1 + AP5 #1 + AP9 #1 + AP1 #1). Written to the simplest-English + progressive-ladder standard ([`HARD_RULES §6.5`](../../INSTRUCTIONS/HARD_RULES.md)); strict zero-repetition (§4.2) — the card's *bet / four pieces as ideas (ReAct, Reflexion, Generative Agents, Voyager) / cognitive-architecture history / march-of-nines arithmetic / scaffolding-vs-model debate / METR task-horizon / four bet-cracks* are **referenced, never re-taught**; [AP2](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)'s *reasoning model* is **pointed at, not opened** (only its role as the in-loop brain that absorbs the "thick middleware" is used); [AP1](../20-the-approaches/01_ap1-scale-and-foundation-models.md)'s *Bitter Lesson* pointed at as the absorbing force. This page adds only the new **mechanism** layer the card skipped: the **stateless-model / harness split** and the three-step **control loop** (Part 1); **tool-calls-as-structured-output**, the **schema**, and **MCP** (Part 2); the **context window** as the agent's finite momentary world, **context engineering**, **context rot** / lost-in-the-middle / the `n²` attention cost (Part 3); the unification of **memory (compaction + retrieval), planning, tools, and skills as operations on one finite page** (Part 4); and the **2026 frontier** — sub-agents as **context isolation**, persistent memory, MCP as standard plug, and the short/long-horizon benchmark split diagnosed as a **context-handling gap, not a reasoning gap** (Part 5). Grounded in **written, quotable** sources, each verified as an exact contiguous string: the **12-Factor Agents guide** (the three-step loop; language models as "stateless functions" that "turn inputs into outputs" — quoted as two exact fragments since the source hyperlinks the first phrase; "get lost when the context window gets too long - they spin out…"; "you'll ALWAYS get better results with a small, focused prompt and context"); **Anthropic, "Building Effective Agents"** (2024 — "systems where LLMs dynamically direct their own processes and tool usage"; "just LLMs using tools based on environmental feedback in a loop"; the workflow/agent distinction); **OpenAI, "A Practical Guide to Building Agents"** (2025 — Model/Tools/Instructions; "External functions or APIs the agent can use to take action"); the **Model Context Protocol documentation** (the USB-C analogy; "Tools enable AI models to perform actions… The model requests tool execution based on context"; "schema-defined interfaces that LLMs can invoke"); **Anthropic, "Effective context engineering for AI agents"** (2025 — the context-engineering definition; "smallest possible set of high-signal tokens"; context rot; the `n²` attention-budget passage; "Context, therefore, must be treated as a finite resource with diminishing marginal returns"); **Liu et al., "Lost in the Middle"** (2023 — "highest when relevant information occurs at the beginning or end"; "significantly degrades… in the middle of long contexts"); and **Anthropic, "How we built our multi-agent research system"** (2025 — subagents with "their own context windows"; "separation of concerns"; "4× more tokens… multi-agent systems use about 15× more tokens than chats"). Full live-SOTA pass (**July 2026**), each fast fact dated: MCP adoption (~97M monthly SDK downloads, 10,000+ public servers, cross-lab); SWE-bench Verified ~13.8%→~82%; the short/long-horizon split (~100% under ~4 min, <10% over ~4 hours) with the "context-handling gap, not a reasoning gap" diagnosis; agent-to-agent protocols as the next roadmap item. Four **engine** cracks (distinct from the card's bet-cracks): **the finite, degrading window everything competes for** (the resource root of the march of nines) · **the harness is permanent, external scaffolding that can never be absorbed into a stateless call** (locates the permanent/temporary line in the card's Stuck #2) · **tool-calling has its own march of nines** (the plumbing compounds too) · **memory is lossy retrieval, not recall** — under the big question: *a mind built this way is only ever as coherent as the harness curating its page; the 2026 frontier of agents is, underneath, the frontier of context.* Degendering: all sources attributed to projects/orgs or name-only (Liu et al.); **0 gendered pronouns**, **0 self-anchor `](#…)` links**, all outbound .md links resolve.

---
*This is the first AP3 deep dive — the **machine** beneath the "a mind is a system" bet. Its stateless-model/harness split is why [AP2 · reasoning](../20-the-approaches/02_ap2-reasoning-and-test-time-compute.md)'s in-chain planning can absorb the "thick middleware," while the thin harness survives; its finite-window truth is the resource under the card's march of nines. To pick the next approach to go deep on, return to the [spine](../APPROACHES_TO_AGI.md).*
