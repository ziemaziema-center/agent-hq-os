# Agent HQ OS Showcase Render Report

Date: 2026-05-19

## Outputs

| Asset | Path | Size |
| --- | --- | ---: |
| MP4 | `visuals/agent_hq_os_showcase.mp4` | 7.25 MB |
| GIF | `visuals/agent_hq_os_showcase.gif` | 20.26 MB |
| Short preview GIF | `visuals/agent_hq_os_short_preview.gif` | 5.92 MB |
| Thumbnail | `visuals/agent_hq_os_thumbnail.png` | 0.10 MB |
| SRT | `visuals/voiceover_script.srt` | 0.00 MB |

## Technical Validation

- MP4 duration: 75.03s
- MP4 resolution: 1920x1080
- MP4 frame rate: 60/1
- MP4 codec: h264
- GIF streams detected: 1
- Short GIF streams detected: 1
- GIF loop mode: infinite (`loop=0`)
- Short preview GIF loop mode: infinite (`loop=0`)
- MP4 decode validation: passed with `ffmpeg -v error`
- README embed choice: short preview GIF embedded; full MP4 linked

## Render Notes

- Style: dark cinematic motion graphics.
- Source: generated operator-console frames plus existing Agent HQ OS visual language.
- No stock footage, no fake AGI imagery, no credential-bearing screenshots.
- Video includes silent AAC audio track for compatibility and separate `voiceover_script.srt` subtitles.
- Full GIF is GitHub-friendly preview quality; MP4 is the primary showcase asset.

## README Guidance

Use `agent_hq_os_short_preview.gif` for a lightweight README embed and link to the MP4 for the full showcase.
