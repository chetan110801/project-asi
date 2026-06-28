# ▶ SESSION 6 START PROMPT — widen course coverage to all domains × many universities
**Paste the block below into a fresh session.** Created 2026-06-28 after gathering session 5.
Companion to [`_UNIVERSITY_PLAYLISTS.md`](_UNIVERSITY_PLAYLISTS.md) (catalog/IDs), [`_COVERAGE_MAP.md`](_COVERAGE_MAP.md) (board), [`_CORPUS_BUILD.md`](_CORPUS_BUILD.md) (method), and the local [`../library/_NEXT-SESSION-HANDOFF.md`](../library/).

> **Honesty note:** the university/channel list below is **candidate targets to SCAN**, not verified playlist IDs. The new session must pull each channel's `/playlists` and **validate every ID live** (playlist_count + first title) before queueing — exactly as session 5 did. The two driver hardenings and the PO-token caption gap are repeated on purpose; a cold session won't otherwise know them.

---

```
Continue the project-asi grounding-corpus build — gathering SESSION 6: collect MANY more
university course playlists, across ALL domains & sub-domains, from MANY universities.

START BY READING (in order):
- RESOURCES/library/_NEXT-SESSION-HANDOFF.md  (esp. the §5b "SESSION 5 DONE" bullet — driver
  hardenings, the NYU-SP20 PO-token gap, and the ~100-entry flat-list cap)
- RESOURCES/corpus/_CORPUS_BUILD.md  (method + §7 handoff procedure)
- RESOURCES/corpus/_UNIVERSITY_PLAYLISTS.md  (what's already collected; To-ADD ID table)
- RESOURCES/corpus/_COVERAGE_MAP.md  (status board + per-session sections)
- INSTRUCTIONS/HARD_RULES.md  (binding standard: durability filter, legality, media rule)

WHERE WE ARE: corpus/courses/ already holds 62 courses / 1,617 transcripts (Stanford+MIT
spine + full long-tail, Berkeley CS285/CS182, CMU 11-785/11-711, NYU, Caltech, 3B1B, fast.ai,
Stanford CS25, etc.). Sessions 1–5 done. Spine modules 0100→1300 written but NOT yet
re-grounded. Do NOT write modules this session — keep gathering.

GOAL THIS SESSION: widen course coverage to the rest of the map — more universities and the
domains/sub-domains we haven't pulled lecture courses for yet. Candidate targets (scan each
channel's /playlists, pick the durable full-lecture courses, skip dups of editions we hold):
- Harvard: CS50 + CS50-AI (Python), CS50-ML, Harvard Stat110 (Blitzstein), CS197.
- Stanford: CS25 newer versions, CS520 knowledge-graphs, CS131/CS231A vision, CS238/AA228
  decision-making, CS379C, CS520, MLSys/SysML, CS324, EE364B, STATS thread, MS&E.
- MIT OCW: 6.034x, 6.S965 TinyML, 6.S898 deep-learning-theory, 9.66 computational-cognition,
  18.S191 (Julia/scientific-ML), 8.05/8.06 quantum, 6.041 probability (Tsitsiklis), 2.x
  robotics/controls, 7.x biology, 8.x physics, 14.x economics — across math/physics/bio/econ.
- Berkeley: CS182 newer, CS188 AI, CS189 ML, Full Stack Deep Learning, EECS127 optimization.
- CMU: 10-708 PGM, 10-725 convex-opt, 11-747 neural-NLP, 15-x systems, robotics (16-x).
- Others: UMich EECS498 Deep-Learning-for-Vision (Justin Johnson), UW CSE, Cornell, Princeton
  COS, Oxford/DeepMind, Cambridge, EPFL, Toronto (Hinton/CSC2541), Tübingen (Geiger),
  Imperial, NPTEL (IIT) for math/physics/EE, 3B1B Essence-of-Calculus, StatQuest, Steve
  Brunton (control/dynamics/SINDy), Artem Kirsanov (neuro), and lab channels.
- Cover the under-served domains: neuroscience, cognitive-science, math/optimization,
  information theory, quantum, robotics/control, biology, materials, physics, economics,
  complex systems — not just AI/ML.

METHOD (reuse the proven, resumable toolchain — rebuild it in scratchpad from the session-5
copies; they still work):
- ytchannel.sh + vtt2txt.pl + runbatch.sh (driver). KEEP the session-5 hardenings:
  `--write-subs --write-auto-subs --sub-langs "en,en-orig,en-en"`, and 429-on-retry leaves a
  video UNMARKED (don't false-.done it). Run ONE queue at a time, BASE sleep >=2.6s.
- Per playlist: yt-dlp --flat-playlist --print "%(id)s|%(title)s" <playlist-url> -> feed to
  the driver -> corpus/courses/<slug>/. yt-dlp at the Python314 path (call via full python).
- VALIDATE every playlist ID live (playlist_count + first title) before queueing; flat-list
  caps ~100 for segment-heavy playlists (note it, bulk is fine).
- After each run, QC: compare on-disk *.txt counts vs expected; re-run any course with empties
  (clears false .done). Some auto-only-caption videos are PO-token-gated and will stay empty
  in this env — accept + document, don't fight it.

RULES (unchanged): durability filter (timeless principles / grounded intuition, full lectures
> 3-min segment spam); legality absolute (course-public auto-subs / open-licensed only, no
pirate mirrors); skip what the owned backup already holds and dup editions (keep newest);
ALL corpus text stays git-ignored — only the tracking markdown is committed.

FINISH: tick _UNIVERSITY_PLAYLISTS.md (add a session-6 ✅ block + new playlist-ID tables) and
_COVERAGE_MAP.md (session-6 section + totals); refresh _NEXT-SESSION-HANDOFF.md; commit the
tracking md to main in the docs(corpus): style. Work in a managed queue, expect hours, stop at
the token boundary and hand off cleanly.
```
