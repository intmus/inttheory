# Writing and Style Guide

This guide is the single source for voice, tone, formatting, pedagogy, and analytical conventions in *Integrated Musicianship: Theory*. All contributors follow these standards when writing new content or editing existing chapters.

---

## File Types and Voice

The textbook uses two main file types per topic, each with a distinct voice.

### Lesson files (`-ex-`)

These are the primary instructional text. They guide students through a concept using a **discovery-based approach**.

- Write in a polished but conversational textbook voice
- Use "we" and "you" consistently — never "I" except in rare editorial asides
- Set up musical examples *before* explaining them — let students work through the example first, then confirm findings in a `### Conclusion` section
- Connect every new concept to something previously learned ("In Unit 7, we discussed...")
- Use questions to guide thinking, not to quiz — frame them as invitations to explore
- Paragraphs can run 3-5 sentences when building an argument, but prefer shorter paragraphs for clarity

### Discussion files (`-tx-`)

These are class discussion notes — closer to a live lecture capture.

- Voice is more casual and direct
- Use **bold-quoted questions** as structural anchors (e.g., `**"Can you tonicize any chord?"**`)
- Bullet points are the primary organizational tool — sub-bullets for elaboration
- Student observations and instructor responses can blend together naturally
- Year-labeled sections (e.g., `# Class discussion 2022`) separate different semesters' notes
- Humor, personality, and informality are welcome here ("the Romantic period was really crazy", "hip alert!")

---

## The Target Voice

The later chapters (14-22) represent the mature writing style to emulate. Key characteristics:

- Short, declarative sentences — rarely over 25 words
- Break complex ideas into multiple short sentences rather than compound-complex clauses
- Paragraphs are concise — 1-3 sentences typical
- Dashes and colons for elaboration rather than subordinate clauses

### What the early chapters (1-8) do well — preserve this

- **Discovery-based pedagogy:** Students examine examples and derive rules *before* seeing conclusions. The pattern is: context → example → guiding questions → `### Conclusion` section. This is the core pedagogical identity of the textbook.
- **"Happy Birthday" as recurring vehicle** (chapters 2-3) — accessible, universally known
- **Bobby McFerrin video, Snarky Puppy case study** — engaging hooks worth keeping
- **Multiple pathways to understanding:** solfege, scale degrees, letter names, interval relationships
- **Step-by-step recipes** for processes
- **Explicit warnings** about what NOT to do

### What the early chapters need — revise this

- Longer, denser paragraphs in chapters 1-4 — need to be broken up
- Some passages are more formal/stiff than the later conversational tone
- Occasional over-explanation where a shorter statement would suffice

---

## Tone and Voice

- **Conversational and direct** — knowledgeable but never pretentious
- **Candid about difficulty** — openly acknowledge when something is confusing, complex, or unusual ("This ex is weird because where we hear the modulation is really ambiguous")
- **Encouraging but honest** — don't soften bad news or over-qualify statements
- **Occasional dry humor** is welcome; forced humor is not
- Use exclamation marks sparingly and only for genuine emphasis or warnings

---

## Section Headers

