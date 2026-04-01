# Explain Model to Stakeholder

Use this prompt when you need to explain a model's performance to a non-technical audience.

## Template

Read the model assessment from `docs/crisp-dm/4-modeling/4.4-model-assessment.md` and the business objectives from `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`.

Then produce a summary that covers:

1. **What the model does** — one sentence, no jargon (e.g., "The model predicts which passengers survived the Titanic disaster")
2. **How well it works** — translate the primary metric into plain language (e.g., "It correctly predicts the outcome for 84 out of 100 passengers")
3. **Where it struggles** — describe the main failure modes in business terms (e.g., "It tends to miss male passengers in third class who survived against the odds")
4. **What drives predictions** — list the top 3-5 factors in plain language (e.g., "Gender, ticket class, and age are the most important factors")
5. **What this means for the business** — connect to the business objective from 1.1
6. **What's next** — clear recommendation (deploy, iterate, or stop)

Rules:
- No technical terms (accuracy, F1, AUC, hyperparameter, feature importance)
- Use analogies and comparisons stakeholders can relate to
- Quantify in business units (euros, hours, units), not statistical units
- Keep it under 300 words
