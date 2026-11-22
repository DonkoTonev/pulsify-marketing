#!/usr/bin/env python3
"""Build a 1080x1920 short video (TikTok / Reels / Shorts) from an app recording or slides.

Usage: python3 make_video.py video.json out.mp4
{
  "source": "out/2026-11-21/recording.webm",       # or "slides": ["slide_01.png", ...] (3 s each)
  "trim": [2.0, 24.0],                              # optional start/end seconds of the recording
  "speed": 1.25,                                    # optional, speeds up slow parts
  "captions": [                                     # big on-screen text, timed (seconds of final video)
    {"t": [0, 2.5], "text": "колко калории има в една баница?"},
    {"t": [9, 14], "text": "спойлер: повече от обяд"}
  ],
  "counter": {"t": [6, 12], "to": 1840, "from": 0, "ramp": 1.4, "suffix": " ккал", "y": 1020},
                                                    # motion graphic: a big number counting up to "to"
  "voice": {"text": "Снимаш баницата и за три секунди...", "voice": "bg-BG-BorislavNeural"},   # optional
  "music": "assets/music/track1.mp3",               # optional, royalty-free only
  "end_card": {"name": "Pulsify", "line1": "Свали безплатно от", "line2": "Google Play",
               "voice": "Свали Пулсифай безплатно от Гугъл Плей"}   # 3 s download card appended to the end
}
"""
import json, subprocess, sys, tempfile, asyncio
from pathlib import Path
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).parent))
from make_slides import font, wrap, bg_gradient, ACCENT

W, H = 1080, 1920


def sh(*a):
    subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def probe_dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True)
    return float(r.stdout.strip())


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


