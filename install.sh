#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
    echo 'Please run as root.'
    exit 1
fi

sudo apt-get install -y tor macchanger secure-delete git-all python3 python3-all python3-dev python3-pip
sudo pip3 install requests bs4 datetime termcolor

git clone https://github.com/BlackArch/torctl
cd torctl
sudo mv service/* /etc/systemd/system
sudo mv bash-completion/torctl /usr/share/bash-completion/completions/torctl
sed -i 's/start_service iptables//' torctl
sed -i 's/TOR_UID="tor"/TOR_UID="debian-tor"/' torctl
sudo mv torctl /usr/bin/torctl
cd .. && rm -r torctl

touch .installed.txt
echo "Don't delete this file." >.installed.txt

clear
echo 'Anonymous Dark Web Tool Installed Successfuly.'
echo 'Run sudo python3 adwt.py'
