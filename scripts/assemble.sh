#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -hide_banner -loglevel error -y -framerate 24 -start_number 1 -i 'output/frame_%04d.png' -i 'audio/MASTER_MIX.wav' -map 0:v:0 -map 1:a:0 -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium -c:a aac -b:a 192k -t 24 -movflags +faststart 'output/RUDENKO_AI_VIDEO_rebuilt.mp4'
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 'output/RUDENKO_AI_VIDEO_rebuilt.mp4'
