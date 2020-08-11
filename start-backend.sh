#!/usr/bin/env bash

set -e

socket=$1

cd backend/lucas

python manage.py collectstatic --no-input

gunicorn -b unix:$socket lucas.wsgi --log-file -
