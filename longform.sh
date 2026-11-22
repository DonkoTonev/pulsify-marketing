#!/bin/bash
# Weekly long YouTube video (Bulgarian). Runs overnight, max 7 h, same backup as run.sh.
set -u
export PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH
cd "$(dirname "$0")"
exec 9>/tmp/pulsify-longform.lock; flock -n 9 || exit 0
mkdir -p state out
set -a; source ./.env; set +a
timeout 7h claude -p "Do the weekly long YouTube video described in CLAUDE.md." --dangerously-skip-permissions >> state/run.log 2>&1 || echo "$(date) longform run failed or timed out" >> state/errors.md
if [ -s state/errors.md ] && [ -n "${ALERT_EMAIL:-}" ]; then
  mail -s "Pulsify marketing: error" "$ALERT_EMAIL" < state/errors.md && mv state/errors.md "state/errors-$(date +%F)-longform.md"
fi
git add -A && git commit -qm "agent: $(date +%F) longform" && (gitleaks git --no-banner --log-level error . && git push -q origin main || echo "$(date) gitleaks or push failed, NOT pushed" >> state/errors.md) || true
