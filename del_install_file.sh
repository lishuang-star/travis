#!/bin/bash

IF_DELETE_INSTALL_FILE=1

INSTALL_FILE="/var/www/html/install"

if [ ${IF_DELETE_INSTALL_FILE} == 1 ];
then
    sudo docker exec -it web-app /bin/sh -c 'rm -rf'${INSTALL_FILE}
    sudo docker exec -it encoder-app /bin/sh -c 'rm -rf'${INSTALL_FILE}
    echo "Delete finished!"
fi