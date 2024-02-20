# Todo
- add to log if transcode takes very little time
- create script that checks if video files are small
- make logs append and only be cleared every week
- add test if there is a 'shipment in progress file in p4a Documents'

# Working
- p4a dock
- win dock
- pi8 dock (unfinished)

# SCP
scp -r ./shows codabool@192.168.0.207:/mnt/sd1/raw/
scp -r * codabool@192.168.0.25:/media/book/new

python /d/Utilities/codadash-scripts/win-manage-docks.py

script will transcode anything that is placed in the /c/Transcode/pull folder
There is a required .ready file to be at the root of whatever is being transferred.
Final transcodes are scp into /media/book/new 

_____________________________________________________________________________________

# HandBrakeCLI
-q (quality float ; use 1-30)
--subtitle-burned none

_____________________________________________________________________________________

# Database
#### create tables
CREATE TABLE p4a (
  "Space Left"      text,
  "Completed"       text,
  "Downloading"     text,
  "Transferring"    text,
  "VPN Status"      text,
  "QBit Status"     text,
  "Last Ran"        timestamp
);
CREATE TABLE p8a (
  "Space Left"       text,
  "Last Ran"         timestamp
);
CREATE TABLE mom (
  "Space Left Internal"    text,
  "Space Left External"    text,
  "Videos"                 text,
  "Last Ran"               timestamp
);

#### add dummy row to initialize
INSERT INTO p4a ("Space Left", "Completed", "Downloading", "Transferring", "VPN Status", "QBit Status", "Last Ran") VALUES ('5', '5', '5', '5', '5', '5', CURRENT_TIMESTAMP);
INSERT INTO p8a ("Space Left", "Last Ran") VALUES ('5', CURRENT_TIMESTAMP);
INSERT INTO mom ("Space Left Internal", "Space Left External", "Videos", "Last Ran") VALUES ('5', '5', '5', CURRENT_TIMESTAMP);

#### update in code
UPDATE p4a SET "Space Left"={space}, Completed"={complete}, "Downloading"={download}, "Transferring"={ready}, "VPN Status"={status}, "Last Ran"=CURRENT_TIMESTAMP;
UPDATE pi8 SET "Space Left"={space}, "New Videos"={new}, "Last Ran"=\'{lastRan}\'  WHERE id=1;
UPDATE win SET "Transcoding"={transcoding}, "Transferring"={transferring}, "Waiting"={waiting}, "Last Ran"=\'{lastRan}\' WHERE id=1;

#### drop tables
drop table p4a;
drop table p8a;
drop table win;
drop table mom;

_____________________________________________________________________________________

# Bashrc
## p4a /etc/bash.bashrc
alias pi="ssh codabool@192.168.0.207"
function m() {
  scp -r "$PWD" codabool@192.168.0.207:/mnt/sd1/raw/
}

## pi8 /etc/bash.bashrc
alias umnt="sudo umount /mnt/sd1"
alias mnt="sudo mount -o rw,users,uid=1000,umask=0001 /dev/sda1 /mnt/sd1"
alias p4a="ssh codabool@192.168.1.16"

# win ~/.bashrc
alias transcode-all="python /d/utilities/codadash-scripts/tran-win.py ./ y n 24"
alias p4a="ssh codabool@192.168.0.244"
alias p4a-get="sftp codabool@192.168.0.244:/home/codabool/Downloads/qbit/complete"
alias pi8="ssh codabool@192.168.0.207"
alias transcode-docks="python /d/utilities/codadash-scripts/manage-docks-windows.py"
alias count-type="python /d/utilities/codadash-scripts/count-simple.py ./ True"
alias count="python /d/utilities/codadash-scripts/read-all-windows.py ./ True"
tran() {
  # arguments: directory, logs, automated, quality, extra
  if [ $# -eq 0 ]
    then
      echo "Provide Logs [y/n] Quality [1-30] and Extra Parameters"
  fi
  python /d/utilities/codadash-scripts/tran-win.py ./ " $1" n " $2" " $3"
}

# Task Scheduler
"C:\Program Files (x86)\cmdow\bin\Release\cmdow.exe"
/run /hid "C:\Program Files (x86)\Python38-32\python.exe" C:\Transcode\codadash-scripts\db-win.py


# Alexa Commands

89.9 (wuvf jazz)= s23356
91.5 (wprk state of the scene college radio) = s22034
89.9 (wucf hd2 latin jazz) = s67214
90.7 (all things considered) = s30977 
90.7 (classical) = s109553

pause/stop
vol [1-10]
speak
alexa
- alexa -d 'Echo Bed' -e pause/play -r spotify
- alexa -d 'Echo Bed' -e vol:10
- alexa -d 'Echo Bed' -e speak:'a'
- alexa -d 'Echo Bed' -r [radioId]
- alexa -e automation:'TV'
- alexa -a (get a list of all device names)

auto
- DB fifty
- DB sixty
- DB seventy
- TV
- sleep
- bye
- sony
- speaker

# Bashrc pi8
alias otp="oathtool --base32 --totp \"[MFA_SECRET_HERE]\""
alexa() {
  ~/Documents/alexa-remote-control/alexa_remote_control.sh "$@"
}

# Bashrc windows git-bash terminal
alias jazz="ssh -t codabool@192.168.0.207 \"~/Documents/alexa-remote-control/alexa_remote_control.sh -d 'Echo Bed' -r s23356\""
alias play="ssh -t codabool@192.168.0.207 \"~/Documents/alexa-remote-control/alexa_remote_control.sh -d 'Echo Bed' -e play\""
alias pause="ssh -t codabool@192.168.0.207 \"~/Documents/alexa-remote-control/alexa_remote_control.sh -d 'Echo Bed' -e pause\""
alias stop="ssh -t codabool@192.168.0.207 \"~/Documents/alexa-remote-control/alexa_remote_control.sh -d 'Echo Bed' -e pause\""
alexa() {
  ssh -t codabool@192.168.0.207 "~/Documents/alexa-remote-control/alexa_remote_control.sh" $@
}
auto() {
  args=$@
  alexa -d 'Echo\ Bed' -e automation:"${args// /\\ }"
}
speak() {
  args=$@
  ssh -t codabool@192.168.0.207 "~/Documents/alexa-remote-control/alexa_remote_control.sh" -d 'Echo\ Bed' -e speak:"${args// /\\ }"
}
vol() {
  alexa -d 'Echo\ Bed' -e vol:$1
}

# Installation
cp ./alexa/template.sh ./alexa/local.sh
sudo apt-get install jq
sudo apt install oathtool
oathtool --base32 --totp "[MFA_SECRET_HERE]" 
chmod +x ./alexa/local.sh

[github](https://github.com/thorsten-gehrig/alexa-remote-control)

repo test 3
