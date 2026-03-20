# Claude Code Template for Colruyt Group

## Context

Colruyt Group needs a simple, copy-paste template that configures Claude Code for data science projects following the **CRISP-DM** methodology. Developers copy a `.claude/` folder and `CLAUDE.md` into their project root and Claude is immediately configured with org standards, CRISP-DM workflows, data science skills, agents, rules, and MCP servers.

Two tiers of configuration:
- **Organization level**: Colruyt Group defaults baked into the template
- **Team level**: Teams fork the template repo and customize for their domain

**Target audience**: Data scientists at Colruyt Group following CRISP-DM (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment).

**Distribution**: Developers clone/download the template and copy its contents into their project. No setup scripts, no MDM, no user-level installation.

---

## What Gets Distributed

```
claude-template/
├── README.md                          # Master usage guide (3 scenarios)
│
├── CLAUDE.md                          # Root org-wide + CRISP-DM instructions
│
├── .claude/
│   ├── settings.json                  # Permissions, model, hooks, env, plugins
│   ├── settings.local.json.example    # Personal overrides reference
│   ├── CLAUDE.md                      # Project-level CRISP-DM template with placeholders
│   │
│   ├── rules/                         # === GLOB-SCOPED RULES ===
│   │   ├── security.md                # No hardcoded secrets, HTTPS-only, OWASP
│   │   ├── coding-standards.md        # Naming, error handling, structured logging
│   │   ├── git-workflow.md            # Branch naming, commit format, MR conventions
│   │   ├── compliance.md              # GDPR, PII handling, data retention
│   │   ├── data-science.md            # DS best practices: reproducibility, leakage, baselines
│   │   ├── notebook-standards.md      # Notebook naming, structure, documentation requirements
│   │   └── model-governance.md        # Model cards, experiment tracking, fairness, monitoring
│   │
│   ├── skills/                        # === CUSTOM SLASH COMMANDS ===
│   │   │
│   │   │  # -- General skills --
│   │   ├── code-review/SKILL.md       # /code-review
│   │   ├── adr/SKILL.md              # /adr -- Architecture Decision Record
│   │   ├── incident-report/SKILL.md   # /incident-report
│   │   ├── mr-description/SKILL.md    # /mr-description -- GitLab MR generator
│   │   │
│   │   │  # -- CRISP-DM Phase 1: Business Understanding --
│   │   ├── init-ds-project/SKILL.md   # /init-ds-project -- scaffold CRISP-DM project structure
│   │   ├── project-charter/SKILL.md   # /project-charter -- generate project charter
│   │   ├── success-criteria/SKILL.md  # /success-criteria -- map business KPIs to tech metrics
│   │   │
│   │   │  # -- CRISP-DM Phase 2: Data Understanding --
│   │   ├── eda-notebook/SKILL.md      # /eda-notebook -- generate EDA notebook template
│   │   ├── data-dictionary/SKILL.md   # /data-dictionary -- scaffold data dictionary from schema
│   │   ├── data-quality/SKILL.md      # /data-quality -- generate data quality assessment
│   │   │
│   │   │  # -- CRISP-DM Phase 3: Data Preparation --
│   │   ├── feature-doc/SKILL.md       # /feature-doc -- document a feature (name, formula, source)
│   │   ├── leakage-check/SKILL.md     # /leakage-check -- audit pipeline for data leakage
│   │   ├── data-validation/SKILL.md   # /data-validation -- generate validation suite
│   │   │
│   │   │  # -- CRISP-DM Phase 4: Modeling --
│   │   ├── baseline-model/SKILL.md    # /baseline-model -- generate baseline for problem type
│   │   ├── experiment-setup/SKILL.md  # /experiment-setup -- configure MLflow/W&B tracking
│   │   ├── error-analysis/SKILL.md    # /error-analysis -- analyze model errors
│   │   │
│   │   │  # -- CRISP-DM Phase 5: Evaluation --
│   │   ├── model-card/SKILL.md        # /model-card -- generate model card
│   │   ├── fairness-audit/SKILL.md    # /fairness-audit -- bias/fairness assessment
│   │   ├── model-comparison/SKILL.md  # /model-comparison -- compare experiments
│   │   │
│   │   │  # -- CRISP-DM Phase 6: Deployment --
│   │   ├── serving-api/SKILL.md       # /serving-api -- generate FastAPI serving endpoint
│   │   ├── monitoring-config/SKILL.md # /monitoring-config -- drift detection setup
│   │   └── runbook/SKILL.md           # /runbook -- generate operations runbook
│   │
│   ├── agents/                        # === CUSTOM SUBAGENTS ===
│   │   ├── security-reviewer.md       # Security-focused code review
│   │   ├── documentation-writer.md    # Documentation generation
│   │   ├── eda-assistant.md           # Exploratory data analysis assistant
│   │   ├── data-quality-checker.md    # Data quality profiling and issue detection
│   │   ├── ml-reviewer.md            # ML code review (leakage, reproducibility, best practices)
│   │   ├── notebook-reviewer.md       # Notebook quality review
│   │   └── experiment-tracker.md      # Summarize and compare experiment results
│   │
│   ├── commands/                      # === LEGACY COMMANDS ===
│   │   ├── summarize.md               # /summarize -- quick summary
│   │   ├── explain-model.md           # /explain-model -- SHAP/interpretability analysis
│   │   └── crisp-status.md            # /crisp-status -- show CRISP-DM phase progress
│   │
│   └── plugins/                       # === PLUGIN BUNDLES ===
│       └── colruyt-ds/
│           ├── plugin.json            # Plugin manifest
│           └── README.md              # What this plugin provides
│
├── .mcp.json                          # MCP servers (GitLab, databases, filesystem, etc.)
│
├── .gitignore.claude                  # Claude-specific gitignore entries
│
└── docs/
    ├── CONFIGURATION-REFERENCE.md     # Exhaustive config options reference
    ├── TEAM-CUSTOMIZATION.md          # How teams fork and customize
    ├── CRISP-DM-WORKFLOW.md           # How this template maps to CRISP-DM phases
    └── MCP-SERVERS-CATALOG.md         # Available MCP servers for data science
```

**Developer workflow**:
```bash
# Greenfield: copy everything
cp -r ~/claude-template/.claude /path/to/my-project/
cp ~/claude-template/CLAUDE.md /path/to/my-project/
cp ~/claude-template/.mcp.json /path/to/my-project/
cat ~/claude-template/.gitignore.claude >> /path/to/my-project/.gitignore

# Brownfield: same, but review before overwriting existing .claude/
```

---

## File Contents

### 1. Root `CLAUDE.md` (project root)

Organization identity, CRISP-DM context, and universal standards. This is the first thing Claude reads.

Contents:
- Colruyt Group context ("You are assisting a data scientist at Colruyt Group, a Belgian retail corporation")
- CRISP-DM methodology context: "Projects follow CRISP-DM. Always be aware of which phase (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment) the current work belongs to."
- Default language: English for all code, comments, documentation
- Commit message format: Conventional Commits with CRISP-DM phase prefix (`feat(modeling): add XGBoost baseline`, `fix(data-prep): resolve date parsing`)
- Branch naming: `feature/JIRA-123-short-description`, `bugfix/JIRA-456-short-description`
- MR description format: Summary, Changes, CRISP-DM Phase, Test Plan, Breaking Changes (GitLab terminology)
- Never commit: `.env`, credentials, PII, API keys, data files (use DVC/LFS), model artifacts >100MB, internal URLs
- Tooling: SonarQube for quality gates, Artifactory for packages, GitLab CI/CD, MLflow for experiment tracking
- Logging: structured JSON, include correlation IDs, use OpenTelemetry
- Security: no eval/exec, validate all inputs, use parameterized queries
- Data science principles: "Always establish a baseline before complex models. Fit preprocessing on train only. Log every experiment. Data is immutable. Explore in notebooks, productionize in scripts."
- `@.claude/CLAUDE.md` import for project-specific instructions
- Placeholder section: `<!-- TEAM: Add team-specific instructions below -->`
- Placeholder section: `<!-- PROJECT: Fill in project details below -->`

