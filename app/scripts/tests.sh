#!/bin/bash

. scripts/activate.sh

cd ..
. .env
PYTHONPATH=$PYTHONPATH pytest -vvv --junitxml=tests/pytest.junit.xml
