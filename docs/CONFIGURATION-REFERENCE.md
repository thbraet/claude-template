# Configuration Reference

Exhaustive reference for all Claude Code configuration options available in this template.

## Settings Files

### `.claude/settings.json` (Project Settings)

Shared across the team, committed to git.

| Option | Type | Description | Default in Template |
|---|---|---|---|
| `permissions.allow` | string[] | Tool patterns to auto-approve | Git, file ops, Python, DS tools |
| `permissions.deny` | string[] | Tool patterns to always block | `rm -rf`, force push, pipe to bash |
| `permissions.defaultMode` | string | Permission mode (`default`, `plan`, `bypassPermissions`) | `default` |
| `model` | string | Default model (`opus`, `sonnet`, `haiku`) | `opus` |
| `effortLevel` | string | Thinking effort (`low`, `medium`, `high`) | `medium` |
| `autoMemoryEnabled` | bool | Enable auto-memory across sessions | `true` |
| `enabledPlugins` | object | Plugin marketplace activations | compound-engineering, data |
| `env` | object | Environment variables for Claude Code | Timeout, telemetry settings |
| `hooks` | object | Pre/post tool execution hooks | Sensitive file guard |

### `.claude/settings.local.json` (Personal Overrides)

Gitignored, personal preferences.

| Option | Type | Description |
|---|---|---|
| `model` | string | Override the project model |
| `effortLevel` | string | Override thinking effort |
| `env.MAX_THINKING_TOKENS` | string | Max tokens for extended thinking |
| `theme` | string | Color theme (`dark`, `light`, `light-daltonized`, `dark-daltonized`) |
| `vim` | bool | Enable vim keybindings |

## Environment Variables

Set in `settings.json` under `env`, or in your shell.

| Variable | Description |
|---|---|
| `BASH_DEFAULT_TIMEOUT_MS` | Default timeout for bash commands (ms) |
| `DISABLE_TELEMETRY` | Disable anonymous usage telemetry |
| `DISABLE_ERROR_REPORTING` | Disable error reporting |
| `MAX_THINKING_TOKENS` | Max tokens for extended thinking |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens per response |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Context window percentage before auto-compacting |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model for subagents |
| `CLAUDE_CODE_SHELL` | Shell to use for bash commands |
| `ANTHROPIC_BASE_URL` | API proxy URL |
| `HTTP_PROXY` / `HTTPS_PROXY` | Corporate proxy |
| `CLAUDE_CODE_CLIENT_CERT` / `CLAUDE_CODE_CLIENT_KEY` | mTLS certificates |
| `DISABLE_AUTOUPDATER` | Disable automatic updates |
| `DISABLE_PROMPT_CACHING` | Disable prompt caching |

## Hooks

Hooks execute shell commands in response to Claude Code events.

| Event | When It Fires |
|---|---|
| `PreToolUse` | Before any tool execution |
| `PostToolUse` | After tool execution |
| `Notification` | When Claude sends a notification |
| `Stop` | When Claude finishes responding |

Hook response format (JSON to stdout):
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "reason shown to user"
  }
}
```

## Permissions

Permission patterns support glob matching:

```
Bash(git *)           # Any git command
Bash(python *)        # Any python command
WebFetch(domain:*)    # Any domain
Read                  # All file reads
```

## CLAUDE.md Files

| Location | Purpose | Loaded When |
|---|---|---|
| `CLAUDE.md` (root) | Org-wide instructions | Always |
| `.claude/CLAUDE.md` | Project-specific instructions | Always (via `@` import) |
| `@path` syntax | Import other instruction files | On reference |

## MCP Servers (`.mcp.json`)

See `docs/MCP-SERVERS-CATALOG.md` for available servers.

## Managed Settings (Enterprise)

For MDM-managed deployments, place settings in:
- macOS: `/Library/Application Support/ClaudeCode/settings.json`
- Linux: `/etc/claude-code/settings.json`

Managed options:
| Option | Description |
|---|---|
| `forceLoginMethod` | Enforce SSO login method |
| `disableBypassPermissionsMode` | Prevent bypassing permissions |
| `extraKnownMarketplaces` | Additional plugin marketplaces |

## Sandbox Configuration

| Option | Description |
|---|---|
| `sandbox.network` | Network access rules |
| `sandbox.filesystem` | Filesystem access rules |
