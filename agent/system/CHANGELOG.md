# Agent System — Changelog

## 2026-05-27

- **Created integrity-scan.py** — structural health check that runs every open session. Checks: expected file structure, broken markdown/backtick-path references, stale workspace files, compaction candidates, todo format compliance, confidential gitignore patterns. Uses only Python stdlib. Reports to `agent/system/integrity-reports/`.
