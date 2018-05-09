sudo apt install vim -y
sudo apt install python3-pip -y
sudo apt install git -y
sudo apt install python-matplotlib -y
sudo apt install python-pip -y
sudo apt-get install manpages-pl manpages-fr-extra -y

pip3 install -r ./basic.txt
git clone https://github.com/ArduPilot/ardupilot.git

#~/ardupilot/Tools/scripts/install-prereqs-ubuntu.sh -y
#. ~/.profile
#./waf configure --board px4-v3
#./waf copter
