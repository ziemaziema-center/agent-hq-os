# AGENTS.md Template

## Operating Mode

Use memory-first, SESSION_BOOT, validation-first, additive-only, and post-task telemetry.

## Before Work

Read:

- `memory/KNOWN_FAILURES.md`
- `memory/VALIDATED_PATTERNS.md`
- `memory/PATCH_HISTORY.md`
- `SESSION_BOOT.md`

## During Work

- Prefer complete patches over partial edits.
- Preserve user changes.
- Validate before claiming completion.
- Escalate secret exposure risk immediately.

## After Work

Update:

- `telemetry/DAILY_EXECUTION_LOG.md`
- `telemetry/SUCCESS_TELEMETRY.md`
- `telemetry/FAILURE_TELEMETRY.md`