### 2. `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git branch *)",
      "Bash(git show *)",
      "Bash(git stash *)",
      "Bash(ls *)",
      "Bash(tree *)",
      "Bash(wc *)",
      "Bash(diff *)",
      "Bash(head *)",
      "Bash(tail *)",
      "Bash(sort *)",
      "Bash(uniq *)",
      "Bash(which *)",
      "Bash(echo *)",
      "Bash(cat *)",
      "Bash(find *)",
      "Bash(grep *)",
      "Bash(python *)",
      "Bash(pip *)",
      "Bash(conda *)",
      "Bash(jupyter *)",
      "Bash(pytest *)",
      "Bash(mlflow *)",
      "Bash(dvc *)",
      "Bash(make *)",
      "Read",
      "Edit",
      "Write",
      "Glob",
      "Grep",
      "WebFetch(domain:gitlab.colruytgroup.com)",
      "WebFetch(domain:confluence.colruytgroup.com)",
      "WebFetch(domain:artifactory.colruytgroup.com)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Bash(git reset --hard *)",
      "Bash(curl * | bash)",
      "Bash(wget * | bash)"
    ],
    "defaultMode": "default"
  },
  "model": "opus",
  "effortLevel": "medium",
  "autoMemoryEnabled": true,
  "enabledPlugins": {
    "compound-engineering@every-marketplace": true,
    "data@knowledge-work-plugins": true
  },
  "env": {
    "BASH_DEFAULT_TIMEOUT_MS": "30000",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1"
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "INPUT=$(cat); CMD=$(echo \"$INPUT\" | jq -r '.tool_input.command // empty'); if echo \"$CMD\" | grep -qiE '\\.(env|pem|key|crt|p12|pfx|jks)'; then echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",\"permissionDecisionReason\":\"Command references a sensitive file type\"}}'; fi",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

### 3. `.claude/settings.local.json.example`

```json
{
  "_comment": "Copy this file to settings.local.json for personal overrides. It is gitignored.",
  "model": "opus",
  "effortLevel": "high",
  "env": {
    "MAX_THINKING_TOKENS": "16000"
  }
}
```

### 4. `.claude/CLAUDE.md`

Project-specific CRISP-DM template with placeholders:

```markdown
# Project: [PROJECT_NAME]

## Business Objective
[What business problem are we solving? Link to project charter: docs/project_charter.md]

## CRISP-DM Phase Tracker
| Phase | Status | Key Artifacts |
|---|---|---|
| 1. Business Understanding | [Not Started/In Progress/Complete] | project_charter.md |
| 2. Data Understanding | [status] | EDA notebooks, data dictionary |
| 3. Data Preparation | [status] | Feature pipeline, validation suite |
| 4. Modeling | [status] | Baseline model, experiment logs |
| 5. Evaluation | [status] | Model card, fairness audit |
| 6. Deployment | [status] | Serving API, monitoring, runbook |

## Data Sources
| Source | Type | Access | Refresh | Description |
|---|---|---|---|---|
| [source] | [DB/API/File] | [how to access] | [frequency] | [what it contains] |

## Development
- Setup environment: `[conda env create / pip install]`
- Run tests: `[pytest]`
- Run pipeline: `[make data && make train && make evaluate]`
- Run EDA: `[jupyter lab]`

## Key Decisions
[Link to docs/adr/ for Architecture Decision Records]

## Conventions
[Project-specific conventions beyond org standards in root CLAUDE.md]

<!-- TEAM: Add team-specific instructions below -->

<!-- PROJECT: Add project-specific context below -->
```

### 5. `.claude/rules/security.md`

```markdown
---
paths:
  - "**/*"
---
# Security Rules

- Never hardcode secrets, API keys, passwords, tokens, or connection strings
- Use environment variables or vault references for all sensitive values
- Never log PII (names, emails, addresses, phone numbers, national registry numbers)
- Flag any use of eval(), exec(), or dynamic code execution
- All HTTP clients must use HTTPS -- no plain HTTP except localhost
- Use parameterized queries -- never concatenate user input into SQL
- Dependencies must come from approved registries (artifactory.colruytgroup.com)
- Validate and sanitize all external input at system boundaries
- Do not disable SSL/TLS certificate verification
- Do not commit .env, .pem, .key, .p12, .pfx, or .jks files
```

### 6. `.claude/rules/coding-standards.md`

```markdown
---
paths:
  - "**/*"
---
# Coding Standards

- Use descriptive, intention-revealing names for variables, functions, and classes
- Prefer explicit over implicit -- avoid magic numbers, unexplained constants
- Keep functions focused -- one responsibility per function
- Handle errors explicitly -- no empty catch blocks, no swallowed exceptions
- Use structured JSON logging with severity levels (DEBUG, INFO, WARN, ERROR)
- Include correlation IDs in log messages for distributed tracing
- Write self-documenting code -- add comments only for "why", not "what"
- Prefer composition over inheritance
- Keep cyclomatic complexity low -- extract complex conditionals into named functions
- Follow the principle of least surprise in API and function design
```

### 7. `.claude/rules/git-workflow.md`

```markdown
---
paths:
  - "**/*"
---
# Git Workflow

- Branch from `main` (never from feature branches unless explicitly coordinating)
- Branch naming: `feature/JIRA-123-short-description` or `bugfix/JIRA-456-short-description`
- Commit messages: Conventional Commits format
  - `feat: add user authentication endpoint`
  - `fix: resolve null pointer in order processing`
  - `chore: update dependency versions`
  - `docs: add API documentation for payments`
  - `refactor: extract validation logic into shared module`
  - `test: add integration tests for cart service`
- One logical change per commit -- do not mix refactoring with feature work
- Squash merge to main via GitLab merge requests
- MR title: under 72 characters, imperative mood
- MR description must include: Summary, Changes (bulleted), Test Plan
- Never force-push to shared branches
- Never commit directly to main
```

### 8. `.claude/rules/compliance.md`

```markdown
---
paths:
  - "**/*"
---
# Compliance & Privacy (GDPR)

- All processing of personal data must have a documented legal basis
- Implement data minimization -- only collect/store what is strictly necessary
- PII must be encrypted at rest and in transit
- Never log PII in application logs, error messages, or stack traces
- Support data subject rights: access, rectification, erasure, portability
- Data retention: follow project-specific retention policy, default to shortest practical period
- Cross-border data transfers require appropriate safeguards (SCCs, adequacy decisions)
- Anonymize or pseudonymize data in non-production environments
- Include privacy impact considerations when designing new features that handle personal data
- Audit trail: log who accessed what data and when (without logging the data itself)
```

### 9. `.claude/rules/data-science.md` (NEW)

```markdown
---
paths:
  - "**/*.py"
  - "**/*.ipynb"
  - "**/*.sql"
---
# Data Science Best Practices

- Always establish a baseline model before building complex models
- Fit all preprocessing (scalers, encoders, imputers) on training data only -- never on validation or test
- Set random seeds for all stochastic processes and document them (numpy, random, torch, sklearn)
- Every experiment must be logged: parameters, metrics, data version, code version, environment
- Raw data is immutable -- never modify original data files in place
- Explore in notebooks, productionize in scripts -- refactor reused notebook code into src/ modules
- Check for data leakage at every stage (target leakage, temporal leakage, preprocessing leakage)
- Pin all dependency versions (requirements.txt with ==, poetry.lock, conda-lock)
- Every result must be reproducible from raw data with a single command (make, dvc repro, etc.)
- Prefer pandas/polars for tabular data, not manual loops
- Use DVC or similar for data versioning -- never commit large data files to git
- Feature engineering code must be identical between training and serving
```

### 10. `.claude/rules/notebook-standards.md` (NEW)

```markdown
---
paths:
  - "**/*.ipynb"
---
# Notebook Standards

- Every notebook starts with a markdown cell: Title, Author, Date, CRISP-DM Phase, Purpose
- Use the naming convention: {number}-{phase}-{description}-{initials}.ipynb
  - Example: 01-du-eda-initial-exploration-jdoe.ipynb
  - Phase codes: bu (Business Understanding), du (Data Understanding), dp (Data Preparation), mod (Modeling), eval (Evaluation), dep (Deployment)
- Section headers must use markdown cells (##) for logical flow
- Markdown cells explain WHY, code cells show WHAT
- Every notebook ends with a Conclusions cell summarizing findings and next steps
- No magic numbers without explanation -- use named constants
- No hardcoded file paths -- use config files or environment variables
- Notebooks must run top-to-bottom without error (Kernel > Restart & Run All before committing)
- Keep notebooks focused -- one analysis question per notebook
- Import all libraries in the first code cell
- Suppress warnings only with documented justification
```

### 11. `.claude/rules/model-governance.md` (NEW)

```markdown
---
paths:
  - "**/*"
---
# Model Governance

- Every production model must have a model card (use /model-card to generate)
- Model cards must include: intended use, limitations, training data, metrics, fairness assessment
- All experiments must be tracked in MLflow/W&B -- no unlogged training runs
- Model artifacts must be versioned in a model registry (MLflow Model Registry, etc.)
- Fairness metrics must be computed across protected groups before deployment
- A monitoring plan is required before any model goes to production
- Document retraining triggers and cadence
- Maintain a rollback plan for every deployed model
- Model performance must be compared against the current production baseline, not just other experiments
- Data drift and prediction drift must be monitored post-deployment
```

### 12. `.claude/skills/code-review/SKILL.md`

```markdown
---
name: code-review
description: Perform a standardized code review following Colruyt Group quality checklist. Use when asked to review code changes.
argument-hint: "[file or branch]"
user-invocable: true
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

# Code Review

Review the specified code changes (or current uncommitted changes if no argument given) against this checklist:

Target: $ARGUMENTS (if empty, review `git diff` output)

## Checklist

### Correctness
- [ ] Logic is correct and handles edge cases
- [ ] Error handling is appropriate and complete
- [ ] No off-by-one errors, null pointer risks, or race conditions

### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation at system boundaries
- [ ] No SQL injection, XSS, or CSRF vulnerabilities
- [ ] Sensitive data is not logged or exposed

### Quality
- [ ] Code is readable and self-documenting
- [ ] No code duplication that should be extracted
- [ ] Functions have single responsibility
- [ ] Naming is clear and consistent

### Testing
- [ ] New code has corresponding tests
- [ ] Edge cases are tested
- [ ] Tests are deterministic (no flaky tests)

### Performance
- [ ] No N+1 queries or unbounded loops
- [ ] Appropriate use of caching, indexing, pagination
- [ ] No unnecessary memory allocation

### Compliance
- [ ] GDPR requirements met for any personal data handling
- [ ] Logging follows structured format without PII

Output a structured review with findings categorized as: CRITICAL, WARNING, SUGGESTION, PRAISE.
```

### 10. `.claude/skills/adr/SKILL.md`

```markdown
---
name: adr
description: Generate an Architecture Decision Record (ADR) for documenting significant technical decisions. Use when the user wants to document an architectural choice.
argument-hint: "[decision title]"
user-invocable: true
allowed-tools: ["Read", "Write", "Glob"]
---

# Architecture Decision Record

Generate an ADR for: $ARGUMENTS

Use this template:

```markdown
# ADR-[NUMBER]: [TITLE]

**Date**: [TODAY]
**Status**: Proposed | Accepted | Deprecated | Superseded
**Deciders**: [who was involved]

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Consequences

### Positive
- [benefit 1]
- [benefit 2]

### Negative
- [trade-off 1]
- [trade-off 2]

### Risks
- [risk 1 and mitigation]

## Alternatives Considered
| Alternative | Pros | Cons | Why rejected |
|---|---|---|---|
| [option A] | ... | ... | ... |
| [option B] | ... | ... | ... |
```

Save to `docs/adr/` directory (create if it doesn't exist). Number sequentially based on existing ADRs.
```

### 11. `.claude/skills/incident-report/SKILL.md`

```markdown
---
name: incident-report
description: Generate a post-incident report following the Colruyt Group template. Use after resolving a production incident.
argument-hint: "[incident summary]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash", "WebFetch"]
---

# Post-Incident Report

Generate an incident report for: $ARGUMENTS

Use this template:

## Incident Report: [TITLE]

**Date**: [DATE]
**Severity**: P1 (Critical) | P2 (Major) | P3 (Minor) | P4 (Low)
**Duration**: [start time] - [end time] ([total duration])
**Affected systems**: [list]
**Impact**: [user-facing impact description]

### Timeline
| Time (UTC) | Event |
|---|---|
| HH:MM | [what happened] |

### Root Cause
[Technical explanation of what went wrong and why]

### Resolution
[What was done to fix it]

### Action Items
| Action | Owner | Priority | Due Date |
|---|---|---|---|
| [action] | [who] | [P1-P4] | [date] |

### Lessons Learned
- What went well:
- What went poorly:
- Where we got lucky:

### Detection
- How was the incident detected?
- How could we detect it faster next time?
```

### 12. `.claude/skills/mr-description/SKILL.md`

```markdown
---
name: mr-description
description: Generate a standardized GitLab merge request description from the current branch diff. Use when preparing to create a merge request.
argument-hint: "[target branch, default: main]"
user-invocable: true
allowed-tools: ["Bash", "Read", "Grep"]
---

# GitLab Merge Request Description Generator

Generate a merge request description for the current branch.

1. Run `git log main..HEAD --oneline` to see commits (use $ARGUMENTS as target branch if provided, otherwise `main`)
2. Run `git diff main..HEAD --stat` for changed files summary
3. Run `git diff main..HEAD` for full diff
4. Analyze the changes and generate:

## MR Description

**Title**: [imperative mood, under 72 chars, include JIRA ticket if in branch name]

**Description**:

### Summary
[1-3 sentences explaining the what and why]

### Changes
- [Bulleted list of logical changes, grouped by area]

### Test Plan
- [ ] [How to verify each change works correctly]

### Breaking Changes
[List any breaking changes, or "None"]

### Screenshots
[Note if UI changes need screenshots]

Output the description in a format ready to paste into GitLab.
```

### CRISP-DM PHASE 1 SKILLS: Business Understanding

### 16. `.claude/skills/init-ds-project/SKILL.md`

```markdown
---
name: init-ds-project
description: Scaffold a CRISP-DM aligned data science project structure. Use when starting a new data science project.
argument-hint: "[project name]"
user-invocable: true
allowed-tools: ["Bash", "Write", "Read"]
---

# Initialize Data Science Project

Create a CRISP-DM aligned project structure for: $ARGUMENTS

Generate the following directory tree:
```
project_name/
├── README.md
├── Makefile                  # make data, make train, make evaluate, make serve
├── pyproject.toml            # or requirements.txt with pinned versions
├── .env.example              # Required environment variables
├── data/
│   ├── raw/                  # Original immutable data
│   ├── interim/              # Intermediate transformed data
│   ├── processed/            # Final datasets for modeling
│   └── external/             # Third-party data sources
├── notebooks/
│   ├── 01-business-understanding/
│   ├── 02-data-understanding/
│   ├── 03-data-preparation/
│   ├── 04-modeling/
│   └── 05-evaluation/
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── config.py         # Paths, parameters, constants
│       ├── data/             # Data loading and processing
│       ├── features/         # Feature engineering
│       ├── models/           # Model training and prediction
│       └── visualization/    # Plotting utilities
├── models/                   # Serialized models, predictions
├── reports/
│   ├── figures/
│   └── model_cards/
├── docs/
│   ├── adr/                  # Architecture Decision Records
│   ├── data_dictionary/
│   └── project_charter.md
├── tests/
└── .dvc/                     # Data version control (if using DVC)
```

Also create a starter README.md with CRISP-DM phase tracking table and project overview sections.
```

### 17. `.claude/skills/project-charter/SKILL.md`

```markdown
---
name: project-charter
description: Generate a structured data science project charter. Use at the start of a CRISP-DM project to document business objectives, success criteria, and scope.
argument-hint: "[business problem description]"
user-invocable: true
allowed-tools: ["Read", "Write"]
---

# Project Charter Generator (CRISP-DM Phase 1)

Generate a project charter for: $ARGUMENTS

Template:
# Project Charter: [TITLE]

## Business Objective
[What business problem are we solving? Why now?]

## Stakeholders
| Name | Role | Responsibility |
|---|---|---|
| [name] | Sponsor | Final approval |
| [name] | Domain Expert | Requirements, validation |
| [name] | Data Scientist | Analysis, modeling |

## Success Criteria
| Business KPI | Target | Measurement Method |
|---|---|---|
| [e.g., reduce churn] | [e.g., by 15%] | [e.g., monthly cohort analysis] |

## Data Mining Goals
| Technical Metric | Target | Rationale |
|---|---|---|
| [e.g., AUC-ROC] | [e.g., > 0.85] | [maps to business KPI above] |

## Scope
- In scope: [what we will do]
- Out of scope: [what we will not do]
- Assumptions: [key assumptions]
- Constraints: [timeline, budget, data access, compute]

## Risk Register
| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| [risk] | High/Med/Low | High/Med/Low | [mitigation] |

## Timeline
| Phase | Duration | Start | End |
|---|---|---|---|
| Business Understanding | [weeks] | | |
| Data Understanding | [weeks] | | |
| Data Preparation | [weeks] | | |
| Modeling | [weeks] | | |
| Evaluation | [weeks] | | |
| Deployment | [weeks] | | |

Save to docs/project_charter.md.
```

### 18. `.claude/skills/success-criteria/SKILL.md`

```markdown
---
name: success-criteria
description: Map business KPIs to measurable technical metrics for a data science project. Use during CRISP-DM Business Understanding phase.
argument-hint: "[business objective]"
user-invocable: true
allowed-tools: ["Read", "Write"]
---

# Success Criteria Mapping (CRISP-DM Phase 1)

For the business objective: $ARGUMENTS

Generate a mapping table:

## Business-to-Technical Metric Mapping

For each business KPI, recommend appropriate ML metrics:

| Business KPI | ML Problem Type | Primary Metric | Secondary Metrics | Threshold | Rationale |
|---|---|---|---|---|---|
| [e.g., reduce fraud losses] | Binary classification | Precision@K | Recall, F1, AUC-PR | Precision > 0.95 at 1% review rate | False positives cost analyst time |

Common mappings to consider:
- Revenue impact → Regression (RMSE, MAE, MAPE)
- Customer churn → Classification (AUC-ROC, Precision-Recall, Lift)
- Anomaly detection → Detection (Precision@K, Recall, F1)
- Ranking/recommendation → Ranking (NDCG, MAP, MRR)
- Segmentation → Clustering (Silhouette, Davies-Bouldin, business-defined purity)

Also generate:
- Baseline performance (what would a naive model achieve?)
- Minimum viable performance (below this, don't deploy)
- Target performance (what we're aiming for)
- Stretch goal (aspirational)
```

### CRISP-DM PHASE 2 SKILLS: Data Understanding

### 19. `.claude/skills/eda-notebook/SKILL.md`

```markdown
---
name: eda-notebook
description: Generate a comprehensive EDA notebook template for a dataset. Use during CRISP-DM Data Understanding phase.
argument-hint: "[dataset path or description]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash", "Glob"]
---

# EDA Notebook Generator (CRISP-DM Phase 2)

Create a comprehensive EDA notebook for: $ARGUMENTS

The notebook should include these sections:

1. **Header cell**: Title, author, date, "CRISP-DM Phase: Data Understanding", purpose
2. **Imports**: pandas, numpy, matplotlib, seaborn, plotly (if available)
3. **Data Loading**: Read the dataset, display shape, dtypes, head()
4. **Overview**: df.info(), df.describe(), memory usage
5. **Missing Values**: Heatmap of nulls, percentage per column, MCAR/MAR/MNAR assessment
6. **Univariate Analysis**: Histograms for numerics, value counts for categoricals, box plots
7. **Bivariate Analysis**: Correlation matrix heatmap, scatter plots for top correlations, cross-tabs
8. **Target Variable Analysis** (if applicable): Distribution, class balance, relationship with features
9. **Temporal Patterns** (if date columns exist): Trends, seasonality, stationarity
10. **Outlier Detection**: IQR-based, z-score, visual inspection
11. **Data Quality Summary**: Table of issues found per column
12. **Hypotheses**: List of initial hypotheses for modeling
13. **Conclusions & Next Steps**: Summary of findings, recommended next actions

Name the notebook following convention: `{number}-du-eda-{description}-{initials}.ipynb`
```

### 20. `.claude/skills/data-dictionary/SKILL.md`

```markdown
---
name: data-dictionary
description: Generate a data dictionary from a dataset schema. Use during CRISP-DM Data Understanding to document every column.
argument-hint: "[dataset path or DataFrame variable]"
user-invocable: true
allowed-tools: ["Read", "Bash", "Write"]
---

# Data Dictionary Generator (CRISP-DM Phase 2)

Generate a data dictionary for: $ARGUMENTS

1. Load the dataset and inspect schema (columns, dtypes, sample values)
2. For each column, generate a row in this template:

| Column | Type | Description | Source | Nulls % | Unique | Example Values | Notes |
|---|---|---|---|---|---|---|---|
| [name] | [dtype] | [TO BE FILLED] | [TO BE FILLED] | [computed] | [computed] | [3 examples] | [anomalies found] |

3. Auto-fill what can be detected (type, null%, unique count, examples)
4. Mark Description and Source as "[TO BE FILLED]" for human review
5. Flag columns needing attention (>50% nulls, single value, suspicious patterns)

Save to docs/data_dictionary/[dataset_name].md
```

### 21. `.claude/skills/data-quality/SKILL.md`

```markdown
---
name: data-quality
description: Generate a data quality assessment report for a dataset. Use during CRISP-DM Data Understanding phase.
argument-hint: "[dataset path]"
user-invocable: true
allowed-tools: ["Read", "Bash", "Write"]
---

# Data Quality Assessment (CRISP-DM Phase 2)

Assess data quality for: $ARGUMENTS

Generate Python code that evaluates these quality dimensions:

1. **Completeness**: Null/missing values per column, overall completeness score
2. **Uniqueness**: Duplicate rows, near-duplicates, primary key violations
3. **Validity**: Values outside expected ranges, invalid formats, type mismatches
4. **Consistency**: Cross-field validation (e.g., end_date > start_date), referential integrity
5. **Timeliness**: Data freshness, gaps in time series, expected vs actual row counts
6. **Accuracy**: Statistical outliers (IQR, z-score), impossible values

Output a structured report:
## Data Quality Report: [DATASET]
- **Overall Score**: [0-100]
- **Dimensions**: [table of scores per dimension]
- **Critical Issues**: [blocking issues that must be resolved]
- **Warnings**: [issues that should be investigated]
- **Recommendations**: [suggested data cleaning steps for Phase 3]
```

### CRISP-DM PHASE 3 SKILLS: Data Preparation

### 22. `.claude/skills/feature-doc/SKILL.md`

```markdown
---
name: feature-doc
description: Document a new feature in the feature registry. Use during CRISP-DM Data Preparation to track all engineered features.
argument-hint: "[feature name] [formula/description]"
user-invocable: true
allowed-tools: ["Read", "Write", "Edit"]
---

# Feature Documentation (CRISP-DM Phase 3)

Document the feature: $ARGUMENTS

Append to docs/feature_registry.md (create if it doesn't exist):

| Feature | Formula/Definition | Source Columns | Rationale | Author | Date | Status |
|---|---|---|---|---|---|---|
| [name] | [how it's computed] | [which raw columns] | [why this feature helps] | [who created it] | [date] | Active/Deprecated |

If this is the first feature, create the file with a header explaining the feature registry purpose.
```

### 23. `.claude/skills/leakage-check/SKILL.md`

```markdown
---
name: leakage-check
description: Audit a data pipeline or notebook for data leakage. Use during CRISP-DM Data Preparation to verify pipeline integrity.
argument-hint: "[file or directory to audit]"
user-invocable: true
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

# Data Leakage Audit (CRISP-DM Phase 3)

Audit for data leakage in: $ARGUMENTS

Check for these common leakage patterns:

1. **Target Leakage**: Features derived from the target variable or that wouldn't be available at prediction time
2. **Temporal Leakage**: Using future data to predict the past (look-ahead bias)
3. **Preprocessing Leakage**: fit_transform() on full dataset before train/test split (must fit on train only)
4. **Group Leakage**: Same entity (customer, session) appearing in both train and test
5. **Feature Leakage**: Features that are proxies for the target (e.g., "is_churned" to predict churn)

Scan code for:
- `fit_transform` called before `train_test_split`
- Scaling/encoding applied to full dataset
- `train_test_split` without `shuffle=False` on time series data
- Missing `group` parameter in GroupKFold scenarios
- Features computed from columns that include the target

Output: PASS/FAIL with specific line references for each finding.
```

### 24. `.claude/skills/data-validation/SKILL.md`

```markdown
---
name: data-validation
description: Generate a data validation suite using pandera or Great Expectations. Use during CRISP-DM Data Preparation.
argument-hint: "[dataset path]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Data Validation Suite Generator (CRISP-DM Phase 3)

Generate validation code for: $ARGUMENTS

1. Inspect the dataset schema and statistics
2. Generate a pandera DataFrameSchema (preferred) or Great Expectations suite that validates:
   - Column presence and types
   - Null constraints (based on observed patterns)
   - Value ranges (min/max for numerics)
   - Allowed values (for low-cardinality categoricals)
   - String patterns (for emails, IDs, dates)
   - Row-level checks (cross-column constraints)
   - Statistical checks (mean within range, std dev bounds)
3. Include both "hard" checks (must pass) and "soft" checks (warnings)
4. Generate a test file that runs the validation on sample data
```

### CRISP-DM PHASE 4 SKILLS: Modeling

### 25. `.claude/skills/baseline-model/SKILL.md`

```markdown
---
name: baseline-model
description: Generate a baseline model for a given problem type. Use at the start of CRISP-DM Modeling phase -- always establish a baseline before complex models.
argument-hint: "[classification|regression|clustering|timeseries] [target column]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Baseline Model Generator (CRISP-DM Phase 4)

Generate a baseline model for: $ARGUMENTS

Based on problem type, create:

**Classification**: DummyClassifier (most_frequent, stratified), LogisticRegression with default params
**Regression**: DummyRegressor (mean, median), LinearRegression with default params
**Clustering**: KMeans with k=2,3,5, simple summary statistics
**Time Series**: Naive (last value), Seasonal naive, Simple moving average

The baseline script must:
1. Load the processed dataset
2. Split train/test (stratified for classification, temporal for time series)
3. Train the simplest possible model
4. Log metrics to MLflow/console
5. Save baseline metrics to reports/baseline_metrics.json
6. Print: "Any model that doesn't beat these numbers is not worth deploying"

This becomes the benchmark all future models must exceed.
```

### 26. `.claude/skills/experiment-setup/SKILL.md`

```markdown
---
name: experiment-setup
description: Configure MLflow or Weights & Biases experiment tracking for a project. Use at the start of CRISP-DM Modeling phase.
argument-hint: "[mlflow|wandb]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Experiment Tracking Setup (CRISP-DM Phase 4)

Set up experiment tracking using: $ARGUMENTS (default: mlflow)

Generate:
1. Configuration file (mlflow_config.py or wandb_config.py) with:
   - Project name, experiment name
   - Tracking URI (local or remote)
   - Artifact storage location
2. Training wrapper function that auto-logs:
   - All hyperparameters
   - All metrics (train + validation)
   - Dataset version/hash
   - Code version (git commit SHA)
   - Random seeds
   - Environment info (Python version, key package versions)
   - Model artifacts
   - Feature importance plots
3. requirements.txt additions
4. Example usage in a training script
```

### 27. `.claude/skills/error-analysis/SKILL.md`

```markdown
---
name: error-analysis
description: Generate an error analysis notebook for a trained model. Use during CRISP-DM Modeling to understand where and why the model fails.
argument-hint: "[model path or description]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Error Analysis (CRISP-DM Phase 4)

Generate an error analysis notebook for: $ARGUMENTS

Include sections for:
1. **Overall Performance**: Confusion matrix / residual distribution
2. **Worst Predictions**: Top 20 largest errors with full feature values
3. **Error by Subgroup**: Performance broken down by key categorical features
4. **Error by Feature Range**: Performance across quantiles of numeric features
5. **Temporal Analysis**: Is performance stable over time or degrading?
6. **Confidence Analysis**: Calibration curve, prediction probability distribution
7. **Cluster Analysis**: Cluster the errors -- are there systematic patterns?
8. **Feature Importance for Errors**: What features correlate with large errors?
9. **Recommendations**: Suggested improvements (more data, new features, different model, etc.)
```

### CRISP-DM PHASE 5 SKILLS: Evaluation

### 28. `.claude/skills/model-card/SKILL.md`

```markdown
---
name: model-card
description: Generate a model card following Google's Model Cards framework. Required before any model goes to production. Use during CRISP-DM Evaluation phase.
argument-hint: "[model name or experiment ID]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash", "Glob"]
---

# Model Card Generator (CRISP-DM Phase 5)

Generate a model card for: $ARGUMENTS

Template (based on Google Model Cards for Model Reporting):

# Model Card: [MODEL NAME]

## Model Details
- **Model type**: [algorithm/architecture]
- **Version**: [version number]
- **Date**: [training date]
- **Owner**: [team/person]
- **Contact**: [email]
- **License**: [internal/open-source]

## Intended Use
- **Primary use cases**: [what this model is for]
- **Out-of-scope uses**: [what this model should NOT be used for]
- **Users**: [who will use this model]

## Training Data
- **Source**: [where the data came from]
- **Date range**: [temporal coverage]
- **Size**: [rows, features]
- **Preprocessing**: [key transformations applied]

## Evaluation Data
- **Source**: [same or different from training]
- **Date range**: [temporal coverage]
- **Size**: [rows]

## Performance Metrics
| Metric | Overall | [Subgroup A] | [Subgroup B] | [Subgroup C] |
|---|---|---|---|---|
| [metric 1] | [value] | [value] | [value] | [value] |

## Ethical Considerations
- **Sensitive attributes**: [what protected characteristics are involved]
- **Fairness assessment**: [disparate impact, equalized odds results]
- **Potential harms**: [what could go wrong]
- **Mitigations**: [what was done to address concerns]

## Limitations & Caveats
- [limitation 1]
- [limitation 2]
- [known failure modes]

## Monitoring
- **Metrics tracked**: [what is monitored in production]
- **Drift detection**: [method and thresholds]
- **Retraining trigger**: [when to retrain]
- **Rollback plan**: [how to revert]

Save to reports/model_cards/[model_name].md
```

### 29. `.claude/skills/fairness-audit/SKILL.md`

```markdown
---
name: fairness-audit
description: Generate a fairness/bias audit for a model across protected attributes. Use during CRISP-DM Evaluation before deployment decisions.
argument-hint: "[model] [protected attributes]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
model: opus
---

# Fairness Audit (CRISP-DM Phase 5)

Audit model fairness for: $ARGUMENTS

Generate Python code that:
1. Load model predictions and test data with protected attributes
2. Compute metrics per subgroup:
   - Demographic Parity (prediction rates across groups)
   - Equalized Odds (TPR and FPR across groups)
   - Calibration (predicted probability accuracy across groups)
   - Disparate Impact Ratio (should be > 0.8 per four-fifths rule)
3. Visualize: bar charts of metrics across groups, ROC curves per group
4. Flag violations with severity ratings
5. Suggest mitigations (threshold adjustment, resampling, fairness constraints)
6. Generate a summary suitable for the model card

Use Fairlearn if available, otherwise implement metrics directly with sklearn.
```

### 30. `.claude/skills/model-comparison/SKILL.md`

```markdown
---
name: model-comparison
description: Compare multiple experiments from experiment tracking. Use during CRISP-DM Evaluation to select the best model.
argument-hint: "[experiment names or IDs]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Model Comparison (CRISP-DM Phase 5)

Compare experiments: $ARGUMENTS

Generate a comparison report including:
1. **Leaderboard table**: All models ranked by primary metric
2. **Multi-metric comparison**: Radar chart of key metrics per model
3. **Complexity vs Performance**: Plot of model complexity (params, inference time) vs accuracy
4. **Statistical significance**: Paired t-test or Wilcoxon test between top models
5. **Resource comparison**: Training time, memory usage, inference latency
6. **Recommendation**: Which model to deploy and why (considering performance, complexity, interpretability, and business requirements)

If MLflow is configured, query the tracking server. Otherwise, read from reports/ directory.
```

### CRISP-DM PHASE 6 SKILLS: Deployment

### 31. `.claude/skills/serving-api/SKILL.md`

```markdown
---
name: serving-api
description: Generate a FastAPI model serving endpoint with input validation. Use during CRISP-DM Deployment phase.
argument-hint: "[model path]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Model Serving API Generator (CRISP-DM Phase 6)

Generate a serving API for: $ARGUMENTS

Create:
1. `src/serving/app.py` -- FastAPI app with:
   - `/predict` endpoint with Pydantic input validation
   - `/health` health check endpoint
   - `/model-info` endpoint returning model card metadata
   - Input validation matching the training feature schema
   - Preprocessing pipeline (same as training)
   - Structured logging with correlation IDs
   - Error handling for malformed inputs
2. `src/serving/schemas.py` -- Pydantic models for request/response
3. `Dockerfile` -- Container for the serving app
4. `tests/test_serving.py` -- Tests for the API
5. Update requirements.txt with serving dependencies (fastapi, uvicorn, pydantic)
```

### 32. `.claude/skills/monitoring-config/SKILL.md`

```markdown
---
name: monitoring-config
description: Generate monitoring configuration for a deployed model. Use during CRISP-DM Deployment to set up drift detection and alerting.
argument-hint: "[model name]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Monitoring Configuration (CRISP-DM Phase 6)

Set up monitoring for: $ARGUMENTS

Generate:
1. **Data drift detection** config (using Evidently AI or custom):
   - Reference dataset (training distribution)
   - Monitored features and drift methods (PSI, KS-test, Wasserstein)
   - Alert thresholds per feature
2. **Prediction drift** monitoring:
   - Prediction distribution tracking
   - Confidence score distribution
3. **Performance monitoring** (when labels become available):
   - Metrics tracked over time windows
   - Performance degradation thresholds
4. **Alerting rules**:
   - Who gets alerted (Slack channel, email)
   - Severity levels and escalation
5. **Retraining triggers**:
   - Automatic retraining conditions
   - Manual review triggers
6. **Dashboard config**: Metrics to display, refresh cadence
```

### 33. `.claude/skills/runbook/SKILL.md`

```markdown
---
name: runbook
description: Generate an operations runbook for a deployed model. Use during CRISP-DM Deployment phase.
argument-hint: "[model/service name]"
user-invocable: true
allowed-tools: ["Read", "Write", "Bash"]
---

# Operations Runbook (CRISP-DM Phase 6)

Generate a runbook for: $ARGUMENTS

# Runbook: [SERVICE NAME]

## Service Overview
- What: [what this model/service does]
- Owner: [team]
- On-call: [rotation]
- Architecture: [how it's deployed]

## Health Checks
- [ ] Endpoint: [health check URL]
- [ ] Expected response: [what "healthy" looks like]
- [ ] Dashboard: [monitoring URL]

## Common Issues & Resolutions
| Symptom | Likely Cause | Resolution |
|---|---|---|
| High latency | Model loading | Restart pod / check memory |
| Prediction drift alert | Data distribution change | Check upstream data, consider retraining |
| 5xx errors | Input schema mismatch | Check input validation logs |

## Retraining Procedure
1. [step-by-step retraining]

## Rollback Procedure
1. [step-by-step rollback]

## Escalation
| Severity | Response Time | Escalation |
|---|---|---|
| P1 | 15 min | [who] |
| P2 | 1 hour | [who] |
| P3 | Next business day | [who] |
```

### AGENTS (expanded with data science agents)

### 34. `.claude/agents/security-reviewer.md`

```markdown
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities. Use proactively when reviewing code that handles authentication, authorization, user input, or sensitive data.
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
model: opus
maxTurns: 10
---

You are a security reviewer at Colruyt Group. Your job is to find security vulnerabilities in code changes.

Review process:
1. Identify all changed files via `git diff --name-only` or the specified scope
2. For each file, check for:
   - OWASP Top 10 vulnerabilities
   - Hardcoded secrets, credentials, or API keys
   - SQL injection (string concatenation in queries)
   - XSS (unescaped user input in output)
   - CSRF (missing token validation)
   - Insecure deserialization
   - Missing input validation at system boundaries
   - PII exposure in logs, errors, or responses
   - Insecure cryptographic practices
   - Missing authentication/authorization checks
   - Path traversal vulnerabilities
   - Server-Side Request Forgery (SSRF)

3. Output a structured report:

### Security Review Report

**Scope**: [files reviewed]
**Risk Level**: CRITICAL | HIGH | MEDIUM | LOW | CLEAN

#### Findings
For each finding:
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **File**: [path:line]
- **Issue**: [description]
- **Impact**: [what could go wrong]
- **Recommendation**: [how to fix]

#### Summary
- Total findings: [count by severity]
- Recommendation: APPROVE / APPROVE WITH CHANGES / BLOCK
```

### 35. `.claude/agents/documentation-writer.md`

(Same content as before -- generates/updates documentation from code changes)

### 36. `.claude/agents/eda-assistant.md` (NEW)

```markdown
---
name: eda-assistant
description: Assists with exploratory data analysis. Use during CRISP-DM Data Understanding when exploring datasets, generating visualizations, or profiling data quality.
tools: Read, Write, Bash, Glob, Grep
model: opus
maxTurns: 20
---

You are a data analysis assistant at Colruyt Group specializing in EDA.

When invoked:
1. Load the specified dataset (CSV, Parquet, or database query)
2. Generate descriptive statistics and data quality metrics
3. Create visualizations for distributions, correlations, and patterns
4. Flag data quality issues (nulls, outliers, duplicates, mixed types)
5. Suggest hypotheses for modeling based on observed patterns

Always:
- Use pandas for data manipulation, seaborn/matplotlib for visualization
- Save figures to reports/figures/ with descriptive names
- Print summary statistics, don't just show raw output
- Suggest which columns need cleaning in Phase 3
- Follow notebook standards (structured markdown cells between code)
```

### 37. `.claude/agents/data-quality-checker.md` (NEW)

```markdown
---
name: data-quality-checker
description: Profiles data quality and detects issues. Use proactively when loading new datasets or before modeling to verify data integrity.
tools: Read, Bash, Glob, Grep
disallowedTools: Write, Edit
model: opus
maxTurns: 15
---

You are a data quality specialist at Colruyt Group. Your job is to find data quality issues before they become model problems.

Check for:
1. **Schema issues**: unexpected types, new/missing columns vs. schema
2. **Completeness**: null patterns, suspicious zero-fill, default values masking missing data
3. **Uniqueness**: duplicate rows, near-duplicates, primary key violations
4. **Validity**: values outside expected ranges, invalid formats, impossible combinations
5. **Consistency**: cross-field contradictions, referential integrity breaks
6. **Distribution shifts**: compare current data vs. historical baselines
7. **PII detection**: scan for email patterns, phone numbers, national registry numbers

Output a structured quality report with severity ratings (CRITICAL, WARNING, INFO).
```

### 38. `.claude/agents/ml-reviewer.md` (NEW)

```markdown
---
name: ml-reviewer
description: Reviews ML code for best practices, data leakage, reproducibility, and common pitfalls. Use proactively when reviewing data science code, notebooks, or pipelines.
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
model: opus
maxTurns: 15
---

You are a senior ML engineer reviewing data science code at Colruyt Group.

Review checklist:
1. **Data Leakage**: fit_transform before split, future data used, target-derived features
2. **Reproducibility**: random seeds set, dependencies pinned, data versioned
3. **Pipeline Correctness**: preprocessing fit on train only, same pipeline for train/serve
4. **Experiment Tracking**: all runs logged with params, metrics, artifacts
5. **Statistical Rigor**: appropriate cross-validation strategy, significance testing
6. **Feature Engineering**: documented, no look-ahead bias, consistent train/serve
7. **Model Selection**: baseline established, multiple approaches compared, not over-tuned
8. **Code Quality**: modular, testable, no notebook-only code for production logic
9. **CRISP-DM Alignment**: work matches the declared phase, artifacts are produced

For each finding: severity (CRITICAL/HIGH/MEDIUM/LOW), file:line, issue, recommendation.
```

### 39. `.claude/agents/notebook-reviewer.md` (NEW)

```markdown
---
name: notebook-reviewer
description: Reviews Jupyter notebooks for quality, documentation, and best practices. Use when reviewing notebooks before committing.
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: opus
maxTurns: 10
---

You are a notebook quality reviewer at Colruyt Group.

Check that the notebook follows standards:
1. **Header**: Has title, author, date, CRISP-DM phase, purpose in first cell
2. **Naming**: Follows {number}-{phase}-{description}-{initials}.ipynb convention
3. **Structure**: Logical section headers, markdown explanations between code cells
4. **Conclusions**: Ends with findings summary and next steps
5. **Imports**: All imports in first code cell
6. **No hardcoded paths**: Uses config or environment variables
7. **No magic numbers**: Named constants or documented values
8. **Clean execution**: No out-of-order cell execution indicators
9. **Visualization quality**: Labeled axes, titles, legends, colorblind-friendly
10. **Data not committed**: No large DataFrames printed (>20 rows), data files not in git
```

### 40. `.claude/agents/experiment-tracker.md` (NEW)

```markdown
---
name: experiment-tracker
description: Summarizes and compares experiment results from MLflow or Weights & Biases. Use during CRISP-DM Modeling and Evaluation.
tools: Read, Bash, Glob, Grep
disallowedTools: Write, Edit
model: opus
maxTurns: 10
---

You are an experiment analysis assistant at Colruyt Group.

When invoked:
1. Query the experiment tracking system (MLflow/W&B) for recent runs
2. Generate a summary table of all experiments with key metrics
3. Identify the best performing model(s)
4. Compare against the baseline (from reports/baseline_metrics.json)
5. Highlight significant improvements or regressions
6. Flag experiments that may have issues (suspiciously high metrics = possible leakage)
7. Recommend which model to advance to evaluation

Output: A concise leaderboard with commentary on each model's strengths and weaknesses.
```

### LEGACY COMMANDS

### 41. `.claude/commands/summarize.md` (legacy command example)

Simple slash commands -- each `.md` file becomes a `/command`. No frontmatter needed (unlike skills). The filename is the command name.

```markdown
Summarize the following code or text. If no argument is provided, summarize the current file.

Focus on:
- What the code/text does (purpose)
- Key components and their relationships
- Notable patterns or decisions

Input: $ARGUMENTS
```

Note: `commands/` is the legacy approach. `skills/` is preferred for new commands because it supports frontmatter (model, tools, argument hints). Both work simultaneously.

### 42. `.claude/commands/explain-model.md` (NEW legacy command)

```markdown
Generate a SHAP-based model interpretability analysis for the specified model.

1. Load the model and test dataset
2. Compute SHAP values (TreeExplainer for tree models, KernelExplainer for others)
3. Generate: summary plot, dependence plots for top 5 features, force plot for sample predictions
4. Save visualizations to reports/figures/
5. Print top 10 most important features with their SHAP impact

Model: $ARGUMENTS
```

### 43. `.claude/commands/crisp-status.md` (NEW legacy command)

```markdown
Review the current project and determine CRISP-DM phase progress.

Check for artifacts that indicate phase completion:
- Phase 1 (Business Understanding): docs/project_charter.md, success criteria defined
- Phase 2 (Data Understanding): EDA notebooks in notebooks/02-*, data dictionary, data quality report
- Phase 3 (Data Preparation): Processed datasets in data/processed/, feature registry, validation suite
- Phase 4 (Modeling): Baseline model, experiment tracking logs, trained models in models/
- Phase 5 (Evaluation): Model card, fairness audit, evaluation report
- Phase 6 (Deployment): Serving API, monitoring config, runbook

Output a status table showing each phase's completion status and missing artifacts.
```

### PLUGINS

### 44. `.claude/plugins/colruyt-ds/plugin.json`

```json
{
  "name": "colruyt-ds",
  "version": "1.0.0",
  "description": "Colruyt Group data science standards, CRISP-DM workflows, and ML governance tools",
  "author": "Colruyt Group Data & Analytics",
  "repository": "https://gitlab.colruytgroup.com/data-analytics/claude-ds-plugin"
}
```

This plugin scaffolds the data science toolchain. Teams extend it by adding domain-specific skills inside the plugin structure. The plugin can also be published to a marketplace for org-wide distribution.

### THIRD-PARTY PLUGINS & MCP SERVERS

### 45. Recommended third-party plugins (configured in `settings.json`)

The `compound-engineering` plugin provides pre-built data skills. Configure in settings.json:

```json
{
  "enabledPlugins": {
    "compound-engineering@every-marketplace": true,
    "data@knowledge-work-plugins": true
  }
}
```

This gives access to these ready-made skills (invoked as `/data:<skill-name>`):

| Skill | What it does |
|---|---|
| `/data:analyze` | End-to-end data analysis -- from quick lookups to full stakeholder reports |
| `/data:explore-data` | Profile and explore datasets (null rates, distributions, quality issues) |
| `/data:write-query` | Write optimized SQL for Snowflake, BigQuery, Postgres, Databricks |
| `/data:sql-queries` | Multi-dialect SQL with CTEs, window functions, optimization |
| `/data:data-visualization` | Create charts with matplotlib, seaborn, plotly |
| `/data:create-viz` | Publication-quality visualizations from DataFrames |
| `/data:build-dashboard` | Interactive HTML dashboards with KPI cards, filters, charts |
| `/data:statistical-analysis` | Descriptive stats, trend analysis, hypothesis testing, outlier detection |
| `/data:validate-data` | QA an analysis before sharing (methodology, accuracy, bias checks) |
| `/data:data-context-extractor` | Bootstrap company-specific data analysis skill from your warehouse |

### 46. `.mcp.json` (project root) -- expanded for data science

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gitlab"],
      "env": {
        "GITLAB_API_URL": "https://gitlab.colruytgroup.com/api/v4",
        "GITLAB_TOKEN": "${GITLAB_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./data", "./reports", "./models"],
      "_comment": "Official MCP reference server -- secure file access for data directories"
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"],
      "_comment": "Official MCP reference server (archived) -- read-only database access with schema inspection"
    },
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "${SQLITE_DB_PATH:-./data/local.db}"],
      "_comment": "Official MCP reference server (archived) -- local database for analysis"
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "_comment": "Official MCP reference server -- persistent knowledge graph for project context"
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "_comment": "Official MCP reference server -- fetch web content (APIs, documentation)"
    }
  }
}
```

**Additional MCP servers to add based on your data stack** (documented in `docs/MCP-SERVERS-CATALOG.md`):

| Server | Package | Type | Use Case |
|---|---|---|---|
| **DuckDB** | `mcp-server-duckdb` (PyPI) | Community (173 stars) | Analytical queries on local files (Parquet, CSV) |
| **MySQL** | `mcp-server-mysql` (npm) | Community (1,377 stars) | MySQL database access |
| **Snowflake** | `Snowflake-Labs/mcp` | Official (Snowflake) | Cortex AI, SQL orchestration |
| **BigQuery** | `LucasHild/mcp-server-bigquery` | Community | Google BigQuery access |
| **AWS suite** | `awslabs/mcp` (8,494 stars) | Official (AWS) | S3, Redshift, SageMaker, data processing (65+ servers) |
| **Databricks** | `markov-kernel/databricks-mcp` | Community | Databricks data access |
| **W&B** | `wandb/wandb-mcp-server` | Official (W&B) | Experiment tracking data |
| **ClickHouse** | `ClickHouse/mcp-clickhouse` | Official (ClickHouse, 725 stars) | OLAP analytics |
| **Jupyter** | `ihrpr/mcp-server-jupyter` | Community | Notebook interaction |
| **DataHub** | `acryldata/mcp-server-datahub` | Official (DataHub) | Data catalog, lineage |
| **Chroma** | `chroma-core/chroma-mcp` | Official (Chroma) | Vector search, embeddings |
| **Sequential Thinking** | Official (in MCP repo) | Official (MCP) | Complex reasoning, problem decomposition |

### 47. `.gitignore.claude`

Lines to append to project `.gitignore`:
```
# Claude Code
.claude/settings.local.json
.claude/agent-memory-local/
```

---

## Exhaustive Configuration Options Reference

All options covered in this template, plus those documented in `docs/CONFIGURATION-REFERENCE.md`:

| Category | Where | Covered in Template | Documented in Reference |
|---|---|---|---|
| **Model selection** (`model`, `availableModels`) | settings.json | Yes | Yes |
| **Effort level** (`effortLevel`) | settings.json | Yes | Yes |
| **Permissions** (allow/deny/ask arrays) | settings.json | Yes | Yes |
| **Permission mode** (`defaultMode`) | settings.json | Yes | Yes |
| **Environment variables** (`env`) | settings.json | Yes | Yes |
| **API proxy** (`ANTHROPIC_BASE_URL`) | settings.json env | Yes | Yes |
| **Corporate proxy** (`HTTP_PROXY`/`HTTPS_PROXY`) | settings.json env | Documented | Yes |
| **mTLS certs** (`CLAUDE_CODE_CLIENT_CERT/KEY`) | settings.json env | Documented | Yes |
| **Telemetry** (`DISABLE_TELEMETRY`) | settings.json env | Yes | Yes |
| **Hooks** (20+ event types) | settings.json | Yes (PreToolUse) | Yes (all events) |
| **MCP servers** | .mcp.json | Yes (GitLab) | Yes |
| **Custom skills** | .claude/skills/*/SKILL.md | Yes (22 skills: 4 general + 18 CRISP-DM) | Yes |
| **Custom agents** | .claude/agents/*.md | Yes (7 agents: 2 general + 5 data science) | Yes |
| **Legacy commands** | .claude/commands/*.md | Yes (3 commands) | Yes |
| **Plugins (local)** | .claude/plugins/*/plugin.json | Yes (colruyt-ds scaffold) | Yes |
| **Plugins (marketplace)** | settings.json `enabledPlugins` | Yes (compound-engineering, data) | Yes |
| **Rules** (glob-scoped) | .claude/rules/*.md | Yes (7 rules: 4 general + 3 data science) | Yes |
| **CLAUDE.md** (root + .claude/) | CLAUDE.md | Yes (both levels) | Yes |
| **Auto memory** (`autoMemoryEnabled`) | settings.json | Yes | Yes |
| **Shell config** (`CLAUDE_CODE_SHELL`) | settings.json env | Documented | Yes |
| **Bash timeout** (`BASH_DEFAULT_TIMEOUT_MS`) | settings.json env | Yes | Yes |
| **Max thinking tokens** (`MAX_THINKING_TOKENS`) | settings.local.json.example | Yes | Yes |
| **Max output tokens** (`CLAUDE_CODE_MAX_OUTPUT_TOKENS`) | settings.json env | Documented | Yes |
| **Keybindings** (~/.claude/keybindings.json) | N/A (personal) | No | Yes |
| **Theme** (settings.json `theme`) | N/A (personal) | No | Yes |
| **Vim mode** (settings.json `vim`) | N/A (personal) | No | Yes |
| **Sandbox network** (`sandbox.network`) | settings.json | Documented | Yes |
| **Sandbox filesystem** (`sandbox.filesystem`) | settings.json | Documented | Yes |
| **Auto-updater** (`DISABLE_AUTOUPDATER`) | settings.json env | Documented | Yes |
| **Prompt caching** (`DISABLE_PROMPT_CACHING`) | settings.json env | Documented | Yes |
| **Context window** (`CLAUDE_CODE_AUTO_COMPACT_WINDOW`) | settings.json env | Documented | Yes |
| **Subagent model** (`CLAUDE_CODE_SUBAGENT_MODEL`) | settings.json env | Documented | Yes |
| **CLAUDE.md imports** (`@path` syntax) | CLAUDE.md | Yes | Yes |
| **Plugin marketplace** (`extraKnownMarketplaces`) | settings.json | Documented | Yes |
| **Managed settings** (MDM) | /Library/Application Support/ClaudeCode/ | Documented | Yes |
| **SSO enforcement** (`forceLoginMethod`) | managed settings | Documented | Yes |
| **Bypass disable** (`disableBypassPermissionsMode`) | managed settings | Documented | Yes |
| **settings.local.json** (personal overrides) | .claude/ | Example file | Yes |

"Documented" = not set in the template but explained in `docs/CONFIGURATION-REFERENCE.md` so teams/users know how to use it.

---

## Distribution Strategy

### New users installing Claude Code
1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Clone template: `git clone https://github.com/thbraet/claude-template.git`
3. For each project, copy the `.claude/`, `CLAUDE.md`, and `.mcp.json` into the project root

