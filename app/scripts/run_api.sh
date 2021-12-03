#!/bin/bash

. scripts/activate.sh
PYTHONPATH=./ FLASK_APP=api.py flask run --host=0.0.0.0
