#!/bin/bash

SLEEP_TIME=4
output=$(timeout $SLEEP_TIME cat /dev/input/mice)

if [[ -z "$output" ]]; then
    mouse=$(ls -1 /dev/input/by-id/*event-mouse | tail -1)
    echo "moved mouse"
    # evemu-event must be ran as sudo
    evemu-event $mouse --type EV_REL --code REL_X --value 1 --sync
    evemu-event $mouse --type EV_REL --code REL_X --value -1 --sync
else
    echo "No need to move mouse"
fi
