# Showcase Video Storyboard

Target length: 60-90 seconds  
Style: dark cinematic, technical, high-trust, operator-grade  
Purpose: GitHub README embed, Claude Code / OSS grant application support, launch post asset

## Creative Direction

The video should feel like an operator console for AI-assisted engineering, not a startup ad. Use restrained motion, dark interface surfaces, terminal panels, queue cards, telemetry lines, and calm narration. Avoid exaggerated claims such as "fully autonomous" or "revolutionary".

Core message:

> AI agents can work longer and safer when projects give them durable memory, validation gates, reviewer loops, and human boundaries.

## Scene-by-Scene Plan

| Scene | Duration | Visual direction | Narration | On-screen text | Runway / Pika / Luma motion prompt | Canva implementation notes | CapCut assembly notes |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| 1. Cold Start Failure | 0-8s | Dark terminal, fragmented chat windows fading in and out, repeated task notes dissolving | "AI agents are useful, but long projects break when every session starts cold." | `Stateless prompting loses operational memory.` | Paste into the generator prompt box: `Dark cinematic developer workstation. Multiple translucent chat windows and terminal panes flicker with repeated task context. Subtle blue-gray lighting, no logos, no readable secrets, high-trust technical mood, slow push-in camera, realistic UI abstraction.` | Create one 16:9 page with dark background, terminal rectangles, blurred text bars. Add the on-screen text centered low. | Add 1s fade in, low ambient hum, subtitle matching narration. |
| 2. Continuation Boot | 8-18s | `SESSION_BOOT.md` opens, memory files snap into a clean stack | "Agent HQ OS starts with continuation: boot instructions, known failures, validated patterns, and patch history." | `Continuation-first execution` | `A clean Markdown operations dashboard appears in a dark terminal environment. Files labeled SESSION_BOOT, KNOWN_FAILURES, VALIDATED_PATTERNS, PATCH_HISTORY align into a structured stack. Slow mechanical motion, crisp typography, cinematic shadows.` | Use four stacked cards with file names. Use monospace labels. | Cut on beat. Add small click sound as each file appears. |
| 3. Runtime Loop | 18-30s | Queue/state board: pending, blocked, validating, reviewed, done | "Work moves through queue and state, not vague intent. Every risky step has a gate." | `Queue / State Runtime` | `Dark operator console with kanban-like runtime state columns: pending, blocked, validating, reviewed, completed. Cards move slowly between columns. Technical, precise, no corporate hype, subtle telemetry lines.` | Build five columns as cards. Highlight one card moving from pending to validating. | Add motion blur lightly. Keep text readable. |
| 4. Deferred Gates | 30-42s | Gate closes before external actions: Telegram, n8n, credentials, trading, deploy | "Deferred gates keep external writes, credentials, publishing, trading, and infrastructure changes under human review." | `Deferred gates protect the boundary.` | `Cinematic security gate overlay on a technical workflow graph. Nodes labeled Telegram preview, n8n draft, credentials, deployment, trading research remain locked until human review. Dark interface, amber gate highlights, calm camera pan.` | Use icons or simple labels. Do not use real service screenshots. Use lock symbols and amber accents. | Add subtitle emphasis on "human review". |
| 5. Validation First | 42-55s | Validation command runs, terminal returns PASS, retry loop branches only when safe | "Validation comes before confidence. Retry only when the failure is actually retryable." | `Validation-first governance` | `Close-up of terminal command running local validation. PASS line appears. A branching flow shows retryable timeout versus terminal processing error. Dark technical UI, green validation signal, no secrets.` | Create split panel: terminal on left, decision tree on right. | Add terminal typing sound. Hold PASS for 1.5s. |
| 6. Telemetry Layer | 55-67s | Success/failure telemetry files update, audit line flows back to memory | "Every result becomes telemetry, so the next session starts smarter." | `Telemetry becomes memory.` | `Markdown telemetry files update in a dark workspace. Success log, failure log, decision log flow into a memory layer. Smooth line animation, precise operator aesthetic, restrained glow.` | Use three file cards: SUCCESS, FAILURE, DECISION. Draw arrows into MEMORY. | Add soft rise in music. Keep narration calm. |
| 7. Bounded Autonomy | 67-80s | Human operator, AI agent, and reviewer loop sit inside a bounded frame | "This is not uncontrolled autonomy. It is bounded execution with explicit stop conditions." | `Safe bounded autonomy, not autopilot.` | `Operator-grade AI runtime diagram in a dark interface. Human reviewer, AI agent, validation, and telemetry sit inside a bounded frame labeled safe scope. External actions remain outside locked gates. Slow cinematic zoom out.` | Use one large frame labeled `safe scope`. Put external actions outside the frame. | Add short pause after "not autopilot". |
| 8. Portfolio Close | 80-90s | Repo map appears: Agent HQ OS at center, related repos around it | "Agent HQ OS is the flagship of a public OSS portfolio for practical AI runtime operations." | `Agent HQ OS` / `Continuation. Validation. Telemetry. Review.` | `Dark cinematic GitHub-style repository map. Agent HQ OS in center, connected to playbooks, model routing workbench, n8n framework, safety lab, docs pack. High-trust technical finish, subtle glow, slow pullback.` | Use the public repo names as nodes. Keep typography large enough for mobile. | End with logo/title card and 1s fade out. |

