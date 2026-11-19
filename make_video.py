#!/usr/bin/env python3
"""Build a 1080x1920 short video (TikTok / Reels / Shorts) from an app recording or slides.

Usage: python3 make_video.py video.json out.mp4
{
  "source": "out/2026-11-21/recording.webm",       # or "slides": ["slide_01.png", ...] (3 s each)
  "trim": [2.0, 24.0],                              # optional start/end seconds of the recording
  "speed": 1.25,                                    # optional, speeds up slow parts
  "captions": [                                     # big on-screen text, timed (seconds of final video)
    {"t": [0, 2.5], "text": "колко калории има в една баница?"},
    {"t": [9, 14], "text": "спойлер: повече от обяд 😅"}
  ],
  "voice": {"text": "Снимаш баницата и за три секунди...", "voice": "bg-BG-BorislavNeural"},   # optional
  "music": "assets/music/track1.mp3"                # optional, royalty-free only
}
"""
import json, subprocess, sys, tempfile, asyncio
from pathlib import Path
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).parent))
from make_slides import font, wrap

W, H = 1080, 1920


def sh(*a):
    subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def caption_png(text, path):
    img = Image.new("RGBA", (W, 420), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(68)
    lines = wrap(d, text, f, 940)
    y = (420 - 85 * len(lines)) // 2
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2
        d.text((x, y), ln, font=f, fill="white", stroke_width=6, stroke_fill="black")
        y += 85
    img.save(path)


async def tts(text, voice, path):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate="+8%").save(path)


def build(spec, out):
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "base.mp4"
    bg = "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0b0f14,setsar=1"
    if "slides" in spec:
        lst = tmp / "l.txt"
        lst.write_text("".join(f"file '{Path(s).resolve()}'\nduration 3\n" for s in spec["slides"]) +
                       f"file '{Path(spec['slides'][-1]).resolve()}'\n")
        sh("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-vf",
           "fps=30," + bg + ",zoompan=z='min(zoom+0.0007,1.06)':d=1:s=1080x1920:fps=30",
           "-pix_fmt", "yuv420p", "-r", "30", str(base))
    else:
        tr = spec.get("trim")
        cut = ["-ss", str(tr[0]), "-to", str(tr[1])] if tr else []
        spd = spec.get("speed", 1.0)
        sh("ffmpeg", "-y", *cut, "-i", spec["source"], "-an", "-vf",
           f"{bg},setpts=PTS/{spd},fps=30", "-pix_fmt", "yuv420p", str(base))

    inputs, filt, last = ["-i", str(base)], "", "[0:v]"
    for i, c in enumerate(spec.get("captions", []), 1):
        p = tmp / f"c{i}.png"; caption_png(c["text"], p)
        inputs += ["-i", str(p)]
        a, b = c["t"]
        filt += f"{last}[{i}:v]overlay=0:240:enable='between(t,{a},{b})'[v{i}];"
        last = f"[v{i}]"
    n = len(spec.get("captions", [])) + 1
    audio = []
    if spec.get("voice"):
        vp = tmp / "voice.mp3"
        asyncio.run(tts(spec["voice"]["text"], spec["voice"].get("voice", "bg-BG-BorislavNeural"), str(vp)))
        inputs += ["-i", str(vp)]; audio.append(f"[{n}:a]volume=1.0[a{n}]"); n += 1
    if spec.get("music"):
        inputs += ["-stream_loop", "-1", "-i", spec["music"]]; audio.append(f"[{n}:a]volume=0.12[a{n}]"); n += 1
    amap = []
    if audio:
        labels = "".join(x.split("]")[-2] + "]" for x in audio)
        filt += ";".join(audio) + f";{labels}amix=inputs={len(audio)}:duration=first[aout];"
        amap = ["-map", "[aout]"]
    filt = filt.rstrip(";") or "null"
    vmap = ["-map", last] if last != "[0:v]" else ["-map", "0:v"]
    sh("ffmpeg", "-y", *inputs, "-filter_complex", filt if filt != "null" else "[0:v]null[vout]",
       *(vmap if filt != "null" else ["-map", "[vout]"]), *amap, "-shortest" if audio else "-y",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-c:a", "aac", "-movflags", "+faststart", out)
    print(out)


if __name__ == "__main__":
    build(json.loads(Path(sys.argv[1]).read_text()), sys.argv[2])
