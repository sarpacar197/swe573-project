# Software Requirements Specification — Craft Heritage Archive

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-27 | Initial version: purpose, scope, requirements, user stories, MVP scope. |

> A changelog against Milestone 1 is required at the MVP milestone. Each later change to this document gets a row in the table above with the reason for the change.

---

## 1. Purpose

Craft Heritage Archive is a community web archive of local and traditional handicrafts such as hand-woven carpets, kilims and pottery. Registered users add crafts they know, other users add the **making story** ("how it is made"), and everyone can browse, search and follow contributors.

The goal is to **preserve knowledge**, not to trade. The system has **no selling, no auctions and no payments**.

## 2. Scope

### 2.1 In scope
- User accounts (register, log in, log out) and public profiles.
- Adding a craft: title, description, craft type, region/origin, photo.
- Viewing crafts and adding making stories to them.
- Following other users and a feed of crafts added by followed users.
- Searching and filtering crafts by craft type and region.
- Moderation through the Django admin.
- A REST API for the same functionality, documented with Swagger UI (OpenAPI).
- A web interface built with Django templates.
- Docker image and a public deployment on Render with PostgreSQL.

### 2.2 Out of scope
- Any commerce: prices, carts, orders, auctions, payments, donations.
- Private messaging and chat.
- Native mobile apps.
- Machine translation and AI-based content generation.

### 2.3 Release plan
| Release | Tag | Due | Content |
|---|---|---|---|
| MVP (Milestone 2) | `milestone-2`, release name `0.2.0-beta` (pre-release) | Mon 30.11.2026 18:00 (demo Tue 01.12.2026) | Stories marked **MVP = Yes** |
| Final | `v0.9` (pre-release) | Sun 06.12.2026 23:59 (demo Tue 08.12.2026) | All **Must** and **Should** stories |

## 3. Stakeholders

| Stakeholder | Interest |
|---|---|
| Contributor (registered user) | Records crafts they know, e.g. from family or their region. |
| Story teller (registered user) | Adds the making process of a craft they know. |
| Learner / enthusiast | Browses, searches and follows contributors to learn crafts. |
| Visitor (not logged in) | Reads the archive without an account. |
| Moderator (Django admin / staff) | Keeps content appropriate and on-topic. |
| Researcher / cultural heritage organisation | Uses the archive as a source about regional crafts. |
| Course instructor | Evaluates the product, the repository and the process. |
| Developer (project owner) | Builds, tests, deploys and defends the system. |

## 4. Glossary

| Term | Meaning |
|---|---|
| Craft | A traditional handmade item or technique recorded in the archive (e.g. "Uşak carpet"). |
| Craft type | A category from a fixed list: carpet, kilim, pottery, weaving, embroidery, woodwork, metalwork, glass, basketry, other. |
| Region / origin | Where the craft comes from, written as free text (e.g. "Uşak, Aegean"). |
| Making story | A text written by a user that explains how a craft is made. A craft can have several making stories. |
| Contributor | The user who added a craft. |
| Follow | A one-way relation: user A follows user B. |
| Feed | The list of crafts added by the users that the current user follows, newest first. |
| Visitor | A person using the site without logging in. |
| Moderator | A staff user who uses the Django admin to manage content. |
| MVP | Minimum viable product, delivered at Milestone 2. |
| MoSCoW | Priority scale: **Must**, **Should**, **Could**, **Won't** (not in this course project). |

## 5. Functional requirements

| ID | Requirement | Priority | MVP |
|---|---|---|---|
| FR-01 | The system shall let a visitor register with a unique username, an email address and a password. | Must | Yes |
| FR-02 | The system shall let a registered user log in and log out. | Must | Yes |
| FR-03 | The system shall let a logged-in user change their password. | Should | No |
| FR-04 | The system shall issue an API token to a registered user who sends valid credentials. | Must | Yes |
| FR-05 | The system shall show a public profile for each user: username, bio, crafts added, stories written, follower and following counts. | Must | Yes |
| FR-06 | The system shall let a user edit their own bio and region. | Should | No |
| FR-07 | The system shall let a logged-in user add a craft with title, description, craft type, region and one photo. | Must | Yes |
| FR-08 | The system shall list crafts newest first, paginated. | Must | Yes |
| FR-09 | The system shall show a craft detail page with all its fields, its contributor and its making stories. | Must | Yes |
| FR-10 | The system shall let only the contributor edit or delete their own craft. | Should | No |
| FR-11 | The system shall restrict craft type to a predefined list. | Must | Yes |
| FR-12 | The system shall accept only image files up to 5 MB as craft photos. | Should | Yes |
| FR-13 | The system shall let a logged-in user add a making story to a craft. | Must | Yes |
| FR-14 | The system shall allow at most one making story per user per craft, and only the author may edit or delete it. | Should | No |
| FR-15 | The system shall list a craft's making stories oldest first, each with author and date. | Must | Yes |
| FR-16 | The system shall let a logged-in user follow and unfollow another user. A user cannot follow themselves or follow the same user twice. | Must | Yes |
| FR-17 | The system shall show the followers and the followed users of a user. | Should | No |
| FR-18 | The system shall show a logged-in user a feed of crafts added by the users they follow, newest first, paginated. | Must | Yes |
| FR-19 | The system shall show guidance when the feed is empty. | Should | Yes |
| FR-20 | The system shall filter crafts by craft type. | Must | Yes |
| FR-21 | The system shall filter crafts by region (case-insensitive, partial match). | Must | Yes |
| FR-22 | The system shall search crafts by keyword in title and description. | Should | No |
| FR-23 | The system shall allow combining the type filter, the region filter and the keyword search. | Should | Yes |
| FR-24 | The system shall let a moderator edit or delete any craft or story and deactivate users through the Django admin. | Must | Yes |
| FR-25 | The system shall let a logged-in user report a craft or story as inappropriate. | Could | No |
| FR-26 | The system shall expose the functionality above through a REST API documented with OpenAPI and Swagger UI. | Must | Yes |
| FR-27 | The system shall not contain any price, payment, auction or sale feature. | Must | Yes |

