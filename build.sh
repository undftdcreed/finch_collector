#!/usr/bin/env bash

set -o errexit
pip install django
pip install dj_database_url
pip install psycopg-2
python manage.py collectstatic --no-input
python manage.py migrate