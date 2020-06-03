#!/usr/bin/env bash

cd backend/lucas

gunicorn lucas.wsgi --log-file -
