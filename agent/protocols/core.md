# Protocols — Integrated Musicianship

## Core Principle

This agent assists in editing, developing, and managing the Integrated Musicianship project. All session work is logged to maintain continuity across conversations.

---

## Processing New Information

When the user gives a task or instruction:

1. **Skill-first check.** Before starting any multi-step task, check `agent/skills/skill-index.md` for an existing skill. If one exists, follow it. If none exists and the task will recur, propose creating one alongside the work.
2. **Route the request.** Determine whether it's content editing, infrastructure work, task management, or something else. Consult the appropriate reference files.
3. **Confirm before acting** on anything that changes authoritative content (Lesson files), modifies agent infrastructure, or affects another role's workspace.

---

## Session Commands

Four natural-language commands on a 2×2 grid. The agent recognizes these from any reasonable phrasing that includes the key words. If the user says something adjacent (e.g., "catch me up") without using the command words, briefly offer the relevant command and explain the difference.

|  | **Lightweight** | **Full (once per day)** |
|---|---|---|
| **Starting** | new session | open session |
| **Ending** | log session | close session |

Each "full" version includes everything in its lightweight counterpart, plus daily-only tasks.

---

### New Session

Get back to work after a terminal switch, break, or context loss.

1. `git pull`
2. Read recent daily logs for the resolved role (most recent first)
3. Read the role's section of `todo/todo.md`
4. **Highlight new items** (multi-user). Compare the role's current todo section against the most recent daily log. Any item not referenced in that log was likely added by another role or from another terminal — flag it to the user.
5. Synthesize and report — what's pending, what needs attention

**Key behavior:** Don't recite logs. Identify what needs to be picked up and ask the user what they want to work on.

### Open Session

Start the day. Run once per day, first session only. Includes everything in New Session, plus:

6. Run any project-specific health checks. Surface BLOCK or WARN items immediately.
7. If more than 7 daily logs exist, offer compaction of the oldest entries.
8. Check for incoming handoff items — read `workspace/sean_ws/active/todo-handoff.md` for new items and surface them for user review.
9. Read `agent/reference/session-log.md` for cross-role notifications (multi-user).
10. **Auto-escalate priorities.** For every open item with a `[by YYYY-MM-DD]` date, calculate the date-derived priority:

    | Days until due | Minimum priority |
    |---|---|
    | Overdue or due today | P1 |
    | 1–3 days | P2 |
    | 4–7 days | P3 |
    | 8–30 days | P4 |
    | 31+ days | P5 |
    | No `[by ...]` date | Untouched |

    If the date-derived priority is more urgent than the current tag, update in place. Never downgrade. Report all changes.

11. Proactively surface overdue tasks, dependency-flagged items, and pending handoffs.

Steps 4, 6, 7, 8, and 9 are conditional — they apply when the project has the relevant infrastructure or is in multi-user mode. The core New Session sequence (1–3, 5) is universal.

### Log Session

Save context and keep working, or save before closing a quick terminal.

1. Summarize the session — what was done, decided, and what's pending
2. Construct a session log entry with three sections:
   - **Summary** — bullet points of completed work and decisions
   - **Handoff Context** — specific enough for a cold-start agent to pick up where this session left off
   - **References** — files created or modified with brief descriptions
3. Write/append to the daily log file (`agent/roles/[role]/short-term/daily/YYYY-MM-DD.md`)
4. **Cross-role task handoff** (multi-user). If this session completed a step in a multi-role process, mark the step done in the todo file and add the next step to the appropriate role's section. Confirm with the user before adding items to another role's section.
5. **Shared notification** (multi-user). If any items are non-sensitive and relevant to other roles, append a brief entry to `agent/reference/session-log.md` under today's date, prefixed with the role.
6. Stage and commit all changed files
7. `git push`

**The cold-start test:** If a fresh agent reads only this log entry, can it continue the work? If not, the handoff context isn't specific enough. "Continue the migration" fails. "3 of 8 files migrated; remaining: X, Y, Z at path/" passes.

**When to use mid-session:**
- After completing a major step in a multi-step task
- After a significant decision
- Before a large or token-intensive operation
- After 30+ minutes of substantial new content

### Close Session

End the day. Run once per day, last session only. Includes everything in Log Session, plus:

8. **Completed-item sweep.** Scan the todo file for `- [x]` items outside the Completed section. For each: extract the title and completion date, append to Completed as a single line, delete the original from its inline location. Remove any content-area sections left empty.
9. Check `identity.md` for a **Close Session** section — if one exists, execute those steps.

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

**Process:**
1. Read the daily file
2. For each session entry, extract decisions, outcomes, and unresolved items
3. Write a one-paragraph summary per day to the monthly file (append if exists)
4. Delete the original daily file
5. Commit the changes

---

## Project-Specific Protocols

### Editing Content

- Always read a file before editing it
- Lesson files are authoritative — do not change content without confirmation from Sean
- Discussion files may contain errors — flag rather than silently fix
- Preserve the discovery-based pedagogical structure (examples before rules, `### Conclusion` sections)
- Match the voice and style of chapters 14-22 (see `agent/reference/style-guide.md`)

### Music Notation

- Use HTML `<sup>` tags for all chord symbols in text
- Use the ABC notation capture/include pattern for musical examples
- See `agent/reference/style-guide.md` for full notation conventions

### Review Workflow

Work from collaborators routes through `agent/review/`:
1. Collaborator places draft in `agent/review/pending/`
2. Sean (or Sean's agent) reviews
3. Approved → `agent/review/approved/`; needs changes → `agent/review/revisions/` with feedback
4. Collaborator revises and resubmits to `pending/`