## 6. Non-functional requirements

| ID | Category | Requirement | MVP |
|---|---|---|---|
| NFR-01 | Usability | A first-time user given the URL and test credentials can add a craft and a story without help. | Yes |
| NFR-02 | Accessibility | Pages follow basic WCAG 2.1 AA practice: every image has alt text, every form field has a label, pages are usable with the keyboard, text contrast is at least 4.5:1. | Yes |
| NFR-03 | Security | Passwords are hashed by Django; forms use CSRF protection; only owners modify their content; secrets come from environment variables; `DEBUG` is off in production. | Yes |
| NFR-04 | Performance | Craft list, detail and feed pages respond within 2 seconds with 1,000 crafts in the database; lists are paginated (12 items per page). | Yes |
| NFR-05 | Portability | The application runs with Docker from the instructions in the README alone. | Yes |
| NFR-06 | Deployability | The application is reachable at a public Render URL and uses PostgreSQL in production, SQLite locally. | Yes |
| NFR-07 | Maintainability | Minimum custom code: Django and DRF built-in features are preferred; no extra library without a written reason. | Yes |
| NFR-08 | Testability | Models, views and API endpoints have automated tests run with `python manage.py test`. | Yes |
| NFR-09 | Privacy | Email addresses are never shown publicly; only data needed for the features is stored. | Yes |
| NFR-10 | Documentation | Swagger UI lists every API endpoint; the README has installation, Docker and environment-variable instructions. | Yes |
| NFR-11 | Content rights | When adding a photo the user confirms they have the right to share it. | No |
| NFR-12 | Internationalisation | Turkish characters (ç, ğ, ı, İ, ö, ş, ü) are stored, displayed and searched correctly (UTF-8). | Yes |
| NFR-13 | Availability | The deployment is up during the demos on 01.12.2026 and 08.12.2026. | Yes |

## 7. User stories

Format: **ID** — *Priority* — *MVP* — linked requirement(s), then the story and its Given/When/Then acceptance criteria.

### 7.1 Epic: Accounts

**US-ACC-01** — Must — MVP: Yes — FR-01
As a visitor, I want to register with a username, email and password so that I can contribute to the archive.
- Given I am on the sign-up page, when I submit a unique username, a valid email and two matching passwords, then my account is created and I am logged in.

**US-ACC-02** — Must — MVP: Yes — FR-01
As a visitor, I want to be told when my username is already taken so that I can choose another one.
- Given the username "ayse" exists, when I register with "ayse", then the form shows "A user with that username already exists." and no account is created.

**US-ACC-03** — Must — MVP: Yes — FR-01, NFR-03
As a visitor, I want weak passwords to be rejected so that my account is safe.
- Given I am on the sign-up page, when I enter a password that is too short or entirely numeric, then the form shows Django's password-validation message.

**US-ACC-04** — Must — MVP: Yes — FR-02
As a registered user, I want to log in with my username and password so that I can add content.
- Given I have an account, when I submit correct credentials on the login page, then I am redirected to the home page and see my username in the navigation bar.

**US-ACC-05** — Must — MVP: Yes — FR-02
As a registered user, I want a clear error when my credentials are wrong so that I know to try again.
- Given I am on the login page, when I submit a wrong password, then I see an error and stay logged out.

**US-ACC-06** — Must — MVP: Yes — FR-02
As a logged-in user, I want to log out so that nobody else can use my account on a shared computer.
- Given I am logged in, when I click "Log out", then my session ends and the navigation bar shows "Log in".

