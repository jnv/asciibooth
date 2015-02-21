#!/bin/sh

# Update && Upgrade
sudo apt-get update && sudo apt-get -y upgrade

# External deps
sudo apt-get -y install enscript mrxvt-mini xfonts-base xfonts-terminus

# Python3.2
sudo apt-get -y install python3-pip python3-picamera python3-dev libaa1

# Pillow dev deps
sudo apt-get -y install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev python3-tk

# Pip packages
pip-3.2 install -r requirements.txt --user
