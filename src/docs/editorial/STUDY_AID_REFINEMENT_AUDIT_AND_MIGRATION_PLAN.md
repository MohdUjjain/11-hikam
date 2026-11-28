# Study Aid Refinement Audit and Migration Plan

**Recorded:** 28 November 2026

**Decision follow-up, 28 November 2026:** explanatory support is incorporated into the expanded memory-aid role (maximum 30 words); no separate general-purpose callout is introduced. Essential/useful/supplementary is a preparation framework without additional visual markers. Colour/icon design, exact Arabic typography and the ordinary-prose bullet/highlighting pass remain deferred. The user has authorized a focused 3.2.5 implementation pass. The measurements below remain the frozen baseline, not measurements of that later revision.

**Policy:** [Study Aid Roles and Reading Design Protocol](STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md).

**Evidence baseline:** repository commit [`7798593e40ceafb9ff9590e1c1fea149347e5fdd`](https://github.com/MohdUjjain/11-hikam/tree/7798593e40ceafb9ff9590e1c1fea149347e5fdd). Measurements describe that edition, not a completed migration to the new rules. The source-page survey covers the broader programme; the detailed main-aid census covers 29 dossiers through 3.2.5. The accompanying [baseline data](data/study_aid_baseline_2026_11_28.json) preserves compact measurements and the 62 source allocations without uploading the original reading files.

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.** Every migration decision must preserve source meaning, attribution, reasoning and certainty. This audit evaluates the notes' classification, length, coverage and presentation; it does not adjudicate the authors' philosophical positions.

## 1 Evidence scope and interpretation

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The completed study-aid audit covers 29 dossiers, 16 English and 13 Arabic, from 1.1.1 through 3.2.5. Its internal division is 20 dossiers through 3.1.1 and nine from 3.1.2 through 3.2.5. The source-length survey separately covers 62 existing dossiers across the wider book. Policy applies throughout the whole corpus; a measured result from the 29-dossier subset must not be presented as a result for all 62.

The user locates the later two-column paragraph-table problem from 3.2.6 onward. A representative 3.2.6 table confirms that form, but no prevalence figure for the remaining corpus is established by the earlier census. Likewise, a documentation update does not establish that all current aids meet the new limits.

The supplied discussion records contain successive policy versions. The later user decisions control: definition 20 words per entry/two entries/40 per box; exactly one opening central concept; memory 30; table normal 10/hard 20; roadmap 7–15. Older sensitivity tables and the historical 30-word definition rule are evidence of the decision process, not current instructions.

Body counts exclude titles, category labels, decorative icons and separately presented quotation attribution, while retaining meaningful inline terms. English and Arabic use the same whitespace-based convention. A table counts once as an aid, and a physical merged cell counts once as a cell. Ordinary body lists are not automatically classified as study aids. Source Depth, Companions, frontmatter and revision have separate inventories.

## 2 The measured component inventory

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The old implementation contains 500 main teaching aids and 191 orientation components. These are implementation counts under the old labels, not a prescription to retain all old types or quantities.

| Legacy family | Main instances | Paragraph-form instances |
| --- | ---: | ---: |
| Central concept | 34 | 33 |
| Definition | 45 | 44 |
| High-yield | 46 | 43 |
| Common mistake | 36 | 36 |
| Examination tip | 25 | 25 |
| Memory | 21 | 21 |
| Source quotation | 36 | 36 |
| Analogy / simple explanation | 25 | 25 |
| Checkpoint | 50 | 14 |
| Comparison table | 102 | 0 |
| Hierarchy / logical structure | 40 | 0 |
| Concept relationship map | 36 | 0 |
| Historical timeline | 4 | 0 |
| **Main teaching aids** | **500** | **277** |

There are also 162 section objectives and 29 roadmaps, bringing the visible teaching/orientation inventory to 691. The six revision formats remain a separate layer, with 174 revision sections in these 29 dossiers. The old total of 15 reading/orientation families described the pre-migration taxonomy; it must not revive retired tips or checkpoints, or the former undifferentiated analogy role.

The 277 paragraph-form aids are 55.4% of main aids and contain 283 paragraphs: 271 have one paragraph and six have two. Their bodies total 11,437 words, average 41.3 and median 39, with a range of 4–124. Excluding quotations, the 241 bodies average 45.4 words and range from 16–124. The longest individual paragraph is 91 words. These are different measurements: multiple paragraphs can still constitute one oversized aid.

Of 207 semantic boxes, 202 are paragraph-form. The 84.1% below 60 words statistic does not demonstrate compliance with maxima of 20, 30, 35 or 40. Paragraph form alone also does not establish a defect: several boxes contain genuine chains, inline numbering, distinctions or formula explanations.

## 3 Functional misclassification and additional central concepts

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The definition family contains direct glossary entries, mixed entries and seven clear instances whose principal operation is not definition. Examples include the 68-word disagreement objection in 1.1.2, the 44-word deconstruction procedure in 1.1.4, and the 91-word historical comparison in 3.1.3. Their existing labels cannot be used as proof of their function. See the frozen [disagreement](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-1-1.html#L394), [procedure](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-1-1.html#L1017), and [historical comparison](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-1.html#L442).

A new definition audit must identify each term-and-meaning entry, then check its 20-word/two-sentence maximum and the two-entry/40-word box maximum. The old statement that 42 of 45 boxes exceed 30 words cannot be reused as a compliance result for this new policy. Mixed historical or explanatory content must be preserved in its proper location rather than truncated under a definition heading.

The five additional central-concept boxes requiring reassignment are:

| Dossier | Existing label | Words | Actual operation to review |
| --- | --- | ---: | --- |
| 1.1.3 | Two Proposed Asymmetries | 52 | Comparison of two proposed asymmetries |
| 2.2.1 | المحصلة — تاريخ الميتافيزيقا ومجالها | 74 | Concluding synthesis |
| 3.1.2 | What counts as evidence for or against monotheism? | 68 | Evidence inventory |
| 3.1.3 | What can warrant assent? | 86 | Position and related questions |
| 3.2.5 | أربع قواعد لترتيب الشواهد | 50 | Four-rule list |

Four of these five already fit the 40–75 range, demonstrating that a length check does not establish role compliance. The new requirement is one central-concept box at the opening of each dossier; the other source material remains to be reassigned.

The high-yield family also needs functional review: a 30-word retrieval chain in 1.1.2 belongs to memory by operation; three later boxes describe source scope; three guided exercises in 3.2.1–3.2.3 have 124, 64 and 116 words; the seven-cause list in 3.2.5 has 111 words of substantive exposition. Removing only `.checkpoint` would leave an assessment function hidden under high-yield styling. Preserve unique source teaching, and move appropriate practice to the independent revision system.

## 4 Memory baseline and the adopted maximum

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The 21 formal memory aids contain 686 body words, ranging from 23–50, with an average of 32.7 and median 35. Thirteen exceed the now-adopted 30-word maximum. The earlier alternatives of 35 or 40 words are no longer active options merely because they occur in a sensitivity table.

The current operations are six ordered chains, five keyword groups, seven paired mappings, two numerical anchors and one hybrid. No existing acronym or rhyme was found in that inventory. This describes the frozen implementation and does not restrict the expanded repertoire in the canonical protocol. The later user decision also admits compact source-grounded explanatory anchors within the memory family; it does not add a new component class or alter the 30-word maximum.

| Dossier or entry | Words | Existing operation |
| --- | ---: | --- |
| 2.1.1 | 35 | Four-stage inquiry chain |
| 2.1.2 | 50 | Recognition, cooperation, comparison and evaluation |
| 2.1.3 | 36 | Eleven stages of the source's inquiry |
| 2.1.4 | 28 | Five democracy questions |
| 2.1.5 | 37 | Five distinctions |
| 2.1.7 | 27 | Demands, outputs and feedback |
| 2.2.1 | 24 | Shelf placement and subject distinction |
| 2.2.2 | 24 | Four topics |
| 2.2.3 | 27 | Cause sequence |
| 2.2.4 | 35 | Contrasts and book groupings |
| 2.2.5 | 37 | Book groupings and outsiders |
| 3.1.3 | 42 | Three thinkers paired with questions |
| 3.1.4 first | 36 | Three fears |
| 3.1.4 second | 23 | Use, consolation and origin |
| 3.1.5 | 23 | Glosses and a boundary against generalization |
| 3.2.1 | 25 | Six argument cues |
| 3.2.2 | 32 | Two proof structures |
| 3.2.3 first | 43 | Three probability anchors |
| 3.2.3 second | 36 | Six conditions grouped for retrieval |
| 3.2.4 first | 35 | Attributes paired with their source relations |
| 3.2.4 second | 31 | Numbers paired with evidence |

The 2.1.2 heading names three stages while its body contains four, including Compare; correct the mismatch against the source. Four analogy headings also use memory terminology, while one high-yield box operates as memory. Searches by the word memory and counts by `.box.memory` therefore answer different questions.

No exact whole-body duplicates were found, but conceptual overlap remains. For each migrated cue, establish the additional retrieval operation, preserve source items and order, and check the complete cue plus key within 30 words. Reclassification must not disguise a newly added analogy as memory.

## 5 Analogy provenance and corrections

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

| Finding among 25 legacy analogy containers | Count |
| --- | ---: |
| Traceable to supplied source material | 17 |
| Positively identified as compiler-added | 1 |
| Origin not established by the audit evidence | 7 |

Sixteen of the 17 source-derived passages contain examples, comparisons, metaphors, thought experiments or illustrations; one is a direct conceptual restatement. Twenty-three containers exceed 30 words, but this does not establish 23 EL10 violations. First establish provenance and actual function, then apply the appropriate rule.

The compiler-added [car mechanism/destination analogy in 1.1.5](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-1-1.html#L1214) is 43 words and needs a source-faithful 20–30-word treatment. The yellow-object illustration in 1.1.2, labelled EL10, was traced to Stout's discussion of Moore on printed page 854. The heart/body comparison discussed through Bradley also needs ownership clarified rather than being treated as a compiler invention.

The contracts/promises explanation in 2.1.6 and the direct contrast of questions in 2.2.2 require function-based reclassification. Source provenance does not turn a non-analogy into an unlimited analogy box. The seven unresolved items remain unresolved until the corresponding original passages are checked; do not infer their origin from a legacy label.

## 6 Table measurements and the visual discrepancy

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

There are 102 main tables: 20 with two columns, 80 with three and two with four. They contain 1,333 physical cells, including one intentionally empty corner header and no empty body cells.

| Population | Cells | Minimum | Maximum | Mean | Median |
| --- | ---: | ---: | ---: | ---: | ---: |
| All main-table cells | 1,333 | 0 | 34 | 5.27 | 4 |
| Header-row cells | 288 | 0 | 7 | 2.51 | 2 |
| Body cells including row headings | 1,045 | 1 | 34 | 6.04 | 5 |

Among body cells, 912 have 1–10 words, 119 have 11–20 and 14 exceed 20. Four exceed 30. Under the new policy, the 14 require correction; the 119 require review against the normal ten-word target. A short cell still needs an accurate, useful meaning.

The body-cell 95th percentile is 13 words: 993 of 1,045 cells are at or below 13, and 52 are longer. This is a description of the distribution, not a permitted maximum. Revision is counted separately: 19 actual tables, 265 cells and a longest cell of 17 words. Both layers are governed by the new per-cell rule when migrated.

Through 3.1.1, the 79 main tables include 19 two-column tables and average 5.72 body words per cell. The 23 tables from 3.1.2–3.2.5 include only one two-column table and average 7.18 body words. This supports a limited finding about the audited subset, not a denial of the user's later 3.2.6 observation.

The shared wrapper and CSS remain in use. In [3.1.1](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-1.html#L67), first-column labels are ordinary `<td>` with bold text. In [3.1.3](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-1.html#L445), semantic `<th scope="row">` cells activate the broad `table.comparison th` rule: chapter tint, 12.5px sans text and a stronger bottom border. The [CSS](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/philosophy_notes.css#L400) does not distinguish their visual role from top column headers.

Caption usage also varies: captions absent in the inspected 3.1.1 tables reappear in 3.1.2, although captions existed in earlier chapters. Chapter hue variation is an established token input. In the inspected chapters, no separate table stylesheet or table-level inline override explains the change. Preserve semantic row headers while standardizing their intended presentation in the design pass.

The first [3.2.6 table](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-2.html#L418) pairs short labels with extended explanatory cells under the same shared component. Its content organization and the earlier header/caption presentation are separate migration issues.

## 7 Hierarchies and concept maps

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The 40 hierarchy components contain 159 nodes. Functional review identified two clear parent-child groupings, 20 ordered progressions, 13 sets of parallel distinctions and five mixed structures. These categories describe operations, not quality scores. Existing indentation is insufficient evidence for decimal nesting: for example, increasingly indented premises in 3.2.1 must not automatically become successive children.

Apply the accepted treatment: decimal numbering for actual parentage, ordinary numbers for argument stages, equal levels for parallel concepts, and explicit role identification before numbering a mixed structure. A return to the parent level must return to that numbering level. Preserve source-established dependencies rather than manufacturing them from layout.

The 36 maps contain 210 concept nodes and 105 relationship labels. Nodes range from 1–9 words, averaging 3.93; relation labels range from 1–4, averaging 1.65. The nodes have not generally become paragraphs.

Two maps contain substantial attached prose: [3.1.5](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-1.html#L677) has 39 explanatory words within a 47-word map body; [3.2.5](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/chapters/subtopic-3-2.html#L347) has 20 within 38. Review their placement while preserving the explanation. Blanket compression of all nodes is not supported by this evidence.

## 8 Roadmaps and orientation

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The audit covers all 29 roadmaps and 147 points. All 101 points through 3.1.1 contain a bold lead-in; none of the 46 points from 3.1.2–3.2.5 does. The shared card/list CSS remains, so the emphasis break is in the authored HTML beginning with 3.1.2.

| Population | Points | Words per point | Mean |
| --- | ---: | --- | ---: |
| Through 3.1.1 | 101 | 7–17 | 11.40 |
| 3.1.2–3.2.5 | 46 | 2–13 | 6.04 |
| Earlier Arabic | 28 | 7–15 | 10.43 |
| Later Arabic | 36 | 2–8 | 4.86 |

All 36 points in the seven later Arabic roadmaps reproduce section headings verbatim. Later English roadmaps retain complete questions or thematic previews. No clear instance of a roadmap promising a topic absent from its chapter was identified; grouping several sections under one point can be legitimate.

The new requirement is a bold topic lead-in plus a faithful preview, **7–15 words for the whole point**. This also means the earlier 16- or 17-word points are not automatically compliant simply because they are in the reference group. Restore the learning function and the current limit across the authorized scope, without inventing new topics or adding generic padding.

## 9 Current palette icons and Arabic presentation

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The baseline uses eight distinct family background fills. Definitions are blue, central concepts green, mistakes red, memory and analogy share purple, high-yield and checkpoint share gold, and examination tips use amber. Quotations and structural cards share the light card surface, while objectives use darker parchment. Structural accents derive from chapter hue; fixed semantic box colours serve a different purpose.

Every semantic box has label text, but only 194 of 207 have icons. The 13 missing icons occur in 3.2.1–3.2.5. Existing icon conventions also vary within families. Standardizing them and separating memory from added EL10 are accepted design objectives; the exact final palette and icon choices remain open. Removing tips does not automatically make their amber token unused, because relationship-map example badges also use that colour.

Observed RTL issues include roadmap padding on both sides, a border reset removing the left outline of some cards, timeline typography differing from ordinary Arabic body treatment, and letter spacing retained in some Arabic captions, citations and relationship labels. These are specific component issues, not all consequences of the post-3.1.1 roadmap change.

The later ordinary Arabic prose also loses selective emphasis:

| Direct main-prose paragraphs only | Six earlier Arabic dossiers through the 3.1.1 boundary | Seven later Arabic dossiers from 3.1.4–3.2.5 |
| --- | ---: | ---: |
| Paragraphs | 68 | 78 |
| With bold anchors | 55 | 0 |
| Mean words | 65.65 | 66.47 |

This excludes aids, optional panels and revision. Headings and component labels still contain bold text. Average paragraph length is almost unchanged; the finding supports restoring meaningful internal emphasis without implying a general increase in prose length.

Representative live screen measurements were:

| Arabic element | Font size | Line height |
| --- | ---: | ---: |
| Main prose and concept-box paragraph | 17.5px | 33.25px |
| Table data cell | 16px | 25.92px |
| Hierarchy value | 17px | 27.54px |
| Objective or map node | 14.5px | 23.49px |
| Timeline description | 14.5px | 22.475px |
| Source Depth paragraph | 14px | 23.1px |

The expanded 3.2.5 Source Depth panel confirmed that its actual paragraph uses 14px despite the Arabic parent setting of 18px; the more specific child rule controls it. See the [Source Depth rules](https://github.com/MohdUjjain/11-hikam/blob/7798593e40ceafb9ff9590e1c1fea149347e5fdd/src/philosophy_notes.css#L2871). Ordinary paragraphs have a 15px bottom margin. The inspected two-paragraph high-yield aids do have a 15px paragraph gap; do not report zero separation.

These values are measurements, not new typography settings. Inspect actual child styles, line spacing, thought-unit separation, selective emphasis and RTL geometry together when that work is authorized. The user has deferred the exact Arabic typography decision and specified the smallest meaningful change as the aim. Short labels do not automatically require the leading of long prose. The ordinary-prose pass, including sentence bullets and improved highlighting, remains deferred.

## 10 Source lengths and the provisional drafting calibration

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The survey counted 78 assigned PDF files; their leaf counts matched the inclusive ranges in the supplied division sheet. The PDF page unit provides stable assigned pagination, while DOCX/native originals remain preferred for content. Covers or reference leaves in an excerpt remain part of its physical length; pages are a rough proxy for conceptual demand.

| Scope | Units | Minimum pages | Maximum pages |
| --- | ---: | ---: | ---: |
| All assigned PDFs including supplementary items | 78 files | 1 | 172 |
| Detailed-pass dossiers through 3.2.5 | 29 dossiers | 6 | 42 |
| Existing main corpus | 62 dossiers | 6 | 74 |
| Planned main programme including two forthcoming readings | 64 dossiers | 2 | 74 |

The 62-dossier allocation uses 64 assigned excerpts and **excludes all 11 مطالعة مزيدة PDFs**, together 754 pages, as well as the 18-page books index. It excludes the separate forthcoming 3.4.1 four-page and 3.8.1 two-page readings. Dossier 2.2.3 combines 6 + 1 = 7 pages; the combined 3.8.3/3.8.4 dossier combines 12 + 5 = 17. Corresponding Word versions are not added again.

| Existing source-page band | Dossiers | Share |
| --- | ---: | ---: |
| 1–10 | 10 | 16.1% |
| 11–20 | 18 | 29.0% |
| 21–30 | 21 | 33.9% |
| 31–40 | 7 | 11.3% |
| 41–50 | 2 | 3.2% |
| 51–60 | 2 | 3.2% |
| 61–70 | 1 | 1.6% |
| 71–80 | 1 | 1.6% |

The source allocations for the 62 dossiers total 1,466 pages; mean 23.65, median 21 and mode 26. With linear-interpolated quantiles, Q1 is 14, Q3 is 28.75, P10 is 8.1 and P90 is 37.7. The middle half is therefore approximately 14–29 pages. Thirty-nine dossiers use 11–30 pages and 56 use 38 or fewer. Six is not an isolated lower outlier: it occurs twice and four readings have seven pages. Under the 1.5-IQR convention, the upper outliers are 58, 58, 65 and 74.

The historical raw 1–172 and planned 2–74 min–max allocations were experiments, not adopted per-dossier rules. The later proposal uses the typical distribution rather than allowing a few long readings to stretch the scale:

`illustrative target = round(40 + 35 × clamp((P − 8.1) / (37.7 − 8.1), 0, 1))`

This gives approximately 40 words at eight pages or fewer, 47 at 14 pages, 55 at 21, 65 at 29 and 75 at 38 pages or more. **The formula remains provisional.** The user accepted soft targets within the permitted 40–75 range, not a new hard limit for each chapter. Source complexity and accurate expression govern the final wording. Do not require every long reading to fill 75 words or every short reading to stop at its estimate.

For the requested 3.2.5 pass, the frozen allocation is **29 assigned source pages**, giving approximately **65 words** under this illustration. That is a reminder of the proposal, not an adopted 65-word requirement. The user's follow-up asks what was discussed and leaves the formula provisional; the binding central-concept rule remains one opening box within **40–75 words**.

## 11 Overall density and the limits of the earlier projection

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The corrected baseline main-aid-plus-objective pool is 28,487 full-visible words or 25,894 body words. Frontmatter, roadmaps, Companions, Source Depth and revision are excluded. A prior extraction joined words at table boundaries; correcting 86 table bodies added 143 words. This did not change paragraph counts or the recorded paragraph-family cap findings.

The earlier mechanical scenario removed 25 tips and 50 checkpoints and subtracted excess above the then-selected four family maxima, including the superseded 30-word definition maximum. It projected 23,724 full-visible words, or 818.07 per dossier, from 982.31; the number below 850 rose from three to 18. Body words projected to 21,456.

**That is not a forecast of the latest policy's result.** It did not include the adopted memory cap, new individual-definition rules, table and roadmap rules, provenance-dependent EL10 treatment, source-preserving reclassification or newly justified aids. Do not present its 4,763-word reduction as the amount to remove now or a quota to replace.

The useful implication remains: a coordinated migration must review missing learning operations and overall teaching distribution, not just shorten individual boxes. Removing 75 legacy containers leaves 425 before reclassification and additions; the final number of useful aids cannot be inferred from that subtraction. Preserve the source-proportionate programme guidance without filler or lost substantive material.

## 12 Optional layers and revision baseline

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The detailed scope contains 312 Companion records: 301 use the contextual three-part display and 11 use one explanation paragraph, in 3.1.4 and 3.1.5. Displayed popup text ranges from 22–62 words and averages 39.8. A single direct explanation is allowed by the context-first policy; lack of three fields alone is not proof of inadequate teaching. Review whether each record resolves its actual local difficulty.

There are 198 Source Depth disclosure groups with 275 source records. Their aggregate body-word measurements are excluded from the visible programme totals and have no overall quota; actual bounded definitions, memory devices and table cells within them retain their unit limits. No essential argument unit may exist only there.

All 29 dossiers have six revision headings. Nineteen Key Table sections contain actual tables; ten, from 2.1.6 through 3.1.1, contain return notes to existing structures. The revision function must be checked, rather than claiming that 29 headings prove 29 actual tables. Keep precise usable references where a return note is retained. No blanket decision to reproduce every table has been made.

Possible Examination Questions remain, with Short Answer, Long Answer, Comparison, Conceptual and Application categories. Removing main-body assessment does not remove this separate revision practice. Definition-entry, memory-device and table-cell limits apply to those bounded units, not to a whole revision section's total text.

## 13 Critical evaluation and reconciled contradictions

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The documentation review distinguishes intellectual fidelity, learning function, implementation evidence and permission. These are the material contradictions and their resolution:

| Earlier wording or risk | Reconciled instruction |
| --- | --- |
| Preserve every NotebookLM sentence | Preserve substantive source teaching; the original reading remains authoritative |
| Exactly 75 words for central concept | One opening concept, 40–75 words, with only soft source-length targets |
| Definition box at most 30 words | Each definition at most 20 words/two sentences; at most two per box and 40 total |
| Memory cap undecided | Maximum 30 words for each complete memory aid |
| Separate general-purpose explanatory callout left open | Compact source-grounded explanation belongs within the expanded memory role; no new family |
| Priority framework requires another visual treatment | Essential/useful/supplementary guides preparation and placement; no extra visual marker |
| EL10 inside memory or any suitable component | Dedicated compiler-added analogy role only, 20–30 words |
| Every source-derived explanation is an analogy | Establish provenance and actual function separately |
| Keep every established aid type | Retain approved functions; retire main-body tips/checkpoints and preserve unique source substance |
| High-yield means exam-likely | An important source-grounded point; no prediction of examination frequency |
| All new Companions must add new facts | A simpler local restatement can resolve a real difficulty |
| Essential material may be hidden if a future print appendix is planned | The current main reading and ordinary print must contain the essential account |
| A second paragraph creates a second allowance | Count the complete bounded unit across all subparts |
| Short cells or a green count prove good aids | Review source meaning and learning operation independently of length |
| Decimal numbers copied from CSS indentation | Establish conceptual parentage first |
| Every roadmap point can repeat a heading | Bold topic plus a faithful 7–15-word preview |
| A shared CSS file guarantees uniform appearance | Check actual markup, selector application, captions and RTL child styles |
| Six revision headings prove six fulfilled functions | Inspect their actual content and relationship to the taught material |
| Full suite mandatory for every candidate | Use checks proportionate to the change and any required gate |
| Old pilot counts define today's whole corpus | Treat dated counts and validation runs as historical evidence |
| Documentation adoption equals reader migration | Report policy, implementation, verification, merge and publication separately |

The source-prohibition sentence appears prominently throughout the active instruction documents by explicit user request. It must not be weakened into a general request for neutrality or balance. Permitted mnemonics and EL10 devices can organize or clarify source-established content; they cannot carry independent judgments.

The later user decision resolves the general-purpose-callout question through the expanded memory family and resolves priority presentation by requiring no additional visual system. Colour/icon treatment, exact Arabic typography and the ordinary-prose bullet/highlighting pass remain deferred. The specific page-target formula remains provisional. Preserve these distinct decision states rather than leaving settled questions open or treating deferred choices as adopted.

## 14 Implementation sequence and completion evidence

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The original consolidation was documentation only. The later 28 November user request authorizes a focused pass on 3.2.5. Use the following sequence within each agreed implementation scope; do not treat that one-dossier authorization as a whole-corpus migration:

1. Confirm the current source and repository revision, the requested dossiers and the source materials. Prefer editable originals where supplied. Preserve any required pre-edit archive before replacing an unrevised dossier.
2. Establish source-unit coverage, actual aid functions and provenance. Identify the definitions within mixed boxes and the analogies whose origin remains unresolved.
3. Reclassify extra concepts and non-definitions, retire main-body tips/checkpoints by function, and preserve each necessary source unit in a suitable visible place.
4. Apply the settled individual limits. Record 11–20-word table cells whose accurate expression requires exceeding the normal target. Preserve quotations and complex source explanations through appropriate placement rather than misleading truncation.
5. Restore roadmap previews and emphasis, correct real hierarchy relations, and review the two maps with attached prose. Do not impose arbitrary uniform node limits or a fixed table column count.
6. Review missing learning operations and the overall aid distribution. Add only aids with a distinct source-grounded purpose.
7. Align the six revision functions, optional layers and exact source references. Confirm essential material survives with popups and disclosures closed and in ordinary print.
8. Implement only the authorized presentation decisions. Use existing tokens, preserve RTL and accessibility, and keep pending palette or pixel choices distinct from adopted policy.
9. Update affected tests that encode superseded roles, preserving unrelated source, archive and reader contracts. Run targeted checks corresponding to changed content or behavior, not the full suite automatically.
10. Review the exact diff, verify the applicable fork/upstream transfer and report what was actually saved, merged or published. Do not claim a reader deployment from a documentation commit alone.

Maintain an item record with dossier, component/location, actual role, source page, old count, applicable limit, required action, destination, final count, semantic review and verification result. For definitions add entry count and sentences per entry; for analogies add provenance; for tables identify physical row/column and merged cells; for roadmaps count the lead-in with the preview. This record makes the correction reviewable without turning counts into substitutes for source reading.

The separate future prose task may split long paragraphs at their actual sentence boundaries into explanatory complete-sentence bullets and improve highlighting. It remains deferred; do not introduce it as an incidental study-aid correction.

## 15 Documentation validation and status boundaries

> **This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

For the documentation portion of an update, check that all active entrypoints reach the canonical policy, local links and anchors resolve, the latest decisions agree across the language/concise/context/design guidance, and superseded instructions are removed from active directions. A documentation-only change contains no reader implementation; a separately authorized chapter migration must have its own scope and verification evidence. The baseline data should reproduce the stated totals and distribution without containing full original reading texts or private language samples.

The GitHub workflows remain separate technical configuration. Selecting targeted documentation checks does not silently change their triggers, bypass branch protections or turn a skipped job into a passed job. The [release guide](../hosting/SECONDARY_FORK_CI_AND_RELEASE.md) distinguishes documentation publication from a built reader release and preserves the fork's verification role where applicable.

Historical source audits, immutable chapter snapshots and prior successful CI runs remain evidence of their own revisions. They are not rewritten to pretend that retired components were never present. Future migration records should state exactly which dossiers and units meet the new policy, with the checked revision and remaining unresolved items.
