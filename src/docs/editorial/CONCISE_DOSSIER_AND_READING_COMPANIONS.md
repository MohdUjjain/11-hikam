# Concise Dossiers and Source-Grounded Reading Companions

**Project:** 11AM — Takhassus Hikam Dossier  
**Adopted:** 18 November 2026  
**Status:** Binding editorial direction; context-first Companions and paragraph-adjacent Source Depth are published for **both** Moran 1.1.1 and Stout 1.1.2. The next source-comparison phase begins with Papineau 1.1.3.  
**Primary authority:** [Standing Language and Source-Fidelity Protocol](LANGUAGE_AND_SOURCE_FIDELITY_REFINEMENT_PROTOCOL.md)

> **Editorial decision:** The dossier should be an exceptionally clear, compact way to learn the author's essential argument, not a second article. Use a source-dependent **650–850 words of main explanation + 850–1,150 words of instructional study aids per reading**, averaged across the programme and excluding chapter frontmatter and the existing end-of-chapter revision block. Preserve all important source material by assigning it a clearly justified place across the main notes, the existing study aids, and carefully source-grounded **Reading Companions** available at the exact point of need. **Neither Arabic nor English language-fidelity rules change at all.**

## Later 18 November amendment — contextual clarity over new popup facts

**This amendment supersedes every earlier statement in this document that a Reading Companion must add a new source fact, named debate or historical qualification in order to avoid duplication.** The student's immediate need is to understand the current idea and why it matters *here*. A short, source-faithful explanation may legitimately restate or connect already visible concepts in simpler words. It must not launch a new historical or technical subplot while the student is trying to follow the main argument.

**Source Depth** is the separately chosen, optional home for further source-specific details that are useful but would increase cognitive burden inside a contextual popup. Such details remain traceable to the original article and are never the sole home of an indispensable premise. Native closed paragraph-adjacent disclosures in both revised chapters are the completed controlled pilot. Its material is excluded from the immediately visible 1,500–2,000-word target and is not exported by the standard chapter-body print compositor. The complete essential argument must stand without it.

**The original language, source-fidelity, study-aid and six-part revision requirements remain unchanged.** The additional goal is *conceptual continuity*: the reader needs a simple picture connecting the author's question, the many names, the different methods, historical changes and the conclusion. Use existing concept maps and actual timelines whenever they represent those relationships better than repeated descriptive prose.

See [Context-First Reading Companions and Optional Source Depth](CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) for the binding pilot rules, source-detail register, UI semantics and acceptance checks. Both Moran and Stout now use the approved method; do not mechanically transfer their exact annotations, text or count to unrelated chapters.

## 19 November 2026 — accessibility and local Source Depth placement

**Latest rule:** apply context-first Companions to both revised dossiers 1.1.1 and 1.1.2. Retain the 34 more detailed source explanations separately as intentionally closed, **paragraph-adjacent** `details.hikam-source-depth-inline` callouts, grouped where several relate to one paragraph. The reader reaches the optional details where they matter; there is no detached appendix and no additional topic forced into a popup. Their source citations remain intact; the indispensable argument stays visible.

Borrow Literature's chapter-pigment visual behavior: dotted underline in the ordinary state, a solid underline on hover/open, visible keyboard focus, expanded-state semantics, touch scrolling and Escape/close focus recovery. Native Source Depth must function with scripts disabled and must be excluded both by print CSS **and by removal from private print-pagination clones**. It is HTML-only optional source expansion, not a new or preferred study-aid type. The original 1,500–2,000-word visible allocation and Arabic/English language-fidelity protocols are unchanged.

This amendment supersedes earlier descriptions of a single end-of-chapter Source Depth appendix or plain-text Stout popups. See [the binding context-first protocol](CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) and the source-coverage register.

## Binding 19 November clarification for all subsequent readings

**Use the completed 1.1.1/1.1.2 standard, not the superseded earlier pilot language elsewhere in this historical document.** Contextual Companions prioritize the present sentence's meaning and argumentative purpose; simpler restatement is acceptable. Source Depth stays closed, directly after the appropriate paragraph, with source-page references, grouped records as needed, no auto-opening, no print/PDF output, no hidden search hits, and native accessibility even without JavaScript. The main argument and all six revision sections must stand without either optional layer.

