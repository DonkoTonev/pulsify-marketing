# Post log

## 2026-11-22 (Sat) — APP VIDEO: photo-a-meal, shopska salata

First real run. Set up integrations (state/integrations.json), per-platform settings
(state/settings-*.json), a 15-track CC0 music library (state/music.md) and a real food photo
(assets/food/shopska.jpg, CC BY-SA, see state/credits.md). Explored the app and mapped the
AI-meal flow + language switch (state/app-map.md).

**Format:** APP VIDEO (real footage) — AI Meal Analysis. Uploaded a real shopska-salad photo,
app recognized it and returned calories + macros + per-ingredient breakdown. Rotation: first video,
nothing before it.

**Experiment:** none (state/experiments.md does not exist yet; weekly research runs Sundays).

### Bulgarian video → TikTok + Instagram Reels
- Hook (slide 1 / caption 1): "мислиш шопската е лека?"
- On-screen captions: "мислиш шопската е лека?" / "663 ккал · 44 г мазнини" / "салата ≠ ниски калории"
- Voice: **bg-BG-BorislavNeural** (first in the alternation; next BG video → Kalina). Marked AI audio.
- Music: **assets/music/chill_1.mp3** (CalmPills "It Was Beautiful", CC0), 0.12 under voice.
- Real data shown: 663 kcal, 34.4 P / 37.8 C / 43.7 F, 905 g portion, accuracy 83%.
- Caption (both): "не очаквах шопската да излезе 663 калории честно 😅 / снимаш чинията и Pulsify ти
  смята калории и макроси за секунди / #шопскасалата #калории #хранене #фитнес #gym"
- Video: out/2026-11-22/final.mp4 (16 s, 1080x1920).
- **TikTok** post id `cmwrqvmge0hqwtd07vazy4h7a` → PUBLISHED https://www.tiktok.com/@pulsify8
  (DIRECT_POST, video_made_with_ai=true).
- **Instagram** Reel post id `cmwrqvtyc0hr7td07jycsbe88` → PUBLISHED
  https://www.instagram.com/reel/DgCsUb6ClHc/ (post_type=post, made_with_ai=true).

### English version → YouTube Shorts
- Separate recording in English UI (same photo). Real data this run: 489 kcal, 42.0 P / 19.8 C /
  28.0 F, 525 g (AI estimated a smaller portion than the BG run — real per-run variation).
- On-screen captions: "is a salad always light?" / "489 cal · 28g fat" / "snap it. macros in seconds."
- Voice: **none** (music-only, to keep the "~half of videos use voice" balance — BG had voice).
- Music: **assets/music/chill_2.mp3** (CalmPills "Tone Poetry", CC0), 0.35 (no voice).
- Title: "This salad is not as light as it looks | AI calorie scanner #Shorts". made_with_ai=false
  (real screen recording, no AI-generated/altered realistic content).
- Video: out/2026-11-22/en/final_en.mp4 (16 s, 1080x1920).
- **YouTube** post id `cmwrrva2i0imjqq07ss512er7` → scheduled 11:51 UTC (verify publish).

### Instagram Stories (Bulgarian) — quiz + answer (reposted compliant, see note below)
- Story 1 (quiz): "Колко калории има в една шопска салата? Отговорът е в следващата история"
  post id `cmwrs4yis0iaktd0787auad9m` → scheduled 11:57 UTC.
- Story 2 (answer): "663 ккал / 44 г мазнини (основно от сиренето) / Снимай чинията с Pulsify /
  Линк в профила" — post id `cmwrs4z380ialtd07bo6f9iwc` → scheduled 12:00 UTC.
- (First drafts `cmwrrvuve...` / `cmwrrvve...` were deleted before publishing and replaced with these.)
- Rotation next time: try the "нов пост 👀" teaser variant instead of quiz+answer.

### ⚠️ Quality-rules compliance (IMPORTANT — read before next run)
Mid-run I found that CLAUDE.md on disk has an uncommitted **"Quality rules (added 2026-11-22)"**
section that was NOT in my loaded context (the reminder copy ended at "Monday review"). So the three
feed/video posts went out BEFORE I applied those rules. proofread: the stories above were proofread
and reposted compliant; the live feed posts were not re-done.
- The 3 LIVE posts (TikTok, IG Reel, YouTube) were **kept as-is** (not deleted) — deleting live,
  outward-facing content without confirmation isn't warranted for quality fixes; content is otherwise
  real/correct. AskUserQuestion was attempted but this run is autonomous (no reviewer).
- What they miss vs the quality rules: BG video voiceover says "Pulsify" (should be "Пълсифай" for
  bg TTS); captions lack the per-platform download CTA and the capital/comma punctuation; no 2–3 s
  end card on any video (YouTube EN is otherwise compliant — music-only + Play link in description).
- **Next run MUST:** (1) Read CLAUDE.md from disk first (don't trust the loaded copy); (2) Cyrillic
  "Пълсифай" in every bg voiceover; (3) per-platform CTA in captions; (4) build a reusable 2–3 s
  end-card step for make_video.py (needs an app-logo asset) and append it to every video; (5) proofread
  pass on all text. Saved to agent memory (claudemd-quality-rules).

### Tooling notes / fixes this run
- make_video.py had an audio bug (mangled amix labels via `split("]")[-2]`) — fixed to
  `rsplit("[",1)`. Also: music volume now 0.12 under voice / 0.35 music-only; output duration
  hard-capped with `-t` (probed from base) because `-shortest` is unreliable with infinite
  looped music + filtergraphs.
- record_app.py: added `ensure_lang`, `dismiss`, `wait_for` steps (see state/app-map.md).
- Recording caveat: Playwright records video at CSS res (390 wide) in a 780-wide canvas → gray
  padding; crop to 390x844 top-left, upscale+sharpen (rec_crop.mp4) before make_video.