def counter_png(text, path, size=150):
    """Big accent-coloured number for the 'counting up' motion graphic."""
    img = Image.new("RGBA", (W, 320), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(size)
    x = (W - d.textlength(text, font=f)) / 2
    d.text((x, (320 - size * 1.15) / 2), text, font=f, fill=ACCENT, stroke_width=9, stroke_fill="black")
    img.save(path)


def render_end_card(ec, path):
    """2-3 s download card: Pulsify logo + 'Свали безплатно от Google Play' on a dark gradient."""
    img = bg_gradient()
    d = ImageDraw.Draw(img)
    logo_path = ec.get("logo", "assets/brand/pulsify_logo.png")
    if Path(logo_path).exists():
        size = 300
        lg = Image.open(logo_path).convert("RGB").resize((size, size))
        mask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, size, size), 66, fill=255)
        img.paste(lg, ((W - size) // 2, 540), mask)
    name = ec.get("name", "Pulsify")
    fn = font(118)
    d.text(((W - d.textlength(name, font=fn)) / 2, 880), name, font=fn,
           fill="white", stroke_width=3, stroke_fill="black")
    l1, l2 = ec.get("line1", "Свали безплатно от"), ec.get("line2", "Google Play")
    f1, f2 = font(62), font(86)
    d.text(((W - d.textlength(l1, font=f1)) / 2, 1130), l1, font=f1,
           fill=(222, 232, 236), stroke_width=4, stroke_fill="black")
    d.text(((W - d.textlength(l2, font=f2)) / 2, 1225), l2, font=f2,
           fill=ACCENT, stroke_width=5, stroke_fill="black")
    img.save(path)


async def tts(text, voice, path):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate="+8%").save(path)


def _segment(spec, out):
    """Render ONE 1080x1920 segment (app recording or slides) with captions/counter/voice/music."""
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "base.mp4"
    bg = "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0b0f14,setsar=1"
    if "slides" in spec:
        lst = tmp / "l.txt"
        lst.write_text("".join(f"file '{Path(s).resolve()}'\nduration {spec.get('slide_dur', 3)}\n" for s in spec["slides"]) +
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

    # Unified overlay list: timed captions (top) + optional counting-up number (lower third).
    overlays = []  # (png_path, t0, t1, y)
    for i, c in enumerate(spec.get("captions", []), 1):
        p = tmp / f"cap{i}.png"; caption_png(c["text"], p)
        overlays.append((p, c["t"][0], c["t"][1], c.get("y", 240)))
    cc = spec.get("counter")
    if cc:
        a, b = cc["t"]; frm = cc.get("from", 0); to = cc["to"]
        ramp = cc.get("ramp", 1.2); steps = cc.get("steps", 14)
        y = cc.get("y", 1000); suffix = cc.get("suffix", "")
        for k in range(steps + 1):
            val = round(frm + (to - frm) * k / steps)
            t0 = a + ramp * (k / steps)
            t1 = b if k == steps else a + ramp * ((k + 1) / steps)
            p = tmp / f"cnt{k}.png"; counter_png(f"{val}{suffix}", p)
            overlays.append((p, round(t0, 3), round(t1, 3), y))

    inputs, filt, last = ["-i", str(base)], "", "[0:v]"
    for i, (p, t0, t1, y) in enumerate(overlays, 1):
        inputs += ["-i", str(p)]
        filt += f"{last}[{i}:v]overlay=0:{y}:enable='between(t,{t0},{t1})'[v{i}];"
        last = f"[v{i}]"
    n = len(overlays) + 1
    audio = []
    if spec.get("voice"):
        vp = tmp / "voice.mp3"
        asyncio.run(tts(spec["voice"]["text"], spec["voice"].get("voice", "bg-BG-BorislavNeural"), str(vp)))
        inputs += ["-i", str(vp)]; audio.append(f"[{n}:a]volume=1.0[a{n}]"); n += 1
    if spec.get("music"):
        mvol = 0.12 if spec.get("voice") else 0.35  # quiet under a voice, fuller when music-only
        inputs += ["-stream_loop", "-1", "-i", spec["music"]]; audio.append(f"[{n}:a]volume={mvol}[a{n}]"); n += 1
    amap = []
    if audio:
        labels = "".join("[" + x.rsplit("[", 1)[1] for x in audio)
        filt += ";".join(audio) + f";{labels}amix=inputs={len(audio)}:duration=longest[aout];"
        amap = ["-map", "[aout]"]
    filt = filt.rstrip(";") or "null"
    vmap = ["-map", last] if last != "[0:v]" else ["-map", "0:v"]
    dur = probe_dur(base)  # hard-cap output to the visual length (music loops are infinite; -shortest is unreliable with filtergraphs)
    sh("ffmpeg", "-y", *inputs, "-filter_complex", filt if filt != "null" else "[0:v]null[vout]",
       *(vmap if filt != "null" else ["-map", "[vout]"]), *amap, "-t", f"{dur:.3f}",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-c:a", "aac", "-ar", "44100",
       "-movflags", "+faststart", out)


def concat_segments(parts, out):
    """Concatenate segments (normalising size/fps/sar/sample-rate so concat never mismatches)."""
    inputs = []
    for p in parts:
        inputs += ["-i", p]
    n = len(parts)
    pre = "".join(f"[{i}:v]scale=1080:1920,setsar=1,fps=30,format=yuv420p[v{i}];[{i}:a]aresample=44100[a{i}];"
                  for i in range(n))
    cat = "".join(f"[v{i}][a{i}]" for i in range(n))
    sh("ffmpeg", "-y", *inputs, "-filter_complex", pre + cat + f"concat=n={n}:v=1:a=1[v][a]",
       "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
       "-c:a", "aac", "-ar", "44100", "-movflags", "+faststart", out)


def build(spec, out):
    ec = spec.get("end_card")
    if not ec:
        _segment(spec, out)
        print(out); return
    tmp = Path(tempfile.mkdtemp())
    main_mp4 = str(tmp / "main.mp4")
    _segment({k: v for k, v in spec.items() if k != "end_card"}, main_mp4)
    ec_png = tmp / "endcard.png"; render_end_card(ec, ec_png)
    voice_name = (spec.get("voice") or {}).get("voice", "bg-BG-KalinaNeural")
    ec_spec = {"slides": [str(ec_png)], "slide_dur": ec.get("dur", 3),
               "voice": {"text": ec.get("voice", "Свали Пулсифай безплатно от Гугъл Плей"),
                         "voice": ec.get("voice_name", voice_name)},
               "music": spec.get("music")}
    ec_mp4 = str(tmp / "endcard.mp4")
    _segment(ec_spec, ec_mp4)
    concat_segments([main_mp4, ec_mp4], out)
    print(out)


if __name__ == "__main__":
    build(json.loads(Path(sys.argv[1]).read_text()), sys.argv[2])