Literature-style reading-specific **chapter-pigment dotted underlines** change to **solid on hover/open**, plus separate keyboard focus indication and semantic keyboard/touch/RTL support; test Escape and explicit close restoring focus without triggering an immediate reopening. Select richer source-evidence/formula/diagram content only where it serves a concrete learner question; preserve provenance, readable text equivalents and Hikam's existing component/tokens. A timeline replaces a table only for a genuine sequence, not for a comparison. All established study aids remain equally valued; EL10 is only an occasional technique.

For every future chapter, the release gate includes the permanent **`src/tests/browser_design_tokens.py`** regression (360° cycle across 39 chapters, original fonts and semantic colors, readable foreground/background), complete source attribution and coverage, Companion anchor integrity, search, no-JavaScript Source Depth, responsive/RTL/keyboard, real A4 PDF and PWA offline checks. Dispatch the second-account fork's reusable **`hikam-fork-verify.yml`** with an explicit editorial branch, inspect the results and generated Git blobs, and only then transfer through the primary review/merge workflow. The fork never publishes the original repository automatically. See [the complete binding accessibility and Source Depth section](CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md#8-binding-future-reading-protocol--accessibility-contextual-richness-and-source-depth).

**Latest application (19 November 2026):** The Gary Gutting reading 1.1.4 now follows the same approved source-dependent teaching distribution: **824 prose + 1,017 existing study-aid words**, 12 local context-first Companions, nine optional paragraph-adjacent, source-cited disclosures and all six revision sections. Its [original-source coverage register](READING_1_1_4_GUTTING_SOURCE_COVERAGE.md) records the necessary distinctions and a fully passed [fork verification](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44562601029). The implementation does **not** change this protocol's original Arabic/English, completeness or design restrictions. The early pilot descriptions further below are historical records, not current limits.

## Adopted source-proportionate range — updated November 18, 2026

**This is the latest instruction and supersedes the former single ~1,500-word planning average wherever it conflicts.** The immediately visible dossier body should ordinarily contain **approximately 1,500–2,000 words**, in a source-dependent ratio: **650–850 words of main prose** and **850–1,150 words of instructional study aids**. For a shorter or less intricate primary reading, plan near **650 + 850 = 1,500**. For a longer, denser or more argumentatively complex reading, plan progressively up to **850 + 1,150 = 2,000**. Select the position within this range by the **actual article's length and intellectual complexity**, not by a desire to fill pages. This is a **normal operating range**, not permission to delete indispensable source content to satisfy a ceiling.

Exclude chapter frontmatter, all six revision sections and optional Reading Companion text from both visible-word categories; record their lengths separately. Do not count Companions as part of the aid allowance. **The author's complete essential argument stays understandable without opening a Companion.** The additional source-grounded examples, qualifications, evidence, distinctions and local technical explanations may be delivered contextually through companions where doing so improves comprehension without duplicating the visible text.

**The previous language instructions are unchanged in every layer**, including every main-body sentence, aid, companion title and explanation, Arabic source text, revision element, caption and source label. This amendment is a distribution/length policy, not a language-policy change.

## 1. What was examined and what each reference repository teaches

The following **actual source files** were examined on `main`, 18 November 2026. The two reference repositories are private; their conceptual patterns are recorded here, not copied into a public repository as proprietary code or unpublished content.

### World History Dossier — `MohdUjjain/11-history`

- `src/chapters/ch01.html`, `src/chapters/ch03.html`: technical terms appear within the existing reading as `button.glossary-term` with an inline `data-definition`. For example, `imperial power`, `formal independence`, `dyarchy` and `internationalism` are clarified **on first meaningful use**, not through a new explanatory section. The sample chapters already carry many contextual definitions within coherent historical arguments.
- `src/docs/authoring/NEW_NOTES_WORKFLOW.md`: **one conceptual owner per layer**. The hero gives orientation; main prose owns the historical causal explanation; an inline term supplies its local definition; a study aid must perform a distinct comparison, memory, mistake or examination operation; revision supports independent recall. Do not put the same definition in both the popup and a nearby definition card.
- `src/docs/editorial/CH01_SOURCE_GROUNDED_EDITION.md` and `src/docs/editorial/CHAPTER_BY_CHAPTER_LANGUAGE_PASS.md`: preserve each author's thesis, evidence, causal mechanisms, exceptions and conclusions while removing **semantic repetition**, not distinct scholarly content. Keep each chapter's original title and author visible; clarify jargon without deleting technical terms. Source fidelity and coherence are assessed against actual textbook chapters.
- Useful interaction **inspiration**: quiet dotted terms, keyboard/touch/hover explanations, non-interference with the reader and deliberate retention of a revision glossary for printable study. History's popups are principally **short definitions**; importing them alone would not solve Hikam's more extensive coverage requirements.

