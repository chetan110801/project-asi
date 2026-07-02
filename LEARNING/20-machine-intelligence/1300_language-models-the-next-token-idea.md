---
id: c-language-models
sortkey: 1300
title: Language models — the next-token idea
domains: [machine-intelligence, nlp]
level: core
prereqs: [c-entropy, c-probability, c-learning, c-neural-networks]
provides: [language-model, next-token-prediction, autoregressive-generation, self-supervised-pretraining, perplexity]
resources: [r-slp3, r-cs336]
status: ready
reading_time: 20 min
rev: 2
created: 2026-06-27
updated: 2026-07-02
---

# Language models — the next-token idea
*One question — "what word comes next?" — turns out to be enough to teach a machine grammar, facts, math, and (maybe) something like understanding. This rung gives you that one idea at full depth: what a language model **is**, why predicting the next word is a **teacher** and not a parlor trick (a small trick done to impress, with nothing deep behind it), why the training text supervises itself, how the score is kept, and the deep information-theory reason the trick works — prediction and compression (making data smaller by exploiting its patterns; here: squeezing the internet into a model's weights) are the same move. Every LLM topic after this — tokenization, transformers, tuning, reasoning, hallucination — is a branch off this trunk.*

> **You are here:** rung 1300, machine intelligence — the opening of the language-model cluster (1300–1358). Rungs written as **[13xx name]** without a link are *planned*, not yet built; their map is the [CURRICULUM](../CURRICULUM.md), and the links go live as each is written.
>
> **Grounded in:** *Speech and Language Processing* 3rd ed. (Jurafsky & Martin, Jan-2026 draft — Ch. 3, 7, 8) [`r-slp3`, corpus `textbooks/slp3`]; MacKay, *Information Theory, Inference, and Learning Algorithms* (corpus `information-computation/mackay-itila`); Brown et al. 2020, *Language Models are Few-Shot Learners* (GPT-3, corpus `papers/D2`); Shane Legg on the Dwarkesh Podcast, 2023, and Andrej Karpathy on the Dwarkesh Podcast, 2025 (corpus `transcripts/`).
>
> **Builds on:** [0300 information & entropy](../00-foundations/0300_information-and-entropy.md) — it built the bridge *predict ⇒ compress ⇒ (arguably) understand* and promised the math would return; here it returns, doing real work. Also [0600 learning](../00-foundations/0600_what-it-means-to-learn.md) (self-supervision) and [1100 neural nets](1100_neural-networks-deep-learning.md) (the machinery that will do the predicting).

---

## One question, asked forever

Start concrete. Finish this sentence:

> *The water of Walden Pond is so beautifully ...*

The textbook that anchors this whole cluster opens with exactly this game:

> "You might conclude that a likely word is blue, or green, or clear, but probably not refrigerator nor this."
> *(Jurafsky & Martin, SLP3, Ch. 3)*

You just did, in your head, the entire job of a language model. Not "picked the right word" — something subtler: you **ranked every word you know** by how likely it is to come next. *Blue* felt strong. *Refrigerator* felt absurd. That ranking-with-strengths is the whole object of study. The formal definition:

> "A language model is a machine learning model that predicts upcoming words. More formally, a language model assigns a probability to each possible next word, or equivalently gives a probability distribution over possible next words."
> *(Jurafsky & Martin, SLP3, Ch. 3)*

Read it plainly first. A **language model** (usually shortened to **LM**) is a machine that, given some text, answers one question: *what comes next, and with what odds?* A quick refresher of the tool it answers with: a **probability distribution** — a list of every possible outcome, each with a number between 0 and 1 saying how likely it is, all the numbers summing to 1 (home: [0500 probability](../00-foundations/0500_probability-and-uncertainty.md)). So the LM's answer is never one word. It is a score for **every** word at once: *blue* 0.32, *green* 0.19, ... , *refrigerator* 0.0000001.

Two small but load-bearing notes (load-bearing — carrying real weight, like a wall that holds the house up; here: details the later ideas rest on) before we go deeper:

- **"Word" is a simplification.** Real models read and write **tokens** — chunks of text, roughly a short word or a piece of a word. Why pieces, how the chopping works (an algorithm called **BPE**), and the strange failure modes it causes all get their own rung → [1305 tokenization]. For this rung, "word" is close enough.
- **The same machine can score whole sentences.** If you can price each next word, you can multiply the prices along a sentence and price the sentence. SLP3's example: an LM can tell that *"all of a sudden I notice three guys standing on the sidewalk"* has much higher probability than the same words scrambled — *"on guys all I of notice sidewalk three a sudden standing the"*. One machine, two uses: **generate** (pick likely next words) and **judge** (score how **plausible** — how believable, how likely-looking — a given text is).

### What the definition rules out

This is worth a beat, because each exclusion kills a common mental picture:

- **It is not a rulebook.** No grammarian wrote rules into it. Whatever "grammar" it has was *absorbed from data* — it is a **model** in the exact [1000](1000_machine-learning-from-examples.md) sense: a function with tunable knobs (**parameters** — the numbers inside the model that training adjusts), set by learning, not by hand.
- **It is not a database of sentences.** It does not look up your sentence in a stored copy of the internet. It *computes* a fresh distribution for a context it has never seen. (How **lossy** — keeping the gist while losing the exact detail — its "memory" of the training data really is is a key fact, and it comes below.)
- **It is not certain about anything.** Its native output is odds, never one answer. Everything downstream — the creativity, the errors, the need for sampling — flows from that.

---

## The double take: why would anyone want a word-guesser?

A **double take** is the surprised second look you give something that shouldn't be as important as it just turned out to be. Here is the question every newcomer should ask, and the field's answer, in the textbook's own (unusually excited) words:

> "Why would we want to predict upcoming words? The main reason is that large language models are built just by training them to predict words!!"
> *(Jurafsky & Martin, SLP3, Ch. 3)*

Two exclamation marks, in a formal textbook. Why the excitement? Because of what the prediction task *forces the predictor to know*. SLP3 Ch. 7 plays the fill-in-the-blank game to make the point. Look at what answering each blank actually requires:

| The blank (SLP3's examples) | What you must know to fill it |
|---|---|
| "With roses, dahlias, and peonies, I was surrounded by ___" → *flowers* | **Category facts** — that roses, dahlias, peonies are all kinds of flowers (ontological knowledge — knowledge about what kinds of things exist and how they group). |
| "The room wasn't just big it was ___" → *enormous* | **Word meaning on a scale** — that *enormous* means "big, but further along the same scale." |
| "The square root of 4 is ___" → *2* | **Math.** |
| "The author of 'A Room of One's Own' is ___" → *Virginia Woolf* | **Facts about the world and history.** |
| "The professor said that ___" → *he* | **Nothing you'd be proud of** — a statistical association between "professor" and male pronouns. The teacher teaches biases too. Hold that thought for the honesty box. |

One task; five *different kinds* of knowledge extracted. Why this example and not a cleaner one? Because a plain statement ("prediction requires knowledge") slides off the mind. The blanks make you *feel* it: there is no way to be good at this game without picking up categories, meanings, math, and facts along the way. The textbook's summary of the whole era:

> "What made the modern NLP revolution possible is that large language models can learn all this knowledge of language, context, and the world simply by being taught to predict the next word, again and again, based on context, in a (very) large corpus of text."
> *(Jurafsky & Martin, SLP3, Ch. 7)*

(A **corpus** is just a large, collected body of text — the model's diet. It's also what this project's own modules are checked against, which is a pleasing symmetry.)

And the reach of the trick is wider still:

> "almost any NLP task can be modeled as word prediction in a large language model, if we think about it in the right way"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

Translation, summarization, question-answering — phrase the task as text, and "do the task" becomes "continue the text well." **One objective swallowed a whole field** (took it over: every task became a case of continue-the-text). That is why this rung is the trunk of the cluster. **[Established]**

### The objection to anticipate

*"Surely predicting words only teaches you about words — patterns of grammar, not real knowledge?"* The blanks above are the resolution: the *only* way to reliably guess "Virginia Woolf" or "2" is to have (something that functions like) the fact. Pattern-matching on grammar alone leaves those blanks unfillable. What remains genuinely open — and it matters — is *what kind* of knowing that is: rich world-understanding or a shallower statistical echo. That debate gets its own rung → [1358 do LLMs understand?]. The claim safe to bank now is narrower: **good prediction requires the information content of the knowledge, whatever form it's stored in.** **[Established]** — the *interpretation* is what's contested.

---

## The labels are free: self-supervision

Now the economic miracle — the reason this objective, among all possible objectives, is the one that scaled.

Quick refresher: in ordinary **supervised learning**, every training example needs a **label** — the right answer, attached by a paid human (home: [0600 learning](../00-foundations/0600_what-it-means-to-learn.md), the "four flavors" of learning). Labels are the expensive, slow part of machine learning. Now watch what the language-modeling task does to that cost:

> "we know the correct answer (it's the next word in the corpus!)"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

That's it. That's the miracle. The text **is** its own answer key. Cover a word, guess it, uncover it, check. And so:

> "We call such a model self-supervised because we don't have to add any special gold labels to the data; the natural sequence of words is its own supervision!"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

("**Gold labels**" — the trusted correct answers a dataset normally needs humans to write in.) **Self-supervision** (general: learning where the supervision signal is manufactured from the data itself; here: the next word plays the role of the label) removes the one **bottleneck** (the narrow point that limits everything behind it; here: the cost of human labeling) that capped every earlier approach. Every book, every forum thread, every line of code ever posted becomes a free exercise-with-solution. The whole internet becomes a teacher that never tires and never sends a bill.

To see how big a deal this is, look at what it replaced. The GPT-3 paper opens by naming the old regime's cost:

> "this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples"
> *(Brown et al., "Language Models are Few-Shot Learners," 2020)*

Thousands of hand-labeled examples *per task* — versus trillions of self-labeled examples for *every* task at once. That is not an improvement; it is a different game.

This training phase has a name you will meet constantly: **pretraining** — in SLP3's words, "learning knowledge about language and the world from iteratively predicting tokens in vast amounts of text." The "pre" signals that it happens *before* any task-specific shaping. SLP3 calls pretraining "the central new idea that makes LLMs possible." The industrial mechanics of it — what data, cleaned how, at what compute cost — are their own rung → [1320 pretraining at scale]; what happens *after* pretraining (instruction tuning, preference alignment) is the [1330]/[1335] pair. **[Established]**

**The misconception to kill here:** "somewhere, someone wrote the correct answers the model learned from." No. Nobody labeled anything during pretraining. The model's entire pretraining "teacher" is the raw text itself — which also means the teacher's *quality* is exactly the text's quality, no better. The director section returns to this, hard.

---

## Keeping score: the loss, and perplexity

A learning loop needs a score to improve against ([0600](../00-foundations/0600_what-it-means-to-learn.md)'s error-reducing loop; made concrete as a **loss function** — one number measuring how wrong the model currently is — at [1000](1000_machine-learning-from-examples.md)). The language model's score is beautifully direct:

> "large language models are trained with cross-entropy loss, also called the negative log likelihood loss. At time t the cross-entropy loss is the negative log probability the model assigns to the next word in the training sequence, - log p(wt+1)."
> *(Jurafsky & Martin, SLP3, Ch. 8)*

Unpack the jargon gently. **Cross-entropy** (general: an information-theory measure of how far your predicted probabilities are from reality; here: the LM's training loss) you already met as *surprise* at [0300](../00-foundations/0300_information-and-entropy.md). **Negative log probability** sounds fearsome but reads simply: take the probability the model gave to the word that *actually came next*, and convert it to a penalty — a probability of 1 (certain, correct) costs 0; smaller probabilities cost more, and the cost climbs steeply toward infinity as the probability approaches 0. In one sentence: **the model is punished by exactly how surprised it was by the true next word.**

Then the standard machinery takes over:

> "The weights in the network are adjusted to minimize the average CE loss over the training sequence via gradient descent."
> *(Jurafsky & Martin, SLP3, Ch. 8)*

(**Gradient descent** — nudge every knob a little in the direction that reduces the error, repeat billions of times; full home at [1000](1000_machine-learning-from-examples.md). The network doing the predicting is a deep neural net — [1100](1100_neural-networks-deep-learning.md); *which* architecture, and why one particular design won, is the next big rung → [1310 attention & the transformer].)

There is also a human-friendly version of the same score, used to report how good a model is. It is called **perplexity**:

> "The perplexity (sometimes abbreviated as PP or PPL) of a language model on a test set is the inverse probability of the test set (one over the probability of the test set), normalized by the number of words (or tokens)."
> *(Jurafsky & Martin, SLP3, Ch. 3)*

Gloss the pieces: **test set** — held-out text the model never trained on ([1000](1000_machine-learning-from-examples.md)'s honest-exam idea); **inverse** — one divided by the number, so *higher probability ⇒ lower perplexity*; **normalized** — averaged per word, so long and short texts compare fairly. The intuition that makes perplexity lovable: it behaves like **the number of words the model is effectively choosing between at each step**. A perplexity of 100 means each next word is, on average, as hard for the model as picking from 100 equally likely options. A perfect predictor would sit at 1. As the textbook puts it:

> "the higher the probability of the word sequence, the lower the perplexity. Thus the ... lower the perplexity of a model on the data, the better the model."
> *(Jurafsky & Martin, SLP3, Ch. 3)*

Why give perplexity space on this rung? Because it is **the scoreboard of the whole LLM era**. When you later read that loss falls smoothly and predictably as models grow ([1322 scaling laws]), *this number* is the thing falling. Prediction quality is the field's heartbeat, and perplexity is how it's taken. (What perplexity does *not* measure — usefulness, truthfulness, task success — is the opening problem of [1345 evaluating LLMs].) **[Established]**

---

## Predict, add, repeat: how text comes out

So far the model only *scores* possible next words. How does a scorer produce an essay? By the simplest loop imaginable: **pick a next word from the distribution, append it to the text, and ask the question again** — now with your own last word as part of the context. SLP3:

> "the model is conditioning on both the priming context and its own subsequently generated outputs"
> *(Jurafsky & Martin, SLP3, Ch. 7)*

("**Conditioning on**" = treating as given; the model's next prediction takes your prompt *and everything it has already written* as the context. "**Priming context**" = the text you started it with — the prompt.) This left-to-right, feed-yourself-your-own-output style is called **causal** (general: about cause and effect; here: each word may depend only on what came *before* it, never on the future) or **autoregressive** generation (general: "autoregressive" = predicting each element of a sequence from the previous elements; here: each token from all earlier tokens). The architecture family built around it:

> "The decoder is the architecture we've introduced above. It takes as input a series of tokens, and iteratively generates an output token one at a time. The decoder is the architecture used to create large language models like GPT, Claude, Llama, and Mistral."
> *(Jurafsky & Martin, SLP3, Ch. 7 — the model list is a 2026 snapshot)*

(The **decoder** is the name of this generate-left-to-right family; its siblings that read text in both directions are met at [1318 pretraining objectives].) Three consequences of this loop are worth fixing in memory now, because they explain behaviors you will see constantly:

1. **Generation is genuinely one token at a time.** The stream you watch in a chat window is not a display trick; it is the mechanism. At each step there is exactly one distribution and one choice. There is no separate "plan the whole essay" module in the loop itself. (Whether *planning-like computation* still happens inside the single step, and how models are now given explicit room to think, is the [1338 reasoning] story — don't pre-judge it from the mechanism alone.)
2. **Its own words become its context.** An early word choice steers everything after it — errors can compound, and style locks in. This one fact will echo all the way to agent design ([1365], where the loop's compounding-error problem becomes the central engineering challenge).
3. **"Pick from the distribution" is a choice you make.** Always take the single most likely word (**greedy decoding**) and the text is dull and repetitive; sample with too much freedom and it rambles. The knobs (**temperature**, **top-p** — dials for how adventurous the draw is) live with the cluster's practical rungs; what matters here is that **randomness is a dial, not a defect** — the model is a distribution, and *some* choice of how to draw from it must be made.

**What this rules out:** the model, at this level, has no goals, no memory beyond its context, no self. It is a probability-of-next-token machine run in a loop. Everything that *looks* like goals and memory is built on top — and the honest boundary of the bare object is rung [1355]. **[Established]**

---

## The deep reason it works: prediction *is* compression

Now the rung's deepest idea — the one that upgrades "neat trick" into "candidate principle of intelligence."

Refresher first: [0300](../00-foundations/0300_information-and-entropy.md) built the general bridge — *to predict well is to find structure, finding structure is what removes surprise (entropy), and removing surprise is exactly what compression does; some argue that is also what understanding is.* That was the claim. This is the promised return of the math, on the exact machine this cluster studies.

MacKay's information-theory textbook states the prediction–compression identity from the compression side:

> "Intuitively, compression works by taking advantage of the predictability of a file."
> *(MacKay, ITILA, Ch. 2)*

> "A data compression program that compresses this file must, implicitly or explicitly, be addressing the question `What is the probability that the next character in this file is a 1?'"
> *(MacKay, ITILA, Ch. 2)*

Sit with that second sentence. **Any** compressor, to work at all, must be — openly or secretly — a next-symbol predictor. MacKay states it as a law of his whole subject: "One of the themes of this book is that data compression and data modelling are one and the same" *(ITILA, Ch. 2)*. And the construction runs forward too: information theory has a standard recipe (**arithmetic coding** — a method that turns probabilities directly into short binary codes) where you plug in a predictor and get a compressor:

> "As each symbol is produced by the source, the probabilistic model supplies a predictive distribution over all possible values of the next symbol"
> *(MacKay, ITILA, Ch. 6)*

> "The encoder makes use of the model's predictions to create a binary string."
> *(MacKay, ITILA, Ch. 6)*

Put the two directions together and the conclusion is exact, not poetic: **a language model and a text compressor are the same mathematical object wearing different clothes.** The LM's training loss (negative log probability of the true next token) *is*, when the log is taken base-2, exactly the number of bits that token would cost under the matched code. Training a model to predict the internet **is** training it to compress the internet. **[Established — this part is mathematics.]**

### From compression to intelligence — the live wire

This is the **live wire** of the section (the wire still carrying current — the part you must handle with care). Why does this identity electrify people? Because "compresses the internet well" has a long-proposed second reading: *understands the world well enough to summarize it*. Shane Legg — who co-founded DeepMind, and whose 2008 thesis proposed measuring intelligence by exactly this kind of text-prediction/compression test — drew the line explicitly when his interviewer pointed out that LLM training matches his old proposal:

> "if you have a fantastically good sequence predictor, some approximation of Solomonoff induction, then going from that to a very powerful, very general AGI system is just sort of another step. You've actually solved a lot of the problem already. And I think that's what we're seeing today, actually, that these incredibly powerful foundation models are incredibly good sequence predictors. They're compressing the world based on all this data"
> *(Shane Legg, Dwarkesh Podcast, 2023)*

(**Solomonoff induction** — a theoretical ideal predictor from the 1960s that formalizes "the best possible next-symbol guesser"; it is **uncomputable** — no machine can actually run it, in the exact [0400](../00-foundations/0400_computation.md) sense — so Legg's point is that LLMs are a *practical approximation* of it. **Foundation model** — an industry term for a huge pretrained model that downstream systems build on; full home → [1320].) Note his framing carefully: prediction gets you *a lot of the problem*, with agency added *on top* — the same "built on top" boundary this rung keeps drawing. **[Likely]** as a research program; **[Contested]** as a claim about what today's models have actually achieved.

### How dramatic is the squeeze? (and the catch)

Andrej Karpathy — a founding OpenAI researcher — gives the concrete numbers, and in the same breath the honest caveat:

> "the compression is dramatic. You're taking 15 trillion tokens and you're compressing it to just your final neural network of a few billion parameters. Obviously it's a massive amount of compression going on. So I refer to it as a hazy recollection of the internet documents."
> *(Andrej Karpathy, Dwarkesh Podcast, 2025 — figures are a 2025-era snapshot)*

Fifteen trillion tokens in; a few billion parameters out — a squeeze of several thousand to one. Two lessons at once:

- **The squeeze is why it can't be memorizing.** There is physically no room to store the training text. To score well anyway, the model is *forced* to extract reusable structure — grammar once, arithmetic once, the pattern behind a million examples instead of the examples. **Compression pressure is generalization pressure.** This resolves the objection "isn't it just regurgitating its training data?" — mostly, it *can't*. (Where memorization does still happen and leak — rare, repeated strings — is a real but bounded phenomenon; details with the pretraining rung.)
- **The squeeze is lossy, and that's a feature-and-a-bug.** "Hazy recollection" is precise: the model keeps the *gist* and sheds the *particulars*. That is why it is genuinely not a database — and why asking it for an exact citation or an exact quote invites trouble. The full anatomy of that failure mode (and why it is intrinsic, not a patch-away bug) is rung [1342 hallucination]; the honest boundary of the object is [1355].

---

## From LM to LLM: the moment "large" changed the meaning

Everything above was true of small language models for decades. What earned the extra **L** — and reorganized the entire field — was the discovery of what happens when you push the *same objective* to enormous scale. The GPT-3 paper is the historical marker:

> "we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model"
> *(Brown et al., 2020)*

> "For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model."
> *(Brown et al., 2020)*

("**Non-sparse**" — a model that uses *all* its parameters on every token; the sparse alternative, where each token wakes only a few experts, is rung [1350 mixture-of-experts].) Decode the second quote, because it announces something genuinely strange. "**Without any gradient updates**" = with training completely finished, weights frozen. "**Few-shot demonstrations ... purely via text interaction**" = you *show* the model a few examples of a brand-new task *inside the prompt*, and it performs the task — having never been trained on it. A pure next-word predictor, asked only to continue text, started doing translation, arithmetic, and word-puzzles *because doing the task well was the most plausible continuation of the prompt*.

Nobody engineered that. It fell out of the objective at scale — and it is the cleanest evidence that "predict the next token" quietly builds machinery far more general than the task sounds. Why *this* example as the rung's closer? Because it hands the baton to the entire rest of the cluster: *how* capability grows with scale (and whether the growth is smooth or jumpy) is [1322 scaling laws & emergence]; *what* this no-training-needed task-learning is and how far it goes is [1325 in-context learning]; and the craft of steering a frozen predictor with words alone is [1328 prompting]. **[Established as a finding; its interpretation → 1358.]**

---

## ⚠️ Honesty box

The next-token idea attracts two opposite hype-failures: breathless over-claiming ("it understands everything") and smug under-claiming ("it's just autocomplete"). Both sides, at full force:

- **"It's just autocomplete" is not a rebuttal — but it's not wrong, either.** The mechanism *is* next-token prediction, full stop; nothing hidden. The compression argument above shows why that mechanism is forced to build real structure — and Legg's line shows serious researchers treating great prediction as *most of* the road to general intelligence. But "forced to build structure" is not "understands like you do," and the gap between those two claims is a genuinely open research question, not a settled one in either direction. **[Contested — the full debate has its own rung, 1358.]**
- **The objective is plausibility, not truth.** The loss rewards the *probable* continuation of the training text, and the training text contains errors, fictions, and lies. A perfectly-trained next-token predictor of the internet would reproduce the internet's untruths *by design*. The mechanics of that failure mode → [1342]. **[Established]**
- **The teacher includes its prejudices.** Remember SLP3's fifth blank: "The professor said that ___ → *he*." The same channel that teaches ontology and math teaches every statistical bias in the corpus. There is no filter in the objective itself. **[Established]**
- **Nothing here says the model keeps learning.** Pretraining ends; weights freeze; GPT-3's whole point was doing tasks *without* weight changes. The apparent "learning" in a conversation is conditioning, not training. The boundary — frozen weights, finite context — is rung [1355]. **[Established]**
- **Snapshot warnings.** "GPT, Claude, Llama, Mistral," "175 billion parameters," "15 trillion tokens" — all dated snapshots (2020–2025 figures), useful as scale anchors, not as current facts. The next-token *idea* is the durable part; every number around it ages fast.

---

## How a director uses this

The next-token idea is unusually decision-relevant, because almost every LLM behavior traces back to it in one hop:

- **When a model surprises you — good or bad — ask the objective's question:** *"what continuation of this text was most plausible under the training data?"* That single question explains fluent nonsense (plausible ≠ true), format-copying (your prompt's style is context), and few-shot magic (your examples made the task the plausible continuation). It is the closest thing to an X-ray you get.
- **You are what you train on — so the data is a directing decision, not a detail.** Self-supervision means the corpus *is* the teacher. Karpathy, on what that teacher actually looks like from inside a frontier lab: "the training data is the internet, which is really terrible... you look at a random internet document, it's total garbage" *(Dwarkesh Podcast, 2025)*. Whoever chooses and cleans the data chooses what the model knows and believes. When you direct any training effort, the data decisions are yours to own, never to delegate blindly.
- **Know which scoreboard you're reading.** Loss/perplexity measures *prediction* quality; your product needs *task* quality — and the two can diverge. A model can predict beautifully and still fail your use case. Never accept a perplexity-style number where a task evaluation ([1345], [1372]) is what matters.
- **Respect the loop's economics.** One token per step means output length ≈ cost and **latency** (the wait time before and during a response); and the model re-reads its context to produce every single token. This is why context size and output length dominate your bill — mechanics at [1305] (tokens) and [1355] (context window).
- **What you delegate:** implementing, training, and serving the predictor — mature engineering you rent or hire. **What you own:** the choice of training data and objective, the evaluation that decides "good enough," and the judgment call on how much to trust the *understanding*-shaped behavior of a plausibility machine.

---

## The cluster ahead (a map, not lessons)

Everything this rung deferred, in reading order — each a full rung of its own (all enumerated with scopes in the [CURRICULUM](../CURRICULUM.md); links go live as each is written):

**[1305]** tokens & tokenization · **[1308]** the counting-based ancestors (n-grams) and the wall they hit · **[1310]** attention & the transformer — the architecture that computes the distribution · **[1312]** how order is injected · **[1315]** embeddings, the geometry of meaning · **[1318]** the three pretraining bets (GPT vs BERT vs T5) · **[1320]** pretraining at industrial scale · **[1322]** scaling laws & emergence · **[1325]** in-context learning · **[1328]** prompting · **[1330]/[1332]/[1335]** shaping the raw predictor (instruction tuning, efficient tuning, preference alignment) · **[1338]** reasoning & test-time compute · **[1342]** hallucination · **[1345]** evaluation · **[1348]/[1350]/[1352]** multimodal, mixture-of-experts, post-transformer bets · **[1355]** the honest boundary of the object · **[1358]** the understanding debate.

## Connections

- **If you keep only three things:** ① a language model = a probability distribution over the next token, run in a loop; ② the text labels itself — that's why the whole internet could be a teacher; ③ predicting well and compressing well are the same math — which is why "just autocomplete" undersells it, and why how far it goes is the field's biggest open question.
- **Stands on:** [0300 information & entropy](../00-foundations/0300_information-and-entropy.md) *(the predict⇒compress⇒understand bridge, now with its math)* · [0500 probability](../00-foundations/0500_probability-and-uncertainty.md) *(distributions)* · [0600 learning](../00-foundations/0600_what-it-means-to-learn.md) *(self-supervision as a flavor of learning)* · [1000 ML](1000_machine-learning-from-examples.md) *(model/loss/gradient descent/held-out test)* · [1100 neural nets](1100_neural-networks-deep-learning.md) *(the function that does the predicting)*.
- **Where to go next:** **the machinery** — what network turns context into that distribution → [1310 attention & the transformer]; **the fuel line** — what "trained on the internet" really involves → [1320]; **the payoff question** — what scale bought and whether it keeps paying → [1322].
- **Contested?** LM definition, self-supervision, cross-entropy/perplexity, autoregression, prediction=compression — **[Established]**. "Great prediction ≈ most of the road to AGI" — **[Likely→Contested]** (Legg's program). "Prediction ⇒ understanding" — **[Contested, open → 1358]**.

## Proof-of-learning *(do one, from memory)*

1. A friend says "LLMs just predict the next word, so they can't really know anything." Using the fill-in-the-blank game, show what's wrong with the inference — and then state honestly which part of your friend's skepticism *survives*.
2. Explain why pretraining needed no human labelers, and what that implies about who the model's real "teacher" is.
3. The model assigned probability 0.001 to the word that actually came next. Say what happens next in training, and why the same number can be read as "bits of compression cost."
4. Why does a 15-trillion-token diet squeezed into a few billion parameters *guarantee* the model is not a lookup table — and what everyday LLM failure does the same squeeze predict?
5. GPT-3 translated text without ever being trained to translate. Explain the mechanism in one sentence built around the phrase "plausible continuation."

## Revision notes

*Newest first — read only what moved.*
- `rev 2 (2026-07-02)` — **grounded rewrite to the v2.5 standard (the proof-of-standard module)**: scope narrowed per [CURRICULUM](../CURRICULUM.md) A3.4 to the next-token idea itself (tokenization/transformer/tuning/scaling/hallucination/understanding-debate split to rungs 1305–1358, per HARD_RULES §4.3); every claim now grounded in and quoted verbatim from the corpus (SLP3 Ch. 3/7/8, MacKay ITILA, GPT-3, Legg & Karpathy interviews); prediction=compression given its full mechanism (the promised return of 0300's bridge); file renamed from `1300_language-models-how-llms-work.md`. Old whole-story coverage preserved in git history; its concepts re-homed via the registry as the cluster is built.
- `rev 1 (2026-06-27)` — created (pre-corpus standard; covered the whole LLM story in one file).

---
*Concepts introduced → logged in [CONCEPT_REGISTRY](../CONCEPT_REGISTRY.md). Announced in [WHATS_NEW](../WHATS_NEW.md). This opens the language-model cluster (1300–1358); the machine that computes the distribution is next → [1310].*
