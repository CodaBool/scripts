#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "= ${RED}work${NC} | ${GREEN}personal${NC} =\n"
printf "===================\n"
printf "1. ${RED}vpn${NC}\n"
printf "2. ${RED}google${NC}\n"
printf "3. ${RED}aws${NC}\n"
printf "4. ${RED}divvy${NC}\n"
printf "5. ${RED}slack${NC}\n"
printf "6. ${RED}akamai${NC}\n"
printf "7. ${GREEN}facebook${NC}\n"
printf "8. ${GREEN}bitwarden${NC}\n"
printf "9. ${GREEN}stripe${NC}\n"
printf "10. ${GREEN}aws${NC}\n"
printf "11. ${GREEN}npm${NC}\n"
printf "12. ${GREEN}aws${NC}\n"

printf "Enter a number to generate an otp for an issuer: "
read input

if [[ $input == 1 ]]; then 
  oathtool -b --totp SECRET_HERE
elif [[ $input == 2 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 3 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 4 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 5 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 6 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 7 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 8 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 9 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 10 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 11 ]]; then
  oathtool -b --totp SECRET_HERE
elif [[ $input == 12 ]]; then
  oathtool -b --totp SECRET_HERE
else
  echo "You did not enter a number from 1 - 12"
fi