### Literature Dossier — `MohdUjjain/11-literature`

- `docs/reading-companions-methodology.md`: a Reading Companion is a **short, complete, optional, non-redundant explanation** attached to an exact existing phrase; it answers the local question the reader cannot resolve from prose and callouts. There is **no required number or hard word quota**. The six acceptance gates are: **(1)** immediate-prose nonduplication; **(2)** study-aid/revision nonduplication; **(3)** genuine intellectual added value; **(4)** support from the assigned source; **(5)** local sufficiency; **(6)** unchanged text and safe exact anchor. An initial eight-entry pilot was reduced after duplication review.
- `source/reading-companions.json`: the actual manifest currently records **219 explanatory companions** (separately from poetry and visual evidence). Each entry records a stable ID, exact passage anchor, quoted existing trigger text, category, informative title, self-contained explanation, source PDF pages and `added_value` justification. `sources_by_reading` identifies editions. Candidate explanations are reviewed reading by reading, not manufactured to reach a numerical quota.
- `reader-companions.js`: uses a unique exact match within a specified passage, creates a quiet inline cue **at runtime**, keeps the original text content unchanged, positions the explanation in the viewport, and supports mouse, touch, keyboard Enter/Space/Escape, dismissal and reading-position continuity. An absent or ambiguous anchor is rejected rather than guessed.
- `tests/phase3_companions_browser.mjs`: checks all expected cues, ambiguous anchors, mobile and desktop placement, wrapped multiword underlines, keyboard activation, Escape and original reading behavior. The native inline-box wrapping issue led to a text-wrapping `span[role=button]` implementation rather than non-wrapping native buttons for multiword phrases.
- `docs/reading-companions-reading-18-audit.md`: Gandhi's *Hind Swaraj* example shows how **five** companion explanations were accepted because they clarified specific source distinctions missing from adjacent prose and callouts; other candidates were rejected for duplicating already-taught material. The source's dialogic assertions were not converted into independent factual claims.
- `docs/reading-18-main-notes-editorial-pilot-2026-11-16.md`: source-proportionate pilot reduces a reading's main prose to **528 words** while keeping the intellectual sequence; its existing study aids and revision material remain separately accounted for. This provides an example of **compact argument structure**, not a universal 528-word rule.
- `docs/reading-companions-evidence-standard.md`: distinguishes **explanatory** companions from original-source evidence (original verse, historical document, article map, source table, faithfully reconstructed chart). Evidence exhibits require provenance, source notation and stated limitations; reconstructions must be explicitly labelled. Not every reading needs such an exhibit.
- Literature's screen-only explanatory Companions are deliberately **not the sole source of an essential academic assertion**. Hikam's adoption must preserve that safeguard while distributing fuller source detail into optional layers.

**Conclusion from these repositories:** Reuse **History's contextual simplicity** and **Literature's scholarly selection/traceability and technically careful point-of-reading interaction**. Do **not** copy their complete design, their chapter structures, their prose, their extra visual features or their software blindly into Hikam.

## 2. The fixed word-density decision

These figures are **programme-level editorial averages**; they are **not** a demand for every individual reading to contain exactly this number of words, and are not grounds to remove an indispensable source distinction.

