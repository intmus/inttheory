# Integrated Musicianship — Project TODO

Last updated: 2026-04-23

Organized by task **type**, not timeline. Each item carries its own target window. This lets the personal-assistant repo query and grab items without sections duplicating work.

**Priority legend:** P0 = blocker / immediate · P1 = high / current quarter · P2 = normal / this year · P3 = backlog / when possible

---

## Completed

- [x] Internal content audit across all 22 chapters (`docs/topic-index.md`)
- [x] Style and voice analysis — early vs. late chapters
- [x] Discussion vs. Lesson file authority assessment
- [x] Project CLAUDE.md for AI-assisted editing
- [x] Writing and style guide (`docs/style-guide.md`)
- [x] Four-layer memory framework (long-term, short-term, todo, toshare)

---

## Meta / Project Management

### M1. Adopt agent harness structure from personal-assistant repo — P0, target: 2026-05
Bring the agent harness architecture from the personal-assistant repo into this project. This includes the TODO format/shorthand, directory structure, cross-repo linking, and any conventions that make the repos work together under a unified agentic workflow.

- [ ] Review the personal-assistant repo's current harness structure and conventions
- [ ] Adapt and apply the structure to this repo (directory layout, file formats, naming)
- [ ] Migrate the TODO list to the agreed format (stable IDs, tags, priority, target window, status)
- [ ] Document the format at the top of this file so future additions follow it
- [ ] Establish the cross-repo linking pattern (see `toshare/registry.md`) so agents in either repo can read from this TODO
- [ ] Reconcile any conflicts between the existing four-layer memory framework and the harness structure

**Why this is P0:** Everything else in this repo benefits from a shared harness — consistent conventions, cross-repo visibility, and agent-ready task definitions. Do this before summer content work begins.

---

## Content to Create or Edit

### C1. Rewrite and reorganize Unit 22 — Intro to Post-Tonal — P1, target: summer 2026
Restructure Chapter 22's treatment of normal form and prime form around a clear conceptual hierarchy and a comparison-driven workflow.

**Pedagogical spine:**
1. **Establish the hierarchy: pitch → pitch class → pitch-class set**
   - Start from what students already know (pitches with octave designations)
   - Introduce pitch class as the abstraction that collapses octave
   - Build pitch-class set as a collection of pitch classes — unordered by default
2. **Drive the lesson via comparison of two unordered sets**
   - Present students with two unordered pc sets and ask: *are these the same?*
   - Use this question to motivate every subsequent step
3. **Progress through the analytical stages, in order, as tools for the comparison**
   - **Ordered set** — put the pcs in order so we can look at them the same way
   - **Normal form** — find the most compact rotation; recognizes transpositional equivalence
   - **Prime form** — final abstraction; shows equivalence under transposition *and* inversion

**Files affected:** `_22-intro-to-post-tonal/a1-ex-pcintnotation.md`, `b1-ex-mod12transnormform.md`, `c1-ex-normalform.md`, `d1-ex-mod12inversion.md`, `e1-ex-primeform.md`, and corresponding `-tx-` Discussion files.

- [ ] Audit current state of Chapter 22 Lesson and Discussion files
- [ ] Draft the revised sequence following the spine above
- [ ] Rewrite Lesson files to follow the comparison-driven flow
- [ ] Preserve discovery-based pedagogy — students derive each stage from the comparison problem
- [ ] Update Discussion files to match
- [ ] Verify ABC examples align with the new sequence

### C2. Grand Unified Theory of Harmonic Function — P1, target: summer 2026
Write a new chapter or framework that crystallizes how primary diatonic functions (tonic, dominant, pre-dominant) connect to and are extended by secondary function, tertiary function, sequences, mediant harmony, mode mixture, chromatic chords, and extended tertian harmonies.

- [ ] Outline the unified analytical lens — single framework showing all concepts growing from shared voice-leading and functional principles
- [ ] Draft the chapter (or cross-chapter framework document)
- [ ] Cross-reference where existing chapters introduce each piece
- [ ] Test pedagogical flow against the discovery-based approach
- [ ] Consider using the overtone series lesson (2e) as a foundation

