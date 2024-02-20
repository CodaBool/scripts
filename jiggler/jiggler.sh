#!/bin/bash

#### uncomment two lines below to help select your mouse event number ####
# grep -E 'Name|Handlers' /proc/bus/input/devices | grep -B1 'mouse'
# printf "\nFind your mouse's event number, it should be in this format 'eventX' where X is your event number\nWrite your event number into the script"
#### end of find mouse event number code ####

EVENT_NUMBER=24 # use above code to get your mouse event number
SLEEP_TIME=8
output=$(timeout $SLEEP_TIME evemu-record /dev/input/event$EVENT_NUMBER)

if ! grep -q "EV_REL / REL_Y" <<< "$output"; then
    mouse=$(ls -1 /dev/input/by-id/*event-mouse | tail -1)
    # evemu-event must be ran as sudo
    evemu-event $mouse --type EV_REL --code REL_X --value 1 --sync
    evemu-event $mouse --type EV_REL --code REL_X --value -1 --sync
fi
