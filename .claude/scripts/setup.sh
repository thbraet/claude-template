#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/.env"
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

# --- Merge tokens from .env into ~/.claude/settings.local.json ---
mkdir -p "$HOME/.claude"

python3 -c "
import json, os

env_file = '$ENV_FILE'
settings_path = '$USER_SETTINGS_LOCAL'

# Parse .env
new_vars = {}
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('\"').strip(\"'\")
            if key and value:
                new_vars[key] = value

# Check for missing tokens
required = ['GITLAB_TOKEN', 'NOTION_TOKEN', 'DATABASE_URL']
missing = [k for k in required if k not in new_vars]
if missing:
    print()
    print('[WARN] Missing tokens in .env:')
    for k in missing:
        print(f'         - {k}')
    print(f'       Fill them in {env_file} and re-run setup.sh')

# Load existing settings
data = {}
if os.path.exists(settings_path):
    with open(settings_path) as f:
        data = json.load(f)

# Merge env vars (add/update, never remove existing keys)
env = data.setdefault('env', {})
env.update(new_vars)

with open(settings_path, 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')

if new_vars:
    print(f'[OK] Merged {len(new_vars)} env var(s) into {settings_path}')
else:
    print(f'[OK] No new env vars to merge into {settings_path}')
"

# --- Ensure Claude-specific gitignore entries ---
GITIGNORE="$SCRIPT_DIR/.gitignore"
if ! grep -qxF '.claude/settings.local.json' "$GITIGNORE" 2>/dev/null; then
  printf '\n# Claude Code\n.claude/settings.local.json\n.claude/agent-memory-local/\n' >> "$GITIGNORE"
  echo "[UPDATED] .gitignore with Claude-specific entries"
else
  echo "[OK] .gitignore already has Claude entries"
fi

echo ""
echo "=== Setup complete ==="
echo ""
echo "Next steps:"
echo "  1. Fill in your tokens in .env (if not done already)"
echo "  2. Re-run 'bash setup.sh' after updating .env"
echo "  3. Run 'claude' to start Claude Code"
echo ""
