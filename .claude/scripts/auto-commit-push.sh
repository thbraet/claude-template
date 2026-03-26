#!/usr/bin/env bash
# Auto-commit and push all changes after each Claude response.
# Called by the Stop hook in settings.

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

# Skip if no changes
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  exit 0
fi

# Stage all changes (tracked + untracked)
git add -A

# Generate commit message from staged diff
STAT=$(git diff --cached --stat | tail -1)          # e.g. "3 files changed, 10 insertions(+), 2 deletions(-)"
FILES=$(git diff --cached --name-only | head -5)     # first 5 changed files
FILE_COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')

# Build a short summary line
if [ "$FILE_COUNT" -eq 1 ]; then
  SUMMARY="update $(echo "$FILES" | head -1)"
elif [ "$FILE_COUNT" -le 5 ]; then
  SUMMARY="update $(echo "$FILES" | paste -sd ', ' -)"
else
  FIRST_THREE=$(echo "$FILES" | head -3 | paste -sd ', ' -)
  SUMMARY="update ${FIRST_THREE}, and $((FILE_COUNT - 3)) more files"
fi

# Commit
git commit -m "$(cat <<EOF
chore: ${SUMMARY}

${STAT}

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"

# Push to both remotes (non-blocking, best-effort)
git push github HEAD 2>/dev/null &
git push gitlab HEAD 2>/dev/null &
wait
