# Design System — Philosophy Revision Dossier

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

> **Repository paths (November 2026):** The authoritative stylesheet is `src/philosophy_notes.css`, the book spine is `src/main.html`, chapter fragments are in `src/chapters/`, and the builder is `src/build.py`. Historical records below retain the filenames and inventories used at the time.

This document describes the existing visual system and the acceptance requirements for later authorized work. For pagination and printing architecture, read [PAGINATION_SYSTEM.md](../pagination/PAGINATION_SYSTEM.md). For current component functions, word limits, source ownership and reading priorities, read the [Study Aid Roles and Reading Design Protocol](../editorial/STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md), together with the [Language and Source Fidelity Protocol](../editorial/LANGUAGE_AND_SOURCE_FIDELITY_REFINEMENT_PROTOCOL.md). The [Audit and Migration Plan](../editorial/STUDY_AID_REFINEMENT_AUDIT_AND_MIGRATION_PLAN.md) separates observed evidence from pending work.

**28 November 2026 — documentation-only authorization:** the latest accepted role rules supersede conflicting older component descriptions. They do not authorize reader/CSS/content implementation, new colours, final icon assignments, a new explanatory callout family, or full-prose bullet conversion. Keep the existing tokens and architecture. Measured typography below is a baseline, not a selected replacement specification. Dated changelog entries preserve implementation evidence; they are not current permissions to add retired tips/checkpoints or embed EL10 in other roles.

The source controls the author's intellectual position, certainty, evidence, qualifications, quotations and conclusions. Design, simplification and reading-priority decisions must preserve them. Essential reasoning remains in the visible main path and ordinary print; optional controls or a proposed future appendix cannot be its only home.

The existing [context-first Companions and paragraph-adjacent Source Depth](../editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md) remain the interaction model. Native `details.hikam-source-depth-inline` belongs immediately after its associated ordinary paragraph, in HTML. Companion cues use the chapter's rotating hue, dotted at rest and solid on hover/open, with visible focus and accessible state. Verification is scoped to affected components and applicable gates; the historical full-suite and exact-39-chapter reports are not requirements for every edit.

## Philosophy

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Parchment / navy ink / gold academic dossier. Distinctive on purpose — not a
generic template. Two rules that protect that:

- **Structure over decoration.** Every visual device (box, hierarchy, badge)
  exists to carry information, not to look nice. If you're adding a visual
  element that doesn't map to a real content distinction, don't.
- **Chapters get their own accent hue; the semantic system never does.**
  Existing semantic tokens (below) are colour-coded consistently across
  the book. Retiring a role does not silently repurpose its token; final
  refinements to colours and icons remain pending. A `.box.definition` is the same blue in chapter 1.1.1 and
  in chapter 3.1.3. Only *structural chrome* (banner, tab, table headers,
  quote rule, hierarchy dots) uses the chapter's rotating `--hue`.

## Palette

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1C2740` | primary text, dark surfaces (banners, end-block, sidebar) |
| `--ink-soft` / `--ink-faint` | `#3C4A68` / `#6B7590` | secondary text |
| `--gold` / `--gold-deep` / `--gold-pale` | `#A87C1F` / `#7C5A12` / `#F1E1AE` | accents, links-on-dark, the one warm colour in an otherwise cool book |
| `--parchment` / `--parchment-deep` | `#F7F1E3` / `#EFE3C8` | page background |
| `--white-card` | `#FCF9F0` | slightly-lifted card background on parchment |
| `--paper-line` / `--paper-line-soft` | `#D9CAA2` / `#E6DAB9` | hairline dividers |
| body background | `#DCD3BC` | the darker backdrop pages/chapters now float against (see Elevation, below) |

### Existing semantic tokens and their role boundaries

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

These are the **existing** colours and observed icons, not a newly approved final colour/icon assignment. Preserve the tokens while documenting the accepted functional changes. A class or colour does not by itself establish that its content satisfies the role.

| Existing class | Observed icon | Existing colour | Current role boundary |
|---|---|---|---|
| `.box.definition` | D (🟦) | `#1F4173` blue | Definition of a term; not historical comparison or extended explanation. |
| `.box.concept` | C (🟩) | `#256B45` green | The dossier's single opening central concept/thesis. |
| `.box.tip` | ! (🟨) | `#96540E` amber | **Legacy examination-tip role, retired from the main body.** Token retained as implementation history; no automatic reassignment. |
| `.box.mistake` | ✕ (🟥) | `#8C2E2E` red | A concrete source-based misunderstanding and its correction. |
| `.box.memory` | ♥ (🟪) | `#5A3A78` purple | A retrieval operation, not an alternative container for an explanatory EL10 analogy. |
| `.box.highyield` | ★ (gold) | `#7E5C0C` | A source-grounded point or relationship especially useful to grasp or remember; not a prediction about examiners. |

Each has a `-bg` tint and `-bd` border variant, such as `--c-def-bg` and `--c-def-bd`. Shared uses of a token elsewhere do not revive a retired component. The 29-dossier audit found 13 icon omissions among 207 boxes, concentrated in 3.2.1–3.2.5; later correction must follow the eventual agreed icon treatment. This documentation pass selects no replacement icon set or palette.

## Cross-component contrast and hue allocation

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**This is the existing design, not a new palette.** The **19 November 2026 verification baseline contained 39 chapters**, allocated at 20° intervals through the full HSL circle beginning at `--hue:208` for 1.1.1:

```
chapter hue = (208 + 20 × (chapter position - 1)) modulo 360
```

The sequence reaches 348° at 2.1.3, wraps to 8° at 2.1.4, and repeats after 18 chapters. A second wrap occurs between 3.2.2 (348°) and 3.2.3 (8°). No hue is reset at a topic boundary. The 18 chapter accent colors should continue to be applied through the existing `hsl(var(--hue) ...)` rules for **structural chrome** (banner, stamp, table header, timeline, revision heading and other structural markers). The six fixed **semantic** callout colors never rotate.

**Foreground must follow its surface**, even across parent/child component boundaries. A dark chapter banner or dark `.end-block` uses the existing light ink/cream foreground; a light `table.comparison` always uses the existing `--white-card` surface and `--ink` foreground, even when the table is nested inside `.end-block`. The chapter source's bold author name must **inherit the source line's light foreground**, not the global prose `strong` rule. Similarly, emphasis in dark revision prose should inherit its local readable color. Table paragraphs and cells must not inherit revision cream on light paper. These rules belong in the shared stylesheet and apply wherever the component pairing occurs; never patch isolated cells, authors or chapters using arbitrary colors. A shared style change still requires separate implementation authorization.

At that baseline, `src/tests/browser_design_tokens.py` checked actual Chromium computed styles at 390px and 1366px: the then-current 39-chapter hue allocation and 18-stop wrap, six semantic token surfaces, the existing Fraunces/Source Serif 4/IBM Plex Sans stacks, author-credit visibility and WCAG AA 4.5:1 foreground contrast in revision comparison-table cells. The dated count is not a permanent current-corpus gate. When later authorized work affects these properties, inspect the applicable test and current allocation before running a scoped regression. Fix a failed **component pairing** at its cause rather than adding compensating late overrides.

