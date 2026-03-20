# Claude Code Template for Colruyt Group

A copy-paste template that configures [Claude Code](https://docs.anthropic.com/en/docs/claude-code) for data science projects following the **CRISP-DM** methodology.

## Quick Start

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed: `npm install -g @anthropic-ai/claude-code`

### Scenario 1: New (Greenfield) Project

```bash
# Clone the template
git clone https://github.com/thbraet/claude-template.git

# Copy template files into your project
cp -r claude-template/.claude /path/to/my-project/
cp claude-template/CLAUDE.md /path/to/my-project/
cp claude-template/.mcp.json /path/to/my-project/
cat claude-template/.gitignore.claude >> /path/to/my-project/.gitignore

# Edit placeholders in CLAUDE.md and .claude/CLAUDE.md for your project
```

### Scenario 2: Existing (Brownfield) Project

```bash
# Clone the template into a temporary directory
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template

# Copy into your existing project
cd /path/to/my-project

# Safe to copy directly -- these won't overwrite existing project files
cp -r /tmp/claude-template/.claude/rules/ .claude/rules/
cp -r /tmp/claude-template/.claude/skills/ .claude/skills/
cp -r /tmp/claude-template/.claude/agents/ .claude/agents/
cp -r /tmp/claude-template/.claude/commands/ .claude/commands/
cp -r /tmp/claude-template/.claude/plugins/ .claude/plugins/

# These files may need manual merging if they already exist
# Review before overwriting:
#   .claude/settings.json    -- merge permissions, hooks, env
#   CLAUDE.md                -- merge org instructions with your existing ones
#   .mcp.json                -- merge server definitions
cp -n /tmp/claude-template/.claude/settings.json .claude/settings.json
cp -n /tmp/claude-template/.claude/settings.local.json.example .claude/settings.local.json.example
cp -n /tmp/claude-template/.claude/CLAUDE.md .claude/CLAUDE.md
cp -n /tmp/claude-template/CLAUDE.md ./CLAUDE.md
cp -n /tmp/claude-template/.mcp.json ./.mcp.json

# Append Claude-specific gitignore entries (safe to run multiple times)
grep -qxF '.claude/settings.local.json' .gitignore 2>/dev/null || cat /tmp/claude-template/.gitignore.claude >> .gitignore

# Clean up
rm -rf /tmp/claude-template

# Edit placeholders in CLAUDE.md and .claude/CLAUDE.md for your project
```

> **Note**: `cp -n` (no-clobber) skips files that already exist. If you want to compare
> your existing files with the template versions, use `diff` before overwriting:
> ```bash
> diff .claude/settings.json /tmp/claude-template/.claude/settings.json
> ```

### Scenario 3: Team Customization

Fork this repo and customize for your team:

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/<your-org>/claude-template.git

# Add team-specific rules, skills, agents
# See docs/TEAM-CUSTOMIZATION.md
```

To stay up to date with the upstream template:

```bash
git remote add upstream https://github.com/thbraet/claude-template.git
git fetch upstream
git merge upstream/main
```

## What's Included

| Type | Count | Details |
|---|---|---|
| **Rules** | 7 | 4 general + 3 data science (glob-scoped) |
| **Skills** | 22 | 4 general + 3 per CRISP-DM phase (6 phases) |
| **Agents** | 7 | 2 general + 5 data science |
| **Legacy Commands** | 3 | summarize, explain-model, crisp-status |
| **Plugins (local)** | 1 | colruyt-ds scaffold |
| **Plugins (marketplace)** | 2 | compound-engineering, data (10+ skills) |
| **MCP Servers** | 6 | GitLab, filesystem, postgres, sqlite, memory, fetch |
| **Hooks** | 1 | PreToolUse sensitive file guard |
| **CLAUDE.md files** | 2 | Root (org+CRISP-DM), .claude/ (project template) |
| **Docs** | 4 | Config reference, team customization, CRISP-DM workflow, MCP catalog |

## CRISP-DM Skills by Phase

| Phase | Skills |
|---|---|
| 1. Business Understanding | `/init-ds-project`, `/project-charter`, `/success-criteria` |
| 2. Data Understanding | `/eda-notebook`, `/data-dictionary`, `/data-quality` |
| 3. Data Preparation | `/feature-doc`, `/leakage-check`, `/data-validation` |
| 4. Modeling | `/baseline-model`, `/experiment-setup`, `/error-analysis` |
| 5. Evaluation | `/model-card`, `/fairness-audit`, `/model-comparison` |
| 6. Deployment | `/serving-api`, `/monitoring-config`, `/runbook` |

General skills: `/code-review`, `/adr`, `/incident-report`, `/mr-description`

## Agents

| Agent | Purpose |
|---|---|
| `security-reviewer` | OWASP vulnerability scanning |
| `documentation-writer` | Auto-generate documentation |
| `eda-assistant` | Exploratory data analysis |
| `data-quality-checker` | Data quality profiling |
| `ml-reviewer` | ML code best practices |
| `notebook-reviewer` | Notebook quality standards |
| `experiment-tracker` | Experiment comparison |

## Directory Structure

```
claude-template/
├── README.md
├── CLAUDE.md                          # Org-wide instructions
├── .claude/
│   ├── settings.json                  # Permissions, model, hooks
│   ├── settings.local.json.example    # Personal overrides reference
│   ├── CLAUDE.md                      # Project template with placeholders
│   ├── rules/                         # 7 glob-scoped rules
│   ├── skills/                        # 22 slash commands
│   ├── agents/                        # 7 specialized agents
│   ├── commands/                      # 3 legacy commands
│   └── plugins/colruyt-ds/            # Plugin scaffold
├── .mcp.json                          # MCP server configuration
├── .gitignore.claude                  # Claude-specific gitignore entries
└── docs/
    ├── CONFIGURATION-REFERENCE.md
    ├── TEAM-CUSTOMIZATION.md
    ├── CRISP-DM-WORKFLOW.md
    └── MCP-SERVERS-CATALOG.md
```

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