## Exact Copy/Paste Instructions

### Runway / Pika / Luma

1. Open the video generator.
2. Create one clip per scene.
3. Paste the scene's "Runway / Pika / Luma motion prompt" into the prompt box.
4. Use 16:9 aspect ratio.
5. Use 5-10 seconds per clip depending on the duration column.
6. Do not upload screenshots that contain secrets, private URLs, or real credentials.
7. Export each clip as MP4.

### Canva

1. Create a 16:9 video design.
2. Make one page per scene.
3. Paste the scene's "On-screen text" into the Canva page text.
4. Use a dark background, monospace accents, and restrained blue/green/amber highlights.
5. Keep all text large enough for mobile viewing.
6. Add repo names and file names as abstract UI text only.
7. Export as MP4 if assembling in Canva, or export PNG pages if assembling in CapCut.

### CapCut

1. Import the generated MP4 clips or Canva page exports.
2. Place scenes in table order.
3. Add narration on the voiceover track.
4. Paste narration text as subtitles.
5. Keep subtitles bottom-center with high contrast.
6. Add low ambient technical music.
7. Add subtle click/terminal sounds only where useful.
8. Export final video at 1080p.

## Full Narration Script

AI agents are useful, but long projects break when every session starts cold.

Agent HQ OS starts with continuation: boot instructions, known failures, validated patterns, and patch history.

Work moves through queue and state, not vague intent. Every risky step has a gate.

Deferred gates keep external writes, credentials, publishing, trading, and infrastructure changes under human review.

Validation comes before confidence. Retry only when the failure is actually retryable.

Every result becomes telemetry, so the next session starts smarter.

This is not uncontrolled autonomy. It is bounded execution with explicit stop conditions.

Agent HQ OS is the flagship of a public OSS portfolio for practical AI runtime operations.

## Thumbnail Idea

Dark background with a clean runtime diagram:

- Center: `Agent HQ OS`
- Left: `Memory`
- Right: `Validation`
- Bottom: `Telemetry`
- Top-right lock label: `Human Review Gates`

Thumbnail text:

```text
AI Agents Need Runtime Discipline
```

Avoid faces, robots, exaggerated glow, or fake dashboards.

## Short YouTube / GitHub Description

Agent HQ OS is a continuation-first, validation-first runtime scaffold for AI-assisted engineering. It keeps memory, queue/state, deferred gates, reviewer loops, and telemetry inside the repo so agents can work safely without pretending to be autonomous production systems.

Public repo: https://github.com/ziemaziema-center/agent-hq-os

## Asset Checklist

- [ ] 8 generated video clips
- [ ] Canva title card
- [ ] CapCut subtitle track
- [ ] Voiceover track
- [ ] 1080p MP4 export
- [ ] 16:9 thumbnail PNG
- [ ] README embed or link

