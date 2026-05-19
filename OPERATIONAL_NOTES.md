# Operational Notes

## Manual Review Still Required

Humans still decide risk boundaries, approve destructive changes, judge whether telemetry is useful, and decide when a failure is important enough to become memory.

## What AI Should Not Automate Blindly

- Publishing, messaging, trading, or infrastructure mutation.
- Secret handling and credential rotation.
- Legal, compliance, platform policy, or financial risk decisions.
- Final public claims about readiness or adoption.

## Common Workflow Failures

- Skipping boot files because the task feels small.
- Treating a generated example as production-ready.
- Letting validation drift behind implementation.
- Recording telemetry that is too vague to help the next session.

## Onboarding Pain Points

New contributors may wonder why there are so many safety notes. The short answer is that these repos touch domains where a small automation mistake can escape the local machine.

## Brittle Areas

Memory files are only as good as the discipline of updating them. Too many templates can feel heavy for small tasks. Multi-agent meetings can become theater if nobody owns validation.

## Expected Learning Curve

Expect the first session to feel slower than a normal prompt. The payoff appears on the second and third sessions, when the project stops forgetting what it already learned.

