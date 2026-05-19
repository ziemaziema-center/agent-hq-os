# Known Failures

Use this file to prevent repeated mistakes. Public examples must stay sanitized.

## Template Entry

- Date:
- Context:
- Failure:
- Impact:
- Detection:
- Prevention:

## Sanitized Example

- Date: 2026-05-19
- Context: media container readiness polling in a social publishing workflow.
- Failure: a terminal processing error was treated like a retryable timeout.
- Impact: the debug alert sent the operator toward retry behavior instead of immediate failure handling.
- Detection: a fixture status response returned `status_code=ERROR` after repeated polling.
- Prevention: classify terminal processing errors separately from readiness timeouts and stop retrying failed containers.

