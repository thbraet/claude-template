# CRISP-DM Framework — Improvement Recommendations

Status legend: `[ ]` = TODO, `[x]` = Done, `[-]` = Skipped

---

## 1. Hooks

| # | Hook | Trigger | Purpose | Status |
|---|---|---|---|---|
| 1.1 | Notebook lint | `PostToolUse` on Write to `*.ipynb` | Validate notebook has PROJECT_ROOT cell, markdown headers, no hardcoded paths | `[x]` |
| 1.2 | Data leakage check | `PostToolUse` on Write to `src/*.py` | Grep for `.fit(` calls that don't guard against test data | `[x]` |
| 1.3 | PII scanner | `PreToolUse` on Write to `data/` | Warn if writing files containing email/phone/BSN patterns | `[x]` |
| 1.4 | CRISP-DM phase gate | `PreToolUse` on skills | Verify prerequisite artifacts exist before running a later-phase skill | `[x]` |
| 1.5 | Large file guard | `PreToolUse` on `git commit` | Warn if staging files >10MB (should use DVC/LFS) | `[x]` |

## 2. Skills / Commands

| # | Command | Purpose | Status |
|---|---|---|---|
| 2.1 | `/data-lineage` | Generate a visual lineage graph: raw → cleaned → features → formatted → model | `[x]` |
| 2.2 | `/experiment-compare` | Compare 2+ MLflow runs side-by-side: metrics, parameters, feature importance diffs | `[x]` |
| 2.3 | `/validate-pipeline` | End-to-end smoke test: load raw → clean → features → format → predict | `[x]` |
| 2.4 | `/generate-submission` | Kaggle-specific: load best model, predict on test set, format submission CSV | `[x]` |
| 2.5 | `/assumption-audit` | Scan all CRISP-DM docs for pending assumptions and produce a summary report | `[x]` |
| 2.6 | `/init-project` | Bootstrap a new project: directory structure, templates, DVC, project CLAUDE.md | `[x]` |

## 3. Agents

| # | Agent | Purpose | Status |
|---|---|---|---|
| 3.1 | data-quality-monitor | Check data drift, schema changes, train/test distribution consistency | `[x]` |
| 3.2 | stakeholder-translator | Translate technical results into business language for summaries and presentations | `[x]` |

## 4. Rules

| # | Rule | Scope | Purpose | Status |
|---|---|---|---|---|
| 4.1 | experiment-tracking | `notebooks/4.*.ipynb` | Every modeling notebook must log to MLflow with run name, params, metrics | `[x]` |
| 4.2 | data-staging | `data/**` | Enforce raw → processed pipeline; prevent writing to `data/raw/` | `[x]` |
| 4.3 | feature-documentation | `src/features.py`, `notebooks/3.3*` | Every feature must have docstring with formula, source, rationale | `[x]` |
| 4.4 | reproducibility | `**/*.py`, `**/*.ipynb` | Random seeds must be set; no `shuffle=True` without explicit seed | `[x]` |

## 5. MCP Servers

| # | Server | Purpose | Status |
|---|---|---|---|
| 5.1 | MLflow MCP | Query experiments, compare metrics, fetch artifacts from Claude | `[ ]` |
| 5.2 | DVC MCP | Check data versions, pull snapshots, verify pipeline status | `[ ]` |
| 5.3 | Slack/Teams MCP | Post status updates to team channels on phase completion | `[ ]` |
| 5.4 | Jira/Linear MCP | Sync CRISP-DM tasks with project tracker | `[ ]` |

## 6. Workflow Improvements

| # | Improvement | Purpose | Status |
|---|---|---|---|
| 6.1 | Phase transition checklist | `/complete-phase N` validates all artifacts, assumptions, generates completion summary | `[x]` |
| 6.2 | Automated doc cross-linking | `/crosslink-docs` verifies and fixes Source Documents references | `[x]` |
| 6.3 | Template variable substitution | Handled by `/init-project` skill (section 2.6) | `[x]` |

## 7. Quality-of-Life

| # | Addition | Purpose | Status |
|---|---|---|---|
| 7.1 | Institutional memory patterns | Save common project patterns so future projects inherit team knowledge | `[x]` |
| 7.2 | `.claude/prompts/` | Pre-built prompt templates for stakeholder explanations, risk assessments | `[-]` Skipped — redundant with stakeholder-translator agent and existing skills |
