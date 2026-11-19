#!/usr/bin/env python3
"""Render a TikTok/IG slideshow (1080x1920 PNGs) from a JSON spec.

Spec (written by the agent):
{
  "slides": [
    {"type": "text",   "text": "I stopped guessing my calories.\nHere's what changed."},
    {"type": "screen", "screen": 2, "caption": "Snap the plate. Macros in 3 sec."},
    {"type": "text",   "text": "Free on Google Play — Pulsify", "small": true}
  ]
}
Usage: python3 make_slides.py spec.json out_dir
"""
import json, sys, random, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
ROOT = Path(__file__).parent
SCREENS = sorted((ROOT / "assets/screens").glob("*.png")) + sorted((ROOT / "assets/screens").glob("*.jpg"))
BG = (11, 15, 20)
ACCENT = (45, 226, 196)


def font(size, bold=True):
    for p in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    ]:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def wrap(draw, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=f) <= max_w:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines


def outlined_text(draw, xy_center_y, text, size, max_w=900):
    """TikTok-native look: white text, black outline, centered."""
    f = font(size)
    lines = wrap(draw, text, f, max_w)
    lh = int(size * 1.25)
    y = xy_center_y - lh * len(lines) // 2
    for ln in lines:
        x = (W - draw.textlength(ln, font=f)) / 2
        draw.text((x, y), ln, font=f, fill="white", stroke_width=max(4, size // 14), stroke_fill="black")
        y += lh


def bg_gradient():
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(glow)
    cx, cy = random.randint(200, 880), random.randint(300, 1600)
    d.ellipse((cx - 500, cy - 500, cx + 500, cy + 500), fill=(18, 60, 70))
    return Image.blend(img, glow.filter(ImageFilter.GaussianBlur(220)), 0.9)


def slide_text(s):
    img = bg_gradient()
    d = ImageDraw.Draw(img)
    outlined_text(d, H // 2, s["text"], 58 if s.get("small") else 76)
    return img


def slide_screen(s):
    img = bg_gradient()
    if SCREENS:
        shot = Image.open(SCREENS[s.get("screen", 0) % len(SCREENS)]).convert("RGB")
        shot.thumbnail((W - 120, H - 520))
        x, y = (W - shot.width) // 2, 380
        mask = Image.new("L", shot.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, *shot.size), 36, fill=255)
        img.paste(shot, (x, y), mask)
    d = ImageDraw.Draw(img)
    if s.get("caption"):
        outlined_text(d, 210, s["caption"], 64)
    return img


def main(spec_path, out_dir):
    spec = json.loads(Path(spec_path).read_text())
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, s in enumerate(spec["slides"], 1):
        img = slide_screen(s) if s["type"] == "screen" else slide_text(s)
        p = out / f"slide_{i:02d}.png"
        img.save(p, optimize=True)
        paths.append(str(p))
    print("\n".join(paths))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
