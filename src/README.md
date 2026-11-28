# Hikam — source code and editorial workspace

`src/main.html` and `src/chapters/subtopic-*.html` are the canonical book source. For reader-source changes, build the website with `python src/build.py` **from the repository root**. No build framework or package installation is required.

## Editorial authority and current scope

Read the **[Study-Aid Roles and Reading Design Protocol](docs/editorial/STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md)** first, then the supporting source-fidelity, concise-dossier and context-first protocols in the **[editorial reading order](docs/editorial/README.md)**. The latest component roles and limits govern all **62 published dossiers**. Earlier blanket instructions to retain every aid type do not reinstate retired main-text exam tips or checkpoints. The six revision sections remain required; source information must be preserved in an appropriate teaching layer.

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The **[audit and migration plan](docs/editorial/STUDY_AID_REFINEMENT_AUDIT_AND_MIGRATION_PLAN.md)** records the narrower frozen audit of **29 dossiers through 3.2.5** at `7798593e40ceafb9ff9590e1c1fea149347e5fdd`. The user's reported table problem beginning at **3.2.6** belongs to the remaining review scope. The whole-corpus policy is not evidence that the other 33 dossiers were included in that audit or that all 62 have already been migrated. This pass updates instructions; chapter, reader, CSS, JavaScript and generated-output implementation remains deferred.

## Existing chapter records and targeted checks

These records describe earlier editions and their source boundaries. Their historical aid inventory does not override the current roles protocol. Use the named source test when changing the corresponding dossier, with other checks selected for the affected behavior under the [release guide](docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md).

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Arabic 2.1.7:** The source-aligned edition uses the [16-page Arabic source and language-fidelity register](docs/editorial/READING_2_1_7_ARABIC_SOURCE_COVERAGE.md); its original full HTML section was [archived before replacement](archive/pre-redevelopment-2026-11-21/README.md). The three teaching syntheses, original DOCX and personal Arabic voice samples remain outside GitHub. Targeted source check: `python src/tests/verify_arabic_politics_source_fidelity.py`.

**Arabic 2.1.8:** The Plato chapter uses the [12-page Arabic source-to-dossier register](docs/editorial/READING_2_1_8_ARABIC_PLATO_SOURCE_COVERAGE.md) and the [pinned full historical section](archive/pre-redevelopment-2026-11-21/README.md). The original DOCX, three Arabic syntheses and personal language samples stay outside the repository. Targeted source check: `python src/tests/verify_arabic_plato_source_fidelity.py`.

**Arabic 2.2.1:** The complete original [16-page Arabic source](docs/editorial/READING_2_2_1_ARABIC_METAPHYSICS_SOURCE_COVERAGE.md) governs the reworked metaphysics chapter; [its prior full 2.2.1 edition is immutable](archive/pre-redevelopment-2026-11-21/README.md). Source DOCX, three syntheses, language profile and personal writing samples remain private editorial references. Targeted source check: `python src/tests/verify_arabic_metaphysics_source_fidelity.py`.

**Arabic 2.2.2:** The original eight-page Arabic reading controls the revised traditional-division dossier. The [full original source-to-section coverage record](docs/editorial/READING_2_2_2_ARABIC_METAPHYSICS_DIVISION_SOURCE_COVERAGE.md) preserves the source's distinct introductory and exposition orderings and all author-attributed positions. The [complete former dossier](archive/pre-redevelopment-2026-11-21/README.md) is stored with a protected Git hash. Source DOCX, Arabic syntheses, writing samples and profile remain private. Targeted source check: `python src/tests/verify_arabic_metaphysics_division_source_fidelity.py`.

**Arabic 2.2.3:** The [full source-to-dossier coverage and two textual-boundary notes](docs/editorial/READING_2_2_3_ARABIC_ISLAM_CHRISTIAN_METAPHYSICS_SOURCE_COVERAGE.md) record the original eight-page Arabic DOCX's blank author metadata, incomplete final Augustine sentence and unverified «حرثات الأجرام السماوية» reading. Neither missing text nor an unverified correction is invented. The [complete predecessor](archive/pre-redevelopment-2026-11-21/README.md) was archived and pinned on `main` first. Targeted source check: `python src/tests/verify_arabic_metaphysics_islam_christian_source_fidelity.py`.

