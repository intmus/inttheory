---
skill: Relation Scan
roles: [sean]
templates: []
last-updated: 2026-05-12
updated-by: sean
---

# Relation Scan

Run a document relationship scan across the repo's markdown files to surface connections, orphans, and drift candidates.

## When to use

- Periodic maintenance (biweekly recommended)
- After large content additions or reorganizations
- When looking for related topics across chapters or tracks

## Context

The scan builds a graph of connections based on frontmatter keywords, headers, bold terms, and people mentions. It requires keyword frontmatter on chapter files to be most effective — without keywords, it can only infer connections from headers and bold terms.

## Steps

1. Verify Python 3.10+ is available with `networkx` and `pyyaml`
2. Run the scan:
   ```bash
   python agent/extractors/relation-scan.py
   ```
3. Review the output report for:
   - **Orphaned files** — documents no index points to
   - **Index gaps** — index entries pointing to files that don't exist
   - **Entity clusters** — groups of documents sharing topics
   - **Drift candidates** — document pairs discussing the same thing but far apart in time
4. Surface findings to the user for action

## Required inputs

- `agent/extractors/relation-scan-config.yaml` must be configured
- Chapter files should have `keywords` in frontmatter for best results

## Outputs

- Markdown report in the terminal
- Optional: `--viz` flag generates an interactive HTML visualization
