---
name: success-criteria
description: Map business KPIs to measurable technical metrics for a data science project. Use during CRISP-DM Business Understanding phase.
argument-hint: "[business objective]"
user-invocable: true
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
- Revenue impact -> Regression (RMSE, MAE, MAPE)
- Customer churn -> Classification (AUC-ROC, Precision-Recall, Lift)
- Anomaly detection -> Detection (Precision@K, Recall, F1)
- Ranking/recommendation -> Ranking (NDCG, MAP, MRR)
- Segmentation -> Clustering (Silhouette, Davies-Bouldin, business-defined purity)

Also generate:
- Baseline performance (what would a naive model achieve?)
- Minimum viable performance (below this, don't deploy)
- Target performance (what we're aiming for)
- Stretch goal (aspirational)
