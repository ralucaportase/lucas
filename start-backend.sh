#!/usr/bin/env bash

set -e

socket=$1

cd backend/lucas

gunicorn -b unix:$socket lucas.wsgi --log-file -
