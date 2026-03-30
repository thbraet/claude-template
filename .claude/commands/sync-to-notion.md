---
description: Bidirectional sync of CRISP-DM docs with Notion — detects changes on both sides, shows conflicts, applies updates after user approval
---

You are orchestrating a bidirectional sync between local CRISP-DM markdown documents and their Notion counterparts.

## Notion API Access — Two Methods

### Method 1: MCP Tools (for page creation, search, reading properties)

The Notion MCP server exposes tools prefixed `mcp__notion__API-`. Use these for:
- **Creating pages**: `mcp__notion__API-post-page` (parent, properties, icon)
- **Searching**: `mcp__notion__API-post-search` (query, page_size)
- **Reading page metadata**: `mcp__notion__API-retrieve-a-page` (page_id)
- **Reading block children**: `mcp__notion__API-get-block-children` (block_id)
- **Deleting blocks**: `mcp__notion__API-delete-a-block` (block_id)
- **Updating page properties**: `mcp__notion__API-patch-page` (page_id, properties, icon)
- **Connectivity check**: `mcp__notion__API-get-self`

**CRITICAL LIMITATIONS of MCP tools:**
- `richTextRequest` has `additionalProperties: false` — **NO annotations (bold, italic, etc.) are supported**
- `blockObjectRequest` only allows `paragraph` and `bulleted_list_item` — **NO headings, dividers, tables, numbered lists, callouts, or quote blocks**
- `mcp__notion__API-post-page` `children` parameter expects block objects but schema is broken for this — **do NOT pass children when creating pages**
- `mcp__notion__API-patch-block-children` only accepts paragraph and bulleted_list_item — **cannot add styled content**

### Method 2: Direct Notion REST API via curl (for ALL styled content)

**ALWAYS use curl for pushing page content.** The `$NOTION_TOKEN` environment variable is available.

```bash
curl -s -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"children": [...]}'
```

This supports the full Notion block API:
- `heading_2`, `heading_3` — for `##` and `###`
- `paragraph` — with `annotations` (bold, italic, code, strikethrough, underline, color)
- `bulleted_list_item` — with annotations
- `numbered_list_item` — for `1.` `2.` lists
- `callout` — with icon + rich_text (used for metadata blocks like `> **Project:** ...`)
- `divider` — for `---`
- `table` + `table_row` children — for markdown tables
- `quote` — for `>` blockquotes
- Nested children — by appending to a block's ID instead of the page ID

Also use curl to **read block children** when you need the full block structure including types and annotations:
```bash
curl -s "https://api.notion.com/v1/blocks/${PAGE_ID}/children?page_size=100" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

And to **delete blocks**:
```bash
curl -s -X DELETE "https://api.notion.com/v1/blocks/${BLOCK_ID}" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

## Sync State

The file `.notion-sync.json` (gitignored) tracks the mapping between local files and Notion pages. Structure:

```json
{
  "project_name": "Store Capacity Forecast",
  "notion_parent_page_id": "<user-provided>",
  "notion_project_page_id": "<created-by-init>",
  "phase_pages": {
    "1-business-understanding": "<notion-page-id>",
    "2-data-understanding": "<notion-page-id>"
  },
  "documents": {
    "docs/crisp-dm/1-business-understanding/1.1-business-objectives.md": {
      "notion_page_id": "<notion-page-id>",
      "phase": "1-business-understanding",
      "title": "1.1 Business Objectives",
      "last_sync_local_hash": "<sha256-prefix>",
      "last_sync_notion_hash": "<sha256-prefix>",
      "last_synced_at": "2026-03-27T10:00:00Z"
    }
  }
}
```

**Hashing for change detection**: Normalize text by collapsing all whitespace to single spaces and trimming, then SHA-256 first 16 hex chars:
```bash
cat "<file>" | tr -s '[:space:]' ' ' | sed 's/^ //;s/ $//' | shasum -a 256 | cut -c1-16
```

## CRISP-DM Page Structure

When initializing, create this hierarchy under the user-provided parent page:

```
<Project Name>                          ← project page (icon: 📊)
├── 1. Business Understanding           ← phase subpage (icon: 🎯)
│   ├── 1.1 Business Objectives         ← document page
│   ├── 1.2 Situation Assessment
│   ├── 1.3 Data Mining Goals
│   └── 1.4 Project Plan
├── 2. Data Understanding               ← (icon: 🔍)
│   ├── 2.1 Data Collection
│   ├── 2.2 Data Description
│   ├── 2.3 Data Exploration
│   └── 2.4 Data Quality
├── 3. Data Preparation                 ← (icon: 🔧)
│   ├── 3.1 Select Data
│   ├── 3.2 Clean Data
│   ├── 3.3 Construct Data
│   ├── 3.4 Integrate Data
│   └── 3.5 Format Data
├── 4. Modeling                         ← (icon: 🤖)
│   ├── 4.1 Select Modeling Techniques
│   ├── 4.2 Generate Test Design
│   ├── 4.3 Build Model
│   └── 4.4 Assess Model
├── 5. Evaluation                       ← (icon: 📏)
│   ├── 5.1 Evaluate Results
│   ├── 5.2 Review Process
│   └── 5.3 Determine Next Steps
└── 6. Deployment                       ← (icon: 🚀)
    ├── 6.1 Plan Deployment
    ├── 6.2 Plan Monitoring & Maintenance
    ├── 6.3 Produce Final Report
    └── 6.4 Review Project
```

