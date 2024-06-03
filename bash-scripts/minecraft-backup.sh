#!/bin/bash
# ran using crontab every Monday at 6am
# keeps the last 2 weeks (2 backups total) backed up
# DOW = 1-7, 1 is Monday
DOW=$(date +%u)
rm -rf /opt/minecraft/backups/world-$DOW
# mv /opt/minecraft/backups/current-world /opt/minecraft/backups/old-world
cp -r /opt/minecraft/server/world /opt/minecraft/backups/world-$DOW
/opt/minecraft/tools/mcrcon/mcrcon -p admin "say Making a daily backup of the world -Doggie Corp."