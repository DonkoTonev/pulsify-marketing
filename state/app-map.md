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