**US-ACC-07** — Must — MVP: Yes — FR-07, NFR-03
As a visitor, I want to be sent to the login page when I try to add content so that I understand I need an account.
- Given I am not logged in, when I open the "Add craft" page, then I am redirected to the login page and returned to "Add craft" after logging in.

**US-ACC-08** — Must — MVP: Yes — FR-04
As an API client developer, I want to obtain a token with my username and password so that I can call protected endpoints.
- Given I have an account, when I POST my credentials to `/api/auth/token/`, then I receive `{"token": "..."}`.
- Given wrong credentials, when I POST them, then I receive HTTP 400.

**US-ACC-09** — Must — MVP: Yes — FR-01, FR-26
As an API client developer, I want to register through the API so that a client app can create accounts.
- Given a unique username, when I POST username, email and password to `/api/auth/register/`, then I receive HTTP 201 with the username and no password in the response.

**US-ACC-10** — Should — MVP: No — FR-03
As a logged-in user, I want to change my password so that I can keep my account secure.
- Given I am logged in, when I submit my old password and a valid new password twice, then the password is changed and I stay logged in.

**US-ACC-11** — Could — MVP: No — FR-03
As a registered user who forgot my password, I want to reset it by email so that I can regain access.
- Given my account has an email, when I request a reset, then I receive a link that lets me set a new password once.

**US-ACC-12** — Could — MVP: No — FR-02
As a registered user, I want to delete my account so that my personal data is removed.
- Given I am logged in, when I confirm account deletion, then my account is deactivated and I am logged out.

### 7.2 Epic: Profiles

**US-PRO-01** — Must — MVP: Yes — FR-05
As a visitor, I want to see a user's profile page so that I can learn who added a craft.
- Given user "mehmet" exists, when I open `/users/mehmet/`, then I see the username, bio and the crafts he added.

**US-PRO-02** — Must — MVP: Yes — FR-05
As a visitor, I want to open a contributor's profile from a craft page so that I can see their other crafts.
- Given I am on a craft detail page, when I click the contributor's username, then I am taken to their profile.

**US-PRO-03** — Must — MVP: Yes — FR-05, FR-17
As a visitor, I want to see follower and following counts on a profile so that I can see how active a user is.
- Given a user has 3 followers and follows 2 users, when I open their profile, then I see "3 followers · 2 following".

**US-PRO-04** — Should — MVP: Yes — FR-05
As a visitor, I want to see the making stories a user has written on their profile so that I can find their knowledge.
- Given a user wrote 2 stories, when I open their profile, then I see links to the 2 crafts with those stories.

**US-PRO-05** — Should — MVP: No — FR-06
As a logged-in user, I want to edit my bio so that others know my background in crafts.
- Given I am on my profile, when I edit my bio and save, then the new bio is shown on my profile.

**US-PRO-06** — Should — MVP: No — FR-06
As a logged-in user, I want to set my home region so that others know where my knowledge comes from.
- Given I am editing my profile, when I enter "Kütahya" as region and save, then my profile shows "Kütahya".

**US-PRO-07** — Must — MVP: Yes — NFR-09
As a registered user, I want my email address to be hidden from others so that my privacy is protected.
- Given any profile page or API profile response, when it is viewed by another user, then no email address appears.

**US-PRO-08** — Must — MVP: Yes — FR-26
As an API client developer, I want to fetch a user's public profile so that I can show it in my client.
- Given user "mehmet" exists, when I GET `/api/users/mehmet/`, then I receive username, bio, region, followers_count and following_count.

**US-PRO-09** — Should — MVP: No — FR-06, FR-26
As an API client developer, I want to read and update the current user's profile so that users can edit it from my client.
- Given I send a valid token, when I PATCH `/api/users/me/` with a new bio, then I receive HTTP 200 and the updated profile.

**US-PRO-10** — Could — MVP: No — FR-06
As a logged-in user, I want to upload a profile picture so that my profile is recognisable.
- Given I upload a valid image under 2 MB, when I save, then the image is shown on my profile with my username as alt text.

### 7.3 Epic: Crafts

**US-CRA-01** — Must — MVP: Yes — FR-07
As a logged-in user, I want to add a craft with title, description, craft type, region and photo so that it is preserved in the archive.
- Given I am logged in and on "Add craft", when I fill all fields and upload a JPEG, then the craft is saved and I am taken to its detail page.

**US-CRA-02** — Must — MVP: Yes — FR-07
As a logged-in user, I want required fields to be validated so that crafts are complete.
- Given I leave the title empty, when I submit, then the form shows "This field is required." and nothing is saved.

**US-CRA-03** — Must — MVP: Yes — FR-11
As a logged-in user, I want to choose the craft type from a list so that crafts are categorised consistently.
- Given I am on "Add craft", when I open the craft type field, then I see only the predefined types (carpet, kilim, pottery, weaving, embroidery, woodwork, metalwork, glass, basketry, other).

