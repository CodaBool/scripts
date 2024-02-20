#!/bin/bash

# Define print colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "\n========================================================\n\n"
systemctl is-active Jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active Radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active qbittorrent >/dev/null 2>&1 && printf "Qbittorrent: ${GREEN}Running${NC}\n" || printf "Qbittorrent ${RED}Stopped${NC}\n"
#PROCESS_NUM=$(ps -ef | grep "qbittorrent" | grep -v "grep" | wc -l)
#if [ $PROCESS_NUM -gt 0 ]; then
#  printf "Qbittorrent: ${GREEN}Running${NC}\n"
#else
#  printf "Qbittorrent: ${RED}Stopped${NC}\n"
#fi
printf "\nChecking VPN...\n\n"
protonvpn status

printf "\n================ ...Happy Torrenting ===================\n\n"

