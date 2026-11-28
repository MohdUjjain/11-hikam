# Phase 3 — publication identity, sidebar hierarchy and UI maintenance

**Status:** technical phase record and preserved behavior. Use the [current scoped verification guide](SECONDARY_FORK_CI_AND_RELEASE.md) for checks appropriate to an actual change and the [current editorial protocol](../editorial/STUDY_AID_ROLES_AND_READING_DESIGN_PROTOCOL.md) for aid roles. A documentation-only pass does not require reader builds, browser/print/offline tests or a whole-book suite, and does not implement visual changes.

**This permission does not authorize an independent judgment that the author’s position is unproved, generalized or unacceptable.**

- The published book keeps its scholarly cover title **Philosophy — The Complete Dossier** while the cover running brand now reads **11AM · Takhassus Hikam Dossier**, matching the site, manifest and installed app. Do not rewrite the authored dossier text or chapter titles for branding.
- **Expand all levels / Collapse all levels** now cover Topic, Sub-topic **and chapter section (§) lists**. They persist the user's manual expansion choices for the current session. The chapter active-location marker never expands collapsed groups on scroll.
- The Tools tab shows **Continue reading** only when a saved reading place exists, and keeps **Revision visibility**, **Print / Export PDF** and **Offline reading** in one consistent navy/gold card system. Revision visibility persists locally; print inclusion remains independent.
- Screen chrome small-text and contrast have been strengthened (including the former `#A87C1F` small dossier number against navy). These rules must not modify print geometry, semantic content callouts, Arabic inherited fonts, or CSS `--hue` chapter palette.
- Removed abandoned `.quicknav` CSS, sidebar `.toc-search-tools` CSS, inactive sidebar `wireSearch()` logic and its unused `data-search-text` attributes. The **top-bar full-book search remains untouched**.
- When changing the visual/reader behaviors described here, select `python src/build.py --check`, the affected publication validations, `python src/tests/verify_visual_polish.py`, bounded desktop/mobile Chromium evidence and a selected-chapter print check where print behavior could be affected. These are affected-feature checks, not an unconditional full-suite gate for every edit.
