#!/usr/bin/env python3
"""Record a real session of the Pulsify web app in a phone-sized browser.

Usage: python3 record_app.py scenario.json out_dir
Scenario (written by the agent):
{
  "steps": [
    {"do": "login"},
    {"do": "click_text", "text": "Ястия"},
    {"do": "upload", "selector": "input[type=file]", "file": "assets/food/banitsa.jpg"},
    {"do": "wait", "ms": 6000},
    {"do": "scroll", "px": 400},
    {"do": "fill", "selector": "textarea", "text": "Какво да ям вечер на cut?"},
    {"do": "press", "key": "Enter"},
    {"do": "screenshot", "name": "result"}
  ]
}
Writes out_dir/recording.webm (+ screenshots). Credentials come from .env (TEST_EMAIL, TEST_PASSWORD).
"""
import json, os, sys, time, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

APP = os.environ.get("APP_URL", "https://apexfit-tracker.onrender.com/")


def run(scenario, out):
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = b.new_context(
            viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True,
            locale="bg-BG", record_video_dir=str(out / "raw"), record_video_size={"width": 780, "height": 1688},
        )
        pg = ctx.new_page()
        pg.set_default_timeout(45000)
        pg.goto(APP, wait_until="networkidle")  # Render may cold-start
        for s in scenario["steps"]:
            d = s["do"]
            if d == "login":
                pg.goto(APP.rstrip("/") + "/login", wait_until="networkidle")
                # Pulsify's username field has no type/name/id attribute — only
                # placeholder "Enter username or email". Match by placeholder, then
                # fall back to "the input that isn't the password/hidden field".
                user = pg.locator(
                    "input[type=email], input[name*=mail i], input[name*=user i], "
                    "input[placeholder*=mail i], input[placeholder*=user i], "
                    "input:not([type=password]):not([type=hidden]):not([type=checkbox]):not([type=radio])"
                ).first
                user.wait_for(state="visible")
                user.fill(os.environ["TEST_EMAIL"])
                pw = pg.locator("input[type=password]").first
                pw.fill(os.environ["TEST_PASSWORD"])
                btn = pg.get_by_role("button", name="Sign In")  # submit; fall back to Enter
                (btn.first.click() if btn.count() else pw.press("Enter"))
                pg.wait_for_load_state("networkidle")
                # On a Render cold start the post-login redirect can lag the 2.5 s wait,
                # so poll the URL for up to ~30 s before declaring failure (false-negative fix).
                for _ in range(30):
                    if "/login" not in pg.url:
                        break
                    pg.wait_for_timeout(1000)
                for skip in ("Пропусни", "Skip"):  # welcome tour
                    if pg.get_by_text(skip, exact=True).count():
                        pg.get_by_text(skip, exact=True).first.click()
                if "/login" in pg.url:
                    pg.screenshot(path=str(out / "login_failed.png"))
                    raise SystemExit("login failed — see login_failed.png")
            elif d == "goto":
                pg.goto(s["url"], wait_until="networkidle")
            elif d == "ensure_lang":
                # Header language button (title="Language") shows the OTHER language as its
                # label (the one you'd switch TO). It sits outside the mobile viewport, so
                # click it via JS. Only click when it offers the language we want.
                want = s.get("lang", "bg").upper()
                lb = pg.locator("button[title=Language]")
                if lb.count():
                    label = (lb.first.inner_text() or "").strip().upper()
                    if label == want:
                        pg.eval_on_selector("button[title=Language]", "e => e.click()")
                        pg.wait_for_timeout(1500)
            elif d == "dismiss":
                # JS-click any known upsell/modal close control; no-op if none present.
                pg.evaluate("""() => {
                    for (const sel of ['button.upsell-close', '.upsell-later',
                                       'button[aria-label=Close]', '.modal-close']) {
                        const el = document.querySelector(sel); if (el) el.click();
                    }
                }""")
            elif d == "wait_for":
                pg.get_by_text(s["text"], exact=s.get("exact", False)).first.wait_for(
                    state="visible", timeout=s.get("timeout", 60000))
            elif d == "click_text":
                pg.get_by_text(s["text"], exact=s.get("exact", False)).first.click()
            elif d == "click":
                pg.locator(s["selector"]).first.click()
            elif d == "fill":
                pg.locator(s["selector"]).first.click()
                pg.locator(s["selector"]).first.press_sequentially(s["text"], delay=60)  # visible typing
            elif d == "press":
                pg.keyboard.press(s["key"])
            elif d == "upload":
                pg.locator(s.get("selector", "input[type=file]")).first.set_input_files(s["file"])
            elif d == "scroll":
                pg.mouse.wheel(0, s.get("px", 400))
            elif d == "wait":
                pg.wait_for_timeout(s.get("ms", 1500))
            elif d == "screenshot":
                pg.screenshot(path=str(out / f"{s['name']}.png"))
            pg.wait_for_timeout(s.get("pause", 700))  # natural pacing
        vid = pg.video.path()
        ctx.close(); b.close()
    shutil.move(vid, out / "recording.webm")
    shutil.rmtree(out / "raw", ignore_errors=True)
    print(out / "recording.webm")


if __name__ == "__main__":
    for line in Path(__file__).with_name(".env").read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1); os.environ.setdefault(k, v)
    run(json.loads(Path(sys.argv[1]).read_text()), Path(sys.argv[2]))
