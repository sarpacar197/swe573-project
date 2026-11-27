# Requirements Elicitation — Craft Heritage Archive

This document lists the questions asked to clarify the requirements, the answer or assumption used for each, and open risks. When an assumption changes, the SRS changelog records it.

Sources: the project description given by the instructor, the milestone specifications, and my own analysis as the developer and a potential user.

## 1. Elicitation questions and assumptions

### 1.1 Purpose and users
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q1 | Is the archive commercial in any way? | **No.** No selling, auctions, prices, payments or donations. | FR-27, US-CRA-15, US-MOD-09 |
| Q2 | Who are the main users? | People who know a traditional craft (often from family or region), learners, and visitors. | Stakeholders |
| Q3 | Can visitors read without an account? | **Yes.** Reading crafts, stories and profiles is public. Writing needs an account. | FR-08, FR-09, FR-05 |
| Q4 | Which language is the interface? | English interface; content may be in Turkish or any language. Turkish characters must work. | NFR-12 |

### 1.2 Accounts and profiles
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q5 | What is needed to register? | Username, email, password. No email verification in the MVP. | FR-01 |
| Q6 | Is the email public? | **No.** Email is private (used only for password reset later). | NFR-09 |
| Q7 | What is on a profile? | Username, bio, region, crafts added, stories written, follower/following counts. | FR-05, FR-06 |
| Q8 | How do API clients authenticate? | DRF's built-in token authentication (`rest_framework.authtoken`). The web interface uses Django sessions. | FR-04 |

### 1.3 Crafts
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q9 | Is craft type free text or a fixed list? | **Fixed list** (carpet, kilim, pottery, weaving, embroidery, woodwork, metalwork, glass, basketry, other) so filtering is consistent. "Other" covers the rest. | FR-11 |
| Q10 | Is region a fixed list? | **Free text** (e.g. "Uşak, Aegean"), because crafts are tied to towns and villages, not only to the 7 geographical regions. Filtering uses case-insensitive partial match. | FR-21 |
| Q11 | Is a photo required? | **Yes**, exactly one photo in the MVP. Multiple photos are a "Could" for later. | FR-07, US-CRA-17 |
| Q12 | Maximum photo size and format? | Images only (Django `ImageField` validates them), maximum 5 MB. | FR-12 |
| Q13 | Can two users add the same craft? | **Yes.** The same craft from two places or two families may differ. Duplicates are handled by moderators if needed. | — |
| Q14 | Who can edit or delete a craft? | Only its contributor, and moderators through the admin. | FR-10, FR-24 |

### 1.4 Making stories
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q15 | Can a craft have several making stories? | **Yes.** Different people know different techniques. | FR-13, FR-15 |
| Q16 | Can one user write several stories for the same craft? | **No**, at most one per user per craft (they can edit it). Enforced from the Final release; in the MVP it is not enforced. | FR-14 |
| Q17 | Can the contributor also write a story for their own craft? | **Yes.** | US-STO-05 |
| Q18 | What does a story contain? | Plain text in the MVP. Materials field and step photos are "Could". | US-STO-11, US-STO-12 |
| Q19 | In what order are stories shown? | Oldest first, so the page reads like a growing record. | FR-15 |

### 1.5 Follow and feed
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q20 | Is following one-way or mutual? | **One-way** (like a social feed), no approval needed. | FR-16 |
| Q21 | What appears in the feed? | Crafts added by followed users, newest first. New stories in the feed are a "Could". | FR-18, US-FEE-08 |
| Q22 | Do my own crafts appear in my feed? | **No.** | US-FEE-02 |
| Q23 | What if I follow nobody? | Show a message and a link to browse crafts. | FR-19 |

### 1.6 Search
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q24 | Which fields can be searched? | Filter by craft type (exact) and region (partial); keyword search in title and description. | FR-20–FR-23 |
| Q25 | Is full-text search needed? | **No.** Simple `icontains` queries are enough at this size. | NFR-07 |

### 1.7 Moderation
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q26 | Who moderates? | Staff users through the built-in Django admin. No custom moderation UI in the MVP. | FR-24 |
| Q27 | Can users report content? | "Could" for the Final release. | FR-25 |

### 1.8 Technical
| # | Question | Answer / assumption | Affects |
|---|---|---|---|
| Q28 | Which stack? | Django, Django REST Framework, drf-spectacular (Swagger UI), Django templates, SQLite locally, PostgreSQL in production, Docker, Render. | NFR-05–NFR-07 |
| Q29 | Is a JavaScript front-end framework needed? | **No.** Server-rendered Django templates keep the code minimal. | NFR-07 |
| Q30 | Where are uploaded photos stored in production? | **Open — see Risk R1.** | US-NFS-11 |

## 2. Assumptions summary
- A1. The archive is non-commercial; no money-related feature will ever be added.
- A2. Reading is public; writing requires login.
- A3. Craft type is a fixed list; region is free text.
- A4. One photo per craft in the MVP.
- A5. Many stories per craft; one per user per craft from the Final release.
- A6. Following is one-way and needs no approval.
- A7. Moderation is done in the Django admin.
- A8. The expected data size is small (hundreds to a few thousand crafts), so no caching or full-text search is needed.

## 3. Risks and open issues
| # | Risk | Impact | Mitigation |
|---|---|---|---|
| R1 | Render's free web service has an **ephemeral filesystem**: uploaded photos are lost on every redeploy. | Craft photos disappear (US-NFS-11). | Decide before deployment: (a) Render persistent disk (paid plan), or (b) external object storage via `django-storages` (one extra library). To be decided in its own issue. |
| R2 | Render's free PostgreSQL database expires after a limited period. | Data loss after the course period. | Acceptable for the course; note the expiry date in the README. |
| R3 | Very short time until the MVP deadline (30.11.2026). | Incomplete MVP, commits concentrated near the deadline. | Keep the MVP to the stories marked MVP: Yes; commit small changes daily. |
| R4 | `icontains` on SQLite is case-insensitive only for ASCII letters, so "kütahya" may not match "Kütahya" locally. | Search behaves differently locally and in production. | Production uses PostgreSQL, where it works; document it and test on PostgreSQL (US-SEA-09). |
| R5 | Users may upload photos they do not own. | Copyright problems. | About page rule, rights checkbox (US-CRA-16), moderator deletion. |