- **Alliterative or punchy short headers** for Discussion file topic sections: "Secondary Secrets," "Leading-tone Liaison," "Mixing it Up," "Modulatory Madness," "Extension Convention," "Sequential Essentials," "Death of Tonality," "Optimus"
- These headers should be creative and memorable — they serve as mnemonics
- Use standard descriptive headers (## and ###) for subtopics and organizational structure within those sections
- Lesson files use more straightforward descriptive headers

---

## Formatting Conventions

### Text Formatting

- **Bold** for:
  - Key terms on first use
  - Critical rules and important warnings
  - Question prompts in Discussion files (bold + quotes)
  - Emphasis on things students must remember
- *Italics* for:
  - Technical terminology (e.g., *tonicization*, *antecedent*, *contrasting idea*)
  - Titles of works and publications (e.g., *The Girl from Ipanema*, *Open Music Theory*)
  - Light emphasis within sentences
  - Solfege syllables when used inline (e.g., *do*, *re*, *mi*)
- Use dashes and colons for elaboration rather than subordinate clauses

### Lists

- Bullet points are the primary organizational tool — use sub-bullets for elaboration
- Numbered lists are reserved for **sequential/step-by-step processes** only (e.g., "Steps for Building an Augmented sixth chord in any key")
- Keep bullet points concise — one idea per bullet

### Tables

Use Markdown tables for side-by-side comparisons (e.g., parallel major/minor chord charts, Roman numeral notation rules). Format:

```markdown
Column 1 | Column 2 | Column 3
 --- | --- | ---
 data | data | data
```

---

## Music Notation Conventions

### Chord Symbols and Roman Numerals

- Use HTML `<sup>` tags for superscript in chord symbols and figured bass:
  - `V<sup>7</sup>` renders as V<sup>7</sup>
  - `vii<sup>o</sup>` renders as vii<sup>o</sup>
  - `vii<sup>o7</sup>` renders as vii<sup>o7</sup>
  - `Ger<sup>+6</sup>` renders as Ger<sup>+6</sup>
  - `V<sup>7(add9)</sup>` for extended harmonies
- Secondary function chords use a slash: `V/V`, `V<sup>7</sup>/V`
- Leadsheet symbols use plain text: `G7`, `Fmaj7`, `Gmaj<sup>9</sup>`
- Inversion figures attach to the Roman numeral *before* the slash in secondary function chords
- Cadential 6/4 labeled as **I<sup>6/4</sup>** (not V<sup>6/4-5/3</sup>)

### Solfege

- Use lowercase solfege syllables: do, re, mi, fa, sol, la, ti
- Use chromatic solfege: fi, si, le, te, ra, me
- Bold solfege when introducing it as a key reference point: **Le**, **Fi**, **So**
- Solfege and scale degree numbers are interchangeable frameworks — offer both when introducing a concept

### Scale Degrees

- Use caret notation in prose: ^6, ^3, ^7
- Use `b` or `#` prefixes for altered scale degrees: b6, #4
- Spell out "sixth scale degree" in running prose when clarity demands it

### Non-Chord Tone Abbreviations

pt, dpt, nt, sus, RET, NG, APP, ET, ANT, PED, INT, ING/ENC

### ABC Notation Examples

Musical examples use ABC notation rendered through Jekyll includes:

```
{% raw %}{% capture ex1 %}X:1
T:Example title
M:4/4
L:1/2
K:C
V:1
[notes]
V:2 clef=bass
[notes]
w:C:I vi ii V I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}{% endraw %}
```

- Number examples sequentially within each file
- Always include a title (`T:` field)
- Include Roman numeral analysis in the `w:` (words) field when relevant
- Use `V:1` and `V:2 clef=bass` for treble and bass clef voices
- Use `[K:Eb]` mid-voice for key changes within an example
- Accidentals: `^` = sharp, `_` = flat, `=` = natural

### Images and Media

- Use Jekyll `{{ site.baseurl }}` for image paths
- Wrap images in `<figure>` tags with `<figcaption>` when attribution is needed
- Spotify/Vimeo embeds use standard `<iframe>` tags

---

## Pedagogical Principles

These are non-negotiable — preserve them in all content.

### 1. Lead with "how," then explain "why"

Introduce concepts by showing students what to *do* before explaining the theory behind it. Walk through the process, then explain the reasoning.

### 2. Connect to prior knowledge

Every new concept should reference something the student already knows. Explicitly name the unit or concept you're building on.

### 3. Discovery before declaration

Students work through examples before being told the rules. The pattern: context → example → guiding questions → `### Conclusion` section. This is the core pedagogical identity of the textbook.

### 4. Multiple mental models

Provide different frameworks for the same concept — solfege, scale degree numbers, letter names, interval relationships. Different students will latch onto different frameworks.

### 5. Step-by-step recipes

When teaching a process (building a chord, finding normal form, analyzing a progression), present it as a numbered, followable recipe.

### 6. Explicit warnings

Be direct about what NOT to do. Common mistakes get their own bullet points or bold warnings:
- "**Do not** tonicize ii<sup>o</sup> in minor or vii<sup>o</sup> ever."
- "**Don't** double the root, and instead double the third."

### 7. K.I.S.S.

When a chord or passage could be analyzed multiple ways, prefer the simpler explanation. Only label something as secondary function if diatonic analysis doesn't work.

### 8. Function over form

Roman numerals describe function, not just chord identity. This thread runs through Chapter 11 and should extend into all chromatic chapters.

---

## Analytical Framework and Terminology

Sean's analytical approach has specific conventions. Use these consistently.

### Harmonic function

- Three tiers: **primary** (tonic, dominant, pre-dominant), **secondary** (tonicization), **tertiary** (cadential, passing, pedal, arpeggiated)
- Progression flowchart: iii → vi → ii → V → I (with IV and vii as substitutions)
- IV = rootless ii<sup>7</sup>; vii<sup>o</sup> = rootless V<sup>7</sup>
- Voice-leading rules based on **chordal members** (third resolves up to root; seventh resolves down to third), not scale degrees

### Specific terminology preferences

- "Pre-dominant" (hyphenated), not "predominant"
- "Chordal third," "chordal fifth," "chordal seventh" — to distinguish from intervals and scale degrees
- "Tonicization" for brief secondary function; "modulation" for key change with cadential confirmation
- "Frustrated leading tone" — inner-voice leading tone that skips down to the fifth of tonic
- "Functional substitution" — vi replacing I in deceptive cadences (I<sup>sub6</sup>)
- Cadential 6/4 labeled as **I<sup>6/4</sup>** (not V<sup>6/4-5/3</sup>)

### What can and cannot be tonicized

- Any major or minor triad can be tonicized
- Diminished triads (vii<sup>o</sup> in major/minor, ii<sup>o</sup> in minor) should NOT be tonicized

---

## Structural Patterns

### Lesson files follow a discovery arc

1. Brief context connecting to prior knowledge
2. Musical example for the student to analyze (with guiding questions)
3. `### Conclusion` section confirming the findings
4. Expansion or complication of the concept
5. Additional examples building complexity

### Discussion files follow a Q&A pattern

1. Punchy alliterative section header
2. Bold-quoted questions from class
3. Bulleted answers/discussion points
4. Practical tips, mnemonics, and warnings

### Further Reading sections

Some files include a `# Further reading` section with content from *Open Music Theory*. These are more formal and academic in tone — that's expected, since they come from a different source. Clearly label them with `## From *Open Music Theory*`.

---

## Common Pitfalls to Avoid

- **Academic stiffness** — this is a conversational textbook, not a journal article
- **Hedging and over-qualification** — say it directly
- **Long unbroken prose blocks** — break them up with headers, bullets, or examples
- **Burying the point in preamble** — lead with the concept
- **Inconsistent notation** — always use `<sup>` for figured bass and chord quality symbols
- **Forgetting to connect concepts** — every new topic should reference where it fits in the larger curriculum
