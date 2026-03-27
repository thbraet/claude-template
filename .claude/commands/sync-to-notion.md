---
description: Bidirectional sync of CRISP-DM docs with Notion — detects changes on both sides, shows conflicts, applies updates after user approval
---

You are orchestrating a bidirectional sync between local CRISP-DM markdown documents and their Notion counterparts using the **Notion MCP tools** directly. No external scripts — you handle everything.

## Notion MCP Tools Reference

The Notion MCP server (configured in `.mcp.json`) exposes these tools (prefixed `mcp__notion__`):

| Tool | Purpose |
|---|---|
| `mcp__notion__notion-search` | Search workspace for pages by title |
| `mcp__notion__notion-fetch` | Retrieve page content and properties by URL or page ID |
| `mcp__notion__notion-create-pages` | Create one or more pages with properties and content |
| `mcp__notion__notion-update-page` | Modify page properties and content |
| `mcp__notion__notion-move-pages` | Relocate pages to new parent |
| `mcp__notion__notion-get-comments` | Retrieve page comments |
| `mcp__notion__notion-create-comment` | Add comments to pages |

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

**Hashing for change detection**: To compute a content hash, normalize the text by collapsing all whitespace to single spaces and trimming, then compute SHA-256 and take the first 16 hex characters. Use Bash:
```bash
cat "<file>" | tr -s '[:space:]' ' ' | sed 's/^ //;s/ $//' | shasum -a 256 | cut -c1-16
```

## CRISP-DM Page Structure

When initializing, create this hierarchy under the user-provided parent page:

```
<Project Name>                          ← project page
├── 1. Business Understanding           ← phase subpage
│   ├── 1.1 Business Objectives         ← document page
│   ├── 1.2 Situation Assessment
│   ├── 1.3 Data Mining Goals
│   └── 1.4 Project Plan
├── 2. Data Understanding
│   ├── 2.1 Data Collection
│   ├── 2.2 Data Description
│   ├── 2.3 Data Exploration
│   └── 2.4 Data Quality
├── 3. Data Preparation
│   ├── 3.1 Select Data
│   ├── 3.2 Clean Data
│   ├── 3.3 Construct Data
│   ├── 3.4 Integrate Data
│   └── 3.5 Format Data
├── 4. Modeling
│   ├── 4.1 Select Modeling Techniques
│   ├── 4.2 Generate Test Design
│   ├── 4.3 Build Model
│   └── 4.4 Assess Model
├── 5. Evaluation
│   ├── 5.1 Evaluate Results
│   ├── 5.2 Review Process
│   └── 5.3 Determine Next Steps
└── 6. Deployment
    ├── 6.1 Plan Deployment
    ├── 6.2 Plan Monitoring & Maintenance
    ├── 6.3 Produce Final Report
    └── 6.4 Review Project
```

Local file mapping convention: `docs/crisp-dm/<phase-key>/<doc-filename>.md`
- Phase key: `1-business-understanding`, `2-data-understanding`, etc.
- Doc filename: `1.1-business-objectives.md`, `2.3-data-exploration.md`, etc.

## Prerequisites Check

Before doing anything, verify:

1. The Notion MCP tools are available. Try calling `mcp__notion__notion-get-self` (fetch the tool first if needed). If it fails, tell the user:
   > The Notion MCP server is not connected. Make sure `NOTION_TOKEN` is set and restart Claude Code.

2. Read `.notion-sync.json` using the Read tool. If it doesn't exist, run the **First-Time Initialization** flow.

## First-Time Initialization

1. Ask the user for their **Notion parent page ID**. Explain: "Paste the Notion page URL or ID where the CRISP-DM subpages should live."

2. Get the project name from `.claude/CLAUDE.md` (suggest "Store Capacity Forecast" or whatever is configured).

3. Create the page hierarchy using `mcp__notion__notion-create-pages`:
   - First, create the **project page** under the parent page.
   - Then, create each **phase subpage** under the project page.
   - Then, for each phase, create the **document pages** under the phase subpage.
   - For any document page where a local markdown file already exists, include the markdown content when creating the page.

4. After each page is created, record its Notion page ID.

