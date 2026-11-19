#!/bin/bash
# One-time: video tools on the 1 GB VM. Usage: bash setup_video.sh
set -e
cd "$(dirname "$0")"
# 1 GB RAM is not enough for Chrome + ffmpeg → add 4 GB swap
if ! swapon --show | grep -q swapfile; then
  sudo fallocate -l 4G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile >/dev/null && sudo swapon /swapfile
  echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab >/dev/null
fi
sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg fonts-dejavu-core >/dev/null
pip install --quiet --break-system-packages playwright edge-tts pillow 2>/dev/null || pip install --quiet playwright edge-tts pillow
python3 -m playwright install --with-deps chromium >/dev/null
mkdir -p assets/food assets/music
grep -q '^TEST_EMAIL=' .env || echo "⚠️  Добави TEST_EMAIL и TEST_PASSWORD в .env (виж инструкциите в чата)"
python3 -c "import edge_tts, playwright; print('✅ Видео инструментите са готови')"
