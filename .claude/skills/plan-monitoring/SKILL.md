---
name: plan-monitoring
description: "CRISP-DM 6.2 — Plan Monitoring and Maintenance. Defines data drift detection, prediction quality monitoring, alert thresholds, retraining triggers, and maintenance procedures for deployed models. Produces a structured monitoring plan in docs/crisp-dm/6-deployment/."
argument-hint: "<optional: specific monitoring concern, drift type, or maintenance question>"
---

# /plan-monitoring — CRISP-DM 6.2: Plan Monitoring and Maintenance

> **Phase:** 6. Deployment | **Task:** 6.2 Plan Monitoring and Maintenance
>
> *"If the data mining result becomes part of the day-to-day business and its environment, monitoring and maintenance issues are important. The careful preparation of a maintenance strategy helps to avoid unnecessarily long periods of incorrect usage of data mining results."*

## Purpose

This skill produces a comprehensive monitoring and maintenance plan covering: data drift detection, prediction drift monitoring, model performance tracking, alerting thresholds, retraining triggers and cadence, and long-term maintenance procedures. It ensures the deployed model continues to deliver value and degrades gracefully when conditions change.

## Output Location

- Plan: `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`
- If it exists, present its contents and ask: *"A monitoring plan already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
  - If it exists, use it — the deployment architecture determines what can be monitored and how.
  - If it does not exist, warn: *"No deployment plan found (task 6.1). Monitoring design depends on the serving architecture."*
- Read `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
  - If it exists, use it — baseline performance metrics and known limitations define what to monitor.
- Read `docs/crisp-dm/4-modeling/4.2-test-design.md`
  - If it exists, use it — evaluation metrics and success thresholds inform alert levels.
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — data distributions and patterns provide the baseline for drift detection.
- Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
  - If it exists, use it — known data quality issues indicate what to watch for.
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — business impact determines monitoring urgency and thresholds.
- Read `.claude/rules/model-governance.md`
  - Use it — monitoring is mandatory before production deployment.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Model performance baselines** (from 4.4) — primary and secondary metrics on validation data
- **Known failure modes** (from 4.4) — underperforming segments, systematic biases
- **Success thresholds** (from 4.2) — minimum acceptable performance levels
- **Input data distributions** (from 2.3) — feature distributions, correlations, temporal patterns
- **Data quality issues** (from 2.4) — known quality problems that may recur
- **Business impact of errors** (from 1.1/4.4) — cost of over- vs. under-prediction
- **Serving architecture** (from 6.1) — batch/real-time, data flow, infrastructure

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Define Data Drift Monitoring

Discuss and document:
- **Feature drift** — which input features to monitor for distribution shifts
  - Statistical tests: PSI (Population Stability Index), KS test, chi-squared, Wasserstein distance
  - Reference windows: training data distribution vs. recent production data
  - Monitoring frequency: how often drift is calculated
- **Label drift** — monitoring the target variable distribution when actuals become available
- **Schema drift** — detecting changes in data structure, types, or missing columns
- **Upstream data quality** — monitoring data freshness, completeness, and consistency from source systems

### Step 4: Define Prediction Monitoring

Discuss and document:
- **Prediction distribution** — monitoring the distribution of model outputs over time
- **Prediction quality** — comparing predictions to actuals once ground truth is available
  - Lag time: how long until actuals are available
  - Comparison frequency: how often prediction quality is calculated
- **Confidence/uncertainty** — if the model produces uncertainty estimates, monitoring calibration
- **Business metric tracking** — monitoring the downstream business metrics that predictions influence

### Step 5: Define Alerting Strategy

Discuss and document:
- **Alert levels** — severity tiers (Info, Warning, Critical) with escalation paths
- **Thresholds** — specific numeric thresholds for each monitored metric
  - Warning: performance degradation is concerning but not yet business-critical
  - Critical: performance has degraded below the minimum acceptable threshold
- **Alert channels** — how alerts are delivered (email, Slack, PagerDuty, dashboard)
- **Alert fatigue mitigation** — how to avoid false positives and noisy alerts
- **On-call procedures** — who responds, investigation playbook, escalation path

### Step 6: Define Retraining Strategy

Discuss and document:
- **Retraining triggers** — what conditions trigger retraining:
  - Scheduled (calendar-based, e.g., monthly)
  - Performance-based (metric drops below threshold)
  - Drift-based (data drift exceeds threshold)
  - Event-based (new stores, restructuring, major promotions)
- **Retraining pipeline** — how retraining is executed (automated vs. manual, pipeline steps)
- **Validation gates** — what checks a retrained model must pass before deployment
- **Data window** — how much historical data to include in retraining
- **A/B testing** — how retrained models are compared to the current production model
- **Rollback on regression** — automatic revert if the retrained model performs worse

### Step 7: Define Maintenance Procedures

Discuss and document:
- **Scheduled maintenance** — regular tasks (dependency updates, infrastructure patches, log rotation)
- **Model versioning** — how model versions are tracked and archived
- **Data retention** — how long predictions, actuals, and monitoring data are stored
- **Documentation updates** — when and how operational docs are refreshed
- **Decommissioning** — criteria and procedure for retiring the model
- **Knowledge transfer** — how to onboard new team members to model ownership

### Step 8: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/6-deployment
```