Local file mapping: `docs/crisp-dm/<phase-key>/<doc-filename>.md`
- Phase key: `1-business-understanding`, `2-data-understanding`, etc.
- Doc filename: `1.1-business-objectives.md`, `2.3-data-exploration.md`, etc.

## Prerequisites Check

Before doing anything:

1. Call `mcp__notion__API-get-self`. If it fails:
   > The Notion MCP server is not connected. Make sure `NOTION_TOKEN` is set and restart Claude Code.

2. Also verify `$NOTION_TOKEN` is set (needed for curl): `echo $NOTION_TOKEN | head -c 10`

3. Read `.notion-sync.json`. If it doesn't exist, run **First-Time Initialization**.

## First-Time Initialization

1. Ask the user for their **Notion parent page ID**: "Paste the Notion page URL or ID where the CRISP-DM subpages should live."

2. Get the project name from `.claude/CLAUDE.md`.

3. Create the page hierarchy using `mcp__notion__API-post-page`:
   - **Do NOT pass `children`** — the schema is broken for this. Create pages empty, then add content via curl.
   - First: project page under parent.
   - Then: 6 phase subpages under project (parallel).
   - Then: all document pages under their phase subpages (parallel, up to 24 calls).

4. For any document page where a local markdown file exists, push its content using the **Markdown → Notion Blocks** conversion via curl (see below).

5. Write `.notion-sync.json` with all page ID mappings and current content hashes.

6. Report the created structure to the user.

## Markdown → Notion Blocks Conversion (Pushing to Notion)

**ALWAYS use curl to push content**, never MCP tools for block content.

### Conversion Rules

Parse the markdown line by line and convert to Notion block JSON:

| Markdown | Notion Block Type | Notes |
|---|---|---|
| `# Heading` | Page title (already set) | Skip — the `#` heading IS the page title |
| `## Heading` | `heading_2` | |
| `### Heading` | `heading_3` | |
| `---` | `divider` | |
| `> **Key:** value` (metadata block) | `callout` with icon 📋 | When blockquote contains key-value metadata |
| `> text` | `quote` | Regular blockquotes |
| `- **Label:** text` | `bulleted_list_item` with bold annotation on label | Split into two rich_text segments |
| `- plain text` | `bulleted_list_item` | |
| `  - nested text` | `bulleted_list_item` as **child of parent** | See nesting rules below |
| `1. text` | `numbered_list_item` | |
| `| col | col |` (table) | `table` with `table_row` children | See table rules below |
| Plain paragraph | `paragraph` | |
| `**bold**` in text | `annotations: {"bold": true}` on that text segment | |
| `*italic*` in text | `annotations: {"italic": true}` | |
| `` `code` `` in text | `annotations: {"code": true}` | |

### Nesting / Indentation Rules

**This is critical.** Markdown indentation (`  - item`) means nested children in Notion.

- Top-level bullets are added as children of the **page**.
- Indented bullets (2+ spaces before `-`) are children of the **preceding top-level bullet block**.
- You CANNOT add nested children in the same API call as the parent. You must:
  1. First call: add the parent bullet to the page → get its block ID from the response
  2. Second call: add child bullets to `https://api.notion.com/v1/blocks/{PARENT_BLOCK_ID}/children`

**Strategy for efficiency**: Group consecutive indented items. After adding a batch of top-level blocks, scan the response for any that need children, then make follow-up calls for each parent that has children.

### Table Rules

Markdown tables convert to Notion `table` blocks:

```json
{
  "type": "table",
  "table": {
    "table_width": <number_of_columns>,
    "has_column_header": true,
    "has_row_header": false,
    "children": [
      {
        "type": "table_row",
        "table_row": {
          "cells": [
            [{"type": "text", "text": {"content": "Cell 1"}, "annotations": {"bold": true}}],
            [{"type": "text", "text": {"content": "Cell 2"}}]
          ]
        }
      }
    ]
  }
}
```

- Skip the separator row (`|---|---|`)
- First row gets bold annotations (header)
- Empty cells: use `[]` (empty array)
- Table rows MUST be included as `children` of the table block in the same API call

