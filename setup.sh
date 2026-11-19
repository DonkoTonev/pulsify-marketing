#!/bin/bash
# One-time setup on the VM. Usage: bash setup.sh <POSTIZ_API_KEY>
set -e
cd "$(dirname "$0")"
KEY="${1:?Usage: bash setup.sh <POSTIZ_API_KEY>}"

printf 'POSTIZ_API_KEY=%s\nALERT_EMAIL=donkotonew@gmail.com\n' "$KEY" > .env
chmod 600 .env

pip install --quiet --break-system-packages pillow 2>/dev/null || pip install --quiet pillow
command -v postiz >/dev/null || npm install -g postiz

# real app screenshots from the Play Store listing
mkdir -p assets/screens
i=0
while read -r url; do
  curl -sL "$url" -o "assets/screens/$(printf %02d $i).png"; i=$((i+1))
done < screens.txt

chmod +x run.sh
# daily at 18:37 Sofia time (good evening slot for TikTok/IG in BG/EU)
( crontab -l 2>/dev/null | grep -v pulsify-marketing/run.sh ; echo "CRON_TZ=Europe/Sofia
37 18 * * * $PWD/run.sh" ) | crontab -

POSTIZ_API_KEY="$KEY" postiz integrations:list && echo "✅ Готово. Първият пост тръгва днес в 18:37. Тест веднага: ./run.sh"
