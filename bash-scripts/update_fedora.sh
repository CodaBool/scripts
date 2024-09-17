#!/bin/bash

# An auto update script for Fedora
# this is an opinionated script which runs weekly and writes logs

# this script makes a few assumptions
#   - using flatpaks
#   - using GNOME
#   - using btrfs
#   - using Nvidia

# to assist with reading the output of the important logs I have the below bash function
# which I use to read the relevant part for actionable items
# it can be ran w/o an argument to view this weeks output
# or ran with a week number to see what the output was for that week

# alternatively a script is written to Desktop which does runs the same bash function

# update_logs() {
#   file=${1:-$(date +%V)}
#   echo "last update happened at:"
#   head -n 1 /home/codabool/Documents/update_logs/update.$file.log
#   awk '/========== General ==========/ {flag=1} /========== update complete, printing new versions ==========/{flag=0} flag' "/home/codabool/Documents/update_logs/update.$file.log" | less -R
# }

# records versions before and after updating

# this will keep a running log of the last 52 weeks
# this means it will keep a year's worth of updates

filename=$(echo "update.$(($(date +%V) % 52)).log")
USERNAME=codabool
BACKUP_LOCATION=/home/$USERNAME/Documents/update_logs/$filename
SSD=/dev/nvme2n1p3

if [ ! -d "/home/$USERNAME/Documents/update_logs" ]; then
  echo "need to create a update_logs folder in ~/Documents/update_logs..."
  sudo -u $USERNAME mkdir -p /home/$USERNAME/Documents/update_logs
fi


function write_versions() {
  # write packages and their description
  # https://superuser.com/questions/1523973/archlinux-pacman-list-installed-packages-with-description?newreg=828a1d0f69b542a88afc8f1a2a35dddc
  echo -e "\nPackages\n" >> $BACKUP_LOCATION
  dnf repoquery --userinstalled >> $BACKUP_LOCATION

  echo -e "\nkernal = $(uname -r)" >> $BACKUP_LOCATION

  echo -e "\ngnome = $(gnome-shell --version)\n" >> $BACKUP_LOCATION

  systemctl --version | head -n 1 >> $BACKUP_LOCATION

  echo -e "\nnvidia = $(dnf info kmod-nvidia | grep Version | awk '{print $3}')\n" >> $BACKUP_LOCATION
}

echo "running as $(whoami)" | tee -a  $BACKUP_LOCATION
echo "writing to log file '~/Documents/update_logs/$filename' as $USERNAME"
sudo -u $USERNAME echo $(date) > $BACKUP_LOCATION

echo -e "\n====== Pre-update ======" >> $BACKUP_LOCATION

write_versions
echo -e "\n========== Available Package Updates ==========\n" >> $BACKUP_LOCATION
echo -e "\n$(dnf list updates)\n" >> $BACKUP_LOCATION

echo -e "\n========== General ==========\n" >> $BACKUP_LOCATION

echo "disk usage $(df -h / | awk 'NR==2 {print $5}')" >> $BACKUP_LOCATION
#echo -e "scheduled snapshots\n"  >> $BACKUP_LOCATION
#snapper list -t single >> $BACKUP_LOCATION
echo -e "\nSSD write lifespan usage\n$(smartctl -a $SSD | grep 'Percentage Used')\n" >> $BACKUP_LOCATION

echo -e "\n========== Update Packages ==========\n" | tee -a  $BACKUP_LOCATION

# for automatic updates this requires allowing the defined user to run pacman without password
# this is an unsafe practice and opens your system up for malicious actors
# never do this on any system where you do not trust 100% of the code running on it
#   to perform this edit (replace codabool with your username)
#     sudo su
#     EDITOR=nano visudo
#     # can use hostnamectl to find the hostname, for me its "pom"
#     codabool pom=(ALL:ALL) NOPASSWD: /usr/bin/dnf

# TODO: get the number of updates this will perform, should be able to use "check-update"
# dnf check-update| grep -Ec ' updates$'
dnf upgrade --refresh --assumeyes | tee -a $BACKUP_LOCATION


echo -e "\n========== update complete, printing new versions ==========\n" >> $BACKUP_LOCATION
write_versions

echo -e "\n========== Update Complete ==========\n" | tee -a $BACKUP_LOCATION

sudo -u $USERNAME DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus notify-send "Packages" "all packages running latest" --app-name="Auto DNF Update"
# TODO: find the number of packages that get updated


# I use systemd timer to perform this
# here is the .service file
  # [Unit]
  # Description=Update DNF
  # After=network-online.target
  # Wants=network-online.target

  # [Service]
  # Type=oneshot
  # ExecStart=/bin/bash /home/codabool/code/scripts/bash-scripts/update_flatpak.sh

  # [Install]
  # WantedBy=default.target

# and here is the .timer file
  # [Unit]
  # Description=Update DNF daily
  # Wants=network-online.target

  # [Timer]
  # OnCalendar=weekly
  # Persistent=true

  # [Install]
  # WantedBy=timers.target

# systemctl --user enable --now update-user-flatpaks.timer
# sudo systemctl enable --now dnf.timer
# guide https://www.jwillikers.com/automate-flatpak-updates-with-systemd