| Visible reading layer | Planning average per dossier | Included | Excluded |
| --- | ---: | --- | --- |
| **Main explanatory prose** | **~650–850 words** | Ordinary chapter-body narrative, paragraph text and main-body headings outside aid components | Main-body callouts/tables, frontmatter, revision block, optional Companion contents |
| **Existing instructional aids** | **~850–1,150 words** | Existing `.box.*`, quotations, section objectives, analogies, concept maps, hierarchies, comparisons/tables, checkpoints, tips and other semantic teaching components | Main explanatory prose, frontmatter, revision block, optional Companion contents |
| **Total immediately visible main-body study** | **~1,500–2,000 words** | Sum of the two categories | Frontmatter, revision block and optional Companion contents |
| **Reading Companions** | **No word quota** | Only source-justified local explanations and evidence with verified triggers | They are audited separately and never used to pad the 850-word aid average |
| **Established revision block** | **Preserve independently** | All six existing components and examination categories | It is **not** charged to either 650 or 850 |
| **Chapter title/frontmatter/roadmap** | **Preserve independently** | Original title and author, roadmap, accurate central thesis | It is **not** charged to either 650 or 850 |

The prior 39-dossier HTML audit found average plain explanatory prose and aid text near **665 / 857** words, while the 37 dossiers other than the overexpanded 1.1.1 and 1.1.2 averaged approximately **495 / 776**. The two newly expanded dossiers were far above the intended model. These new targets restore the book's intended **study-note density** rather than demand new length throughout.

**Measure against the actual canonical HTML**, excluding `.end-block` and `.chapter-frontmatter`. Report each reading's prose, study-aid, Companion and revision counts **separately**. Readability and source fidelity are decisive; an unusually dense reading may require a justified variance. Never expand a short chapter just to hit a number or silently delete a source premise to get under a count.

## 3. Four complementary intellectual functions

1. **Main explanation — the author's intellectual spine.** In simple, precise Arabic or English, show the problem, principal thesis, necessary premises, decisive distinctions, principal evidence, key objection/reply where supplied, and conclusion **in the author's own progression**. Favor connected, straightforward sentences and complete one-line points over developed mini-essays. The main notes must remain intelligible when Companions are disabled.
2. **Study aids — distinctive learning operations.** Assign factual comparisons to tables, sequences to timelines or hierarchies, essential meanings to definitions, real ambiguities to mistake cards, simple bridges to analogies/EL10 where appropriate, and retrieval to checkpoints. Do not re-narrate the same material in every component. All established types retain equal standing.
3. **Reading Companions — exact local difficulty or fuller source detail.** A quiet cue on an **already present phrase** can explain a precise technical qualification, the reason for an inference, an omitted illustrative source case, an author's handling of evidence, a distinction between similar concepts, or a short connection that would otherwise expand the running prose. They are **not** a shadow chapter, long explanatory essays, a generic glossary quota, or a hiding place for independent research.
4. **Revision block — independent recall, not a substitute for teaching.** Keep Chapter Summary, One-Page Revision Sheet, Key Definitions, Key Table, Memory Aids Collected and Possible Examination Questions, with Short Answer, Long Answer, Comparison, Conceptual and Application items. Revision counts remain outside the planning word averages.

**Coverage rule:** every important unit of the primary reading must be traced and assigned a meaningful home. An indispensable premise, thesis or objection must be clear from the **main reading and study aids** even if the Companion does not open. The **more detailed source qualification, illustrative evidence, case, derivation or technical clarification** can live in a Companion at its relevant phrase. If a source-critical assertion truly exists **only** in a Companion, the proposed edition must provide a tested, non-interactive **print/offline recovery route** before approval; never allow essential substance to disappear from printable or no-JavaScript study. The precise print treatment is an implementation decision, not an excuse to change the existing print engine before testing.

**Important:** a shorter note can still be faithful if its wording selects and connects the author's real claims, while nonredundant detail remains accessible. A short chapter is *not* faithful if key claims, author qualifications, objections, evidentiary cases or conclusions are simply deleted.

## 4. Language rules do not change in any layer

- The full standing protocol and the user's **`skill - language profiling.md`** and Arabic writing samples still govern **Arabic prose, English prose, all study aids, all Reading Companion titles and explanations, source labels, captions and revision text**.
- Use natural, very easy-to-follow **scholarly** language, with source terminology defined at first meaningful use. Short sentences and one-line points must remain grammatically complete and logically connected, never terse jargon fragments.
- For Arabic, preserve the source author's confidence and the user's accessible Arabic voice, with correct RTL, `lang="ar"`, Amiri, directionality and `<bdi>` as applicable. Do not mechanically translate English text or write thesis-level syntactic density just because the language model samples are dissertations.
- Source fidelity overrides all stylistic choices: preserve the author's position, sequence, certainty, source attribution, objections, replies and conclusions. Do not insert independent philosophical adjudication, artificial balance, unsolicited hedges or general-knowledge corrections.
- EL10 is **only** a local technique for helping an intrinsically difficult concept become intuitive; it is neither a phase, a quota, nor more important than any other aid. A Companion is likewise a delivery mechanism, **not** a waiver of language rules.

