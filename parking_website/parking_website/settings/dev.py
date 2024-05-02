from .base import *

SECRET_KEY = "django-insecure-az!u=wrd1&ulls7#s613_%5m(0@3(*!7gp4k%g*v%uj(8r_wja"

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"

DATA_SERVER_URL = 'http://localhost'

