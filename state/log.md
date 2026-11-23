# Post log

## 2026-11-23 (Mon) — MONDAY REVIEW + DAILY RUN

### Monday weekly review (section 12) — FIRST review
- Pulled `postiz analytics:platform` (3 channels) + `analytics:post` (4 posts). All 6 Nov-22 posts
  are PUBLISHED, no errors (YouTube EN short + 2 stories confirmed live).
- Day-1 numbers (posts ~1 day old): TikTok 763 views total (shopska morning app 588 / banitsa
  evening 175), 7 likes, 0 comments/shares. IG reel 19 views / 17 reach / 0 saves. YT-EN 41 views.
- Conclusions written to state/insights.md; algorithm.md "Our data" updated; hooks.md seeded.
  Key reads (all weak — 1 day): TikTok is the only real reach; claim-lead hook (shopska 588) beat the
  soft "Колко калории има в..." opener (banitsa 175, matches the 10.1 kill list); 0 comments/shares
  everywhere. **API limitation:** postiz exposes only views/likes/comments/shares (+reach/saves IG),
  NO retention/watch-time/completion. No experiments were active -> nothing to fold/drop.
- Housekeeping found two missing state files and created them: **state/numbers.md** (backfilled
  shopska + banitsa from the logs) and later added döner + cheeseburger; experiments.md still absent
  (research.sh hasn't run — the Nov-22 "first run" was actually a Sunday setup run; the log mislabeled
  Nov-22 as "Sat" — Nov 22 2026 was a SUNDAY, Nov 23 is Monday).

### Daily run — Monday = app-integrated morning TikTok + YouTube Short + IG carousel + stories

**MORNING TikTok (app-integrated) — "Кое има повече калории?": Дюнер vs Чийзбургер**
- Premise step: 10 two-food face-offs scored; winner "Дюнер vs Чийзбургер" (8.3). Twist discovered
  from the real scan.
- Real data: **Дюнер = 653 ккал, 44.3 P / 52.7 C / 27.0 F, 340 г** (REAL Pulsify scan, test acct,
  accuracy 86%, tortilla+beef+salad). **Голям чийзбургер ≈ 535 ккал / ~200 г** (reliable source,
  USDA "single large patty with condiments" — the daily free AI-scan limit was hit after the döner,
  so the burger used a cited reference, flagged on-screen + in caption). Both in state/numbers.md.
- Format: hero split (döner/burger + VS) -> real Pulsify döner result (653) shown once at ~7 s
  (after 3 s ✓, ~1/3 in) -> burger counter 0→535 -> comparison card "Дюнерът НЕ е по-леката опция"
  (653 vs 535, sources shown) -> QR end card. Built via out/2026-11-23/compose.py (segments + lay
  continuous music over the whole thing). final.mp4 = **26.3 s**, 1080x1920.
- Hook (frame 0, on-screen + voice): "Дюнер или чийзбургер?" / "Кое е по-калорично?"
- Voice: **bg-BG-BorislavNeural** (alternation: Nov-22 eve = Kalina -> today Borislav; next BG -> Kalina).
  "Пулсифай"/"Гугъл Плей" + numbers written as Bulgarian words for TTS. Marked AI audio.
- Music: **assets/music/upbeat_1.mp3** (Komiku "Battle Theme", CC0), 0.12 under voice, continuous
  (not per-segment). Not upbeat_3 (last used). Thematic "battle" for a face-off.
- Photos: Pixabay doner (angelorosa) + cheeseburger (RitaE, cropped) — credits in state/credits.md.
- Quality gate: first-2s = two appetizing foods + VS + hook, no app/logo/black ✓. Contact sheet: app
  once (~7 s), QR end card present, numbers match numbers.md. Scores H8/C9/Surprise7/Pace7/Share8/
  Prod8 = avg 7.8, hook 8 -> PASS. Weakest = pace (7 s intro a touch long; next time animate the
  countdown / shorten). **proofread: ok** (comma before "че"/"а"; "Pulsify" Latin on-screen+caption).