### Rich Text with Annotations

When text contains bold/italic/code markers, split into multiple `rich_text` segments:

```json
"rich_text": [
  {"type": "text", "text": {"content": "Label: "}, "annotations": {"bold": true}},
  {"type": "text", "text": {"content": "the rest of the text"}}
]
```

### Batch Size

The Notion API accepts up to **100 children per PATCH call**. If a page has more than 100 blocks, split into multiple sequential calls.

### Updating Existing Page Content

To replace a page's content (push local changes):
1. Fetch all existing block IDs: `GET /v1/blocks/{page_id}/children`
2. Delete each block: `DELETE /v1/blocks/{block_id}` (parallel, batch in shell loop)
3. Add new blocks via `PATCH /v1/blocks/{page_id}/children`

## Notion Blocks → Markdown Conversion (Pulling from Notion)

When pulling from Notion to local markdown:

1. Fetch all blocks: `GET /v1/blocks/{page_id}/children?page_size=100`
2. For each block with `has_children: true` (except tables), recursively fetch its children
3. Convert using these rules:

| Notion Block | Markdown |
|---|---|
| `heading_2` | `## text` |
| `heading_3` | `### text` |
| `divider` | `---` |
| `callout` | `> **Key:** value` (reconstruct blockquote metadata) |
| `quote` | `> text` |
| `paragraph` | Plain text (empty paragraph = blank line) |
| `bulleted_list_item` | `- text` (indent children with 2 spaces: `  - text`) |
| `numbered_list_item` | `1. text` |
| `table` | Pipe-delimited markdown table with separator row |

4. For rich_text with annotations:
   - `bold: true` → wrap in `**...**`
   - `italic: true` → wrap in `*...*`
   - `code: true` → wrap in `` `...` ``

## Sync Workflow

Every time this command runs after initialization:

### Step 1 — Gather state from both sides

For every document tracked in `.notion-sync.json`:

1. **Local side**: Check if file exists. If yes, compute content hash.
2. **Notion side**: Fetch page block children via curl, extract plain text, compute hash.
3. **Compare** both current hashes against `last_sync_*` hashes:
   - Both unchanged → `up_to_date`
   - Only local hash differs → `local_changed`
   - Only Notion hash differs → `notion_changed`
   - Both differ → `conflict`

Also scan `docs/crisp-dm/` for local files NOT in sync state → `new_local`.

**Performance**: Use parallel curl calls in bash for fetching multiple Notion pages simultaneously.

### Step 2 — Present findings

Show a summary table:

```
| Document                  | Status         | Action needed    |
|---------------------------|----------------|------------------|
| 1.1 Business Objectives   | Local changed  | Push to Notion   |
| 1.2 Situation Assessment  | Notion changed | Pull to local    |
| 2.1 Data Collection       | CONFLICT       | Resolve          |
| 1.4 Project Plan          | Up to date     | —                |
| 3.1 Select Data           | New local      | Create in Notion |
```

If everything is up to date, say so and stop.

### Step 3 — Handle each category (with user approval)

**Local-only changes** (push to Notion):
- List the files. Ask: "Push these to Notion?"
- If approved: read local markdown, clear existing Notion blocks, push new styled blocks via curl.
- Update sync state hashes.

**Notion-only changes** (pull to local):
- List the pages. Ask: "Pull these to local files?"
- If approved: fetch Notion blocks, convert to markdown, write to local file.
- Update sync state hashes.

**Conflicts** (both sides changed):
For each conflict:
1. Read local file and fetch Notion content.
2. Present comparison of differences.
3. Ask: **keep local**, **keep notion**, or **merge**.
4. Apply choice. Update sync state.

**New local files** (not yet tracked):
- List files. Ask: "Create Notion pages for these?"
- If approved: create page via MCP tool, push content via curl, add to sync state.

### Step 4 — Save state and summarize

1. Write updated `.notion-sync.json`.
2. Show summary of all actions taken.

## Error Handling

- If Notion API call fails, show error and suggest: check integration access, NOTION_TOKEN validity, page IDs still valid.
- If local file in sync state no longer exists: warn and ask to remove or pull from Notion.
- If Notion page in sync state no longer exists: warn and ask to remove or re-create.

## Important Rules

- **NEVER auto-apply changes without user approval.** Always present status and confirm.
- **NEVER overwrite a conflicting file** without showing both versions.
- **Always run full status check first** — never push/pull blindly.
- **Sync state is source of truth** for last synced. Always update after every successful operation.
- **ALWAYS use curl for pushing/reading styled content** — MCP tools cannot handle formatting.
- **Use MCP tools only for**: creating pages (empty), searching, reading page properties, deleting blocks.
- **Handle nesting in a separate pass** — add parent blocks first, then nest children using parent block IDs from the response.
