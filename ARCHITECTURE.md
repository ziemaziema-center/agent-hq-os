# Architecture

## System Intent

Make AI execution inspectable and recoverable. The system should preserve decisions, known failures, validated patterns, and patch history so every new session starts with institutional memory.

## Main Components

- `AGENTS.md`: local operating instructions.
- `CLAUDE.md`: Claude/Claude Code specific guidance.
- `SESSION_BOOT.md`: startup checklist.
- `memory/`: known failures, validated patterns, patch history.
- `telemetry/`: daily logs and success/failure records.
- `playbooks/`: meeting and role protocols.

## Data Flow

A user request enters HQ, HQ loads memory, delegates bounded tasks, validates outputs, applies only complete changes, then writes telemetry back to memory.

## Trust Boundaries

- Local operator workspace.
- Sanitized public fixtures.
- Optional external APIs, which are disabled or stubbed in public examples.
- Telemetry and logs, which must never contain secrets.

## Failure Handling

- Prefer fail-closed behavior.
- Preserve append-only audit context for decisions.
- Use validation before mutation.
- Escalate ambiguous states to human review.

## Extension Points

- Add tool-specific boot templates.
- Add agent role cards.
- Add validation recipes for each project type.
- Add exporter scripts for public-safe documentation packs.

