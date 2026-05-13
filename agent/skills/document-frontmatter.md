---
skill: Document Frontmatter
last-updated: 2026-05-13
updated-by: Claude
---

# Document Frontmatter

Maintain consistent YAML frontmatter on every markdown document in the repo. Frontmatter provides the metadata that powers the relation scan, enables document discovery, and keeps the repo navigable at scale.

**This is a mandatory behavior, not an optional skill.** The agent maintains frontmatter as part of normal document handling — creating, editing, archiving, or processing any markdown file.

---

## When to Apply

**Every time the agent creates or substantively edits a markdown document.** This includes:
- Creating new documents in `workspace/sean_ws/active/` or `workspace/miranda_ws/active/`
- Writing or updating wiki entries (`wiki/`)
- Creating or editing agent infrastructure files (`agent/`)
- Substantive content edits to chapter files (adding sections, rewriting content)
- Processing uploads into their destination
- Archiving documents

**Do not update frontmatter for:**
- Trivial edits (fixing a typo, appending a single bullet to a running list)
- Session logs (`agent/roles/*/short-term/`)
- Index files that use their own format (skill-index.md, protocol index, extractor index, etc.)
- Todo files (`todo/todo.md`)
- Jekyll content files that use Jekyll's own frontmatter schema (`content/_**/`)

---

## Required Fields

Every document should have at minimum:

```yaml
---
title: Document Title
type: lesson | discussion | reading | assignment | skill | protocol | reference | wiki | project | notes
date: YYYY-MM-DD
keywords:
  - keyword-one
  - keyword-two
  - keyword-three
---
```

### Field Definitions

| Field | Required | Description |
|---|---|---|
| `title` | Yes | Human-readable title. Match the H1 heading if one exists. |
| `type` | Yes | Document category. Use the closest match from the list above; propose new types to the user if none fit. |
| `date` | Yes | Content date — when the document was created or when the event occurred. ISO format. |
| `keywords` | Yes | 3–7 terms describing what the document is substantively about. See guidelines below. |
| `track` | Conditional | `theory`, `aural-skills`, or `piano`. Required for content-facing documents and project specs that target a specific track. Omit for track-agnostic infrastructure. |
| `file_type` | Conditional | `lesson`, `discussion`, `reading`, or `assignment`. Required for chapter content files. Omit for agent/infrastructure documents. |
| `status` | Conditional | Required for workspace project specs: `draft`, `active`, `review`, `complete`. |
| `completion_date` | Conditional | Required for workspace documents with a deadline. |
| `source` | Optional | Where the content came from. Required for reference files. |

### Additional Fields by Context

**Reference files** (`agent/reference/`): also require `last-updated`, `updated-by`, `source`, and `source-date` where applicable.

**Wiki documents** (`wiki/`): may include `last-reviewed` for documents that need periodic accuracy checks.

**The agent should think about what additional metadata would be useful.** A chapter content project might benefit from `chapters-affected` or `scope`. The core fields above are universal; additional fields are project-specific and should be proposed to the user when first encountered.

---

## Keyword Guidelines

Keywords power the relation scan's ability to find meaningful connections between documents. Good keywords make the graph useful; bad keywords add noise.

### What Makes a Good Keyword

- **Substantive concepts**, not structural labels — not "summary," "notes," "overview"
- **Specific enough** to connect related documents — not "music" in a music theory repo where everything is about music
- **People, topics, pedagogical concepts, or technical systems** that the document is *about*
- **Consistent with existing terms** — reuse keywords already used elsewhere in the repo rather than inventing synonyms

### Format

- Lowercase, hyphenated slugs: `harmonic-function`, `voice-leading`, `post-tonal`
- People as keywords use their name: `sean-butterfield`, `miranda-wilson`
- Use the canonical name for concepts, not abbreviations: `secondary-dominants` not `sec-dom`

### How Many

3–7 per document. Fewer for tightly focused documents, more for documents that touch multiple topics. If you can't identify at least 3 meaningful keywords, the document may be too generic or too short to benefit — use your judgment, but don't pad with weak terms.

### When to Update

- **On creation:** generate initial keywords from the content
- **On substantive edit:** review whether existing keywords still capture the document's scope; add or remove as needed
- **On archive:** final keyword review — last chance to ensure the document is discoverable via the relation scan

### Examples

Chapter project spec:
```yaml
keywords:
  - post-tonal
  - set-theory
  - chapter-rewrite
  - pedagogy
```

Wiki document about site architecture:
```yaml
keywords:
  - jekyll
  - multi-track
  - collections-dir
  - site-infrastructure
```

Workspace project:
```yaml
keywords:
  - style-revision
  - prose-voice
  - chapters-1-8
```

---

## Backfill Process

When the user requests a frontmatter backfill on existing documents:

1. **Assess scope** — count documents needing updates by location (workspace, agent, wiki). Report the count.
2. **Propose a batch plan** — group by directory or document type. Don't attempt everything in one session.
3. **For each document:** read the content, generate frontmatter following the rules above, write it. If the document already has partial frontmatter, merge — don't overwrite existing valid fields.
4. **After each batch:** commit with a descriptive message (e.g., "Add frontmatter to wiki/ (4 files)").
5. **Track progress** — add a todo item or update an existing one so the next session knows what's been done.

---

## Merging with Existing Frontmatter

Many documents already have partial frontmatter. When updating:

- **Keep** existing valid fields — don't overwrite `title`, `date`, `status`, etc. if they're already correct
- **Add** missing required fields (`keywords`, `type` if absent)
- **Fix** incorrect fields only if clearly wrong (e.g., `date` doesn't match the document's actual content date)
- **Remove** deprecated or meaningless fields only if the user has approved cleanup of that field type

---

## Quality Check

After adding or updating frontmatter, verify:
- `title` matches the H1 heading (or is a reasonable title if no H1 exists)
- `date` is accurate — sourced from content, not from when you're editing
- `type` is the closest match from the standard list
- `track` and `file_type` are set correctly for content-facing documents
- Keywords are substantive and specific to this document's content
- No duplicate keywords
- Keywords are consistent with terms used in related documents
