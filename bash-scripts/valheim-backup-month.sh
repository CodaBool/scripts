#!/bin/bash
# ran using crontab every Month at 6am first day
# MONTH = full text of the current month
MONTH_YEAR=$(date +"%m-%Y")
echo $MONTH_YEAR
rm -rf /home/steam/.config/unity3d/IronGate/Valheim/backups/worlds-$MONTH_YEAR
cp -r /home/steam/.config/unity3d/IronGate/Valheim/worlds /home/steam/.config/unity3d/IronGate/Valheim/backups/worlds-$MONTH_YEAR