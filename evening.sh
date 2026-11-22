#!/bin/bash
# Evening run: one extra TikTok post. Same setup and backup as run.sh.
set -u
export PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH
cd "$(dirname "$0")"
exec 9>/tmp/pulsify-evening.lock; flock -n 9 || exit 0
mkdir -p state out
if pgrep -f "daily run as described" >/dev/null; then echo "$(date) evening skipped: morning run still going" >> state/errors.md; exit 0; fi
set -a; source ./.env; set +a
claude -p "Do the evening TikTok run described in CLAUDE.md." --dangerously-skip-permissions >> state/run.log 2>&1 || echo "$(date) evening run failed" >> state/errors.md
if [ -s state/errors.md ] && [ -n "${ALERT_EMAIL:-}" ]; then
  mail -s "Pulsify marketing: error" "$ALERT_EMAIL" < state/errors.md && mv state/errors.md "state/errors-$(date +%F)-evening.md"
fi
git add -A && git commit -qm "agent: $(date +%F) evening" && (gitleaks git --no-banner --log-level error . && git push -q origin main || echo "$(date) gitleaks or push failed, NOT pushed" >> state/errors.md) || true
