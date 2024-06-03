#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "= ${GREEN}AWS${NC} =\n"
printf "===================\n"
printf "1. ${GREEN}ezapp${NC}\n"
printf "2. ${GREEN}flh${NC}\n"
printf "3. ${GREEN}pwss${NC}\n"
printf "4. ${GREEN}ecws${NC}\n"

printf "Enter a number pick a AWS account to sign into: "
read input

if [[ $input == 1 ]]; then 
  xdg-open "https://signin.aws.amazon.com/switchrole?roleName=aws-crossacct-ezapp-mgmt&account=aws-hhs-cms-ezapp&displayName=MYYG"
elif [[ $input == 2 ]]; then
  xdg-open "https://signin.aws.amazon.com/switchrole?roleName=aws-crossacct-flh-poweruser&account=aws-hhs-cms-flh-v3&displayName=MYYG"
elif [[ $input == 3 ]]; then
  xdg-open "https://signin.aws.amazon.com/switchrole?roleName=aws-crossacct-geoapi-poweruser&account=aws-hhs-cms-pwss&displayName=MYYG"
elif [[ $input == 4 ]]; then
  xdg-open "https://signin.aws.amazon.com/switchrole?roleName=aws-crossacct-ecws-v3-poweruser&account=aws-hhs-cms-ecws-v3&displayName=MYYG"
else
  echo "You did not enter a number from 1 - 4"
fi

TOTP=$(oathtool -b --totp 'SECRET_HERE')
printf "\nTOTP = $TOTP\n"