## 5. Acceptance gates for each proposed Companion

For **each candidate**, answer the questions below **before inclusion**:

1. **Real question:** what exactly will the learner fail to understand from the nearby notes?
2. **Not already taught:** do the immediate sentence, surrounding paragraphs, tables, memory aids, other callouts, roadmap or revision block already give the answer? If yes, omit or change the Companion's function.
3. **Source-grounded:** where is the passage in the complete original file (page/section)? Whose statement is it and how certain is it?
4. **Distinct intellectual value:** does it clarify a definition, mechanism, comparison, inference, objection, reported testimony, example, terminology, method or source evidence **not sufficiently covered already**?
5. **Local completeness:** can it answer this one reader question directly in the **shortest accurate language**, without “read more,” jumping to another box or another popup?
6. **Exact safe anchor:** can the cue attach to a **unique existing phrase** in an identified chapter/passage **without rewriting that phrase**, moving content, or swallowing adjacent text? If ambiguous, flag and withhold.
7. **Fallback:** does the dossier retain its indispensable argument when annotations are off or missing? If the Companion contains otherwise unique critical material, is the corresponding print/no-JS recovery tested?

**No count or length quota:** zero Companions can be correct; a dense scholarly reading may need more. A 12-word answer may work; a technical point may require 45 or more. Select only the shortest **complete** source-faithful explanation. Never use popups to hide arbitrary numbers of long paragraphs.

### Per-candidate source-coverage register

Keep a compact evidence record (internal during authoring; publish only editorial metadata where appropriate):

| Field | Required |
| --- | --- |
| Dossier and primary reading | Original title, author, edition and file/page scope when available |
| Source unit / scholarly role | Thesis, premise, evidence, distinction, objection/reply, qualification, example, conclusion |
| Visible home | Exact main-body sentence/aid or section that establishes the essential idea |
| Companion role (if any) | The specific still-unanswered question and source-backed detail it adds |
| Unique anchor | Chapter ID, stable passage identifier where needed and exact existing words |
| Source citation | Original page(s), section and whose claim it represents |
| Redundancy check | What was compared in prose, aids and revision; why popup does *different* work |
| Decision | Include, rewrite, merge, omit as duplicate, or flag as unverifiable |
| Test result | Anchor uniqueness, full source continuity, keyboard/touch, RTL, print, offline/search |

The coverage register must show **no important source unit lost**. An unverified assertion does not become acceptable merely because it is moved from prose into a popup.

## 6. What a Hikam implementation must preserve

**Current repository constraints:** `src/main.html` provides the TOC/cover; `src/chapters/subtopic-*.html` owns academic content; `src/philosophy_notes.css` and `src/philosophy_notes.js` own the existing design/reader and JS print pagination; `src/build.py` generates `src/philosophy_study_notes.html`, published `index.html` and content-hashed `service-worker.js`. Arabic chapters have RTL/Amiri conventions. The single-page reader includes navigation, chapter progress, search, reading resume, hidden revision, print selection and offline functionality.

**Recommended design to validate in a small pilot before touching all 39 dossiers:**

