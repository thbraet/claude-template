#!/usr/bin/env python3
"""Convert a markdown file to Notion blocks and push to a Notion page via REST API."""

import json
import os
import re
import subprocess
import sys

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_VERSION = "2022-06-28"


def notion_api(method, path, body=None):
    """Make a Notion API call via curl to avoid Python SSL issues."""
    url = f"https://api.notion.com/v1{path}"
    cmd = ["curl", "-s", "-X", method, url,
           "-H", f"Authorization: Bearer {NOTION_TOKEN}",
           "-H", f"Notion-Version: {NOTION_VERSION}"]
    if body:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def clear_page(page_id):
    """Delete all blocks from a page."""
    result = notion_api("GET", f"/blocks/{page_id}/children?page_size=100")
    for block in result.get("results", []):
        notion_api("DELETE", f"/blocks/{block['id']}")


def text_seg(content, bold=False, italic=False, code=False):
    """Create a rich_text segment."""
    seg = {"type": "text", "text": {"content": content}}
    ann = {}
    if bold:
        ann["bold"] = True
    if italic:
        ann["italic"] = True
    if code:
        ann["code"] = True
    if ann:
        seg["annotations"] = ann
    return seg


def parse_inline(text):
    """Parse inline markdown formatting into rich_text segments."""
    segments = []
    # Pattern: **bold**, *italic*, `code`
    pattern = re.compile(r'(\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`)')
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            segments.append(text_seg(text[pos:m.start()]))
        if m.group(2):  # bold
            segments.append(text_seg(m.group(2), bold=True))
        elif m.group(3):  # italic
            segments.append(text_seg(m.group(3), italic=True))
        elif m.group(4):  # code
            segments.append(text_seg(m.group(4), code=True))
        pos = m.end()
    if pos < len(text):
        segments.append(text_seg(text[pos:]))
    if not segments:
        segments.append(text_seg(text))
    return segments


def parse_bullet_text(text):
    """Parse a bullet item that may have **Label:** format."""
    m = re.match(r'\*\*(.+?)\*\*\s*(.*)', text)
    if m:
        segs = [text_seg(m.group(1), bold=True)]
        rest = m.group(2)
        if rest:
            segs.extend(parse_inline(rest))
        return segs
    return parse_inline(text)


def parse_table(lines):
    """Parse markdown table lines into a Notion table block."""
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)
    # Remove separator row (---|---)
    data_rows = [r for r in rows if not all(re.match(r'^-+$', c.strip()) for c in r)]
    if not data_rows:
        return None
    width = max(len(r) for r in data_rows)
    table_rows = []
    for i, row in enumerate(data_rows):
        cells = []
        for j in range(width):
            cell_text = row[j] if j < len(row) else ""
            if i == 0:  # header row
                cells.append([text_seg(cell_text, bold=True)])
            else:
                cells.append(parse_inline(cell_text) if cell_text else [])
        table_rows.append({
            "type": "table_row",
            "table_row": {"cells": cells}
        })
    return {
        "type": "table",
        "table": {
            "table_width": width,
            "has_column_header": True,
            "has_row_header": False,
            "children": table_rows
        }
    }


