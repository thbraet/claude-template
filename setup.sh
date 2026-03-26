#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

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

# --- Generate .mcp.json from template ---
if [ -f "$SCRIPT_DIR/.mcp.json.template" ]; then
  cp "$SCRIPT_DIR/.mcp.json.template" "$SCRIPT_DIR/.mcp.json"
  echo "[GENERATED] .mcp.json from template"
else
  echo "[WARN] .mcp.json.template not found -- skipping MCP configuration"
fi

# --- Create .env from .env.example if it doesn't exist ---
if [ -f "$SCRIPT_DIR/.env" ]; then
  echo "[OK] .env already exists"
else
  if [ -f "$SCRIPT_DIR/.env.example" ]; then
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    echo "[CREATED] .env from .env.example -- fill in your tokens"
  fi
fi

# --- Append Claude-specific gitignore entries ---
GITIGNORE="$SCRIPT_DIR/.gitignore"
GITIGNORE_CLAUDE="$SCRIPT_DIR/.gitignore.claude"
if [ -f "$GITIGNORE_CLAUDE" ]; then
  if ! grep -qxF '.mcp.json' "$GITIGNORE" 2>/dev/null; then
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
echo "  1. Fill in your tokens in .env (GITLAB_TOKEN, GITHUB_TOKEN, etc.)"
echo "  2. Run 'claude' to start Claude Code"
echo ""
