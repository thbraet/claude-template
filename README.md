# Claude Code Template for Colruyt Group

A copy-paste template that configures Claude Code for data science projects following the **CRISP-DM** methodology.

## Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed: `npm install -g @anthropic-ai/claude-code`

### Scenario 1: New (Greenfield) Project

```bash
# Copy template files into your project
cp -r /path/to/claude-template/.claude /path/to/my-project/
cp /path/to/claude-template/CLAUDE.md /path/to/my-project/
cp /path/to/claude-template/.mcp.json /path/to/my-project/
cat /path/to/claude-template/.gitignore.claude >> /path/to/my-project/.gitignore

# Edit placeholders in CLAUDE.md and .claude/CLAUDE.md for your project
```

### Scenario 2: Existing (Brownfield) Project

Same as greenfield. If `.claude/` already exists, review and merge manually. Template files have clear placeholder sections.

### Scenario 3: Team Customization

Fork the template repo and customize for your team:

```bash
git clone https://gitlab.colruytgroup.com/devtools/claude-template.git
# Add team-specific rules, skills, agents
# See docs/TEAM-CUSTOMIZATION.md
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
