#!/bin/bash -x

celery -A sportShop beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile /tmp/celerybeat.pid