Write the file `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md` using this template:

```markdown
# 6.2 Monitoring and Maintenance Plan

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 6. Deployment
> **Status:** Draft | Review | Approved

---

## Monitoring Overview

- **Model in Production:** [technique + version]
- **Baseline Performance:** [primary metric] = [value] (validation set, [date])
- **Minimum Acceptable Performance:** [metric] >= [threshold]
- **Ground Truth Lag:** [how long until actuals are available]
- **Monitoring Tool:** [tool/platform]
- **Dashboard Location:** [URL or path]

---

## Data Drift Monitoring

### Feature Drift

| Feature | Test | Reference Window | Warning Threshold | Critical Threshold | Frequency |
|---------|------|-----------------|-------------------|-------------------|-----------|
| [feature] | [PSI/KS/chi-sq] | [training data / last 30d] | [value] | [value] | [daily/weekly] |

### Label Drift
| Target Variable | Test | Warning Threshold | Critical Threshold | Frequency |
|----------------|------|-------------------|-------------------|-----------|
| [target] | [test] | [value] | [value] | [frequency] |

### Schema Drift
| Check | Description | Frequency |
|-------|-------------|-----------|
| Column presence | [all expected columns exist] | [every batch] |
| Data types | [types match expected schema] | [every batch] |
| Value ranges | [values within expected bounds] | [every batch] |

### Upstream Data Quality
| Source | Freshness SLA | Completeness Check | Quality Check |
|--------|--------------|-------------------|--------------|
| [source] | [e.g., data arrives by 04:00] | [e.g., < 5% missing] | [specific checks] |

---

## Prediction Monitoring

### Prediction Distribution
| Metric | Expected Range | Warning Threshold | Critical Threshold |
|--------|---------------|-------------------|-------------------|
| Mean prediction | [range] | [deviation] | [deviation] |
| Prediction variance | [range] | [deviation] | [deviation] |
| % predictions outside [range] | [baseline %] | [threshold] | [threshold] |

### Prediction Quality (vs. Actuals)
| Metric | Baseline | Warning Threshold | Critical Threshold | Calculation Window |
|--------|----------|-------------------|-------------------|--------------------|
| [primary metric] | [value] | [value] | [value] | [e.g., rolling 7 days] |
| [secondary metric] | [value] | [value] | [value] | [e.g., rolling 7 days] |

### Business Metric Tracking
| Business Metric | Baseline | Target | Measurement |
|----------------|----------|--------|------------|
| [e.g., workforce misallocation hours] | [current] | [target] | [how measured] |

---

## Alerting Strategy

### Alert Levels

| Level | Definition | Response Time | Escalation |
|-------|-----------|---------------|-----------|
| Info | [performance trending down but within bounds] | Next business day | None |
| Warning | [performance approaching minimum threshold] | Within 4 hours | [team lead] |
| Critical | [performance below minimum threshold or system failure] | Within 1 hour | [management] |

### Alert Configuration

| Alert | Metric | Condition | Level | Channel | Recipient |
|-------|--------|-----------|-------|---------|-----------|
| [alert name] | [metric] | [condition] | [level] | [channel] | [who] |

### On-call Procedures
| Scenario | Investigation Steps | Resolution Steps | Escalation |
|----------|-------------------|-----------------|-----------|
| Data drift alert | [steps] | [steps] | [who/when] |
| Performance degradation | [steps] | [steps] | [who/when] |
| Pipeline failure | [steps] | [steps] | [who/when] |
| Prediction anomaly | [steps] | [steps] | [who/when] |

---

## Retraining Strategy

### Retraining Triggers

| Trigger Type | Condition | Action |
|-------------|-----------|--------|
| Scheduled | [e.g., first Monday of each month] | Automatic retraining pipeline |
| Performance-based | [primary metric] < [threshold] for [N] consecutive days | Manual review + retraining |
| Drift-based | [drift metric] > [threshold] | Automatic retraining pipeline |
| Event-based | [e.g., new stores added, major restructuring] | Manual retraining with updated data |

### Retraining Pipeline

1. [Step 1 — e.g., collect data from last N months]
2. [Step 2 — e.g., run data preparation pipeline]
3. [Step 3 — e.g., train model with current hyperparameters]
4. [Step 4 — e.g., evaluate on holdout set]
5. [Step 5 — e.g., compare to production model]
6. [Step 6 — e.g., deploy if validation passes]

### Validation Gates for Retrained Models

| Gate | Criterion | Threshold |
|------|-----------|-----------|
| Performance | [metric] on holdout >= [threshold] | [value] |
| Regression | [metric] on holdout >= current production model | [value] |
| Data quality | Training data passes quality checks | Pass/Fail |
| Bias check | Fairness metrics within bounds | [value] |

### Data Window
- **Training window:** [e.g., last 24 months of data]
- **Rationale:** [why this window — recency vs. volume trade-off]
- **Expanding vs. sliding:** [expanding / sliding — with rationale]

---

## Maintenance Procedures

### Scheduled Maintenance
| Task | Frequency | Owner | Procedure |
|------|-----------|-------|-----------|
| Dependency updates | [frequency] | [who] | [how] |
| Infrastructure patches | [frequency] | [who] | [how] |
| Log rotation | [frequency] | [who] | [how] |
| Dashboard review | [frequency] | [who] | [how] |

### Model Versioning
- **Registry:** [e.g., MLflow Model Registry]
- **Naming convention:** [e.g., project-name/v1.0.0]
- **Retention:** [how many versions to keep, archival policy]

### Data Retention
| Data Type | Retention Period | Storage | Deletion Policy |
|-----------|-----------------|---------|----------------|
| Predictions | [period] | [where] | [how deleted] |
| Actuals | [period] | [where] | [how deleted] |
| Monitoring metrics | [period] | [where] | [how deleted] |
| Model artifacts | [period] | [where] | [how deleted] |

### Decommissioning Criteria
| Criterion | Description |
|-----------|-------------|
| [criterion] | [when the model should be retired — e.g., business process change, replacement model ready] |

---

## To Be Clarified

[List any items that need further investigation or stakeholder input. Remove this section if everything is complete.]

---

## Source Documents

- 6.1 Deployment Plan: `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
- 4.4 Model Assessment: `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
- 4.2 Test Design: `docs/crisp-dm/4-modeling/4.2-test-design.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 2.4 Data Quality: `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- Model Governance: `.claude/rules/model-governance.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| MLOps Engineer | | | Pending |
| Operations Lead | | | Pending |
| Business Stakeholder | | | Pending |
```

### Step 9: Summary and Next Steps

After writing the document, present a summary:

> **Monitoring and Maintenance Plan created** at `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`
>
> **Summary:**
> - [N] features monitored for drift
> - Prediction quality tracked against [metric] baseline of [value]
> - Alert levels: Info / Warning / Critical with defined thresholds
> - Retraining triggers: [scheduled/performance/drift/event-based]
> - Retraining cadence: [frequency]
> - Data retention: [summary]
> - Decommissioning criteria: defined
>
> **Next step in CRISP-DM:** Proceed to **6.3 Produce Final Report** — compile the complete project documentation including executive summary, technical report, and model card.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 6.2 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Data drift monitoring covers the most important input features (not just all of them)
- [ ] Drift detection methods are appropriate for the feature types (continuous vs. categorical)
- [ ] Prediction quality monitoring accounts for ground truth lag
- [ ] Alert thresholds are specific numbers, not vague descriptions
- [ ] Alert levels have clear escalation paths and response times
- [ ] Retraining triggers cover both scheduled and reactive scenarios
- [ ] Retrained models must pass validation gates before deployment (no automatic blind deployment)
- [ ] Data retention policy complies with GDPR and data minimization principles
- [ ] Monitoring dashboard location is specified
- [ ] On-call procedures are actionable (not just "investigate")
- [ ] Upstream data quality monitoring is included (not just model-level monitoring)
- [ ] Business metric tracking connects model performance to stakeholder-visible outcomes
- [ ] Decommissioning criteria and procedure are defined
- [ ] No PII or sensitive data in the monitoring plan
- [ ] All prerequisite documents are cross-referenced
