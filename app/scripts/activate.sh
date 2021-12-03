#!/bin/bash

if [ -f venv/bin/activate ]; then
    . venv/bin/activate

elif [ -f venv/Scripts/activate ]; then
	. venv/Scripts/activate

else
	echo No Python Virtual Env found
	exit 127

fi
