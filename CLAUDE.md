# CLAUDE.md Template

Claude and Claude Code sessions should boot from local memory, state assumptions, and avoid live external side effects unless the operator explicitly confirms them.

## Required Startup

1. Read `SESSION_BOOT.md`.
2. Read memory files.
3. Identify safety-sensitive surfaces.
4. Define validation commands before patching.

## Patch Rules

- Additive by default.
- No secret exposure.
- No production mutation without explicit operator instruction.
- Record telemetry after completion.

