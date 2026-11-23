# Insights (Monday reviews)

## 2026-11-23 (Mon) — first review, baseline only

Caveat up front: this reads **one day** of data. The accounts launched 2026-11-22 (Sun) and
TikTok/IG spread a new post over 24 h+. Per state/algorithm.md we do not judge a post in its first
hours, so these are **baselines to beat**, not conclusions. No experiments were active (research
has not run yet), so nothing to fold or drop.

### Numbers (as of 2026-11-23, ~1 day after the Nov 22 posts)
| Post | Channel | Type | Voice | Views | Likes | Comments | Shares | Saves |
|---|---|---|---|---|---|---|---|---|
| shopska morning | TikTok | app-integrated | Borislav | 588 | 4 | 0 | 0 | — |
| banitsa evening | TikTok | educational (guess-cal) | Kalina | 175 | 2 | 0 | 0 | — |
| shopska reel | Instagram | app-integrated | Borislav | 19 | 0 | 0 | — | 0 |
| shopska EN short | YouTube | app-integrated | none | 41 | 0 | 0 | — | — |
- TikTok platform total: 763 views, 7 likes, 0 comments, 0 shares. IG reach 17. All 6 posts PUBLISHED, no errors.

### What the data says (weakly — thin sample)
1. **TikTok is the discovery engine.** 763 views vs IG 19 vs YT 41 on day one. For a brand-new
   account with 0 followers, TikTok is where reach comes from; IG/YT need a follower base first and
   should be treated as long-build, not daily-reach channels.
2. **The claim-lead hook beat the soft-question hook.** shopska ("мислиш шопската е лека?",
   a belief-challenge) got 588 first-day views; banitsa ("Колко калории има тази баница?", a soft
   "Колко калории има в..." opener — on the 10.1 kill list) got 175. Confound: shopska had a ~7 h
   head start and the morning app push. But the direction matches doctrine, so **keep leading with a
   claim/conflict, not a soft question.** → recorded in hooks.md.
3. **Like-rate was higher on the evening video** (banitsa 1.14% vs shopska 0.68% of views). Weak,
   but the guess-the-calories game may engage per-view slightly better. Watch, don't act yet.
4. **Zero comments/shares/saves anywhere.** The comment-bait questions ("Познахте ли колко е?",
   "Ти колко позна?") have not converted on day one. Could be pure earliness (few viewers, no
   follower base to comment) or a weak CTA-to-comment. **Watch next week**; if still zero at real
   view counts, make the comment prompt more concrete (ask for a specific guess/number).

### Open comparisons we cannot judge yet
- **Voice vs no-voice:** both TikToks had voice; only YT-EN was voiceless (different platform +
  language + tiny sample). No valid comparison. → to compare, alternate voice/no-voice **within
  TikTok** over the coming weeks and watch completion.
- **Morning vs evening:** only one of each, and they differ in format, dish and head-start. Not an
  A/B. Need several weeks.
- **Quality-gate scores vs results:** both videos scored hook 8+/avg 7+; both got modest day-one
  reach. Can't correlate to retention yet.

### Tooling limitation (important for future reviews)
`postiz analytics:post` exposes only **views / likes / comments / shares** (+ reach/saves on IG).
It does **not** expose 2-second retention, average watch time or completion. So the quality gate's
retention claims can't be validated against real retention through this API. For real retention we'd
need TikTok/IG native analytics (manual). Until then, judge with views + engagement + follower
growth and treat retention as a design assumption, not a measured number.

### To watch next Monday (2026-11-30)
- Do the day-1 numbers above grow over the week (TikTok spreads slowly)? Record 7-day totals.
- First comments/shares/saves/follows — which format earns them.
- Follower count on each channel (not in the API dump; check natively if possible).
