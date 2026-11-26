# Music library (assets/music/) — royalty-free, for background beds in videos

**Sourcing note (2026-11-22):** Pixabay Music (the source named in CLAUDE.md) is bot-blocked
in this environment — its HTML 403s to curl and serves a stripped page to headless Chromium, so
no CDN audio URLs can be extracted. Internet Archive *general* CC0 search is polluted with
mislabeled copyrighted/chart uploads (Ed Sheeran, XXXTENTACION, Pink Floyd…), which would break
the "never use commercial/chart songs" rule — so those were NOT used. Instead every track below is
from a **named, verified-legitimate CC0 artist/project**. All tracks are **CC0 1.0 (public domain,
no attribution required)**, trimmed to 60 s loops and loudness-normalized. make_video.py loops the
bed with -stream_loop -1 and cuts to video length, so 60 s is enough.

Rotation rule (CLAUDE.md): never the same track twice in a row; match mood to the video
(workout → gym/upbeat, recipe/food → chill, build-in-public/motivational → motivational).

## chill / lofi / ambient
Source: "Calm Pills — Relaxing Ambient Music" by **Alaeddin Hallak**, CC0 1.0.
https://archive.org/details/CalmPills
- chill_1.mp3  — Calm Pill 12 "It Was Beautiful"
- chill_2.mp3  — Calm Pill 10 "Tone Poetry"
- chill_3.mp3  — Calm Pill 14 "Absolvo"
- chill_4.mp3  — Calm Pill 11 "The Healing Lake"
- chill_6.mp3  — Calm Pill 13 "Introverted Chords"
- chill_7.mp3  — Calm Pill 15 "Painting Twilight"
- chill_8.mp3  — Calm Pill 10 "Tone Poetry" (different section)

## upbeat / gym / motivational
Source: **Komiku**, "It's Time For Adventure! Vol 2", CC0 1.0.
https://archive.org/details/Komiku-ItsTimeForAdventureVol2
- chill_5.mp3        — 07 "Frozen Jungle" (atmospheric, use as chill)
- upbeat_1.mp3       — 03 "Battle Theme"
- upbeat_2.mp3       — 12 "Tension"
- upbeat_3.mp3       — 01 "Balance"
- gym_1.mp3          — 13 "Fight run breath deeply"
- gym_2.mp3          — 09 "This one is tough"
- motivational_1.mp3 — 15 "Victory"
- motivational_2.mp3 — 10 "Something to save"

## Last used (keep updated to enforce no-repeat)
- 2026-11-22: chill_1 (BG shopska video), chill_2 (EN shopska video),
  upbeat_3 (evening banitsa guess-the-calories video).
- 2026-11-23: **upbeat_1 (Komiku "Battle Theme") — morning döner vs cheeseburger face-off.**
- 2026-11-23 evening: **chill_3 (CalmPills "Absolvo") — "Мит или факт: вечерята не те качва" (no-voice, 0.35).**
- 2026-11-24: **upbeat_2 (Komiku "Tension") — morning мюсли app TikTok; chill_5 (CalmPills "Frozen Jungle") — IG sleep reel.**
- 2026-11-24 evening: **upbeat_3 (Komiku "Balance") — "Пърженето утроява калориите" fries edu TikTok (no-voice, 0.35).**
  Next video: avoid upbeat_3 back-to-back; morning used upbeat_2, so pick a different track either way.
- 2026-11-25: **upbeat_1 (Komiku "Battle Theme") — morning app TikTok "Калорийна битка" (voice Borislav, 0.12).**
  Thematic "battle" track; not used since 11-23 (not back-to-back). Next video: avoid upbeat_1 back-to-back.
  (IG carousel/stories are silent images — no music track.)
- 2026-11-25 evening: **chill_6 (CalmPills "Introverted Chords") — "Фрапето крие повече" течни-калории edu TikTok (no-voice, 0.35).**
  Fresh track (never used before); calm café mood. Not upbeat_1 (morning) / upbeat_3 (11-24 eve). SFX: ding (ingredients) + impact (170 lock). Next video: avoid chill_6 back-to-back. (NOTE: this evening post FAILED to publish — run failed — but the track still counts as used.)
- 2026-11-26: **upbeat_2 (Komiku "Tension") — morning app TikTok "Как изглеждат 500 калории" (no-voice, 0.33).**
  Not chill_6 (11-25 eve) / upbeat_1 (11-25 morn) — no back-to-back. SFX: ding (850 reveal) + impact (93 reveal).
  **chill_4 (CalmPills "The Healing Lake") — IG reel "Мит или факт: вода" (voice Kalina, 0.12).** FRESH track
  (never used before), calm water mood. Next video: avoid upbeat_2 / chill_4 back-to-back.
