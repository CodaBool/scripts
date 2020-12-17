#!/bin/bash

# ===== Working way to speak on server =====
# IP=$(curl https://g5rkignyck.execute-api.us-east-1.amazonaws.com)
# echo "$IP"
# /opt/minecraft/tools/mcrcon/mcrcon -p admin "say $IP"

# get filename
# echo -n "Enter File Name : "
# read fileName

# # make sure file exits for reading
# if [ ! -f $fileName ]; then
#   echo "Filename $fileName does not exists"
#   exit 1
# fi

# display last five lines of the file using tail command
OUT=$(tail -5 /opt/minecraft/server/logs/latest.log)
echo "output =" $OUT