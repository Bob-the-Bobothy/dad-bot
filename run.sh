#!/usr/bin/env bash

python -m venv .venv

chmod +x .venv/Scripts/activate
bash .venv/Scripts/activate

python3 -m pip install -r requirements.txt