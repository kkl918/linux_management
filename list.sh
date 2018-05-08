sudo apt-get install vim -y
sudo apt-get install python3-pip -y
sudo apt-get install git -y
sudo apt-get install python-matplotlib -y
sudo apt install python-pip -y

#　Pymavlink

sudo apt-get install libxml2-dev libxslt-dev python-dev
sudo pip2 install -U future lxml
sudo pip2 install -U pymavlink

# gcc -------------------------------------

pushd .
cd ~
wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-rm/7-2017q4/gcc-arm-none-eabi-7-2017-q4-major-linux.tar.bz2
tar -jxf gcc-arm-none-eabi-7-2017-q4-major-linux.tar.bz2
exportline="export PATH=$HOME/gcc-arm-none-eabi-7-2017-q4-major/bin:\$PATH"
if grep -Fxq "$exportline" ~/.profile; then echo nothing to do ; else echo $exportline >> ~/.profile; fi
popd

# end -------------------------------------