**US-CRA-04** — Should — MVP: Yes — FR-12
As a logged-in user, I want non-image files to be rejected so that the archive only shows photos.
- Given I upload a PDF as the photo, when I submit, then the form shows an error that the file is not a valid image.

**US-CRA-05** — Should — MVP: Yes — FR-12
As the site owner, I want photos larger than 5 MB to be rejected so that storage stays small.
- Given I upload an 8 MB image, when I submit, then the form shows "Photo must be 5 MB or smaller."

**US-CRA-06** — Must — MVP: Yes — FR-07
As a contributor, I want the craft to record me as its contributor automatically so that I get credit.
- Given I am logged in as "ayse", when I add a craft, then its contributor is "ayse" and I cannot choose another user.

**US-CRA-07** — Must — MVP: Yes — FR-08
As a visitor, I want to see a list of crafts with photo, title, type and region so that I can browse the archive.
- Given crafts exist, when I open the home page, then I see cards with photo, title, craft type and region, newest first.

**US-CRA-08** — Must — MVP: Yes — FR-08, NFR-04
As a visitor, I want the craft list to be paginated so that pages load quickly.
- Given 30 crafts exist, when I open the home page, then I see 12 crafts and links to the next page.

**US-CRA-09** — Must — MVP: Yes — FR-09
As a visitor, I want to open a craft's detail page so that I can read its full description.
- Given a craft exists, when I click its card, then I see its photo, title, description, type, region, contributor and date added.

**US-CRA-10** — Must — MVP: Yes — FR-09
As a visitor, I want a clear "not found" page for a deleted or wrong craft so that I am not confused.
- Given no craft with id 999 exists, when I open `/crafts/999/`, then I get a 404 page.

**US-CRA-11** — Should — MVP: No — FR-10
As a contributor, I want to edit my craft so that I can correct mistakes.
- Given I added a craft, when I edit the description and save, then the new description is shown.

**US-CRA-12** — Should — MVP: No — FR-10, NFR-03
As a contributor, I want other users to be unable to edit my craft so that my content is protected.
- Given "ayse" added a craft, when "mehmet" opens its edit URL or sends PATCH to the API, then he receives HTTP 403.

**US-CRA-13** — Should — MVP: No — FR-10
As a contributor, I want to delete my craft after a confirmation so that I can remove wrong entries.
- Given I added a craft, when I click "Delete" and confirm, then the craft and its stories are deleted and I am taken to the craft list.

**US-CRA-14** — Must — MVP: Yes — FR-26
As an API client developer, I want to list and create crafts through the API so that clients can use the archive.
- Given a valid token, when I POST a multipart request with title, description, craft_type, region and photo to `/api/crafts/`, then I receive HTTP 201 with the craft JSON including `photo` URL and `contributor`.
- Given no token, when I POST to `/api/crafts/`, then I receive HTTP 401.

**US-CRA-15** — Must — MVP: Yes — FR-27
As a community member, I want crafts to have no price or sale option so that the archive stays non-commercial.
- Given any craft form or API schema, when I inspect its fields, then there is no price, sale, auction or payment field.

**US-CRA-16** — Could — MVP: No — NFR-11
As a contributor, I want to confirm that I have the right to share the photo so that the archive respects copyright.
- Given I am adding a craft, when I submit without ticking "I have the right to share this photo", then the form shows an error.

**US-CRA-17** — Could — MVP: No — FR-07
As a contributor, I want to add more than one photo so that I can show details of the craft.
- Given I am adding a craft, when I upload up to 5 images, then all are shown on the detail page.

### 7.4 Epic: Stories

**US-STO-01** — Must — MVP: Yes — FR-13
As a logged-in user, I want to add a making story to a craft so that others learn how it is made.
- Given I am logged in and on a craft detail page, when I write a story and click "Add story", then the story appears under the craft with my username and the date.

**US-STO-02** — Must — MVP: Yes — FR-13
As a logged-in user, I want empty stories to be rejected so that the archive has useful content.
- Given I am on a craft page, when I submit an empty story, then the form shows "This field is required." and nothing is saved.

**US-STO-03** — Must — MVP: Yes — FR-13, NFR-03
As a visitor, I want to be asked to log in before adding a story so that stories have an author.
- Given I am not logged in, when I view a craft, then instead of the story form I see "Log in to add a making story."

**US-STO-04** — Must — MVP: Yes — FR-15
As a visitor, I want to read all making stories of a craft in order so that I can follow the knowledge as it was added.
- Given a craft has 3 stories, when I open it, then I see all 3, oldest first, each with author and date.

**US-STO-05** — Must — MVP: Yes — FR-13
As the contributor of a craft, I want to be able to add a story to my own craft too so that I can share what I know.
- Given I added a craft, when I open it, then the story form is available to me.

