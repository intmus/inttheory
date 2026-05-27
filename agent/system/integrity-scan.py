#!/usr/bin/env python3
"""
Integrated Musicianship ACP — Integrity Scan

Structural health check for the inttheory repo. Answers: "Is anything broken?"
Runs every open session. Uses only Python stdlib — no external dependencies.

Usage:
    python agent/system/integrity-scan.py [--out=<path>]

Exit codes:
    0 = clean or info-only
    1 = warn-level items found
    2 = block-level items found
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

BLOCK = "BLOCK"
WARN = "WARN"
INFO = "INFO"

# Multi-role structure: files and dirs expected to exist (relative to REPO_ROOT)
EXPECTED_STRUCTURE = [
    # Core agent infrastructure
    ("agent/protocols/core.md", BLOCK),
    ("agent/protocols/index.md", WARN),
    ("agent/reference/shorthand.md", WARN),
    ("agent/reference/style-guide.md", WARN),
    ("agent/reference/session-log.md", WARN),
    ("agent/skills/skill-index.md", WARN),
    ("agent/skills/document-frontmatter.md", WARN),
    ("agent/templates/index.md", WARN),
    ("agent/extractors/index.md", WARN),
    ("agent/toshare/registry.md", WARN),
    ("agent/system/CHANGELOG.md", WARN),
    # Sean's role
    ("agent/roles/sean/identity.md", BLOCK),
    ("agent/roles/sean/role-config.md", BLOCK),
    ("agent/roles/sean/short-term/daily", WARN),
    ("agent/roles/sean/short-term/compacted", WARN),
    ("agent/roles/sean/system/CHANGELOG.md", WARN),
    # Miranda's role
    ("agent/roles/miranda/identity.md", WARN),
    ("agent/roles/miranda/role-config.md", WARN),
    ("agent/roles/miranda/system/CHANGELOG.md", WARN),
    # Project-level files
    ("todo/todo.md", BLOCK),
    ("docs/topic-index.md", WARN),
    ("docs/lesson-naming.md", WARN),
    ("CLAUDE.md", BLOCK),
]

# Patterns to skip when checking markdown links (historical/generated content)
LINK_CHECK_SKIP_PATTERNS = [
    "/short-term/daily/",
    "/short-term/compacted/",
    "CHANGELOG.md",
    "relation-reports/",
    "integrity-reports/",
]

# Backtick path prefixes to check — matches this repo's directory layout
BACKTICK_PATH_PATTERN = re.compile(
    r"`((?:agent|workspace|todo|archive|wiki|docs|content|repeatable-processes)"
    r"/[^\s`]+\.(?:md|py|bat|sh|json|yaml|docx|xlsx))`"
)


def check_structure(report):
    """Verify expected files and directories exist."""
    for item, severity in EXPECTED_STRUCTURE:
        item_path = REPO_ROOT / item
        if not item_path.exists():
            report.append((severity, "Missing expected file/folder", item))


def check_broken_references(report):
    """Scan .md files for local file references and verify targets exist."""
    md_link_pattern = re.compile(r"\[[^\]]+\]\(([^):]+\.md)(?:#[^)]+)?\)")

    for md_file in REPO_ROOT.rglob("*.md"):
        rel = str(md_file.relative_to(REPO_ROOT)).replace("\\", "/")

        if any(skip in rel for skip in LINK_CHECK_SKIP_PATTERNS):
            continue
        if rel.startswith("_site/") or rel.startswith("vendor/"):
            continue

        try:
            content = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for match in md_link_pattern.finditer(content):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if _is_template_reference(target):
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                report.append((INFO, "Broken markdown link", f"{rel} -> {target}"))

        for match in BACKTICK_PATH_PATTERN.finditer(content):
            target = match.group(1)
            if _is_template_reference(target):
                continue
            target_path = REPO_ROOT / target
            if not target_path.exists():
                report.append((INFO, "Broken repo path reference", f"{rel} -> {target}"))


def _is_template_reference(path_str):
    """A path is a template reference if it contains placeholders."""
    return bool(
        re.search(r"\[[a-z][-a-z ]*\]", path_str, re.IGNORECASE)
        or re.search(r"YYYY|MM-DD|YYYY-MM", path_str)
        or "*" in path_str
    )


def check_workspace_stale(report):
    """Flag files in workspace active areas not modified in 30+ days."""
    active_dirs = [
        REPO_ROOT / "workspace" / "sean_ws" / "active",
        REPO_ROOT / "workspace" / "miranda_ws" / "active",
    ]
    today = datetime.date.today()
    stale_days = 30

    for active_dir in active_dirs:
        if not active_dir.exists():
            continue
        for item in active_dir.rglob("*"):
            if not item.is_file():
                continue
            if item.name == ".gitkeep":
                continue
            try:
                mtime = datetime.date.fromtimestamp(item.stat().st_mtime)
            except OSError:
                continue
            age = (today - mtime).days
            if age >= stale_days:
                rel = str(item.relative_to(REPO_ROOT)).replace("\\", "/")
                report.append((INFO, f"Stale workspace file ({age}d)", rel))


def check_compaction_candidates(report):
    """Flag daily logs older than 7 days that haven't been compacted."""
    today = datetime.date.today()
    threshold = today - datetime.timedelta(days=7)

    roles_dir = REPO_ROOT / "agent" / "roles"
    if not roles_dir.exists():
        return

    for role_dir in roles_dir.iterdir():
        if not role_dir.is_dir():
            continue
        daily_dir = role_dir / "short-term" / "daily"
        compacted_dir = role_dir / "short-term" / "compacted"

        if not daily_dir.exists():
            continue

        compacted_months = set()
        if compacted_dir.exists():
            for f in compacted_dir.iterdir():
                if f.suffix == ".md":
                    compacted_months.add(f.stem)

        for log_file in sorted(daily_dir.iterdir()):
            if log_file.suffix != ".md":
                continue
            try:
                log_date = datetime.date.fromisoformat(log_file.stem)
            except ValueError:
                continue
            if log_date >= threshold:
                continue
            rel = str(log_file.relative_to(REPO_ROOT)).replace("\\", "/")
            report.append((WARN, "Compaction candidate", rel))


