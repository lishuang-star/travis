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

apt-get update && apt-get install -y \
  curl \
  python3 \
  python3-pip 

pip3 install -r requirements_config.txt

bash wait-for-it.sh mysql:3306 -- echo 1 
bash wait-for-it.sh youphptube:8888 -- echo 2
bash wait-for-it.sh youphptube-encoder:8889 -- echo 3

# # Install 
curl -i -s -k  -X $'POST' \
    --data-binary $'webSiteRootURL=http%3A%2F%2F192.168.1.3%3A8888%2F&systemRootPath=%2Fvar%2Fwww%2Fhtml%2F&webSiteTitle=YouPHPTube&databaseHost=mysql&databasePort=3306&databaseUser=root&databasePass=password&databaseName=youPHPTube&mainLanguage=en&systemAdminPass=cuccs123&contactEmail=894597649%40qq.com&createTables=2' \
    $'http://192.168.1.3:8888/install/checkConfiguration.php'

curl -i -s -k  -X $'POST' \
    --data-binary $'user=admin&pass=cuccs123&siteURL=http%3A%2F%2F192.168.1.3%3A8888%2F' \
    $'http://192.168.1.3:8888//login'

curl -i -s -k  -X $'POST' \
    --data-binary $'webSiteRootURL=http%3A%2F%2F192.168.1.3%3A8889%2F&systemRootPath=%2Fvar%2Fwww%2Fhtml%2F&databaseHost=mysql&databaseUser=root&databasePass=password&databaseName=youPHPTube-Encoder&createTables=2&siteURL=http%3A%2F%2F192.168.1.3%3A8888%2F&inputUser=admin&inputPassword=cuccs123&allowedStreamers=http%3A%2F%2F192.168.1.3%3A8888%2F&defaultPriority=1' \
    $'http://192.168.1.3:8889/install/checkConfiguration.php'

python3 datafill.py