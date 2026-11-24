# Post log

## 2026-11-24 (Tue) — EVENING TikTok (educational): "Пърженето утроява калориите на картофа"

**Run:** evening (evening.sh, ~19:59 Sofia / 17:59 UTC). TikTok ONLY (no IG/YouTube/stories/review, §7).
This is today's **2nd** TikTok (max 2/day) — verified exactly 1 existed before this run (morning мюсли app
`cmwud8sah00knoa07c7yynrpx`). Different topic AND format from the morning: morning = app-integrated food
scan ("Скритите калории", мюсли 614); evening = educational cooking-method contrast (no app, no CTA).
Output: out/2026-11-24-evening/.

**Premise step (§10.1):** 10 educational candidates scored; winner **"label serving-size trick" (8.3)**.
BUT Pixabay had NO clean packaged-chips footage (results polluted: camel, forest birds, abstract cards,
Eiffel Tower, + one AI-generated rabbit clip barred by §5). The two clean, subject-correct, in-motion
vertical food clips were **steamy fries** and **popcorn**. Since frame 0 is everything (§10.2/§17),
pivoted to the premise that fits the killer fries footage honestly: **cooking-method contrast — same
potato, boiled vs fried** (~8.0, still fresh + on-brand calorie-awareness). Avoided the dishonest move of
labeling fries as "чипс" (§17 subject-match; §5 honesty).

**Format / beats (no app, no CTA, no QR, no end card — educational §4; §16-tight):** 4 beats, **13.80 s**:
A HOOK 3.2 s (steamy golden fries, push-in zoom) callout "Ако обичаш пържени картофки, гледай това" ->
B 3.3 s baseline CARD (dark gradient) "Същият картоф / ВАРЕН / 87 ккал / на 100 г" + open loop
"А пърженият?" (ding on the 87) -> C 3.3 s fries (zoom) "Същото количество, но пържено..." ->
D 4.0 s PAYOFF: count-up 0->312 on fries + "ПЪРЖЕН · на 100 г" + "Почти 4 пъти повече / Виновно е
олиото" + "Запази си го" (impact when 312 locks), loops back into A. Built via
out/2026-11-24-evening/compose.py (per-segment ffmpeg ultrafast + concat stream-copy; counter = 10 PNG
stamps overlaid in sequence). Visual variety §10.4 = (b) real Pixabay footage + (c) motion graphics
(baseline card + count-up).

**Hook (frame 0, on-screen):** "Ако обичаш пържени картофки, гледай това". **Hook type (§17) = 4
(callout)** — rotates off the morning's type 1.

**Voice:** **NONE** (no-voice: big captions + music + 2 SFX). Alternation: morning had voice (Kalina),
so evening is voiceless -> clean daily voice-vs-no-voice read within TikTok. No AI voice + no AI-generated
realistic content -> **video_made_with_ai=false** (honest).

**Music:** **assets/music/upbeat_3.mp3** (Komiku "Balance", CC0), 0.35 (no voice). Not upbeat_2 (morning).
SFX: ding on the baseline 87, impact on the fried-312 lock (reused synth ding.wav/impact.wav, credits.md).

**Accuracy (§5):** varen potato ~87 ккал/100 г vs deep-fried fries ~312 ккал/100 г (≈3.6×); the gap is
mostly the oil absorbed in frying. Web-checked; recorded both as reference rows in state/numbers.md.
No personal calorie target, no weight-loss promise, no body/food shaming — frames a healthier cooking
choice (bake instead of fry). **Източник in caption:** USDA FoodData Central.

**Quality gate (§10.5 / §16):** dur 13.80 s ✓ (12-20). First-2 s = full-bleed steamy fries in motion +
claim-lead callout, no app/logo/letterbox/black ✓. Contact sheet: motion every beat, NO app (educational),
NO end card/QR, payoff (312) only in the last beat via the counter (87 baseline is setup, not the answer) ✓.
Loop fries->fries seamless. Audio mean -27.6 / max -10.9 dB (no clip). Numbers match numbers.md (87/312),
portion basis "на 100 г" shown. Scores **H8 / C8 / Surprise8 / Pace7.5 / Share8 / Prod8 = avg 7.9,
hook 8 -> PASS** (one pass, no re-render). Weakest = the Варен baseline card (~3.3 s, slightly slow) but it
carries the open loop "А пърженият?" that sets up the payoff. **hunspell: ok** (only Latin/ккал/г flags);
**editor: OK** (§20 independent fresh-context editor returned OK, no changes). **proofread: ok** (пълен
член "пърженият/картофът"; comma before "а"/"което"; "Pulsify" not used — educational).

