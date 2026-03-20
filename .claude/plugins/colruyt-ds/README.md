# Colruyt DS Plugin

This plugin bundles Colruyt Group's data science standards, CRISP-DM workflows, and ML governance tools for Claude Code.

## What This Plugin Provides

- **Rules**: Security, coding standards, git workflow, compliance, data science best practices, notebook standards, model governance
- **Skills**: 22 slash commands covering all 6 CRISP-DM phases plus general development tasks
- **Agents**: 7 specialized agents for security review, documentation, EDA, data quality, ML review, notebook review, and experiment tracking
- **Commands**: 3 legacy commands for summarization, model explanation, and CRISP-DM status

## Usage

This plugin is automatically activated when the `.claude/` directory is present in a project. Teams can extend it by adding domain-specific skills, agents, and rules.

## Extending

To add team-specific capabilities:
1. Add new skills to `.claude/skills/your-skill/SKILL.md`
2. Add new agents to `.claude/agents/your-agent.md`
3. Add new rules to `.claude/rules/your-rule.md`
