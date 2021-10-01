#!/bin/bash
OUT=$(tail -1 /opt/minecraft/server/logs/latest.log)
if [[ $OUT == *"joined the game"* ]]; then
  IP=$(curl https://g5rkignyck.execute-api.us-east-1.amazonaws.com)
  /opt/minecraft/tools/mcrcon/mcrcon -p admin "say $IP"
fi