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

# Bashrc
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
