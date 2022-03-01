#!/usr/bin/bash

PYTHON_VERSION=3.9.10
sudo apt update -y
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev zlib1g-dev

cd /usr/src
sudo wget http://python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz --no-check-certificate
sudo tar xf Python-${PYTHON_VERSION}.tar.xz
cd Python-${PYTHON_VERSION}
./configure --enable-optimizations
sudo make altinstall