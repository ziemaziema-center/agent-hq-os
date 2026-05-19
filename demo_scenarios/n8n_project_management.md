# N8N Project Management

## User Request

Ship a realistic project improvement without losing safety, validation, or memory.

## HQ Planning

HQ reads `SESSION_BOOT.md`, checks known failures, identifies the files in scope, and chooses the minimum agent set.

## Agent Delegation

- Implementer owns the scoped change.
- Safety Reviewer checks external side effects and secret exposure.
- Validator owns the proof.

## Execution

The implementer makes the change, avoids unrelated refactors, and records assumptions.

## Validation

Validator runs the relevant script or checklist and records pass/fail evidence.

## Telemetry

HQ updates daily execution log, success telemetry, and failure telemetry if any assumption failed.

## Iteration

If validation fails, the failure becomes memory before the next attempt.

