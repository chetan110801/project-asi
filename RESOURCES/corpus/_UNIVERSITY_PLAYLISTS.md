# University Course Playlists — scan & collection worklist
**Top-university full-course lecture playlists (YouTube) across our domains.** Scanned 2026-06-28 (gathering session 3) from each channel's `/playlists` tab via `yt-dlp --flat-playlist`. **The LIST is below; COLLECTION runs in a new session** (learner: "we can do this in a new session"). Method + resumable driver in §Method. Same rules as the rest of the corpus: transcripts are git-ignored local text, durability filter applies (timeless principles), use lectures for grounded intuition.

`Status: catalog ready · SPINE + WIDEN-TIER-1 (session 4) + FULL LONG-TAIL & TO-ADD CHANNELS (session 5) + ALL-DOMAIN × MANY-UNIVERSITIES WIDENING (session 6, 2026-06-29) COLLECTED · Created 2026-06-28 (v2.4, session 3)`

> **How to collect (next session):** rebuild `ytchannel.sh` + `vtt2txt.pl` (see §Method / `_CORPUS_BUILD.md` §4), then for each playlist below: `yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/playlist?list=<PLID>" > list.txt` → feed `list.txt` to `ytchannel.sh` with outdir `corpus/courses/<slug>/`. The driver is **resumable** (skips `.done_<id>` markers + existing files) — safe to re-run. Pace politely (YouTube 429s; one sub-lang per video, `--sleep-requests`, base sleep ≥2.5s). **Run channels/playlists in a managed queue, not all at once.**

---

## ✅ COLLECTED — gathering session 4 (2026-06-28): SPINE + WIDEN TIER-1 = 24 courses · 398 transcripts · 27 MB (`corpus/courses/`)
All git-ignored. Driver = `ytchannel.sh` + `vtt2txt.pl` (resumable; `.done_<id>` markers for genuine no-caption videos). One transient-429 storm hit the two 47-video playlists (CS224W, CS156) — markers cleared + re-run at slower pace recovered the rate-limited ones; the rest are genuine no-caption short clips.

**SPINE (14 courses · 217):**
- Stanford (7 · 111): CS229 `19` · CS230 `9` · CS231N `18` · CS224N `23` · CS234 `16` · CS336 `17` · CME295 `9`
- DeepMind×UCL (4 · 45) — **reused from the session-3 whole-channel pull (0 re-downloads), re-foldered in lecture order:** Intro-to-RL-2015 (Silver) `10` · RL-2018 (Hasselt) `10` · DL-2021 `13` · DL-2020 `12`
- MIT OCW (3 · 61): 6.7960 Deep Learning (F24) `24` · 9.13 The Human Brain `17` · 9.40 Neural Computation `20`

**WIDEN TIER-1 (10 courses · 181):**
- Stanford: CS224R Deep RL `19` · CS236 Deep Generative Models `18` · CS330 Meta-Learning `17` · CS329H ML-from-Human-Preferences `8` · CME296 Diffusion & Vision `8` · CS224W ML-with-Graphs `22` (25 no-caption clips skipped) · ECON295/CS323 AI-Awakening (Brynjolfsson) `5`
- NYU Deep Learning FL22 (LeCun & Canziani) `8` · Caltech CS156 Learning-From-Data (Abu-Mostafa) `16` (2 no-caption) · MIT RES.9-003 Brains, Minds & Machines `60`

---

## ✅ COLLECTED — gathering session 5 (2026-06-28): FULL LONG-TAIL + TO-ADD CHANNELS = 33 courses · 1,165 transcripts (`corpus/courses/`)
All git-ignored. Same driver (`ytchannel.sh`+`vtt2txt.pl`), now hardened: pulls **manual subs + `en`/`en-orig`/`en-en` auto** (`--write-subs --write-auto-subs`), and a 429-on-retry leaves the video **unmarked** (so a re-run retries it instead of falsely marking it done). Course corpus now = **62 folders · 1,617 transcripts · 68 MB**.

