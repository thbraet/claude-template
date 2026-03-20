# Team Customization Guide

How to fork the template and customize it for your team.

## Getting Started

1. Fork the template repo on GitHub:
   ```bash
   # Fork https://github.com/thbraet/claude-template on GitHub, then clone your fork
   git clone https://github.com/<your-org>/claude-template.git
   cd claude-template
   ```

2. Create a team-specific branch:
   ```bash
   git checkout -b team/your-team-name
   ```

3. Customize the components described below.

## What to Customize

### Rules (`.claude/rules/`)

Add team-specific rules:

```markdown
---
paths:
  - "src/your-domain/**/*.py"
---
# Your Team Rules

- [team-specific coding convention]
- [domain-specific requirement]
```

Example: a pricing team might add `pricing-rules.md` scoped to `src/pricing/**/*.py`.

### Skills (`.claude/skills/`)

Add team-specific slash commands:

```bash
mkdir -p .claude/skills/your-skill
```

Create `.claude/skills/your-skill/SKILL.md`:
```markdown
---
name: your-skill
description: What this skill does
argument-hint: "[expected input]"
user-invocable: true
---

# Your Skill

Instructions for Claude...
```

### Agents (`.claude/agents/`)

Add team-specific agents for specialized review or analysis:

```markdown
---
name: your-agent
description: What this agent does
tools: Read, Bash, Glob
model: opus
maxTurns: 10
---

You are a [role] at Colruyt Group...
```

### Settings (`.claude/settings.json`)

Extend permissions for team-specific tools:

```json
{
  "permissions": {
    "allow": [
      "Bash(your-team-tool *)"
    ]
  }
}
```

### CLAUDE.md

Add team context to the root `CLAUDE.md` under the team placeholder:

```markdown
<!-- TEAM: Add team-specific instructions below this line -->

## Team: [Your Team Name]
- Domain: [what your team works on]
- Data sources: [team-specific data sources]
- Key contacts: [who to ask for domain questions]
```

### MCP Servers (`.mcp.json`)

Add team-specific data sources:

```json
{
  "mcpServers": {
    "team-database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${TEAM_DATABASE_URL}"]
    }
  }
}
```

## Best Practices

1. **Don't remove org-level rules** -- only add to them
2. **Use glob scoping** in rules to limit them to relevant files
3. **Document customizations** in your team's CLAUDE.md section
4. **Keep skills focused** -- one task per skill
5. **Test skills** by running them in a sample project
6. **Sync with upstream** periodically to pick up template improvements

## Syncing with Upstream

```bash
git remote add upstream https://github.com/thbraet/claude-template.git
git fetch upstream
git merge upstream/main
# Resolve any conflicts in your customizations
```
