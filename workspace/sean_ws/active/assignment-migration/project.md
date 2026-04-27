# Migrate Google Drive Assignments into Repo

**Status:** Not started
**Priority:** P4
**Target:** Summer 2026

## Goal

All assignments and answer keys currently live in Google Drive. Move them into a structured, machine-readable format in the repo.

## Open Questions

- What format are the current assignments in (Docs, PDFs, sheets)?
- Difficulty granular (1-5) or categorical?
- Pool size per topic?

## Steps

- [ ] Audit the Google Drive — inventory assignments, answer keys, topic/chapter coverage
- [ ] Design the data format (Markdown + YAML frontmatter: topic tags, difficulty, chapter, semester, answer key ref)
- [ ] Migrate assignments into that format
- [ ] Tag each: topic(s), difficulty, chapter alignment, prerequisites
- [ ] Store answer keys securely (not public; available to instructor)
