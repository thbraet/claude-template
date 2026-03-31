# Claude Code Template for Colruyt Group

A copy-paste template that configures [Claude Code](https://docs.anthropic.com/en/docs/claude-code) for data science projects following the **CRISP-DM** methodology.

## Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) (for Claude Code and npx-based MCP servers)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed: `npm install -g @anthropic-ai/claude-code`

### New (Greenfield) Project

```bash
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template

cp -r /tmp/claude-template/.claude /path/to/my-project/
cp /tmp/claude-template/CLAUDE.md /path/to/my-project/
cp /tmp/claude-template/.mcp.json /path/to/my-project/
cp /tmp/claude-template/CRISP-DM.md /path/to/my-project/

# Add Claude-specific entries to your .gitignore
echo -e '\n# Claude Code\n.claude/settings.local.json\n.claude/agent-memory-local/' >> /path/to/my-project/.gitignore

rm -rf /tmp/claude-template

# Edit placeholders in CLAUDE.md and .claude/CLAUDE.md for your project
```

### Existing (Brownfield) Project

```bash
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template
cd /path/to/my-project

# Safe to copy directly -- these won't overwrite existing project files
cp -r /tmp/claude-template/.claude/rules/ .claude/rules/
cp -r /tmp/claude-template/.claude/skills/ .claude/skills/
cp -r /tmp/claude-template/.claude/agents/ .claude/agents/
cp -r /tmp/claude-template/.claude/commands/ .claude/commands/
cp -r /tmp/claude-template/.claude/plugins/ .claude/plugins/

# These files may need manual merging if they already exist (cp -n = no-clobber)
cp -n /tmp/claude-template/.claude/settings.json .claude/settings.json
cp -n /tmp/claude-template/.claude/settings.local.json.example .claude/settings.local.json.example
cp -n /tmp/claude-template/.claude/CLAUDE.md .claude/CLAUDE.md
cp -n /tmp/claude-template/CLAUDE.md ./CLAUDE.md
cp -n /tmp/claude-template/.mcp.json ./.mcp.json
cp -n /tmp/claude-template/CRISP-DM.md ./CRISP-DM.md

# Add Claude-specific entries to your .gitignore
grep -qxF '.claude/settings.local.json' .gitignore 2>/dev/null || \
  echo -e '\n# Claude Code\n.claude/settings.local.json\n.claude/agent-memory-local/' >> .gitignore

rm -rf /tmp/claude-template
```

> **Tip**: Compare before overwriting: `diff .claude/settings.json /tmp/claude-template/.claude/settings.json`

### Team Customization

Fork this repo and customize for your team:

```bash
git clone https://github.com/<your-org>/claude-template.git
# Add team-specific rules, skills, agents
# See docs/TEAM-CUSTOMIZATION.md
```

Stay up to date with upstream:

```bash
git remote add upstream https://github.com/thbraet/claude-template.git
git fetch upstream && git merge upstream/main
```

## What's Included

| Type | Count | Details |
|---|---|---|
| **Rules** | 7 | 4 general (security, coding standards, git workflow, compliance) + 3 data science (best practices, notebook standards, model governance) |
| **Skills** | 24 | CRISP-DM task skills covering all 6 phases |
| **Agents** | 6 | One per CRISP-DM phase |
| **Commands** | 27 | CRISP-DM task commands + `/status`, `/next`, `/sync-to-notion` |
| **Plugins** | 2 marketplace | compound-engineering, data |
| **MCP Servers** | 3 | GitLab, Postgres, Notion |
| **Hooks** | 1 | PreToolUse sensitive file guard |
| **CLAUDE.md** | 2 | Root (org-wide standards), `.claude/` (project-specific template) |
| **Docs** | 4 | Config reference, team customization, CRISP-DM workflow, MCP catalog |

## CRISP-DM Coverage

Each CRISP-DM phase has a dedicated agent and task-level skills/commands:

| Phase | Agent | Skills |
|---|---|---|
| 1. Business Understanding | `business-understanding` | `/define-business-objectives`, `/assess-situation`, `/determine-data-mining-goals`, `/produce-project-plan` |
| 2. Data Understanding | `data-understanding` | `/collect-initial-data`, `/describe-data`, `/explore-data`, `/verify-data-quality` |
| 3. Data Preparation | `data-preparation` | `/select-data`, `/clean-data`, `/construct-data`, `/integrate-data`, `/format-data` |
| 4. Modeling | `modeling` | `/select-modeling-techniques`, `/generate-test-design`, `/build-model`, `/assess-model` |
| 5. Evaluation | `evaluation` | `/evaluate-results`, `/review-process`, `/determine-next-steps` |
| 6. Deployment | `deployment` | `/plan-deployment`, `/plan-monitoring`, `/produce-final-report`, `/review-project` |

Utility commands: `/status` (phase progress dashboard), `/next` (suggest next task), `/sync-to-notion`

## Directory Structure

```
claude-template/
├── CLAUDE.md                          # Org-wide instructions (language, git, security, DS principles)
├── CRISP-DM.md                        # Full CRISP-DM reference model
├── .mcp.json                          # MCP server configuration (GitLab, Postgres, Notion)
├── .claude/
│   ├── CLAUDE.md                      # Project-specific template (fill in per project)
│   ├── settings.json                  # Permissions, model, hooks, plugins
│   ├── settings.local.json.example    # Personal overrides reference
│   ├── rules/                         # 7 glob-scoped rules
│   ├── skills/                        # 24 CRISP-DM task skills
│   ├── agents/                        # 6 phase agents
│   ├── commands/                      # 27 task + utility commands
│   └── plugins/colruyt-ds/            # Local plugin scaffold
└── docs/
    ├── CONFIGURATION-REFERENCE.md     # All config options explained
    ├── TEAM-CUSTOMIZATION.md          # How to fork and extend
    ├── CRISP-DM-WORKFLOW.md           # Skills mapped to CRISP-DM phases
    └── MCP-SERVERS-CATALOG.md         # Available MCP servers for data science
```

## Configuration

### `settings.json` (shared, committed)

Pre-configured with:
- Permissions for common data science tools (python, pip, conda, jupyter, pytest, mlflow, dvc, git)
- Deny rules for destructive operations (`rm -rf`, `git push --force`, `git reset --hard`)
- PreToolUse hook that flags access to sensitive files (`.env`, `.pem`, `.key`, etc.)
- Marketplace plugins: `compound-engineering` and `data`

### `settings.local.json` (personal, gitignored)

Copy `settings.local.json.example` to `settings.local.json` for personal overrides like API tokens, model preferences, or extra permissions.

### `.mcp.json` (MCP servers)

Pre-configured with GitLab, Postgres, and Notion servers. Tokens are referenced via `${ENV_VAR}` syntax and resolved from `settings.local.json` env vars.

## Documentation

- [Configuration Reference](docs/CONFIGURATION-REFERENCE.md) -- All config options
- [Team Customization](docs/TEAM-CUSTOMIZATION.md) -- How to fork and extend
- [CRISP-DM Workflow](docs/CRISP-DM-WORKFLOW.md) -- Skills mapped to phases
- [MCP Servers Catalog](docs/MCP-SERVERS-CATALOG.md) -- Available MCP servers

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. Push and open a pull request

## License

Internal use at Colruyt Group.
