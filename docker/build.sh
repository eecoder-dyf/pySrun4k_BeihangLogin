#!/usr/bin/env bash
#换源
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
apt-get update -y
apt-get install -y python3-pip

pip3 install -r /tmp/requirements.txt
