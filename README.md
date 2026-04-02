# Claude Code Template for Colruyt Group

A reusable template that configures [Claude Code](https://docs.anthropic.com/en/docs/claude-code) for data science projects following the **CRISP-DM** methodology.

## Quick Start

### As a Git Submodule (recommended)

Add this template as the `.claude/` directory of your project:

```bash
cd /path/to/my-project
git submodule add https://github.com/thbraet/claude-template.git .claude
```

Then create a root `CLAUDE.md` in your project with project-specific context:

```markdown
# Project: My Project Name

@.claude/CLAUDE.md

## Business Objective
...

## Data Sources
...
```

### Update the Submodule

```bash
git submodule update --remote .claude
git add .claude
git commit -m "chore: update claude-template submodule"
```

### Standalone (copy-paste)

```bash
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template
cp -r /tmp/claude-template/.claude /path/to/my-project/
rm -rf /tmp/claude-template

# Add Claude-specific entries to your .gitignore
echo -e '\n# Claude Code\n.claude/settings.local.json\n.claude/agent-memory-local/' >> /path/to/my-project/.gitignore
```

## What's Included

| Type | Count | Details |
|---|---|---|
| **Rules** | 11 | Security, coding standards, git workflow, compliance, data science, notebook standards, model governance, etc. |
| **Skills** | 30+ | CRISP-DM task skills covering all 6 phases |
| **Agents** | 9 | Phase agents + code review, data quality monitor, stakeholder translator |
| **Commands** | 27+ | CRISP-DM task commands + `/status`, `/next`, `/sync-to-notion` |
| **Plugins** | 1 | colruyt-ds local plugin |
| **MCP Servers** | 3 | GitLab, Postgres, Notion |
| **Hooks** | 5 | Large file guard, PII scanner, notebook lint, data leakage check, phase gate |
| **Docs** | 5 | Config reference, team customization, CRISP-DM workflow, framework recommendations, MCP catalog |

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
claude-template/                       # Mounts as .claude/ in consumer projects
├── README.md
├── .gitignore
├── CLAUDE.md                          # Generic Colruyt/CRISP-DM conventions
├── .mcp.json                          # MCP server configuration
├── settings.json                      # Permissions, model, hooks, plugins
├── settings.local.json.example        # Personal overrides reference
├── CRISP-DM-manual.md                 # Full CRISP-DM reference model
├── docs/
│   ├── CONFIGURATION-REFERENCE.md
│   ├── CRISP-DM-WORKFLOW.md
│   ├── FRAMEWORK-RECOMMENDATIONS.md
│   ├── MCP-SERVERS-CATALOG.md
│   └── TEAM-CUSTOMIZATION.md
├── scripts/
│   ├── setup.sh                       # Project setup script
│   └── hooks/                         # PreToolUse hooks
├── rules/                             # Glob-scoped rules
├── skills/                            # CRISP-DM task skills
├── agents/                            # Phase agents
├── commands/                          # Task + utility commands
└── plugins/colruyt-ds/                # Local plugin scaffold
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

- [Configuration Reference](docs/CONFIGURATION-REFERENCE.md)
- [Team Customization](docs/TEAM-CUSTOMIZATION.md)
- [CRISP-DM Workflow](docs/CRISP-DM-WORKFLOW.md)
- [Framework Recommendations](docs/FRAMEWORK-RECOMMENDATIONS.md)
- [MCP Servers Catalog](docs/MCP-SERVERS-CATALOG.md)

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. Push and open a pull request

## License

Internal use at Colruyt Group.
