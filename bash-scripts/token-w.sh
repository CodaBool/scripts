#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "= ${RED}work${NC} | ${GREEN}personal${NC} =\n"
printf "===================\n"
printf "1. ${RED}MYYG${NC}\n"
printf "2. ${RED}VPN${NC}\n"
printf "3. ${RED}AWS IAM user${NC}\n"
printf "4. ${GREEN}CodaBool${NC}\n"
printf "Enter a number to generate an token for an account: "
read input

if [[ $input == 1 ]]; then
  echo '' | clip.exe
elif [[ $input == 2 ]]; then
  echo '' | clip.exe
elif [[ $input == 3 ]]; then
  echo '' | clip.exe
  # Print clipboard
  powershell.exe Get-Clipboard
elif [[ $input == 4 ]]; then
  echo '' | clip.exe
else
  echo "You did not enter a number from 1 - 4"
fi

if [ $input -lt 5 ]; then
  echo "Copied to clipboard!"
fi
