#!/usr/bin/env bash

python3 -m venv .venv

chmod +x ./.venv/Scripts/activate
./.venv/Scripts/activate

python3 -m pip install -r requirements.txt

cd dad-bot
python3 main.py &

cd ../vndb-quotes
python3 main.py &
