---
description: Bidirectional sync of CRISP-DM docs with Notion — detects changes on both sides, shows conflicts, applies updates after user approval
---

You are orchestrating a bidirectional sync between local CRISP-DM markdown documents and their Notion counterparts. The Python script `scripts/notion_sync.py` handles API calls; you handle orchestration, conflict resolution, and user interaction.

## Prerequisites

Before running any sync commands, verify:

1. **NOTION_API_TOKEN** is set in the environment. If not, tell the user:
   > Set your Notion integration token: `export NOTION_API_TOKEN=ntn_...`
   > Create one at https://www.notion.so/my-integrations if needed.
   > Make sure the integration has access to the target page (Share > Invite integration).

2. **Sync state file** (`.notion-sync.json`) exists. If not, this is a first-time setup — run the initialization flow below.

## First-Time Initialization

If `.notion-sync.json` does not exist:

1. Ask the user for their Notion parent page ID (the page under which all CRISP-DM phase subpages will be created). Explain they can find it in the page URL: `notion.so/<workspace>/<page-title>-<PAGE_ID>`.
2. Ask for the project name (suggest using the project name from `.claude/CLAUDE.md`).
3. Run: `python scripts/notion_sync.py init --parent-page-id <ID> --project-name "<name>"`
4. Report the created page structure to the user.

## Sync Workflow

Every time this command runs (after initialization):

### Step 1 — Check status on both sides

Run:
```bash
python scripts/notion_sync.py status --json
```

Read the JSON output. It categorizes every tracked document into:
- `no_change` — identical on both sides since last sync
- `local_only` — changed locally but not in Notion → push candidate
- `notion_only` — changed in Notion but not locally → pull candidate
- `conflict` — changed on BOTH sides since last sync → needs resolution
- `new_local` — local file exists but is not yet tracked in Notion

### Step 2 — Present findings to the user

Show a clear summary table:

```
| Document                  | Status         | Action needed    |
|---------------------------|----------------|------------------|
| 1.1 Business Objectives   | Local changed  | Push to Notion   |
| 1.2 Situation Assessment  | Notion changed | Pull to local    |
| 2.1 Data Collection       | CONFLICT       | Resolve          |
| 1.4 Project Plan          | Up to date     | —                |
```

### Step 3 — Handle each category

**Local-only changes** (push candidates):
- Tell the user which files changed locally.
- Ask: "Push these local changes to Notion?"
- If approved, run `python scripts/notion_sync.py push <path>` for each.

**Notion-only changes** (pull candidates):
- Tell the user which pages changed in Notion.
- Ask: "Pull these Notion changes to local files?"
- If approved, run `python scripts/notion_sync.py pull <path>` for each.

**Conflicts** (changed on both sides):
- For EACH conflicting document:
  1. Read the local file with the Read tool.
  2. Get the Notion version: `python scripts/notion_sync.py content <path>`
  3. Show the user both versions side by side (or a summary of differences).
  4. Ask: "Which version should be kept? Options:
     - **local** — push local version to Notion (overwrites Notion changes)
     - **notion** — pull Notion version to local (overwrites local changes)
     - **merge** — I'll help you merge the two versions manually"
  5. If **merge**: create a merged version incorporating changes from both sides, show it to the user for approval, write it to the local file, then push to Notion.
  6. If **local**: run `python scripts/notion_sync.py push <path>`
  7. If **notion**: run `python scripts/notion_sync.py pull <path>`

**New local files** (not yet tracked):
- Tell the user these files exist locally but have no Notion counterpart.
- This means the file was created after `init`. Ask: "Should I create Notion pages for these and push the content?"
- If approved: you will need to add the document to the sync state and create a page under the correct phase page. Use the phase_pages mapping in `.notion-sync.json` to find the right parent, then run appropriate API calls.

### Step 4 — Summary

After all operations complete, show a summary of what was done:
- Files pushed to Notion
- Files pulled from Notion
- Conflicts resolved (and how)
- Any errors encountered

## Error Handling

- If the Notion API returns errors, show the error message and suggest the user check:
  - Integration token is valid
  - Integration has access to the pages (Share > Invite)
  - Page IDs in `.notion-sync.json` are still valid
- If a local file referenced in sync state no longer exists, warn the user and ask if it should be removed from tracking.

## Important Rules

- NEVER auto-apply changes without user approval. Always present and confirm first.
- NEVER overwrite a conflicting file without showing the user both versions.
- Always run status check first — never push/pull blindly.
- Treat the sync state file as the source of truth for what was last synced.
