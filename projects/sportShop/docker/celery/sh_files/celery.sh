#!/bin/bash -x

celery -A sportShop worker -l info
