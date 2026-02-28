#!/bin/sh

# Automatically set wallpaper depending on the time of day.
# Dependencies: feh.
# To change wallpapers ewery hours crontab [0 * * * * export DISPLAY=:0; /usr/local/bin/auto-wallpaper.sh]

# Get the current hour in 24-hour format hour ( 0..23).
HOUR=$(date '+%H')

# Directories for different times of the day
WALLPAPERS_DESKTOP_DIR="$HOME/.wallpapers/desktop"
NIGHT_DIR="$WALLPAPERS_DESKTOP_DIR/night"
MORNING_DIR="$WALLPAPERS_DESKTOP_DIR/morning"
DAY_DIR="$WALLPAPERS_DESKTOP_DIR/day"
EVENING_DIR="$WALLPAPERS_DESKTOP_DIR/evening"

# feh options
FEH_OPTS="--no-menus --no-fehbg --bg-fill -recursive --randomize"

# Check if X server run.
if ! xset q &>/dev/null; then
    exit 1
fi

# Choose wallpaper based on the hour
case $HOUR in
    0[0-5])
        # Night 00-05
        feh $FEH_OPTS "$NIGHT_DIR"
        ;;
    0[6-9])
        # Morning 06-10
        feh $FEH_OPTS "$MORNING_DIR"
        ;;
    1[0-6])
        # Day 11-16
        feh $FEH_OPTS "$DAY_DIR"
        ;;
    1[7-9]|2[0-1])
        # Evening 17-21
        feh $FEH_OPTS "$EVENING_DIR"
        ;;
    2[2-3])
        # Night 22-23
        feh $FEH_OPTS "$NIGHT_DIR"
        ;;
esac