**First verification:** [Secondary-account GitHub Actions run 44524655246](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44524655246) passed the complete canonical build, source/structure tests, Chromium computed-style audit at 390px and 1366px, Reader/RTL, real PDF pagination and offline/PWA regressions. The computed-style audit confirmed **39 chapters**, **18 unique rotational hues**, **two existing revision comparison tables** (Moran and Stout), **two authored source-credit emphasis instances**, and the six fixed semantic backgrounds. The missing table/author contrast was caused by CSS foreground inheritance, not by a missing or reset hue sequence. No source text or semantic callout type was revised.

### Stable hue allocation for catalog insertions

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The 39 chapter hues in that historical baseline were retained when the first two 3.3 dossiers were inserted in numerical reading order. New 3.3.2 and 3.3.3 use the next two slots of the same 20° wheel (268°, 288°), while 3.4.3 retains 128°. Dossiers 3.3.4–3.3.6 use the next slots at 308°, 328°, and 348°. Dossiers 3.3.7 and 3.3.8 continue at 8° and 28°. Dossier 3.4.2 then takes 48°; the existing 3.4 hues remain in place. Dossiers 3.5.1–3.5.4 continue with 68°, 88°, 108°, and 128°. Dossiers 3.6.1–3.6.6 adopt 148°, 168°, 188°, 208°, 228°, and 248° in order. Dossiers 3.7.1–3.7.3 continue at 268°, 288°, and 308°. Dossier 3.8.2 and combined 3.8.3–3.8.4 continue at 328° and 348°. Check the full hue cycle in allocation order; screen and print retain chapter-number order. This does not change the palette, semantic callout colors, or page geometry.

## Typography

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

| Token | Stack | Use |
|---|---|---|
| `--font-display` | Fraunces | h1/h2, chapter titles, big display numerals |
| `--font-body` | Source Serif 4 | running prose, golden-quotes |
| `--font-sans` | IBM Plex Sans | UI chrome: kickers, labels, buttons, sidebar |
| `--font-mono` | IBM Plex Mono | page numbers, dossier numbers, sidebar `#N` |
| `--font-arabic` | Amiri | Arabic prose and display text, with explicit component exceptions below |
| `--font-arabic-sans` | Noto Sans Arabic | Actively used by the explicit RTL exception list for labels, table headers, citations and other selected components |

The global `.ar` / `[lang="ar"]` rule supplies the Arabic font, RTL direction and bidi isolation. Preserve that semantic markup. It does **not** guarantee correct typography for every descendant: an explicit component `font` or `font-family` rule can override an inherited Arabic value. The existing RTL exception list actively uses Noto Sans Arabic; inspect actual computed descendants before diagnosing font, size or joining problems. This documentation pass chooses no new typography values or replacement font policy.

## Elevation system (added in the "SaaS" pass)

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Radius and shadow are tokens, applied consistently rather than per-element
guesses:

```
--radius-sm: 10px   small chips: section-objective, rel-node, memlist items, sidebar rows
--radius-md: 16px   content boxes: .box, .analogy, tables, hierarchy/checkpoint/concept-rel, golden-quote, revision-sheet
--radius-lg: 24px   (reserved — not currently used, headroom for a future component)
--radius-xl: 32px   the two "sheet" containers: .page and .chapter

--shadow-card  the big page/chapter float — layered, navy-tinted, not flat black
--shadow-soft  subtle lift for nested cards (cover-part-card, tables)
--shadow-pop   hover state — buttons, cards, the sidebar itself
--shadow-inset  (available, currently unused)
```

Pills that were already maximally rounded (`toc-back`, `endnav-btn`, `secnum`,
`rel-badge`, `tt-num`) keep their literal `20px`/`30px` values rather than
being forced onto the token scale — they're already at "as round as a
rectangle-with-text can get," the tokens exist for elements that had *flat*
corners before.

**Circles stay circles** — seals, dots, the FAB, box icons all use
`border-radius:50%` and are untouched by any of this.

**Current print behavior:** the v3 print reset makes physical page-boundary elements (`.page`, `.chapter`, `.chapter-banner`, `.end-block`, `.js-print-page`) square. Content islands inside the page, including boxes and tables, retain their rounded corners. Listed shadows and hover transforms are removed for print. Preserve this distinction: the earlier all-flat reset is a historical iteration, not the present rule. Inspect the actual print selectors and pagination behavior when later authorized work affects an element; do not add a blanket radius reset or an overflow rule that clips generated pages.

## Structural component glossary and accepted limits

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Role is established by intellectual function and source ownership, not by HTML class or appearance. Paragraph-form aids can perform valid teaching functions. Preserve source material when a later authorized migration removes, shortens or reclassifies an instance. Complete-body counts exclude external category labels/icons but retain substantive inline content; preserve block and cell boundaries when extracting text.

| Component | Existing structure | Accepted role / requirement |
|---|---|---|
| Chapter roadmap | `.in-this-chapter` | Before any `§`; **7–15 words per point**, including a **bold topic lead-in** and source-faithful preview. No fixed point count. |
| Central concept / thesis | `.box.concept` | **Exactly one**, at the beginning of the dossier's main study content, **40–75 words**. Additional concept boxes require functional reclassification. |
| Definition | `.box.definition` | Definitions only: **≤20 words and ≤2 sentences per definition; ≤2 definitions per box; ≤40 words for the whole box**. No transfer of unused words between entries. |
| High-yield | `.box.highyield` | Source-grounded importance or a valuable relationship; **≤40 words** for the complete body. |
| Common mistake | `.box.mistake` | Correct a source-based confusion; **≤35 words** for the complete body; no independent adjudication of the author. |
| Memory | `.box.memory` | A meaningful retrieval cue or operation; **≤30 words** for the complete body. |
| Source quotation | `.golden-quote` with `<cite>` | Verbatim quotation with context, actual ownership and reference; no new word cap. |
| Section objective | `.section-objective` | The genuine question answered by the section, after its heading; included in the visible aid budget. No new universal word cap. |
| Hierarchy / sequence | `.hierarchy` and its nodes | Decimal levels for parent–child relations; ordinary numbering for actual steps; peers share a level. Do not infer intellectual rank from CSS indentation. |
| Concept relationship map | `.concept-rel` | Concise concepts and explicit short source-grounded relations; no substantial attached paragraph masquerading as a node. |
| EL10 / ELI10 / compiler-added analogy | Dedicated analogy container, using the approved existing architecture | The three names denote the same role: a compiler-added explanatory analogy, **20–30 words**, hard maximum 30; no quota and no embedding in memory/other roles. |
| Source analogy / simple explanation | Existing source-content presentation with explicit attribution | An analogy or explanatory comparison supplied or cited by the author, preserving its inference; outside the EL10 cap. Source-derived non-analogies require reclassification, not unlimited generic callouts. |
| Tables / comparisons | `.tbl-wrap`, `table.comparison` | Every physical cell, including column headers, row headers and revision tables: normally **≤10 words**; **11–20 only for accuracy**; hard maximum **20**. |
| Timeline | `.historical-timeline` | Source-grounded chronological sequence; a thematic comparison stays a comparison. |
| Examination tip / checkpoint | `.box.tip`, `.checkpoint` | **Legacy main-body components, retired.** Necessary source content must be accounted for during later migration. No midpoint checkpoint quota remains. |
| End-of-chapter revision | `.end-block` | Exactly: Chapter Summary → One-Page Revision Sheet → Key Definitions → Key Table → Memory Aids Collected → Possible Examination Questions. |
| Exam questions | `.examq` | Five classes in order: Short Answer, Long Answer, Comparison, Conceptual, Application. Retirement of main-body tips/checkpoints does not remove these. |
| Table title | `<caption>` in the table | Existing centered, chapter-hue treatment; preserve the distinction between a caption, top headers and semantic row headers. |