**Caption (TikTok, educational — no app CTA; §15 cross-promo N/A for educational):**
"Същият картоф, но варен е около 87 ккал на 100 г, а пържен — около 312. Разликата е основно олиото,
което картофът попива при пърженето. Една средна порция пържени картофки (150 г) е към 470 калории. /
Ти как ги правиш — на фурна или в тиган? Пиши отдолу. / Източник: USDA FoodData Central. / #картофи
#пържени #калории #хранене #фитнес" (concrete фурна/тиган comment prompt per insights.md).

**Experiment:** none active (state/experiments.md still absent — research.sh hasn't run).

**Publish:** uploaded final.mp4 -> https://uploads.postiz.com/b55E7jofdy.mp4. **TikTok** post id
**`cmwuzx650099io307d06qnlp1`**, --shortLink false (§18), settings DIRECT_POST + video_made_with_ai=false.
**PUBLISHED 17:59:00Z** -> https://www.tiktok.com/@pulsify8 (releaseId v_pub_url~v2.7711798982841763873,
no error; verified via posts:list foreground poll). Today's TikTok count: **2/2** (morning мюсли app +
this evening fries edu).

**Dish/topic log (30-day no-repeat):** shopska (11-22), баница (11-22 eve), дюнер (11-23), чийзбургер
(11-23), meal-timing myth (11-23 eve), 5 cheap proteins (11-23 IG), мюсли купа 614 (11-24),
сън↔глад (11-24 IG), **варен vs пържен картоф 87/312 (11-24 eve, NEW)**.

---

## 2026-11-24 (Tue) — DAILY RUN (run.sh): morning app TikTok + YouTube Short + IG edu Reel + stories

**Run:** daily (run.sh, ~08:40 Sofia / 06:40–07:45 UTC). Tuesday ⇒ NOT Monday, so no weekly review.
Posts per §3 for Tue: morning app-integrated TikTok + YouTube Short (same file) + IG educational Reel
(different topic) + IG stories. Output: out/2026-11-24/. Evening TikTok is a separate run (evening.sh).

**Pre-flight / fixes this run:**
- Re-read CLAUDE.md from disk (working tree had §20 uncommitted — now in loaded context too).
- Verified yesterday's posts all PUBLISHED incl. the rescheduled YT short (SllyTJwKTsI, 10:00Z).
- **§18 link-shortener catch:** `postiz posts:create --shortLink` DEFAULTS TO true → that's why
  yesterday's YT description became a dub.sh link. Passed **`--shortLink false` on EVERY post today**
  so the full Google Play URL survives.
- **record_app.py login fix:** the first scan "failed" but the screenshot showed a logged-in dashboard
  — a Render cold-start redirect race (2.5 s wait too short). Patched login to poll the URL up to ~30 s
  before declaring failure; re-ran on the warm server → scan succeeded. No AI scan was wasted (first
  attempt died before upload). Used the ONE daily free AI scan on the granola bowl.

### MORNING TikTok (app-integrated) — "Скритите калории": мюсли купа = 614 ккал
- **Premise step (§10.1):** 10 "скритите калории" candidates scored; winner **granola/muesli bowl (8.3)**
  — universally believed "light", ingredients stack, scannable. Killed: цезар салата (salad/shopska used
  <30 d). The twist discovered from the real scan: 614 ≈ дюнер (653), only **39 ккал** apart.
- **Real scan (numbers.md):** "Мюсли с кисело мляко и горски плодове", **614 ккал**, 16.8 P / 110.9 C /
  12.4 F, **420 г**, точност 86%. Per-ingredient: мюсли 120 г = **456 ккал** (380 ккал/100 г — the hidden
  bomb, 74% of total), кисело мляко 150 г = 90, малини 70 г = 36, къпини 50 г = 22, ягоди ≈ 10.
  assets/food/granola.jpg = the scanned photo (Pixabay, user "Pexels").
- **Format / beats (~16.9 s, §16-tight, payoff last, loop):** A HOOK 3.2 s (real yogurt-bowl b-roll in
  motion, push-in) "Мислиш, че мюслито е лека закуска?" → B 3.5 s the REAL scanned muesli photo + stamped
  "456 ккал" + "120 г · 380 ккал на 100 г" (ding) → **APP 3.2 s** real Pulsify result card (614 / точност
  86%) — app once, ~1/3 in (6.7 s) → C 3.7 s closer muesli + stamped "614 ккал · 420 г" (ding) → **D 3.3 s
  twist** "Почти колкото цял ДЮНЕР / Купа мюсли 614 vs Дюнер 653 / Разликата е само 39 ккал" + small CTA
  overlay, loops to A. Built via out/2026-11-24/compose_morning.py (per-segment ffmpeg + concat stream-copy;
  added a push-in zoom to seg_clip). final.mp4 = **16.90 s**, 1080x1920.
