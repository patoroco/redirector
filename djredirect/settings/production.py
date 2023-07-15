from .base import *  # noqa

DEBUG = False

STORAGE_DIR = "/app/storage/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(STORAGE_DIR, "db.sqlite3"),
    }
}

STATIC_ROOT = os.path.join(STORAGE_DIR, "staticfiles")

STATIC_URL = '/static/'
