# Multi-Track Architecture

## Design

The Integrated Musicianship suite will serve three tracks from a single repo:

| Track | Prefix | Status |
|-------|--------|--------|
| Theory | *(none — existing names)* | Active, 22 chapters |
| Aural Skills | `as-` | Planned import from Pressbooks |
| Piano | `pn-` | Future |

All tracks' collections live in `content/` under `collections_dir: content`. Theory collections keep their current names to preserve existing URLs.

## Cross-Track Navigation

A `_data/track-map.yml` file will map parallel topics between tracks. For example, secondary dominants in Theory (ch. 14) maps to the corresponding Aural Skills ear training chapter.

The sidebar will be extended with a track switcher — a button or tab that takes the student from their current topic in one track to the equivalent section in another. The `track-map.yml` alignment data drives this.

## Naming Convention

- Theory: `_01-pitches-clefs` through `_22-intro-to-post-tonal` (no change)
- Aural Skills: `_as-01-[topic]`, `_as-02-[topic]`, etc.
- Piano: `_pn-01-[topic]`, `_pn-02-[topic]`, etc.

The sidebar template will filter collections by prefix to group them by track.

## Repo Rename (Deferred)

The repo is currently `intmus/inttheory` served at `intmus.github.io/inttheory`. Renaming to `intmusicianship` would change the GitHub Pages URL and break all existing links. This is deferred until the full website overhaul, when proper redirects can be coordinated.
