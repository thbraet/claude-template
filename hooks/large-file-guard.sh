#!/usr/bin/env bash
# Hook: Large File Guard (PreToolUse on Bash)
# Warns when git add/commit would stage files >10MB.
# These should use DVC or Git LFS instead of being committed directly.
set -euo pipefail

INPUT=$(cat)
CMD=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Only check git add and git commit commands
echo "$CMD" | grep -qE '^\s*git\s+(add|commit)' || exit 0

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
THRESHOLD=10485760  # 10MB in bytes
LARGE_FILES=""

# Check files already staged
while IFS= read -r file; do
  [ -z "$file" ] && continue
  filepath="$PROJECT_ROOT/$file"
  [ ! -f "$filepath" ] && continue
  size=$(wc -c < "$filepath" 2>/dev/null | tr -d ' ')
  if [ "$size" -gt "$THRESHOLD" ]; then
    size_mb=$((size / 1048576))
    LARGE_FILES="${LARGE_FILES}  - ${file} (${size_mb}MB)\n"
  fi
done < <(git -C "$PROJECT_ROOT" diff --cached --name-only 2>/dev/null)

# For git add: also check files being explicitly added
if echo "$CMD" | grep -qE '^\s*git\s+add'; then
  # Extract file arguments (skip flags like -A, -u, --all)
  for arg in $(echo "$CMD" | sed 's/^\s*git\s\+add\s*//' | tr ' ' '\n'); do
    [[ "$arg" == -* ]] && continue
    [[ "$arg" == "." ]] && continue

    filepath="$arg"
    [ ! -f "$filepath" ] && filepath="$PROJECT_ROOT/$arg"
    [ ! -f "$filepath" ] && continue

    size=$(wc -c < "$filepath" 2>/dev/null | tr -d ' ')
    if [ "$size" -gt "$THRESHOLD" ]; then
      size_mb=$((size / 1048576))
      LARGE_FILES="${LARGE_FILES}  - ${arg} (${size_mb}MB)\n"
    fi
  done
fi

if [ -n "$LARGE_FILES" ]; then
  echo -e "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",\"permissionDecisionReason\":\"Large files detected (>10MB) — use DVC or Git LFS instead of committing directly:\n${LARGE_FILES}\"}}"
fi
