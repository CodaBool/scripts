filename=$(echo "update.$(($(date +%V) % 52)).log")
USERNAME=codabool
BACKUP_LOCATION=/home/$USERNAME/Documents/update_logs/flatpak_$filename
SSD=/dev/nvme2n1p3

function write_versions() {
  echo -e "\n========== Pre-Update Check Versions ==========\n" >> $BACKUP_LOCATION
  flatpak list >> $BACKUP_LOCATION
}

echo "running as $(whoami)" | tee -a  $BACKUP_LOCATION
echo "writing to log file '~/Documents/update_logs/flatpak_$filename' as $USERNAME"
echo $(date) > $BACKUP_LOCATION
write_versions

echo -e "\n========== Flatpak Available Updates ==========\n" | tee -a  $BACKUP_LOCATION

flatpak update --appstream >> $BACKUP_LOCATION

# find a way to get the number
# updates=$(flatpak update --no-deps | tee)
# update_count=$(echo "$updates" | grep -c "will be updated")
# echo "Number of Flatpak apps that can be updated: $update_count"

flatpak remote-ls --updates | tee -a $BACKUP_LOCATION

echo -e "\n========== Flatpak Update Check ==========\n" | tee -a  $BACKUP_LOCATION
flatpak update --assumeyes --noninteractive | tee -a  $BACKUP_LOCATION
notify-send "Flatpak" "all packages running latest" --app-name="Auto Flatpak Update"
# notify-send "All Flatpaks Updated" "updated N packages" --app-name="Auto Flatpak Update"
