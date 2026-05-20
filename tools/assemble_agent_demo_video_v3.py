#!/usr/bin/env python3
"""Assemble Agent HQ OS grant cut v3.

Place Runway source clips in:
  visuals/runway_v3_source_clips/

Required clip names are listed in visuals/runway_v3_shot_manifest.json.
If a clip is missing, this script renders a clear placeholder scene so timing,
voiceover, subtitles, and the final package can still be tested locally.
"""

from __future__ import annotations

import asyncio
import json
import math
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
VISUALS = ROOT / "visuals"
SRC = VISUALS / "runway_v3_source_clips"
WORK = ROOT.parent / "_private_render_work" / "agent_hq_os_grant_cut_v3"

WIDTH = 1920
HEIGHT = 1080
FPS = 30
SCENE_SECONDS = 8.0


@dataclass(frozen=True)
class Scene:
    n: int
    title: str
    label: str
    narration: str
    ko: str
    clip: str | None = None
    kind: str = "clip"


SCENES = [
    Scene(1, "A Real Task Lands", "NOT JUST CHAT", "A task lands in Codex. HQ treats it like a project, not a chat reply.", "작업이 들어오면 HQ는 단순 답변이 아니라 실제 프로젝트로 처리합니다.", "v3_01_task_lands.mp4"),
    Scene(2, "HQ Forms the Team", "AGENT ROLES", "HQ assigns roles, ownership, and review responsibility before work starts.", "HQ가 역할, 소유권, 리뷰 책임을 먼저 배정합니다.", "v3_02_hq_assigns_agents.mp4"),
    Scene(3, "Agents Challenge the Plan", "REVIEW LOOP", "The agents challenge the plan. Weak shortcuts are rejected early.", "에이전트들이 계획을 검토하고 약한 지름길은 초기에 걸러냅니다.", "v3_03_agents_debate.mp4"),
    Scene(4, "Memory Boots First", "SESSION_BOOT", "Memory opens first, so old failures are not repeated.", "먼저 메모리를 열어 같은 실패가 반복되지 않게 합니다.", "v3_04_memory_vault.mp4"),
    Scene(5, "Queue and State Runtime", "VISIBLE WORK", "Work moves through visible states: planned, building, blocked, validating, and reviewed.", "작업은 계획, 빌드, 차단, 검증, 리뷰 상태로 투명하게 이동합니다.", kind="queue"),
    Scene(6, "The Build Becomes Real", "FILES, DEMOS, TESTS", "The build produces files, demos, docs, and validation checks.", "빌드는 파일, 데모, 문서, 검증 체크라는 실제 산출물로 남습니다.", "v3_06_build_happens.mp4"),
    Scene(7, "Deferred Gates Hold Risk", "HUMAN BOUNDARIES", "Risky actions stop at deferred gates until a human approves.", "위험한 작업은 사람이 승인할 때까지 지연 게이트에서 멈춥니다.", "v3_07_deferred_gate.mp4"),
    Scene(8, "Telegram Ops Console", "CONTROL FROM CHAT", "Telegram becomes the ops console: approve, reject, pause, retry, status, and logs.", "Telegram에서 승인, 거절, 일시정지, 재시도, 상태 확인, 로그 확인까지 제어합니다.", kind="telegram"),
    Scene(9, "Validation Before Confidence", "EVIDENCE FIRST", "Validation happens before confidence. Evidence beats vibes.", "확신보다 검증이 먼저입니다. 느낌보다 증거가 우선입니다.", kind="validation"),
    Scene(10, "Telemetry Closes the Loop", "NEXT SESSION MEMORY", "Telemetry records what worked, what failed, and what the next session should remember.", "텔레메트리는 성공, 실패, 다음 세션이 기억할 결정을 기록합니다.", "v3_10_telemetry_loop.mp4"),
    Scene(11, "Agent HQ OS", "SAFE BOUNDED AUTONOMY", "Agent HQ OS connects memory, agents, queues, gates, Telegram control, validation, and telemetry.", "Agent HQ OS는 메모리, 에이전트, 큐, 게이트, Telegram 제어, 검증, 텔레메트리를 연결합니다.", kind="final"),
]


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def font(name: str, size: int):
    for candidate in [
        Path("C:/Windows/Fonts") / name,
        Path("C:/Windows/Fonts/malgun.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


FONT_H1 = font("segoeuib.ttf", 64)
FONT_H2 = font("segoeuisb.ttf", 38)
FONT_BODY = font("segoeui.ttf", 29)
FONT_KO = font("malgun.ttf", 31)
FONT_SMALL = font("segoeui.ttf", 22)
FONT_MONO = font("consola.ttf", 24)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    out: list[str] = []
    line = ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_w:
            line = test
        else:
            if line:
                out.append(line)
            line = word
    if line:
        out.append(line)
    return out


def make_bg(scene: Scene) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#080d15")
    px = img.load()
    accents = [
        ((60, 140, 255), (45, 225, 160)),
        ((100, 100, 245), (255, 184, 72)),
        ((55, 225, 165), (110, 190, 255)),
        ((255, 184, 72), (100, 190, 255)),
        ((255, 184, 72), (255, 96, 120)),
        ((92, 190, 255), (45, 225, 160)),
        ((255, 96, 120), (255, 184, 72)),
        ((46, 229, 157), (75, 170, 255)),
        ((255, 184, 72), (46, 229, 157)),
        ((96, 110, 250), (46, 229, 157)),
        ((255, 255, 255), (46, 229, 157)),
    ]
    a, b = accents[(scene.n - 1) % len(accents)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            d1 = math.sqrt(((x - WIDTH * 0.18) / WIDTH) ** 2 + ((y - HEIGHT * 0.18) / HEIGHT) ** 2)
            d2 = math.sqrt(((x - WIDTH * 0.90) / WIDTH) ** 2 + ((y - HEIGHT * 0.85) / HEIGHT) ** 2)
            r1 = max(0.0, 1.0 - d1 * 2.2)
            r2 = max(0.0, 1.0 - d2 * 2.0)
            px[x, y] = tuple(min(255, int([8, 13, 21][i] + a[i] * r1 * 0.20 + b[i] * r2 * 0.16)) for i in range(3))
    return img


def rounded(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chrome(draw: ImageDraw.ImageDraw, scene: Scene) -> None:
    for x in range(0, WIDTH, 80):
        draw.line((x, 0, x, HEIGHT), fill=(255, 255, 255, 9), width=1)
    for y in range(0, HEIGHT, 80):
        draw.line((0, y, WIDTH, y), fill=(255, 255, 255, 8), width=1)
    draw.text((88, 52), f"SCENE {scene.n:02d}", font=FONT_MONO, fill=(150, 190, 255, 255))
    draw.text((88, 88), scene.title, font=FONT_H1, fill=(246, 249, 255, 255))
    rounded(draw, (1400, 60, 1820, 118), 18, (255, 255, 255, 18), (255, 255, 255, 60), 1)
    w = draw.textbbox((0, 0), scene.label, font=FONT_SMALL)[2]
    draw.text((1400 + (420 - w) / 2, 77), scene.label, font=FONT_SMALL, fill=(228, 238, 255, 240))
    rounded(draw, (86, 922, 1834, 1020), 24, (0, 0, 0, 142), (255, 255, 255, 36), 1)
    lines = wrap(draw, scene.ko, FONT_KO, 1570)
    y = 950 if len(lines) == 1 else 936
    for line in lines[:2]:
        draw.text((130, y), line, font=FONT_KO, fill=(246, 248, 255, 250))
        y += 39
    for idx in range(len(SCENES)):
        fill = (78, 222, 161, 230) if idx < scene.n else (255, 255, 255, 36)
        rounded(draw, (148 + idx * 34, 1040, 148 + idx * 34 + 22, 1048), 4, fill)


def draw_clip_frame(draw: ImageDraw.ImageDraw, scene: Scene, missing: bool) -> None:
    frame = (300, 188, 1620, 896)
    rounded(draw, frame, 24, (10, 16, 28, 226), (118, 174, 255, 96), 2)
    if missing:
        rounded(draw, (445, 390, 1475, 650), 28, (255, 184, 72, 28), (255, 184, 72, 150), 2)
        draw.text((610, 448), "RUNWAY SOURCE CLIP NEEDED", font=FONT_H2, fill=(255, 245, 220, 255))
        draw.text((590, 512), scene.clip or "synthetic scene", font=FONT_MONO, fill=(255, 225, 180, 240))
        draw.text((545, 565), "Generate/download this clip, then rerun the v3 assembler.", font=FONT_BODY, fill=(230, 238, 255, 230))


def draw_queue(draw: ImageDraw.ImageDraw) -> None:
    states = [("PLANNED", "scope + roles"), ("BUILDING", "files + demos"), ("BLOCKED", "human gate"), ("VALIDATING", "tests + review"), ("REVIEWED", "telemetry saved")]
    colors = [(118, 174, 255), (46, 229, 157), (255, 96, 120), (255, 184, 77), (180, 145, 255)]
    for idx, (state, note) in enumerate(states):
        x = 190 + idx * 315
        y = 330
        c = colors[idx]
        rounded(draw, (x, y, x + 250, y + 145), 24, (*c, 34), (*c, 180), 2)
        draw.text((x + 28, y + 36), state, font=FONT_MONO, fill=(246, 249, 255, 255))
        draw.text((x + 28, y + 86), note, font=FONT_SMALL, fill=(218, 232, 245, 230))
        if idx < len(states) - 1:
            draw.line((x + 265, y + 72, x + 305, y + 72), fill=(220, 235, 255, 150), width=4)
    draw.text((430, 585), "Visible states prevent invisible automation drift.", font=FONT_H2, fill=(240, 247, 255, 245))


def draw_telegram(draw: ImageDraw.ImageDraw) -> None:
    rounded(draw, (690, 185, 1230, 850), 38, (9, 14, 24, 248), (83, 170, 255, 140), 2)
    rounded(draw, (720, 224, 1200, 800), 24, (15, 25, 38, 255), (255, 255, 255, 30), 1)
    draw.text((760, 248), "Telegram Ops Console", font=FONT_H2, fill=(245, 249, 255, 255))
    messages = [("HQ", "Validation pending."), ("Safety", "Live action is gated."), ("Operator", "Approve docs. Hold live."), ("HQ", "Telemetry saved.")]
    y = 332
    for sender, msg in messages:
        rounded(draw, (760, y, 1160, y + 72), 18, (65, 140, 255, 30), (65, 140, 255, 120), 1)
        draw.text((784, y + 13), sender, font=FONT_MONO, fill=(120, 190, 255, 255))
        draw.text((784, y + 40), msg, font=FONT_SMALL, fill=(236, 244, 255, 240))
        y += 88
    buttons = [("APPROVE", 230, 380), ("REJECT", 230, 490), ("PAUSE", 230, 600), ("RETRY", 1420, 380), ("STATUS", 1420, 490), ("LOGS", 1420, 600)]
    for label, x, y in buttons:
        rounded(draw, (x, y, x + 250, y + 78), 20, (255, 255, 255, 18), (255, 255, 255, 110), 2)
        draw.text((x + 42, y + 25), label, font=FONT_MONO, fill=(245, 249, 255, 250))


def draw_validation(draw: ImageDraw.ImageDraw) -> None:
    checks = [("structure", "PASS"), ("secrets", "PASS"), ("links", "PASS"), ("unsafe action", "BLOCKED"), ("review", "REQUIRED")]
    x0, y0 = 430, 290
    for idx, (name, status) in enumerate(checks):
        y = y0 + idx * 86
        color = (46, 229, 157) if status == "PASS" else (255, 184, 77) if status == "REQUIRED" else (255, 96, 120)
        rounded(draw, (x0, y, x0 + 1060, y + 64), 16, (*color, 28), (*color, 160), 2)
        draw.text((x0 + 30, y + 18), name, font=FONT_MONO, fill=(245, 249, 255, 245))
        draw.text((x0 + 830, y + 18), status, font=FONT_MONO, fill=(*color, 255))
    draw.text((545, 760), "Validation happens before confidence.", font=FONT_H2, fill=(240, 247, 255, 245))


def draw_final(draw: ImageDraw.ImageDraw) -> None:
    center = (960, 505)
    rounded(draw, (705, 392, 1215, 608), 32, (46, 229, 157, 48), (84, 245, 184, 190), 3)
    draw.text((805, 444), "Agent HQ OS", font=FONT_H2, fill=(246, 255, 252, 255))
    draw.text((790, 502), "project execution runtime", font=FONT_SMALL, fill=(220, 238, 235, 240))
    nodes = [("MEMORY", 320, 240), ("AGENTS", 1340, 240), ("QUEUE", 325, 670), ("GATES", 1350, 670), ("TELEGRAM", 705, 735), ("VALIDATION", 980, 735), ("TELEMETRY", 1180, 500)]
    for label, x, y in nodes:
        draw.line((center[0], center[1], x + 120, y + 36), fill=(100, 190, 255, 120), width=3)
        rounded(draw, (x, y, x + 245, y + 74), 20, (255, 255, 255, 18), (120, 190, 255, 130), 2)
        w = draw.textbbox((0, 0), label, font=FONT_MONO)[2]
        draw.text((x + (245 - w) / 2, y + 24), label, font=FONT_MONO, fill=(245, 249, 255, 255))


def make_scene_bg(scene: Scene, out: Path, missing: bool) -> None:
    img = make_bg(scene)
    draw = ImageDraw.Draw(img, "RGBA")
    chrome(draw, scene)
    if scene.kind == "clip":
        draw_clip_frame(draw, scene, missing)
    elif scene.kind == "queue":
        draw_queue(draw)
    elif scene.kind == "telegram":
        draw_telegram(draw)
    elif scene.kind == "validation":
        draw_validation(draw)
    elif scene.kind == "final":
        draw_final(draw)
    img.save(out)


def tts(text: str, out: Path) -> None:
    try:
        import edge_tts

        mp3 = out.with_suffix(".mp3")

        async def synth() -> None:
            voice = edge_tts.Communicate(text=text, voice="en-US-BrianNeural", rate="+5%")
            await voice.save(str(mp3))

        asyncio.run(synth())
        run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-ar", "48000", "-ac", "2", str(out)])
    except Exception as exc:
        print(f"TTS fallback: {exc}", file=sys.stderr)
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000", "-t", str(SCENE_SECONDS), str(out)])


def render_scene(scene: Scene, clip: Path | None, bg: Path, voice: Path, out: Path) -> None:
    if clip and clip.exists():
        filt = (
            f"[1:v]fps={FPS},scale=1160:-2:flags=lanczos,setsar=1,tpad=stop_mode=clone:stop_duration=3,"
            f"trim=0:{SCENE_SECONDS},setpts=PTS-STARTPTS[v];"
            f"[0:v][v]overlay=(W-w)/2:216:format=auto,fade=t=in:st=0:d=0.2,fade=t=out:st={SCENE_SECONDS-0.2}:d=0.2,format=yuv420p[vo];"
            f"[2:a]aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{SCENE_SECONDS},afade=t=in:st=0:d=0.1,afade=t=out:st={SCENE_SECONDS-0.25}:d=0.25[ao]"
        )
        inputs = ["-loop", "1", "-t", str(SCENE_SECONDS), "-i", str(bg), "-i", str(clip), "-i", str(voice)]
    else:
        filt = (
            f"[0:v]scale={WIDTH}:{HEIGHT},zoompan=z='min(zoom+0.0008,1.05)':d={int(SCENE_SECONDS*FPS)}:"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={WIDTH}x{HEIGHT}:fps={FPS},"
            f"trim=0:{SCENE_SECONDS},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.2,fade=t=out:st={SCENE_SECONDS-0.2}:d=0.2,format=yuv420p[vo];"
            f"[1:a]aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{SCENE_SECONDS},afade=t=in:st=0:d=0.1,afade=t=out:st={SCENE_SECONDS-0.25}:d=0.25[ao]"
        )
        inputs = ["-loop", "1", "-t", str(SCENE_SECONDS), "-i", str(bg), "-i", str(voice)]
    run(["ffmpeg", "-y", *inputs, "-filter_complex", filt, "-map", "[vo]", "-map", "[ao]", "-r", str(FPS), "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", str(out)])


def write_srt(path: Path, korean: bool) -> None:
    def ts(sec: float) -> str:
        ms = int((sec - int(sec)) * 1000)
        return f"00:{int(sec//60):02d}:{int(sec%60):02d},{ms:03d}"
    lines: list[str] = []
    for scene in SCENES:
        start = (scene.n - 1) * SCENE_SECONDS
        end = start + SCENE_SECONDS - 0.2
        text = scene.ko if korean else scene.narration
        lines.extend([str(scene.n), f"{ts(start)} --> {ts(end)}", text, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise SystemExit("ffmpeg and ffprobe are required")
    WORK.mkdir(parents=True, exist_ok=True)
    SRC.mkdir(parents=True, exist_ok=True)
    VISUALS.mkdir(parents=True, exist_ok=True)

    rendered: list[Path] = []
    missing: list[str] = []
    for scene in SCENES:
        clip = SRC / scene.clip if scene.clip else None
        is_missing = scene.kind == "clip" and (clip is None or not clip.exists())
        if is_missing and scene.clip:
            missing.append(scene.clip)
        bg = WORK / f"scene_{scene.n:02d}_bg.png"
        voice = WORK / f"scene_{scene.n:02d}_voice.wav"
        out = WORK / f"scene_{scene.n:02d}.mp4"
        make_scene_bg(scene, bg, is_missing)
        tts(scene.narration, voice)
        render_scene(scene, None if is_missing else clip, bg, voice, out)
        rendered.append(out)

    concat = WORK / "concat.txt"
    concat.write_text("".join(f"file '{p.as_posix()}'\n" for p in rendered), encoding="utf-8")
    mp4 = VISUALS / "agent_hq_os_grant_cut_v3.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(mp4)])

    srt = VISUALS / "agent_hq_os_grant_cut_v3.srt"
    ko_srt = VISUALS / "agent_hq_os_grant_cut_v3_ko.srt"
    write_srt(srt, korean=False)
    write_srt(ko_srt, korean=True)

    palette = WORK / "palette.png"
    gif = VISUALS / "agent_hq_os_grant_cut_v3_preview.gif"
    run(["ffmpeg", "-y", "-ss", "0", "-t", "24", "-i", str(mp4), "-vf", "fps=12,scale=960:-1:flags=lanczos,palettegen=stats_mode=diff", str(palette)])
    run(["ffmpeg", "-y", "-ss", "0", "-t", "24", "-i", str(mp4), "-i", str(palette), "-lavfi", "fps=12,scale=960:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=4", str(gif)])

    thumb = VISUALS / "agent_hq_os_grant_cut_v3_thumbnail.png"
    final_img = make_bg(SCENES[-1])
    draw = ImageDraw.Draw(final_img, "RGBA")
    chrome(draw, SCENES[-1])
    draw_final(draw)
    final_img.save(thumb)

    probe = run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size", "-show_streams", "-of", "json", str(mp4)])
    report = VISUALS / "agent_hq_os_grant_cut_v3_render_report.md"
    report.write_text(
        "\n".join([
            "# Agent HQ OS Grant Cut v3 Render Report",
            "",
            f"- Rendered: {datetime.now().isoformat(timespec='seconds')}",
            "- Voice: `en-US-BrianNeural`",
            "- Korean subtitles: burned in and exported as SRT",
            "- Safety: no credentials, no live workflow execution, no production deployment",
            "",
            "## Outputs",
            "",
            f"- `visuals/{mp4.name}`",
            f"- `visuals/{gif.name}`",
            f"- `visuals/{thumb.name}`",
            f"- `visuals/{srt.name}`",
            f"- `visuals/{ko_srt.name}`",
            "",
            "## Missing Runway Clips",
            "",
            *(f"- `{name}`" for name in missing),
            "" if missing else "- None",
            "",
            "## FFprobe",
            "",
            "```json",
            json.dumps(json.loads(probe.stdout), indent=2),
            "```",
        ]),
        encoding="utf-8",
    )
    print(f"MP4={mp4}")
    print(f"GIF={gif}")
    print(f"THUMBNAIL={thumb}")
    print(f"REPORT={report}")
    if missing:
        print("MISSING_RUNWAY_CLIPS=" + ",".join(missing))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
