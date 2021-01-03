#!/bin/bash
# ran using crontab every Monday at 6am
# keeps the last 2 weeks (2 backups total) backed up
rm -rf /opt/minecraft/backups/old-world
mv /opt/minecraft/backups/current-world /opt/minecraft/backups/old-world
cp -r /opt/minecraft/server/world /opt/minecraft/backups/current-world
/opt/minecraft/tools/mcrcon/mcrcon -p admin "say making a backup of the world -Doggie"