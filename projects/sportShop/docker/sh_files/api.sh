#!/bin/bash -x

python manage.py makemigrations &&
python manage.py migrate &&
gunicorn sportShop.wsgi:application --bind 0.0.0.0:"$APP_PORT"
