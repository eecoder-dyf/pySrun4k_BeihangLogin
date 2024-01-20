#!/usr/bin/env bash
# #换源
apt-get update -y
apt-get install -y python3-pip

pip3 install -r /tmp/requirements.txt
