---
name: leakage-check
description: Audit a data pipeline or notebook for data leakage. Use during CRISP-DM Data Preparation to verify pipeline integrity.
argument-hint: "[file or directory to audit]"
user-invocable: true
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