**US-STO-06** — Should — MVP: No — FR-14
As a reader, I want each user to have at most one story per craft so that a craft page is not flooded by one person.
- Given I already wrote a story for a craft, when I open the craft again, then I see "Edit your story" instead of a new story form.
- Given I POST a second story for the same craft via the API, then I receive HTTP 400.

**US-STO-07** — Should — MVP: No — FR-14
As a story author, I want to edit my story so that I can add details later.
- Given I wrote a story, when I edit and save it, then the updated text is shown with an "edited" date.

**US-STO-08** — Should — MVP: No — FR-14
As a story author, I want to delete my story so that I can remove wrong information.
- Given I wrote a story, when I click "Delete" and confirm, then the story is removed from the craft page.

**US-STO-09** — Should — MVP: No — FR-14, NFR-03
As a story author, I want other users to be unable to change my story so that my words are not altered.
- Given "ayse" wrote a story, when "mehmet" sends PATCH `/api/stories/{id}/`, then he receives HTTP 403.

**US-STO-10** — Must — MVP: Yes — FR-26
As an API client developer, I want to list and add stories of a craft through the API so that clients can show and collect them.
- Given craft 5 exists, when I GET `/api/crafts/5/stories/`, then I receive its stories oldest first.
- Given a valid token, when I POST `{"body": "..."}` to `/api/crafts/5/stories/`, then I receive HTTP 201 and the story with author set to me.

**US-STO-11** — Could — MVP: No — FR-13
As a story author, I want to list materials and tools separately so that readers can prepare before trying the craft.
- Given I am adding a story, when I fill an optional "Materials and tools" field, then it is shown as a separate section of the story.

**US-STO-12** — Could — MVP: No — FR-13
As a story author, I want to add a photo of a making step so that the process is easier to understand.
- Given I am adding a story, when I attach an image under 5 MB, then it is shown with the story and has alt text.

**US-STO-13** — Could — MVP: No — FR-15
As a reader, I want to see how many stories a craft has on its card so that I can find well-documented crafts.
- Given a craft has 2 stories, when I view the craft list, then its card shows "2 stories".

### 7.5 Epic: Follow

**US-FOL-01** — Must — MVP: Yes — FR-16
As a logged-in user, I want to follow another user from their profile so that I see their new crafts.
- Given I am on "mehmet"'s profile and do not follow him, when I click "Follow", then the button changes to "Unfollow" and his follower count increases by 1.

**US-FOL-02** — Must — MVP: Yes — FR-16
As a logged-in user, I want to unfollow a user so that their crafts leave my feed.
- Given I follow "mehmet", when I click "Unfollow" on his profile, then the button changes to "Follow" and his crafts no longer appear in my feed.

**US-FOL-03** — Must — MVP: Yes — FR-16
As a logged-in user, I want to be unable to follow myself so that my follower count is honest.
- Given I am on my own profile, then no "Follow" button is shown.
- Given I POST `/api/users/<my username>/follow/`, then I receive HTTP 400.

**US-FOL-04** — Must — MVP: Yes — FR-16
As a logged-in user, I want following the same user twice to have no effect so that counts stay correct.
- Given I already follow "mehmet", when I POST `/api/users/mehmet/follow/` again, then I receive HTTP 200 and the follower count does not change.

**US-FOL-05** — Must — MVP: Yes — FR-16, NFR-03
As a visitor, I want to be asked to log in when I click "Follow" so that I understand following needs an account.
- Given I am not logged in, when I view a profile, then the follow button links to the login page.

**US-FOL-06** — Should — MVP: No — FR-17
As a visitor, I want to see the list of a user's followers so that I can discover people with similar interests.
- Given "mehmet" has followers, when I open `/users/mehmet/followers/`, then I see their usernames linking to their profiles.

**US-FOL-07** — Should — MVP: No — FR-17
As a visitor, I want to see who a user follows so that I can discover other contributors.
- Given "mehmet" follows users, when I open `/users/mehmet/following/`, then I see their usernames linking to their profiles.

**US-FOL-08** — Must — MVP: Yes — FR-16, FR-26
As an API client developer, I want follow and unfollow endpoints so that clients support following.
- Given a valid token, when I POST `/api/users/mehmet/follow/`, then I receive HTTP 201 and a follow relation exists.
- Given a valid token, when I DELETE `/api/users/mehmet/follow/`, then I receive HTTP 204 and the relation is removed.

**US-FOL-09** — Should — MVP: No — FR-17, FR-26
As an API client developer, I want to list followers and following of a user so that clients can show them.
- Given "mehmet" exists, when I GET `/api/users/mehmet/followers/`, then I receive a paginated list of usernames.

**US-FOL-10** — Could — MVP: No — FR-16
As a logged-in user, I want to follow a user directly from a craft card so that following is quick.
- Given I am on the craft list, when I click "Follow" next to a contributor's name, then I follow them without leaving the page.

