# Secondary-account fork: CI verification and safe return to Hikam

**Status:** Implemented and validated on 18 November 2026: fork CI passed in [run 44367909907](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44367909907), and generated assets were transferred as [upstream PR #13](https://github.com/MohdUjjain/11-hikam/pull/13), merging into the Moran editorial branch (commit `acd72217ebf6945abb1c0a6d844b84f6e97bdb7e`). This record also governs future fork runs.  
**Upstream and sole public publication:** [`MohdUjjain/11-hikam`](https://github.com/MohdUjjain/11-hikam) (GitHub Pages remains here)  
**Proposed CI fork owner:** [`Mohd-Ujjain`](https://github.com/Mohd-Ujjain)  
**Precedent actually examined:** [`Mohd-Ujjain/nehj-majhud`](https://github.com/Mohd-Ujjain/nehj-majhud), a genuine private fork of `MohdUjjain/nehj-majhud`, running successful Actions jobs in the fork on 18 November 2026.  
**First candidate:** the existing [context-first Moran pilot PR #12](https://github.com/MohdUjjain/11-hikam/pull/12), branch `editorial/contextual-companions-source-depth-moran`.

## Ownership and billing are essential, not cosmetic

GitHub charges private-repository Actions minutes to the **owner of the repository that runs the workflow**, not the account that triggers it. A workflow executed on `MohdUjjain/11-hikam` still uses the original account's allowance even if triggered by another person. The verification jobs must therefore execute **inside** `Mohd-Ujjain/11-hikam`.

A pull request **targeting the original repository** may trigger the original repository's `pull_request` workflow and should not be used as the first verification mechanism when upstream Actions are out of minutes. Start by verifying in the fork. Keep publication and final merge at the upstream repository after reviewing the complete tested diff.

GitHub documentation: [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) · [Forking](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo?tool=webui) · [Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

## One-time GitHub UI setup

1. With the **`Mohd-Ujjain`** account, open `MohdUjjain/11-hikam`, select **Fork**, choose owner `Mohd-Ujjain`, keep the fork **private**, and **uncheck** `Copy the DEFAULT branch only` so the pending editorial branch is copied as well. Create the fork. If GitHub disallows private forking because of repository policy, do not publish a public duplicate: resolve access/permissions first.
2. In the new `Mohd-Ujjain/11-hikam` fork, open **Actions** and select the GitHub UI option to understand/enable workflows on the fork. Check **Settings → Actions → General** for enabled actions and suitable `GITHUB_TOKEN` permissions. Avoid broad read-write permissions when the job only reads and tests.
3. Keep **GitHub Pages disabled** on the fork (the canonical Pages reader remains upstream). Do not connect the fork to the original project's public domain.
4. Retain the candidate branch `editorial/contextual-companions-source-depth-moran` in the fork. Configure a fork-only verification workflow on that branch (not the original source repository), limited to explicit pilot-branch pushes and optionally `workflow_dispatch`.

## Verification pipeline on the fork

The first fork workflow must be reproducible, not merely a green status on unrelated tests:

1. Check out the exact fork candidate commit and record its SHA, together with its upstream-base SHA. Set up Python 3.12 and Ubuntu 24.04.
2. Run **`python src/build.py`** (the fork's original generated assets are stale for PR #12) and **`python src/build.py --check`**. Verify that `index.html`, `src/philosophy_study_notes.html`, and `service-worker.js` are produced by the canonical builder and belong to the same edition.
3. Execute the repository's **existing full structural verification commands**, including `verify_reading_companions.py`, `verify_publication.py`, `verify_source_attribution.py`, `validate_structure.py`, revision/search/reader contracts, and offline cache lifecycle scripts. The original `.github/workflows/verify-pages.yml` is the authoritative current command list; do not duplicate only a convenient subset.
4. Install `playwright==1.57.0` and `pypdf==5.9.0`, install Chromium, and run the **complete** browser test list in `.github/workflows/verify-pages.yml`, including `browser_reading_companions.py`, mobile/desktop, keyboard/RTL, print-clone and A4 PDF, reading state, offline/PWA upgrades.
5. Upload the built files, logs and test screenshots/PDF evidence as Actions artifacts with short retention. Avoid storing original copyrighted PDFs, source-language sample files, credentials or tokens in artifacts.
6. Only after all gates pass, commit the three **generated** outputs to the candidate branch of the **fork**; recheck the generated assets against the unchanged canonical source. Do not automatically push or merge into `MohdUjjain/11-hikam`.
7. Record the exact tested fork commit SHA, successful workflow run URL and candidate-file list. Compare the fork candidate with the upstream review branch to confirm that only intended changes and freshly built outputs differ.

## Returning verified work to the authoritative repository

1. The source-controlled editorial changes remain **in upstream PR #12** until the same edition has passed verification in the fork. Match the tested fork source tree to the upstream candidate (especially the complete `src/chapters/subtopic-1-1.html`, `src/reading_companions.json`, `src/reading_companions.js`, `src/philosophy_notes.css`, documentation and tests).
2. Transfer the three generated outputs **together**, not individually, back to upstream PR #12. They must be byte-for-byte consistent with the exact verified source tree. Check `python src/build.py --check` and hash/edition consistency where execution is available.
3. Review the final PR diff for unrelated chapter changes, generated file mismatches, unauthorized source uploads and unwanted workflow changes. Do not merge the fork-only CI workflow back to the canonical project.
4. Merge the original PR **only after** the fork run passes and the exact tested artifacts are present in the upstream PR. Confirm the GitHub Pages deployment from the upstream `main` merge commit. Upstream CI may show a quota-related failure or be unavailable; record the successful *fork* validation evidence explicitly rather than misrepresenting the upstream CI result.
5. For subsequent work, sync the secondary fork from original `main`, create a fresh fork feature branch, run the same gates and return only approved, verified changes. Avoid diverging fork-specific master content.

## Quota conservation

- Keep the ordinary upstream verification workflow as it stands unless the owner explicitly authorizes disabling/changing it. Do not consume scarce upstream minutes on repeated retries known to be blocked by account billing.
- In the fork prefer one **consolidated**, concurrency-cancelled workflow per candidate revision and avoid running separate full suites on both `push` and `pull_request` for the same change.
- Use short-lived artifacts and explicit `permissions: contents: read` for test jobs, with a separate narrowly scoped write step only if committing generated assets.
- Keep the fork **private**. The original companion articles and language-profile samples must remain outside either public repository or artifacts.

## Hold points

The flow cannot proceed beyond setup until the second-account fork is created and GitHub Actions enabled there. **No run or deploy is successful merely because this document exists.** Once the fork is visible through the second GitHub connection, create and run its actual workflow, verify the candidate, transfer the generated files, and only then merge the upstream PR.


## First successful pilot — verified result, 18 November 2026

- Source branch on fork: `editorial/contextual-companions-source-depth-moran`.
- Complete secondary-account build, source checks, full Chromium/RTL/PDF/print/PWA suite: [successful run 44367909907](https://github.com/Mohd-Ujjain/11-hikam/actions/runs/44367909907).
- Temporary fork-only workflow removed after verification; no fork workflow was copied upstream.
- Generated outputs transferred through [PR #13](https://github.com/MohdUjjain/11-hikam/pull/13) into the **original editorial branch**, not directly into original `main`.
- Exact Git blob SHA match verified in both repositories for `index.html`, `src/philosophy_study_notes.html`, `service-worker.js`, the canonical chapter, Companion manifest/reader JS, and CSS.
- This demonstrates that fork-hosted testing works. Published deployment is a **separate** gate and should be recorded only after independently verified.
