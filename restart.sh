#!/bin/sh

source .venv/bin/activate
pm2 restart -s run