- **QG fix (1 re-render):** first build used a honey/ICE-CREAM clip for the "само мюслито" beat (misleading)
  and a near-static hook. Rebuilt: real scanned-muesli photo for the muesli beats (honest, subject-correct)
  + push-in zoom on the hook for motion.
- **Hook (frame 0):** "Мислиш, че мюслито е лека закуска?" — our proven belief-challenge shape
  (= "мислиш шопската е лека?", day-1 winner). **Hook type (§17) = 1 (belief-challenge).** Chose our
  strongest data pattern for the money post over strict rotation; the IG reel tests a different type.
- **Voice:** **bg-BG-KalinaNeural** (rotation: 11-23 morning = Borislav, evening = no-voice → today Kalina).
  TTS phonetic "Пулсифай", numbers as Bulgarian words, rate +10%. **video_made_with_ai=true** (AI voice).
- **Music:** assets/music/upbeat_2.mp3 (Komiku "Tension", CC0), 0.12 under voice. Not upbeat_1 (11-23 AM).
  SFX: ding on the 456 & 614 stamps, impact on the дюнер twist (reused out/…-evening/sfx/*.wav, synth).
- **Quality gate (§10.5/§16):** dur 16.9 s ✓ (12-20). First-2 s = appetizing bowl in motion + claim-lead
  text, no app/logo/letterbox/black ✓. Contact sheet: motion every beat, app once & after 3 s, NO end
  card/QR (§16), payoff in the last beat ✓. Audio mean -24 dB / max -5 dB (voice+music+SFX present).
  Scores **H8 / C8 / Surprise8 / Pace7.5 / Share7.5 / Prod8 = avg 7.8, hook 8 → PASS.**
  **proofread: ok**; **hunspell: ok** (only Latin/loanword flags); **editor: OK** (§20 — one fix applied:
  "грелина (хормонът→хормона на глада)" in the IG caption; re-ran → OK).
- **Caption (TikTok, §11.3 standard CTA; §15 cross-promo NOT used this post — kept the money post direct,
  will rotate cross-promo onto a later app TikTok):** "Купа мюсли с кисело мляко и горски плодове — звучи
  леко, нали? Сканирах я и излезе 614 ккал, почти колкото цял дюнер. Най-много дава самото мюсли — 456 ккал
  за 120 г. / Колко мислеше, че е? Пиши число отдолу 👇 / Потърси Pulsify в Google Play 🔍 / Източник:
  реален скан с Pulsify. / #мюсли #закуска #калории #хранене #фитнес" (concrete number-guess comment bait,
  per insights.md).
- **Publish:** uploaded → uploads.postiz.com/BFERwV50iG.mp4. **TikTok** post id **`cmwud8sah00knoa07c7yynrpx`**
  (DIRECT_POST, --shortLink false, made_with_ai=true). **PUBLISHED** → https://www.tiktok.com/@pulsify8
  (verified posts:list, state PUBLISHED, no error). Today's TikTok count: **1/2** (evening.sh will add #2).

### YouTube Short — same BG file (NOT a separate EN version, per §2/§3)
- Title "614 калории в една купа мюсли? Скритите калории в закуската". Description: 2-3 sentences + **FULL**
  Play link (https://play.google.com/store/apps/details?id=com.apex.fitness, --shortLink false) + Pixabay/
  Komiku credits + Източник. made_with_ai=true. **Scheduled 2026-11-24T10:00:00Z** (past the ~08:00 UTC
  new-channel quota reset, like yesterday) — id **`cmwud9kxg00ies2072iktupye`**. VERIFY after 10:00 UTC.

### INSTAGRAM educational Reel — "Недоспиването те прави по-гладен" (sleep & hunger)
- **Different topic** from the TikTok (§3) + **healthy-habits variety** (§3 "1 in 3", none recently; never
  two in a row — OK). Educational, **no app, no CTA**, ends on "Запази си го". ~22 s, out/2026-11-24/
  compose_ig.py. **NO voice** (captions + chill music + 2 SFX) → gives the Monday review a voice-vs-no-voice
  read against the morning TikTok (voice). **made_with_ai=false** (no AI voice/content).
- Beats: A HOOK (woman on phone in bed at night — the cause) "Недоспиването те прави по-гладен" → B (face)
  "По-малко сън, повече грелин" / "Грелинът е хормонът на глада" → C stat card "+250 ккал на ден при
  недоспиване / най-вече сладко и мазно" (ding) → D (morning tray) "И посягаш към сладко и мазно" →
  E "Първо оправи съня, после диетата / Запази си го", loops.
- **Hook type (§17) = 2 (mistake/correction)** — rotates off the TikTok's type 1.
- **Accuracy (§5):** недоспиване → ↑грелин (15-28%) и средно до +250 ккал/ден приет прием; web-checked.
  **Източник on-screen + caption: Nature Reviews Endocrinology, 2022** (s41574-022-00747-7). No medical
  advice, no body-shape framing, no personal targets. Stock people = atmosphere only, not testimonials (§5).
- **QG:** dur 22 s ✓ (15-40). Frame-0 real person in motion, no bands ✓. H8/C8/Surprise7/Pace7.5/Share7.5/
  Prod7.5 = avg 7.6, hook 8 → PASS. editor: OK.
- **Caption:** "Ако си гладен постоянно, виж колко спиш. При недоспиване тялото вдига грелина (хормона на
  глада) и хората ядат средно до 250 калории повече на ден, най-вече сладко и мазно. Понякога решението не
  е нова диета, а повече сън. / Запази си го и го прати на вечно гладен приятел 👇 / Източник: Nature
  Reviews Endocrinology, 2022. / #сън #глад #хранене #навици #фитнес"
- **Publish:** uploads.postiz.com/Wblxg6pYnx.mp4 → **IG Reel** post id **`cmwudfko200l1s207dqcpeq7w`**
  (post_type=post, made_with_ai=false), sched 07:34Z. VERIFY.

### INSTAGRAM stories (3 frames) — myth → fact → CTA (rotates off 11-22/11-23 guess/this-or-that)
- out/2026-11-24/stories.py, 1080x1920, text inside y 260–1660. Real granola photo + real app card.
  Removed 👉/👆 emojis (render as tofu in DejaVu). editor: OK on the new lines.
- 1 (myth) granola + "МИТ или ФАКТ: Мюслито винаги ли е лека закуска? / Истината в следващата стори" —
  id `cmwudizyl00n4s207g7zoxe00`, sched 07:42Z.
- 2 (fact) real app card + "ФАКТ: 614 ккал в една купа / Почти колкото цял дюнер" — id
  `cmwudj0ie00p4oa07yvjil712`, 07:43Z.
- 3 (CTA) "Снимай чинията с Pulsify / Линк в профила" — id `cmwudj10y00p5oa07u5m4zqlk`, 07:44Z.
- Say "стори" (§9) ✓. Rotation next time: behind-the-scenes or a quick tip.

**Dish/topic log (30-day no-repeat):** shopska (11-22), баница (11-22 eve), дюнер (11-23), чийзбургер
(11-23), meal-timing myth (11-23 eve), 5 cheap proteins (11-23 IG), **мюсли купа 614 (11-24, NEW)**,
**сън↔глад (11-24 IG, NEW)**. Hooks logged in hooks.md. Credits in credits.md.

---

## 2026-11-23 (Mon) — EVENING TikTok (educational): "Мит или факт — вечерята не те качва"

**Run:** evening (evening.sh, ~21:00 Sofia). TikTok ONLY (no IG/YouTube/stories/review). This is today's
**2nd** TikTok (max 2/day) — morning was the app-integrated döner vs cheeseburger face-off. Different
topic (meal-timing myth, no food calorie number) AND different format (educational "Мит или факт" vs
the morning app two-food face-off). Output: out/2026-11-23-evening/.

**Context / recovery:** an earlier evening attempt (~17:4x) had fetched Pixabay b-roll + SFX and a
half-written compose but never rendered/published (the §18 background-wait trap from the file header; it
was also a 31.5 s cut that broke §16). This run REUSED the fetched assets but **rebuilt** the compose to
§16: a tight **16.0 s** cut with the payoff stamped at the very end and a seamless loop. Nothing double-
posted (verified only 1 TikTok existed today before this run).

**Premise step (§10.1):** 10 educational-myth candidates scored; winner "Не, вечерята не те качва"
(late-eating / „не яж след 18:00" myth), ~8.3 — highly relatable to the common Bulgarian 18:00 rule,
claim-lead/belief-challenge (our day-1 winning pattern), creates a gap. Beats #3,#8 (soft/hedged
variants) killed per the 10.1 kill list.

**Format / beats (no app, no CTA, no QR, no end card — educational §4):**
A HOOK 3.0 s (fork into a salmon salad, close-up in motion) + "Не, вечерята не те качва" ->
B 3.0 s (slicing mushroom) "„Не яж след 18:00" е мит" + series tag "Мит или факт" (appears only AFTER
3 s, §17) + impact SFX -> C 3.3 s (person on a sofa in the evening) open loop "Тогава какво те качва?"
-> D 3.2 s (food prep) "Вечер дояждаш, без да усетиш" -> E 3.5 s ФАКТ card (ding SFX) "Важно е общото
за деня, не часът" + "Запази си го", looping back into A. Built via out/2026-11-23-evening/
compose_evening.py (one ffmpeg pass per segment + concat stream-copy — the only way it finishes on the
2-core/<1 GB VM; the old multi-pass version timed out). final.mp4 = **16.0 s**, 1080x1920.

**Hook (frame 0, on-screen):** "Не, вечерята не те качва". Hook type (§17) = **1 (contrast/surprise,
belief-challenge)** — rotates off the morning's type 3 (challenge/guess).

**Voice:** **NONE** (no-voice: big captions + music + 2 SFX). Alternation: morning had voice (Borislav),
so evening is voiceless — gives the Monday review a voice-vs-no-voice read within TikTok. Because there
is no AI voice and no AI-generated realistic content, set **video_made_with_ai=false** (honest; the morning
app videos were true because of the AI voiceover).

**Music:** **assets/music/chill_3.mp3** (CalmPills "Absolvo", CC0), 0.35 (no voice). Not upbeat_1
(morning). SFX: impact on "е мит", ding on the ФАКТ reveal (short synthesized tones, see credits.md).

**Pixabay b-roll (credits.md):** 227128 kurt_BID (salad hook), 141853 Amina_Salim (mushroom),
43459 Nicolas_Garay (sofa, atmosphere only — NOT a testimonial), 254753 xBriantcx (dough). The rest of
the fetch was mislabeled junk (camel, moonlit sea, NO-SIGNAL card, street, yoga) — vetted out.

**Accuracy (§5):** claim = meal *timing/clock* itself is not what makes you gain; total daily intake is,
and late eating usually adds extra snacks on top. Checked via web search against controlled-trial
evidence (matched-calorie RCTs show little timing effect; late-eating→weight-gain link is driven by
higher total intake). No personal calorie target, no weight-loss promise, no body shaming. **Източник in
caption:** научен преглед за времето на хранене (PMC 9010393, 2022), https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9010393/

**Quality gate (§10.5 / §16):** dur 16.0 s ✓ (12-20 s). First-2 s = appetizing salmon-salad close-up in
motion + claim-lead text, no app/logo/letterbox/black ✓. Contact sheet: motion every ~1.5 s, no app
(educational), no end card/QR, ФАКТ reveal only in the last beat ✓. One fix: the 🔖 emoji rendered as a
tofu box (DejaVu lacks it) -> removed, re-rendered. Scores **H8 / C8 / Surprise7 / Pace7 / Share7 /
Prod8 = avg 7.5, hook 8 -> PASS.** Weakest = the sofa beat (slightly overexposed/slow) but it carries the
open-loop question. **proofread: ok** (capitals; „…" curly quotes; comma before "а"/"без"; "Pulsify" not
used on-screen since educational).

**Caption (TikTok, educational — no app CTA, §11.3 / §15 N/A for educational):**
"Мит или факт: „Не яж след 18:00". / Часът сам по себе си не те качва. Значение има колко изяждаш за
целия ден, а вечер лесно дояждаш, без да усетиш. / Ти спазваш ли правилото за 18:00? Пиши „да" или „не" 👇
/ Източник: научен преглед за времето на хранене (PMC, 2022). / #хранене #калории #митилифакт #вечеря
#фитнес". (Concrete да/не comment prompt, per the insights.md note to make comment-bait specific.)

**Experiment:** none active (state/experiments.md still absent — research.sh hasn't run).

**Publish:** uploaded final.mp4 -> https://uploads.postiz.com/ey11JfkOvM.mp4. **TikTok** post id
**`cmwtn2rw005qgmf08wpgdskxa`**, --shortLink false (§18). **PUBLISHED 19:12:09Z** ->
https://www.tiktok.com/@pulsify8 (releaseId v_pub_url~v2.7711446660664051745, no error). Verified via
posts:list. Today's TikTok count: **2/2** (morning döner app + this evening myth).

**Dish/topic log (30-day no-repeat):** meal-timing / „не яж след 18:00" myth (NEW, 2026-11-23 eve). No
dish calorie number used (myth-bust, not a dish video).

---

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
