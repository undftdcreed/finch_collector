#!/usr/bin/env bash

set -o errexit
pip install django
pip install dj_database_url
pip install psycopg2-binary
pip install whitenoise
python manage.py collectstatic --no-input
python manage.py migrate