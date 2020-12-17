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
example = "[02:33:24] [Server thread/INFO]: CodaBool joined the game"
OUT=$(tail -1 /opt/minecraft/server/logs/latest.log)
if [[ $example == *"joined the game"* ]]; then
  echo "It's there!"
else
  echo "oh poo it's not there"
fi

#echo "output =" $OUT