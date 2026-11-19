# Pulsify Marketing Agent

An autonomous social-media marketing agent for [Pulsify](https://play.google.com/store/apps/details?id=com.apex.fitness),
an AI calorie & fitness tracker I build solo. Every day it plans, produces and publishes a post to TikTok, Instagram and
YouTube, with no human in the loop. Once a week it reviews the analytics and adjusts its own strategy.

It runs on a free Oracle Cloud VM (1 vCPU, 1 GB RAM) and is driven by a cron job.

## How it works

```
cron (daily)
  └─ run.sh
       └─ Claude Code (headless, guided by CLAUDE.md)
            ├─ reads state/log.md + state/insights.md   ← what was posted, what worked
            ├─ picks a format (slideshow · app video · macro card · stories)
            ├─ produces media
            │    ├─ make_slides.py   → 1080x1920 slides (Pillow) with real app screenshots
            │    ├─ record_app.py    → records the real web app in a phone-sized headless Chrome (Playwright)
            │    └─ make_video.py    → ffmpeg edit: trim, captions, Edge-TTS voiceover, music
            ├─ reviews its own output (reads the rendered frames, re-renders if broken)
            ├─ publishes via the Postiz CLI → TikTok, Instagram (+ Stories), YouTube Shorts
            └─ appends to state/log.md
  └─ git commit + push (this repo is the agent's memory + audit trail)

weekly: pulls analytics → rewrites state/insights.md → shifts the content mix
```

## Design decisions

- **Real footage, not synthetic people.** Videos are recordings of the actual app driven by Playwright, so content is
  authentic and doesn't need "AI-generated person" labels. No fake reviews, testimonials or results.
- **Rules as a prompt file.** `CLAUDE.md` holds the brand voice, content mix, platform rules and hard limits
  (no medical claims, max 1 post/channel/day, language per platform). Changing strategy = editing a markdown file.
- **Self-correcting.** When a selector breaks, the agent screenshots the page, fixes `record_app.py`, and records the
  fix in `state/app-map.md` (it did exactly this on day one when the login form changed).
- **Language split.** TikTok/Instagram in Bulgarian (local niche, Bulgarian food database is the edge),
  YouTube in English. Bulgarian voiceovers alternate between two voices.
- **Cheap by design.** Free VM, free TTS, free royalty-free music, Claude subscription instead of per-token API billing.
- **Secrets never hit git.** `.env` is ignored and every automated commit is scanned with gitleaks before push.

## Stack

Claude Code · Python (Playwright, Pillow, edge-tts) · ffmpeg · Postiz · cron · Oracle Cloud Always Free

## Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | The agent's instructions: product, audience, formats, rules |
| `run.sh` | Daily entry point (cron), weekly review on Mondays, git backup |
| `make_slides.py` | Slideshow renderer |
| `record_app.py` | Scripted screen recording of the web app |
| `make_video.py` | Video assembly: captions, TTS, music |
| `setup.sh`, `setup_video.sh` | One-time VM setup |
| `state/` | Agent memory: post log, insights, app selector map |
