#!/bin/bash

# Change the source.list
cp /etc/apt/sources.list /etc/apt/sources.list.bak
cat >sources.list <<EOL
deb http://mirrors.163.com/debian/ jessie main non-free contrib
deb http://mirrors.163.com/debian-archive/debian/ jessie-backports main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib
deb-src http://mirrors.163.com/debian-archive/debian/ jessie-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
EOL
cp sources.list /etc/apt/sources.list
rm sources.list

# Install basic softwares
apt -o Acquire::Check-Valid-Until=false update #更新源

apt install python3.8 -y
apt install python3-pip -y

pip3 install -r requirements_poc.txt

chmod 777 poc.py
echo 'ready to run poc'

bash wait-for-it.sh config -- echo 1 

## injection
python3 poc.py
echo 'poc done'