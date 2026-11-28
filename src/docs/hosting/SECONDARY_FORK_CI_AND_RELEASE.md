# Secondary-account fork: scoped verification and safe return to Hikam

**Current operating policy — 28 November 2026.** This guide distinguishes documentation-only work from reader changes and replaces the earlier unconditional full-suite and first-pilot setup instructions. Historical verification remains recorded below; it is not a gate to repeat for every chapter.

## Authority and scope

Follow the **[Study-Aid Roles and Reading Design Protocol](../editorial/STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md)** and the **[editorial reading order](../editorial/README.md)** for content authority. The new editorial policy applies to all 62 published dossiers; the [frozen audit and migration plan](../editorial/STUDY_AID_REFINEMENT_AUDIT_AND_MIGRATION_PLAN.md) distinguishes the 29 audited dossiers through 3.2.5 from the remaining review scope. Verification establishes the actual changed behavior; it does not authorize additional editorial, reader or design work.

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The current documentation pass leaves chapters, CSS, JavaScript, generated reader assets and workflow configuration unchanged. Future reader implementation follows its authorized scope and the appropriate checks below. Existing authorization for a release remains effective; this document does not introduce a new confirmation requirement.

## Repositories and publication authority

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

- **Authoritative source and public reader:** [`MohdUjjain/11-hikam`](https://github.com/MohdUjjain/11-hikam), with [GitHub Pages](https://mohdujjain.github.io/11-hikam/) served from upstream `main`.
- **Established secondary-account testing fork:** [`Mohd-Ujjain/11-hikam`](https://github.com/Mohd-Ujjain/11-hikam). Record checks as fork checks when they execute there. A workflow targeting upstream is not a fork run merely because the other account initiated it.
- **Fork-only verification configuration:** temporary targeted workflows belong to the testing fork and must not be copied into the canonical project as part of an editorial transfer.

The fork already exists and has successful historical runs. The former PR #12 setup instructions are historical, not an outstanding setup or approval gate. The upstream reader remains the publication destination; a fork test result alone does not establish a Pages deployment.

## Select checks for the actual change

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

Do not run the complete whole-book suite routinely for every chapter or documentation edit. Select meaningful checks for the changed files and affected behavior; broaden them only for a concrete unresolved risk or an actual required gate.

| Change | Verification scope |
| --- | --- |
| Documentation only | Review the exact diff and authorized file list; verify Markdown paths/anchors, policy precedence, numerical/status claims and whitespace. Confirm reader source, generated assets and workflow files are unchanged. No reader build, browser, print, offline or full-suite run is required. |
| One dossier and its teaching records | Verify the original-source coverage, predecessor/archive integrity, current component contracts, word-count boundaries, exact Companion anchors and isolation of unrelated chapters/records. Rebuild canonically and check reproducibility. Use bounded desktop/mobile, RTL/keyboard/no-JS and actual selected-chapter A4 evidence where the rendered change requires them. |
| A shared reader, design, navigation, print or offline behavior | Exercise the affected shared contract and representative uses. Expand only as the demonstrated scope requires; preserve unrelated source content and established A4 page geometry and pagination boundaries. A shared change must itself be within the authorized task. |

Existing tests are evidence tools, not independent editorial authority. When a later authorized implementation retires or reclassifies a component, reconcile only the affected legacy test contract with the current policy; retain source, accessibility, isolation and print verification. Do not alter a valid assertion solely to obtain a green result.

## Run targeted fork verification when needed

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

1. Identify the authoritative upstream base and the exact candidate SHA. Use a fresh candidate branch in the testing fork; compare the complete intended diff with that base.
2. For reader-source changes, run `python src/build.py` and `python src/build.py --check`. The canonical source and `index.html`, `src/philosophy_study_notes.html`, and `service-worker.js` must describe one edition. Documentation-only changes leave all three generated files untouched.
3. Run the selected source and behavior checks in one bounded workflow. Pin the runtime dependencies required by those checks. Arabic browser/PDF evidence must use the intended fonts when typography or glyph coverage is being verified; fallback-only output does not establish that result.
4. Inspect the relevant screenshots, actual PDF pages and diagnostic artifacts before accepting a rendered change. Record failures and exact corrections; do not speculate about CSS or pagination causes.
5. Record the successful run URL, tested SHA, command scope and any unavailable or unrun checks accurately. Store only relevant generated artifacts, logs and screenshots/PDFs with short retention. Private source files, writing samples, credentials and tokens do not belong in repository uploads or test artifacts.
6. Stop optional verification once the necessary checks establish the candidate. If a correction changes the candidate, rerun the affected checks against the corrected edition; do not claim that an earlier SHA verifies later files.

## Return verified work and publish

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

For a **reader-source release**, transfer the intended canonical source and all three matching generated outputs together. Compare the transferred Git blobs with the exact verified candidate. Review the upstream diff for unrelated chapter changes, generated mismatches, private source uploads and accidental fork-workflow transfer. Check the final edition's reproducibility where execution is available. Merge and publish within the user's existing authorization, respecting repository protection rules, and separately confirm the upstream merge and Pages result before claiming publication.

For a **documentation-only release**, transfer only the reviewed documentation files. Record the local documentation checks and exact candidate/base; do not rebuild or transfer reader assets merely to publish instructions. When using the standard `[skip ci]` commit marker for this documentation-only path, it must be present on the commit triggering the push or on the pull request HEAD. A later merge commit triggering the upstream `main` push needs its own marker; an earlier marked commit does not suppress future runs. Verify the resulting workflow/check state and describe skipped checks as skipped, never passed. Required skipped checks can remain pending and block a merge; respect and report that protection rather than bypassing it. See GitHub's [workflow-skipping documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs).

A merge, check or deployment is successful only when its actual outcome has been verified. Documentation publication does not mean that the reader has already implemented the new aid policy.

## Existing automation and quota discipline

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

The existing [`.github/workflows/verify-pages.yml`](../../../.github/workflows/verify-pages.yml) responds to upstream pull requests and pushes to `main`, and contains broad structural and browser jobs without documentation path filters. **This documentation update does not change that configuration.** Scoped manual verification does not, by itself, stop automatic runs or prove that they did not start. Inspect and report the actual state for the release path used.

Use one consolidated targeted workflow per candidate revision when fork execution is needed; avoid duplicate full suites on both push and pull request. Keep test-job permissions at `contents: read` unless an actual task requires a narrowly scoped write operation. Do not repeat quota-blocked jobs without a reason the new attempt can succeed. Preserve the original publication authority and keep private source material outside repository and artifact uploads.

## Historical first pilot — verified result, 18 November 2026

- Source branch on fork: `editorial/contextual-companions-source-depth-moran`, associated with the original [pilot PR #12](https://github.com/MohdUjjain/11-hikam/pull/12).
- Complete secondary-account build, source checks, full Chromium/RTL/PDF/print/PWA suite: [successful run 44367909907](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44367909907). This is evidence of that historical full run, not a current requirement to repeat it.
- Temporary fork-only workflow removed after verification; no fork workflow was copied upstream.
- Generated outputs transferred through [PR #13](https://github.com/MohdUjjain/11-hikam/pull/13) into the original editorial branch, not directly into original `main`; merge commit `acd72217ebf6945abb1c0a6d844b84f6e97bdb7e`.
- Exact Git blob SHA matches were verified in both repositories for `index.html`, `src/philosophy_study_notes.html`, `service-worker.js`, the canonical chapter, Companion manifest/reader JavaScript and CSS.
- The pilot established that fork-hosted verification works. Its test result and any later public deployment remain distinct evidence.
