#!/bin/bash
# Weekly research (Sundays): looks for new app-marketing tactics on the web.
# Sandboxed: no shell, cannot post, can only write state/research.md and state/experiments.md.
set -u
export PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH
cd "$(dirname "$0")"
mkdir -p state
touch state/research.md state/experiments.md
claude -p "Do the weekly research described in the 'Self-improvement' section of CLAUDE.md." \
  --allowedTools "WebSearch,WebFetch,Read,Edit(state/research.md),Edit(state/experiments.md),Edit(state/algorithm.md)" \
  --disallowedTools "Bash" \
  >> state/research.log 2>&1 || echo "$(date) research failed" >> state/errors.md
