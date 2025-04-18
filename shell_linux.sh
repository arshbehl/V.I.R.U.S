#!/bin/sh
feh --bg-fill "<image_path>" &
xtrlock -b -f &
zenity --info --text="Press OK to unlock" --title=Timer &
sleep 10
killall xtrlock; killall feh
zenity --info --text "System unlocked." --title "Timer"
