#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/.env"
# User-scoped settings -- per-user home dir, never conflicts between users
USER_SETTINGS_LOCAL="$HOME/.claude/settings.local.json"

echo "=== Claude Code Template Setup ==="
echo ""

# --- Check Node.js / npm ---
if ! command -v npm &>/dev/null; then
  echo "[ERROR] npm is not installed. Install Node.js from https://nodejs.org/"
  exit 1
fi
echo "[OK] npm $(npm --version)"

# --- Check Claude Code ---
if command -v claude &>/dev/null; then
  echo "[OK] Claude Code installed"
else
  echo "[WARN] Claude Code not found. Install with: npm install -g @anthropic-ai/claude-code"
fi

# --- Create .env from .env.example if it doesn't exist ---
if [ -f "$ENV_FILE" ]; then
  echo "[OK] .env already exists"
else
  if [ -f "$SCRIPT_DIR/.env.example" ]; then
    cp "$SCRIPT_DIR/.env.example" "$ENV_FILE"
    echo "[CREATED] .env from .env.example -- fill in your tokens"
  fi
fi

# --- Read tokens from .env ---
declare -A ENV_VARS
if [ -f "$ENV_FILE" ]; then
  while IFS= read -r line; do
    # Skip comments and blank lines
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    key="${line%%=*}"
    value="${line#*=}"
    # Strip surrounding quotes if present
    value="${value#\"}"
    value="${value%\"}"
    value="${value#\'}"
    value="${value%\'}"
    if [[ -n "$key" && -n "$value" ]]; then
      ENV_VARS["$key"]="$value"
    fi
  done < "$ENV_FILE"
fi

# --- Check for missing tokens ---
MISSING=()
for key in GITLAB_TOKEN NOTION_TOKEN DATABASE_URL; do
  if [[ -z "${ENV_VARS[$key]:-}" ]]; then
    MISSING+=("$key")
  fi
done

if [[ ${#MISSING[@]} -gt 0 ]]; then
  echo ""
  echo "[WARN] Missing tokens in .env:"
  for key in "${MISSING[@]}"; do
    echo "         - $key"
  done
  echo "       Fill them in $ENV_FILE and re-run setup.sh"
fi

# --- Merge tokens into ~/.claude/settings.local.json ---
# User-scoped so multiple users on the same machine each get their own tokens.
# Merges new env vars without clobbering existing settings or other projects' vars.
mkdir -p "$HOME/.claude"

python3 -c "
import json, os, sys

path = '$USER_SETTINGS_LOCAL'

# Load existing settings if present
data = {}
if os.path.exists(path):
    with open(path) as f:
        data = json.load(f)

# Merge env vars (add/update, never remove existing keys)
env = data.setdefault('env', {})
new_vars = {
$(for key in "${!ENV_VARS[@]}"; do printf "    '%s': '%s',\n" "$key" "${ENV_VARS[$key]}"; done)
}
env.update(new_vars)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')

if new_vars:
    print(f'[OK] Merged {len(new_vars)} env var(s) into {path}')
else:
    print(f'[OK] No new env vars to merge into {path}')
" 2>/dev/null || {
  echo "[ERROR] Failed to update $USER_SETTINGS_LOCAL -- is python3 available?"
  exit 1
}

# --- Append Claude-specific gitignore entries ---
GITIGNORE="$SCRIPT_DIR/.gitignore"
GITIGNORE_CLAUDE="$SCRIPT_DIR/.gitignore.claude"
if [ -f "$GITIGNORE_CLAUDE" ]; then
  if ! grep -qxF '.claude/settings.local.json' "$GITIGNORE" 2>/dev/null; then
    cat "$GITIGNORE_CLAUDE" >> "$GITIGNORE"
    echo "[UPDATED] .gitignore with Claude-specific entries"
  else
    echo "[OK] .gitignore already has Claude entries"
  fi
fi

echo ""
echo "=== Setup complete ==="
echo ""
echo "Next steps:"
echo "  1. Fill in your tokens in .env (if not done already)"
echo "  2. Re-run 'bash setup.sh' after updating .env"
echo "  3. Run 'claude' to start Claude Code"
echo ""
