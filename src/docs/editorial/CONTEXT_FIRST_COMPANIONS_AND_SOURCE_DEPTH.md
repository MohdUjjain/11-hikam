# Context-First Reading Companions and Optional Source Depth

**Project:** Takhassus Hikam · **Decision:** 18 November 2026  
**Pilot:** Dossier 1.1.1 — Dermot Moran, *Towards an Assessment of Twentieth-Century Philosophy*  
**Status:** Implemented and fully verified on the secondary-account fork through [Actions run 44367909907](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44367909907); the exact built edition was returned to the upstream editorial branch via [PR #13](https://github.com/MohdUjjain/11-hikam/pull/13). Publication remains a separate release check.  
**Also read:** [Language and Source-Fidelity Refinement Protocol](LANGUAGE_AND_SOURCE_FIDELITY_REFINEMENT_PROTOCOL.md), [Concise Dossiers and Reading Companions](CONCISE_DOSSIER_AND_READING_COMPANIONS.md), and [Design System](../design/DESIGN_SYSTEM.md).

## 1. The problem this decision corrects

Short sentences do not automatically form a comprehensible intellectual picture. A reading that rapidly introduces different philosophers, methods and historical turns may still feel like disconnected facts. A student opens a Companion to understand **the sentence being read**, but a Companion that immediately introduces new historians, disputes or names increases the student's cognitive burden. This was observed in the first live Moran pilot. The former Companion criterion of **always providing new information** was too narrowly applied.

**Latest governing rule:** A Reading Companion clarifies **the immediate concept, sentence, connection or argumentative role already present in the visible reading**. It must not introduce an unrelated new intellectual branch merely to earn a nonduplication justification. A careful simpler rephrasing is legitimate added *understanding*, even when it repeats the existing proposition without adding a new fact. The full original article still determines what the note means.

## 2. Intellectual ownership across five layers

| Layer | Intellectual job | Safeguard |
| --- | --- | --- |
| Main prose | The source author's problem, complete essential reasoning and conclusion in connected, natural sentences | Must work independently of popups and optional disclosures |
| Existing study aids | Comparison, structure, dates, definitions, analogy, recall, quotation and assessment using their established meanings | No decorative replacement or privileging EL10 |
| **Context-First Reading Companion** | A direct, small clarification of **what this phrase means and why it appears at this point in the argument** | No unrelated names, source excursions or new thesis; the wording may simplify an already-taught idea |
| **Source Depth** | Optional further source examples, historical particulars, qualifications, named debates or detail that would interrupt normal reading | Accessible separately, never essential to comprehend the visible argument; specific source pages preserved |
| Six-part revision system | Independent end-of-reading recall and examination preparation | Remains intact, not a replacement for teaching |

The unchanged target for the immediately visible chapter body is about **650–850 words of prose plus 850–1,150 words of existing study aids (1,500–2,000 total)**, scaled to article length and complexity. Companions, Source Depth, frontmatter and revision blocks are counted separately. This is not permission to omit indispensable source claims.

## 3. Three-step Companion writing test

When a contextual cue is genuinely useful, write only the amount necessary:

1. **In simple words:** explain the term, claim or relationship right in front of the reader. Do not start with a new scholarly detour.
2. **Why this appears here:** connect the phrase to the same paragraph/section and the source author's larger question, using the concepts the reader has already met.
3. **Remember:** an optional one-line recall handle; it must say the same thing accurately, not add a second argument.

These three labels are not a mandatory textual quota. One direct explanation may suffice in other chapters. **Editorial sufficiency, not format uniformity, governs.** Avoid empty repetitions, childish tone, ungrounded analogies and introductory labels that are more complex than the concept. English and Arabic must continue to follow the full language-profiling and fidelity rules.

**Acceptance gates:**
- Can a student read the adjacent paragraph, open the Companion and *return immediately* with better understanding of the same argument?
- Does the Companion answer a real local question rather than simply reproduce a definition?
- Does it avoid new thinkers, examples and distinctions not needed for this local point?
- Is the authorial claim and degree of certainty still faithful to the primary reading?
- Is the unique original phrase anchored in the correct main prose paragraph?
- Does the paragraph still stand alone without opening it?

**Example — Russell:** the old trigger explained Russell's intellectual genealogy through Bradley, McTaggart and Hylton. The new trigger says what Russell's analysis means and why Moran introduces it as an early analytic method. The genealogy is retained in optional Source Depth, not deleted.

## 4. Source Depth: a separate intentionally chosen mode

For the Moran pilot, additional details formerly located in ten Companions are transferred **without loss** into the independent Source Depth disclosure **after** the chapter's main body and **before** its navigation/revision block.

- One visibly distinct **closed outer native `<details>`** control announces optional original-source detail. Nothing opens automatically while reading.
- Inside are ten individually closed `<details>` cards with informative source-specific titles, original short explanations and Moran's printed page references.
- They may be read selectively after the chapter, not as popups interrupting sentences. The depth section works with keyboard and without JavaScript.
- The source items are **outside `.chapter-body`**, preserving visible-word accounting, original source text search/paragraph anchors and the established print-compositor's main-body selection.
- The source-depth appendix is screen-only and is **not printed** by the existing chapter-body print compositor. This is acceptable only where the unique content is supplementary; no indispensable premise may exist solely here. A future printable research appendix requires a separately tested opt-in design.
- No new hidden online fetch, public PDF upload, new note-specific JS library, layout overhaul or forced reading path is introduced.

In later readings, **not every Companion requires a Source Depth counterpart**; selection follows the primary source and the student's actual confusion.

## 5. Moran pilot source-to-layer traceability

| Inline contextual cue | What the Companion now clarifies | Preserved optional source detail | Printed Moran pages |
| --- | --- | --- | --- |
| `h111-russell-idealism` | Analysis as an early method and its place in the story | Russell's idealist inheritance and competing historical classifications | 28–29 |
| `h111-naturalism-critique` | Naturalism versus the question of objectivity | Husserl's source-specific criticism of naturalism | 5 |
| `h111-freud-later` | Why diverse beginnings appear together around 1900 | Freud's delayed reception by academic philosophers | 9–10 |
| `h111-husserl-development` | Phenomenological description and its argumentative role | Husserl's early descriptive and later transcendental phases | 10–11 |
| `h111-quine-holism` | The analytic/synthetic distinction and Quine's challenge | Quine's more detailed critique of analyticity and isolated verification | 18–19 |
| `h111-europe-concept` | Europe as intellectual identity, not only geography | Contrasting accounts by Husserl, Patočka, Derrida and Habermas | 26–27 |
| `h111-frege-politics` | Why Frege's precise logic matters here | Scope of Frege's influence and Moran's political historical report | 12–13 |
| `h111-tradition-labels` | Shared questions behind analytic/Continental labels | Problems with labels and historians' alternative names | 13–14 |
| `h111-political-philosophy-return` | Why politics enters the philosophical history | Timing and different political thinkers discussed by Moran | 31 |
| `h111-history-philosophy` | Why the history of ideas is part of philosophy | Hegelian historical self-reflection without a predetermined master narrative | 24–25 |

The source-detail wording is transferred from the previous published manifest to the static optional appendix. The contextual rewrite does not replace Moran's substantive conclusions in the main notes.

## 6. A whole-chapter thread and correct chronological visualization

Before the names multiply, the reader should meet a **single orienting thread**: changing methods and institutions → surviving older questions → different traditions answering partly shared problems → wars and migration reshaping philosophy → Moran's qualified assessment without a single inevitable-progress narrative.

This is placed within the **existing concept-relationship** format and supplemented by a short bridge explaining why four foundational thinkers appear together. It is source-faithful organizational scaffolding, not an independent theory of the century.

An actual historical succession belongs in the new **`.historical-timeline`** structural component: dates run along a visible chronological line, with a small source-faithful event description. A timeline must not be used for conceptual ranking, and a table should remain a table where side-by-side comparison is the true pedagogical function. The four-period Moran table (1900s; 1914–1918; 1930s–1940s; after 1945) is the pilot. Timeline typography and chapter hue follow the existing design system.

## 7. Implementation and release checks

**Files:** `src/chapters/subtopic-1-1.html` (only 1.1.1), `src/reading_companions.json` (only Moran's ten entries), `src/reading_companions.js` (backward-compatible structured rendering), `src/philosophy_notes.css` (scoped additions), relevant editorial/design docs and regression tests. Build only through `src/build.py`.

Validate:
1. All ten Moran contextual cues still anchor uniquely in existing prose; all 24 Stout Companions retain their earlier behavior and text.
2. The same ten source-detail explanations and printed references are in Source Depth, and it is closed by default, keyboard accessible and works without JavaScript.
3. Popup shows short labelled contextual fields; Stout's plain popup fallback remains intact; Escape, touch, focus and RTL work.
4. Timeline order/text, 39 chapters, unchanged title/author/frontmatter, all six revision-block sections, search and reading-progress controls remain sound.
5. No source detail is silently deleted and none of the optional material is required to follow the essential argument.
6. Print clones contain neither popup controls nor optional Source Depth; timeline prints coherently; offline PWA embeds the same version atomically.
7. Rebuild, run source-anchor/manifest and all repository structural tests, plus real Chromium mobile/desktop, PDF pagination and offline-update checks.

**Follow-on scope:** assess the actual reading experience of 1.1.1 before extending this contextual rewrite or Source Depth treatment to 1.1.2 and the other 37 dossiers. No automatic rollout or artificial Companion count.
