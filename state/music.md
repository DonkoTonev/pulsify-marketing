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
  Next video: avoid upbeat_1 back-to-back; for a calm/food topic use a chill_* track.
