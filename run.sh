#!/bin/sh

python3 dad-bot/main.py &
python3 vndb-quotes/main.py &

wait
