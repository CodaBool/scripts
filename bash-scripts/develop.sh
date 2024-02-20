#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "\nENTERING DEVELOPER MODE\n"
printf "\n================ Initial Status  ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services

printf "\n================ Stopping All Services ===================\n"
printf "Disconnecting from VPN...\n"
protonvpn d
systemctl stop jackett sonarr radarr docker jellyfin apache2
snap disable nextcloud

printf "\n================ New Service Status  ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services

printf "\nSearching for qBittorrents using: ${GREEN}ps -ef | grep qbittorrent${NC}"
printf "\nkill using using: ${GREEN}sudo kill -9 [PID]${NC}\n"
ps -ef | egrep "qbittorrent|PID"

printf "\n================ Developer Mode Ready ===================\n\n"

