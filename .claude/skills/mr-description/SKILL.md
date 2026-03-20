---
name: mr-description
description: Generate a standardized GitLab merge request description from the current branch diff. Use when preparing to create a merge request.
argument-hint: "[target branch, default: main]"
user-invocable: true
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
