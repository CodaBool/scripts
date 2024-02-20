#!/bin/bash
# ran using crontab every Monday at 6am
# keeps the last 2 weeks (2 backups total) backed up
# DOW = 1-7, 1 is Monday
DOW=$(date +%u)
rm -rf /home/steam/.config/unity3d/IronGate/Valheim/backups/worlds-$DOW
cp -r /home/steam/.config/unity3d/IronGate/Valheim/worlds /home/steam/.config/unity3d/IronGate/Valheim/backups/worlds-$DOW