Individual definitions, memory devices and table cells retain their limits in revision or optional layers. Entire revision collections do not acquire a 20-, 30- or 40-word aggregate cap; a definition callout still has at most two definitions. A necessary long source quotation belongs intact outside a bounded cell or memory unit, rather than bypassing its limit.

### Memory, analogy provenance and pending categories

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Memory can use mnemonics, acronyms, memorable phrases, visual associations, memory palaces, conceptual anchors, comparison tricks, pattern recognition and “remember this because” connections. A suitable short source quotation is allowed with its attribution and the same 30-word memory-body cap. Its retrieval operation must be identifiable, its cues must agree with its label, and its content must remain source faithful. Compiler-created cues do not become source quotations or evidence.

A compiler-created **explanatory analogy** belongs in the dedicated EL10 role even when memorable. A source author's own or cited analogy belongs to source content with its actual ownership. Check the supplied original before assigning provenance; an old class, missing quotation marks or a familiar image proves neither origin. Keep unresolved cases explicit. A direct explanation, classification or summary does not acquire an unlimited allowance by being source-derived or labelled “simple explanation.”

The general-purpose explanatory callout remains a **proposal**, not an approved family. Final colour/icon assignments and the full-prose bullet conversion remain deferred. The optional page-based central-concept formula is only a planning proposal within 40–75 words; no source-page number or calibration silently becomes a required length. Reading priorities describe the learner's route, not whether an author's claims are true or acceptable.

## Numbering & content conventions

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

`Topic` (1 digit) → `Sub-topic` (N.N) → `Chapter`/"Dossier" (N.N.N). One
`.part-divider` page per Topic *and* per Sub-topic (except Topic 1, whose
single sub-topic 1.1 is folded into the Topic-level divider rather than
getting its own — a historical quirk, not a pattern to copy for future
topics with more than one sub-topic).

Recorded catalog snapshot (use the live canonical spine and sidebar for the
current inventory; historical counts elsewhere in this document are dated):

- **Topic 1** — Sub-topic 1.1, chapters 1.1.1–1.1.5 (English)
- **Topic 2** — Sub-topic 2.1 (2.1.1–2.1.8, English + 2 Arabic), Sub-topic 2.2
  (2.2.1–2.2.6, Arabic + 2 English)
- **Topic 3** — Sub-topic 3.1 complete (3.1.1–3.1.5, three English + two Arabic),
  Sub-topic 3.2 complete (3.2.1–3.2.8, six Arabic + two English),
  Sub-topic 3.3 has seven dossiers (3.3.2–3.3.8), and Sub-topic 3.4 has eight (3.4.2–3.4.9), and Sub-topic 3.5 has four (3.5.1–3.5.4), Sub-topic 3.6 has six (3.6.1–3.6.6), Sub-topic 3.7 has three (3.7.1–3.7.3), and Sub-topic 3.8 has two dossiers

### Chapter hue

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

