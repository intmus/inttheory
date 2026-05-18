# System Changelog — Sean

## 2026-05-18

- **Full ACP implementation** — closed all remaining gaps against the authoritative spec (`agent-harness-impl.md`)
- **Ported** `agent/extractors/relation-scan.py` from personal-assistant hub
- **Updated** `relation-scan-config.yaml` — added Miranda's workspace, shared workspace, agent/ to targets; added report_dir
- **Created** `workspace/shared/` — cross-role shared workspace per ACP spec §11
- **Added** `## Miranda Wilson` section to `todo/todo.md`
- **Created** `workspace/miranda_ws/active/todo-handoff.md` — dormant handoff file with hub activation instructions
- **Updated** `agent/roles/miranda/identity.md` — added Communication Preferences, Hub Connection, Close Session sections
- **Updated** `agent/roles/miranda/role-config.md` — added Hub Expansion section
- **Updated** `agent/protocols/core.md` — added process tag documentation, generalized handoff path, added close-session hook reference
- **Updated** `CLAUDE.md` — added shared workspace to directory tree, removed "after porting" note from relation scan command
- **Updated** `.gitignore` — added `agent/extractors/relation-reports/`
- **Updated** `agent/extractors/index.md` — removed "not yet ported" note

## 2026-04-27

- **Migration:** Adopted agent harness from LHSOM/personal-assistant frameworks
- **Created** `role-config.md` — structural config with file authority hierarchy, content status, technical notes
- **Created** `identity.md` — user profile, agent role, contributors, post-logsession hook for hub sync
- **Migrated** session logs from `short-term-memory/daily/` to `agent/roles/sean/short-term/daily/`
- **Created** `agent/protocols/core.md` — `/logsession` and `/remember` commands, session log format, compaction rules
- **Created** `agent/shared/SHORTHAND.md` — abbreviations, shortcuts, key people, workspace quick-access
- **Created** `agent/toshare/registry.md` — hub connection with User Heading column
- **Created** `todo/todo.md` — migrated from `docs/TODO.md` to P1-P6 checkbox format
- **Created** project folders under `workspace/sean_ws/active/` with detailed specs
- **Created** `agent/review/` pipeline (pending/approved/revisions)
- **Rewrote** `CLAUDE.md` as lean map; merged editorial content into `docs/style-guide.md`

## 2026-04-04

- **Created** `long-term-memory/identity.md` — agent role, user profile, key contributors, project context
- **Created** `long-term-memory/protocols.md` — core commands, session log format, compaction rules
- **Created** `long-term-memory/CHANGELOG.md` — original changelog (now superseded by this file)