1. An **independently authored Companion manifest**, with stable ID, chapter ID, stable paragraph/section anchor, exact trigger text, short category and title, explanation, original source page and an `added_value` editorial field. Keep private or restricted primary source contents outside the public repository; a public Companion record must not reproduce restricted long passages.
2. The reader attaches a subtle, chapter-accent **dotted underline** to an exact **single** text occurrence in the *main explanatory region*, never inside revision, quoted source strings, tables or other callouts by accident. No fuzzy substring fallbacks. The original scholarly text and copy/search text must remain intact.
3. **Screen only:** on hover where supported, click/tap or keyboard activation, show a small readable, source-grounded, **self-contained** popup. Escape, outside click, focus departure or location change closes it. Mobile viewport positioning, multiword wrapping, keyboard focus, ARIA semantics, reduced motion, and **Arabic RTL typography** must be tested.
4. No automatic navigation, “open full explanation,” scroll jump, stacked mini-lessons, change of hash, saved reading position, active section, sidebar semantics, study-aid palette or revision visibility.
5. Hikam's currently generated **single-file HTML** and content-hashed PWA differ from Literature's external JSON reader. The selected manifest delivery must work offline and remain in the **atomic edition**. Prefer inlining the small validated metadata at build time or otherwise formally caching/versioning it; do not silently rely on an online JSON fetch.
6. **Print and source preservation:** unwrapping any screen-only cues from **private print clones** is a tested necessity for today's JS pagination. The print/PDF must remain coherent, correctly paginated and free of broken buttons. If unique indispensable source detail would otherwise be invisible, determine and test a proper optional print/evidence appendix or equivalent before making the popup its only home; never dump hidden popups into print pages unreviewed.
7. Confirm no loss of chapter/TOC IDs, author and exact title credits, original quotations, six-part revision zones, search results, progress, resume behavior or offline cache. No unrelated redesign or wholesale CSS/JS refactor.

**Scope boundary (pilot):** Hikam now has a small, internally authored Reading Companion controller and manifest for 1.1.1 and 1.1.2, documented in [the pilot audit](READING_COMPANIONS_PILOT_1_1_1_1_1_2.md). This does **not** mean all dossiers are annotated, an original-evidence viewer has been built, or the expanded chapters have been shortened. Browser/print/PWA verification and a source-to-layer coverage map remain required before expanding the pilot or compressing chapter content.

## 7. Per-reading editorial procedure under the new word decision

1. Reopen the standing protocol, this file, the actual original source, the currently published dossier and its study/revision aids; confirm title/author.
2. Make a complete **source-unit traceability map** before trying to shorten anything.
3. Write a very clear **~650–850-word intellectual spine**, scaled to the actual reading, keeping the author's reasoning, not extended lectures. Put compact comparisons, definitions, diagrams, quotes, checkpoints and exam aids into **~850–1,150 words of purposeful study aids**, preserving established types where useful.
4. Identify remaining source-specific detail and difficult points. Apply the updated context-first gates: write source-backed, simple, locally complete popups when they genuinely clarify an immediate idea, even by restating it more simply. Assign further source-specific details to optional paragraph-adjacent Source Depth where justified; never use a popup to launch an unrelated subject. Distinguish author examples from newly devised educational illustrations.
5. Review **semantic repetition** across body, hero, all aid types, companion candidates and revisions. Remove redundant *exposition*, not separate premises, counterarguments, cases or qualifications.
6. Re-check every important unit of the original against its assigned location; confirm authorship, quotations, cited pages, strength of claims and any unresolved source gaps.
7. Audit four word pools **separately**: explanatory prose, existing teaching aids, optional companions and end-block revision. Report why a particular reading differs materially from the programme average.
8. Rebuild canonically, verify integrity and actual reading interaction, print/RTL and offline packaging; report precisely what was tested. **Never claim a chapter has been condensed or companions installed when only the instructions have changed.**

### Immediate programme implication

The **1.1.1 (Moran)** and **1.1.2 (Stout)** source-faithful concise editions and their context-first, paragraph-adjacent Companion/Source Depth teaching method are already published. The next reading, **1.1.3 (David Papineau, _Philosophy of Science_, _The Blackwell Companion to Philosophy_, 2nd ed.)**, has now completed its full primary-source comparison and controlled edition under the same standard. Its [completed source-coverage register](READING_1_1_3_SOURCE_COVERAGE_PREPARATION.md#v-completed-source-coverage-resolution--final-113-edition-19-november) records 821 visible prose words, 1,137 equally important study-aid words, 12 contextual Companions and nine optional Source Depth records; the complete fork CI passed before public release.

**Final editorial standard:** **~650–850 words of immediately readable scholarly prose + ~850–1,150 words of genuinely useful study aids (together ~1,500–2,000, source-proportionate) + optional, exact, context-clarifying, source-grounded Reading Companions + separately optional paragraph-adjacent Source Depth + independently preserved revision material.** Helpful restatement can add understanding without new factual content. All source-relevant information remains traceable; all original Arabic/English language and established design rules remain binding.
