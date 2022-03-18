#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "= Pick a git account =\n"
printf "===================\n"
printf "1. ${RED}school${NC}\n"
printf "2. ${GREEN}personal${NC}\n"
printf "3. ${RED}work${NC}\n"

printf "Enter a number to pick an git account: "
read input

if [[ $input == 1 ]]; then
elif [[ $input == 2 ]]; then
elif [[ $input == 3 ]]; then
else
  echo "You did not enter a number from 1 - 3"
fi