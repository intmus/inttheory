# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Integrated Musicianship** is an open-source, interactive, online curriculum suite for college music courses, built as a Jekyll site. It is an OER based at the University of Idaho.

- **Live site:** https://intmus.github.io/inttheory
- **GitHub:** https://github.com/intmus/inttheory
- **Tech stack:** Jekyll, Markdown, ABC notation, HTML/CSS/JS

The suite includes three tracks: **Integrated Theory** (active, 22 chapters in this repo), **Integrated Aural Skills** (planned import from Pressbooks), and **Integrated Piano** (future).

---

## Session Lifecycle

Four natural-language commands — see `agent/protocols/core.md` for full steps.

|  | Lightweight | Full (once/day) |
|---|---|---|
| **Starting** | new session | open session |
| **Ending** | log session | close session |

---

## Directory Structure

```
inttheory/
├── CLAUDE.md                          ← this file (project map)
├── content/                           ← all Jekyll collections (collections_dir)
│   ├── _01-pitches-clefs/
│   ├── ... (20 more chapter dirs)
│   ├── _22-intro-to-post-tonal/
│   ├── _assignments/
│   └── _final-project/
├── _includes/                         ← Jekyll templates (not collections)
├── _layouts/
├── _sass/
├── _data/                             ← Jekyll data files (track map, etc.)
├── todo/
│   └── todo.md                        ← task list (P1-P6 format)
├── agent/
│   ├── roles/
│   │   ├── sean/                       ← owner/author role
│   │   │   ├── role-config.md         ← structural config (read-only)
│   │   │   ├── identity.md            ← preferences, active threads, close-session hook
│   │   │   ├── short-term/daily/      ← session logs
│   │   │   ├── short-term/compacted/  ← monthly summaries
│   │   │   ├── long-term/             ← persistent role knowledge
│   │   │   └── system/CHANGELOG.md
│   │   └── miranda/                   ← collaborator/author role
│   │       └── [same structure]
│   ├── protocols/
│   │   ├── index.md                   ← protocol index
│   │   └── core.md                    ← session management, editing, review workflow
│   ├── skills/
│   │   └── skill-index.md
│   ├── templates/
│   │   └── index.md
│   ├── extractors/
│   │   └── index.md
│   ├── reference/
│   │   ├── shorthand.md               ← abbreviations, commands, key people
│   │   ├── style-guide.md             ← voice, tone, formatting, pedagogy, analytical framework
│   │   └── session-log.md             ← cross-role notification layer
│   ├── toshare/
│   │   └── registry.md               ← cross-project hub connection
│   └── review/
│       ├── pending/                   ← work awaiting approval
│       ├── approved/
│       └── revisions/
├── workspace/
│   ├── sean_ws/
│   │   ├── active/                    ← project folders with detailed specs
│   │   ├── uploads/
│   │   └── confidential/             ← gitignored
│   └── miranda_ws/
│       └── [same structure]
├── archive/                           ← completed outputs
├── wiki/                              ← permanent knowledge base
├── repeatable-processes/              ← semester cycle checklists
├── docs/
│   ├── topic-index.md                ← all 88 files indexed across 22 chapters
│   └── lesson-naming.md             ← file naming conventions
├── assets/, images/, forum/, search/  ← site assets
└── index.md, about.md, toc.md, ...   ← site pages
```

---

## Common Commands

```bash
# Determine today's date (run at session start)
python -c "from datetime import date; d = date.today(); print(f'{d.strftime(\"%A, %B\")} {d.day}, {d.year}')"

# Relation scan (after porting script from hub)
python agent/extractors/relation-scan.py                     # Default scan
python agent/extractors/relation-scan.py --viz               # With HTML visualization

# Jekyll local dev server
bundle exec jekyll serve
```

---

## Key Files

| File | Purpose |
|------|---------|
| `agent/roles/sean/role-config.md` | File authority hierarchy, content status, technical notes |
| `agent/roles/sean/identity.md` | User profile, contributors, active threads, close-session hook |
| `agent/protocols/core.md` | Session management, processing new information, editing protocols, review workflow |
| `agent/reference/shorthand.md` | Abbreviations, note-taking shorthand, key people, workspace quick-access |
| `agent/reference/style-guide.md` | Voice, tone, formatting, pedagogy, analytical framework — the editorial bible |
| `agent/skills/skill-index.md` | Index of reusable workflows (check before starting multi-step tasks) |
| `agent/skills/document-frontmatter.md` | **Mandatory.** Frontmatter spec for all markdown documents — maintained automatically during processing |
| `docs/topic-index.md` | Complete index of all files across all 22 chapters |
| `docs/lesson-naming.md` | File naming conventions by chapter range |
| `todo/todo.md` | All tasks, P1-P6 priority, links to project specs in workspace |
| `agent/toshare/registry.md` | Cross-project connection to personal-assistant hub |
