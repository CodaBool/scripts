#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "\n====================================================\n\n"
systemctl is-active nginx >/dev/null 2>&1 && printf "Nginx: ${GREEN}Running${NC}\n" || printf "Nginx: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active minecraft >/dev/null 2>&1 && printf "Minecraft: ${GREEN}Running${NC}\n" || printf "Minecraft: ${RED}Stopped${NC}\n"
if [ "$( docker container inspect -f '{{.State.Status}}' bitwarden )" == "running" ]; then
printf "bitwarden: ${GREEN}Running${NC}\n"
else
  printf "bitwarden: ${RED}Stopped${NC}\n"
fi

if [ "$( docker container inspect -f '{{.State.Status}}' jellyfin )" == "running" ]; then
printf "jellyfin: ${GREEN}Running${NC}\n"
else
  printf "jellyfin: ${RED}Stopped${NC}\n"
fi

if [ "$( docker container inspect -f '{{.State.Status}}' npm_app_1 )" == "running" ]; then
printf "npm_app_1: ${GREEN}Running${NC}\n"
else
  printf "npm_app_1: ${RED}Stopped${NC}\n"
fi

if [ "$( docker container inspect -f '{{.State.Status}}' npm_db_1 )" == "running" ]; then
printf "npm_db_1: ${GREEN}Running${NC}\n"
else
  printf "npm_db_1: ${RED}Stopped${NC}\n"
fi
echo
snap services



# printf "\n================ Starting Normal Services ===================\n"
# systemctl start docker jellyfin apache2
# snap enable nextcloud

# printf "\n================ New Service Status  ===================\n"
# systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
# systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
# systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
# systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
# systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
# systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
# snap services
# docker container ls 

printf "\n====================================================\n\n"