### 7.6 Epic: Feed

**US-FEE-01** — Must — MVP: Yes — FR-18
As a logged-in user, I want a feed of crafts added by the users I follow so that I see new content from people I care about.
- Given I follow "mehmet" and "ayse", when I open `/feed/`, then I see only crafts added by them, newest first.

**US-FEE-02** — Must — MVP: Yes — FR-18
As a logged-in user, I want my own crafts and crafts of users I do not follow to be excluded from the feed so that the feed is focused.
- Given "ali" is not followed by me, when "ali" adds a craft, then it does not appear in my feed.

**US-FEE-03** — Must — MVP: Yes — FR-18, NFR-04
As a logged-in user, I want the feed to be paginated so that it loads quickly.
- Given the feed has 30 crafts, when I open it, then I see 12 and a link to the next page.

**US-FEE-04** — Should — MVP: Yes — FR-19
As a new user, I want guidance when my feed is empty so that I know how to fill it.
- Given I follow nobody, when I open my feed, then I see "You are not following anyone yet" and a link to browse crafts.

**US-FEE-05** — Must — MVP: Yes — FR-18, NFR-03
As a visitor, I want to be asked to log in when I open the feed so that I understand it is personal.
- Given I am not logged in, when I open `/feed/`, then I am redirected to the login page.

**US-FEE-06** — Must — MVP: Yes — FR-18, FR-26
As an API client developer, I want a feed endpoint so that clients can show a personal feed.
- Given a valid token, when I GET `/api/feed/`, then I receive a paginated list of crafts by users I follow, newest first.
- Given no token, then I receive HTTP 401.

**US-FEE-07** — Must — MVP: Yes — FR-18
As a logged-in user, I want a "Feed" link in the navigation bar so that I can reach my feed from any page.
- Given I am logged in, when I look at the navigation bar, then I see a "Feed" link.

**US-FEE-08** — Could — MVP: No — FR-18
As a logged-in user, I want the feed to also show new making stories on crafts by people I follow so that I do not miss new knowledge.
- Given someone adds a story to a craft by a user I follow, when I open my feed, then I see an entry "New story on <craft>".

**US-FEE-09** — Could — MVP: No — FR-18, FR-20
As a logged-in user, I want to filter my feed by craft type so that I can focus on one craft.
- Given my feed has carpets and pottery, when I choose "pottery", then only pottery crafts are shown.

### 7.7 Epic: Search

**US-SEA-01** — Must — MVP: Yes — FR-20
As a visitor, I want to filter crafts by craft type so that I can see, for example, only kilims.
- Given kilims and pottery exist, when I choose "kilim" in the type filter, then only kilims are listed.

**US-SEA-02** — Must — MVP: Yes — FR-21
As a visitor, I want to filter crafts by region so that I can explore the crafts of one place.
- Given crafts from "Uşak" and "Kütahya" exist, when I enter "uşak" in the region filter, then only crafts whose region contains "Uşak" are listed.

**US-SEA-03** — Should — MVP: Yes — FR-23
As a visitor, I want to combine type and region filters so that I can find, for example, pottery from Kütahya.
- Given I choose type "pottery" and region "Kütahya", when I apply the filter, then only crafts matching both are listed.

**US-SEA-04** — Should — MVP: No — FR-22
As a visitor, I want to search crafts by keyword so that I can find a craft whose name I partly remember.
- Given a craft titled "Yağcıbedir carpet" exists, when I search "yağcı", then it appears in the results.

**US-SEA-05** — Must — MVP: Yes — FR-20, FR-21
As a visitor, I want a message when no crafts match my filters so that I know to change them.
- Given no craft matches, when I apply the filters, then I see "No crafts match your filters."

**US-SEA-06** — Should — MVP: Yes — FR-20, FR-21
As a visitor, I want my chosen filters to stay visible on the results page and in pagination links so that I know what I am looking at.
- Given I filtered by "kilim", when I go to page 2, then the filter is still "kilim" and still applied.

**US-SEA-07** — Must — MVP: Yes — FR-20, FR-21, FR-26
As an API client developer, I want query parameters for filtering so that clients can search the archive.
- Given crafts exist, when I GET `/api/crafts/?craft_type=pottery&region=kütahya`, then I receive only matching crafts.

**US-SEA-08** — Should — MVP: No — FR-22, FR-26
As an API client developer, I want a keyword search parameter so that clients can offer search.
- Given crafts exist, when I GET `/api/crafts/?search=yağcı`, then I receive crafts whose title or description contains "yağcı".

**US-SEA-09** — Should — MVP: No — NFR-12
As a Turkish-speaking user, I want search to work with Turkish characters so that "kütahya" finds "Kütahya".
- Given a craft with region "Kütahya", when I filter by "kütahya", then the craft is found (verified on PostgreSQL in production).