### Greenfield project
```bash
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template
cp -r /tmp/claude-template/.claude ./
cp /tmp/claude-template/CLAUDE.md ./
cp /tmp/claude-template/.mcp.json ./
cat /tmp/claude-template/.gitignore.claude >> .gitignore
rm -rf /tmp/claude-template
# Edit CLAUDE.md and .claude/CLAUDE.md placeholders for your project
```

### Brownfield project
```bash
git clone --depth 1 https://github.com/thbraet/claude-template.git /tmp/claude-template
cd /path/to/my-project

# Safe to copy directly -- these won't conflict with existing files
cp -r /tmp/claude-template/.claude/rules/ .claude/rules/
cp -r /tmp/claude-template/.claude/skills/ .claude/skills/
cp -r /tmp/claude-template/.claude/agents/ .claude/agents/
cp -r /tmp/claude-template/.claude/commands/ .claude/commands/
cp -r /tmp/claude-template/.claude/plugins/ .claude/plugins/

# These may need manual merging if they already exist (cp -n = no-clobber)
cp -n /tmp/claude-template/.claude/settings.json .claude/settings.json
cp -n /tmp/claude-template/.claude/settings.local.json.example .claude/settings.local.json.example
cp -n /tmp/claude-template/.claude/CLAUDE.md .claude/CLAUDE.md
cp -n /tmp/claude-template/CLAUDE.md ./CLAUDE.md
cp -n /tmp/claude-template/.mcp.json ./.mcp.json

# Append Claude-specific gitignore entries (idempotent)
grep -qxF '.claude/settings.local.json' .gitignore 2>/dev/null || cat /tmp/claude-template/.gitignore.claude >> .gitignore

rm -rf /tmp/claude-template
```

