import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def set_db(is_docker: bool):

    if is_docker is True:

        return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'sportshop_postgres',
            'USER': 'postgres',
            'PASSWORD': 'mohsen1160417237',
            'HOST': '86.104.32.99',
            'port': 5432
        }

    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
