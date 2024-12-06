#!/usr/bin/env bash
python3.9 -m pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --no-input --clear