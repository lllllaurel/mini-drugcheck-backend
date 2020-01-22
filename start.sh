#!/bin/sh

virtualenv-3 .venv
source .venv/bin/activate
pip3 install flask
pip3 install opencv-python
pm2 start -s --name=run run.py
