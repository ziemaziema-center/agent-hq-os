# Runway Prompt Pack: Agent HQ OS Grant Cut v3

Use these prompts in Runway Web UI to generate source clips only. Do not rely on Runway for final text, subtitles, product labels, or UI claims. Codex will add all precise text during final assembly.

## Recommended Runway Settings

- Mode: Text-to-video or Image-to-video if available
- Model: current best Gen-4 / Gen-4.5 option available in the account
- Aspect ratio: 16:9 landscape
- Duration: 5-7 seconds per clip
- Motion: medium, cinematic, controlled
- Style: dark cinematic developer-tool animation, polished but not flashy
- Export: MP4
- Important: avoid readable text inside the generated footage

## Global Negative Prompt

Use this negative prompt with every scene if Runway exposes a negative prompt field:

```text
No readable text, no fake logos, no GitHub stars, no fake metrics, no credentials, no API keys, no passwords, no trading screen, no production deployment, no celebrity faces, no exaggerated AGI fantasy, no chaotic glitch, no horror, no spam UI, no distorted hands, no unreadable UI claims, no watermark-like text.
```

## Naming Convention

After downloading, rename the clips exactly:

```text
v3_01_task_lands.mp4
v3_02_hq_assigns_agents.mp4
v3_03_agents_debate.mp4
v3_04_memory_vault.mp4
v3_06_build_happens.mp4
v3_07_deferred_gate.mp4
v3_10_telemetry_loop.mp4
```

Place them in:

```text
oss_portfolio_export/01_agent_hq_os/visuals/runway_v3_source_clips/
```

## Clip 01: Task Lands

Paste into Runway prompt box:

```text
Cinematic developer-tool animation. A focused software operator sits at a dark workstation as a serious project request arrives as a glowing abstract task object, not readable text. The room is quiet, technical, and high-trust. The task object expands into a structured execution card with abstract lines and nodes, no readable words. Camera slowly pushes in from behind the operator to the glowing task card. Premium AI infrastructure aesthetic, deep navy background, subtle teal and blue accents, realistic lighting, no logos, no readable text.
```

Purpose: establish "not chat, project execution."

## Clip 02: HQ Assigns Agents

Paste into Runway prompt box:

```text
Cinematic command-center animation. A central HQ coordinator avatar stands in a clean holographic operations room, assigning abstract agent avatars to different work lanes. Each agent is represented by a distinct glowing silhouette with subtle color coding, but no readable labels. The scene feels like a serious engineering operations center, not a fantasy spaceship. Smooth lateral camera move, balanced composition, dark UI panels, blue and green light, no readable text, no logos.
```

Purpose: show orchestration and role assignment.

## Clip 03: Agents Debate

Paste into Runway prompt box:

```text
Premium comic-cinematic animation of several abstract AI agent avatars around a holographic planning table. They compare three possible plan paths shown as abstract branching lines, then reject two weak paths with subtle red warning marks and keep one stable path in green. No readable text. The tone is intelligent, collaborative, and slightly playful, like a serious engineering review meeting. Camera orbits slowly around the table, clean dark background, polished developer-tool aesthetic.
```

Purpose: make multi-agent review visible and not fake.

## Clip 04: Memory Vault

Paste into Runway prompt box:

```text
Cinematic close-up of an abstract AI agent opening a secure glowing project-memory vault before touching any work. Inside the vault are organized abstract cards, timelines, and small warning markers, but no readable text. The feeling is careful, methodical, and safety-conscious. Camera moves from the agent's hand to the opening vault, teal and amber light, dark technical environment, no logos, no readable words.
```

Purpose: make memory-first workflow concrete.

## Clip 06: Build Happens

Paste into Runway prompt box:

```text
Fast but controlled engineering montage. Abstract builder agent assembles modular blocks representing files, demos, documentation, and validation checks. Blocks snap into a clean project structure, like a real software workspace becoming organized. No readable text. Smooth satisfying motion, no chaos, dark UI environment, subtle green validation glow, cinematic lighting, professional developer-tool style.
```

Purpose: show output as artifacts, not response text.

## Clip 07: Deferred Gate

Paste into Runway prompt box:

```text
Funny but professional cinematic scene. A glowing red live-action object rolls toward an automation pipeline, then a transparent safety gate drops calmly in front of it. The pipeline pauses without damage. A human operator silhouette appears beside the gate as the final approval boundary. No readable text, no logos, no dangerous content. Tone is clever and reassuring, not dramatic. Dark technical environment, red risk light, green safe path light.
```

Purpose: show safe bounded autonomy and human review.

## Clip 10: Telemetry Loop

Paste into Runway prompt box:

```text
Beautiful motion graphic animation of an execution feedback loop. Abstract signals for success, failure, decision, and follow-up move into a memory core, then a new session starts from that memory. No readable text. Smooth clockwise motion, elegant data trails, dark navy background, teal, blue, amber, and violet accents. High-trust AI infrastructure visual, clean and calm, no logos, no fake metrics.
```

Purpose: make telemetry and continuity memorable.

## Optional Alternate: Telegram Atmosphere Clip

Only use if you want Runway atmosphere behind Codex's deterministic Telegram UI. Do not use generated Telegram text as the final UI.

```text
Cinematic over-the-shoulder shot of a human operator holding a phone with an abstract chat interface controlling an automation run. The phone screen shows colored message bubbles and simple abstract buttons, but no readable text. The operator is in a dark engineering workspace with a large operations dashboard in the background. Calm, professional, high-trust, no logos, no readable words, no credentials.
```

## Download Checklist

- Each clip is MP4.
- Each clip is 16:9.
- No readable generated text is visible.
- No secret-looking strings appear.
- No fake product metrics appear.
- Visual style is consistent enough with the other clips.
- Rename files exactly before giving them back to Codex.
