# Jekyll Site Structure

## Overview

The site uses Jekyll (GitHub Pages, v3.9+) with a theme adapted from Lanyon by Evan Williamson. Content is organized as Jekyll collections — each chapter is its own collection.

## Collections

All collection directories live in `content/` (set via `collections_dir: content` in `_config.yml`). Each collection is defined in `_config.yml` with `output: true` and a display `name`.

Current theory collections: `_01-pitches-clefs` through `_22-intro-to-post-tonal`, plus inactive `_assignments` and `_final-project`.

Future tracks will add collections with prefixed names:
- Aural Skills: `_as-01-...`
- Piano: `_pn-01-...`

## URL Generation

Jekyll generates URLs by stripping the `_` prefix from the collection directory name. The `collections_dir` path is also stripped — so `content/_01-pitches-clefs/a1-pitchesclefs.md` generates the URL `/inttheory/01-pitches-clefs/a1-pitchesclefs.html`.

## Navigation

The sidebar (`_includes/sidebar.html`) auto-generates the chapter list by iterating `site.collections`. It filters out `posts`, `assignments`, and `final-project`. No `_data/` nav config is needed for the current single-track setup.

## Layouts

- `chapter.html` — primary layout for all chapter content. Implements prev/next navigation by iterating collection docs.
- `default.html` — base layout
- `page.html`, `post.html`, `forum.html` — secondary layouts

## Key Includes

- `abc-example.html` — renders ABC notation with playback
- `sidebar.html` — chapter navigation
- `head.html` — conditionally loads ABC JS/CSS when `page.abc` is true

## Assets

`assets/`, `images/`, `forum/`, `search/` stay at the repo root. All content references use `{{ site.baseurl }}/images/...` or `{{ site.baseurl }}/assets/...`.
