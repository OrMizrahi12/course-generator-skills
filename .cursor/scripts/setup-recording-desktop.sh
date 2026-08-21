#!/usr/bin/env bash
set -euo pipefail

# Course recording desktop: 1920x1080, no top panel, no bottom dock.
DISPLAY="${DISPLAY:-:1}"
export DISPLAY

wait_for_x() {
  local attempts=0
  while ! xdpyinfo -display "${DISPLAY}" >/dev/null 2>&1; do
    sleep 0.5
    attempts=$((attempts + 1))
    if [ "${attempts}" -ge 120 ]; then
      echo "Timed out waiting for X on ${DISPLAY}" >&2
      return 1
    fi
  done
}

wait_for_x

if xrandr --display "${DISPLAY}" | grep -q '1920x1080'; then
  xrandr --display "${DISPLAY}" --output VNC-0 --mode 1920x1080 2>/dev/null || true
fi

# Remove Cursor top panel (cursor-logo menu + clock).
pkill -x xfce4-panel 2>/dev/null || true
xfconf-query -c xfce4-panel -p /panels -r 2>/dev/null || true

# Stop Plank dock and its desktop-init respawn loop (keep noVNC alive).
pkill -x plank 2>/dev/null || true
main_init_pid="$(pgrep -f '^/bin/bash /usr/local/share/desktop-init\.sh$' | head -1 || true)"
if [ -n "${main_init_pid}" ]; then
  while read -r child_pid child_cmd; do
    if [[ "${child_cmd}" == *"/usr/local/share/desktop-init.sh"* ]]; then
      kill "${child_pid}" 2>/dev/null || true
    fi
  done < <(ps --ppid "${main_init_pid}" -o pid=,args= 2>/dev/null || true)
fi
pkill -x plank 2>/dev/null || true

echo "Recording desktop ready: $(xdpyinfo -display "${DISPLAY}" | awk '/dimensions/ {print $2}')"
