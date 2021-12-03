#!/bin/bash

python3 -m venv venv
. scripts/activate.sh

pip install --upgrade pip
pip install -r requirements-dev.txt
