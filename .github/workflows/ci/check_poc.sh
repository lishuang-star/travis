#!/bin/bash

exp_log=$(sudo docker-compose logs poc)
echo "$exp_log"
[[ $exp_log =~ "PoC success!" ]] || exit 1