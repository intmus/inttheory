# To-Do

<!--
Priority scale:
  P1 — Immediate priority
  P2 — Within the next few days
  P3 — Within the week
  P4 — Within 30 days
  P5 — Due date more than 30 days out
  P6 — No due date, tracking only
-->

## Sean Butterfield

### Agent Infrastructure

- [ ] **Test close session with hub snapshot** — verify todo snapshot appends to hub's `todo-handoff.md` [P4]
- [x] **Port relation-scan.py** — copy script from personal-assistant hub to `agent/extractors/`. Config is ready. [P4]
- [ ] **Frontmatter backfill** — add frontmatter (title, type, date, keywords) to all non-Jekyll markdown documents per `agent/skills/document-frontmatter.md`. Batch by directory: agent/ files first, then workspace/, wiki/. Jekyll chapter files are handled separately by Frontmatter enrichment. [P3]

### Content QA

- [ ] **Fix filename bugs** — remove space in `b2- modesandpentatonics.md`, remove double extension on `d2-tx-mustexture.md.md`, fix "Pentonic" → "Pentatonic" in Ch 2b Discussion title [P3]
- [ ] **Verify multimedia embeds** — check Spotify/Vimeo embeds in Discussion files, investigate ABC examples flagged with playback issues [P5]
- [ ] **Standardize file naming convention** — decide whether to unify ch 1-12 and ch 13+ naming patterns across the whole book. See `docs/lesson-naming.md`. [P6]

### Content Projects

- [ ] **Rewrite Unit 22** — restructure post-tonal chapter around comparison-driven workflow. See `workspace/sean_ws/active/unit-22-rewrite/project.md` [P4]
- [ ] **Grand Unified Theory of Harmonic Function** — new chapter crystallizing how all harmonic concepts connect. See `workspace/sean_ws/active/grand-unified-theory/project.md` [P4]
- [ ] **Style revision, chapters 1-8** — match prose voice to chapters 14-22 without changing pedagogy. See `workspace/sean_ws/active/style-revision/project.md` [P4]
- [ ] **Fill Chapter 13 content gaps** — draft Lesson prose for Phrasing and Texture. See `workspace/sean_ws/active/chapter-13-content/project.md` [P4]
- [ ] **Full proofread** — spelling, grammar, notation consistency, ABC rendering, broken links. See `workspace/sean_ws/active/proofread/project.md` [P4]
- [ ] **Lesson prose, chapters 14-22** — fill empty Lesson files where Discussion files carry all weight. See `workspace/sean_ws/active/lesson-prose-14-22/project.md` [P5]
- [ ] **Import Integrated Aural Skills** — convert from Pressbooks, integrate into Jekyll site. Miranda leads. See `workspace/sean_ws/active/aural-skills-import/project.md` [P4]

### Site and Infrastructure

- [ ] **Frontmatter enrichment** — add `track`, `file_type`, and `keywords` to all 130+ chapter files. Batched by chapter group. [P4]
- [ ] **Verify site after collections_dir move** — spot-check intmus.github.io/inttheory after push: home, TOC, chapters, ABC, images, search [P3]
- [ ] **Website modernization** — update Jekyll site theme, support three-track architecture. See `workspace/sean_ws/active/website-modernization/project.md` [P4]
- [ ] **Assignment distribution system** — replace Discord with integrated assignment/discussion layer. See `workspace/sean_ws/active/assignment-distribution/project.md` [P4]
- [ ] **Flexible curriculum reordering** — config-driven topic ordering for 2/3-semester layouts. See `workspace/sean_ws/active/curriculum-reordering/project.md` [P5]
- [ ] **OER fork-and-customize tool** — agentic workflow for adopting instructors. See `workspace/sean_ws/active/oer-customize-tool/project.md` [P6]

### Assignment Management

- [ ] **Migrate Google Drive assignments** — move assignments and answer keys into structured repo format. See `workspace/sean_ws/active/assignment-migration/project.md` [P4]
- [ ] **Build assignment rotation system** — tagged pool shuffled year-to-year. Depends on assignment migration and distribution system. See `workspace/sean_ws/active/assignment-rotation/project.md` [P5]

### Agentic Part Writing

- [ ] **Agentic part-writing model** — build an agentic system for musical part writing. Details forthcoming from personal-assistant hub. [P4]
  - [ ] **OMR software evaluation** — test five OMR tools against a homegrown agent + LilyPond approach:
    1. [Soundslice](https://www.soundslice.com/sheet-music-scanner/)
    2. [Audiveris](https://en.wikipedia.org/wiki/Audiveris)
    3. [SmartScore Music-to-XML](https://www.musitek.com/music-to-xml.html)
    4. [capella-scan](https://www.capella-software.com/us/index.cfm/products/capella-scan/info-capella-scan/)
    5. [homr](https://github.com/liebharc/homr)

### Integrated Piano

- [ ] **Draft piano curriculum** — future Class Piano track. Infrastructure only for now. See `workspace/sean_ws/active/piano-curriculum/project.md` [P6]

### Maintenance

- [ ] **Completed todo cleanup** — Review the Completed section. Keep anything still useful; move the rest to archive/todo-completed.md. After cleanup, set the next due date 3 months out. [by 2026-08-12] [P5]

---

## Miranda Wilson

### Aural Skills Import

*To be populated when Miranda begins working in this repo.*

---

## Completed

<!--
Title-only archive. Details in session logs and git history.
Cleanup: every 3 months, review this list. Keep anything still useful; move the rest to archive/todo-completed.md.
-->

- [x] Internal content audit [completed 2026-03-28]
- [x] Style and voice analysis [completed 2026-03-27]
- [x] Discussion vs. Lesson file authority assessment [completed 2026-03-28]
- [x] Project CLAUDE.md [completed 2026-03-28]
- [x] Writing and style guide [completed 2026-03-27]
- [x] Four-layer memory framework [completed 2026-04-04]
- [x] Agent harness migration [completed 2026-04-27]
- [x] Register inttheory in hub registry [completed 2026-05-13]
- [x] Test new/open session [completed 2026-05-13]
