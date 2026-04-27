# Plan: Reorganize Chapter Directories with `collections_dir`

## Problem

The repo root currently has 22 chapter directories (`_01-pitches-clefs` through `_22-intro-to-post-tonal`), plus `_assignments` and `_final-project`. That's 24 collection directories mixed in with Jekyll infrastructure, site pages, and agent files. When aural skills content arrives, it could add another 20+ collection directories, making the root unmanageable.

## Solution

Jekyll's `collections_dir` config option lets you move all collections into a single parent directory. One line in `_config.yml`, one folder move.

### Current root (abbreviated)

```
inttheory/
├── _01-pitches-clefs/
├── _02-int-scales-keys/
├── ... (20 more chapter dirs)
├── _assignments/
├── _final-project/
├── _includes/
├── _layouts/
├── _sass/
├── _config.yml
├── agent/
├── docs/
├── todo/
├── workspace/
├── assets/
├── images/
├── index.md
└── ... (other site pages and files)
```

### Proposed root

```
inttheory/
├── content/
│   ├── _01-pitches-clefs/
│   ├── _02-int-scales-keys/
│   ├── ... (20 more chapter dirs)
│   ├── _assignments/
│   └── _final-project/
├── _includes/
├── _layouts/
├── _sass/
├── _config.yml
├── agent/
├── docs/
├── todo/
├── workspace/
├── assets/
├── images/
├── index.md
└── ... (other site pages and files)
```

When aural skills arrives, it gets its own collections inside `content/`:

```
content/
├── _01-pitches-clefs/          ← theory
├── ...
├── _22-intro-to-post-tonal/    ← theory
├── _as-01-rhythm/              ← aural skills (naming TBD)
├── _as-02-melody/              ← aural skills
├── _assignments/
└── _final-project/
```

Alternatively, if Jekyll allows nested `collections_dir` or if we switch to a different naming convention, theory and aural skills collections could be more clearly separated. That decision depends on the navigation/URL structure chosen during the redesign.

## Config Change

In `_config.yml`, add one line:

```yaml
collections_dir: content
```

Jekyll will then look for all `_collection-name/` directories inside `content/` instead of at the root.

## What Moves

| Item | Action |
|------|--------|
| `_01-` through `_22-` (22 dirs) | Move into `content/` |
| `_assignments/` | Move into `content/` |
| `_final-project/` | Move into `content/` |
| `_includes/` | **Stays at root** — not a collection |
| `_layouts/` | **Stays at root** — not a collection |
| `_sass/` | **Stays at root** — not a collection |

## What Could Break

### Paths in layouts and includes
- `abc-example.html` and other includes may reference paths relative to the collection root
- Check all `{{ site.baseurl }}` and `{{ page.url }}` references

### URL generation
- By default, `collections_dir` should not change generated URLs — Jekyll strips the collections_dir from output paths
- Verify with a local build: `bundle exec jekyll serve`

### GitHub Pages compatibility
- `collections_dir` has been supported since Jekyll 3.7 (2018). GitHub Pages runs Jekyll 3.9+, so this should work. Verify before pushing.

### Hardcoded paths in content files
- Grep for any relative paths in chapter markdown files that assume they're at root
- Image references using `{{ site.baseurl }}/images/` should be unaffected since `images/` stays at root

## Verification Checklist

- [ ] Add `collections_dir: content` to `_config.yml`
- [ ] Create `content/` directory
- [ ] Move all 24 collection directories into `content/`
- [ ] Run `bundle exec jekyll serve` locally
- [ ] Spot-check: chapter pages render, ABC examples work, navigation intact
- [ ] Check URLs haven't changed (important for any existing links/bookmarks)
- [ ] Grep for broken relative paths across all moved files
- [ ] Push to a test branch and verify on GitHub Pages before merging
