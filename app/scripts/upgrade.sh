#!/bin/bash

python3 -m venv venv
. scripts/activate.sh

pip install --upgrade pip
pip install -U Flask
pip install -U flask-cors
pip install -U flask_swagger_ui

pip freeze 2>/dev/null > requirements.txt
