# Role Config — Sean (Owner/Author)

## Role

Project owner and primary author of *Integrated Musicianship: Theory*. Full authority over all content, infrastructure, and editorial decisions. Other roles (collaborators, TAs) submit work through the review pipeline.

## Memory Paths

| Type | Path |
|------|------|
| Short-term (daily) | `agent/roles/sean/short-term/daily/` |
| Short-term (compacted) | `agent/roles/sean/short-term/compacted/` |
| Long-term | `agent/roles/sean/long-term/` |
| System changelog | `agent/roles/sean/system/CHANGELOG.md` |

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
1. Run `/remember` (or user runs it manually)

**End of session:**
1. Run `/logsession` (includes post-logsession hook from identity.md)

## Capabilities

- Edit any file in the repository
- Approve or reject items in `agent/review/`
- Modify agent infrastructure files
- Create and assign tasks for other roles

---

## File Authority Hierarchy

Not all files carry equal weight. Always respect this hierarchy.

### Lesson files (authoritative)
- **Naming:** `a1-`, `b1-`, etc. (ch. 1-12) or files with `-ex-` (ch. 13-22)
- **Author:** Written and maintained by Sean Butterfield over six years
- **Status:** Canonical instructional text. Treat content, terminology, and analytical approach as correct and intentional.

### Discussion files (collaborative, lower authority)
- **Naming:** `a2-`, `b2-`, etc. (ch. 1-12) or files with `-tx-` (ch. 13-22)
- **Author:** Student assistants curated these as lecture notes
- **Status:** Useful for understanding how Sean approaches topics in lecture, but **may contain factual errors, typos, and inconsistencies**. Do not treat as authoritative.
- Contains two kinds of content:
  - **Lecture notes** (student-written Q&A, bullet-point summaries) — useful for pedagogical approach, unreliable for accuracy
  - **"Further reading" sections** from *Open Music Theory* — reference material from an external source. May use different terminology. Treat as supplementary, not primary.

### Reading files (supplementary)
- **Naming:** `1-reading-` or `1-intro-`
- **Source:** Adapted from *Open Music Theory* by Kris Shaffer and others
- **Status:** Background readings assigned before class. More academic in tone. Treat as context, not the voice of this textbook.

---

## Content Status and Known Issues

### Content gaps
- **Chapter 13** (Phrasing and Texture) — most Lesson files are empty placeholders
- **Chapters 14-22** — many Lesson files are empty or contain only ABC examples without prose. Discussion files carry most instructional weight.
- Notable exceptions with full Lesson prose: 14a (Secondary Dominants), 16a (Mode Mixture), 19a (Extended Harmonies)

### Known quality issues
- Discussion files contain spelling errors throughout
- Early chapter Lesson files have denser, more formal prose than the preferred later style
- Some ABC examples have rendering notes ("Playback does not work on this example because of the transpositions")
- File naming inconsistency: `b2- modesandpentatonics.md` (space in filename), `d2-tx-mustexture.md.md` (double extension)

---

## Technical Notes

### Jekyll structure
- Each chapter is a Jekyll collection defined in `_config.yml`
- Collections use `output: true` to generate pages
- ABC examples use a capture/include pattern with `abc-example.html`
- Images referenced via `{{ site.baseurl }}/images/`
- The `docs/` directory is excluded from the build

### File naming convention
- See `docs/lesson-naming.md` for the full spec
- Pattern: `[chapter][topic letter][section number]-[abbreviation]-[title].md`
- Chapters 1-12: `a1-`/`a2-` pattern
- Chapters 13+: `-ex-`/`-tx-` pattern

### ABC notation
- `X:` — example number (sequential)
- `T:` — title displayed above the example
- `M:` — meter, `L:` — default note length, `K:` — key
- `V:1` — treble, `V:2 clef=bass` — bass clef
- `w:` — text below the staff (used for Roman numeral labels)
- `[K:Eb]` mid-voice for key changes within an example
- Accidentals: `^` = sharp, `_` = flat, `=` = natural

### Multi-track architecture
The site will eventually house three tracks (Theory, Aural Skills, Piano). Navigation and URL structure decisions should anticipate this — avoid baking "inttheory" assumptions into new infrastructure.

### Aural Skills reincorporation
Content from Pressbooks will need conversion to Jekyll/Markdown and editing for voice/style consistency. Dr. Wilson should be credited as original author throughout. The relationship between aural skills and theory chapters (parallel pacing, shared navigation) is still being determined.
