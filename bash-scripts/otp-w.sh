#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "= ${RED}work${NC} | ${GREEN}personal${NC} =\n"
printf "===================\n"
printf "1. ${RED}vpn${NC}\n"
printf "2. ${RED}cms${NC}\n"
printf "3. ${RED}aws${NC}\n"
printf "4. ${RED}divvy${NC}\n"
printf "5. ${RED}slack${NC}\n"
printf "6. ${RED}akamai${NC}\n"
printf "7. ${RED}OneLogin${NC}\n"
printf "8. ${RED}Google${NC}\n"
printf "9. ${RED}CMS enterprise${NC}\n"
printf "10. ${GREEN}facebook${NC}\n"
printf "11. ${GREEN}bitwarden${NC}\n"
printf "12. ${GREEN}stripe${NC}\n"
printf "13. ${GREEN}aws${NC}\n"
printf "14. ${GREEN}npm${NC}\n"
printf "15. ${GREEN}alexa${NC}\n"
printf "16. ${GREEN}npm codabool${NC}\n"
printf "17. ${GREEN}nintendo${NC}\n"
printf "18. ${GREEN}paypal${NC}\n"
printf "19. ${GREEN}mint${NC}\n"

printf "Enter a number to generate an otp for an issuer: "
read input

if [[ $input == 1 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 2 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 3 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 4 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 5 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 6 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 7 ]]; then
  # can use custom sso https://onelogin.service-now.com/support?id=kb_article&sys_id=17195b07db1e9f0024c780c74b96192d
  oathtool -b --totp '' | clip.exe
elif [[ $input == 8 ]]; then
   oathtool -b --totp '' | clip.exe
elif [[ $input == 9 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 10 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 11 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 12 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 13 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 14 ]]; then
  oathtool -b --totp '' | clip.exe
elif [[ $input == 15 ]]; then
  oathtool --base32 --totp "" | clip.exe
elif [[ $input == 16 ]]; then
  oathtool -b --totp "" | clip.exe
elif [[ $input == 17 ]]; then
  oathtool -b --totp "" | clip.exe
elif [[ $input == 18 ]]; then
  oathtool -b --totp "" | clip.exe
elif [[ $input == 19 ]]; then
  oathtool -b --totp "" | clip.exe
else
  echo "You did not enter a number from 1 - 19"
fi

if [ $input -lt 20 ]; then
  powershell.exe Get-Clipboard
  echo "Copied to clipboard!"
fi