5. Write the complete `.notion-sync.json` state file with all page ID mappings and current content hashes.

6. Report the created structure to the user.

## Sync Workflow

Every time this command runs after initialization:

### Step 1 — Gather state from both sides

For every document tracked in `.notion-sync.json`:

1. **Local side**: Check if the local file exists. If yes, compute its content hash.
2. **Notion side**: Fetch the page content using `mcp__notion__notion-fetch` with the stored page ID. Convert the returned content to plain text / markdown and compute its hash.
3. **Compare** both current hashes against the `last_sync_*` hashes stored in the sync state:
   - Both unchanged → `up_to_date`
   - Only local hash differs → `local_changed`
   - Only Notion hash differs → `notion_changed`
   - Both differ → `conflict`

Also scan `docs/crisp-dm/` for any local markdown files that are NOT in the sync state → `new_local`.

**Performance**: Fetch all Notion pages in parallel where possible (multiple tool calls in one message).

### Step 2 — Present findings

Show a summary table to the user:

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
- List the files that changed locally.
- Ask: "Push these to Notion?"
- If approved: for each file, read local content, then use `mcp__notion__notion-update-page` to replace the Notion page content with the local markdown.
- Update sync state hashes.

**Notion-only changes** (pull to local):
- List the pages that changed in Notion.
- Ask: "Pull these to local files?"
- If approved: for each page, fetch Notion content via `mcp__notion__notion-fetch`, convert to markdown, write to local file using the Write tool.
- Update sync state hashes.

**Conflicts** (changed on both sides):
For EACH conflicting document:
1. Read the local file content.
2. Fetch the Notion page content.
3. Present a clear comparison — either a side-by-side summary of what differs, or key sections that diverged.
4. Ask the user:
   > **Conflict in [doc title]**. Both local and Notion versions changed since last sync.
   > - **keep local** — overwrite Notion with local version
   > - **keep notion** — overwrite local with Notion version
   > - **merge** — I'll combine both changes and show you the result for approval
5. Apply the user's choice:
   - **keep local**: update Notion page with local content
   - **keep notion**: write Notion content to local file
   - **merge**: intelligently merge changes from both, present the merged version to the user, wait for approval, then write to both sides
6. Update sync state hashes.

**New local files** (not yet tracked):
- List the files.
- Ask: "Create Notion pages for these?"
- If approved: determine the correct phase subpage from the file path, create the page using `mcp__notion__notion-create-pages` under the right phase parent, add to sync state.

### Step 4 — Save state and summarize

1. Write the updated `.notion-sync.json`.
2. Show a summary:
   - Files pushed to Notion
   - Files pulled from Notion
   - Conflicts resolved (and how)
   - New pages created
   - Errors encountered (if any)

## Markdown ↔ Notion Content Conversion

When **pushing to Notion** (`notion-update-page` or `notion-create-pages`):
- The Notion MCP tools accept markdown content directly. Pass the markdown content in the page content/body field.

When **pulling from Notion** (`notion-fetch`):
- The Notion MCP returns structured content. Convert it back to clean markdown preserving:
  - Headings (`#`, `##`, `###`)
  - Bullet lists and numbered lists
  - Bold, italic, inline code
  - Tables (pipe-delimited markdown tables)
  - Code blocks
  - Blockquotes
  - Horizontal rules (`---`)

## Error Handling

- If a Notion API call fails, show the error and suggest:
  - Check that the integration has access to the page (Share > Invite integration)
  - Check that `NOTION_TOKEN` is valid
  - Check that page IDs in `.notion-sync.json` are still valid (pages not deleted)
- If a local file in sync state no longer exists, warn the user and ask whether to remove it from tracking or pull from Notion.
- If a Notion page in sync state no longer exists, warn the user and ask whether to remove from tracking or re-create from local.

## Important Rules

- **NEVER auto-apply changes without user approval.** Always present the status and confirm first.
- **NEVER overwrite a conflicting file** without showing the user both versions.
- **Always run the full status check first** — never push/pull blindly.
- **Sync state is the source of truth** for what was last synced. Always update it after every successful operation.
- **Parallel fetches**: When checking Notion-side content for multiple pages, batch the fetch calls in parallel for speed.
