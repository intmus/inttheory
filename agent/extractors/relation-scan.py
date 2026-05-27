#!/usr/bin/env python3
"""
relation-scan.py — Local document relationship scanner.

Parses markdown files, extracts entities and cross-references,
builds a relationship graph, and outputs a report surfacing
orphans, broken references, entity clusters, and drift candidates.

All processing is local. No document content leaves the machine.

Usage:
    python agent/extractors/relation-scan.py
    python agent/extractors/relation-scan.py archive/ workspace/active/
    python agent/extractors/relation-scan.py --config path/to/config.yaml

Dependencies: networkx, pyyaml
"""

import argparse
import datetime
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.parse import unquote
import json

import networkx as nx
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

DEFAULT_CONFIG = REPO_ROOT / "agent" / "extractors" / "relation-scan-config.yaml"

MD_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^):]+\.md)(?:#[^)]+)?\)")
BACKTICK_PATH_PATTERN = re.compile(
    r"`((?:agent|workspace|todo|archive|wiki|docs|content|repeatable-processes)"
    r"/[^\s`]+\.(?:md|py|bat|sh|json|yaml|docx|xlsx))`"
)
HEADER_PATTERN = re.compile(r"^#{1,3}\s+(.+)$", re.MULTILINE)
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
BOLD_PATTERN = re.compile(r"\*\*([^*]+)\*\*")
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
TEMPLATE_PATTERN = re.compile(
    r"\[[a-z][-a-z ]*\]|YYYY|MM-DD|\*", re.IGNORECASE
)


@dataclass
class DocumentNode:
    path: str
    rel_path: str = ""
    title: str = ""
    doc_type: str = ""
    date: str = ""
    modified: Optional[datetime.date] = None
    content_date: Optional[datetime.date] = None
    headers: list = field(default_factory=list)
    references: list = field(default_factory=list)
    people: list = field(default_factory=list)
    dates: list = field(default_factory=list)
    tags: list = field(default_factory=list)
    topics: list = field(default_factory=list)
    keywords: list = field(default_factory=list)


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        print(f"Config not found: {config_path}", file=sys.stderr)
        sys.exit(1)
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip("-")


def load_roster_from_shorthand(shorthand_path: Path) -> list[str]:
    if not shorthand_path.exists():
        return []
    content = shorthand_path.read_text(encoding="utf-8", errors="ignore")
    in_people_section = False
    names = []
    for line in content.splitlines():
        if line.strip().startswith("## Key People"):
            in_people_section = True
            continue
        if in_people_section and line.strip().startswith("## "):
            break
        if not in_people_section:
            continue
        if not line.strip().startswith("|") or line.strip().startswith("|---"):
            continue
        cols = [c.strip() for c in line.split("|")]
        cols = [c for c in cols if c]
        if not cols or cols[0].lower().startswith("name"):
            continue
        raw_name = cols[0]
        for part in re.split(r"\s*/\s*", raw_name):
            part = re.sub(r"\(.*?\)", "", part).strip()
            if part and len(part) > 1:
                names.append(part)
    return names


def collect_files(targets: list[str], excludes: list[str]) -> list[Path]:
    files = []
    for target in targets:
        target_path = REPO_ROOT / target
        if not target_path.exists():
            continue
        for md_file in target_path.rglob("*.md"):
            rel = str(md_file.relative_to(REPO_ROOT)).replace("\\", "/")
            skip = False
            for exc in excludes:
                if exc.startswith("*."):
                    if md_file.suffix == exc[1:]:
                        skip = True
                        break
                elif rel.startswith(exc):
                    skip = True
                    break
            if not skip:
                files.append(md_file)
    return files


def parse_frontmatter(content: str) -> dict:
    m = FRONTMATTER_PATTERN.match(content)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _resolve_content_date(fm_date: str, rel_path: str,
                          modified: Optional[datetime.date]) -> Optional[datetime.date]:
    """Best-effort content date: frontmatter > filename > modification date."""
    if fm_date and fm_date != "None":
        try:
            return datetime.date.fromisoformat(str(fm_date)[:10])
        except ValueError:
            pass
    fn_match = re.search(r"(\d{4}-\d{2}-\d{2})", rel_path.split("/")[-1])
    if fn_match:
        try:
            return datetime.date.fromisoformat(fn_match.group(1))
        except ValueError:
            pass
    return modified


def parse_document(path: Path, roster: list[str], tag_list: list[str],
                   stop_topics: set = None) -> DocumentNode:
    rel = str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    doc = DocumentNode(path=str(path), rel_path=rel)

    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return doc

    fm = parse_frontmatter(content)
    doc.title = str(fm.get("title", ""))
    doc.doc_type = str(fm.get("type", ""))
    doc.date = str(fm.get("date", fm.get("start_date", "")))

    fm_keywords = fm.get("keywords", [])
    if isinstance(fm_keywords, list):
        doc.keywords = [str(k).strip().lower() for k in fm_keywords if k]

    try:
        doc.modified = datetime.date.fromtimestamp(os.path.getmtime(path))
    except OSError:
        pass

    doc.content_date = _resolve_content_date(doc.date, rel, doc.modified)

    if stop_topics is None:
        stop_topics = set()
    raw_headers = HEADER_PATTERN.findall(content)
    doc.headers = raw_headers
    doc.topics = list({slugify(h) for h in raw_headers
                       if len(slugify(h)) > 2 and slugify(h) not in stop_topics})

    bold_terms = BOLD_PATTERN.findall(content)
    for term in bold_terms:
        s = slugify(term)
        if len(s) > 2 and s not in doc.topics and s not in stop_topics:
            doc.topics.append(s)

    md_refs = MD_LINK_PATTERN.findall(content)
    bt_refs = BACKTICK_PATH_PATTERN.findall(content)
    doc.references = list(set(md_refs + bt_refs))

    content_lower = content.lower()
    for name in roster:
        if name.lower() in content_lower:
            doc.people.append(name)

    doc.dates = list(set(DATE_PATTERN.findall(content)))

    if tag_list:
        tag_pattern = re.compile(r"\[(" + "|".join(re.escape(t) for t in tag_list) + r")\]")
        doc.tags = list(set(tag_pattern.findall(content)))

    return doc


def build_graph(documents: dict[str, DocumentNode], min_shared: int) -> nx.Graph:
    G = nx.Graph()
    for rel_path, doc in documents.items():
        G.add_node(rel_path, title=doc.title, doc_type=doc.doc_type,
                    date=doc.date, modified=str(doc.modified or ""))

    paths = list(documents.keys())
    for i in range(len(paths)):
        doc_a = documents[paths[i]]
        for j in range(i + 1, len(paths)):
            doc_b = documents[paths[j]]

            shared_people = set(doc_a.people) & set(doc_b.people)
            shared_topics = set(doc_a.topics) & set(doc_b.topics)
            shared_tags = set(doc_a.tags) & set(doc_b.tags)
            shared_keywords = set(doc_a.keywords) & set(doc_b.keywords)
            total = (len(shared_people) + len(shared_topics) +
                     len(shared_tags) + len(shared_keywords))

            if total >= min_shared:
                G.add_edge(paths[i], paths[j],
                           weight=total,
                           shared_people=list(shared_people),
                           shared_topics=list(shared_topics),
                           shared_tags=list(shared_tags),
                           shared_keywords=list(shared_keywords),
                           edge_type="shared-entity")

    for rel_path, doc in documents.items():
        for ref in doc.references:
            if TEMPLATE_PATTERN.search(ref):
                continue
            resolved_from_file = (Path(doc.path).parent / ref)
            resolved_from_root = REPO_ROOT / ref
            for candidate in [resolved_from_file, resolved_from_root]:
                try:
                    candidate = candidate.resolve()
                    candidate_rel = str(candidate.relative_to(REPO_ROOT)).replace("\\", "/")
                    if candidate_rel in documents and candidate_rel != rel_path:
                        if G.has_edge(rel_path, candidate_rel):
                            G[rel_path][candidate_rel]["has_direct_ref"] = True
                        else:
                            G.add_edge(rel_path, candidate_rel,
                                       weight=1, shared_people=[], shared_topics=[],
                                       shared_tags=[], edge_type="direct-reference",
                                       has_direct_ref=True)
                        break
                except (ValueError, OSError):
                    continue

    return G


def find_orphans(documents: dict[str, DocumentNode], indexes: list[str]) -> list[str]:
    indexed_files = set()
    for idx_rel in indexes:
        idx_path = REPO_ROOT / idx_rel
        if not idx_path.exists():
            continue
        try:
            content = idx_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for ref in MD_LINK_PATTERN.findall(content):
            if TEMPLATE_PATTERN.search(ref):
                continue
            decoded = unquote(ref)
            resolved = (idx_path.parent / decoded).resolve()
            try:
                indexed_files.add(str(resolved.relative_to(REPO_ROOT)).replace("\\", "/"))
            except ValueError:
                continue
        for ref in BACKTICK_PATH_PATTERN.findall(content):
            if TEMPLATE_PATTERN.search(ref):
                continue
            indexed_files.add(ref)

    orphans = []
    for rel_path in documents:
        if rel_path.startswith("workspace/active/"):
            continue
        if rel_path.startswith("todo/"):
            continue
        if rel_path.startswith("references/"):
            continue
        if rel_path.startswith("archive/vault/"):
            continue
        if rel_path.endswith("README.md"):
            continue
        if rel_path.endswith("INDEX.md"):
            continue
        if rel_path not in indexed_files:
            orphans.append(rel_path)

    return sorted(orphans)


def find_index_gaps(indexes: list[str]) -> list[tuple[str, str]]:
    gaps = []
    for idx_rel in indexes:
        idx_path = REPO_ROOT / idx_rel
        if not idx_path.exists():
            continue
        try:
            content = idx_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for ref in MD_LINK_PATTERN.findall(content):
            if TEMPLATE_PATTERN.search(ref):
                continue
            if ref.startswith(("http://", "https://", "mailto:")):
                continue
            decoded = unquote(ref)
            resolved = (idx_path.parent / decoded).resolve()
            if not resolved.exists():
                gaps.append((idx_rel, ref))
        for ref in BACKTICK_PATH_PATTERN.findall(content):
            if TEMPLATE_PATTERN.search(ref):
                continue
            target = REPO_ROOT / ref
            if not target.exists():
                gaps.append((idx_rel, ref))
    return gaps


def find_clusters(G: nx.Graph, documents: dict[str, DocumentNode],
                  freshness_threshold: int) -> list[dict]:
    entity_subgraph = nx.Graph()
    for u, v, data in G.edges(data=True):
        if data.get("edge_type") != "direct-reference":
            entity_subgraph.add_edge(u, v, **data)

    if entity_subgraph.number_of_edges() == 0:
        return []

    try:
        from networkx.algorithms.community import louvain_communities
        communities = louvain_communities(entity_subgraph, weight="weight",
                                          resolution=1.5, seed=42)
    except Exception:
        communities = list(nx.connected_components(entity_subgraph))

    clusters = []
    for community in communities:
        if len(community) < 3:
            continue

        members = sorted(community)

        internal_people = defaultdict(int)
        internal_topics = defaultdict(int)
        internal_keywords = defaultdict(int)
        for u in members:
            for v in members:
                if entity_subgraph.has_edge(u, v):
                    edge = entity_subgraph[u][v]
                    for p in edge.get("shared_people", []):
                        internal_people[p] += 1
                    for t in edge.get("shared_topics", []):
                        internal_topics[t] += 1
                    for k in edge.get("shared_keywords", []):
                        internal_keywords[k] += 1

        top_topics = sorted(internal_topics, key=internal_topics.get, reverse=True)
        top_people = sorted(internal_people, key=internal_people.get, reverse=True)
        top_keywords = sorted(internal_keywords, key=internal_keywords.get, reverse=True)

        content_dates = []
        for m in members:
            doc = documents[m]
            if doc.content_date:
                content_dates.append(doc.content_date)

        freshness_gap = 0
        if len(content_dates) >= 2:
            freshness_gap = (max(content_dates) - min(content_dates)).days

        label_candidates = (top_keywords[:3] if top_keywords
                            else top_topics[:3] if top_topics
                            else top_people[:2])
        label = ", ".join(label_candidates) if label_candidates else "unlabeled"

        clusters.append({
            "label": label,
            "members": members,
            "shared_people": top_people,
            "shared_topics": top_topics,
            "shared_keywords": top_keywords,
            "freshness_gap": freshness_gap,
            "flagged": freshness_gap > freshness_threshold,
            "content_dates": {m: str(documents[m].content_date or "unknown")
                              for m in members},
        })

    clusters.sort(key=lambda c: len(c["members"]), reverse=True)
    return clusters


def find_drift_candidates(clusters: list[dict], documents: dict[str, DocumentNode],
                          G: nx.Graph, freshness_threshold: int) -> list[dict]:
    candidates = []
    seen_pairs = set()

    for cluster in clusters:
        if not cluster["flagged"]:
            continue
        members = cluster["members"]
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                if a.startswith("archive/vault/") and b.startswith("archive/vault/"):
                    continue
                pair_key = tuple(sorted([a, b]))
                if pair_key in seen_pairs:
                    continue

                if not G.has_edge(a, b):
                    continue
                edge = G[a][b]
                shared_count = edge.get("weight", 0)
                if shared_count < 3:
                    continue

                doc_a = documents[a]
                doc_b = documents[b]
                date_a = doc_a.content_date
                date_b = doc_b.content_date
                if not date_a or not date_b:
                    continue
                gap = abs((date_a - date_b).days)
                if gap < freshness_threshold:
                    continue

                shared_entities = (
                    edge.get("shared_people", []) +
                    edge.get("shared_topics", []) +
                    edge.get("shared_keywords", [])
                )

                seen_pairs.add(pair_key)
                candidates.append({
                    "doc_a": a,
                    "doc_b": b,
                    "shared_entities": shared_entities,
                    "gap_days": gap,
                    "date_a": str(date_a),
                    "date_b": str(date_b),
                })

    candidates.sort(key=lambda c: c["gap_days"], reverse=True)
    return candidates


CLUSTER_COLORS = [
    "#5c6bc0", "#e53935", "#43a047", "#fb8c00", "#1e88e5",
    "#8e24aa", "#00acc1", "#f4511e", "#7cb342", "#5e35b1",
    "#d81b60", "#00897b", "#ffb300", "#3949ab", "#c0ca33",
    "#6d4c41", "#039be5", "#e64a19", "#00796b", "#7e57c2",
]
ORPHAN_COLOR = "#bdbdbd"
DEFAULT_COLOR = "#b0bec5"

VIS_TEMPLATE = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>Relation Scan — {title}</title>
<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
         background: #ffffff; color: #333; }}
  #graph {{ width: 100vw; height: 100vh; border-bottom: 1px solid #e0e0e0; }}
  #info {{ position: fixed; top: 12px; left: 12px; background: rgba(255,255,255,0.95);
           border: 1px solid #ccc; border-radius: 8px; padding: 16px; max-width: 360px;
           font-size: 13px; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
  #info h2 {{ font-size: 16px; margin-bottom: 8px; color: #1a1a2e; }}
  #info p {{ margin: 4px 0; color: #666; }}
  #controls {{ position: fixed; top: 12px; right: 12px; z-index: 10; display: flex; gap: 8px; }}
  #controls button {{ padding: 8px 16px; border: 1px solid #ccc; border-radius: 6px;
                      background: #fff; color: #333; font-size: 13px; cursor: pointer;
                      box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
  #controls button:hover {{ background: #f5f5f5; }}
  #legend {{ position: fixed; bottom: 12px; left: 12px; background: rgba(255,255,255,0.95);
             border: 1px solid #ccc; border-radius: 8px; padding: 12px; font-size: 12px;
             z-index: 10; max-height: 40vh; overflow-y: auto;
             box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
  #legend h3 {{ font-size: 13px; margin-bottom: 6px; color: #333; }}
  .legend-item {{ display: flex; align-items: center; margin: 3px 0; color: #555; }}
  .legend-dot {{ width: 10px; height: 10px; border-radius: 50%; margin-right: 8px; flex-shrink: 0; }}
  #detail {{ position: fixed; bottom: 12px; right: 12px; background: rgba(255,255,255,0.95);
             border: 1px solid #ccc; border-radius: 8px; padding: 16px; max-width: 400px;
             font-size: 13px; z-index: 10; display: none;
             box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
  #detail h3 {{ font-size: 14px; margin-bottom: 8px; color: #1a1a2e; }}
  #detail p {{ margin: 3px 0; color: #555; }}
  #status {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
             font-size: 14px; color: #999; z-index: 5; }}
  @media print {{
    #controls, #status {{ display: none !important; }}
    #info, #legend, #detail {{ position: static; box-shadow: none; border: 1px solid #ccc;
                                margin: 8px; page-break-inside: avoid; }}
    #graph {{ height: 80vh; }}
  }}
</style>
</head><body>
<div id="status">Arranging layout&hellip;</div>
<div id="graph"></div>
<div id="info">
  <h2>Relation Scan &mdash; {title}</h2>
  <p>{file_count} documents &middot; {edge_count} connections</p>
  <p>{cluster_count} clusters &middot; {orphan_count} orphaned</p>
  <p style="margin-top:8px;color:#999;">Click a node for details. Drag nodes to reposition.</p>
</div>
<div id="controls">
  <button onclick="network.setOptions({{physics:true}});setTimeout(function(){{network.setOptions({{physics:false}});}},3000);">Re-arrange</button>
  <button onclick="window.print();">Print</button>
</div>
<div id="legend"><h3>Clusters</h3>{legend_html}</div>
<div id="detail"></div>
<script>
var nodes = new vis.DataSet({nodes_json});
var edges = new vis.DataSet({edges_json});
var container = document.getElementById('graph');
var data = {{ nodes: nodes, edges: edges }};
var options = {{
  nodes: {{ font: {{ color: '#fff', size: 12, face: 'Segoe UI, sans-serif' }},
            borderWidth: 2, shape: 'box', margin: 8,
            shadow: {{ enabled: true, color: 'rgba(0,0,0,0.08)', size: 4 }} }},
  edges: {{ smooth: {{ type: 'continuous' }} }},
  physics: {{ solver: 'barnesHut',
              barnesHut: {{ gravitationalConstant: -8000, centralGravity: 0.15,
                            springLength: 200, springConstant: 0.02,
                            avoidOverlap: 0.8 }},
              stabilization: {{ iterations: 400, fit: true }},
              minVelocity: 0.75 }},
  interaction: {{ hover: true, tooltipDelay: 100, zoomSpeed: 0.4 }}
}};
var network = new vis.Network(container, data, options);
network.once('stabilizationIterationsDone', function() {{
  network.setOptions({{ physics: false }});
  document.getElementById('status').style.display = 'none';
}});
var detail = document.getElementById('detail');
network.on('click', function(params) {{
  if (params.nodes.length > 0) {{
    var node = nodes.get(params.nodes[0]);
    var html = '<h3>' + node.label + '</h3>';
    html += '<p><b>Path:</b> ' + node.id + '</p>';
    if (node.content_date) html += '<p><b>Content date:</b> ' + node.content_date + '</p>';
    if (node.doc_type) html += '<p><b>Type:</b> ' + node.doc_type + '</p>';
    if (node.cluster_label) html += '<p><b>Cluster:</b> ' + node.cluster_label + '</p>';
    if (node.keywords) html += '<p><b>Keywords:</b> ' + node.keywords + '</p>';
    if (node.people) html += '<p><b>People:</b> ' + node.people + '</p>';
    if (node.topic_count) html += '<p><b>Topics:</b> ' + node.topic_count + '</p>';
    detail.innerHTML = html;
    detail.style.display = 'block';
  }} else {{
    detail.style.display = 'none';
  }}
}});
</script>
</body></html>"""


def generate_viz(G: nx.Graph, documents: dict[str, DocumentNode],
                 clusters: list[dict], orphans: list[str], report_dir: str):
    node_cluster_map = {}
    node_cluster_label = {}
    for i, c in enumerate(clusters):
        for m in c["members"]:
            node_cluster_map[m] = i
            node_cluster_label[m] = c["label"]

    orphan_set = set(orphans)

    vis_nodes = []
    for rel_path, doc in documents.items():
        degree = G.degree(rel_path) if rel_path in G else 0
        if degree == 0 and rel_path not in orphan_set:
            continue

        cluster_idx = node_cluster_map.get(rel_path)
        if rel_path in orphan_set:
            color = ORPHAN_COLOR
        elif cluster_idx is not None:
            color = CLUSTER_COLORS[cluster_idx % len(CLUSTER_COLORS)]
        else:
            color = DEFAULT_COLOR

        label = doc.title if doc.title else rel_path.split("/")[-1].replace(".md", "")

        font_size = max(10, min(16, 10 + degree))

        vis_nodes.append({
            "id": rel_path,
            "label": label,
            "font": {"size": font_size, "color": "#fff"},
            "color": {"background": color, "border": color,
                       "highlight": {"background": "#e3f2fd", "border": color}},
            "content_date": str(doc.content_date or ""),
            "doc_type": doc.doc_type,
            "cluster_label": node_cluster_label.get(rel_path, "none"),
            "keywords": ", ".join(doc.keywords[:7]) if doc.keywords else "",
            "people": ", ".join(doc.people[:5]) if doc.people else "",
            "topic_count": str(len(doc.topics)),
        })

    vis_edges = []
    for u, v, data in G.edges(data=True):
        if u not in documents or v not in documents:
            continue
        is_direct = data.get("has_direct_ref", False)
        weight = data.get("weight", 1)
        vis_edges.append({
            "from": u, "to": v,
            "width": max(0.5, min(4, weight * 0.5)),
            "dashes": not is_direct,
            "color": {"color": "#555" if is_direct else "#333",
                       "opacity": 0.6 if is_direct else 0.25},
        })

    legend_items = []
    for i, c in enumerate(clusters):
        color = CLUSTER_COLORS[i % len(CLUSTER_COLORS)]
        legend_items.append(
            f'<div class="legend-item">'
            f'<div class="legend-dot" style="background:{color}"></div>'
            f'{c["label"]} ({len(c["members"])})</div>'
        )
    if orphans:
        legend_items.append(
            f'<div class="legend-item">'
            f'<div class="legend-dot" style="background:{ORPHAN_COLOR}"></div>'
            f'orphaned ({len(orphans)})</div>'
        )
    legend_html = "\n".join(legend_items)

    html = VIS_TEMPLATE.format(
        title=datetime.date.today().isoformat(),
        file_count=len(vis_nodes),
        edge_count=len(vis_edges),
        cluster_count=len(clusters),
        orphan_count=len(orphans),
        legend_html=legend_html,
        nodes_json=json.dumps(vis_nodes),
        edges_json=json.dumps(vis_edges),
    )

    out_dir = REPO_ROOT / report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{datetime.date.today().isoformat()}.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Visualization: {out_path.relative_to(REPO_ROOT)}")
    return out_path


def write_report(orphans, index_gaps, clusters, drift_candidates,
                 file_count, entity_count, targets, report_dir):
    today = datetime.date.today().isoformat()
    report_path = REPO_ROOT / report_dir
    report_path.mkdir(parents=True, exist_ok=True)
    out = report_path / f"{today}.md"

    lines = [
        f"# Relation Scan — {today}",
        "",
        f"**Targets:** {', '.join(targets)}",
        f"**Files scanned:** {file_count}",
        f"**Total entities extracted:** {entity_count}",
        "",
    ]

    lines.append(f"## Orphaned Files ({len(orphans)})")
    lines.append("")
    if orphans:
        lines.append("Files in `archive/` not referenced by any index:")
        lines.append("")
        for o in orphans:
            lines.append(f"- `{o}`")
    else:
        lines.append("No orphaned files found.")
    lines.append("")

    lines.append(f"## Index Gaps ({len(index_gaps)})")
    lines.append("")
    if index_gaps:
        lines.append("Index entries pointing to missing files:")
        lines.append("")
        for source, target in index_gaps:
            lines.append(f"- `{source}` → `{target}` — not found")
    else:
        lines.append("All index references resolved.")
    lines.append("")

    flagged_clusters = [c for c in clusters if c["flagged"]]
    lines.append(f"## Entity Clusters ({len(clusters)} total, {len(flagged_clusters)} flagged)")
    lines.append("")
    if clusters:
        for c in clusters:
            flag = " ⚠" if c["flagged"] else ""
            lines.append(f"### \"{c['label']}\" — {len(c['members'])} documents{flag}")
            lines.append("")
            lines.append("| File | Content Date |")
            lines.append("|---|---|")
            for m in c["members"]:
                lines.append(f"| `{m}` | {c['content_dates'].get(m, 'unknown')} |")
            lines.append("")
            if c.get("shared_keywords"):
                display_keywords = c["shared_keywords"][:10]
                lines.append(f"**Shared keywords:** {', '.join(display_keywords)}")
                lines.append("")
            if c["shared_people"]:
                display_people = c["shared_people"][:10]
                lines.append(f"**Shared people:** {', '.join(display_people)}")
                lines.append("")
            if c["shared_topics"]:
                display_topics = c["shared_topics"][:10]
                lines.append(f"**Shared topics:** {', '.join(display_topics)}")
                lines.append("")
            if c["flagged"]:
                lines.append(f"**Freshness gap:** {c['freshness_gap']} days")
                lines.append("")
    else:
        lines.append("No clusters with 3+ documents found.")
    lines.append("")

    lines.append(f"## Drift Candidates ({len(drift_candidates)})")
    lines.append("")
    if drift_candidates:
        lines.append("Document pairs with high entity overlap and divergent content dates.")
        lines.append("Agent should read and compare these for accuracy.")
        lines.append("")
        lines.append("| Doc A (date) | Doc B (date) | Shared Entities | Gap (days) |")
        lines.append("|---|---|---|---|")
        for dc in drift_candidates:
            entities_str = ", ".join(dc["shared_entities"][:5])
            lines.append(f"| `{dc['doc_a']}` ({dc['date_a']}) | `{dc['doc_b']}` ({dc['date_b']}) | {entities_str} | {dc['gap_days']} |")
        lines.append("")
    else:
        lines.append("No drift candidates found.")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Orphaned files: {len(orphans)}")
    lines.append(f"- Index gaps: {len(index_gaps)}")
    lines.append(f"- Entity clusters: {len(clusters)} ({len(flagged_clusters)} with freshness gaps)")
    lines.append(f"- Drift candidates: {len(drift_candidates)}")
    lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {out.relative_to(REPO_ROOT)}")

    summary_parts = []
    if orphans:
        summary_parts.append(f"{len(orphans)} orphans")
    if index_gaps:
        summary_parts.append(f"{len(index_gaps)} index gaps")
    if flagged_clusters:
        summary_parts.append(f"{len(flagged_clusters)} flagged clusters")
    if drift_candidates:
        summary_parts.append(f"{len(drift_candidates)} drift candidates")

    if summary_parts:
        print(f"Findings: {', '.join(summary_parts)}")
    else:
        print("Clean scan — no issues found.")

    return out


def main():
    parser = argparse.ArgumentParser(description="Local document relationship scanner")
    parser.add_argument("targets", nargs="*", help="Directories to scan (overrides config)")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Config file path")
    parser.add_argument("--viz", action="store_true", help="Generate interactive HTML visualization")
    args = parser.parse_args()

    config = load_config(Path(args.config))

    targets = args.targets if args.targets else config.get("targets", [])
    excludes = config.get("exclude", [])
    indexes = config.get("indexes", [])
    tag_list = config.get("tags", [])
    freshness_threshold = config.get("freshness_threshold", 180)
    min_shared = config.get("min_shared_entities", 2)
    report_dir = config.get("report_dir", "agent/extractors/relation-reports/")

    shorthand_path = REPO_ROOT / config.get("shorthand_path", "agent/reference/SHORTHAND.md")
    roster = load_roster_from_shorthand(shorthand_path)
    if not roster:
        roster = config.get("roster", [])
    if roster:
        print(f"Roster: {len(roster)} people loaded from {shorthand_path.relative_to(REPO_ROOT) if shorthand_path.exists() else 'config fallback'}")

    stop_topics = set(config.get("stop_topics", []))

    md_files = collect_files(targets, excludes)
    print(f"Scanning {len(md_files)} files across {', '.join(targets)}...")

    documents = {}
    total_entities = 0
    for f in md_files:
        doc = parse_document(f, roster, tag_list, stop_topics)
        documents[doc.rel_path] = doc
        total_entities += (len(doc.headers) + len(doc.references) +
                           len(doc.people) + len(doc.dates) +
                           len(doc.tags) + len(doc.topics) +
                           len(doc.keywords))

    G = build_graph(documents, min_shared)
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    orphans = find_orphans(documents, indexes)
    index_gaps = find_index_gaps(indexes)
    clusters = find_clusters(G, documents, freshness_threshold)
    drift = find_drift_candidates(clusters, documents, G, freshness_threshold)

    write_report(orphans, index_gaps, clusters, drift,
                 len(documents), total_entities, targets, report_dir)

    if args.viz:
        generate_viz(G, documents, clusters, orphans, report_dir)


if __name__ == "__main__":
    main()
