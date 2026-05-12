# Next Steps — Post-ACP Upgrade and Repo Reorganization

*Created 2026-05-12. Temporary working document — delete when absorbed into todo or completed.*

---

## Completed This Session (2026-05-12)

- ACP upgrade: 4-command session system (new/open/log/close session)
- File moves: shorthand → `agent/reference/`, style-guide → `agent/reference/`
- New infrastructure: protocol index, extractor index, session-log, extractors dir
- `collections_dir: content` — all 24 collection dirs moved into `content/`
- Placeholders: `archive/`, `wiki/`, `repeatable-processes/`, `_data/`
- `_data/track-map.yml` for future cross-track navigation
- Relation scan skill + config (script not yet ported)
- Todo updates: agentic part-writing project, quarterly cleanup task, verification tasks
- Fixed: `docs/topic-index.md` paths updated to `content/` prefix
- Fixed: `_config.yml` tagline updated to 2025-26
- Fixed: `.claude/` added to `.gitignore`

---

## 1. Quick Fixes (next session, <30 min total)

### Filename bug fixes (P3)
- `content/_02-int-scales-keys/b2- modesandpentatonics.md` — remove space in filename
- `content/_13-phrasing-texture/d2-tx-mustexture.md.md` — remove double `.md` extension
- Fix "Pentonic" → "Pentatonic" in Ch 2b Discussion title (frontmatter)

### CHANGELOG entries
Add to `agent/roles/sean/system/CHANGELOG.md`:
- ACP upgrade (4-command system, reference file moves, new indexes)
- `collections_dir` reorganization (24 dirs → `content/`)
- New infrastructure directories (archive, wiki, repeatable-processes, _data)

### Review README.md
May reference old repo structure, old edition URLs, or outdated contributor info. Read and update.

### Review remaining docs/ files
`docs/` still contains `abc-include.md`, `class-discussion.md`, `discord.md`. Determine:
- Still relevant? → keep in `docs/`
- Permanent reference? → move to `wiki/`
- Obsolete? → delete

### Mark collections-dir-plan.md as executed
At `workspace/sean_ws/active/website-modernization/collections-dir-plan.md` — note that it was implemented on 2026-05-12.

---

## 2. Frontmatter Enrichment (1-3 sessions)

### Create document-frontmatter skill first
`agent/skills/document-frontmatter.md` — standardize what fields go on which file types (chapter files vs. wiki vs. workspace). Reference the ACP impl guide spec. Wire into core.md "Processing New Information" section.

### Mechanical pass (~20 min)
- Add `track: theory` to all chapter .md files in `content/`
- Add `file_type: lesson|discussion|reading` derived from filename patterns

### Keyword pass (batched across sessions)
- Add `keywords:` array (3-7 per file) to all 130+ chapter files
- Use `docs/topic-index.md` descriptions and file content to select terms
- Maintain consistent vocabulary (see plan file for controlled vocab)
- Batch: ch 1-4, 5-8, 9-12, 13-16, 17-22

### Verify after each batch
Push and spot-check that the site still renders. Malformed YAML would break the build.

---

## 3. Infrastructure Completion (1 session)

### Port relation-scan.py
- Copy from `personal-assistant/agent/extractors/relation-scan.py`
- Install dependencies: `networkx`, `pyyaml`
- Test against `content/` with current config
- Update `agent/extractors/index.md` when ported

### Test ACP protocols
- **Close session** — verify todo snapshot appends to hub's `todo-handoff.md`
- **Open session** — verify full protocol: pull, logs, priority escalation, compaction, handoffs
- **New session** — verify lightweight variant works

### Register in hub
- Add inttheory entry to the hub's `agent/toshare/registry.md` (must be done from the personal-assistant repo)

### Scan workspace project specs for stale paths
The 14 project folders in `workspace/sean_ws/active/` were created before the `collections_dir` move. Any file paths referencing `_01-pitches-clefs/` etc. need the `content/` prefix. Batch scan and update.

### Miranda onboarding prep
- Add Close Session section to `agent/roles/miranda/identity.md` (when she's ready to use the hub handoff)
- No urgency — summer onboarding

---

## 4. Summer Content Projects (sequencing recommendation)

These are all tracked in `todo/todo.md`. Listed here for sequencing context.

1. **Filename fixes + frontmatter mechanical pass** — quick wins that unblock everything
2. **Frontmatter keywords** — batched, enables the relation scan
3. **Run relation scan** — identify orphans, clusters, and drift before starting content work
4. **Style revision, chapters 1-8** — benefits from keyword analysis of cross-chapter connections
5. **Full proofread** — can run in parallel with or after style revision
6. **Chapter 13 gaps, Unit 22 rewrite, Grand Unified Theory** — independent, tackle based on energy
7. **Lesson prose, chapters 14-22** — P5, lower priority
8. **Import Integrated Aural Skills** — Miranda leads; multi-track infrastructure is ready

---

## 5. Site and Infrastructure Projects

- **Website modernization** — track-map and `collections_dir` are in place; remaining: theme update, sidebar redesign for multi-track nav, mobile responsiveness
- **Assignment distribution** — replace Discord with integrated layer
- **Assignment migration** — Google Drive → repo format (tagged, rotatable pool)
- **Flexible curriculum reordering** — config-driven topic ordering for 2/3-semester layouts
- **OER fork-and-customize tool** — P6, future

---

## 6. Agentic Part Writing

- Details forthcoming from personal-assistant hub
- Project spec needed at `workspace/sean_ws/active/agentic-part-writing/project.md`
- OMR evaluation: Soundslice, Audiveris, SmartScore, capella-scan, homr
- Compare against homegrown agent + LilyPond approach
