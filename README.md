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
| **Rules** | 11 | Security, coding standards, git workflow, compliance, data science, notebook standards, model governance, reproducibility, etc. |
| **Skills** | 34 | CRISP-DM task skills covering all 6 phases + cross-cutting concerns |
| **Agents** | 9 | Phase agents + code review, data quality monitor, stakeholder translator |
| **Commands** | 37 | 28 CRISP-DM task commands + 9 utility commands (`/status`, `/next`, `/sync-to-notion`, etc.) |
| **Plugins** | 1 | colruyt-ds local plugin |
| **MCP Servers** | 3 | GitLab, Postgres (read-only), Notion |
| **Hooks** | 5 | Large file guard, PII scanner, notebook lint, data leakage check, phase gate |
| **Docs** | 5 | Config reference, team customization, CRISP-DM workflow, framework recommendations, MCP catalog |

## CRISP-DM Coverage

Each CRISP-DM phase has a dedicated agent and task-level skills/commands:

| Phase | Agent | Commands |
|---|---|---|
| 1. Business Understanding | `business-understanding` | `/define-business-objectives`, `/assess-situation`, `/determine-data-mining-goals`, `/produce-project-plan` |
| 2. Data Understanding | `data-understanding` | `/collect-initial-data`, `/describe-data`, `/explore-data`, `/verify-data-quality` |
| 3. Data Preparation | `data-preparation` | `/select-data`, `/clean-data`, `/construct-data`, `/integrate-data`, `/format-data` |
| 4. Modeling | `modeling` | `/select-modeling-techniques`, `/generate-test-design`, `/build-model`, `/assess-model` |
| 5. Evaluation | `evaluation` | `/evaluate-results`, `/review-process`, `/determine-next-steps` |
| 6. Deployment | `deployment` | `/plan-deployment`, `/plan-monitoring`, `/produce-final-report`, `/review-project` |

Utility commands: `/status`, `/next`, `/sync-to-notion`, `/assumption-audit`, `/crosslink-docs`, `/data-lineage`, `/experiment-compare`, `/generate-submission`, `/validate-pipeline`, `/review-mr`

## Directory Structure

```
claude-template/                       # Mounts as .claude/ in consumer projects
├── CLAUDE.md                          # Colruyt/CRISP-DM conventions
├── CRISP-DM-manual.md                 # Full CRISP-DM reference model
├── settings.json                      # Permissions, model, hooks, plugins
├── settings.local.json.example        # Personal overrides reference
├── .mcp.json                          # MCP server configuration
├── agents/                            # 9 phase + support agents
├── commands/                          # 37 task + utility commands
├── skills/                            # 34 CRISP-DM task skills
├── rules/                             # 11 glob-scoped rules
├── scripts/
│   ├── setup.sh                       # Project setup script
│   └── hooks/                         # 5 PreToolUse/PostToolUse hooks
├── plugins/colruyt-ds/                # Local plugin scaffold
└── docs/
    ├── CONFIGURATION-REFERENCE.md
    ├── CRISP-DM-WORKFLOW.md
    ├── FRAMEWORK-RECOMMENDATIONS.md
    ├── MCP-SERVERS-CATALOG.md
    └── TEAM-CUSTOMIZATION.md
```

## Configuration

### `settings.json` (shared, committed)

Pre-configured with:
- Permissions for common data science tools (jupyter, pytest, mlflow, dvc, make)
- Deny rules for destructive operations (`rm -rf`, `rm -r`, `git push --force`, `git push -f`, `git reset --hard`, `eval`, `python -c`, piped `curl`/`wget`)
- PreToolUse hooks that flag access to sensitive files (`.env`, `.pem`, `.key`, `.secret`, `.credential`, etc.)
- PostToolUse hooks for notebook linting and data leakage detection
- Marketplace plugins: `compound-engineering` and `data`

### `settings.local.json` (personal, gitignored)

Copy `settings.local.json.example` to `settings.local.json` for personal overrides like API tokens, model preferences, or extra permissions. Store secrets as environment variables in your shell profile and reference them via `${ENV_VAR}` syntax -- never store plaintext tokens in config files.

### `.mcp.json` (MCP servers)

Pre-configured with GitLab, Postgres (read-only), and Notion servers. Tokens are referenced via `${ENV_VAR}` syntax and resolved from environment variables.

## Security

This template enforces several security guardrails:

- **Sensitive file detection**: PreToolUse hook prompts before accessing `.env`, `.pem`, `.key`, `.secret`, `.credential` files
- **PII scanning**: PreToolUse hook scans file writes for personally identifiable information
- **Data leakage checks**: PostToolUse hook validates that preprocessing isn't fit on test data
- **Large file guard**: PreToolUse hook prevents accidental commits of large data files
- **Phase gating**: PreToolUse hook ensures skills are invoked in proper CRISP-DM order
- **Deny list**: Blocks destructive shell commands and arbitrary code execution via `python -c` / `eval`

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
