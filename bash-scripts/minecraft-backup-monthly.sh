#!/bin/bash
# ran using crontab every Month at 6am first day
# MONTH = full text of the current month
SOMETHING=$(LC_ALL=C date +%B + %Y)
YEAR=date +"%Y"
echo $SOMETHING
echo $YEAR
cmd_output=$(date +"%B + % Y")
echo $cmd_output

# rm -rf /opt/minecraft/backups/world-$MONTH
# cp -r /opt/minecraft/server/world /opt/minecraft/backups/world-$MONTH
# /opt/minecraft/tools/mcrcon/mcrcon -p admin "say Making a monthly backup of the world -Doggie Corp."