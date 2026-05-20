# Agent HQ OS Grant Cut v3 Plan

This plan is for the public-facing grant/application video, not a generic README GIF. The goal is to make Agent HQ OS understandable as an operator-governed AI runtime in under 90 seconds.

## Positioning

Agent HQ OS should not look like another prompt pack or a montage of AI agents. The video must show a system of work:

- a serious task enters Codex;
- HQ assigns agents and ownership;
- agents review the plan before building;
- memory is read before edits;
- work moves through queue/state stages;
- risky actions stop at deferred gates;
- Telegram acts as the operator console;
- validation and telemetry close the loop for the next session.

## Target Cut

- Length: 80-90 seconds
- Format: 1920x1080, 30fps, H.264 MP4
- Voice: natural English neural narration
- Subtitles: burned-in Korean subtitles plus separate English/Korean SRT files
- Style: cinematic technical motion graphics, not AGI fantasy
- Tone: serious, operational, safety-aware, developer-tool credible

## Production Split

Runway should generate only atmosphere and character/action shots. It should not generate final UI text, repo claims, diagrams, or subtitles.

Codex/FFmpeg should own all precise information:

- scene titles;
- Korean subtitles;
- Telegram control labels;
- queue/state labels;
- validation gates;
- telemetry labels;
- final architecture map;
- MP4/GIF/thumbnail packaging;
- README-safe relative paths.

## Scene Plan

| Scene | Time | Purpose | Visual Type | Runway Needed |
| --- | ---: | --- | --- | --- |
| 01 | 0-7s | Show why chat alone is not execution | Cinematic developer task intake | Yes |
| 02 | 7-15s | HQ converts task into project | HQ control room assigning agents | Yes |
| 03 | 15-23s | Agents debate strategy before building | Agent council / whiteboard | Yes |
| 04 | 23-31s | Memory-first boot prevents repeated failures | Project memory vault | Yes |
| 05 | 31-39s | Queue/state runtime makes work visible | Deterministic motion graphics | No |
| 06 | 39-48s | Build produces artifacts, not a paragraph | Engineering montage | Yes |
| 07 | 48-57s | Deferred gates stop unsafe actions | Gate / blocked live action | Yes |
| 08 | 57-67s | Telegram controls the run | Deterministic Telegram UI | No |
| 09 | 67-76s | Validation-first execution | Deterministic validation board | Optional |
| 10 | 76-84s | Telemetry closes the loop | Telemetry loop / audit trail | Yes |
| 11 | 84-90s | Final flagship reveal | Deterministic system map | No |

## Narrative Script

1. "A task lands in Codex. HQ treats it like a project, not a chat reply."
2. "It assigns roles, ownership, and review responsibility before work starts."
3. "The agents challenge the plan. Weak shortcuts are rejected early."
4. "Memory opens first, so old failures are not repeated."
5. "Work moves through visible states: planned, building, blocked, validating, reviewed."
6. "The build produces files, demos, docs, and validation checks."
7. "Risky actions stop at deferred gates until a human approves."
8. "Telegram becomes the ops console: approve, reject, pause, retry, status, and logs."
9. "Validation happens before confidence. Evidence beats vibes."
10. "Telemetry records what worked, what failed, and what the next session should remember."
11. "Agent HQ OS: memory, agents, gates, Telegram control, validation, and telemetry."

## Korean Subtitle Intent

Korean subtitles should be direct and operational, not literal marketing translation. They should help the viewer understand why the system matters:

- "답변" vs "프로젝트 실행" contrast;
- "역할 배정" and "소유권";
- "메모리 먼저";
- "상태 기반 실행";
- "Telegram에서 승인/거절/중지/재시도/상태 확인";
- "검증 전에는 완료가 아니다";
- "텔레메트리가 다음 세션의 기억이 된다".

## Runway Rules

Runway prompts must follow these constraints:

- No readable text inside generated footage.
- No fake GitHub stars, users, metrics, or testimonials.
- No live trading, production deployment, credential screens, or secret-like values.
- No brand logos except generic UI symbols.
- No real public figures.
- Keep characters consistent: abstract operators and luminous agent avatars, not celebrity faces.
- Generate 5-7 second clips in 16:9 landscape.
- Prefer image-to-video or Gen-4/Gen-4.5 with consistent style if available.

## Codex Assembly Rules

Codex should:

- normalize all source clips to 1920x1080;
- frame low-resolution clips inside a clean operator UI rather than stretching them;
- add Korean subtitles as burned-in text;
- generate English and Korean SRT files;
- create a short GIF preview for README;
- create a thumbnail with a clear product promise;
- run FFmpeg decode validation;
- extract QA frames from Telegram, queue/state, validation, and final scenes;
- scan public text artifacts for secret-like strings and local absolute paths;
- avoid pushing until final human review.

## Quality Gates

The cut is not ready unless all pass:

- The first 10 seconds explain that this is project execution, not chat.
- Telegram control appears visually, not only in narration.
- Validation and telemetry are shown as system parts, not vague claims.
- No generated text artifacts are used as authoritative product labels.
- Korean subtitles fit in the subtitle box without clipping.
- MP4 decodes cleanly.
- README preview GIF stays below a reasonable size.
- No local absolute paths appear in public markdown.
- No secret-like strings appear in public markdown or subtitles.

## Handoff

After Runway clips are generated, download them and place or rename them as:

```text
visuals/runway_v3_source_clips/v3_01_task_lands.mp4
visuals/runway_v3_source_clips/v3_02_hq_assigns_agents.mp4
visuals/runway_v3_source_clips/v3_03_agents_debate.mp4
visuals/runway_v3_source_clips/v3_04_memory_vault.mp4
visuals/runway_v3_source_clips/v3_06_build_happens.mp4
visuals/runway_v3_source_clips/v3_07_deferred_gate.mp4
visuals/runway_v3_source_clips/v3_10_telemetry_loop.mp4
```

Then run:

```bash
python tools/assemble_agent_demo_video_v3.py
```

Expected outputs:

```text
visuals/agent_hq_os_grant_cut_v3.mp4
visuals/agent_hq_os_grant_cut_v3_preview.gif
visuals/agent_hq_os_grant_cut_v3_thumbnail.png
visuals/agent_hq_os_grant_cut_v3.srt
visuals/agent_hq_os_grant_cut_v3_ko.srt
visuals/agent_hq_os_grant_cut_v3_render_report.md
```
