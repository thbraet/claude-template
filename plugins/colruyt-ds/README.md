# CRISP-DM Plugin

A Claude Code plugin implementing the full **CRISP-DM** (CRoss-Industry Standard Process for Data Mining) methodology as executable commands.

## Phases & Commands

### Phase 1: Business Understanding
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/define-business-objectives` | Determine Business Objectives | 1.1 |
| `/assess-situation` | Assess Situation | 1.2 |
| `/define-dm-goals` | Determine Data Mining Goals | 1.3 |
| `/produce-project-plan` | Produce Project Plan | 1.4 |

### Phase 2: Data Understanding
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/collect-initial-data` | Collect Initial Data | 2.1 |
| `/describe-data` | Describe Data | 2.2 |
| `/explore-data` | Explore Data | 2.3 |
| `/verify-data-quality` | Verify Data Quality | 2.4 |

### Phase 3: Data Preparation
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/select-data` | Select Data | 3.1 |
| `/clean-data` | Clean Data | 3.2 |
| `/construct-data` | Construct Data | 3.3 |
| `/integrate-data` | Integrate Data | 3.4 |
| `/format-data` | Format Data | 3.5 |

### Phase 4: Modeling
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/select-model` | Select Modeling Technique | 4.1 |
| `/generate-test-design` | Generate Test Design | 4.2 |
| `/build-model` | Build Model | 4.3 |
| `/assess-model` | Assess Model | 4.4 |

### Phase 5: Evaluation
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/evaluate-results` | Evaluate Results | 5.1 |
| `/review-process` | Review Process | 5.2 |
| `/determine-next-steps` | Determine Next Steps | 5.3 |

### Phase 6: Deployment
| Command | Task | CRISP-DM Ref |
|---------|------|--------------|
| `/plan-deployment` | Plan Deployment | 6.1 |
| `/plan-monitoring` | Plan Monitoring & Maintenance | 6.2 |
| `/produce-final-report` | Produce Final Report | 6.3 |
| `/review-project` | Review Project | 6.4 |

### Code Review
| Command | Task | Description |
|---------|------|-------------|
| `/review-mr` | Code Review | Review branch diff as senior dev/data scientist before merging |

## Agents

| Agent | Scope |
|-------|-------|
| `business-understanding` | Phases 1.1–1.4 |
| `data-understanding` | Phases 2.1–2.4 |
| `data-preparation` | Phases 3.1–3.5 |
| `modeling` | Phases 4.1–4.4 |
| `evaluation` | Phases 5.1–5.3 |
| `deployment` | Phases 6.1–6.4 |
| `code-review` | MR review before merge |

## Usage

Each command guides you through the CRISP-DM task interactively, prompting for required inputs and producing standardized output artifacts stored in `docs/crisp-dm/`.