- Caption (TikTok): "Мислиш, че дюнерът е по-леката опция от чийзбургер? Един дюнер е 653 ккал, а
  голям чийзбургер — 535. Ти кое избра? 😅 / Дюнерът е реален скан, бургерът е по USDA. / Потърси
  Pulsify в Google Play 🔍 / #дюнер #чийзбургер #калории #хранене #фитнес"
- Источник: USDA FoodData Central (cheeseburger). Döner number = real scan.
- **TikTok** post id `cmwsy17hz051vqs07sqtqzt7q` (DIRECT_POST, video_made_with_ai=true), sched 07:29:40Z.

**YouTube Short — same BG video file (NOT a separate EN version).**
- CLAUDE.md §2/§3 say YouTube is Bulgarian + uses the morning TikTok file. (settings-youtube.json's
  "English only" note is stale from the Nov-22 run; CLAUDE.md overrides — did NOT make an EN version.)
- Title: "Дюнер или чийзбургер — кое има повече калории?" Description has the full Play link + Pixabay/
  Komiku credits. made_with_ai=true. **YouTube** first attempt `cmwsy1gx00528qs07urcc6csl` **FAILED:
  "daily upload quota is exhausted for today"** (new channel, low daily cap). Deleted it and
  **rescheduled** the same BG short for **2026-11-23T10:00:00Z**, new id `cmwsy6xho04w6kc07gmqd6k8c`
  (past the ~08:00 UTC quota reset). Logged in state/errors.md; verify after 10:00 UTC.

**INSTAGRAM carousel (educational, Monday) — "5 евтини източника на протеин"**
- Different topic from the TikTok. 7 slides 1080x1350 (out/2026-11-23/carousel.py). No app, no app CTA.
- Protein numbers verified via web search: яйца 6–7 g/egg, извара ~17 g/100g, пилешко ~30 g/100g,
  леща/боб ~9 g/100g, риба тон ~25 g/100g. **Източник: USDA FoodData Central, forlife.bg** (in caption
  + last slide). Last slide "Запази си го" + "Кое слагаш в количката?".
- Caption ends on save (no app CTA). **IG carousel** post id `cmwsy1ps604kpmf07dt1oc2xb`, sched 07:30:04Z.

**INSTAGRAM stories (3 frames) — teaser -> reveal -> CTA** (out/2026-11-23/stories.py, 1080x1920)
- 1 (teaser) "Дюнер или чийзбургер?" split image — id `cmwsy1yxu04sfkc07lf0rhz2a`.
- 2 (reveal) real app screen + "Дюнер 653 / Чийзбургер 535 (USDA) / Дюнерът води" — id `cmwsy1zih04sgkc07uzb4e5sn`.
- 3 (CTA) "Снимай чинията с Pulsify / Линк в профила" — id `cmwsy203l04sikc074fulseoz`.
- Staggered 07:30/07:31/07:32Z to keep order. Rotation: next time try myth/fact or behind-the-scenes.

### Publish verification (07:33Z)
- **TikTok** PUBLISHED -> https://www.tiktok.com/@pulsify8
- **IG carousel** PUBLISHED -> https://www.instagram.com/p/DgE2PYLnEtn/
- **IG story 1/2/3** PUBLISHED (stories/pulsifyfit/...9080, ...3153, ...0837)
- **YouTube** FAILED (quota) -> rescheduled 10:00 UTC, QUEUE (`cmwsy6xho04w6kc07gmqd6k8c`). Verify later.

**Dish log (30-day no-repeat):** shopska (11-22), баница (11-22 eve), **дюнер (11-23)**, чийзбургер (11-23).
**Tooling this run:** make_video.py render_end_card now draws a **QR code** (python qrcode) + "Задръж Home
и огради кода" — closes the missing-QR gap (was logo+text only). qrcode installed. out/2026-11-23/ has
compose.py, carousel.py, stories.py (reusable patterns). Pixabay API works with a User-Agent header and
WITHOUT the `category` param (that combo 403s). Daily free AI-scan limit on the test account ≈ enough for
~1 scan/run — plan one real scan per day; use cited sources for extras.

