#!/bin/bash
# Daily run: the agent creates and publishes one post. Weekly review on Mondays.
set -u
export PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH
cd "$(dirname "$0")"
set -a; source ./.env; set +a
export POSTIZ_API_KEY
mkdir -p state out
touch state/log.md state/insights.md

TASK="Do today's daily run as described in CLAUDE.md."
[ "$(date +%u)" = "1" ] && TASK="First do the weekly review from CLAUDE.md, then today's daily run."

claude -p "$TASK" --dangerously-skip-permissions >> state/run.log 2>&1 || echo "$(date) run failed" >> state/errors.md

# alert by email if something broke (needs: apt install mailutils)
if [ -s state/errors.md ] && [ -n "${ALERT_EMAIL:-}" ]; then
  mail -s "Pulsify marketing: error" "$ALERT_EMAIL" < state/errors.md && mv state/errors.md "state/errors-$(date +%F).md"
fi

# keep only 14 days of rendered slides
find out -mindepth 1 -maxdepth 1 -type d -mtime +14 -exec rm -rf {} +

# back up rules + agent memory to GitHub (secrets/media are gitignored)
git add -A && git commit -qm "agent: $(date +%F)" && (gitleaks git --no-banner --log-level error . && git push -q origin main || echo "$(date) gitleaks or push failed, NOT pushed" >> state/errors.md) || true
