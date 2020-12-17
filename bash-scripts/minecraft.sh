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
# example="[02:33:24] [Server thread/INFO]: CodaBool joined the game"
OUT=$(tail -1 /opt/minecraft/server/logs/latest.log)
if [[ $OUT == *"joined the game"* ]]; then
  IP=$(curl https://g5rkignyck.execute-api.us-east-1.amazonaws.com)
  echo "Someone has entered! using quote "$IP
  /opt/minecraft/tools/mcrcon/mcrcon -p admin "say $IP"
  touch /home/codabool/yes-findy
else
  echo "oh poo I don't see anyone"
  touch /home/codabool/no-findy
fi

#echo "output =" $OUT
# str="Learn-to-Split-a-String-in-Bash-Scripting"
# IFS='-' # hyphen (-) is set as delimiter
# read -ra ADDR <<< "$str" # str is read into an array as tokens separated by IFS
# for i in "${ADDR[@]}"; do # access each element of array
#     echo "$i"
# done
# IFS=' ' # reset to default value after usage