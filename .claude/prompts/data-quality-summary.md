# Data Quality Summary for Stakeholders

Use this prompt to produce a non-technical data quality summary for business owners.

## Template

Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md` and the data description from `docs/crisp-dm/2-data-understanding/2.2-data-description.md`.

Then produce a summary that answers:

1. **What data do we have?** — datasets, time range, volume (in plain terms: "12 months of delivery data covering 200 stores")
2. **How complete is it?** — percentage of usable records, key gaps (e.g., "95% of records are complete; the main gap is missing age information for 20% of passengers")
3. **Can we trust it?** — overall quality verdict: Good / Acceptable with caveats / Needs work
4. **What's missing or broken?** — top 3 quality issues in plain language, with business impact
5. **What do we need from you?** — any data access requests, clarifications, or business rules needed to proceed
6. **Recommendation** — can we proceed to data preparation, or is more data needed?

Rules:
- Frame quality issues as business risks, not statistical observations
- "20% missing ages" → "We can't determine age for 1 in 5 records, which may reduce prediction accuracy for age-dependent patterns"
- Keep it under 250 words
- End with a clear go/no-go recommendation
