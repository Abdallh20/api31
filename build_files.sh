#!/usr/bin/env bash
pip install -r requirements.txt
python3.x manage.py makemigrations
python3.x manage.py migrate
python3.x manage.py collectstatic --no-input --clear