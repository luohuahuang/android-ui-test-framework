#!/usr/bin/env bash

# run with a & if you have two devices for dev and master respectively
# sh ./client-pre-dev--connects--server-develop.sh &
sh ./client-pre-dev--connects--server-develop.sh
sh ./client-dev--connects--server-master.sh
sh ./client-pre-dev--connects--server-master.sh