def check_todo_format(report):
    """Check todo/todo.md for format compliance."""
    todo_path = REPO_ROOT / "todo" / "todo.md"
    if not todo_path.exists():
        return

    content = todo_path.read_text(encoding="utf-8", errors="ignore")

    for i, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()
        if not stripped.startswith("- [ ]"):
            continue
        if re.search(r"^\s*- \[ \]\s+\d+\.", stripped):
            continue
        if not re.search(r"\[P[1-6]\]", stripped):
            report.append((INFO, "Todo missing priority", f"todo/todo.md line {i}"))
        if re.search(r"\[by\s+\d{4}-\d{2}-\d{2}\]", stripped):
            if not re.search(r"\[by\s+\d{4}-\d{2}-\d{2}\]\s*\[P[1-6]\]", stripped):
                report.append((INFO, "Todo format: [by date] should precede [P#]",
                               f"todo/todo.md line {i}"))


def check_confidential_gitignore(report):
    """Verify role-specific confidential directories are gitignored."""
    gitignore = REPO_ROOT / ".gitignore"
    if not gitignore.exists():
        report.append((BLOCK, ".gitignore missing",
                       "Confidential workspace patterns cannot be enforced"))
        return
    content = gitignore.read_text(encoding="utf-8")

    expected_patterns = [
        "workspace/sean_ws/confidential/",
        "workspace/miranda_ws/confidential/",
    ]
    for pattern in expected_patterns:
        if pattern not in content:
            report.append((WARN, "Confidential gitignore pattern missing",
                           f".gitignore does not contain `{pattern}`"))


def write_report(report, out_path=None):
    today = datetime.date.today().isoformat()
    if out_path:
        report_path = Path(out_path)
        report_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        reports_dir = REPO_ROOT / "agent" / "system" / "integrity-reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = reports_dir / f"{today}.md"

    severity_order = {BLOCK: 0, WARN: 1, INFO: 2}
    report.sort(key=lambda r: (severity_order[r[0]], r[1]))

    counts = {BLOCK: 0, WARN: 0, INFO: 0}
    for sev, _, _ in report:
        counts[sev] += 1

    lines = [
        f"# Integrity Scan — {today}",
        "",
        f"Generated by `agent/system/integrity-scan.py`.",
        "",
        "## Summary",
        "",
        f"- **Block** (address immediately): {counts[BLOCK]}",
        f"- **Warn** (address soon): {counts[WARN]}",
        f"- **Info** (awareness only): {counts[INFO]}",
        "",
    ]

    if sum(counts.values()) == 0:
        lines.append("No issues detected.")
    else:
        for level in (BLOCK, WARN, INFO):
            if counts[level] == 0:
                continue
            lines.append(f"## {level} ({counts[level]})")
            lines.append("")
            for sev, title, detail in report:
                if sev == level:
                    lines.append(f"- **{title}** — {detail}")
            lines.append("")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report written: {report_path.relative_to(REPO_ROOT)}")

    if counts[BLOCK]:
        print(f"\n  BLOCK: {counts[BLOCK]}  |  WARN: {counts[WARN]}  |  INFO: {counts[INFO]}")
        return 2
    if counts[WARN]:
        print(f"\n  BLOCK: {counts[BLOCK]}  |  WARN: {counts[WARN]}  |  INFO: {counts[INFO]}")
        return 1
    print(f"\n  BLOCK: 0  |  WARN: 0  |  INFO: {counts[INFO]}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Integrated Musicianship ACP integrity scan")
    parser.add_argument("--out", default=None, help="Override report output path")
    args = parser.parse_args()

    report = []
    check_structure(report)
    check_broken_references(report)
    check_workspace_stale(report)
    check_compaction_candidates(report)
    check_todo_format(report)
    check_confidential_gitignore(report)

    return write_report(report, args.out)


if __name__ == "__main__":
    sys.exit(main())