`--hue` steps +20° globally in [allocation order](#stable-hue-allocation-for-catalog-insertions), wrapping at 360°. An insertion uses the next slot; it does not recolor existing chapters. The same hue recurs every 18 allocations.

### Arabic chapter markup and language

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Add `class="chapter rtl"` and `lang="ar"` to the
`<section>`. Keep the `.chapter-stamp` tagline in English (cross-book
scannability) but everything else — title, body, boxes, end-block — in
Arabic. Inline Arabic inside an otherwise-English element (for example,
`<span class="ar" lang="ar">الميتافيزيقا</span>` in a kicker) uses the
`.ar`/`lang="ar"` span. Check explicit descendant font rules as well as the
inherited direction; the markup alone is not a typography acceptance test.

### Mixed-direction section references

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Inline `§` section references inside Arabic prose need `<bdi>` around
them — e.g. `(<bdi>§I</bdi>)`, or `<bdi>§I–§IV</bdi>` for a range. Without
it, the Unicode bidi algorithm can visually reorder the reference's own
characters (renders as "I§" instead of "§I") wherever it sits inside
surrounding RTL text. This applies to inline references embedded mid-sentence
in prose, `.cr-title`, and `.rel-node` text.

### Section-number badges

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The `.secnum` badge (the `§I` chip at the start of every `h2.sec`
heading) has the identical bug and is fixed in the CSS, not per-instance.
This was wrongly believed to be exempt for a while — it isn't; it was just
easy to misread at small badge size. It affects *every* `h2.sec` in *every*
Arabic chapter in the book, old and new alike, not just newly-written ones.
Fixed once, centrally: `h2.sec .secnum{ unicode-bidi:isolate; direction:ltr;
}`. Note both properties are required — `unicode-bidi:isolate` alone isolates
the content from the surrounding bidi context but does **not** itself pick a
direction; the badge still inherits `direction:rtl` from its Arabic ancestor
unless `direction:ltr` is also set explicitly. (This is also why HTML's
native `<bdi>` element works without an explicit `direction` — per the HTML
spec `<bdi>` carries an *additional*, separate "auto-detect from content"
directionality heuristic that plain `unicode-bidi:isolate` on a `<span>`
does not replicate on its own.) Verified with `getComputedStyle` plus a
character-by-character bounding-box check in headless Chromium, not just a
screenshot — see `PAGINATION_SYSTEM.md` for how to run that check again if
a similar bug is suspected elsewhere.

### Explicit font rules and the Arabic cascade

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Font-family is a cause to check before assuming an ordering or alignment bug — a
user report of Arabic text "looking broken" turned out to mean this, not
the bidi-ordering issue above, and it was the more serious of the two. The
book's font cascade is: `.rtl{font-family:var(--font-arabic)}` (Amiri) sets
the default for a whole chapter by inheritance, then one shared exceptions
list (search the CSS for `.rtl .chapter-kicker, .rtl .box-label...`)
re-targets specific UI-chrome components (badges, table headers, labels) to
`var(--font-arabic-sans)` (Noto Sans Arabic) instead, under the established component distinction. That existing distinction
does not justify Latin uppercase tracking on Arabic text; check joining and
actual readability separately. **Any component with its own explicit `font-family`
declaration outside that exceptions list silently falls back to whatever
non-Arabic font it names** (usually `var(--font-sans)`, IBM Plex Sans, which
has no real Arabic glyph support) — because a rule that *directly* targets
an element always beats a value the element only *inherited* from an
ancestor, regardless of the `.rtl` ancestor's own specificity. This is a
CSS-cascade trap, not a typo, and it silently affects any newly-added
component that copies an existing English-only rule's `font-family` without
also adding a matching `.rtl` line to the exceptions list. Four components
were found missing (`table.comparison th`, `.memlist li b`,
`.golden-quote cite`, `.rel-row` — the last one meant `.rel-node`, which
holds real Arabic sentences, was inheriting the wrong font every single
place a concept-relationship map appeared in any Arabic chapter) plus the
table `<caption>` after it was redesigned and lost its inherited font along
the way. All four+one are now in the shared exceptions list.

### Scoped verification of Arabic font coverage

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

A targeted selector-by-selector
check is not enough — it only catches what you thought to test, and this bug
was found on the *second* pass, not the first. When an authorized shared CSS change affects Arabic font selection, use a
scoped Chromium check across the affected Arabic surfaces: walk
each affected element under `.rtl`, keep the ones whose own direct text node
contains an Arabic Unicode codepoint (`\u0600`–`\u06FF` etc.), and flag any
where `getComputedStyle(el).fontFamily` doesn't contain "Amiri" or
"Arabic". Zero hits is the bar — not "the ones I checked passed."

Before writing a new Arabic chapter, check an existing working one's markup
for these patterns rather than re-deriving them.

### Chapter-stamp taglines

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The established stamp guidance is 3–6 words. Its original measurement was
a historical 24-chapter sample (shortest 2; a one-off 7 was trimmed). That
record is not a current all-corpus count.
The circular badge is sized for that range — a longer one wraps to 4 lines
and looks visibly cramped next to every other chapter's clean 2–3 line
badge. Keep new ones inside that range rather than rediscovering the ceiling
by screenshot.

### Adding a chapter when authorized

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Copy an existing `<section class="chapter">` whole,
update id/hue/tabnum/stamp/title/source, add its TOC row. See
`PAGINATION_SYSTEM.md` for the *print*-side steps (page-name templates) —
those are easy to forget and fail silently (blank running header) if skipped.

## Arabic readability and presentation acceptance

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

These are acceptance requirements for **later authorized implementation**, not CSS changes enacted by this documentation pass. Their source is the recorded audit through **3.2.5: 29 dossiers, including 13 Arabic dossiers**, plus examination of the current stylesheet. Do not generalize these measurements into a completed audit of the later corpus. The [Audit and Migration Plan](../editorial/STUDY_AID_REFINEMENT_AUDIT_AND_MIGRATION_PLAN.md) retains the evidence and scope.

### Selective emphasis and prose rhythm

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Among ordinary Arabic main-body paragraphs, excluding aids, optional layers and revision, **55 of 68 paragraphs in the earlier six Arabic dossiers** contained inline bold; **0 of 78 in the later seven, 3.1.4–3.2.5**, did. Average paragraph lengths were similar. This identifies a loss of selective visual emphasis, not a rule that every paragraph needs bold or that later prose must be cut.

Use restrained emphasis for a meaningful technical term, contrast, condition or argumentative pivot. Include any negation or qualification needed to avoid changing the highlighted claim. Keep attribution legible. Avoid entire bold paragraphs, dense repeated labels or mechanically bolding a fixed number of words. Preserve comfortable separation between genuinely distinct paragraphs. Review multi-paragraph aid spacing as actually rendered; do not remove useful paragraph breaks to imitate a compact box. Wholesale conversion of ordinary prose into bullet points is deferred.

### Measured typography and descendant overrides

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The following recorded screen values are **baselines, not replacement targets**. Component roles differ, so equal pixel sizes or one universal line-height are not acceptance criteria.

| Sampled Arabic content | Computed font size | Computed line height |
|---|---|---|
| Ordinary prose and sampled concept paragraphs | 17.5px | 33.25px (1.9) |
| Table body cells | 16px | 25.92px (1.62) |
| Hierarchy values | 17px | 27.54px (1.62) |
| Relationship-map nodes and section objectives | 14.5px | 23.49px (1.62) |
| Timeline descriptions | 14.5px | 22.475px (1.55) |
| Source Depth item paragraphs | 14px | 23.1px (1.65) |

Inspect the font, size, line height, wrapping and spacing on the text-bearing child itself. In current CSS, the Arabic Source Depth content parent declares **18px**, while the more specific item paragraph declares **14px/1.65**. Its item heading also has a direct **14px sans font shorthand**. A correct parent declaration cannot certify readable or correctly selected Arabic descendants. These are concrete cascade issues to resolve and verify later; no replacement sizes are approved here.

Check all content-bearing text and labels affected by a future change, including timeline titles, citations, captions and relationship labels. The audit recorded an Arabic timeline title using the Latin sans stack, as well as retained letter spacing on some Arabic captions, citations and relation badges. Preserve Arabic font coverage and joining. Do not assume that a Latin label's tracking or small-cap treatment transfers appropriately to Arabic.

### RTL borders, indents and mixed-direction text

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Maintain correct `lang`, RTL direction and isolated Latin/math/date/section references. Check logical reading order as well as right alignment. Existing `border-left:none` RTL resets can erase the thin opposite outline when moving an accent border to the right. Acceptance requires the intended card outline and logical accent to remain coherent; do not solve one edge by removing another indiscriminately.

Roadmap lists currently expose double-sided indentation from physical padding combined with RTL behavior. Later correction should produce one coherent leading indent, not a cramped reading column. Inspect actual narrow and desktop wrapping. Preserve the source's sequence and hierarchy when changing alignment; direction does not change intellectual order.

### Roadmap previews and heading continuity

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Each roadmap point must contain **7–15 words in total**, including a **bold topic lead-in** followed by a short source-faithful preview of what the reader will learn. Bold selects the topic; it does not consume the entire point. Preview the actual section without inventing an additional thesis or merely duplicating its heading.

The recorded audit found 101 earlier points with bold topic lead-ins and 46 later points with no bold; all 36 later Arabic points were exact section-heading copies. Their shared wrappers did not explain the change. Correct content and emphasis together during the later migration rather than inventing a different roadmap design. No fixed number of roadmap points is selected.

### Semantic tables and the row-header cascade

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The observed table-style difference has a specific cause: some first-column entries use `<td><strong>…</strong></td>`, while others correctly use `<th scope="row">`. The shared `table.comparison th` rule styles **all** header cells as top headers, so semantic row headers inherit that font, background and border treatment. Do not remove row-header semantics to make them look like body cells. Preserve accessible headers and, when authorized, distinguish the column-header and row-header selectors using the established tokens.

Captions are an established table feature, not a new colour/header design. Preserve their semantic title role and language-appropriate alignment. Keep body text readable inside both ordinary and dark revision contexts; a light table nested in a dark block retains a compatible foreground. Count the full content of every physical cell, including all paragraphs and inline terms: normally ≤10 words, 11–20 only where accuracy requires, hard maximum 20 for all cells. A row-header tag, caption-like label inside a cell, or revision location grants no exemption.

Long exposition cannot be made compliant merely by changing the table font or splitting a sentence into arbitrary cells. A table must encode a useful comparison or mapping. Preserve necessary source explanations in their appropriate visible teaching form when a later source-guided migration restructures it. The 29-dossier audit does not establish how often long two-column exposition occurs in all later dossiers.

### Focused acceptance and preservation of source meaning

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

For a later affected-component change, inspect the relevant Arabic prose, aid, table, optional layer and revision contexts at desktop and narrow widths. Verify actual computed descendants where the cascade is at issue; use screenshots for wrapping, rhythm, borders and spacing. Check keyboard/assistive semantics when changed, and actual selected-print PDF output when print can be affected. Shared changes warrant coverage of affected components across relevant chapters, not a routine full suite after every draft.

The source's distinctions, uncertainty or certainty, attribution, sequence and essential reasoning must survive typography, emphasis, abbreviation and layout changes. An easier visual presentation is insufficient if it changes what the author claims. Essential content remains visible and in ordinary print. Use the exact scoped verification record; do not imply that old screenshots or tests verify a new implementation.

## Known debt and historical measurements

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

- `--radius-lg` and `--shadow-inset` were recorded as unused tokens. Do not remove or repurpose them in this documentation pass; verify actual use before a separately authorized change.
- The older claim that Noto Sans Arabic was unused was incorrect for the current CSS. The explicit RTL exception list uses it; remaining font-cascade and tracking issues are identified above.
- A historical print inventory recorded 23 templates for 22 chapters. It is not a current orphan-template finding; inspect the live print architecture before any cleanup.
- Semantic table headers, RTL outlines/indents, selective Arabic emphasis, descendant typography, roadmap previews and missing icons are documented migration concerns. Final colours/icons and typography choices remain pending; documentation is not implementation.

## Changelog — historical implementation record

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The entries below preserve dated implementation evidence, including old inventories, retired component vocabulary and earlier source descriptions. They do not establish current source coverage or authorize a new intellectual claim. Apply the current role/fidelity rules above when doing new work. In particular, references to six active box types, examination tips, midpoint checkpoints or embedded EL10 describe legacy implementations; source-preserving migration remains deferred.

- **CSS split off into `philosophy_notes.css`**, linked via `<link>` instead
  of an inline `<style>` block, to cut editing-session token cost.
- **JS split off into `philosophy_notes.js`** the same way.
- **Topic 3 added**: Sub-topic 3.1, dossiers 3.1.1–3.1.3, in the established
  house style (Central Thesis, six-box system, concept-rel, five-category
  exam questions), cross-referenced against the origin prompts. Fixed three
  separate stale "Four dossiers" references to Sub-topic 2.2 (actually six)
  found while doing this.
- **Sidebar navigation added**, replacing the old hand-maintained `.quicknav`
  bar and the in-flow `#toc` page. Self-builds from the live DOM (topic
  dividers + chapter kicker text) — extending the book requires no sidebar
  maintenance. `#howto` removed entirely; its one genuinely load-bearing tip
  (export via Chrome/Edge, Margins on Default) now lives as a hint in the
  sidebar's print panel instead.
- **Arabic preserved through the sidebar**: chapter/kicker Arabic spans are
  carried into the sidebar as real markup (not flattened to text), so the
  existing global `.ar`/`[lang="ar"]` rule applies there too.
- **Flat chapter numbering (#1–#22)** added, shown in the sidebar and on each
  chapter's own opening page next to its "DOSSIER x.x.x" tab — used by the
  custom-range print feature (see `PAGINATION_SYSTEM.md`).
- **Cover-page cards corrected**: Topic 3's card no longer claims "eight
  forthcoming sub-topics" (3.1 has started) and lost its dashed "not yet"
  border styling.
- **Hue sequence verified** end-to-end against the live build after a
  correctness question — confirmed continuous, no discontinuity at any
  topic boundary, full color wheel repeats every 18 chapters by design.
- **SaaS elevation pass**: radius/shadow token system introduced, applied to
  every previously-flat-cornered element. Went through two design
  iterations on how `.chapter` achieves its rounded look — see the next
  two entries.
- **Print corners, round 1**: shipped with everything (including page-level
  containers) flattened to square in print, out of caution. Also caught and
  fixed a real risk before shipping: `.chapter`'s new `overflow:hidden`
  would have clipped JS-generated print pages, since they insert as direct
  children of `.chapter` — worked around at the time with an explicit
  `overflow:visible !important` reset in print.
- **Print corners, round 2 (current)**: per feedback that flattening
  *everything* in print was overcorrecting — content islands (boxes,
  tables, cards) are supposed to show rounded corners in the exported PDF
  too, same as on screen. Redesigned `.chapter` to not need
  `overflow:hidden` at all, on screen or in print — `.chapter-banner` and
  `.end-block` round their own top/bottom corners directly instead, each
  self-clipping their own background with no overflow property anywhere.
  That removed the content-loss risk at the source rather than resetting
  around it. The print reset is now split in two: physical page-boundary
  elements (`.page`, `.chapter`, `.chapter-banner`, `.end-block`,
  `.js-print-page` — these fill an actual sheet edge-to-edge, so a rounded
  corner just exposes whatever's behind the cut) stay square; content
  islands living *within* a page's margins keep their radius in print.
- **Two print-system gaps found and fixed** while doing the above: dossiers
  3.1.1–3.1.3 were missing their `@page ch3-1-*`/`rev3-1-*` running-header
  templates entirely (silently falls back to a blank header) — added. The
  top-of-file build-instructions comment still referenced the deleted
  `.quicknav` bar and a months-stale chapter inventory — updated.
- **Topic vs. Sub-topic dividers differentiated**: Topic-level part-dividers
  keep the plain deep-navy gradient; Sub-topic dividers now work a warm
  gold undertone into the same navy base (`.part-divider[id^="s"]`), so
  the two levels are distinguishable by color, not only by kicker text.
- **Sub-topic 3.1 given its Arabic title** (الفلسفة والدين), matching every
  other sub-topic divider — it had been missing since 3.1 was first written.
- **Sidebar keyboard support added**: Escape closes and returns focus to the
  toggle button; opening moves focus into the panel; Tab/Shift+Tab are
  trapped inside the sidebar while open; every expand/collapse button
  carries a live `aria-expanded`.
- **Fixed a double close-button bug**: the sidebar toggle turned into an "✕"
  when open *and* the panel has its own dedicated close button — two
  overlapping close affordances. The toggle button now hides itself
  entirely while the panel is open instead.
- Added an explicit `html{margin:0;padding:0}` after a reported (but not
  reproduced — no conflicting rule, transformed ancestor, or duplicate
  element found in the CSS itself) gap above the sidebar in Chrome. Flag
  this again with a screenshot if it persists — it needs live reproduction
  to actually diagnose, not another guess.
- **Sub-topic 3.1 completed**: dossiers 3.1.4 and 3.1.5 written (Arabic,
  full RTL treatment), closing out the sub-topic at five dossiers. Every
  place that referenced "3.1: three dossiers" turned out to mean updating
  four separate locations, not one — the s3-1 divider, the t3 topic
  divider's sub-topic list, the cover-page card, and the colophon's total
  count — worth remembering next time a sub-topic completes.
- **The `.secnum` bidi bug turned out to be book-wide, not new-content-only**
  — a screenshot of an *established* chapter (2.2.4) showed the same "I§"
  reversal as the new ones. Root-caused and fixed centrally in the CSS
  rather than patching individual chapters (see the RTL section above for
  the full explanation of why `unicode-bidi:isolate` alone wasn't enough).
  Verified with a real bounding-box check in headless Chromium across both
  an old and a new chapter before trusting it fixed.
- **3.1.4's chapter-stamp trimmed** from 7 words to 4 after comparing tagline
  lengths across all 24 chapters found it was a genuine outlier (established
  range: 2–6 words) — this, not a hidden CSS difference, was what made its
  banner look inconsistent with other Arabic dossiers. Documented the range
  above so it's checked before writing rather than caught after.
- **Table captions redesigned**, English and Arabic both: centered instead
  of hardcoded `text-align:left` (which left Arabic captions visibly
  misaligned), with a hue-tinted background and bottom border matching the
  `th` row instead of a plain floating label — reads as a card header now,
  consistent with the rest of the elevation system.
- **Font-family, not ordering, was the real complaint** — after the bidi
  fixes above, a follow-up report ("Arabic font style keeps breaking
  everywhere") pointed at a different, bigger bug: components with their
  own explicit `font-family` outside the `.rtl` exceptions list silently
  fall back to a non-Arabic font, because a direct rule always beats an
  inherited one regardless of the `.rtl` ancestor's specificity. An
  exhaustive scan (every Arabic-text element under `.rtl`, computed
  font-family checked programmatically, not sampled) found five real
  instances — `table.comparison th`, `.memlist li b`, `.golden-quote cite`,
  `.rel-row` (meaning every `.rel-node`, i.e. every concept-relationship
  map in every Arabic chapter), and the table `<caption>` after its
  redesign. All fixed; the exhaustive-scan method is now documented above
  so the next suspected instance gets checked the same way, not sampled.
- **Sub-topic 3.2 started**: dossiers 3.2.1 (the argument from innate
  disposition / fitrah) and 3.2.2 (the moral argument) written, Arabic,
  full RTL treatment. Ran the exhaustive font-family scan and the secnum
  bidi check from the entries above against the finished chapters *before*
  shipping, not after a report — both came back clean on the first pass,
  which is the actual point of writing those checks down.
- **Dossier 3.2.3 added** (the fine-tuning argument — cosmic constants,
  Dembski's universal probability bound, Penrose's number, the four
  pillars of physical/chemical tuning), continuing the same rigor: the
  chapter arrived pre-written (from source content plus this doc's own
  Arabic-chapter conventions) already using `<bdi>` correctly around every
  inline `§` reference and the right font stack throughout — re-verified
  with the exhaustive scans rather than assumed correct because it looked
  right. Hue continues cleanly (328→348→8, wrapping past 360 as expected).
  Sandbox state was lost between sessions here (a fresh container with no
  memory of `/home/claude`); the working tree was rebuilt from the last
  shipped `outputs/` zip plus the person's own re-upload of the in-progress
  file, which is why re-verifying from scratch mattered more than usual —
  nothing about that recovery step should be assumed correct without
  re-running the checks, and it wasn't.
- **Dossiers 3.2.4 and 3.2.5 added**: the classical argument from creation
  (*kalam* — Ibn Rushd's two-tier distinction, Ibn Hazm's three-way proof
  against an uncaused/self-caused origin, the train-carriages analogy
  against infinite regress, then Big Bang redshift/CMB and the second law
  of thermodynamics as independent scientific corroboration) and an
  anatomy of New Atheism as a modern phenomenon (the five-way belief-stance
  taxonomy, the post-9/11 "militant atheism" turn and its four horsemen,
  a three-dimensional causal analysis of youth deconversion, and Pascal's
  Wager). Sub-topic 3.2 is now five dossiers deep. Both chapters were
  written directly against this document's own conventions (box vocabulary,
  `<bdi>`-wrapped section references, hue rotation) rather than adapted
  from an existing chapter, and both passed the exhaustive font/bidi scans
  and print-pagination check on the first run — the documented conventions
  did their job. One naming note for future sessions: dossier 3.2.5 and
  the still-forthcoming Sub-topic 3.3 are both titled "New Atheism" in the
  source material; they're not a duplicate — 3.2.5 is a sociological/
  psychological anatomy of the movement, while 3.3 is planned as book-by-book
  replies to specific atheist authors. Don't "fix" this apparent collision
  without checking the TOC's own sub-topic 3.3 breakdown first.
- **Sub-topic 3.2 completed**: dossiers 3.2.6 (a recall guide answering
  three objections — "no sufficient evidence," Hawking's "something from
  nothing," and the problem of evil, via a "bright vs. obscure" priority
  rule), 3.2.7 (a second, more systematic objections chapter — burden of
  proof, the argument from order dismantling "nature as the orderer," and
  the temporal/essential distinction in the argument from origination),
  and 3.2.8 (English — Karen Armstrong's *The Case for God*: mythos vs.
  logos, religion as a practiced "knack" rather than an accepted belief,
  and fundamentalism/atheism as twin, mirror-image reactions to the same
  17th-century rupture). This closes out the sub-topic at eight dossiers.
  Two things worth flagging for future sessions:
  - **3.2.8 is deliberately LTR English** inside an otherwise all-Arabic
    run of six chapters (3.2.1–3.2.6 Arabic, 3.2.7 Arabic, 3.2.8 English)
    — matching the TOC, which already listed it in English before any of
    this sub-topic was written. Verified with getComputedStyle that it
    renders `direction:ltr` and carries no stray `.rtl` class, and
    confirmed visually that the banner correctly mirrors (tabnum strip
    moves to the left edge) rather than just failing to apply the RTL
    rules. Don't assume every dossier in an Arabic-heavy sub-topic should
    be Arabic — check the TOC's own language for that entry first.
  - **A real bug this round, not just a check that passed**: the `s3-2`
    divider I'd edited across three separate turns had accumulated a
    genuine extra `</div>` (from a stale line surviving one of the earlier
    edits), caught only by the per-file div-balance script, not by eye —
    the previous edit's `str_replace` had left the file *individually*
    unbalanced while the full-book diff still looked plausible at a
    glance. Worth remembering: run the balance check on every touched
    source file individually, not just the assembled output, since a
    multi-file build can mask which fragment actually broke.
  Completing "3.2 done, 5 more sub-topics to go" touched five separate
  locations again (TOC, `s3-2` divider, `t3` divider's pd-list, the
  cover-page card, the colophon count) — same pattern flagged when 3.1
  completed; it is evidently not a one-off.


## 2026-11-04 — Sub-topic 3.4 partial integration (dossiers 3.4.3–3.4.4)

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Historical integration record.** Its counts, forthcoming labels and source summaries describe that stage, not the present corpus.

- Added `subtopic-3-4.html` with its own divider and **two completed dossiers**;
  3.4.1–3.4.2 and 3.4.5–3.4.9 remain explicitly forthcoming.
- Dossier **3.4.3** is Arabic RTL (`lang="ar"`, `.rtl`) and follows the supplied
  *جدلية الإلحاد والدين* study extract; **3.4.4** is English LTR and follows the
  supplied biochemical black-box / irreducible-complexity study extract.
- Continued the completed-chapter hue series from 3.2.8 (108°) to **128°**
  for 3.4.3 and **148°** for 3.4.4 (not a hue based on missing planned chapters).
- Both chapters contain a thesis, roadmap, section objectives, source-preserving
  substantive discussion, semantic tables/diagrams, conclusion, and a full
  six-part revision block.
- Source attribution is explicit: contested biological, historical and numeric
  claims are presented as positions in the supplied extracts, not independently
  verified scientific conclusions. Do not silently strengthen their certainty.
- Replaced the two 3.4 table-of-contents placeholders with linked rows; updated
  Topic 3 and cover prose, colophon to **34 ready dossiers / 6 started sub-topics**,
  and 3.2.8's no-longer-final next-chapter navigation.
- Added matching `@page ch3-4-*`, `@page rev3-4-*`, and selector assignments in
  the print CSS; the sidebar still auto-discovers chapters, while the JS
  paginator received a measured, chapter-scoped packing reserve to prevent
  footer collisions in these two dense new excerpts. Re-run `build.py` after further source changes.
- The exact two uploaded study extracts are archived under `source_materials/`
  for traceability; they are not loaded by `build.py` or by the browser.


## 2026-11-04 — Pedagogical reconstruction of dossiers 3.4.3 and 3.4.4

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Historical reconstruction record.** Embedded analogies and formative checkpoints below describe the legacy implementation; the current dedicated EL10 and retired-checkpoint rules supersede them.

- Benchmarked the original 32 dossiers, especially the explanatory → analogy → relationship → retrieval cycle.
- Revised only the content fragment `subtopic-3-4.html`; the 32 established chapter fragments and existing CSS/JS behavior remain untouched.
- Added explicit definitions, conceptual warning/high-yield boxes, embedded analogies, hierarchy maps, formative checkpoints, and a restored chronological/source data pathway.
- Replaced accidental ASCII-diagram/table debris with native responsive house components and reinstated the omitted scholar details and an attributed evolutionary-sequence outline.
- Rebuilt both end-blocks so memory aids are collected from explanations actually introduced in the body; returned the examination questions to all five house categories, including Conceptual.
- Preserved the two supplied study extracts under `source_materials/`; disputed scientific/history claims remain attributed to the source, not independently verified.
- Preserve all established colors, print layout tokens, chapter IDs and subtopic numbering.

## 2026-11-04 — Editorial voice: write the notes as the explanation

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Continuing language principle, within source fidelity:** direct exposition does not turn an attributed, disputed, quoted or tentative source statement into the compiler’s independent fact. Preserve necessary ownership and the source’s exact degree of certainty without repetitive distancing. The examples and implementation count below are historical.

In the main body of a dossier, use **direct explanatory prose**, not a
third-person running commentary on the supplied extract. The reader already
knows these are notes from the assigned material. Prefer “The modern synthesis
combined selection with Mendelian genetics” to “The extract explains that the
modern synthesis combined …”; likewise prefer “تُبحث آليات التطور في علم الأحياء”
to “يردّ المصدر بأن آليات التطور …”.

Keep **essential provenance** where accuracy requires it: identify named
speakers before attributed quotations, distinguish an author's particular
objection from an observed fact when that distinction matters, and retain
source labels/academic references. Do not replace sustained explanation with
repeated “according to the text” caveats. Preserve the existing teaching
components and their internal text unless specifically asked to revise them.

The 2026-11-04 direct-voice pass applied this rule only to the standalone
explanatory paragraphs of dossiers 3.4.3 and 3.4.4: **17 Arabic paragraphs and
15 English paragraphs** were rephrased. All earlier dossiers, the new chapters'
teaching tools, lists, quotations, headings and revision sections were left
unchanged; CSS and JS were not edited.

## 2026-11-05 — Accessible contents and print sidebar

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The screen-only contents drawer retains the book's gold/navy sidebar styling.
`#tocBackdrop` is a dismissible backdrop. `#tocSidebar` is a labelled modal
`role="dialog"` with focus trapping, Escape to close, focus return, and the
`inert` attribute while closed; the trigger advertises its `aria-controls`
and `aria-expanded`. Respect `prefers-reduced-motion` for the drawer and
collapsible groups. Print CSS always excludes the entire sidebar and backdrop.

The navigation builds Topic → Sub-topic → Chapter → §Section from actual
chapter headings; screen-only section `id` attributes are generated at load,
without rewriting the authored chapter fragments. The Arabic title from a
Topic divider is reproduced as a compact `<span lang="ar" dir="rtl">`, NOT
as the source's full `<h1>` (which broke sidebar line heights). Section labels
inherit the Arabic font where applicable.

Two levels of disclosure coexist: (1) topic/subtopic branches; (2) per-chapter
section links. Collapsed controls expose `aria-expanded=false`, `aria-controls`
and `inert` descendants so keyboard focus cannot enter visually hidden nodes.
Active-chapter indication from scroll NEVER auto-expands a manually closed
branch; searches expand only temporarily and restore the user's expansion
choices when cleared. Search supports chapter numbers, titles, section titles,
and Arabic diacritic-insensitive matching. Expand/Collapse All are explicit.

`src/tests/verify_sidebar.py` checks source markup, UI semantics, print hooks
and the generated reader as part of the GitHub Actions workflow. When later
authorized navigation changes affect these behaviors, select the relevant
keyboard, narrow-viewport, Arabic, link, search, print-selection and restoration
checks. This is not a requirement to run the navigation suite for every edit.

## 2026-11-05 — Screen-only reading orientation and local continuity

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

A 3px gold rail in `#readingProgressHeader` denotes physical progress through
the **entire** assembled book; the separate 34px circular gauge denotes the
active chapter's progress. They are deliberately different shapes and do not
represent exam completion. The header respects `lang=ar` / `dir=rtl` on Arabic
chapter titles, truncates long headings on narrow screens, and lives outside
all print-page surfaces. On-screen headings `h2.sec` get a 54px scroll margin
to compensate for the narrow sticky bar; `@media print` removes the bar and
the optional resume prompt completely.

Current § highlighting derives from the existing chapter scroll tracker.
Never auto-open manual TOC disclosures; keep both active chapter and section
markers legible. The resume prompt stays in the navy/parchment/gold palette
and never auto-navigates. Technical rules, privacy, and QA are documented in
`src/docs/hosting/READING_POSITION.md`.

## 2026-11-18 — Complete house-style reconstruction of 3.4.5–3.4.9

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Historical reconstruction and verification record.** The 39-chapter count and tip/checkpoint requirements below describe that implementation. Its structural sibling rule and complete revision functions remain relevant; retired component quotas must not override the current role policy in a later authorized migration. The named regression is not automatically required for unrelated documentation edits.

- Replaced five brief, structurally incomplete entries with full source-aligned English dossiers; preserved the existing 3.4.3 and 3.4.4 texts, TOC numbers, hue sequence (168° / 188° / 208° / 228° / 248°), and 39-chapter book structure.
- **Structural regression found in the earlier implementation:** `.chapter-endnav` and `.end-block` were nested inside `.chapter-body` rather than being direct siblings. Because the JS print engine selects these independently, that markup is **not equivalent** and must never be used for new dossiers.
- The six-section end-block is mandatory, not optional. Each new revision again includes the one-page rev-grid, pagination-safe definition groups, key-table recall, body-linked memory aids, and all five examination-question categories.
- Restored the full teaching vocabulary: concept/definition/high-yield/tip/mistake boxes; structured comparisons with captions; functional hierarchies; ELI10 analogies; a midpoint checkpoint; concept-relationship maps; and conclusions that follow the supplied source's own logical sequence.
- An enforceable architecture regression now lives in `src/tests/verify_3_4_house_style.py` so missing components or nested revisions cannot silently pass a future build.
- See `src/docs/editorial/RECONSTRUCTION_3_4_5_TO_3_4_9.md` for the source-bound content map and exact retained figures. No substantive opinions or counter-arguments were inserted.

### Browser-verified PDF and revision integrity

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The reconstructed dossiers were checked in actual Chromium at 390px and 1366px, including the independent dark end-block, and through the JavaScript A4 paginator. All five used the established hue and component treatments with no horizontal overflow. The targeted print test detected a separate existing selected-print issue: the print CSS hid the paginator's off-screen measurement probe during `beforeprint`, causing drastic PDF truncation. The probe is now exempt from the selected-body visibility rule while it exists. See `PAGINATION_SYSTEM.md` for the verified root cause and measurements. The new browser regression also requires the actual exported PDF to contain all six dark revision sections, not just their presence in the on-screen DOM.


## 19 November 2026 — Companion a11y state and paragraph-level Source Depth

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Supersedes the former detached Source Depth placement**, not the design system itself. Author compact native `<details class="hikam-source-depth-inline">` immediately after relevant ordinary main-body `<p>` elements, grouping multiple source references that attach to the same paragraph. Closed summary shows a subtle chapter-tinted SOURCE DEPTH label and descriptive title; expanding reveals the original source-specific discussion with page citation. The material lives in HTML `.chapter-body` but is excluded from visible word counts, CSS print and `philosophy_notes.js`'s private paginator clone **before measurement**. It is not a `.box`, hierarchy or replacement for any existing component.

The `.hikam-companion-trigger` uses the chapter `--hue` in its underline, **dotted at rest and solid on hover/open** (following the observed Literature cue). Open state must be reflected with `aria-expanded`/`aria-controls`; popup contents have a named region, a keyboard/touch dismiss control, scrollable content when pinned, a visible `:focus-visible` outline and Escape restoring focus. The inline text itself is unchanged, and generated print clones must unwrap it to plain text. Arabic/RTL inherits existing font and direction rules.

Source Depth is intentionally optional and no-JavaScript accessible. Every essential premise, qualification, reply and conclusion must remain in the visible main path and ordinary print; a possible later appendix cannot justify hiding it here. Do not index its contents as though they were ordinary visible paragraphs, or let popup anchors attach inside it. Do not introduce new visual-semantic colours or force this pattern into chapters without a source-specific reason.

## Context-first Companion, optional Source Depth and historical timeline — 18 November 2026

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

**Obsolete detached-placement pilot, retained for historical architecture evidence.** Its detached Source Depth location and pilot-only status were superseded on 19 November by paragraph-adjacent disclosures. Its references to six active box classes do not override the later role decisions. Do not copy the obsolete placement into new work.

This small addition follows the [context-first editorial pilot](../editorial/CONTEXT_FIRST_COMPANIONS_AND_SOURCE_DEPTH.md). It does **not** repurpose any of the established six semantic box classes or remove comparison tables, hierarchy diagrams, concept maps, quotations, memory aids or revision elements.

- **Contextual Companion:** the existing dotted inline trigger remains unchanged. For pilot entries with `simple`, `why_here` and `remember` fields, the same existing popup now renders labelled **In simple words**, **Why this appears here** and **Remember** lines. The final line is optional recall, not new theory. Existing plain `explanation` records render as before. English/Arabic direction and typography, keyboard, hover, tap, Escape, print-clone unwrapping and exact prose-anchor constraints remain.
- **Source Depth:** one independent and deliberately collapsed `details.hikam-source-depth` after Moran's `.chapter-body`. Nested `details.hikam-source-depth-item` records preserve individually selectable short additional-source explanations and original printed-page citations. Use semantic native disclosure/summary controls. This feature is screen-only and excluded from the regular print-composition body; its content cannot be essential to the chapter's primary argument. It is not an elevated study aid or a second set of Companions that interrupts reading.
- **Historical timeline:** use `div.historical-timeline > ol.historical-timeline-events > li.historical-timeline-event` with date and description for a genuinely chronological progression, as piloted by Moran's four periods. The connecting line and ordered list encode chronological sequence. Do not turn a thematic comparison into a timeline. Chapter hue is structural only; no new semantic colours.
- **Conceptual thread:** within the existing `.concept-rel` component, make the chapter's primary question, continuing ideas, changing methods and conclusion readable before additional named positions appear.
- **Responsive and print:** timeline elements wrap on small screens and remain within the page; the optional Source Depth is omitted from the JS paginator by its location outside `.chapter-body` and defensively hidden by print CSS. Never change the print engine merely for this pilot.

The pilot is intentionally limited to 1.1.1. Further adoption requires source-coverage and reader-comprehension review, not copying boxes to every dossier.
