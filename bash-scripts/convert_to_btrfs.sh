#!/bin/bash

# add subvolumes to active folders

[[ "$(id -u)" -eq 0 ]] || (echo "Got root?" ; exit 5)
command -v btrfs > /dev/null || (echo "Command not found: btrfs" ; exit 4)
for folder in $* ; do
  echo "creating subvolume for $folder"
  mount | awk '{print $3}' | grep "$(pwd)/${folder}" && echo "${folder} has a submount?" && exit 1
  btrfs sub list . | grep "${PWD##*/}/${folder}" && echo "${folder} has a subvolume?" && exit 2
  [ -e ${folder}.temp ] && echo "${folder}.temp already exists?" && exit 3 || true
  mv ${folder} ${folder}.temp
  btrfs sub create ${folder}
  USER=$(stat -c '%U' ${folder}.temp)
  GROUP=$(stat -c '%G' ${folder}.temp)
  chown ${USER}.${GROUP} ${folder}
  cp -a --reflink=always ${folder}.temp/. ${folder}/
  echo "Delete ${folder}.temp/ if happy with ${folder}/"
done