**US-SEA-10** — Could — MVP: No — FR-21
As a visitor, I want to click a region or type on a craft page so that I see all crafts of that region or type.
- Given I am on a craft from "Uşak", when I click "Uşak", then I see the craft list filtered by region "Uşak".

**US-SEA-11** — Could — MVP: No — FR-08
As a visitor, I want to sort crafts by newest or by number of stories so that I can find well-documented crafts.
- Given crafts exist, when I choose "Most stories", then crafts are ordered by story count, highest first.

### 7.8 Epic: Moderation

**US-MOD-01** — Must — MVP: Yes — FR-24
As a moderator, I want to log in to the Django admin so that I can manage content.
- Given I am a staff user, when I log in at `/admin/`, then I see Users, Crafts, Stories and Follows.

**US-MOD-02** — Must — MVP: Yes — FR-24
As a moderator, I want to delete an inappropriate craft so that the archive stays on-topic.
- Given an inappropriate craft exists, when I delete it in the admin, then it no longer appears on the site.

**US-MOD-03** — Must — MVP: Yes — FR-24
As a moderator, I want to delete an inappropriate story so that the archive stays respectful.
- Given an inappropriate story exists, when I delete it in the admin, then it no longer appears on the craft page.

**US-MOD-04** — Should — MVP: Yes — FR-24
As a moderator, I want to deactivate an abusive user so that they cannot log in.
- Given a user is active, when I untick "active" in the admin, then that user can no longer log in.

**US-MOD-05** — Should — MVP: Yes — FR-24
As a moderator, I want to search and filter crafts in the admin by type, region and contributor so that I can find content quickly.
- Given many crafts exist, when I use the admin search and list filters, then the list narrows to matching crafts.

**US-MOD-06** — Could — MVP: No — FR-25
As a logged-in user, I want to report a craft as inappropriate so that moderators can review it.
- Given I am on a craft page, when I click "Report" and enter a reason, then a report is saved and I see "Thank you, a moderator will review it."

**US-MOD-07** — Could — MVP: No — FR-25
As a logged-in user, I want to report a story as inappropriate so that moderators can review it.
- Given I am reading a story, when I click "Report" and enter a reason, then a report is saved.

**US-MOD-08** — Could — MVP: No — FR-25
As a moderator, I want to see open reports in the admin so that I can handle them.
- Given reports exist, when I open Reports in the admin, then I see each report with its target, reason and reporter, and I can mark it resolved.

