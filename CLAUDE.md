# Integrated Musicianship — Project Instructions

**Integrated Musicianship** is an open-source, interactive, online curriculum suite for college music courses, built as a Jekyll site. It is an OER based at the University of Idaho.

- **Live site:** https://intmus.github.io/inttheory
- **GitHub:** https://github.com/intmus/inttheory
- **Tech stack:** Jekyll, Markdown, ABC notation, HTML/CSS/JS

The suite includes three tracks: **Integrated Theory** (active, 22 chapters in this repo), **Integrated Aural Skills** (planned import from Pressbooks), and **Integrated Piano** (future).

---

## Directory Structure

```
inttheory/
├── CLAUDE.md                          ← this file (project map)
├── todo/
│   └── todo.md                        ← task list (P1-P6 format)
├── agent/
│   ├── roles/
│   │   ├── sean/                       ← owner/author role
│   │   │   ├── role-config.md         ← structural config (read-only)
│   │   │   ├── identity.md            ← preferences, active threads, post-logsession hook
│   │   │   ├── short-term/daily/      ← session logs
│   │   │   ├── short-term/compacted/  ← monthly summaries
│   │   │   ├── long-term/             ← persistent role knowledge
│   │   │   └── system/CHANGELOG.md
│   │   └── miranda/                   ← collaborator/author role
│   │       └── [same structure]
│   ├── protocols/
│   │   └── core.md                    ← /logsession, /remember, session format
│   ├── skills/
│   │   └── skill-index.md
│   ├── templates/
│   │   └── index.md
│   ├── shared/
│   │   └── SHORTHAND.md              ← abbreviations, shortcuts, key people
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
├── docs/
│   ├── style-guide.md                ← single source for writing style, formatting, pedagogy, analytical framework
│   ├── topic-index.md                ← all 88 files indexed across 22 chapters
│   └── lesson-naming.md             ← file naming conventions
└── _01- through _22-/               ← chapter content (Jekyll collections)
```

---

## Key Files

| File | Purpose |
|------|---------|
| `agent/roles/sean/role-config.md` | File authority hierarchy, content status, technical notes |
| `agent/roles/sean/identity.md` | User profile, contributors, active threads, post-logsession hook |
| `agent/protocols/core.md` | Session management commands, editing protocols, review workflow |
| `agent/shared/SHORTHAND.md` | Abbreviations, note-taking shorthand, key people, workspace quick-access |
| `agent/skills/skill-index.md` | Index of reusable workflows (check before starting multi-step tasks) |
| `docs/style-guide.md` | Voice, tone, formatting, pedagogy, analytical framework — the editorial bible |
| `docs/topic-index.md` | Complete index of all files across all 22 chapters |
| `docs/lesson-naming.md` | File naming conventions by chapter range |
| `todo/todo.md` | All tasks, P1-P6 priority, links to project specs in workspace |
| `agent/toshare/registry.md` | Cross-project connection to personal-assistant hub |