**Stanford long-tail (8 · 191):** CS221 AI `20` · CS224U NLU `50` · CS229M ML-Theory `20` · CS109 Probability `29` · EE364A Convex-Opt `18` · EE274 Data-Compression `18` · CS149 Parallel-Computing `19` · AA228V Safety-Critical `17`
**NYU (2 of 3 · 40):** SP21 (LeCun) `31` · AI-SP24 `9` · **SP20 = 0 (GAP — auto-only captions are now PO-token/impersonation-gated in this env; superseded by SP21 ✓ which is the newer full edition of the same course)**
**MIT long-tail (11 · 480):** 9.35 Perception `23` · 18.065 Matrix-Methods (Strang) `36` · 18.S096 Matrix-Calculus `17` · 18.404J Theory-of-Computation (Sipser) `25` · 6.006 Algorithms `32` · 6.S897 ML-Healthcare `25` · 7.91J Comp-Systems-Bio `22` · 16.412J Cognitive-Robotics `7` · 6.042J Math-for-CS `98` · 8.04 Quantum-I `97` · RES.6-012 Probability `98`  *(the last three are segment-style playlists; this yt-dlp build's flat-list caps at ~100 entries — bulk captured; a few short segment clips genuinely lack captions)*
**TO-ADD channels — now scanned + collected (11 · 454):** Berkeley CS285 Deep-RL (Levine) `99` · Berkeley CS182 Deep-Learning `66` · CMU 11-785 Intro-DL (S24, Raj) `28` · CMU 11-711 Advanced-NLP (Neubig) `23` · Stanford CS25 Transformers-United `50` · MIT 6.034 AI (Winston) `30` · MIT 18.06 Linear-Algebra (Strang) `36` · 3Blue1Brown Essence-of-Linear-Algebra `16` · 3Blue1Brown Neural-Networks (incl. transformers/attention chapters) `9` · fast.ai Practical-DL-2022 `8` · MIT 6.S191 Intro-DL (Amini, multi-year) `89`
> **Skipped (deliberate):** CMU 11-785 **Spring-2020** (overlaps the S24 we took — "keep newest") · Stanford **CS324 LLMs** (reading-based course, no clean lecture playlist; LLMs already covered by CS336/CME295/CS25) · CS336 Spring-2026 & CS224N-2023 (newer/older dups of editions already held). Playlist IDs for all collected To-ADD courses are in the new §"To-ADD — collected" table below.

**⬅️ REMAINING:** effectively **none** of the catalogued long-tail. Only loose ends: NYU **SP20** (env-blocked, low value), 2 8.04 + a handful of genuinely caption-less segment clips.

---

## ✅ COLLECTED — gathering session 6 (2026-06-29): ALL-DOMAIN × MANY-UNIVERSITIES WIDENING = 31 courses · 1,050 transcripts (`corpus/courses/`)
All git-ignored. Same hardened driver (`ytchannel.sh`+`vtt2txt.pl`+`runbatch.sh`; manual + `en`/`en-orig`/`en-en` auto subs; 429-on-retry leaves video unmarked). **Every playlist ID validated live (count + first title) before queueing.** Ran in **4 managed queues, one at a time**, base sleep 2.6 s. Course corpus now = **93 folders · 2,667 transcripts · 99 MB**. This session widened past AI/ML into the **under-served domains** (probability, quantum, physics, economics, biology, robotics/control, neuroscience, cognitive-science, applied-math/calculus, **efficient-ML/TinyML**) and added **4 universities not previously represented** (Harvard, UMich, Cornell, Tübingen) + 2 expert channels (Steve Brunton, Artem Kirsanov) + the MIT HAN-Lab efficient-ML course.

**Q1 — core university full-lecture courses (14 · 430):** Harvard STAT110 Probability (Blitzstein) `35` · UC Berkeley CS188 AI `21` · UMich EECS498-007 Deep-Learning-for-CV (Johnson) `22` · CMU 10-708 Probabilistic-Graphical-Models `29` · CMU 11-747 Neural-Nets-for-NLP (Neubig) `25` · MIT 6.041SC Probabilistic-Systems (Tsitsiklis) `76` · MIT 6.832 Underactuated-Robotics (Tedrake) `23` · MIT 7.016 Introductory-Biology `35` · MIT 9.14 Brain-Structure `35` · MIT 14.01 Microeconomics `26` · MIT 14.02 Macroeconomics `25` · MIT 2.003SC Engineering-Dynamics `38` · MIT 18.02 Multivariable-Calculus `35` · MIT 24.08J Philosophical-Issues-in-Brain-Science `5`
**Q2 — expert intuition channels + physics/quantum (13 · 481):** 3Blue1Brown Essence-of-Calculus `11` · 3B1B Differential-Equations `8` · Steve Brunton Control-Bootcamp `36` · Brunton Physics-Informed-ML `23` · Brunton Data-Driven-Dynamical-Systems `24` · Brunton Eng-Math-DiffEq-&-Dynamical-Systems `49` · Brunton Singular-Value-Decomposition `43` · Artem Kirsanov Neuroscience `26` · Kirsanov AI-&-ML `9` · MIT 8.05 Quantum-Physics-II `24` · MIT 8.03SC Vibrations-&-Waves `33` · MIT 8.06 Quantum-Physics-III `100` · MIT 8.01SC Classical-Mechanics `95`
**Q3 — additional universities (2 · 87):** Cornell CS4780 Machine-Learning (Weinberger) `41` · University of Tübingen Deep-Learning (Geiger) `46`
**Q4 — efficient-ML domain + flagship AI intro (2 · 52):** MIT 6.5940 TinyML & Efficient-Deep-Learning (HAN Lab, F23) `45` · Harvard CS50 Introduction-to-AI-with-Python (2023) `7`
> **Benign empties (all documented, not failures):** Berkeley CS188 is a *curated "best-of"* playlist — 15 of its 36 entries are `NA`/private/deleted placeholders + 1 caption-off intro (21 real lectures captured). MIT 8.06/8.01 are **segment-style** playlists this yt-dlp build flat-list-caps at ~100 (bulk captured). A few genuinely caption-less clips across 3B1B-calculus(1)/Brunton(4)/MIT-8.05(2)/8.03(3)/8.01(5)/2.003(1). **No rate-limit losses** — no 429 storms this session.
> **Skipped (deliberate):** a generic "Stanford Lectures" mixed playlist (`PLoROMvodv4rM2uc1Cg9oTblVaF-EEOlw-`) whose first entries are AA228V — **dups the `aa228v-safety-critical` we already hold**; Toronto CSC2516/421 (no clean public lecture playlist found).

### Session-6 playlist IDs (all validated live 2026-06-29)
| Course | Playlist ID | got |
|---|---|---|
| Harvard STAT 110 Probability (Blitzstein) | `PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo` | 35 |
| UC Berkeley CS188 Introduction to Artificial Intelligence | `PLtFb24pIhyHv6d6OqDr_tVaygbj86mCGA` | 21 |
| UMich EECS 498-007 Deep Learning for Computer Vision (Johnson) | `PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r` | 22 |
| CMU 10-708 Probabilistic Graphical Models | `PLhuJd8bFXYJtxHjuWrnTPgvh88mJ_oaVk` | 29 |
| CMU 11-747 Neural Nets for NLP (Neubig) | `PLbdKUKMAnh9Qqs5uwEBDfRb_L3YaLbRKq` | 25 |
| MIT 6.041SC Probabilistic Systems Analysis (Tsitsiklis, F13) | `PLUl4u3cNGP60A3XMwZ5sep719_nh95qOe` | 76 |
| MIT 6.832 Underactuated Robotics (Tedrake, S09) | `PL58F1D0056F04CF8C` | 23 |
| MIT 7.016 Introductory Biology (F18) | `PLUl4u3cNGP63LmSVIVzy584-ZbjbJ-Y63` | 35 |
| MIT 9.14 Brain Structure and Its Origins (S14) | `PLUl4u3cNGP62ABe0O-0qtaHHxyKQi1ZwR` | 35 |
| MIT 14.01 Principles of Microeconomics (F23) | `PLUl4u3cNGP60V7HxLYRaJMbFzP77bzEjb` | 26 |
| MIT 14.02 Principles of Macroeconomics (S23) | `PLUl4u3cNGP62EXoZ4B3_Ob7lRRwpGQxkb` | 25 |
| MIT 2.003SC Engineering Dynamics (F11) | `PLUl4u3cNGP62esZEwffjMAsEMW_YArxYC` | 38 |
| MIT 18.02 Multivariable Calculus (F07) | `PL4C4C8A7D06566F38` | 35 |
| MIT 24.08J Philosophical Issues in Brain Science (S09) | `PL8FD2F66DF27A663D` | 5 |
| 3Blue1Brown Essence of Calculus | `PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr` | 11 |
| 3Blue1Brown Differential Equations | `PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6` | 8 |
| Steve Brunton Control Bootcamp | `PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m` | 36 |
| Steve Brunton Physics Informed Machine Learning | `PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa` | 23 |
| Steve Brunton Data-Driven Dynamical Systems (with ML) | `PLMrJAkhIeNNR6DzT17-MM1GHLkuYVjhyt` | 24 |
| Steve Brunton Eng-Math: Differential Equations & Dynamical Systems | `PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA` | 49 |
| Steve Brunton Singular Value Decomposition | `PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv` | 43 |
| Artem Kirsanov Neuroscience Exploration | `PLgtmMKe4spCMzkiVa4-eSHVk-N4SC8r9K` | 26 |
| Artem Kirsanov AI & Machine Learning | `PLgtmMKe4spCPsxyMpg-sxf3EcbsFYlzPK` | 9 |
| MIT 8.05 Quantum Physics II (F13) | `PLUl4u3cNGP60QlYNsy52fctVBOlk-4lYx` | 24 |
| MIT 8.03SC Physics III: Vibrations and Waves (F16) | `PLUl4u3cNGP61R5sPDPKVfcFlu95wSs2Kx` | 33 |
| MIT 8.06 Quantum Physics III (S18) | `PLUl4u3cNGP60Zcz8LnCDFI8RPqRhJbb4L` | 100 |
| MIT 8.01SC Classical Mechanics (F16) | `PLUl4u3cNGP61qDex7XslwNJ-xxxEFzMNV` | 95 |
| Cornell CS4780 Machine Learning for Intelligent Systems (Weinberger, SP17) | `PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS` | 41 |
| University of Tübingen Deep Learning (Andreas Geiger, 2020-21) | `PL05umP7R6ij3NTWIdtMbfvX7Z-4WEXRqD` | 46 |
| MIT 6.5940 TinyML & Efficient Deep Learning (HAN Lab, Fall 2023) | `PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB` | 45 |
| Harvard CS50 Introduction to AI with Python (2023) | `PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm` | 7 |

> **Considered but skipped this session:** Berkeley CS189 ML (no public YouTube playlist — bCourses-gated) · NPTEL/IIT Deep Learning (Khapra, 156 segment clips — DL is our most-saturated domain; adding only for the institution badge fails the anti-redundancy/durability filter) · Toronto CSC2516/421 (no clean public lecture playlist).

---

## Stanford Online (`@stanfordonline`) — AI/ML spine
| Course | Playlist ID |
|---|---|
| CS229 Machine Learning (Spring 2022) | `PLoROMvodv4rNyWOpJg_Yh4NSqI4Z4vOYy` |
| CS230 Deep Learning (Autumn 2025) | `PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X` |
| CS231N Deep Learning for Computer Vision (2025) | `PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16` |
| CS224N NLP with Deep Learning (Spring 2024, Manning) | `PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D` |
| CS224N NLP with Deep Learning (2023) | `PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4` |
| CS234 Reinforcement Learning (Spring 2024, Brunskill) | `PLoROMvodv4rN4wG6Nk6sNpTEbuOSosZdX` |
| CS224R Deep Reinforcement Learning | `PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL` |
| CS336 Language Modeling from Scratch (2025) | `PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_` |
| CS336 Language Modeling from Scratch (Spring 2026) | `PLoROMvodv4rMqXOcazWaTUHhq-yembLCV` |
| CME295 Transformers & Large Language Models (Autumn 2025) | `PLoROMvodv4rOCXd21gf0CF4xr35yINeOy` |
| CME296 Diffusion & Large Vision Models | `PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu` |
| CS236 Deep Generative Models (2023, Ermon) | `PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8` |
| CS221 Artificial Intelligence: Principles & Techniques (Autumn 2025) | `PLoROMvodv4rMeDqwS1yFl3j3sR_-MQNEN` |
| CS330 Deep Multi-Task & Meta Learning (Autumn 2022, Finn) | `PLoROMvodv4rNjRoawgt72BBNwL2V7doGI` |
| CS329H Machine Learning from Human Preferences (Autumn 2024) | `PLoROMvodv4rNm525zyAObP4al43WAifZz` |
| CS224W Machine Learning with Graphs (Leskovec) | `PLoROMvodv4rOP-ImU-O1rYRg2RFxomvFp` |
| XCS224U Natural Language Understanding (2023) | `PLoROMvodv4rOwvldxftJTmoR3kRcWkJBp` |
| CS229M Machine Learning Theory (2021) | `PLoROMvodv4rP8nAmISxFINlGKSK4rbLKh` |
| **Math/optim/info:** CS109 Probability for CS (2022, Piech) | `PLoROMvodv4rOpr_A7B9SriE_iZmkanvUg` |
| EE364A Convex Optimization (2023, Boyd) | `PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h` |
| EE274 Data Compression: Theory & Applications (2023) | `PLoROMvodv4rPj4uhbgUAaEKwNNak8xgkz` |
| **Systems:** CS149 Parallel Computing (2023) | `PLoROMvodv4rMp7MTFr4hQsDEcX7Bx6Odp` |
| **Society/safety:** ECON295/CS323 The AI Awakening (2024, Brynjolfsson) | `PLoROMvodv4rN1Xruk6giv3dapv0WIdz68` |
| AA228V Validation of Safety-Critical Systems (2025) | `PLoROMvodv4rOq1LMLI8U7djzDb8--xpaC` |

## MIT OpenCourseWare (`@mitocw`) — DL / brain / math / theory / physics / bio
| Course | Playlist ID |
|---|---|
| 6.7960 Deep Learning (Fall 2024) | `PLUl4u3cNGP63URZnh5iqBzDTDYPUTQT-8` |
| 9.40 Introduction to Neural Computation (Spring 2018) | `PLUl4u3cNGP61I4aI5T6OaFfRK2gihjiMm` |
| 9.13 The Human Brain (Spring 2019) | `PLUl4u3cNGP60IKRN_pFptIBxeiMc0MCJP` |
| RES.9-003 Brains, Minds and Machines (Summer 2015) | `PLUl4u3cNGP61RTZrT3MIAikp2G5EEvTjf` |
| 9.35 Perception (Spring 2024) | `PLUl4u3cNGP62-9RweyYBIpkqfo5dfcuS8` |
| 18.065 Matrix Methods in Data Analysis, Signal Processing & ML (2018, Strang) | `PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k` |
| 18.S096 Matrix Calculus for Machine Learning and Beyond (IAP 2023) | `PLUl4u3cNGP62EaLLH92E_VCN4izBKK6OE` |
| 18.404J Theory of Computation (Fall 2020, Sipser) | `PLUl4u3cNGP60_JNv2MmK3wkOt9syvfQWY` |
| 6.006 Introduction to Algorithms (Spring 2020) | `PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY` |
| 6.042J Mathematics for Computer Science (Spring 2015) | `PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ` |
| RES.6-012 Introduction to Probability (Spring 2018) | `PLUl4u3cNGP60hI9ATjSFgLZpbNJ7myAg6` |
| 6.S897 Machine Learning for Healthcare (Spring 2019) | `PLUl4u3cNGP60B0PQXVQyGNdCyCTDU1Q5j` |
| 8.04 Quantum Physics I (Spring 2016) | `PLUl4u3cNGP60cspQn3N9dYRPiyVWDd80G` |
| 7.91J Foundations of Computational & Systems Biology | `PLUl4u3cNGP63uK-oWiLgO7LLJV6ZCWXac` |
| 16.412J Cognitive Robotics (Spring 2016) | `PLUl4u3cNGP62Bkdzwe7caTZC7soj7ZYvk` |
| *(354 MIT playlists scanned — `_pl_mitocw.txt`; also of note: 6.034 AI, 6.S191 Intro DL, 18.06 full Linear Algebra — add next session)* | — |

## DeepMind × UCL (`@GoogleDeepMind` playlists) — DL & RL lecture series
| Course | Playlist ID |
|---|---|
| Deep Learning Lecture Series 2021 | `PLqYmG7hTraZDVH599EItlEWsUOsJbAodm` |
| Deep Learning Lecture Series 2020 | `PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF` |
| Reinforcement Learning Course 2018 (Hado van Hasselt) | `PLqYmG7hTraZBKeNJ-JE_eyJHZ7XgBoAyb` |
| Introduction to Reinforcement Learning 2015 (David Silver) | `PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ` |

## NYU Deep Learning (`@alfcnz`, LeCun & Canziani)
| Course | Playlist ID |
|---|---|
| NYU Deep Learning FL22 | `PLLHTzKZzVU9d_3TcHbyiAjl5qCbpJR-o0` |
| NYU Deep Learning SP21 | `PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq` |
| NYU Deep Learning SP20 | `PLLHTzKZzVU9fAwRrnyu4QOd9KDqCE9c3y` |
| NYU Artificial Intelligence SP24 | `PLLHTzKZzVU9cH26X9VQ14lIA0aPwZiZTx` |

## Caltech (`@caltech`)
| Course | Playlist ID |
|---|---|
| CS156 Learning From Data (Abu-Mostafa) | `PLD63A284B7615313A` |

## To-ADD — COLLECTED session 5 (playlist IDs, all validated live 2026-06-28)
| Course | Playlist ID | got |
|---|---|---|
| Berkeley CS285 Deep Reinforcement Learning (Fall 2023, Levine) | `PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps` | 99 |
| Berkeley CS182 Deep Learning (Spring 2021, Levine) | `PL_iWQOsE6TfVmKkQHucjPAoRtIJYt8a5A` | 66 |
| CMU 11-785 Introduction to Deep Learning (Spring 2024, Raj & Singh) | `PLp-0K3kfddPxUJzAW0KxNNjGiK_hISFas` | 28 |
| CMU 11-711 Advanced NLP (Fall 2024, Neubig) | `PL8PYTP1V4I8D4BeyjwWczukWq9d8PNyZp` | 23 |
| Stanford CS25 Transformers United (V1–V6) | `PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM` | 50 |
| MIT 6.034 Artificial Intelligence (Fall 2010, Winston) | `PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi` | 30 |
| MIT 18.06 Linear Algebra (Spring 2005, Strang) | `PLE7DDD91010BC51F8` | 36 |
| 3Blue1Brown Essence of Linear Algebra | `PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab` | 16 |
| 3Blue1Brown Neural Networks (incl. transformers/attention chapters) | `PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi` | 9 |
| fast.ai Practical Deep Learning for Coders (2022, Howard) | `PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU` | 8 |
| MIT 6.S191 Introduction to Deep Learning (Amini, multi-year) | `PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI` | 89 |

**Deliberately skipped:** CMU 11-785 *Spring-2020* (`PLp-0K3kfddPzCnS4CqKphh-zT3aDwybDe`, overlaps S24 — keep newest) · Stanford **CS324 LLMs** (reading course, no clean lecture playlist; LLM coverage via CS336/CME295/CS25) · Berkeley Full-Stack-DL, CMU 10-708 PGM, Harvard CS50-AI, 3B1B Essence-of-Calculus, MIT 8.05/8.06 & 6.041 (optional future adds — quantum/probability already deep in corpus).

---

## Method (rebuild in the collecting session)
1. `ytchannel.sh <videolist> <outdir_abs> <label> [base_sleep]` — pulls `--write-subs --write-auto-subs --sub-langs "en,en-orig,en-en" --sub-format vtt` (session-5 hardening: grabs **manual** subs if present, else the `en`/`en-orig`/`en-en` auto track — many videos now expose auto-captions as `en-en` "English from English", which a bare `--sub-langs en` misses), cleans via `vtt2txt.pl` (strips cue numbers/timestamps/tags, de-dupes rolling captions), writes one `<id>_<slug>.txt` per video, `.done_<id>` marker for genuine no-caption videos. **A 429 that survives the retry leaves the video UNMARKED** (re-run retries it) — not falsely "done". Resumable.
   - **Known env limit (session 5):** some videos' captions are **auto-only and PO-token/impersonation-gated** — this yt-dlp build (no JS-runtime EJS solver / no `curl_cffi` impersonation) downloads a 101-byte empty VTT for them via the `android_vr` fallback. Manual-caption videos are unaffected. This is why NYU **SP20** (auto-only) yielded 0; install a JS runtime + `--remote-components ejs:github` + impersonation deps to recover such videos later.
2. `vtt2txt.pl` — VTT → de-duplicated plain text (see `_CORPUS_BUILD.md` §4).
3. Per playlist: dump `yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/playlist?list=<PLID>"` → feed to `ytchannel.sh`.
4. Tick this file + `_COVERAGE_MAP.md`; commit tracking md (transcripts stay git-ignored).

> **Durability filter:** lecture courses are deep + grounded — high value. But a single course is ~20–30 lectures × ~75 min; collect the **spine first** (CS229/CS230/CS231N/CS224N/CS234/CS336/CME295 + DeepMind RL/DL + MIT 6.7960 + neuro 9.13/9.40), then widen. Collect in a managed queue; expect hours.
