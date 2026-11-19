# Context-First Reading Companions and Optional Source Depth

**Project:** Takhassus Hikam · **Decision:** 18 November 2026  
**Pilot:** Dossiers 1.1.1 (Dermot Moran) and 1.1.2 (Rowland Stout); no unrelated chapter.  
**Status:** Both 1.1.1 and 1.1.2 are implemented and published on authoritative `main`; final [fork verification 44375169683](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44375169683), [upstream verification 44376223971](https://github.com/MohdUjjain/11-hikam/actions/runs/44376223971), and [Pages deployment 44376223150](https://github.com/MohdUjjain/11-hikam/actions/runs/44376223150) succeeded. Subsequent shared contrast corrections were verified and published at `dafd2f38`.  
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

## 4. Source Depth: adjacent, collapsed and printable only by explicit future design

**Updated 19 November 2026 — governing location rule:** Source Depth is not a distant second article at the end of the chapter. Place the **native collapsed callout immediately after the relevant ordinary prose paragraph** so the reader may consult the original reading's additional example, named debate, historical qualification or source evidence *at the point where it becomes relevant*. It is never part of the inline Companion popup.

- Use `<details class="hikam-source-depth-inline">` with a native `<summary>` identifying **SOURCE DEPTH**, a brief grounded title and a signal that the material is optional.
- Show no expanded information until the student chooses to open that summary. All callouts start closed. They work with keyboard, touch, screen readers and **without JavaScript**. Multiple details attached to the same paragraph belong inside one callout with separately titled internal source records, rather than repeated consecutive disclosure controls.
- Each record has the exact originating author and **printed source-page number(s)**; distinguish paraphrase from quotation, preserve the source's level of certainty, and never manufacture references.
- The ten original additional Moran explanations and the twenty-four original additional Stout explanations are **preserved as source records**. Their **34 inline Companions** instead answer *What does this mean?* and *Why is it here?*, with a short recall line. The two modes must never duplicate each other's instructional job.
- The supplemental detail is inside the **HTML `.chapter-body`** solely to keep it beside its source paragraph. It remains **outside the 1,500–2,000 immediately visible word count**. Do not confuse its closed textual DOM presence with visible study-aid prose.
- Source Depth is **screen-only**: CSS hides it in regular printing, and the canonical JS page compositor explicitly removes `.hikam-source-depth-inline` from its private clones **before measuring**. Otherwise hidden callout text can accidentally affect pagination, source indexing or A4 output. Keep the on-screen original intact.
- No essential premise, decisive objection, argument or conclusion may exist solely inside optional Source Depth. The visible prose and existing study aids must still explain the author fully, and the independent six-part revision system must remain sound.
- Not every paragraph needs a callout, and not every future Companion needs a Source Depth counterpart. Select additions by genuine source value rather than quotas or visual decoration.

**Accessibility and underline convention (studied against 11-literature):** the inline Companion cue inherits its chapter pigment, has a **dotted underline while closed**, and becomes a **solid underline on hover or while expanded**. Keyboard `focus-visible` must have an additional visible outline. The popup's controlled expanded state and labelled content must work with keyboard, Escape, touch scrolling, RTL and a close action that restores focus. A closed native Source Depth uses the browser's semantic `summary/details` controls and must not be a screen-reader-invisible hover-only element.

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

## 7. Implementation and release gates — both dossiers, 19 November

**Scope:** `src/chapters/subtopic-1-1.html` (1.1.1 and 1.1.2 only); `src/reading_companions.json` (34 context-first records); existing controller, style and print compositor; affected source/browser/print tests; editorial and design documentation. No unrelated academic chapter or component role may be rewritten. Generate the publication only through `src/build.py`.

Acceptance checks:

1. All 34 contextual cues still attach uniquely to normal, visible prose. The source-depth text itself cannot become a Companion anchor.
2. Exactly ten Moran source records and twenty-four Stout source records retain their original explanations and printed references, immediately below the corresponding paragraph and inside closed native disclosures (grouped when several refer to one paragraph).
3. Each Companion shows **In simple words**, **Why this appears here**, and **Remember**, without adding a new intellectual branch. Different chapter pigments, dotted/rest versus solid/open behavior, focus outline, semantic expanded state, close/restore-focus behavior and touch-safe popup scrolling are tested.
4. `Source Depth` works with JavaScript disabled, remains optional, and never appears in generated print pages or print measurements. Main prose, memory aids, existing study-aid types and six revision sections remain intelligible without it.
5. All 39 chapters, navigational links, search, reading progress, RTL, mobile screen widths, browser accessibility and offline PWA continue to function. Check real Chromium print/PDF pagination and no accidental cutoffs.
6. Rebuild and run the repository's complete canonical tests on the **second-account CI fork**, compare generated blob hashes with the authoritative review branch, and only then merge the verified edition into original `main`.

**Follow-on scope:** both 1.1.1 and 1.1.2 are now the controlled local-disclosure pilot. Do not mechanically extend it to the remaining 37 dossiers before reviewing accessibility and student comprehension. No artificial Companion quotas.

## 8. Binding future-reading protocol — accessibility, contextual richness, and Source Depth

**Adopted 19 November 2026 for subsequent dossiers, beginning with the 1.1.3 preparation.** This consolidates the reader's approval of the two-chapter pilot. It does not authorize copying its exact number of cues or length to new chapters, nor does it replace the source-coverage audit.

### The Companion teaches the current passage

- Begin with the **reader's local confusion**: define this claim/term in easy language, explain **why it appears here**, and optionally offer one precise **Remember** line. These three roles are available within the existing popup; do not require three repetitive blocks where one explanation suffices.
- **Helpful explanatory restatement is allowed.** The old rule that every Companion must introduce a previously absent fact no longer applies. Reject redundant *teaching work*, not simpler wording that genuinely resolves a difficulty.
- Avoid launching a named theory, source-specific exception, historical detour or unrelated philosophical dispute in the popup. Source-based further detail belongs in Source Depth. Neither container may alter the author's claim, add ChatGPT's independent qualifications or conceal a necessary argumentative premise.

### Source Depth is local, optional and accessible

- Attach one normally closed native `<details class="hikam-source-depth-inline">` **immediately after the relevant visible prose paragraph**; group several source records concerning the same paragraph within that single disclosure, with each record clearly titled and accurately cited to the original edition/page.
- This is **not** a chapter-end appendix, automatically opened modal, new essential explanatory layer or a substitute for main notes. It is for substantial additional source context which would otherwise interrupt the reader's concentration. Preserve full citations and distinguish the primary author's claim from any sourced quotation or secondary interpretation.
- A native disclosure must remain usable by keyboard, touch and screen reader with **JavaScript disabled**. Its summary must announce a meaningful title and the optional nature of the additional information, rather than a label with no context.
- Source Depth is present in the interactive HTML but hidden in print and removed from print-compositor clones **before pagination measurement**. It must not create search hits that navigate into collapsed or invisible text. Verify that the main printed notes and full six-part revision system still teach the indispensable argument without it.

### Use Literature's cue behavior within Hikam's existing design tokens

- The exact inline phrase remains normal text with a subtle **chapter-hue dotted underline at rest**. On hover or while open, the underline becomes **solid**, using the same rotating `--hue`, not a new accent or a hardcoded identical color for every chapter.
- A clear `:focus-visible` outline supplements the underline for keyboard users. Check click, Enter/Space activation, Escape, outside dismissal, accessible name and expanded-state semantics, focus return to the originating phrase **without reopening**, touch positioning, scrollable expanded content, and mobile/RTL Arabic typography.
- The cue must wrap across lines without changing the text, quotation, reading position, anchor or print copy. Every trigger must match a uniquely identified existing prose occurrence; never let a generated hint attach to a quotation, a revision element or a hidden disclosure by accident.
- Treat **color contrast and the 360° system as release gates**: use the established navy/parchment/gold foreground-surface pairings, Fraunces/Source Serif 4/IBM Plex Sans/Amiri type tokens and six immutable semantic box colors. The automated `src/tests/browser_design_tokens.py` checks all 39 chapters and should remain mandatory alongside source, accessibility, print/PDF and offline/PWA tests.

### Rich presentations, without a new information burden

- Literature's richer original-language evidence, faithfully reconstructed figures and source tables are **conditional precedents**, not a request to turn every Companion into a large card. Hikam may use a purposeful existing structure (short comparison, formula breakdown, evidence excerpt, tiny annotated diagram) **only if it directly resolves the local difficulty**, is source-faithful, accessible by text/keyboard, and respects the existing design system.
- Put extended original-source evidence and illustrations in optional **Source Depth** when they do not belong in the immediate clarification. Label reconstructions and new teaching analogies explicitly; never pass them off as quotations, diagrams or empirical evidence from the source. Record original edition/page and any limits.
- Do not create a new box taxonomy or prioritize EL10 over other aids; real chronological succession uses the established `.historical-timeline`, while simultaneous distinctions remain tables or other existing comparative formats.

### Required editorial and deployment handoff

For each next reading: (1) reopen the primary source and author/title; (2) compare the complete source section by section against the canonical chapter and all six revision areas; (3) preserve the core author's argument visibly within the 650–850 prose / 850–1,150 study-aid planning bands when the source allows; (4) assign only justified local conceptual clarification to Companions and optional further source material to Source Depth; (5) register exact anchors/pages and verify no essential claims are hidden; (6) run source-integrity, design-token, keyboard/mobile/RTL, search, no-JavaScript, actual A4 print, and offline-PWA checks; (7) use the **manually dispatched `.github/workflows/hikam-fork-verify.yml` on the second-account fork** to validate an explicit branch and, where appropriate, commit its generated outputs **only to the fork**; (8) transfer verified identical Git blobs through an upstream review branch, then confirm publication on the primary repository. The fork workflow must never be represented as authorizing an automatic change to the original.

**1.1.3 transition:** Papineau's *Philosophy of Science* has its own source-to-dossier register. Reuse these standards, not the Moran/Stout text, source records, cue count or paragraph positions. The existing 1.1.3 chapter is not yet approved as source-complete merely because the two prior chapters are.
