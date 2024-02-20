#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "\nENTERING SERVICE MODE\n"
printf "\n================ Initial Status  ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services

printf "\n================ Stopping Torrenting Services ===================\n"
printf "Disconnecting from VPN...\n"
protonvpn d
systemctl stop jackett sonarr radarr

printf "${RED}ERROR${NC}: systemctl nonfunctional for radarr"
printf "\ncan be found using ${GREEN}ps -ef | grep cli${NC}\n"
printf "\n================ Starting Normal Services ===================\n"
systemctl start docker jellyfin apache2
snap enable nextcloud

printf "\n================ New Service Status  ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services
docker container ls 

printf "\n================ All services Online  ===================\n\n"