**US-MOD-09** — Should — MVP: No — FR-27
As a moderator, I want to remove crafts that are sale advertisements so that the archive stays non-commercial.
- Given a craft description advertises a sale, when I review it in the admin, then I can delete it (the rule is stated in the site's About page).

**US-MOD-10** — Could — MVP: No — FR-24
As a moderator, I want inactive users' content to stay visible but marked so that knowledge is not lost.
- Given a user is deactivated, when I view their craft, then it is still shown and their name is marked "(inactive)".

### 7.9 Epic: Accessibility

**US-ACS-01** — Must — MVP: Yes — NFR-02
As a screen-reader user, I want every craft photo to have alt text so that I know what it shows.
- Given a craft with a photo, when the page is rendered, then the `<img>` has an `alt` attribute containing the craft title.

**US-ACS-02** — Must — MVP: Yes — NFR-02
As a screen-reader user, I want every form field to have a label so that I know what to type.
- Given any form (sign-up, login, add craft, add story, filters), when I inspect it, then every input has a connected `<label>`.

**US-ACS-03** — Must — MVP: Yes — NFR-02
As a keyboard user, I want to reach every link, button and form field with Tab so that I can use the site without a mouse.
- Given any page, when I press Tab repeatedly, then focus moves through all interactive elements in a logical order and the focus is visible.

**US-ACS-04** — Should — MVP: Yes — NFR-02
As a low-vision user, I want text to have enough contrast so that I can read it.
- Given any page, when it is checked with a contrast checker, then normal text has a contrast ratio of at least 4.5:1.

**US-ACS-05** — Should — MVP: Yes — NFR-02
As a screen-reader user, I want pages to use headings and landmarks so that I can jump to the main content.
- Given any page, when I inspect it, then it has one `<h1>`, a `<nav>` and a `<main>` element.

**US-ACS-06** — Must — MVP: Yes — NFR-02
As a screen-reader user, I want form errors to be shown as text next to the field so that I know what to fix.
- Given I submit a form with an error, when the page reloads, then the error message is text placed next to its field, not only a colour change.

**US-ACS-07** — Should — MVP: Yes — NFR-02
As a mobile user, I want pages to fit my screen so that I can browse without zooming.
- Given a 375 px wide screen, when I open any page, then there is no horizontal scrolling.

**US-ACS-08** — Should — MVP: Yes — NFR-02
As a screen-reader user, I want the page language to be declared so that the text is read with correct pronunciation.
- Given any page, when I inspect the `<html>` tag, then it has a `lang` attribute.

**US-ACS-09** — Could — MVP: No — NFR-02
As a contributor, I want to write my own alt text for a photo so that it describes the image better than the title.
- Given I am adding a craft, when I fill the optional "Photo description" field, then it is used as the alt text.

**US-ACS-10** — Could — MVP: No — NFR-02
As a keyboard user, I want a "Skip to content" link so that I do not tab through the navigation on every page.
- Given any page, when I press Tab once, then a "Skip to content" link appears and moves focus to `<main>`.

### 7.10 Epic: Non-functional

**US-NFS-01** — Must — MVP: Yes — NFR-05
As a developer, I want to run the app with Docker so that it runs the same on any machine.
- Given Docker is installed, when I follow the README (`docker build` then `docker run` with the listed environment variables), then the app is reachable at `http://localhost:8000`.

**US-NFS-02** — Must — MVP: Yes — NFR-06
As the instructor, I want the app deployed at a public URL so that I can test it without installing anything.
- Given the Render deployment, when I open the URL, then the home page loads over HTTPS.

**US-NFS-03** — Must — MVP: Yes — NFR-06
As the site owner, I want production to use PostgreSQL so that data survives restarts.
- Given the app runs on Render, when the service restarts, then crafts, users and stories are still there.

**US-NFS-04** — Must — MVP: Yes — NFR-03
As the site owner, I want secrets and settings to come from environment variables so that no secret is in the repository.
- Given the repository, when I search it, then `SECRET_KEY` and database passwords are not present; production reads them from the environment.

**US-NFS-05** — Must — MVP: Yes — NFR-03
As the site owner, I want `DEBUG` to be off in production so that error pages do not leak internals.
- Given the production deployment, when I open a missing URL, then I see a plain 404 page without a stack trace.

**US-NFS-06** — Must — MVP: Yes — NFR-08
As a developer, I want automated tests for models, views and the API so that I can change code safely.
- Given the code, when I run `python manage.py test -v 2`, then all tests pass and the output lists each test.

**US-NFS-07** — Must — MVP: Yes — NFR-10, FR-26
As an API client developer, I want Swagger UI listing all endpoints so that I can try the API in the browser.
- Given the deployment, when I open `/api/docs/`, then Swagger UI lists every endpoint with request and response schemas.

**US-NFS-08** — Must — MVP: Yes — NFR-10
As a developer new to the project, I want README instructions with system requirements so that I can install it from the README alone.
- Given a clean machine with Python and Docker, when I follow the README step by step, then the app runs locally.

**US-NFS-09** — Must — MVP: Yes — NFR-04
As a visitor, I want pages to load quickly so that browsing is pleasant.
- Given 1,000 crafts in the database, when I open the craft list, then the response arrives in under 2 seconds.

**US-NFS-10** — Must — MVP: Yes — NFR-12
As a Turkish-speaking user, I want Turkish characters to display correctly so that names like "Çanakkale" are not broken.
- Given a craft with region "Çanakkale", when it is saved and displayed, then it appears exactly as typed in the page and the API.

**US-NFS-11** — Should — MVP: Yes — NFR-03
As the site owner, I want uploaded photos to be stored where they survive redeploys so that crafts do not lose their images.
- Given a craft with a photo exists on the deployment, when the service is redeployed, then the photo is still shown.

**US-NFS-12** — Should — MVP: No — NFR-08
As a developer, I want tests to run automatically on every pull request so that broken code is not merged.
- Given a pull request, when it is opened or updated, then a GitHub Actions workflow runs the tests and reports the result on the PR.

**US-NFS-13** — Must — MVP: Yes — NFR-13
As the instructor, I want seed demo data and test credentials so that I can try the system immediately.
- Given the deployment, when I log in with the test credentials from the report, then I see existing crafts, stories and a non-empty feed.

---

## 8. MVP summary

The MVP (Milestone 2) covers every story marked **MVP: Yes**: register, log in/out, API token, public profile, add/list/view crafts with photo, add and list making stories, follow/unfollow, feed, type and region filters, Django-admin moderation, accessibility basics, REST API with Swagger UI, tests, Docker and Render deployment.

Editing and deleting own content, one-story-per-user, keyword search, followers lists, password change and CI are planned for the Final release.

## 9. Story count

| Epic | Stories | MVP: Yes |
|---|---|---|
| Accounts | 12 | 9 |
| Profiles | 10 | 6 |
| Crafts | 17 | 12 |
| Stories | 13 | 6 |
| Follow | 10 | 6 |
| Feed | 9 | 7 |
| Search | 11 | 6 |
| Moderation | 10 | 5 |
| Accessibility | 10 | 8 |
| Non-functional | 13 | 12 |
| **Total** | **115** | **77** |
