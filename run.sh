#!/usr/bin/env bash

python3 -m venv .venv

chmod +x .venv/Scripts/activate
bash .venv/Scripts/activate

python3 -m pip install -r requirements.txt