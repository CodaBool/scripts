#!/bin/bash

# $thingy = curl

IP=$(curl https://g5rkignyck.execute-api.us-east-1.amazonaws.com)
echo "IP = $IP"
# sed "s/IP/$IP/" nsupdate.txt | nsupdate
# echo "sed =" $sed
echo "/opt/minecraft/tools/mcrcon/mcrcon -p admin \"say $IP\""

/opt/minecraft/tools/mcrcon/mcrcon -p admin "say $IP"
