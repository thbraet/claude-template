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
