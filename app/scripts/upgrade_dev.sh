#!/bin/bash

. scripts/activate.sh

pip install -U pylint
pip install -U pytest
pip install -U coverage

pip freeze 2>/dev/null > requirements-dev.txt