def md_to_blocks(md_text):
    """Convert markdown text to Notion block objects.
    Returns list of (block, [child_blocks]) tuples.
    """
    lines = md_text.split('\n')
    blocks = []  # list of (block_dict, [child_block_dicts])
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip the H1 title (it's the page title)
        if re.match(r'^# ', line):
            i += 1
            continue

        # Divider
        if re.match(r'^---\s*$', line):
            blocks.append(({"type": "divider", "divider": {}}, []))
            i += 1
            continue

        # Heading 2
        m = re.match(r'^## (.+)', line)
        if m:
            blocks.append(({"type": "heading_2", "heading_2": {"rich_text": parse_inline(m.group(1))}}, []))
            i += 1
            continue

        # Heading 3
        m = re.match(r'^### (.+)', line)
        if m:
            blocks.append(({"type": "heading_3", "heading_3": {"rich_text": parse_inline(m.group(1))}}, []))
            i += 1
            continue

        # Table (starts with |)
        if re.match(r'^\|', line):
            table_lines = []
            while i < len(lines) and re.match(r'^\|', lines[i]):
                table_lines.append(lines[i])
                i += 1
            table_block = parse_table(table_lines)
            if table_block:
                blocks.append((table_block, []))
            continue

        # Blockquote / callout
        if re.match(r'^>', line):
            quote_lines = []
            while i < len(lines) and re.match(r'^>', lines[i]):
                quote_lines.append(re.sub(r'^>\s?', '', lines[i]))
                i += 1
            combined = '\n'.join(quote_lines)
            # Check if it's a metadata callout (contains **Key:** patterns)
            if re.search(r'\*\*.+?\*\*:', combined):
                segs = []
                for ql in quote_lines:
                    if segs:
                        segs.append(text_seg("\n"))
                    segs.extend(parse_inline(ql))
                blocks.append(({
                    "type": "callout",
                    "callout": {
                        "icon": {"type": "emoji", "emoji": "📋"},
                        "rich_text": segs
                    }
                }, []))
            else:
                segs = parse_inline(combined)
                blocks.append(({
                    "type": "quote",
                    "quote": {"rich_text": segs}
                }, []))
            continue

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.+)', line)
        if m:
            blocks.append(({
                "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": parse_inline(m.group(2))}
            }, []))
            i += 1
            continue

        # Bullet list item (top-level)
        m = re.match(r'^- (.+)', line)
        if m:
            children = []
            bullet_text = m.group(1)
            i += 1
            # Collect indented children
            while i < len(lines) and re.match(r'^  +- ', lines[i]):
                child_text = re.sub(r'^  +- ', '', lines[i])
                children.append({
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": parse_bullet_text(child_text)}
                })
                i += 1
            blocks.append(({
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": parse_bullet_text(bullet_text)}
            }, children))
            continue

        # Empty line -> skip
        if not line.strip():
            i += 1
            continue

        # Paragraph
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3} |---|\||>|- |\d+\. )', lines[i]):
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            blocks.append(({
                "type": "paragraph",
                "paragraph": {"rich_text": parse_inline(' '.join(para_lines))}
            }, []))

    return blocks


def push_blocks(page_id, blocks_with_children):
    """Push blocks to a Notion page, handling nesting."""
    # First pass: add all top-level blocks in batches of 100
    top_blocks = [b for b, _ in blocks_with_children]
    parents_needing_children = []  # (index_in_response, children)

    for batch_start in range(0, len(top_blocks), 100):
        batch = top_blocks[batch_start:batch_start + 100]
        result = notion_api("PATCH", f"/blocks/{page_id}/children", {"children": batch})

        # Track which blocks need children
        for local_idx, (_, children) in enumerate(blocks_with_children[batch_start:batch_start + len(batch)]):
            if children:
                response_block = result["results"][local_idx]
                parents_needing_children.append((response_block["id"], children))

    # Second pass: add children to parent blocks
    for parent_id, children in parents_needing_children:
        for child_batch_start in range(0, len(children), 100):
            child_batch = children[child_batch_start:child_batch_start + 100]
            notion_api("PATCH", f"/blocks/{parent_id}/children", {"children": child_batch})


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <page_id> <markdown_file>")
        sys.exit(1)

    page_id = sys.argv[1]
    md_file = sys.argv[2]

    with open(md_file, 'r') as f:
        md_text = f.read()

    # Clear existing content
    print(f"Clearing {page_id}...")
    clear_page(page_id)

    # Convert and push
    print(f"Converting {md_file}...")
    blocks = md_to_blocks(md_text)
    print(f"Pushing {len(blocks)} blocks...")
    push_blocks(page_id, blocks)
    print(f"Done: {md_file} -> {page_id}")


if __name__ == "__main__":
    main()
