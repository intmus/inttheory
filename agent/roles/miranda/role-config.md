# Role Config — Miranda (Collaborator/Author)

## Role

Collaborator and author of *Integrated Aural Skills*. Primary responsibility: importing and integrating aural skills content from Pressbooks into the Jekyll site. Submits content through the review pipeline for Sean's approval.

## Memory Paths

| Type | Path |
|------|------|
| Short-term (daily) | `agent/roles/miranda/short-term/daily/` |
| Short-term (compacted) | `agent/roles/miranda/short-term/compacted/` |
| Long-term | `agent/roles/miranda/long-term/` |
| System changelog | `agent/roles/miranda/system/CHANGELOG.md` |

## System Files

| File | When to consult |
|------|-----------------|
| `agent/protocols/core.md` | Every session — session management commands |
| `agent/shared/SHORTHAND.md` | When resolving abbreviations, names, or shortcuts |
| `docs/style-guide.md` | When writing or editing any content |
| `docs/topic-index.md` | When locating content across chapters |
| `docs/lesson-naming.md` | When creating or renaming files |
| `todo/todo.md` | At session start and when tracking work |

## Session Checklist

**Start of session:**
1. Run `/remember`

**End of session:**
1. Run `/logsession`

## Capabilities

- Edit files in her workspace (`workspace/miranda_ws/`)
- Submit content to `agent/review/pending/` for Sean's approval
- Edit her own role files (`agent/roles/miranda/`)
- View (but not modify) shared agent files

## Constraints

- Cannot modify Sean's role files or workspace
- Cannot approve review items — only Sean can
- Cannot modify agent infrastructure (protocols, skills, templates) without Sean's approval
- Content edits to chapter files should go through the review pipeline
