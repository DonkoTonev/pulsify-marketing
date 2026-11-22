# Pulsify web app — selector map

App URL: https://apexfit-tracker.onrender.com/ (Render free tier — may cold-start,
so always `goto(..., wait_until="networkidle")` and expect the first load to be slow).
Viewport used for recording: 390x844, mobile, locale bg-BG.

## Login (`/login`)
The form fields carry **no `type`/`name`/`id` attributes** — only placeholders.
Match them by placeholder, never by `input[type=text]` (there is no such attribute).

- Username/email field: `input[placeholder*=mail i]` (placeholder "Enter username or email").
  Robust fallback: `input:not([type=password]):not([type=hidden]):not([type=checkbox]):not([type=radio])`.
- Password field: `input[type=password]` (placeholder "Enter password"). ← only field with a real type.
- Submit: `get_by_role("button", name="Sign In")`. Enter in the password field also submits.
- Other buttons on the page: two icon-only buttons (language globe, light/dark theme) with empty text,
  plus "Register" / "Forgot password?" links. Don't match the "Sign In" card heading as a button.
- Success check: after submit, URL leaves `/login`. (No welcome-tour "Skip"/"Пропусни" appeared on the
  test account, but the handler for it is kept.)

Credentials come from `.env` → `TEST_EMAIL`, `TEST_PASSWORD`.

## After login — main app (dashboard "Diary")
Bottom tab bar (text labels): `Diary`, `Workouts`, `Water`, `More`.
Dashboard shows: "Today vs. your targets" card (Calories / Protein / Carbohydrates / Fats),
"TDEE Calculator" card, and primary buttons **"Log a meal"** and **"Photo a meal"**.
Nav via `get_by_text("<label>")` / `click_text`.

> UI is in **English** on the test account regardless of `locale=bg-BG`. Use `click_text` with the
> English labels above. Re-verify labels with a screenshot before relying on new ones.

## Language switch (added 2026-11-22)
Header button `button[title="Language"]` toggles EN<->BG. It shows the language you'd switch TO:
label "BG" => UI is currently English (click to get Bulgarian); label "EN" => already Bulgarian.
It lives in the desktop sidebar header and is **outside the 390x844 mobile viewport**, so a normal
Playwright click fails ("element is outside of the viewport"). Click it via JS:
`pg.eval_on_selector("button[title=Language]", "e=>e.click()")`.
record_app.py now has a step for this: `{"do":"ensure_lang","lang":"bg"}` (or "en") — idempotent,
only clicks when the button offers the wanted language. The whole UI (nav, forms, results) localizes.
Theme toggle is a sibling `button.theme-toggle` ("Light theme"/"Светла тема") — don't confuse them.

## Upsell modal (added 2026-11-22)
After login (on /daily) a Pro upsell modal can appear ("See what Pro includes" / "Not now",
`button.upsell-close`, `.upsell-later`). It intercepts clicks. record_app.py step `{"do":"dismiss"}`
JS-clicks the close controls (no-op if absent). Navigating straight to /ai-meal usually avoids it.

## AI Meal Analysis — the photo-a-meal feature (added 2026-11-22)
Route: **/ai-meal** (sidebar "AI Meal Analysis" / "AI Анализ на ястие"). Flow:
1. Two hidden `input[type=file]` (accept=image/*). Upload directly: `input[type=file]` .first +
   set_input_files — no need to click "From Gallery"/"🖼️ От галерия". Buttons: "📷 Take Photo",
   "🖼️ From Gallery", "🎥 Live scan".
2. After a file is set, a form appears: dish name (optional, placeholder suggests "шопска салата"),
   "How was it prepared?" chips (air fryer/oven/pan/deep-fried/boiled/grill...), approx weight (optional),
   and an **"Анализирай"** / "Analyze" button. click_text "Анализирай" to run.
3. Analysis takes ~10-40s (real AI call on the test account). Wait for result with
   `{"do":"wait_for","text":"Разпознати храни","timeout":90000}` (EN: "Recognized foods").
4. Result renders below the photo: title (e.g. "🍲 Шопска салата"), description, "N храни ·
   Точност на оценката: висока (NN%)", big macro cards (ккал / Протеин / Въглех. / Мазнини), then a
   per-ingredient breakdown, "+ Добави съставка", "Запази в дневника". Scroll down to reveal macros.
   New step `{"do":"wait_for",...}` added to record_app.py for AI latency.
