# 11AM — Takhassus Hikam Dossier

**[Open the published book](https://mohdujjain.github.io/11-hikam/)** · Bilingual Arabic/English philosophy and religious studies notes · 62 published dossiers.

This repository follows the same **published root → modular `src/` → organized documentation/tests** model as [World History Dossier](https://github.com/MohdUjjain/world-history-dossier). The book text, interactive sidebar, print layout and offline app have not been redesigned during this directory migration.

## Current editorial instructions and scope

The **[Study-Aid Roles and Reading Design Protocol](src/docs/editorial/STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md)** records the latest user-approved editorial policy for **all 62 published dossiers**, in both languages. Read it first, then the [language and source-fidelity protocol](src/docs/editorial/LANGUAGE_AND_SOURCE_FIDELITY_REFINEMENT_PROTOCOL.md), [concise dossier and layer-allocation protocol](src/docs/editorial/CONCISE_DOSSIER_AND_READING_COMPANIONS.md), and [context-first Companion and Source Depth protocol](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md). The latest policy supersedes conflicting older component-preservation, aid-role, word-limit and routine full-suite directions. It retires main-text exam-tip and checkpoint components while retaining the six-part revision system and preserving source information in appropriate teaching layers.

**Source fidelity governs every permitted editorial change. This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The **[Refinement Audit and Migration Plan](src/docs/editorial/STUDY_AID_REFINEMENT_AUDIT_AND_MIGRATION_PLAN.md)** separates current instructions from frozen evidence: the detailed component audit covers **29 dossiers, from 1.1.1 through 3.2.5**, at commit `7798593e40ceafb9ff9590e1c1fea149347e5fdd`. The user's report that paragraph-style tables deteriorate from **3.2.6** is a migration concern beyond that completed audit, not an audited finding about every later dossier. Historical counts and scenarios remain dated evidence; they do not establish compliance with the newer limits.

**Implementation status:** this instruction update changes documentation. Applying the new policy to chapter content, reader behavior, CSS, JavaScript and generated publication assets remains deferred. Use the [editorial index](src/docs/editorial/README.md) for the full reading order and the [release guide](src/docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md) for checks appropriate to the actual change.

The following chapter records preserve earlier releases and their original evidence. Their references to former aid types, counts or test runs do not override the current policy above.

**Arabic 2.1.8:** The [source-led Plato revision and twelve-page coverage register](src/docs/editorial/READING_2_1_8_ARABIC_PLATO_SOURCE_COVERAGE.md) preserve the user's scholarly Arabic voice and the source's exact perspective. The [entire unrevised 2.1.8](src/archive/pre-redevelopment-2026-11-21/README.md) was archived on original `main` before any replacement. Private source materials and writing samples are not published.

**Arabic 2.2.1:** The new [source-faithful metaphysics reading and full 16-page coverage register](src/docs/editorial/READING_2_2_1_ARABIC_METAPHYSICS_SOURCE_COVERAGE.md) retain the original author's treatment of principles, cognition, existence and death. The [entire previous 2.2.1](src/archive/pre-redevelopment-2026-11-21/README.md) was archived before replacement. Arabic language samples and source files remain unpublished.

**Arabic 2.2.2:** The [source-faithful eight-page Arabic traditional-division coverage register](src/docs/editorial/READING_2_2_2_ARABIC_METAPHYSICS_DIVISION_SOURCE_COVERAGE.md) governs the expanded source-verified four-branch dossier and preserves the source's Kant/Hegel conclusion. The [full old edition](src/archive/pre-redevelopment-2026-11-21/README.md) was archived before replacement. Private Arabic sources and authorial profile samples are not published.

**Arabic 2.2.3:** The [eight-page Islamic and Christian metaphysics source register](src/docs/editorial/READING_2_2_3_ARABIC_ISLAM_CHRISTIAN_METAPHYSICS_SOURCE_COVERAGE.md) governs the original author's treatment of al-Kindi, al-Farabi, Ibn Sina, Ibn Rushd, and Augustine, including the incomplete final sentence and unresolved manuscript wording. The [complete previous Arabic dossier](src/archive/pre-redevelopment-2026-11-21/README.md) was archived before the update. Primary DOCX, supplements and language-profile samples are private.

**Historical preservation:** The complete 2.1.6 pre-redevelopment section was separately preserved [on 21 November 2026](src/archive/pre-redevelopment-2026-11-21/README.md), before its replacement, with a pinned Git blob and verification. The existing ten-file original archive remains unchanged.

**Earlier historical preservation:** [Ten complete original dossier sections](src/archive/pre-revamp-2026-11-05/README.md) (1.1.1–1.1.5 and 2.1.1–2.1.5) have been preserved from the 5 November 2026 pre-revamp commit, with a pinned manifest and CI integrity check. These are read-only historical snapshots outside the published book; the revised `main` dossiers remain canonical.

**Arabic dossier 2.1.7:** The source-faithful Arabic edition of *تطور علم السياسة* follows the user-supplied language-profile and three editorial protocols, with [the 16-page original-to-dossier coverage record](src/docs/editorial/READING_2_1_7_ARABIC_SOURCE_COVERAGE.md) and a [complete pre-redevelopment historical snapshot](src/archive/pre-redevelopment-2026-11-21/README.md). The source DOCX, profile and private Arabic writing samples are not published in this repository.

## Quick start

Published GitHub Pages URL: **https://mohdujjain.github.io/11-hikam/**. GitHub Pages serves the root `index.html` from `main`, folder `/(root)`.

The reader shows a narrow **whole-book progress rail** and a separate **per-chapter circular gauge**, follows the active § section in the sidebar, and optionally offers **Resume Reading** from a position saved on this device (no account or sync).

Use **Install app** on Chrome/Edge/Android, or **Add to Home Screen** on iPhone/iPad. Visit online first, confirm **Entire book saved offline** in the contents panel, then reopen without a network connection. CacheStorage can be cleared by browsers or operating systems.

## Directory guide

| Path | Purpose |
| --- | --- |
| `index.html` | **Published** self-contained 62-chapter reader; generated, not hand edited |
| `service-worker.js` | **Published** content-hashed offline service worker; generated |
| `manifest.webmanifest`, `icons/`, `og-image.jpg` | PWA installation icons and social-sharing preview |
| `404.html`, `sitemap.xml`, `robots.txt`, `.nojekyll` | GitHub Pages and discovery assets |
| `src/main.html` | Authored book spine, cover, TOC, chapter include markers and metadata |
| `src/chapters/subtopic-*.html` | **Canonical chapter content** (eleven subtopic modules, 62 dossiers) |
| `src/philosophy_notes.css` and `src/philosophy_notes.js` | Shared design, navigation and print/pagination engine |
| `src/offline-reader.js`, `src/service-worker.template.js` | PWA status and offline worker source |
| `src/build.py` | Rebuilds published HTML, local reference HTML and service worker |
| `src/philosophy_study_notes.html` | Generated traditional, non-inlined HTML for local authoring/print preview |
| `src/docs/` | Living design, printing, editorial, hosting and history documentation |
| `src/tests/` | Structure, publication and offline service-worker checks |
| `src/source_materials/` | Previously supplied extracts for 3.4.3 and 3.4.4 (public!) |
| `src/tools/migrate_flat_repo.py` | One-time safe cleanup when moving from the previous flat repository |

More details: [src/README.md](src/README.md), [documentation index](src/docs/README.md).

**Verification and publication:** [Secondary-account CI fork and verified upstream release protocol](src/docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md) — use checks scoped to the change; the original repository remains the publication authority. The documentation policy does not itself change existing automatic workflows.

**Bilingual delivery rules:** [Accessible context-first Companions and paragraph-adjacent Source Depth](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) support the current roles protocol. Essential teaching stays immediately visible; optional Source Depth does not print. Retain the complete six-part revision system.

**Approved comprehension method:** [Context-first explanation, accessible chapter-hue cues and source-grounded chronology](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md#8-binding-future-reading-protocol--accessibility-contextual-richness-and-source-depth) — the original Moran/Stout pilot remains implementation evidence, read under the current component roles and limits.

**Science & Religion (3.8):** [Assigned source boundaries, attributions and visible word counts](src/docs/editorial/READINGS_3_8_SOURCE_COVERAGE.md).

**Religion & Ethics (3.7.1–3.7.3):** [Assigned source boundaries, attributions and visible word counts](src/docs/editorial/READINGS_3_7_1_THROUGH_3_7_3_SOURCE_COVERAGE.md).

**Prophecy & Polemics (3.6.1–3.6.6):** [Assigned source boundaries, attributions and visible word counts](src/docs/editorial/READINGS_3_6_1_THROUGH_3_6_6_SOURCE_COVERAGE.md).

**The Problem of Evil (3.5.1–3.5.4):** [Assigned source boundaries, attributions and visible word counts](src/docs/editorial/READINGS_3_5_1_THROUGH_3_5_4_SOURCE_COVERAGE.md).

**Design & Evolution (3.4.2–3.4.9):** [Assigned source boundaries, attributions, and visible word counts](src/docs/editorial/READINGS_3_4_2_THROUGH_3_4_9_SOURCE_COVERAGE.md).

**Historical concise release — dossiers 2.1.3–2.1.5 (21 November 2026):** [Detailed source-to-layer comparison and final measurements](src/docs/editorial/READINGS_2_1_3_TO_2_1_5_CONCISE_REPASS.md) records the then-used **650–850 main prose / 850–1,150 meaningful study-aid / 1,500–2,000 immediately visible words** criteria without suppressing essential primary-source arguments. Final CI counts were **2.1.3 — War: 780 prose + 1,117 aids = 1,897 visible; 2.1.4 — Introduction & Who Should Rule?: 729 + 1,131 = 1,860; 2.1.5 — The Place of Liberty: 715 + 1,113 = 1,828**. The three combined visible readings fell from **7,628 to 5,585 words (2,043 fewer; 26.8%)**; all **64** existing context-first Companion explanations, **47** cited records in **27** adjacent Source Depth disclosures, all six revision sections for each chapter and all **39** book chapters present at that release remained. Source limits and original authorial qualifications were retained. The user's [archived pre-revamp dossiers](src/archive/pre-revamp-2026-11-05/README.md) remain unchanged. [Passing secondary-fork CI](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44804689030), [PR #31](https://github.com/MohdUjjain/11-hikam/pull/31) with [independent review verification](https://github.com/MohdUjjain/11-hikam/actions/runs/44805445176), [successful post-merge main checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44806050346) and [Pages publication](https://github.com/MohdUjjain/11-hikam/actions/runs/44806049856) validate that released academic commit [`f275047f`](https://github.com/MohdUjjain/11-hikam/commit/f275047f4d1365b720af05c3bb315db98018264f). Previously reported larger figures in the three earlier source audits refer to the **historical pre-compression editions**; these historical measurements are not a new-policy compliance result.

**Historical 2.1.5 source-verified release (superseded word counts):** [2.1.5 — Jonathan Wolff, *The Place of Liberty*: Oxford revised 2006 source-to-dossier register](src/docs/editorial/READING_2_1_5_WOLFF_LIBERTY_SOURCE_COVERAGE.md). The supplied original contains **14 PDF pages, printed pp. 104–117**, ending immediately after Wolff raises—but does not resolve—the utilitarian legislator's proposed single law to maximise happiness. This source-faithful edition preserves Mill's Liberty Principle and maturity exclusions, free discussion, Rousseau's challenge **and Wolff's remaining reservation**, the qualified Alexandrian-library and evolution accounts, offence versus harm, competition and rights-based interests, and utility without importing the missing argument beyond p. 117. The measured distribution is **1,331 visible prose + 1,202 visible study-aid words**, **22 context-first Reading Companions**, **eight adjacent Source Depth disclosures with 16 individually cited records** (1,653 optional words), and all six independently complete revision sections. [Successful secondary-fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44793566594), [original PR #30](https://github.com/MohdUjjain/11-hikam/pull/30), [upstream PR tests](https://github.com/MohdUjjain/11-hikam/actions/runs/44794462647), [successful post-merge main regression](https://github.com/MohdUjjain/11-hikam/actions/runs/44795127805) and [successful GitHub Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44795126411) establish release evidence for academic merge `a55c7d70`. All **12 transferred Git blobs** matched the fork-verified edition exactly; no original PDF or derivative study guide was committed.

**Previously published source-verified reading:** [2.1.4 — Jonathan Wolff, *Introduction & Who Should Rule?*: Oxford revised 2006 source-to-dossier register](src/docs/editorial/READING_2_1_4_WOLFF_SOURCE_COVERAGE.md). The original assigned extract joins the Introduction (printed pp. 1–5) and the beginning of Chapter 3 (pp. 62–77), stopping within the introductory Rousseau epigraph. The revised dossier preserves Wolff's successive arguments about authority, democracy, Plato's guardianship, conflicting interests, mixed-motivation voting, Condorcet's **conditional** theorem and democracy's intrinsic value, without importing later pages of Rousseau. The verified distribution is **1,430 explanatory prose + 1,247 study-aid words**, **23 context-first Reading Companions**, **nine adjacent Source Depth disclosures containing 17 source records** (1,682 optional words) and all six independent revision sections. [Passing fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44737649820), [original PR checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44738545054), [post-merge verification](https://github.com/MohdUjjain/11-hikam/actions/runs/44739056579) and [GitHub Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44739056012) all succeeded. All 12 transferred files matched their verified fork Git blobs; no source PDF or supporting synthesis was committed.

**Previously published source-verified reading:** [2.1.3 — Colin Bird, *War*, second edition (2019): complete 30-page source-to-dossier register](src/docs/editorial/READING_2_1_3_BIRD_WAR_SOURCE_COVERAGE.md). This particularly dense reading preserves the full debate on just war, pacifism and realism—including the final self-defence, innocent-combatant, excuse/justification and civilian-command arguments—with **1,234 explanatory prose + 1,184 study-aid words**, 19 context-first Companions, 10 paragraph-adjacent Source Depth disclosures holding 14 additional source records (1,457 optional words), and all six independent revision sections. [Secondary-fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44732155879), [upstream PR checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44733202430), [post-merge verification](https://github.com/MohdUjjain/11-hikam/actions/runs/44733691326) and [GitHub Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44733690577) all passed. All transferred source and generated blobs matched the tested fork; no supplied primary-source PDF or teaching synthesis was committed.

**Previously published source-verified reading:** [2.1.2 — Colin Bird, *The Common Good*: original ten-page chapter source-to-dossier register](src/docs/editorial/READING_2_1_2_BIRD_SOURCE_COVERAGE.md). The dossier contains **836 explanatory prose + 985 study-aid words**, 12 context-first Reading Companions, six optional paragraph-adjacent Source Depth records (573 words) and all six independent revision sections. [Secondary-fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44726626192), [upstream PR checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44727494105), [post-merge checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44727941869) and [Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44727941424) all passed. No source PDF or supporting synthesis was committed.

**Earlier published source-verified reading:** [2.1.1 — Colin Bird, “Introduction,” *An Introduction to Political Philosophy*: source-coverage register](src/docs/editorial/READING_2_1_1_BIRD_SOURCE_COVERAGE.md). The source-faithful dossier has 793 explanatory prose + 854 study-aid words, 11 context-first Reading Companions, six adjacent optional Source Depth records (512 words), and all six revision sections. [Secondary-fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44597229284), [upstream PR checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44598174309), [post-merge checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44598684378) and [Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44598683310) succeeded. No source PDF or teaching synthesis was committed.

**Previously published source-verified reading:** [1.1.5 — Simon Critchley, *The Gap between Knowledge and Wisdom*: page-by-page source-coverage register](src/docs/editorial/READING_1_1_5_CRITCHLEY_SOURCE_COVERAGE.md). The dossier contains 822 visible prose + 900 study-aid words, nine contextual Reading Companions, five adjacent optional Source Depth records, and the complete six-part revision system. [Fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44580992713), [original review checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44582569244), [post-merge checks](https://github.com/MohdUjjain/11-hikam/actions/runs/44583169276) and [GitHub Pages deployment](https://github.com/MohdUjjain/11-hikam/actions/runs/44583168139) succeeded. The source PDF and teaching syntheses were not committed.

**Previously verified editorial reading:** [1.1.4 — Gary Gutting, *Sartre, Foucault and Derrida*: completed source-coverage register](src/docs/editorial/READING_1_1_4_GUTTING_SOURCE_COVERAGE.md). This edition has 824 visible prose + 1,017 study-aid words, 12 contextual Companions, nine optional Source Depth records and a self-contained six-part revision system. [Complete fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44562601029) passed before transfer; the original PDF and three teaching syntheses were never committed.

**Previously completed editorial reading:** [1.1.3 — David Papineau, *Philosophy of Science*: source-to-dossier resolution and verified audit](src/docs/editorial/READING_1_1_3_SOURCE_COVERAGE_PREPARATION.md#v-completed-source-coverage-resolution--final-113-edition-19-november). The revised chapter contains 821 prose + 1,137 study-aid words, 12 context-first Companions and nine optional paragraph-adjacent Source Depth records; it passed full fork verification before upstream release. The supplied original and three teaching syntheses were not committed.

**Standing editorial refinement instructions:** use the [current reading order and precedence](src/docs/editorial/README.md). The roles protocol defines current component limits and programme-level averages; historical chapter audits do not establish a compulsory minimum for every individual dossier.

**Historical Reading Companion pilot:** 34 source-grounded context-first cues (ten in 1.1.1 and twenty-four in 1.1.2), with separately closed paragraph-adjacent Source Depth and source references; the reader is offline-embedded. [Teaching/interaction method](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) · [pilot audit](src/docs/editorial/READING_COMPANIONS_PILOT_1_1_1_1_1_2.md). Use the [design-system regression](src/tests/browser_design_tokens.py) when the changed behavior requires it, under the scoped release guide.

## Build and verify

Choose checks that establish the changed behavior and preserve the affected contracts. Do not run the whole-book suite routinely for every chapter or documentation edit. Follow the [scoped verification and release guide](src/docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md).

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Documentation-only changes:** check the exact diff, Markdown links, policy consistency, historical/current status and authorized file scope. They do not require rebuilding the reader or running browser, print, offline or whole-book tests. Leave generated publication files unchanged.

**Reader-source changes:** build with Python 3 from the repository root, verify reproducibility, then run the source and behavior checks relevant to that change. Node.js is needed when the offline-service-worker simulation is relevant.

```bash
python src/build.py
python src/build.py --check
```

Available targeted checks include `verify_publication.py`, `validate_structure.py`, chapter-specific source/archive/Companion checks, `verify_sidebar.py`, `verify_reading_progress.py` and `node src/tests/test_offline_cache.mjs`. Their presence is not an instruction to run every command for every change. When rendered chapter content changes, inspect bounded desktop/mobile and actual selected-chapter A4 evidence as required by that change; preserve the established print geometry.

For reader-source releases, transfer the canonical source and all three matching generated outputs (`index.html`, `src/philosophy_study_notes.html`, `service-worker.js`) as one verified edition. The existing `.github/workflows/verify-pages.yml` still responds to upstream pull requests and `main` pushes; changing this documentation does not change those triggers or prove any run passed. The [release guide](src/docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md) distinguishes documentation-only publication from reader verification and records skipped or unavailable checks accurately. The public release does not automatically publish a PDF.

### Upgrading from the original flat layout

The [Windows migration instructions](src/docs/hosting/WINDOWS_CMD_DEPLOY.md) explain how to extract the complete organized ZIP into the existing checkout and remove duplicate old root files **only after SHA-256 checks**. Do not simply extract without running the migration cleanup, or old files will remain in the root.

**Public-content note:** Everything committed to this public repository—including `src/source_materials/`—is publicly accessible, even though it no longer appears at the website root. Move private/restricted source material outside the Git repository before distributing, if needed.
