#!/bin/bash
if test -f "/home/codabool/scripts/alexa/resetSoon"; then
  if echo $(( `expr $(date +%s) - $(head lastRan)` > 9 )) | grep -q '1'; then
    rm "/home/codabool/scripts/alexa/resetSoon"
    /home/codabool/scripts/alexa/local.sh -d 'Echo Bed' -e speak:'default'
  fi
fi