### Team customization
Teams fork the template repo on GitHub and customize:
- Add team-specific rules to `.claude/rules/`
- Add team-specific skills to `.claude/skills/`
- Add team-specific agents to `.claude/agents/`
- Adjust `settings.json` permissions for their toolchain
- Extend `CLAUDE.md` with team conventions
- Add team-specific MCP servers to `.mcp.json`

---

## Implementation Sequence

1. Create directory structure and `.gitignore`
2. Write root `CLAUDE.md` with org + CRISP-DM instructions
3. Write `.claude/settings.json` with permissions, model, hooks, env, plugins
4. Write `.claude/settings.local.json.example`
5. Write `.claude/CLAUDE.md` project template with CRISP-DM placeholders
6. Write `.claude/rules/` -- general (4): security, coding-standards, git-workflow, compliance
7. Write `.claude/rules/` -- data science (3): data-science, notebook-standards, model-governance
8. Write `.claude/skills/` -- general (4): code-review, adr, incident-report, mr-description
9. Write `.claude/skills/` -- Phase 1 (3): init-ds-project, project-charter, success-criteria
10. Write `.claude/skills/` -- Phase 2 (3): eda-notebook, data-dictionary, data-quality
11. Write `.claude/skills/` -- Phase 3 (3): feature-doc, leakage-check, data-validation
12. Write `.claude/skills/` -- Phase 4 (3): baseline-model, experiment-setup, error-analysis
13. Write `.claude/skills/` -- Phase 5 (3): model-card, fairness-audit, model-comparison
14. Write `.claude/skills/` -- Phase 6 (3): serving-api, monitoring-config, runbook
15. Write `.claude/agents/` -- general (2): security-reviewer, documentation-writer
16. Write `.claude/agents/` -- data science (5): eda-assistant, data-quality-checker, ml-reviewer, notebook-reviewer, experiment-tracker
17. Write `.claude/commands/` (3): summarize, explain-model, crisp-status
18. Write `.claude/plugins/colruyt-ds/plugin.json` and README.md
19. Write `.mcp.json` with GitLab + data science MCP servers
20. Write `.gitignore.claude`
21. Write `docs/CONFIGURATION-REFERENCE.md` (exhaustive config reference)
22. Write `docs/TEAM-CUSTOMIZATION.md` (how to fork and extend)
23. Write `docs/CRISP-DM-WORKFLOW.md` (how template maps to CRISP-DM phases)
24. Write `docs/MCP-SERVERS-CATALOG.md` (available MCP servers for data science)
25. Write `README.md` (quick-start for all 3 scenarios)

