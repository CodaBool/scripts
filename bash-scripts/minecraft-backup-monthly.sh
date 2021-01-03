#!/bin/bash
# ran using crontab every Month at 6am first day
# MONTH = full text of the current month
MONTH_YEAR=$(date +"%B + %Y")
echo $MONTH_YEAR

# rm -rf /opt/minecraft/backups/world-$MONTH
# cp -r /opt/minecraft/server/world /opt/minecraft/backups/world-$MONTH
# /opt/minecraft/tools/mcrcon/mcrcon -p admin "say Making a monthly backup of the world -Doggie Corp."