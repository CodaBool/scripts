BLACK="\033[1;30m"
RED="\033[1;31m"
ORANGE="\033[1;33m"
GREEN="\033[1;32m"
PURPLE="\033[1;35m"
RED_BG="\033[41m"
ORANGE_BG="\033[43m"
GREEN_BG="\033[42m"
BLACK_BG="\033[40m"
PURPLE_BG="\033[45m"
RESET="\033[0m"

writeLog () {
  log=$(echo "$1" | cut -d' ' -f3-)
  ts=$(echo "$line" | head -c 32)

  # only print logs that are json
  if [ $(echo "$log" | head -c 1) = "{" ]
  then
    message=$(echo "${log}" | jq -r .message)
    level=$(echo "${log}" | jq -r .level)
    func=$(echo "${log}" | jq -r .func)

    # zerolog will put errors under the error field
    # and omit message field
    if [ "$message" = "null" ]
    then
      message=$(echo "${log}" | jq -r .error)
    fi

    # time ago
    now=$(date +%s)
    TSseconds=$(date -d "$ts" +%s)
    AgeSeconds=$(( now - $TSseconds ))
    AgeDays=$(( $AgeSeconds / (60 * 60 * 24) ))
    AgeHours=$(( $AgeSeconds / (60 * 60) ))
    AgeMinutes=$(( $AgeSeconds / 60 ))
    timePrint="${AgeDays}d"

    # less than 24 hours
    if [ "$AgeDays" -eq "0" ]; then 
      timePrint="${AgeHours}h"
    fi
    # less than 60 minutes
    if [ "$AgeHours" -eq "0" ]; then 
      timePrint="${AgeMinutes}m"
    fi
    # Add a space of padding to the 2 character timePrint
    if [ "${#timePrint}" -eq "2" ]; then
      timePrint=" ${timePrint}"
    fi

    color=$RESET
    if [ "$level" = "panic" ] || [ "$level" = "fatal" ] || [ "$level" = "error" ]
    then
      color=${RED_BG}
    elif [ "$level" = "warn" ]
    then
      color=${ORANGE_BG}
    elif [ "$level" = "info" ]
    then
      color=${GREEN_BG}
    elif [ "$level" = "debug" ]
    then
      color=${BLACK_BG}
    elif [ "$level" = "trace" ]
    then
      color=${PURPLE_BG}
    fi
    printf "${BLACK}%s${RESET} ${color} ${RESET} ${RESET}%s${RESET}" "${timePrint}" "${message}"
    if [ -z "$func" ]
    then
      printf "\n"
    else
      printf " ${BLACK_BG}%s${RESET}\n" "${func}"
    fi
  fi
}

filter=""
if [ "$#" -eq 3 ]; then
  filter='{ $.level = "error"  || $.level = "fatal" || $.level = "panic" }'
fi

aws logs tail /aws/$1 --since $2 --filter-pattern "$filter" |  while read -r line
do
  writeLog "$line"
done

while true
do
  aws logs tail /aws/$1 --since 21s |  while read -r line
  do
    writeLog "$line"
  done
	sleep 5
  # 18s sleep 4 also works well
done
