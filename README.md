# 11AM — Takhassus Hikam Dossier

**[Open the published book](https://mohdujjain.github.io/11-hikam/)** · Bilingual Arabic/English philosophy and religious studies notes · 39 published dossiers.

This repository follows the same **published root → modular `src/` → organized documentation/tests** model as [World History Dossier](https://github.com/MohdUjjain/world-history-dossier). The book text, interactive sidebar, print layout and offline app have not been redesigned during this directory migration.

## Quick start

Published GitHub Pages URL: **https://mohdujjain.github.io/11-hikam/**. GitHub Pages serves the root `index.html` from `main`, folder `/(root)`.

The reader shows a narrow **whole-book progress rail** and a separate **per-chapter circular gauge**, follows the active § section in the sidebar, and optionally offers **Resume Reading** from a position saved on this device (no account or sync).

Use **Install app** on Chrome/Edge/Android, or **Add to Home Screen** on iPhone/iPad. Visit online first, confirm **Entire book saved offline** in the contents panel, then reopen without a network connection. CacheStorage can be cleared by browsers or operating systems.

## Directory guide

| Path | Purpose |
| --- | --- |
| `index.html` | **Published** self-contained 39-chapter reader; generated, not hand edited |
| `service-worker.js` | **Published** content-hashed offline service worker; generated |
| `manifest.webmanifest`, `icons/`, `og-image.jpg` | PWA installation icons and social-sharing preview |
| `404.html`, `sitemap.xml`, `robots.txt`, `.nojekyll` | GitHub Pages and discovery assets |
| `src/main.html` | Authored book spine, cover, TOC, chapter include markers and metadata |
| `src/chapters/subtopic-*.html` | **Canonical chapter content** (six subtopic modules, 39 dossiers) |
| `src/philosophy_notes.css` and `src/philosophy_notes.js` | Shared design, navigation and print/pagination engine |
| `src/offline-reader.js`, `src/service-worker.template.js` | PWA status and offline worker source |
| `src/build.py` | Rebuilds published HTML, local reference HTML and service worker |
| `src/philosophy_study_notes.html` | Generated traditional, non-inlined HTML for local authoring/print preview |
| `src/docs/` | Living design, printing, editorial, hosting and history documentation |
| `src/tests/` | Structure, publication and offline service-worker checks |
| `src/source_materials/` | Previously supplied extracts for 3.4.3 and 3.4.4 (public!) |
| `src/tools/migrate_flat_repo.py` | One-time safe cleanup when moving from the previous flat repository |

More details: [src/README.md](src/README.md), [documentation index](src/docs/README.md).

**GitHub Actions quota workaround:** [Secondary-account CI fork and verified upstream release protocol](src/docs/hosting/SECONDARY_FORK_CI_AND_RELEASE.md) — staged in the current editorial review branch; the original repository remains the publication authority.

**Current bilingual editorial delivery rules:** [Accessible context-first Companions and paragraph-adjacent Source Depth](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md), applied to Moran 1.1.1 and Stout 1.1.2. Existing study aids, revision blocks and source fidelity are preserved; optional Source Depth does not print.

**Approved comprehension method:** [Context-First Companions, paragraph-adjacent Source Depth, accessible chapter-hue dotted/solid cues and real timelines](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md#8-binding-future-reading-protocol--accessibility-contextual-richness-and-source-depth) — published for both Moran 1.1.1 and Stout 1.1.2; all original study aids and source fidelity remain binding.

**Next editorial preparation:** [Dossier 1.1.3 — David Papineau, *Philosophy of Science*: primary-source coverage register](src/docs/editorial/READING_1_1_3_SOURCE_COVERAGE_PREPARATION.md). The supplied original reading and three separate teaching syntheses are not published in this repository; chapter 1.1.3 is not yet source-coverage approved.

**Standing editorial refinement instructions:** [Language, Source Fidelity & Study-Aid Protocol](src/docs/editorial/LANGUAGE_AND_SOURCE_FIDELITY_REFINEMENT_PROTOCOL.md) and [Concise Dossiers & Reading Companions](src/docs/editorial/CONCISE_DOSSIER_AND_READING_COMPANIONS.md) — read both before any reading-by-reading editorial pass. The adopted density targets are approximately 650–850 words of main prose + 850–1,150 words of teaching aids per dossier, chosen according to the original source (1,500–2,000 total visible words), excluding frontmatter and revision; Companions are separately audited, and the Arabic/English language rules remain unchanged.

**Published Reading Companion implementation:** 34 source-grounded context-first cues (ten in 1.1.1 and twenty-four in 1.1.2), with separately closed paragraph-adjacent Source Depth and source references; the reader is offline-embedded. [Binding teaching/interaction method](src/docs/editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) · [historical pilot audit](src/docs/editorial/READING_COMPANIONS_PILOT_1_1_1_1_1_2.md). The current [design-system regression](src/tests/browser_design_tokens.py) is required alongside source and publication checks.

## Build and verify

Requires Python 3; Node.js is additionally needed for the offline-service-worker simulation.

```bash
python src/build.py
python src/build.py --check
python src/tests/verify_publication.py
python src/tests/validate_structure.py
python src/tests/verify_sidebar.py
python src/tests/verify_reading_progress.py
node src/tests/test_offline_cache.mjs
```

Check generated outputs into `main` along with source changes. A GitHub Actions workflow verifies reproducibility and online metadata on push/PR; it does **not** automatically publish a PDF.

### Upgrading from the original flat layout

The [Windows migration instructions](src/docs/hosting/WINDOWS_CMD_DEPLOY.md) explain how to extract the complete organized ZIP into the existing checkout and remove duplicate old root files **only after SHA-256 checks**. Do not simply extract without running the migration cleanup, or old files will remain in the root.

**Public-content note:** Everything committed to this public repository—including `src/source_materials/`—is publicly accessible, even though it no longer appears at the website root. Move private/restricted source material outside the Git repository before distributing, if needed.
