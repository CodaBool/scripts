#!/bin/bash

source /home/codabool/.env
DOMAINS="artifactory.cms.gov ci.backends.cms.gov splunk.aws.healthcare.gov cloudtamer.cms.gov"

echo $EUA_PASSWORD
echo $TOTP_SECRET
# "s3-website-us-east-1.amazonaws.com"
# "cloudbeesjenkins.cms.gov"

if [ "$1" = "full" ]; then
  printf '%s\n%s\n' $EUA_PASSWORD $(oathtool -b --totp $TOTP_SECRET) | sudo openconnect -b -u $EUA_USERNAME --passwd-on-stdin --pfs cloudvpn.cms.gov
  printf "\n👀 all traffic through VPN"
elif [ "$1" = "disconnect" ]; then
  echo "🔌 disconnected"
  sudo pkill -SIGINT openconnect
elif [ "$1" = "split" ]; then
  printf '%s\n%s\n' $EUA_PASSWORD $(oathtool -b --totp $TOTP_SECRET) | sudo openconnect -u $EUA_USERNAME --passwd-on-stdin --pfs -s "vpn-slice $DOMAINS" cloudvpn.cms.gov
fi
