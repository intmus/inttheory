# Shorthand Reference

A single reference for all abbreviations, acronyms, note-taking shorthand, and custom commands used in this project.

---

## Users

| User | Role(s) |
|---|---|
| Sean Butterfield | Owner/Author (this repo), Director (LHSOM), Owner (personal-assistant) |
| Miranda Wilson | Collaborator/Author (this repo), Cello faculty at LHSOM |

In framework documentation and handoff files, "user" refers to any human and "agent" refers to the AI assistant.

---

## Custom Shortcuts

Slash commands recognized by the agent. Defined in `agent/protocols/core.md`.

| Shortcut | What it does |
|---|---|
| `/logsession` | Summarize conversation, write to today's session log, commit, push, run post-logsession hook |
| `/remember` | Pull latest, read recent session logs, report what's pending |

---

## Note-Taking Shorthand

Commands Sean embeds in notes. The agent scans for these after note submission but **does not act immediately** — items are queued for joint review.

| Shorthand | Meaning | What the agent does |
|---|---|---|
| `todo:` | Add to the todo list | Queues for review. On confirmation, adds to `todo/todo.md` under the appropriate content area. |
| `recap:` | Ask me about this later | Flags for discussion during the next review session. |

**Processing rules:**
1. After creating a note, scan for shorthand markers
2. List extracted items back to Sean with their source
3. Hold until Sean says "show me my todo" or "let's review" — not auto-added
4. During review, Sean confirms, edits, reprioritizes, or discards
5. Confirmed items added to `todo/todo.md` with a reference to the source

---

## Abbreviations and Acronyms

| Abbreviation | Meaning | Context |
|---|---|---|
| LHSOM | Lionel Hampton School of Music | Sean's unit at U of I |
| U of I | University of Idaho | Institution |
| OER | Open Educational Resource | Project type |
| TA | Teaching Assistant | Graduate position |
| NCT | Non-Chord Tone | Music theory term |
| pc / pcs | Pitch class / pitch-class set | Post-tonal analysis |

---

## Key People

| Name/Reference | Who they are |
|---|---|
| Sean Butterfield | Author of Integrated Theory, project owner, music theory professor at U of I |
| Miranda Wilson | Author of Integrated Aural Skills, cello faculty at LHSOM, collaborator on this project |
| Evan Williamson | Cofounder — built the original repo, Jekyll/ABC setup. Collaborator for technical help. |

---

## Workspace Quick-Access Names

| What Sean says | What it maps to |
|---|---|
| "check uploads" | Scan `workspace/sean_ws/uploads/` for new files |
| "check handoffs" | Scan `workspace/sean_ws/active/todo-handoff.md` for incoming items |
| "check review" / "what's pending" | Scan `agent/review/pending/` for items awaiting approval |
| "hand this off to [project]" | Write item to that project's handoff file, add to Pending in Other Repos |
| "[project name]" (e.g., "unit 22," "proofread") | Resolve to matching folder in `workspace/sean_ws/active/` |

If the agent can't resolve a natural name to a single file, ask for clarification.

---

## Adding New Entries

- **Unknown acronyms:** Ask the user for the full meaning before using or recording it. Never guess.
- **New shorthand:** Add to Note-Taking Shorthand table and update `agent/protocols/core.md`
- **New abbreviation:** Add to Abbreviations table
- **New person:** Add to Key People table
- **New shortcut:** Add to Custom Shortcuts table and update `agent/protocols/core.md`
- **New quick-access name:** Add to Workspace Quick-Access Names table

All changes to this file should be logged in `agent/roles/sean/system/CHANGELOG.md`.