## Subsequent dossier snapshots

Dossier 2.1.6 was archived in full before its first replacement on 21 November 2026: [pre-redevelopment snapshot](archive/pre-redevelopment-2026-11-21/README.md). It is separately pinned and never a build input. The fixed original ten-dossier baseline below remains unchanged.

## Preserved pre-revamp originals

The [dated original-dossier archive](archive/pre-revamp-2026-11-05/README.md) holds the **full unmodified HTML chapter sections** for 1.1.1–1.1.5 and 2.1.1–2.1.5 from the 5 November 2026 baseline, including every original study aid and revision block. These are **not build inputs**. Do not edit or incorporate them into the live reader. Verify the pinned content with `python src/tests/verify_dossier_archive.py`; follow the standing editorial protocol to preserve future pre-edit snapshots.

## Authoring sequence

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

1. Establish the authorized scope and read the current editorial instructions. For a documentation-only task, edit only the relevant instructions and references; check their links, policy consistency and exact diff. Do not rebuild the reader or run browser, print, offline or whole-book tests for that task.
2. When a dossier implementation pass is authorized, read its original source and current complete chapter, preserve the required predecessor snapshot, and edit only the relevant `src/chapters/subtopic-*.html` fragment and its associated records. Apply current aid roles and limits while preserving the source's arguments, distinctions, qualifications, evidence and conclusions.
3. Update `src/main.html` only if the actual chapter count, title, TOC or divider metadata changes. Preserve chapter IDs and the user-established 3.2.5 versus 3.3 distinction. Do not modify unrelated chapters or global CSS/JavaScript as an incidental editorial cleanup.
4. Keep the existing shared design tokens, RTL behavior, print isolation and established A4 page geometry and pagination boundaries. A demonstrated design or pagination change requires its own appropriate scope and documentation; this sequence does not authorize speculative fixes or a replacement design system.
5. For reader-source changes, run `python src/build.py` and `python src/build.py --check`, plus the targeted source/archive/Companion and rendered-behavior checks required by the change. Follow the [scoped release guide](docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md); a complete suite is not a routine chapter gate. Transfer `index.html`, `src/philosophy_study_notes.html` and `service-worker.js` with their exact matching canonical source as one verified edition.

`src/philosophy_study_notes.html` is a generated non-inlined HTML export kept next to its CSS and JavaScript; `index.html` is the public, offline self-contained reader. Do not hand-edit either generated file.

The `src/source_materials/` extracts remain publicly visible to anyone browsing this public repository; the directory move is organizational only, not access control.

## Contents and printing

The accessible Topic → Sub-topic → Chapter → Section sidebar supports live search, explicit branch control, a chapter-only ordered print selector, and optional revision pages. See [SIDEBAR_GUIDE.md](docs/hosting/SIDEBAR_GUIDE.md). When changing that behavior, validate with `python src/tests/verify_sidebar.py` and the relevant bounded browser checks.

## Screen-only reading location

The sticky progress rail, circular chapter gauge, sidebar's active § link,
and optional locally saved Resume Reading prompt are implemented in
`src/main.html`, `src/philosophy_notes.css`, and the **same existing**
`wireScrollSpy()` in `src/philosophy_notes.js`. See
[`docs/hosting/READING_POSITION.md`](docs/hosting/READING_POSITION.md).
Do not add a second scroll tracker or save print-transformed positions.

## On-screen revision visibility

The Tools tab has **Show chapter Revision Blocks** (default: on). Turning it off
hides every chapter's complete `.end-block` from the screen, with preference
stored under `11am-hikam-show-revisions-v1` in device `localStorage`.
The main book and every revision block remain in the HTML. The print dialog
has an **independent** Include chapter revision pages option; hiding a block
on screen never excludes it from a PDF unless that print option is unchecked.
Search still indexes the entire book and reveals Revision Blocks when a
reader deliberately selects a result inside a hidden block.
