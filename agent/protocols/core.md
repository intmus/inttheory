# Protocols — Integrated Musicianship

## Core Principle

This agent assists in editing, developing, and managing the Integrated Musicianship project. All session work is logged to maintain continuity across conversations.

---

## Command Shortcuts

### Session Management

| Shortcut | Action |
|---|---|
| `/logsession` | Session memory save — write log, commit, push, run post-logsession hook |
| `/remember` | Start-of-session context reload — pull, read recent logs, surface pending work |

---

### /logsession

**Purpose:** Session memory save. Use for both mid-session checkpoints and end-of-session logging.

**Steps:**

1. Summarize the current conversation — what was done, decided, and what's pending
2. Construct a session log entry with three sections: **Summary**, **Handoff Context**, **References**
3. Read `agent/roles/[role]/short-term/daily/YYYY-MM-DD.md` (today's date). Append if it exists; create with frontmatter if not.
4. Write/append the entry
5. Stage the daily log file and any other files modified during the session
6. Commit: `git commit -m "Log session YYYY-MM-DD — [brief description]"`
7. Push: `git push`
8. **Post-logsession hook:** Check the role's `identity.md` for a **Post-logsession** section. If one exists, execute those steps.

**The cold-start test:** If a fresh agent reads only this log entry, can it continue the work? If not, the handoff context isn't specific enough. "Continue the migration" fails. "3 of 8 files migrated; remaining: X, Y, Z at path/" passes.

**When to use mid-session:**
- After completing a major step in a multi-step task
- After a significant decision
- Before a large or token-intensive operation
- After 30+ minutes of substantial new content

### /remember

**Purpose:** Start-of-session context reload.

**Steps:**

1. Run `git pull`
2. Read daily log files for the active role (most recent first)
3. Read the role's section of `todo/todo.md`
4. Synthesize and report — what's pending, what needs attention
5. Proactively surface handoff items

**Key behavior:** Don't recite logs. Identify what needs to be picked up and ask the user what they want to work on.

---

## Session Log Format

Every entry in `agent/roles/[role]/short-term/daily/YYYY-MM-DD.md`:

```markdown
---
date: YYYY-MM-DD
role: [role name]
---

# YYYY-MM-DD — Session Log

## Summary

- Completed X
- Decided Y
- Deferred Z (reason)

## Handoff Context

### [Topic Name]
State of work. What's done, what's next. Exact file paths. Specific decisions and why.

### [Another Topic]
Same structure. One subsection per active thread.

## References

- `path/to/file-created.md` — what it is
- `path/to/file-modified.md` — what changed
```

Multiple sessions per day: append with a descriptive header (e.g., "## Afternoon Session — Proofreading").

---

## Compaction

Daily logs older than **7 days** compact into monthly files in `agent/roles/[role]/short-term/compacted/YYYY-MM.md`.

**Keep:** Decisions and rationale, outcomes, unresolved items and where carried forward, significant file paths.

**Strip:** Step-by-step process details, troubleshooting back-and-forth, conversational filler, superseded intermediate states.

**Format:** One paragraph per day summarizing key decisions and outcomes.

---

## Project-Specific Protocols

### Editing Content

- Always read a file before editing it
- Lesson files are authoritative — do not change content without confirmation from Sean
- Discussion files may contain errors — flag rather than silently fix
- Preserve the discovery-based pedagogical structure (examples before rules, `### Conclusion` sections)
- Match the voice and style of chapters 14-22 (see `docs/style-guide.md`)

### Music Notation

- Use HTML `<sup>` tags for all chord symbols in text
- Use the ABC notation capture/include pattern for musical examples
- See `docs/style-guide.md` for full notation conventions

### Skill-First Check

Before starting any multi-step task, check `agent/skills/skill-index.md` for an existing skill. If one exists, follow it. If none exists and the task will recur, propose creating one alongside the work.

### Review Workflow

Work from collaborators routes through `agent/review/`:
1. Collaborator places draft in `agent/review/pending/`
2. Sean (or Sean's agent) reviews
3. Approved → `agent/review/approved/`; needs changes → `agent/review/revisions/` with feedback
4. Collaborator revises and resubmits to `pending/`
