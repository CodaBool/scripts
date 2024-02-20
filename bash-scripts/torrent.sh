#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "\nENTERING TORRENT MODE\n"
printf "\n================ Initial Status  ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services

printf "\n================ Stopping Uneeded Services  ===================\n"
systemctl stop docker jellyfin apache2
snap disable nextcloud

printf "\n================ Starting Torrent Services ====================="
printf "\nStarting VPN using tcp"
sudo protonvpn init # will require user confirmation
sudo protonvpn c US-FL#19 -p tcp
sudo protonvpn status
systemctl start jackett sonarr radarr

printf "\n================ New Service Status ===================\n"
systemctl is-active jackett >/dev/null 2>&1 && printf "Jackett: ${GREEN}Running${NC}\n" || printf "Jackett: ${RED}Stopped${NC}\n"
systemctl is-active sonarr >/dev/null 2>&1 && printf "Sonarr: ${GREEN}Running${NC}\n" || printf "Sonarr: ${RED}Stopped${NC}\n"
systemctl is-active radarr >/dev/null 2>&1 && printf "Radarr: ${GREEN}Running${NC}\n" || printf "Radarr: ${RED}Stopped${NC}\n"
systemctl is-active docker >/dev/null 2>&1 && printf "Docker: ${GREEN}Running${NC}\n" || printf "Docker: ${RED}Stopped${NC}\n"
systemctl is-active jellyfin >/dev/null 2>&1 && printf "Jellyfin: ${GREEN}Running${NC}\n" || printf "Jellyfin: ${RED}Stopped${NC}\n"
systemctl is-active apache2 >/dev/null 2>&1 && printf "Apache: ${GREEN}Running${NC}\n" || printf "Apache: ${RED}Stopped${NC}\n"
snap services

printf "\nStart a headless qBittorrent with 'nohup qbittorrent&'"
printf "\n7878 -> Movies | 8989 -> Shows\n"
printf "\n${RED}WARNING${NC}: If there is no killswitch enable it with ${GREEN}sudo protonvpn configure${NC}, then 5 2\n"
printf "\n================ ...Happy Torrenting ===================\n\n"

