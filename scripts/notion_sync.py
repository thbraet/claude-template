#!/usr/bin/env python3
"""
notion_sync.py — Bidirectional sync between local CRISP-DM markdown and Notion.

Subcommands:
    init     Create project page structure in Notion
    status   Show sync status for all tracked documents
    push     Push a local markdown file to its Notion page
    pull     Pull a Notion page to its local markdown file
    diff     Show content differences between local and Notion
    content  Dump Notion page content as markdown (for conflict review)

Environment:
    NOTION_API_TOKEN   Required. Notion integration token.

State:
    .notion-sync.json  Tracks page IDs and content hashes for change detection.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NOTION_API_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"
SYNC_STATE_FILE = ".notion-sync.json"
DOCS_ROOT = Path("docs/crisp-dm")
MAX_BLOCKS_PER_REQUEST = 100
MAX_RT_LENGTH = 2000

PHASE_STRUCTURE = {
    "1-business-understanding": {
        "title": "1. Business Understanding",
        "documents": {
            "1.1-business-objectives.md": "1.1 Business Objectives",
            "1.2-situation-assessment.md": "1.2 Situation Assessment",
            "1.3-data-mining-goals.md": "1.3 Data Mining Goals",
            "1.4-project-plan.md": "1.4 Project Plan",
        },
    },
    "2-data-understanding": {
        "title": "2. Data Understanding",
        "documents": {
            "2.1-data-collection.md": "2.1 Data Collection",
            "2.2-data-description.md": "2.2 Data Description",
            "2.3-data-exploration.md": "2.3 Data Exploration",
            "2.4-data-quality.md": "2.4 Data Quality",
        },
    },
    "3-data-preparation": {
        "title": "3. Data Preparation",
        "documents": {
            "3.1-select-data.md": "3.1 Select Data",
            "3.2-clean-data.md": "3.2 Clean Data",
            "3.3-construct-data.md": "3.3 Construct Data",
            "3.4-integrate-data.md": "3.4 Integrate Data",
            "3.5-format-data.md": "3.5 Format Data",
        },
    },
    "4-modeling": {
        "title": "4. Modeling",
        "documents": {
            "4.1-select-modeling-techniques.md": "4.1 Select Modeling Techniques",
            "4.2-generate-test-design.md": "4.2 Generate Test Design",
            "4.3-build-model.md": "4.3 Build Model",
            "4.4-assess-model.md": "4.4 Assess Model",
        },
    },
    "5-evaluation": {
        "title": "5. Evaluation",
        "documents": {
            "5.1-evaluate-results.md": "5.1 Evaluate Results",
            "5.2-review-process.md": "5.2 Review Process",
            "5.3-determine-next-steps.md": "5.3 Determine Next Steps",
        },
    },
    "6-deployment": {
        "title": "6. Deployment",
        "documents": {
            "6.1-plan-deployment.md": "6.1 Plan Deployment",
            "6.2-plan-monitoring.md": "6.2 Plan Monitoring & Maintenance",
            "6.3-produce-final-report.md": "6.3 Produce Final Report",
            "6.4-review-project.md": "6.4 Review Project",
        },
    },
}


# ---------------------------------------------------------------------------
# Notion API client
# ---------------------------------------------------------------------------


class NotionClient:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_API_VERSION,
            "Content-Type": "application/json",
        }

    def _request(self, method: str, endpoint: str, payload: dict | None = None) -> dict:
        url = f"{NOTION_BASE_URL}/{endpoint}"
        resp = requests.request(method, url, headers=self.headers, json=payload, timeout=30)
        if not resp.ok:
            raise RuntimeError(f"Notion API {method} {endpoint} failed ({resp.status_code}): {resp.text}")
        return resp.json()

    def create_page(self, parent_id: str, title: str, blocks: list[dict] | None = None) -> dict:
        payload = {
            "parent": {"page_id": parent_id},
            "properties": {"title": [{"text": {"content": title}}]},
        }
        if blocks:
            payload["children"] = blocks[:MAX_BLOCKS_PER_REQUEST]
        page = self._request("POST", "pages", payload)
        # Append remaining blocks in batches if needed
        if blocks and len(blocks) > MAX_BLOCKS_PER_REQUEST:
            self._append_blocks_batched(page["id"], blocks[MAX_BLOCKS_PER_REQUEST:])
        return page

    def get_page(self, page_id: str) -> dict:
        return self._request("GET", f"pages/{page_id}")

    def get_blocks(self, block_id: str) -> list[dict]:
        blocks = []
        cursor = None
        while True:
            endpoint = f"blocks/{block_id}/children?page_size=100"
            if cursor:
                endpoint += f"&start_cursor={cursor}"
            data = self._request("GET", endpoint)
            blocks.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
        # Recursively fetch children for blocks that have them
        for block in blocks:
            if block.get("has_children") and block["type"] not in ("child_page", "child_database"):
                block["_children"] = self.get_blocks(block["id"])
        return blocks

    def append_blocks(self, block_id: str, children: list[dict]) -> dict:
        return self._request("PATCH", f"blocks/{block_id}/children", {"children": children})

    def _append_blocks_batched(self, block_id: str, blocks: list[dict]):
        for i in range(0, len(blocks), MAX_BLOCKS_PER_REQUEST):
            batch = blocks[i : i + MAX_BLOCKS_PER_REQUEST]
            self.append_blocks(block_id, batch)

    def delete_block(self, block_id: str) -> dict:
        return self._request("DELETE", f"blocks/{block_id}")

    def replace_page_content(self, page_id: str, new_blocks: list[dict]):
        old_blocks = self.get_blocks(page_id)
        for block in old_blocks:
            if block["type"] != "child_page":
                self.delete_block(block["id"])
        self._append_blocks_batched(page_id, new_blocks)

    def get_child_pages(self, page_id: str) -> list[dict]:
        blocks = self.get_blocks(page_id)
        return [b for b in blocks if b["type"] == "child_page"]


# ---------------------------------------------------------------------------
# Markdown -> Notion blocks
# ---------------------------------------------------------------------------


def _annotations(bold=False, italic=False, code=False, strikethrough=False, underline=False):
    return {
        "bold": bold,
        "italic": italic,
        "code": code,
        "strikethrough": strikethrough,
        "underline": underline,
        "color": "default",
    }


def _parse_inline(text: str) -> list[dict]:
    """Parse markdown inline formatting into Notion rich_text array."""
    tokens = []
    # Order matters: bold before italic, code is non-greedy
    pattern = re.compile(
        r"(\*\*(.+?)\*\*"       # bold
        r"|\*(.+?)\*"           # italic
        r"|`(.+?)`"             # inline code
        r"|\[([^\]]+)\]\(([^)]+)\)"  # link
        r")"
    )
    last = 0
    for m in pattern.finditer(text):
        if m.start() > last:
            tokens.append(_rt(text[last : m.start()]))
        if m.group(2):
            tokens.append(_rt(m.group(2), bold=True))
        elif m.group(3):
            tokens.append(_rt(m.group(3), italic=True))
        elif m.group(4):
            tokens.append(_rt(m.group(4), code=True))
        elif m.group(5):
            tokens.append(_rt(m.group(5), link=m.group(6)))
        last = m.end()
    if last < len(text):
        tokens.append(_rt(text[last:]))
    return tokens if tokens else [_rt(text)]


def _rt(content: str, bold=False, italic=False, code=False, link=None) -> dict:
    """Create a single Notion rich_text object."""
    # Truncate to API limit
    content = content[:MAX_RT_LENGTH]
    rt = {
        "type": "text",
        "text": {"content": content},
        "annotations": _annotations(bold=bold, italic=italic, code=code),
    }
    if link:
        rt["text"]["link"] = {"url": link}
    return rt


def md_to_blocks(markdown: str) -> list[dict]:
    """Convert markdown string to a list of Notion block objects."""
    lines = markdown.split("\n")
    blocks = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Blank line — skip
        if not line.strip():
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^-{3,}\s*$", line):
            blocks.append({"type": "divider", "divider": {}})
            i += 1
            continue

        # Code block
        if line.strip().startswith("```"):
            lang = line.strip().lstrip("`").strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            blocks.append({
                "type": "code",
                "code": {
                    "rich_text": [_rt("\n".join(code_lines))],
                    "language": lang if lang else "plain text",
                },
            })
            continue

        # Headings
        heading_match = re.match(r"^(#{1,3})\s+(.*)", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            htype = f"heading_{level}"
            blocks.append({"type": htype, htype: {"rich_text": _parse_inline(text)}})
            i += 1
            continue

        # Blockquote
        if line.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].startswith(">"):
                quote_lines.append(lines[i].lstrip(">").strip())
                i += 1
            blocks.append({
                "type": "quote",
                "quote": {"rich_text": _parse_inline("\n".join(quote_lines))},
            })
            continue

        # Table
        if "|" in line and i + 1 < len(lines) and re.match(r"^\|[-\s|:]+\|$", lines[i + 1].strip()):
            table_rows = []
            # Header row
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            table_rows.append(header_cells)
            i += 1  # skip header
            i += 1  # skip separator
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                table_rows.append(cells)
                i += 1
            width = max(len(r) for r in table_rows)
            # Pad rows to same width
            for row in table_rows:
                while len(row) < width:
                    row.append("")
            table_block = {
                "type": "table",
                "table": {
                    "table_width": width,
                    "has_column_header": True,
                    "has_row_header": False,
                    "children": [],
                },
            }
            for row in table_rows:
                table_block["table"]["children"].append({
                    "type": "table_row",
                    "table_row": {"cells": [_parse_inline(cell) for cell in row]},
                })
            blocks.append(table_block)
            continue

        # Numbered list
        num_match = re.match(r"^(\d+)\.\s+(.*)", line)
        if num_match:
            text = num_match.group(2).strip()
            block = {
                "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": _parse_inline(text)},
            }
            # Check for nested items
            children = []
            i += 1
            while i < len(lines) and re.match(r"^  +[-\d]", lines[i]):
                nested = re.sub(r"^  +[-\d.]+\s*", "", lines[i]).strip()
                children.append({
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": _parse_inline(nested)},
                })
                i += 1
            if children:
                block["numbered_list_item"]["children"] = children
            blocks.append(block)
            continue

        # Bulleted list
        bullet_match = re.match(r"^[-*]\s+(.*)", line)
        if bullet_match:
            text = bullet_match.group(1).strip()
            block = {
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": _parse_inline(text)},
            }
            # Check for nested items
            children = []
            i += 1
            while i < len(lines) and re.match(r"^  +[-*]", lines[i]):
                nested = re.sub(r"^  +[-*]\s*", "", lines[i]).strip()
                children.append({
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": _parse_inline(nested)},
                })
                i += 1
            if children:
                block["bulleted_list_item"]["children"] = children
            blocks.append(block)
            continue

        # Paragraph (fallback)
        blocks.append({"type": "paragraph", "paragraph": {"rich_text": _parse_inline(line)}})
        i += 1

    return blocks


# ---------------------------------------------------------------------------
# Notion blocks -> Markdown
# ---------------------------------------------------------------------------


def _extract_text(rich_text_list: list[dict]) -> str:
    """Convert Notion rich_text array to markdown inline string."""
    parts = []
    for rt in rich_text_list:
        content = rt.get("text", {}).get("content", "")
        ann = rt.get("annotations", {})
        link = rt.get("text", {}).get("link")

        if ann.get("code"):
            content = f"`{content}`"
        if ann.get("bold"):
            content = f"**{content}**"
        if ann.get("italic"):
            content = f"*{content}*"
        if link:
            content = f"[{content}]({link['url']})"

        parts.append(content)
    return "".join(parts)


def blocks_to_md(blocks: list[dict], indent: int = 0) -> str:
    """Convert Notion blocks to markdown string."""
    lines = []
    prefix = "  " * indent

    for block in blocks:
        btype = block["type"]
        data = block.get(btype, {})

        if btype == "divider":
            lines.append(f"{prefix}---")
            lines.append("")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = int(btype[-1])
            text = _extract_text(data.get("rich_text", []))
            lines.append(f"{prefix}{'#' * level} {text}")
            lines.append("")

        elif btype == "paragraph":
            text = _extract_text(data.get("rich_text", []))
            lines.append(f"{prefix}{text}")
            lines.append("")

        elif btype == "bulleted_list_item":
            text = _extract_text(data.get("rich_text", []))
            lines.append(f"{prefix}- {text}")
            children = block.get("_children", data.get("children", []))
            if children:
                child_md = blocks_to_md(children, indent + 1)
                lines.append(child_md.rstrip())

        elif btype == "numbered_list_item":
            text = _extract_text(data.get("rich_text", []))
            lines.append(f"{prefix}1. {text}")
            children = block.get("_children", data.get("children", []))
            if children:
                child_md = blocks_to_md(children, indent + 1)
                lines.append(child_md.rstrip())

        elif btype == "quote":
            text = _extract_text(data.get("rich_text", []))
            for qline in text.split("\n"):
                lines.append(f"{prefix}> {qline}")
            lines.append("")

        elif btype == "code":
            lang = data.get("language", "")
            if lang == "plain text":
                lang = ""
            text = _extract_text(data.get("rich_text", []))
            lines.append(f"{prefix}```{lang}")
            lines.append(text)
            lines.append(f"{prefix}```")
            lines.append("")

        elif btype == "table":
            children = block.get("_children", data.get("children", []))
            if children:
                for row_idx, row_block in enumerate(children):
                    cells = row_block.get("table_row", {}).get("cells", [])
                    cell_texts = [_extract_text(cell) for cell in cells]
                    lines.append(f"{prefix}| {' | '.join(cell_texts)} |")
                    if row_idx == 0:
                        lines.append(f"{prefix}|{'|'.join(['---' for _ in cell_texts])}|")
            lines.append("")

        elif btype == "child_page":
            # Skip child pages — they are separate sync targets
            pass

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Sync state management
# ---------------------------------------------------------------------------


def _content_hash(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text.strip())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def load_state(path: str = SYNC_STATE_FILE) -> dict:
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_state(state: dict, path: str = SYNC_STATE_FILE):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)


def local_path_for(phase_key: str, doc_filename: str) -> Path:
    return DOCS_ROOT / phase_key / doc_filename


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


def cmd_init(client: NotionClient, args):
    """Create project structure in Notion and initialize sync state."""
    parent_id = args.parent_page_id
    project_name = args.project_name or "CRISP-DM Project"

    state = load_state()
    if state.get("notion_project_page_id"):
        print(f"Already initialized. Project page: {state['notion_project_page_id']}")
        print("Use --force to reinitialize.")
        if not args.force:
            return
        print("Reinitializing...")

    # Create project page
    project_page = client.create_page(parent_id, project_name)
    project_page_id = project_page["id"]
    print(f"Created project page: {project_name} ({project_page_id})")

    state = {
        "project_name": project_name,
        "notion_parent_page_id": parent_id,
        "notion_project_page_id": project_page_id,
        "phase_pages": {},
        "documents": {},
    }

    # Create phase subpages
    for phase_key, phase_info in PHASE_STRUCTURE.items():
        phase_page = client.create_page(project_page_id, phase_info["title"])
        phase_page_id = phase_page["id"]
        state["phase_pages"][phase_key] = phase_page_id
        print(f"  Created phase page: {phase_info['title']} ({phase_page_id})")

        # Create document pages (empty or from local file if it exists)
        for doc_file, doc_title in phase_info["documents"].items():
            local_path = local_path_for(phase_key, doc_file)
            blocks = []
            local_hash = ""
            if local_path.exists():
                content = local_path.read_text()
                blocks = md_to_blocks(content)
                local_hash = _content_hash(content)
                print(f"    Created page: {doc_title} (from local file)")
            else:
                print(f"    Created page: {doc_title} (empty)")

            doc_page = client.create_page(phase_page_id, doc_title, blocks)
            doc_page_id = doc_page["id"]

            rel_path = str(local_path)
            state["documents"][rel_path] = {
                "notion_page_id": doc_page_id,
                "phase": phase_key,
                "title": doc_title,
                "last_sync_local_hash": local_hash,
                "last_sync_notion_hash": local_hash,
                "last_synced_at": datetime.now(timezone.utc).isoformat(),
            }

    save_state(state)
    print(f"\nSync state saved to {SYNC_STATE_FILE}")


def cmd_status(client: NotionClient, args):
    """Check both sides for changes and report sync status."""
    state = load_state()
    if not state.get("notion_project_page_id"):
        print("ERROR: Not initialized. Run 'init' first.")
        sys.exit(1)

    results = {"no_change": [], "local_only": [], "notion_only": [], "conflict": [], "new_local": [], "missing_local": []}

    for phase_key, phase_info in PHASE_STRUCTURE.items():
        for doc_file, doc_title in phase_info["documents"].items():
            local_path = local_path_for(phase_key, doc_file)
            rel_path = str(local_path)
            doc_state = state.get("documents", {}).get(rel_path)

            if not doc_state:
                if local_path.exists():
                    results["new_local"].append({"path": rel_path, "title": doc_title, "phase": phase_key})
                continue

            notion_page_id = doc_state["notion_page_id"]
            last_local_hash = doc_state.get("last_sync_local_hash", "")
            last_notion_hash = doc_state.get("last_sync_notion_hash", "")

            # Current local state
            if local_path.exists():
                current_local = local_path.read_text()
                current_local_hash = _content_hash(current_local)
            else:
                current_local_hash = ""

            # Current Notion state
            try:
                notion_blocks = client.get_blocks(notion_page_id)
                notion_md = blocks_to_md(notion_blocks)
                current_notion_hash = _content_hash(notion_md)
            except Exception as e:
                print(f"WARNING: Could not fetch Notion page for {rel_path}: {e}")
                current_notion_hash = last_notion_hash

            local_changed = current_local_hash != last_local_hash
            notion_changed = current_notion_hash != last_notion_hash

            entry = {
                "path": rel_path,
                "title": doc_title,
                "phase": phase_key,
                "notion_page_id": notion_page_id,
                "local_hash": current_local_hash,
                "notion_hash": current_notion_hash,
            }

            if not local_changed and not notion_changed:
                results["no_change"].append(entry)
            elif local_changed and not notion_changed:
                results["local_only"].append(entry)
            elif not local_changed and notion_changed:
                results["notion_only"].append(entry)
            else:
                results["conflict"].append(entry)

    # Output as JSON for the command to parse
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("=== Sync Status ===\n")
        if results["no_change"]:
            print(f"Up to date ({len(results['no_change'])}):")
            for e in results["no_change"]:
                print(f"  {e['title']}")
        if results["local_only"]:
            print(f"\nLocal changes to push ({len(results['local_only'])}):")
            for e in results["local_only"]:
                print(f"  -> {e['title']} ({e['path']})")
        if results["notion_only"]:
            print(f"\nNotion changes to pull ({len(results['notion_only'])}):")
            for e in results["notion_only"]:
                print(f"  <- {e['title']}")
        if results["conflict"]:
            print(f"\nCONFLICTS ({len(results['conflict'])}):")
            for e in results["conflict"]:
                print(f"  !! {e['title']} ({e['path']})")
        if results["new_local"]:
            print(f"\nNew local files (not tracked) ({len(results['new_local'])}):")
            for e in results["new_local"]:
                print(f"  + {e['title']} ({e['path']})")
        total = sum(len(v) for v in results.values())
        print(f"\nTotal documents: {total}")


def cmd_push(client: NotionClient, args):
    """Push a local markdown file to its Notion page."""
    state = load_state()
    rel_path = args.path
    doc_state = state.get("documents", {}).get(rel_path)

    if not doc_state:
        print(f"ERROR: {rel_path} is not tracked. Run 'init' or add it to sync state.")
        sys.exit(1)

    local_path = Path(rel_path)
    if not local_path.exists():
        print(f"ERROR: Local file {rel_path} does not exist.")
        sys.exit(1)

    content = local_path.read_text()
    blocks = md_to_blocks(content)
    notion_page_id = doc_state["notion_page_id"]

    client.replace_page_content(notion_page_id, blocks)

    content_hash = _content_hash(content)
    doc_state["last_sync_local_hash"] = content_hash
    doc_state["last_sync_notion_hash"] = content_hash
    doc_state["last_synced_at"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    print(f"Pushed {rel_path} -> Notion ({notion_page_id})")


def cmd_pull(client: NotionClient, args):
    """Pull Notion page content to a local markdown file."""
    state = load_state()
    rel_path = args.path
    doc_state = state.get("documents", {}).get(rel_path)

    if not doc_state:
        print(f"ERROR: {rel_path} is not tracked.")
        sys.exit(1)

    notion_page_id = doc_state["notion_page_id"]
    blocks = client.get_blocks(notion_page_id)
    markdown = blocks_to_md(blocks)

    local_path = Path(rel_path)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text(markdown)

    content_hash = _content_hash(markdown)
    doc_state["last_sync_local_hash"] = content_hash
    doc_state["last_sync_notion_hash"] = content_hash
    doc_state["last_synced_at"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    print(f"Pulled Notion ({notion_page_id}) -> {rel_path}")


def cmd_diff(client: NotionClient, args):
    """Show the Notion version of a document as markdown (for comparison)."""
    state = load_state()
    rel_path = args.path
    doc_state = state.get("documents", {}).get(rel_path)

    if not doc_state:
        print(f"ERROR: {rel_path} is not tracked.")
        sys.exit(1)

    notion_page_id = doc_state["notion_page_id"]
    blocks = client.get_blocks(notion_page_id)
    notion_md = blocks_to_md(blocks)

    if args.notion_only:
        print(notion_md)
        return

    local_path = Path(rel_path)
    if local_path.exists():
        local_md = local_path.read_text()
    else:
        local_md = ""

    # Write temp files and diff
    import tempfile
    import subprocess

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", prefix="local_", delete=False) as f_local:
        f_local.write(local_md)
        f_local_path = f_local.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", prefix="notion_", delete=False) as f_notion:
        f_notion.write(notion_md)
        f_notion_path = f_notion.name

    try:
        result = subprocess.run(
            ["diff", "--unified", f"--label=local:{rel_path}", f"--label=notion:{rel_path}", f_local_path, f_notion_path],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print("No differences.")
        else:
            print(result.stdout)
    finally:
        os.unlink(f_local_path)
        os.unlink(f_notion_path)


def cmd_content(client: NotionClient, args):
    """Dump Notion page content as markdown."""
    state = load_state()
    rel_path = args.path
    doc_state = state.get("documents", {}).get(rel_path)

    if not doc_state:
        print(f"ERROR: {rel_path} is not tracked.")
        sys.exit(1)

    blocks = client.get_blocks(doc_state["notion_page_id"])
    print(blocks_to_md(blocks))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Bidirectional CRISP-DM <-> Notion sync")
    sub = parser.add_subparsers(dest="command", required=True)

    # init
    p_init = sub.add_parser("init", help="Create project structure in Notion")
    p_init.add_argument("--parent-page-id", required=True, help="Notion parent page ID")
    p_init.add_argument("--project-name", default=None, help="Project name (default: from sync state or 'CRISP-DM Project')")
    p_init.add_argument("--force", action="store_true", help="Reinitialize even if already set up")

    # status
    p_status = sub.add_parser("status", help="Show sync status")
    p_status.add_argument("--json", action="store_true", help="Output as JSON")

    # push
    p_push = sub.add_parser("push", help="Push local file to Notion")
    p_push.add_argument("path", help="Relative path to local markdown file")

    # pull
    p_pull = sub.add_parser("pull", help="Pull Notion page to local file")
    p_pull.add_argument("path", help="Relative path to local markdown file")

    # diff
    p_diff = sub.add_parser("diff", help="Show diff between local and Notion")
    p_diff.add_argument("path", help="Relative path to local markdown file")
    p_diff.add_argument("--notion-only", action="store_true", help="Only print Notion content as markdown")

    # content
    p_content = sub.add_parser("content", help="Dump Notion page content as markdown")
    p_content.add_argument("path", help="Relative path to local markdown file")

    args = parser.parse_args()

    token = os.environ.get("NOTION_API_TOKEN")
    if not token:
        print("ERROR: NOTION_API_TOKEN environment variable is not set.")
        print("Create a Notion integration at https://www.notion.so/my-integrations")
        print("and set the token: export NOTION_API_TOKEN=ntn_...")
        sys.exit(1)

    client = NotionClient(token)

    cmd_map = {
        "init": cmd_init,
        "status": cmd_status,
        "push": cmd_push,
        "pull": cmd_pull,
        "diff": cmd_diff,
        "content": cmd_content,
    }
    cmd_map[args.command](client, args)


if __name__ == "__main__":
    main()
