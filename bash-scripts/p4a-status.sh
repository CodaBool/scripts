#!/bin/bash
pro=$(protonvpn status)
# reset contents
> '/home/codabool/scripts/bash-scripts/status.txt'
for word in $pro
do
    printf "$word\n" >> '/home/codabool/scripts/bash-scripts/status.txt'
done
sys=$(systemctl is-active qbittorrent)
echo $sys >> '/home/codabool/scripts/bash-scripts/status.txt'