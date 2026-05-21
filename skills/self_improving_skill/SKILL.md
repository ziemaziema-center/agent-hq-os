---
name: self-improving-skill
description: Convert execution telemetry into review-gated improvements for Agent HQ OS memory, playbooks, and validation rules.
---

# Self-Improving Skill

Use this skill after a completed task, failed run, repeated reviewer finding, or unclear operating decision.

## Operating Rule

This skill proposes improvements. It does not apply them blindly.

Every improvement must be:

- evidence-backed;
- local and bounded;
- free of secrets or private execution details;
- reviewed by a maintainer;
- validated before it changes future behavior.

## Procedure

1. Read current memory:
   - `memory/KNOWN_FAILURES.md`
   - `memory/VALIDATED_PATTERNS.md`
   - `memory/PATCH_HISTORY.md`
2. Read task telemetry:
   - `telemetry/DAILY_EXECUTION_LOG.md`
   - `telemetry/SUCCESS_TELEMETRY.md`
   - `telemetry/FAILURE_TELEMETRY.md`
3. Classify the lesson:
   - repeated failure;
   - validated pattern;
   - ambiguous decision;
   - missing validation;
   - unsafe automation boundary;
   - documentation/onboarding friction.
4. Draft a proposal using `templates/SKILL_IMPROVEMENT_PROPOSAL.md`.
5. Define the narrowest validation command or review check.
6. Ask a maintainer to accept, revise, or reject the proposal.
7. If accepted, update memory and patch history.

## Safety Stop Conditions

Stop and require human review when the proposal touches:

- credentials or `.env` values;
- production URLs;
- social publishing;
- trading or finance actions;
- live n8n workflow activation;
- external API calls;
- destructive filesystem or Git operations;
- user identity, account metadata, or private logs.

## Output Format

```md
## Proposed Improvement

- Evidence:
- Proposed memory/playbook change:
- Validation:
- Safety boundary:
- Human decision needed:
```

## Example

```md
## Proposed Improvement

- Evidence: Two failed renders were caused by assuming FFmpeg existed on PATH.
- Proposed memory/playbook change: Add FFmpeg availability to preflight checks before promising local video output.
- Validation: Run `ffmpeg -version` and `python validation/validate_repo.py`.
- Safety boundary: Local-only check; no credentials or network calls.
- Human decision needed: Accept as a validated pattern.
```
