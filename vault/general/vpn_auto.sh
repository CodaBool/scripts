#!/bin/bash
source /home/codabool/.env
DOMAINS="artifactory.cms.gov ci.backends.cms.gov splunk.aws.healthcare.gov cloudtamer.cms.gov hsls-dev-615990403.us-east-1.elb.amazonaws.com hsls-dev-20230828192557641300000001.c0ca9s9jmfmr.us-east-1.rds.amazonaws.com checkip.amazonaws.com splunk.cloud.cms.gov internal.artifactory.backends.cms.gov status.healthcare.gov"
printf '%s\n%s\n' $EUA_PASSWORD $(oathtool -b --totp $TOTP_SECRET) | sudo openconnect -u $EUA_USERNAME --passwd-on-stdin --pfs -s "vpn-slice $DOMAINS" cloudvpn.cms.gov
