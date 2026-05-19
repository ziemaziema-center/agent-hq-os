# Design Tradeoffs

## Why This Shape

This exists because long AI-assisted work tends to rot at the boundaries: the agent forgets yesterday's failure, the human forgets the exact validation command, and a second tool repeats the same bad assumption.

## Decisions That Were Intentional

- Prefer plain files over hidden state so a reviewer can inspect the operating model.
- Prefer fixture paths before live integrations so a new contributor can reproduce behavior safely.
- Prefer explicit human approval for risky actions over pretending automation can infer intent.

## What Was Intentionally Avoided

A hosted platform, a prompt library, and a complex agent framework. Plain files won because they survive tool changes and can be inspected in code review.

## Why Simpler Alternatives Were Not Enough

A README-only approach explains intent but does not create a repeatable operating loop. A script-only approach can validate structure but cannot capture judgment. The current shape keeps docs, examples, and validation close together because the failure modes usually happen between those layers.

## What Still Feels Messy

Memory files are only as good as the discipline of updating them. Too many templates can feel heavy for small tasks. Multi-agent meetings can become theater if nobody owns validation.

## Where the Architecture May Break

The model breaks when teams skip session boot, write vague telemetry, or treat agent role names as a substitute for engineering ownership.

## Scalability Concerns

The first scaling problem is not traffic. It is consistency. As more examples and adapters are added, each one must preserve the same safety boundary, fixture discipline, and validation expectation. Without that, the repo becomes a pile of special cases.

## Human Approval Still Required

Humans still decide risk boundaries, approve destructive changes, judge whether telemetry is useful, and decide when a failure is important enough to become memory.

