# Model Risk Assessment

Use this prompt to produce a structured risk assessment before deploying a model.

## Template

Read the following artifacts:
- `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
- `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`

Then produce a risk assessment covering:

### 1. Technical Risks
- **Overfitting risk**: Train vs. validation gap, dataset size, feature count ratio
- **Distribution shift risk**: How likely is the production data to differ from training data?
- **Feature availability risk**: Will all input features be available at inference time?
- **Latency/performance risk**: Can the model serve predictions within SLA requirements?

### 2. Data Risks
- **Data quality degradation**: What happens if upstream data quality drops?
- **Missing data risk**: What happens if a required feature is missing at inference?
- **Schema drift risk**: What happens if column names/types change upstream?
- **Data freshness risk**: How stale can the training data get before retraining is needed?

### 3. Business Risks
- **False positive cost**: What is the business impact of a false prediction?
- **False negative cost**: What is the business impact of a missed prediction?
- **Adoption risk**: Will end users trust and use the model's predictions?
- **Regulatory risk**: Any GDPR, fairness, or compliance concerns?

### 4. Mitigation Plan
For each risk rated Medium or High, provide:
- Monitoring mechanism (how will we detect this risk materializing?)
- Mitigation action (what do we do when it happens?)
- Owner (who is responsible?)

Format as a table:

| Risk | Severity | Likelihood | Monitoring | Mitigation | Owner |
|---|---|---|---|---|---|
