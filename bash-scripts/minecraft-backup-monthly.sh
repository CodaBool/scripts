#!/bin/bash
# ran using crontab every Month at 6am first day
# MONTH = full text of the current month
MONTH_YEAR=$(date +"%m-%Y")
echo $MONTH_YEAR
rm -rf /opt/minecraft/backups/world-$MONTH_YEAR
cp -r /opt/minecraft/server/world /opt/minecraft/backups/world-$MONTH_YEAR
/opt/minecraft/tools/mcrcon/mcrcon -p admin "say Making a monthly backup of the world -Doggie Corp."