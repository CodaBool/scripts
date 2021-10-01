#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ "$( docker container inspect -f '{{.State.Status}}' photoprism )" == "running" ]; then
printf "photoprism: ${GREEN}Running${NC}\n"
else
  printf "photoprism: ${RED}Stopped${NC}\n"
fi