---

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

## 2026-11-22 (Sat) — EVENING TikTok: "познай калориите" баница (video)

**Run:** evening (evening.sh, ~20:30 Sofia). TikTok ONLY. This is today's 2nd TikTok post (max 2/day) —
morning was the shopska APP VIDEO. Different dish (banitsa) + different format (guess-the-calories vs
morning's confession/POV). No Instagram/YouTube/Stories/review this run. Output: out/2026-11-22-evening/.

**Format:** guess-the-calories video, 4 beats via out/2026-11-22-evening/compose.py →
(A) real banitsa photo + hook, (B) dark bg + **counting-up calorie counter 0→2660** (motion graphic),
(C) **real app recording** proof (Pulsify result screen), (D) 4 s download end card. Video variety ✓
(combines (a) app recording + (c) motion graphics). final.mp4 = **22.1 s**, 1080x1920.

- Hook (on-screen + voice @0.3 s): "Колко калории има тази баница?"
- Real data (from the app, real AI call on test account, banitsa.jpg): **2660 ккал**, 80 P / 300 C /
  120 F, 950 g, 280 ккал/100 г. App titled it "печена пита със сирене и билки" (= cheese banitsa).
  Framed honestly as a WHOLE homemade banitsa (цяла тава, 950 г), not a single piece.
- On-screen captions: "Колко калории има тази баница?" / "Отговорът:" + counter "2660 ккал" /
  "цяла тава · 950 г" / "Разпознато от Pulsify за секунди" / end card "Pulsify · Свали безплатно от
  Google Play".
- Voice: **bg-BG-KalinaNeural** (alternation: morning=Borislav → tonight Kalina; next BG video →
  Borislav). "Пулсифай"/"Гугъл Плей" written in Cyrillic for TTS (CLAUDE.md line 134 = "Пулсифай" with
  у, NOT "Пълсифай" — fixed the memory note that had it wrong). Marked AI audio (video_made_with_ai=true).
- Music: **assets/music/upbeat_3.mp3** (Komiku "Balance", CC0), 0.12 under voice. Not chill_1/chill_2
  (morning). Mood: playful/light for a guess game.
- Caption: "Цяла домашна баница излезе 2660 калории 🤯 И това е за цялата тава, не за едно парче.
  Познахте ли колко е? / Потърси Pulsify в Google Play 🔍 / #баница #калории #хранене #фитнес
  #българскахрана"
- **proofread: ok** (capitals, commas before "не"; "Пулсифай" in all TTS; "Pulsify" kept Latin on-screen
  + caption). One stylistic lowercase label kept ("цяла тава · 950 г" — a fragment, not a sentence).
- Algorithm checklist: hook <2 s ✓; keyword "калории/баница" spoken + on-screen + in caption ✓;
  comment trigger = question "Познахте ли колко е?" ✓; surprising-number share trigger ✓.
- **TikTok** post id `cmws6cuhm0rk3qq07s5sxjux3` → **PUBLISHED** https://www.tiktok.com/@pulsify8
  (DIRECT_POST, video_made_with_ai=true, state=PUBLISHED, no error). Verified via posts:list 18:35Z.
- Experiment: none active (state/experiments.md still does not exist; research runs Sundays).
- Dish log (30-day no-repeat): shopska (2026-11-22 morning), **баница (2026-11-22 evening)**.

**Tooling added this run (reusable):** make_video.py now has an `end_card` step (logo + download CTA,
appended via concat_segments, with its own TTS) and a `counter` motion-graphic step (counting-up number);
captions accept an optional `y`. App-logo asset cropped to assets/brand/pulsify_logo.png (from the
AI-meal screen). This closes the morning run's "end-card step needs building" TODO.