### C3. Style and voice revision — early chapters (1-8) — P1, target: summer 2026
Edit chapters 1-8 so the prose matches the voice of chapters 14-22. Do not revise the teaching method — the discovery/puzzle-solving pedagogy is the core identity of those chapters.

- [ ] Revise Lesson (`-ex-` / `a1-`, `b1-`) files first
- [ ] Shorten paragraphs (1-3 sentences typical)
- [ ] Break compound-complex sentences into short declarative ones
- [ ] Preserve "Happy Birthday," Bobby McFerrin, and Snarky Puppy hooks
- [ ] Discussion files are lower priority for style work

### C4. Fill Chapter 13 content gaps (Phrasing and Texture) — P1, target: summer 2026
Biggest content hole in the theory text — Lesson files are mostly empty placeholders.

- [ ] Draft Lesson prose for each topic in Chapter 13
- [ ] Align with Discussion file content where it exists
- [ ] Fix the double-extension file `d2-tx-mustexture.md.md` as part of this work

### C5. Fill uneven Lesson prose in Chapters 14-22 — P2, target: summer-fall 2026
Many Lesson files are empty or contain only ABC examples; Discussion files currently carry most of the instructional weight. Full-prose exceptions already exist for 14a, 16a, 19a.

- [ ] Inventory which Lesson files need prose vs. which are intentionally example-only
- [ ] Decide per chapter: write full Lesson prose or restructure the chapter format
- [ ] Prioritize chapters students struggle most with

### C6. Import and incorporate Integrated Aural Skills — P2, target: summer-fall 2026
Dr. Wilson originally co-authored *Integrated Aural Skills* as a companion to *Integrated Theory*. She has since moved to music history; the text now lives on Pressbooks, not in this repo.

- [ ] Locate and audit the Pressbooks version
- [ ] Compare against any content remaining in the original repo
- [ ] Decide structure: parallel chapters? interleaved? separate collection?
- [ ] Convert from Pressbooks format to Jekyll/Markdown
- [ ] Align aural skills topics with theory chapters
- [ ] Edit for voice/style consistency with theory text
- [ ] Review for accuracy — different editorial chain
- [ ] Credit Dr. Wilson appropriately throughout

**Open questions:** What is the Pressbooks URL? 1:1 mapping to theory chapters, or independent sequence? Same navigation or separate track?

### C7. Draft Integrated Piano curriculum — P3, target: 2027+
Future third track covering the Class Piano cycle. Not active; plan ahead so infrastructure supports it.

- [ ] Define scope — which semesters of Class Piano to cover
- [ ] Determine relationship to theory and aural skills sequences
- [ ] Draft initial content outline

---

## Content QA and Proofreading

### Q1. Full proofread of theory text — P1, target: summer 2026
- [ ] Spelling, grammar, factual errors across all chapters
- [ ] Focus on Discussion files (student-managed, more errors expected)
- [ ] Consistency of notation (superscript formatting, solfege spelling, Roman numeral style)
- [ ] Verify ABC notation examples render correctly
- [ ] Check for broken links and missing images

### Q2. Fix known Discussion file spelling errors — P2, target: summer 2026
Errors observed during audit: "becuase," "plut," "errros," "Accpetable," "sround," "bottomm," "reslve," "quailty," "nubmer," "parantheses," "Undordered," "intergers," "equivilants," "refurring," "relatd," "likey," "modualtory," "explanantion"

- [ ] Global spellcheck pass across all `-tx-` / `a2-` / `b2-` files
- [ ] Batch-fix confirmed errors; flag anything ambiguous

### Q3. Fix filename and title bugs — P1, target: 2026-05
- [ ] `_02-int-scales-keys/b2- modesandpentatonics.md` — remove leading space in filename
- [ ] `_13-phrasing-texture/d2-tx-mustexture.md.md` — remove double extension
- [ ] Chapter 2b Discussion title: "Pentonic" → "Pentatonic"

### Q4. Standardize file naming convention — P3, target: 2027
Chapters 1-12 use `a1-`/`a2-` without descriptive suffixes; chapters 13+ use `-ex-`/`-tx-`. Decide whether to standardize across the whole book. See `docs/lesson-naming.md`.

