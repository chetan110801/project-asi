# University Course Playlists — scan & collection worklist
**Top-university full-course lecture playlists (YouTube) across our domains.** Scanned 2026-06-28 (gathering session 3) from each channel's `/playlists` tab via `yt-dlp --flat-playlist`. **The LIST is below; COLLECTION runs in a new session** (learner: "we can do this in a new session"). Method + resumable driver in §Method. Same rules as the rest of the corpus: transcripts are git-ignored local text, durability filter applies (timeless principles), use lectures for grounded intuition.

`Status: catalog ready · collection PENDING (next session) · Created 2026-06-28 (v2.4, session 3)`

> **How to collect (next session):** rebuild `ytchannel.sh` + `vtt2txt.pl` (see §Method / `_CORPUS_BUILD.md` §4), then for each playlist below: `yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/playlist?list=<PLID>" > list.txt` → feed `list.txt` to `ytchannel.sh` with outdir `corpus/courses/<slug>/`. The driver is **resumable** (skips `.done_<id>` markers + existing files) — safe to re-run. Pace politely (YouTube 429s; one sub-lang per video, `--sleep-requests`, base sleep ≥2.5s). **Run channels/playlists in a managed queue, not all at once.**

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

## To ADD next session (not yet scanned — known high-value channels)
- **Berkeley:** CS285 Deep Reinforcement Learning (Levine); CS182 Deep Learning; Full Stack Deep Learning.
- **CMU:** 11-785 Introduction to Deep Learning (Bhiksha Raj); 11-711 Advanced NLP (Neubig); 10-708 Probabilistic Graphical Models.
- **Harvard:** CS50's Intro to AI with Python.
- **3Blue1Brown:** Neural Networks / Linear Algebra / Calculus series (intuition only — ground facts elsewhere).
- **fast.ai:** Practical Deep Learning for Coders.
- **MIT (add):** 6.034 AI (Winston), 6.S191 Intro to Deep Learning, 18.06 full Linear Algebra (Strang), 8.05/8.06 Quantum, 6.041 Probability (Tsitsiklis).
- **Stanford (add):** CS25 Transformers United; CS324 LLMs; MLSys seminar.

---

## Method (rebuild in the collecting session)
1. `ytchannel.sh <videolist> <outdir_abs> <label> [base_sleep]` — pulls `--write-auto-subs --sub-langs en --sub-format vtt`, cleans via `vtt2txt.pl` (strips cue numbers/timestamps/tags, de-dupes rolling captions), writes one `<id>_<slug>.txt` per video, `.done_<id>` marker for empties. Resumable.
2. `vtt2txt.pl` — VTT → de-duplicated plain text (see `_CORPUS_BUILD.md` §4).
3. Per playlist: dump `yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/playlist?list=<PLID>"` → feed to `ytchannel.sh`.
4. Tick this file + `_COVERAGE_MAP.md`; commit tracking md (transcripts stay git-ignored).

> **Durability filter:** lecture courses are deep + grounded — high value. But a single course is ~20–30 lectures × ~75 min; collect the **spine first** (CS229/CS230/CS231N/CS224N/CS234/CS336/CME295 + DeepMind RL/DL + MIT 6.7960 + neuro 9.13/9.40), then widen. Collect in a managed queue; expect hours.
