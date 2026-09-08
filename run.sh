#!/usr/bin/env bash

source ".venv/bin/activate"

cd dad-bot
python3 main.py & 

cd ../vndb-quotes
python3 main.py &