### Q5. Verify multimedia embeds — P2, target: summer 2026
- [ ] Check Spotify and Vimeo embeds in Discussion files (may have broken over time)
- [ ] Investigate ABC examples flagged with "Playback does not work" notes

---

## Site and Infrastructure

### I1. Website modernization — P1, target: summer 2026
Update the Jekyll site with a modern look/theme. Currently Lanyon-based.

- [ ] Evaluate: stay with Jekyll or switch stacks
- [ ] Select or design theme
- [ ] Ensure the new architecture supports three tracks (Theory, Aural Skills, Piano) without overwhelming navigation

### I2. Assignment distribution and discussion system — P1, target: summer 2026, launch fall 2026
Replace current Discord system with an integrated assignment/discussion layer on the site.

- [ ] Post assignments with due dates
- [ ] Simple discussion board below each assignment
- [ ] **User anonymity:** first name only, no full names or email
- [ ] **Simple password system:** each section gets a password; only registered students view/participate
- [ ] Decide: static-only vs. lightweight backend (Firebase, Supabase)

### I3. Flexible curriculum reordering system — P2, target: 2026-2027
Support reordering topics into different institutional layouts (2-semester, 3-semester, custom) without rewriting content.

- [ ] Design a curriculum mapping layer (config file defining order + grouping, independent of file structure)
- [ ] Ensure `docs/topic-index.md` and topic tagging are robust enough for reordering
- [ ] Build navigation that reads from the curriculum map, not file order
- [ ] Test with current 2-semester and draft 3-semester layouts
- [ ] Extend to Aural Skills and Piano once those tracks exist

### I4. OER fork-and-customize tool — P3, target: 2027
Agentic workflow letting adopting instructors provide a syllabus and get a custom curriculum config.

- [ ] Define "customization" scope — reorder? hide topics? merge chapters?
- [ ] Design config format (human-editable + machine-readable)
- [ ] Spec the agent workflow: syllabus → topic mapping → config → rebuilt site
- [ ] Document the fork-and-customize process for adopters
- [ ] Decide how upstream content updates merge into customized forks

---

## Assignment Management

### A1. Migrate Google Drive assignments into the repo — P1, target: summer 2026
All assignments and answer keys currently live in Google Drive. Move them into a structured, machine-readable format in the repo.

- [ ] Audit the Google Drive — inventory assignments, answer keys, topic/chapter coverage
- [ ] Design the data format (Markdown + YAML frontmatter: topic tags, difficulty, chapter, semester, answer key ref)
- [ ] Migrate assignments into that format
- [ ] Tag each: topic(s), difficulty, chapter alignment, prerequisites
- [ ] Store answer keys securely (not public; available to instructor)

**Open questions:** What format are the current assignments in (Docs, PDFs, sheets)? Difficulty granular (1-5) or categorical? Pool size per topic?

### A2. Build assignment rotation system — P2, target: summer-fall 2026
Depends on A1 and I2. A pool of tagged assignments shuffled year-to-year so pages build themselves.

- [ ] Design the rotation logic (tags in, assignment set out)
- [ ] Integrate with assignment/discussion pages from I2
- [ ] Test with a single chapter's pool before scaling

---

## Notes

- **Integrated Musicianship** is the umbrella name: Theory, Aural Skills, and (eventually) Piano
- Lesson files are **authoritative** — written and maintained by Sean Butterfield over six years
- Discussion files are collaborative lecture notes curated by student assistants — useful for pedagogy, may contain errors
- The textbook was written in chapter order over one year; later chapters represent the preferred writing style
- The puzzle-solving/discovery pedagogical approach from early chapters must be preserved even as prose style is updated
- Dr. Wilson is the original author of Integrated Aural Skills and must be credited in all reincorporated content
- Strong hooks to preserve in early chapters: "Happy Birthday" vehicle, Bobby McFerrin video, Snarky Puppy case study
- Overtone series lesson (2e) is a strong candidate foundation for the Grand Unified Theory chapter (C2)
- "Function over Form" thread across Chapter 11 is a motif worth extending into chromatic chapters
- Some Discussion files contain HTML teaching comments revealing in-class strategies — mine these during style revision (C3)
