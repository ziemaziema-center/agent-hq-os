# Validated Patterns

Use this file to preserve approaches that have already worked. Keep public examples generic and fixture-based.

## Template Entry

- Pattern:
- Applies to:
- Validation evidence:
- Limits:

## Sanitized Example

- Pattern: distinguish terminal external processing failures from retryable readiness timeouts.
- Applies to: polling loops that wait for generated media, exports, or async jobs.
- Validation evidence: local fixture simulation with `status_code=ERROR` produced a non-retryable failure classification.
- Limits: this pattern preserves diagnostics; it does not recover failed external jobs.