## Verification

- Validate all JSON files with `jq .`
- Copy the template into a test directory, open Claude Code, verify settings load
- Run `/code-review` to verify general skill loads
- Run `/init-ds-project test-project` to verify CRISP-DM skill loads
- Run `/crisp-status` to verify legacy command loads
- Run `/data:explore-data` to verify compound-engineering plugin is active
- Check that rules appear by asking "what rules do you follow?"
- Verify `.mcp.json` is recognized (GitLab MCP server connects with valid token)
- Verify data science agents load by asking Claude to "run the ml-reviewer on the current code"

## Summary of All Components

| Type | Count | Details |
|---|---|---|
| **Rules** | 7 | 4 general + 3 data science (glob-scoped to .py/.ipynb/.sql) |
| **Skills** | 22 | 4 general + 3 per CRISP-DM phase (6 phases) |
| **Agents** | 7 | 2 general + 5 data science |
| **Legacy Commands** | 3 | summarize, explain-model, crisp-status |
| **Plugins (local)** | 1 | colruyt-ds scaffold |
| **Plugins (marketplace)** | 2 | compound-engineering, data (10+ additional skills) |
| **MCP Servers** | 6 | GitLab, filesystem, postgres, sqlite, memory, fetch |
| **Hooks** | 1 | PreToolUse sensitive file guard |
| **CLAUDE.md files** | 2 | Root (org+CRISP-DM), .claude/ (project template) |
| **Docs** | 4 | Config reference, team customization, CRISP-DM workflow, MCP catalog |
