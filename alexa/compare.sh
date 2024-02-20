#!/bin/bash
if test -f "/home/codabool/scripts/alexa/resetSoon"; then
  if echo $(( `expr $(date +%s) - $(head /home/codabool/scripts/alexa/lastRan)` > 4 )) | grep -q '1'; then
    rm "/home/codabool/scripts/alexa/resetSoon"
    /home/codabool/scripts/alexa/local.sh -d 'Echo Office' -e automation:'reset'
  fi
fi
