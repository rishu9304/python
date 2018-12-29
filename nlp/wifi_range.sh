#!/bin/bash

# Make sure your system is up to date !!!
printf "\n\n[+] Updating the system ...\n\n"
apt update -y && apt upgrade -y && apt dist-upgrade -y

# install the headers module [ IMPORTANT ] !!!
printf "\n\n[+] Installing linux headers ...\n\n"
apt-cache search linux-headers-4.*
apt install -y linux-headers-"`uname -r`"

# Grab the firmware files
printf "\n\n[+] Downloading files ...\n\n"
cd /opt
git clone https://github.com/lwfinger/rtlwifi_new
chmod +x rtlwifi_new/** 
cd rtlwifi_new

# Installing...
printf "\n\n[+] Installing firmware ...\n\n"
make && make install
depmod -a
modprobe -rv rtl8723be
modprobe -v rtl8723be ant_sel=2
ip link set wlan0 up
echo "options rtl8723be ant_sel=2" | sudo tee /etc/modprobe.d/50-rtl8723be.conf